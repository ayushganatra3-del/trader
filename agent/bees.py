"""AI bees: three competing AI traders powered by Jev, as in Creator Magic's video.

Jev is TypeSafe's "System One" decision model, served through OpenRouter's
Decisions API. Instead of writing text it answers typed multiple-choice
questions, with a probability for each option, in well under a second and for
a fraction of a cent. Every minute each bee sends Jev one compact snapshot
(live 1-minute numbers for each symbol plus what the bee holds) and asks one
question per symbol that is trading right now: buy, hold or sell. With the
default universe that is about 100 decisions a minute while US markets are
open (3 bees x 32 symbols), and 15 a minute overnight, when only crypto trades.

Answers are noisy from one minute to the next, and trading on each one paid
more in fees than any move earned. So the bees act only on steady, confident
calls: each symbol's buy and sell probabilities are averaged over recent
answers, a new position is held for a minimum time unless its stop-loss hits,
and a sold symbol isn't bought straight back.

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
    min_prob: float  # buy only when Jev's (smoothed) "buy" probability is at least this
    sell_prob: float  # sell only when its (smoothed) "sell" probability is at least this
    hold_minutes: float  # a new position is kept at least this long, unless its stop-loss hits
    stop_loss: float  # exit at this loss on the position (fees included), whatever its age
    cooldown_minutes: float  # a sold symbol isn't bought back for this long

    @property
    def sleeve(self) -> str:
        return SLEEVE_PREFIX + self.name


BEES = (
    Bee("Bizzy", "Bizzy, a busy momentum trader: buy what is rising fast on strong volume, sell as soon as the "
                 "move stalls, and rotate into whatever is leading now.",
        cap=0.25, max_positions=4, max_exposure=1.0, min_prob=0.55, sell_prob=0.5, hold_minutes=10,
        stop_loss=0.02, cooldown_minutes=20),
    Bee("Breezy", "Breezy, a calm, cautious investor: only buy index ETFs and large caps in steady uptrends, avoid "
                  "3x ETFs and small coins, keep plenty of cash and trade rarely.",
        cap=0.2, max_positions=3, max_exposure=0.6, min_prob=0.6, sell_prob=0.6, hold_minutes=60,
        stop_loss=0.03, cooldown_minutes=60),
    Bee("Boozy", "Boozy, a reckless speculator: go all in on the single most explosive name (3x ETFs, COIN, MSTR, "
                 "BITX, ETHU, crypto) and ride the biggest moves.",
        cap=1.0, max_positions=1, max_exposure=1.0, min_prob=0.5, sell_prob=0.5, hold_minutes=15,
        stop_loss=0.04, cooldown_minutes=15),
)

SMOOTHING = 0.3  # weight of the newest answer in each symbol's running buy/sell probability (~3-minute memory)
MEMORY = pd.Timedelta(minutes=10)  # older running probabilities start afresh

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


@dataclass(frozen=True)
class Holding:
    weight: float  # fraction of the sleeve
    pnl: float | None  # gain on the position after fees, as a fraction
    age_minutes: float


def _prob(probabilities, option: str) -> float:
    try:
        return float((probabilities or {}).get(option) or 0.0)
    except (TypeError, ValueError, AttributeError):
        return 0.0


def plan(bee: Bee, answers: dict, keys: dict[str, str], book: dict[str, Holding], memory: dict,
         now: pd.Timestamp) -> tuple[dict, dict]:
    """Jev's answers -> target weights, trading only on steady, confident calls.

    Acting on every minute's answer churned the first bees into the ground: fees were nearly all of their
    losses. So each symbol's buy and sell probabilities are smoothed over the bee's recent answers, a buy needs
    both the latest answer and the running probability, a new position is held at least ``hold_minutes`` unless
    its stop-loss hits, and a sold symbol isn't bought back until its cooldown ends.
    ``memory`` (running probabilities and sale times) is updated in place.
    Returns (targets, {symbol: [choice, running buy probability, what was done]})."""
    stamp = now.isoformat()
    probs, sold = memory.setdefault("probs", {}), memory.setdefault("sold", {})
    targets = {s: h.weight for s, h in book.items() if h.weight > 1e-9}  # anything not asked about is left alone
    locked = {s for s in targets if book[s].age_minutes < bee.hold_minutes}
    decisions = {}
    for key, symbol in keys.items():
        answer = answers.get(key) if isinstance(answers, dict) else None
        if not isinstance(answer, dict):
            continue
        choice, probabilities = answer.get("choice"), answer.get("probabilities")
        p_buy, p_sell = _prob(probabilities, "buy"), _prob(probabilities, "sell")
        prev = probs.get(symbol)
        if prev and now - pd.Timestamp(prev[2]) <= MEMORY:
            p_buy_avg = SMOOTHING * p_buy + (1 - SMOOTHING) * prev[0]
            p_sell_avg = SMOOTHING * p_sell + (1 - SMOOTHING) * prev[1]
        else:
            p_buy_avg, p_sell_avg = p_buy, p_sell
        probs[symbol] = [round(p_buy_avg, 4), round(p_sell_avg, 4), stamp]
        held = book.get(symbol)
        note = ""
        if symbol in targets:
            if held.pnl is not None and held.pnl <= -bee.stop_loss:
                note = f"stop-loss at {100 * held.pnl:+.1f}%"
            elif symbol in locked:
                note = f"holding ({held.age_minutes:.0f} of {bee.hold_minutes:.0f} min)"
            elif choice == "sell" and p_sell_avg >= bee.sell_prob:
                note = f"sell (sell p={p_sell_avg:.2f}) after {held.age_minutes:.0f} min"
            elif choice == "buy" and p_buy_avg >= bee.min_prob:
                targets[symbol] = max(targets[symbol], bee.cap * p_buy_avg)  # a buy never shrinks a position
                note = f"add (buy p={p_buy_avg:.2f})"
            if note.startswith(("stop", "sell")):
                targets.pop(symbol)
                locked.discard(symbol)
        elif choice == "buy" and min(p_buy, p_buy_avg) >= bee.min_prob:
            if symbol in sold and now - pd.Timestamp(sold[symbol]) < pd.Timedelta(minutes=bee.cooldown_minutes):
                note = "cooling down after a sale"
            else:
                targets[symbol] = bee.cap * p_buy_avg
                note = f"buy (buy p={p_buy_avg:.2f})"
        decisions[symbol] = [choice, round(p_buy_avg, 3), note]
    # positions still inside their holding time come first, then the strongest
    keep = sorted(targets, key=lambda s: (s not in locked, -targets[s]))[:bee.max_positions]
    targets = {s: targets[s] for s in keep}
    fixed = sum(w for s, w in targets.items() if s in locked)
    free = sum(w for s, w in targets.items() if s not in locked)
    if fixed + free > bee.max_exposure and free > 0:  # trim the rest, never the positions being held
        scale = max(0.0, bee.max_exposure - fixed) / free
        targets = {s: (w if s in locked else w * scale) for s, w in targets.items()}
    targets = {s: round(w, 4) for s, w in targets.items() if w > 1e-4}
    for symbol in book:
        if book[symbol].weight > 1e-9 and symbol not in targets:
            sold[symbol] = stamp
    for table in (probs, sold):  # forget what is a day old
        for symbol in [s for s, v in table.items() if now - pd.Timestamp(v[2] if isinstance(v, list) else v) > pd.Timedelta(days=1)]:
            del table[symbol]
    return targets, decisions


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
        self.feed_config = data.config  # every symbol the bees may trade; each round fetches only the open ones

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
        # fetch only what trades now, plus a few minutes after the close for the closing bar: closed stocks have no
        # fresh bars, so asking every minute (all weekend) would only burn Yahoo's rate limit, which the main
        # 5-minute feed shares
        fetch = open_now | {a.symbol for a in self.assets if is_open(a.kind, now - pd.Timedelta(minutes=5))}
        feed = self.feed_config
        self.data.set_universe(dataclasses.replace(feed, universe=tuple(a for a in feed.universe if a.symbol in fetch)),
                               fetch)
        self.data.errors = {s: e for s, e in self.data.errors.items() if s in fetch}  # closed symbols' old errors
        errors = self.data.refresh(now)
        quotes = self.quotes(now, fx_to_gbp)
        market = {s: n for s in sorted(open_now) if s in quotes and quotes[s].tradable
                  and (n := live_numbers(self.data.bars.get(s))) is not None}
        return quotes, market, errors

    def ask(self, bee: Bee, market: dict[str, dict], sleeve: Sleeve, usage: dict, memory: dict,
            now: pd.Timestamp) -> tuple[dict, dict]:
        """One bee's decisions -> (target weights, {symbol: [choice, running buy probability, what was done]}).

        ``usage`` ({"usd", "calls"}) is updated after every request, so paid batches count even if a later one fails;
        ``memory`` keeps the bee's running probabilities and recent sales between rounds."""
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
        answers = {}
        batch = list(questions.items())
        for start in range(0, len(batch), QUESTIONS_PER_CALL):
            part, cost = self.client.decide(state, dict(batch[start:start + QUESTIONS_PER_CALL]))
            usage["usd"] += cost
            usage["calls"] += 1
            answers.update(part)
        book = {}
        for symbol, position in positions.items():
            mark = sleeve.data["last_marks"].get(symbol)
            opened = pd.Timestamp(position["opened_at"])
            book[symbol] = Holding(held.get(symbol, 0.0),
                                   position["units"] * mark / position["cost_gbp"] - 1 if mark and position["cost_gbp"] > 0 else None,
                                   (now - (opened if opened.tzinfo else opened.tz_localize("UTC"))) / pd.Timedelta(minutes=1))
        return plan(bee, answers, keys, book, memory, now)

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

        usage = {bee.name: {"usd": 0.0, "calls": 0} for bee in BEES}
        memory = store.setdefault("memory", {})
        for bee in BEES:
            memory.setdefault(bee.name, {})

        def ask(bee):
            try:
                return self.ask(bee, market, sleeves[bee.name], usage[bee.name], memory[bee.name], now), None
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
            spend["usd"] = round(spend["usd"] + usage[bee.name]["usd"], 6)
            spend["calls"] += usage[bee.name]["calls"]
            if result is not None:
                targets, decisions = result
                spend["decisions"] += len(decisions)
                counts = {c: sum(1 for d in decisions.values() if d[0] == c) for c in MENU}
                info = {"at": now_iso, "decisions": decisions, "counts": counts, "targets": targets, "error": None}
            else:
                targets = sleeve.weights()  # no fresh decision: hold what it has
                if error is not None:
                    log.warning("%s: Jev call failed: %s", bee.sleeve, error)
                    info = {**info, "error": str(error)[:300], "error_at": now_iso}
            reason = lambda symbol, side, d=info.get("decisions") or {}: (  # noqa: E731
                f"Jev: {d[symbol][2] or d[symbol][0]}" if symbol in d and len(d[symbol]) > 2 else "")
            trades.extend(sleeve.rebalance(targets, quotes, risk_for(bee.sleeve), now_iso, today, reason))
            state["sleeves"][bee.sleeve] = sleeve.data
            store[bee.name] = info
        return trades
