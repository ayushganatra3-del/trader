"""Paper portfolio ("sleeve") accounting in GBP.

Each sleeve starts with its own virtual capital and moves toward target
weights at the latest completed bar's close, paying the configured cost per
side. Risk overlays: a daily loss limit (flatten and pause until the next UTC
day) and a kill switch (flatten and stop for good after a large drawdown).
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .config import RiskConfig

EPS = 1e-9


@dataclass
class Quote:
    symbol: str
    price: float  # quote currency
    fx: float  # multiply to convert to GBP
    cost: float  # fraction of notional per side
    tradable: bool

    @property
    def gbp(self) -> float:
        return self.price * self.fx


def new_sleeve(name: str, capital: float, now_iso: str) -> dict:
    return {"name": name, "created_at": now_iso, "capital_gbp": capital, "cash_gbp": capital,
            "positions": {}, "realised_gbp": 0.0, "fees_gbp": 0.0, "closed_trades": 0, "wins": 0,
            "losses": 0, "gross_win_gbp": 0.0, "gross_loss_gbp": 0.0, "peak_equity_gbp": capital,
            "max_drawdown_pct": 0.0, "day": None, "day_start_equity_gbp": capital, "halted_day": None,
            "disabled": False, "disabled_reason": None, "equity_gbp": capital, "last_marks": {}}


class Sleeve:
    def __init__(self, data: dict):
        self.data = data

    @property
    def name(self) -> str:
        return self.data["name"]

    def equity(self, quotes: dict[str, Quote]) -> float:
        value = self.data["cash_gbp"]
        marks = self.data["last_marks"]
        for symbol, position in self.data["positions"].items():
            quote = quotes.get(symbol)
            price = quote.gbp if quote else marks.get(symbol, position["cost_gbp"] / max(position["units"], EPS))
            value += position["units"] * price
        return value

    def mark(self, quotes: dict[str, Quote]) -> float:
        for symbol in self.data["positions"]:
            if symbol in quotes:
                self.data["last_marks"][symbol] = quotes[symbol].gbp
        equity = self.equity(quotes)
        self.data["equity_gbp"] = equity
        self.data["peak_equity_gbp"] = max(self.data["peak_equity_gbp"], equity)
        drawdown = equity / self.data["peak_equity_gbp"] - 1
        self.data["max_drawdown_pct"] = min(self.data["max_drawdown_pct"], round(drawdown * 100, 3))
        return equity

    # ------------------------------------------------------------ trading
    def _buy(self, quote: Quote, notional: float, now_iso: str, reason: str) -> dict:
        exec_price = quote.gbp * (1 + quote.cost)
        units = notional / exec_price
        fee = notional - units * quote.gbp
        position = self.data["positions"].setdefault(
            quote.symbol, {"units": 0.0, "cost_gbp": 0.0, "opened_at": now_iso, "entry_price": quote.price, "realised_gbp": 0.0})
        position["units"] += units
        position["cost_gbp"] += notional
        self.data["cash_gbp"] -= notional
        self.data["fees_gbp"] += fee
        return {"t": now_iso, "sleeve": self.name, "symbol": quote.symbol, "side": "buy", "units": units,
                "price": quote.price, "value_gbp": notional, "fee_gbp": fee, "pnl_gbp": None, "reason": reason}

    def _sell(self, quote: Quote, units: float, now_iso: str, reason: str) -> dict:
        position = self.data["positions"][quote.symbol]
        units = min(units, position["units"])
        gross = units * quote.gbp
        fee = gross * quote.cost
        proceeds = gross - fee
        fraction = units / position["units"] if position["units"] > EPS else 1.0
        basis = position["cost_gbp"] * fraction
        pnl = proceeds - basis
        position["units"] -= units
        position["cost_gbp"] -= basis
        position["realised_gbp"] += pnl
        self.data["cash_gbp"] += proceeds
        self.data["fees_gbp"] += fee
        self.data["realised_gbp"] += pnl
        closed = position["units"] <= EPS or position["units"] * quote.gbp < 0.01
        if closed:
            total = position["realised_gbp"]
            self.data["closed_trades"] += 1
            if total > 0:
                self.data["wins"] += 1
                self.data["gross_win_gbp"] += total
                self.data["loss_streak"] = 0
            else:
                self.data["losses"] += 1
                self.data["gross_loss_gbp"] += -total
                self.data["loss_streak"] = self.data.get("loss_streak", 0) + 1
            if position["units"] > EPS:  # dust
                self.data["cash_gbp"] += position["units"] * quote.gbp
            del self.data["positions"][quote.symbol]
            self.data["last_marks"].pop(quote.symbol, None)
        return {"t": now_iso, "sleeve": self.name, "symbol": quote.symbol, "side": "sell", "units": units,
                "price": quote.price, "value_gbp": proceeds, "fee_gbp": fee, "pnl_gbp": pnl, "reason": reason,
                "closed": closed}

    def rebalance(self, targets: dict[str, float], quotes: dict[str, Quote], risk: RiskConfig,
                  now_iso: str, today: str, reason_for=lambda symbol, side: "") -> list[dict]:
        data = self.data
        equity = self.mark(quotes)
        if data["day"] != today:
            data["day"] = today
            data["day_start_equity_gbp"] = equity
        halt_reason = None
        if not data["disabled"] and equity <= data["peak_equity_gbp"] * (1 - risk.kill_drawdown):
            data["disabled"] = True
            data["disabled_reason"] = f"Kill switch: down {risk.kill_drawdown:.0%} from peak"
        if data["disabled"]:
            halt_reason = data["disabled_reason"]
        elif data["halted_day"] == today or equity <= data["day_start_equity_gbp"] * (1 - risk.daily_loss_limit):
            if data["halted_day"] != today:
                data["halted_day"] = today
            halt_reason = f"Daily loss limit ({risk.daily_loss_limit:.0%}) hit; paused until tomorrow (UTC)"
        else:
            halt_reason = self._period_halt(risk, equity, today)
        now = pd.Timestamp(now_iso)
        cooling = bool(data.get("cooldown_until")) and now < pd.Timestamp(data["cooldown_until"])

        trades = []
        sells, buys = [], []
        for symbol in sorted(set(targets) | set(data["positions"])):
            quote = quotes.get(symbol)
            if quote is None or not quote.tradable:
                continue
            weight = 0.0 if halt_reason else max(0.0, targets.get(symbol, 0.0))
            held_units = data["positions"].get(symbol, {}).get("units", 0.0)
            current = held_units * quote.gbp
            target = weight * equity
            if weight <= EPS:
                if held_units > EPS:
                    sells.append((quote, held_units, halt_reason or reason_for(symbol, "sell") or "target is flat"))
                continue
            diff = target - current
            if current <= EPS:
                if diff >= risk.min_trade_gbp:
                    buys.append((quote, diff, reason_for(symbol, "buy") or "entry"))
            elif abs(diff) >= risk.rebalance_band * equity and abs(diff) >= risk.min_trade_gbp:
                if diff > 0:
                    buys.append((quote, diff, "rebalance up"))
                else:
                    sells.append((quote, -diff / quote.gbp, "rebalance down"))
        for quote, units, why in sells:
            trades.append(self._sell(quote, units, now_iso, why))
        for quote, notional, why in ([] if cooling else buys):
            notional = min(notional, data["cash_gbp"])
            if notional >= risk.min_trade_gbp:
                trades.append(self._buy(quote, notional, now_iso, why))
        if risk.loss_streak_cooldown and data.get("loss_streak", 0) >= risk.loss_streak_cooldown:
            data["cooldown_until"] = (now + pd.Timedelta(hours=risk.cooldown_hours)).isoformat()
            data["loss_streak"] = 0
        if not halt_reason and data.get("cooldown_until") and now < pd.Timestamp(data["cooldown_until"]):
            halt_reason = f"{risk.loss_streak_cooldown} losing trades in a row: no new buys until {data['cooldown_until'][:16]}"
        data["halt_reason"] = halt_reason
        self.mark(quotes)
        return trades

    def _period_halt(self, risk: RiskConfig, equity: float, today: str) -> str | None:
        """Week-to-date and month-to-date loss limits (off unless configured)."""
        data = self.data
        day = pd.Timestamp(today)
        week = f"{day.isocalendar().year}-W{day.isocalendar().week:02d}"
        month = today[:7]
        if data.get("week") != week:
            data["week"], data["week_start_equity_gbp"] = week, equity
        if data.get("month") != month:
            data["month"], data["month_start_equity_gbp"] = month, equity
        if risk.weekly_loss_limit and equity <= data["week_start_equity_gbp"] * (1 - risk.weekly_loss_limit):
            return f"Weekly loss limit ({risk.weekly_loss_limit:.0%}) hit; paused until next week"
        if risk.monthly_loss_limit and equity <= data["month_start_equity_gbp"] * (1 - risk.monthly_loss_limit):
            return f"Monthly loss limit ({risk.monthly_loss_limit:.0%}) hit; paused until next month"
        return None

    def weights(self) -> dict[str, float]:
        """Current holdings as fractions of equity (what a broker account should mirror)."""
        equity = self.data["equity_gbp"]
        if equity <= 0:
            return {}
        marks = self.data["last_marks"]
        return {s: p["units"] * marks.get(s, 0.0) / equity for s, p in self.data["positions"].items()}

    def summary(self) -> dict:
        data = self.data
        capital = data["capital_gbp"]
        closed = data["closed_trades"]
        return {
            "equity_gbp": round(data["equity_gbp"], 4),
            "return_pct": round((data["equity_gbp"] / capital - 1) * 100, 3),
            "cash_gbp": round(data["cash_gbp"], 4),
            "realised_gbp": round(data["realised_gbp"], 4),
            "fees_gbp": round(data["fees_gbp"], 4),
            "closed_trades": closed,
            "win_rate_pct": round(100 * data["wins"] / closed, 1) if closed else None,
            "profit_factor": round(data["gross_win_gbp"] / data["gross_loss_gbp"], 2) if data["gross_loss_gbp"] > 0 else None,
            "max_drawdown_pct": data["max_drawdown_pct"],
            "halted": bool(data.get("halt_reason")),
            "halt_reason": data.get("halt_reason"),
            "disabled": data["disabled"],
            "positions": [
                {"symbol": symbol, "units": round(p["units"], 8), "cost_gbp": round(p["cost_gbp"], 4),
                 "value_gbp": round(p["units"] * data["last_marks"].get(symbol, 0.0), 4),
                 "pnl_gbp": round(p["units"] * data["last_marks"].get(symbol, 0.0) - p["cost_gbp"], 4),
                 "opened_at": p["opened_at"], "entry_price": p["entry_price"]}
                for symbol, p in sorted(data["positions"].items())],
        }
