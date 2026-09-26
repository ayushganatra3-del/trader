"""AI bees: three competing AI traders powered by Jev, as in Creator Magic's video.

Jev is TypeSafe's "System One" decision model, served through OpenRouter's
Decisions API. Instead of writing text it answers typed multiple-choice
questions, with a probability for each option, in well under a second and for
a fraction of a cent. Every minute each bee sends Jev one compact snapshot
(live 1-minute numbers for each symbol plus what the bee holds) and asks one
question per symbol that is trading right now: buy, hold or sell. With the
default universe that is about 100 decisions a minute while US markets are
open (3 bees x 32 symbols), and 15 a minute overnight, when only crypto trades.

Each bee trades its own £100 paper sleeve at the latest 1-minute prices. The
bees only run forward, only when OPENROUTER_API_KEY is set, and stop calling
Jev (holding what they have) once the daily budget is spent.
"""
from __future__ import annotations

import dataclasses
import json
import logging
import os
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .config import Config
from .data import MarketData
from .portfolio import Quote, Sleeve, new_sleeve
from .sessions import is_open

log = logging.getLogger(__name__)

DECISIONS_URL = "https://openrouter.ai/api/alpha/decisions"
QUESTIONS_PER_CALL = 32  # the lowest per-request limit documented for Jev
SLEEVE_PREFIX = "AI bee: "


@dataclass(frozen=True)
class Bee:
    name: str
    strategy: str
    cap: float  # largest position, as a fraction of the sleeve
    max_positions: int
    max_exposure: float  # at most this much invested; the rest stays in cash
    min_prob: float  # buy only when Jev gives "buy" at least this probability

    @property
    def sleeve(self) -> str:
        return SLEEVE_PREFIX + self.name


BEES = (
    Bee("Bizzy", "Bizzy, a busy momentum trader: buy what is rising fast on strong volume, sell as soon as the "
                 "move stalls, and rotate into whatever is leading now.", 0.25, 4, 1.0, 0.5),
    Bee("Breezy", "Breezy, a calm, cautious investor: only buy index ETFs and large caps in steady uptrends, avoid "
                  "3x ETFs and small coins, keep plenty of cash and trade rarely.", 0.2, 3, 0.6, 0.65),
    Bee("Boozy", "Boozy, a reckless speculator: go big on the most volatile names (3x ETFs, COIN, MSTR, BITX, "
                 "ETHU, crypto) and chase the biggest moves.", 0.5, 2, 1.0, 0.4),
)

MENU = {
    "buy": "Buy now, or add: for this trader, the price is likely to rise over the next few minutes",
    "hold": "Hold: leave the current position (or no position) as it is",
    "sell": "Sell: exit any position or stay out; the price is likely to fall or the setup no longer fits",
}


