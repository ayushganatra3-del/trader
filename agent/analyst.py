"""AI analyst sleeve: a TradingAgents-style research desk run by Claude.

Once per US trading day, after the close, Claude gets the daily numbers for
the stock universe plus the market regime, searches the web for news, argues
the bull and bear case, and picks a portfolio for the next session. The pick
takes effect at the next US open and is traded like the other daily sleeves.

It only runs forward: a model cannot be backtested honestly on dates it may
already know about, so its record starts the day it is switched on.
It is off unless the ANTHROPIC_API_KEY secret is set (cost: roughly $0.50-1
per trading day with the defaults).
"""
from __future__ import annotations

import json
import logging
import os

import numpy as np
import pandas as pd

from .config import Config
from .copytrade import CopyBook, _next_open_utc
from .daily import bullish_score

log = logging.getLogger(__name__)

BOOK = "AI analyst (Claude)"

SYSTEM = """You run a small trading desk modelled on a research firm: technical, news/sentiment and macro \
analysts report, a bull and a bear researcher debate, a trader proposes a portfolio and a risk manager signs it off. \
You manage a £100 long-only paper account that can only buy the symbols listed. Positions are opened at the next US \
open and reviewed after every close, so the horizon is roughly one to five sessions. Cash is a valid position. \
Transaction costs are about 0.05% per side. Be concrete and sceptical; prefer no trade to a weak one."""


def _num(value, digits=2):
    return None if value is None or not np.isfinite(value) else round(float(value), digits)