def question_key(symbol: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", symbol)


def _pct(a: float, b: float) -> float | None:
    return round(100 * (a / b - 1), 3) if b and np.isfinite(a) and np.isfinite(b) else None


def live_numbers(bars: pd.DataFrame) -> dict | None:
    """What a trader would glance at on a 1-minute chart (completed bars only)."""
    if bars is None or len(bars) < 16:
        return None
    close, volume = bars["close"], bars["volume"]
    last = float(close.iloc[-1])
    change = lambda n: _pct(last, float(close.iloc[-1 - n])) if len(close) > n else None  # noqa: E731
    delta = close.diff().tail(60)
    gain, loss = delta.clip(lower=0).mean(), (-delta.clip(upper=0)).mean()
    today = bars[bars.index.normalize() == bars.index[-1].normalize()]
    base = volume.iloc[-65:-5].mean()
    return {"price": round(last, 6), "chg_1m_pct": change(1), "chg_5m_pct": change(5), "chg_15m_pct": change(15),
            "chg_60m_pct": change(60), "chg_today_pct": _pct(last, float(today["open"].iloc[0])),
            "rsi_60m": round(float(100 - 100 / (1 + gain / loss)), 1) if loss > 0 else 100.0,
            "volume_vs_hour": round(float(volume.tail(5).mean() / base), 2) if base > 0 else None}


def to_weights(bee: Bee, answers: dict, keys: dict[str, str], held: dict[str, float]) -> tuple[dict, dict]:
    """Jev's answers -> target weights. Returns (targets, {symbol: [choice, buy probability]})."""
    targets = {s: w for s, w in held.items() if w > 1e-9}  # anything not asked about is left alone
    decisions = {}
    for key, symbol in keys.items():
        answer = answers.get(key) if isinstance(answers, dict) else None
        if not isinstance(answer, dict):
            continue
        choice = answer.get("choice")
        try:
            p_buy = float((answer.get("probabilities") or {}).get("buy") or 0.0)
        except (TypeError, ValueError):
            p_buy = 0.0
        decisions[symbol] = [choice, round(p_buy, 3)]
        if choice == "buy" and p_buy >= bee.min_prob:
            targets[symbol] = max(targets.get(symbol, 0.0), bee.cap * p_buy)  # a buy never shrinks a position
        elif choice == "sell":
            targets.pop(symbol, None)
    targets = dict(sorted(targets.items(), key=lambda kv: -kv[1])[:bee.max_positions])
    total = sum(targets.values())
    if total > bee.max_exposure:
        targets = {s: w * bee.max_exposure / total for s, w in targets.items()}
    return {s: round(w, 4) for s, w in targets.items()}, decisions


class JevError(RuntimeError):
    pass


class JevClient:
    """OpenRouter's Decisions API (stdlib HTTP, like the rest of the data code)."""

    def __init__(self, api_key: str, model: str, timeout: float = 20.0, url: str = DECISIONS_URL):
        self.api_key, self.model, self.timeout, self.url = api_key, model, timeout, url

    def decide(self, state: dict, questions: dict) -> tuple[dict, float]:
        """Returns (answers keyed like ``questions``, cost in USD)."""
        body = json.dumps({"model": self.model, "state": state, "questions": questions}).encode()
        request = urllib.request.Request(self.url, data=body, method="POST", headers={
            "Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read(5_000_000))
        except urllib.error.HTTPError as error:
            detail = error.read(2000).decode(errors="replace")
            try:
                detail = json.loads(detail).get("error", {}).get("message") or detail
            except (ValueError, AttributeError):
                pass
            raise JevError(f"HTTP {error.code}: {detail}"[:400]) from error
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            raise JevError(str(error)[:400]) from error
        answers = payload.get("answers")
        if not isinstance(answers, dict):
            raise JevError(f"no answers in the reply: {str(payload)[:300]}")
        try:
            cost = float((payload.get("usage") or {}).get("cost") or 0.0)
        except (TypeError, ValueError):
            cost = 0.0
        return answers, cost


class Hive:
    """Runs every bee once per engine tick."""

    def __init__(self, config: Config, client=None, data: MarketData | None = None):
        self.config = config
        self.cfg = config.bees
        wanted = set(self.cfg.symbols) if self.cfg.symbols else None
        self.assets = [a for a in config.universe if a.kind in ("us_equity", "crypto")
                       and (wanted is None or a.symbol in wanted)]
        self.client = client or JevClient(os.environ.get("OPENROUTER_API_KEY", ""), self.cfg.model)
        if data is None:  # its own feed, so a rate limit on 1-minute bars never touches the main 5-minute data
            universe = tuple(dataclasses.replace(a, trade_strategies=True) for a in self.assets)  # all fetched every minute
            data = MarketData(dataclasses.replace(config, universe=universe, interval="1m", history_range="1d"), None)
        self.data = data

    @staticmethod
    def available() -> bool:
        return bool(os.environ.get("OPENROUTER_API_KEY"))

    def quotes(self, now: pd.Timestamp, fx_to_gbp) -> dict[str, Quote]:
        quotes = {}
        max_age = pd.Timedelta(minutes=self.cfg.max_quote_age_minutes)
        for asset in self.assets:
            bars = self.data.bars.get(asset.symbol)
            if bars is None or bars.empty:
                continue
            fresh = now - (bars.index[-1] + pd.Timedelta(minutes=1)) <= max_age
            quotes[asset.symbol] = Quote(asset.symbol, float(bars["close"].iloc[-1]), fx_to_gbp(asset.currency),
                                         self.config.cost(asset), fresh and is_open(asset.kind, now))
        return quotes

    def refresh(self, now: pd.Timestamp, fx_to_gbp) -> tuple[dict[str, Quote], dict[str, dict], dict[str, str]]:
        """Fresh 1-minute bars for the symbols trading now -> (quotes, per-symbol numbers for Jev, data errors)."""
        open_now = {a.symbol for a in self.assets if is_open(a.kind, now)}
        self.data.set_universe(self.data.config, open_now)
        errors = self.data.refresh(now)
        quotes = self.quotes(now, fx_to_gbp)
        market = {s: n for s in sorted(open_now) if s in quotes and quotes[s].tradable
                  and (n := live_numbers(self.data.bars.get(s))) is not None}
        return quotes, market, errors

    def ask(self, bee: Bee, market: dict[str, dict], sleeve: Sleeve) -> tuple[dict, float, dict, int]:
        """One bee's decisions -> (target weights, cost in USD, {symbol: [choice, buy probability]}, API calls)."""
        held = sleeve.weights()
        positions = sleeve.data["positions"]
        state = {"trader": bee.strategy, "cash_pct": round(100 * sleeve.data["cash_gbp"] / max(sleeve.data["equity_gbp"], 1e-9), 1),
                 "market": {}}
        keys = {}
        for symbol, numbers in market.items():
            key = question_key(symbol)
            keys[key] = symbol
            row = dict(numbers, held_pct=round(100 * held.get(symbol, 0.0), 1))
            if symbol in positions and (mark := sleeve.data["last_marks"].get(symbol)):
                position = positions[symbol]
                row["position_pnl_pct"] = _pct(position["units"] * mark, position["cost_gbp"])  # after fees
            state["market"][key] = row
        questions = {key: {"type": "choice", "criteria": MENU,
                           "instructions": f"You are the trader described in `trader`. From the live 1-minute numbers "
                                           f"and your holding in `market.{key}`, what do you do with {symbol} right now?"}
                     for key, symbol in keys.items()}
        answers, cost, calls = {}, 0.0, 0
        batch = list(questions.items())
        for start in range(0, len(batch), QUESTIONS_PER_CALL):
            part, part_cost = self.client.decide(state, dict(batch[start:start + QUESTIONS_PER_CALL]))
            answers.update(part)
            cost, calls = cost + part_cost, calls + 1
        targets, decisions = to_weights(bee, answers, keys, held)
        return targets, cost, decisions, calls

    def run(self, state: dict, now: pd.Timestamp, fx_to_gbp, risk_for) -> list[dict]:
        """One round: fresh 1-minute bars, one Jev call per bee, then each bee's sleeve trades."""
        store = state.setdefault("bees", {"model": self.cfg.model})
        store["model"] = self.cfg.model
        today, now_iso = now.strftime("%Y-%m-%d"), now.tz_convert("UTC").isoformat().replace("+00:00", "Z")
        spend = store.get("spend") or {}
        if spend.get("day") != today:
            spend = {"day": today, "usd": 0.0, "calls": 0, "decisions": 0}
        store["spend"] = spend
        quotes, market, errors = self.refresh(now, fx_to_gbp)
        store["data_errors"] = dict(list(errors.items())[:10])
        budget_left = spend["usd"] < self.cfg.daily_budget_usd
        store["budget_spent"] = not budget_left

        sleeves = {}
        for bee in BEES:
            sleeve = Sleeve(state["sleeves"].get(bee.sleeve) or new_sleeve(bee.sleeve, self.config.starting_capital_gbp, now_iso))
            sleeve.mark(quotes)
            sleeves[bee.name] = sleeve

        def ask(bee):
            try:
                return self.ask(bee, market, sleeves[bee.name]), None
            except Exception as error:  # an API problem must not stop trading
                return None, error

        results = {}
        if market and budget_left:
            with ThreadPoolExecutor(max_workers=len(BEES)) as pool:
                results = dict(zip([b.name for b in BEES], pool.map(ask, BEES)))

        trades = []
        for bee in BEES:
            sleeve = sleeves[bee.name]
            info = store.get(bee.name) or {}
            result, error = results.get(bee.name, (None, None))
            if result is not None:
                targets, cost, decisions, calls = result
                spend["usd"] = round(spend["usd"] + cost, 6)
                spend["calls"] += calls
                spend["decisions"] += len(decisions)
                counts = {c: sum(1 for d in decisions.values() if d[0] == c) for c in MENU}
                info = {"at": now_iso, "decisions": decisions, "counts": counts, "targets": targets, "error": None}
            else:
                targets = sleeve.weights()  # no fresh decision: hold what it has
                if error is not None:
                    log.warning("%s: Jev call failed: %s", bee.sleeve, error)
                    info = {**info, "error": str(error)[:300], "error_at": now_iso}
            reason = lambda symbol, side, d=info.get("decisions") or {}: (  # noqa: E731
                f"Jev: {d[symbol][0]} (buy p={d[symbol][1]:.2f})" if symbol in d else "")
            trades.extend(sleeve.rebalance(targets, quotes, risk_for(bee.sleeve), now_iso, today, reason))
            state["sleeves"][bee.sleeve] = sleeve.data
            store[bee.name] = info
        return trades