def snapshot(daily: dict[str, pd.DataFrame], symbols: list[str]) -> list[dict]:
    """Compact daily numbers per symbol (all computed from completed bars)."""
    rows = []
    for symbol in symbols:
        bars = daily.get(symbol)
        if bars is None or len(bars) < 60:
            continue
        close = bars["close"]
        delta = close.diff()
        gain = delta.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
        loss = (-delta.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
        rsi = 100 - 100 / (1 + gain.iloc[-1] / loss.iloc[-1]) if loss.iloc[-1] > 0 else 100.0
        change = lambda n: _num(100 * (close.iloc[-1] / close.iloc[-1 - n] - 1)) if len(close) > n else None  # noqa: E731
        sma = lambda n: _num(100 * (close.iloc[-1] / close.tail(n).mean() - 1)) if len(close) >= n else None  # noqa: E731
        rows.append({"symbol": symbol, "close": _num(close.iloc[-1]), "chg_1d_pct": change(1), "chg_5d_pct": change(5),
                     "chg_20d_pct": change(20), "chg_60d_pct": change(60), "vs_sma50_pct": sma(50),
                     "vs_sma200_pct": sma(200), "rsi14": _num(rsi, 1),
                     "vol_20d_pct": _num(100 * close.pct_change().tail(20).std() * np.sqrt(252), 1),
                     "volume_vs_20d": _num(bars["volume"].iloc[-1] / bars["volume"].tail(20).mean()),
                     "bullish_score": _num(bullish_score(bars).iloc[-1])})
    return rows


def decision_schema(symbols: list[str]) -> dict:
    return {
        "type": "object",
        "properties": {
            "market_view": {"type": "string"},
            "positions": {"type": "array", "items": {
                "type": "object",
                "properties": {"symbol": {"type": "string", "enum": symbols},
                               "weight": {"type": "number"},
                               "reason": {"type": "string"}},
                "required": ["symbol", "weight", "reason"],
                "additionalProperties": False}},
        },
        "required": ["market_view", "positions"],
        "additionalProperties": False,
    }


def clean_positions(positions: list[dict], symbols: list[str], max_positions: int, cap: float) -> dict[str, float]:
    """Keep known symbols, cap each weight, keep the largest few, total <= 100%."""
    weights: dict[str, float] = {}
    for row in positions or []:
        symbol = row.get("symbol")
        try:
            weight = float(row.get("weight") or 0)
        except (TypeError, ValueError):
            continue
        if weight > 1.0:  # the model answered in percent
            weight /= 100
        if symbol in symbols and weight > 0:
            weights[symbol] = min(cap, weights.get(symbol, 0.0) + weight)
    weights = dict(sorted(weights.items(), key=lambda kv: -kv[1])[:max_positions])
    total = sum(weights.values())
    if total > 1.0:
        weights = {s: w / total for s, w in weights.items()}
    return {s: round(w, 4) for s, w in weights.items()}


class Analyst:
    """Calls Claude once per session. ``client`` is an ``anthropic.Anthropic``
    (a fake in tests)."""

    def __init__(self, config: Config, client=None):
        self.config = config
        self.cfg = config.ai
        self._client = client

    @staticmethod
    def available() -> bool:
        return bool(os.environ.get("ANTHROPIC_API_KEY"))

    @property
    def client(self):
        if self._client is None:
            import anthropic

            self._client = anthropic.Anthropic(timeout=300.0, max_retries=2)
        return self._client

    # ------------------------------------------------------------ calls
    def research(self, prompt: str) -> str:
        """Web-searching analysis with the bull/bear debate; returns its text."""
        messages = [{"role": "user", "content": prompt}]
        response = None
        for _ in range(4):  # the server pauses long web-search turns; resume a few times
            response = self.client.beta.messages.create(
                model=self.cfg.model, max_tokens=16000, system=SYSTEM,
                thinking={"type": "adaptive"}, output_config={"effort": self.cfg.effort},
                tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": self.cfg.max_searches}],
                betas=["server-side-fallback-2026-07-01"], fallbacks="default",
                messages=messages)
            if response.stop_reason != "pause_turn":
                break
            messages = [messages[0], {"role": "assistant", "content": response.content}]
        if response.stop_reason == "refusal":
            raise RuntimeError("the model declined to analyse")
        text = "\n".join(block.text for block in response.content if block.type == "text").strip()
        if not text:
            raise RuntimeError(f"no analysis returned (stop reason {response.stop_reason})")
        return text

    def decide(self, research: str, symbols: list[str]) -> dict:
        """Turn the analysis into a validated JSON portfolio."""
        response = self.client.messages.create(
            model=self.cfg.model, max_tokens=16000,
            output_config={"effort": "low", "format": {"type": "json_schema", "schema": decision_schema(symbols)}},
            messages=[{"role": "user", "content": (
                f"{research}\n\n---\nAs the risk manager, write down the final portfolio from the analysis above: at most "
                f"{self.cfg.max_positions} positions, each weight a fraction of the account (0-{self.cfg.max_weight}), "
                "total at most 1, the rest in cash. An empty list means all cash. Give a one-sentence reason each "
                "and a one-sentence market view.")}])
        if response.stop_reason == "refusal":
            raise RuntimeError("the model declined to decide")
        return json.loads(next(block.text for block in response.content if block.type == "text"))

    # ------------------------------------------------------------ daily run
    def prompt(self, daily: dict[str, pd.DataFrame], regime: dict, symbols: list[str], session: str,
               held: dict[str, float]) -> str:
        table = snapshot(daily, symbols)
        return (f"Session just closed: {session} (New York). Decide what to hold from the next open.\n\n"
                f"Market regime (Nasdaq distribution/follow-through-day model): {json.dumps(regime, default=str)}\n\n"
                f"Currently held (fraction of account): {json.dumps(held) if held else 'nothing (all cash)'}\n\n"
                f"Daily numbers for the symbols you may buy (percent changes, RSI, trend distance, 20-day annualised "
                f"volatility, bullish score out of about 9):\n{json.dumps(table)}\n\n"
                "Search for news that matters for these names and the market today (earnings dates, guidance, macro "
                "events, sector moves), have each analyst report briefly, run the bull/bear debate, then give the "
                "trader's proposal and the risk manager's final call with weights.")

    def due(self, store: dict, session: str, now: pd.Timestamp) -> bool:
        if store.get("last_session") == session:
            return False
        last = store.get("last_attempt")
        return not last or now - pd.Timestamp(last) >= pd.Timedelta(hours=2)  # retry failures later

    def run(self, store: dict, daily: dict[str, pd.DataFrame], regime: dict, now: pd.Timestamp) -> CopyBook | None:
        """Update ``store`` (the ``analyst`` part of the agent state) and return the book."""
        index = daily.get(self.config.daily.index)
        symbols = [a.symbol for a in self.config.universe
                   if a.kind == "us_equity" and a.trade_strategies and a.symbol in daily]
        if index is not None and len(index) and symbols:
            session = index.index[-1].strftime("%Y-%m-%d")
            if self.due(store, session, now):
                store["last_attempt"] = now.isoformat()
                book = CopyBook.from_dict(store["book"]) if store.get("book") else CopyBook(
                    BOOK, f"Claude ({self.cfg.model}) as a TradingAgents-style desk: web news, analyst reports, "
                          "bull/bear debate and a risk-managed pick of up to "
                          f"{self.cfg.max_positions} names after each US close. Forward-only: no backtest.",
                    "Claude API with web search", kind="ai", cap=self.cfg.max_weight)
                try:
                    analysis = self.research(self.prompt(daily, regime, symbols, session, book.current()))
                    decision = self.decide(analysis, symbols)
                    weights = clean_positions(decision.get("positions"), symbols, self.cfg.max_positions,
                                              self.cfg.max_weight)
                    when = max(_next_open_utc(pd.Timestamp(session)), now.ceil("5min"))
                    book.schedule = (book.schedule + [[when.isoformat(), weights]])[-400:]
                    book.as_of, book.error = session, None
                    store["last_session"] = session
                    store["latest"] = {"session": session, "effective": when.isoformat(), "model": self.cfg.model,
                                       "market_view": str(decision.get("market_view") or "")[:600],
                                       "positions": [{"symbol": r.get("symbol"), "weight": weights.get(r.get("symbol"), 0.0),
                                                      "reason": str(r.get("reason") or "")[:300]}
                                                     for r in decision.get("positions") or [] if r.get("symbol") in weights],
                                       "analysis": analysis[:6000]}
                except Exception as error:  # an API problem must not stop trading
                    log.warning("AI analyst failed: %s", error)
                    book.error = f"Analysis failed: {str(error)[:300]}"
                book.updated_at = now.isoformat()
                store["book"] = book.to_dict()
        return CopyBook.from_dict(store["book"]) if store.get("book") else None
