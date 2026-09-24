"""The autonomous loop: fetch bars -> recompute signals -> trade every sleeve
-> (optionally) mirror the Agent sleeve into a broker -> write reports."""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from . import report
from .config import Config
from .data import INTERVAL_SECONDS, MarketData
from .portfolio import Quote, Sleeve, new_sleeve
from .research import Research, run_research
from .sessions import is_open
from .state import STATE_VERSION, StateStore
from .strategies import all_strategies

log = logging.getLogger(__name__)

HISTORY_EVERY = pd.Timedelta(minutes=10)


def iso(ts: pd.Timestamp) -> str:
    return ts.tz_convert("UTC").isoformat().replace("+00:00", "Z")


@dataclass
class Engine:
    config: Config
    state_dir: Path
    market: MarketData | None = None
    cache_dir: Path | None = None
    broker: object | None = None
    forecaster: object | None = None
    research: Research | None = None
    _data_marker: tuple | None = field(default=None, repr=False)

    def __post_init__(self):
        self.state_dir = Path(self.state_dir)
        self.store = StateStore(self.state_dir)
        if self.market is None:
            self.market = MarketData(self.config, self.cache_dir or Path(".cache/bars"))
        if self.broker is None and self.config.broker.mode != "paper":
            from .live import make_broker
            self.broker = make_broker(self.config)

    # ------------------------------------------------------------ helpers
    def _load_state(self, now: pd.Timestamp) -> dict:
        state = self.store.load()
        if state is None:
            state = {"version": STATE_VERSION, "created_at": iso(now), "mode": self.config.broker.mode,
                     "starting_capital_gbp": self.config.starting_capital_gbp, "sleeves": {},
                     "kronos": {}, "last_history_at": None, "ticks": 0, "broker": None}
        return state

    def _strategies(self):
        return all_strategies(kronos=self.config.kronos.enabled, disabled=self.config.disabled_strategies)

    def _kronos_extra(self, state: dict, now: pd.Timestamp) -> dict | None:
        if not self.config.kronos.enabled:
            return None
        try:
            from .kronos.forecaster import KronosForecaster, forecasts_as_series, kronos_available, update_forecasts
        except ImportError as error:
            log.warning("Kronos unavailable: %s", error)
            return None
        if self.forecaster is None:
            if not kronos_available():
                log.warning("Kronos enabled but torch/einops/huggingface_hub are not installed")
                return None
            self.forecaster = KronosForecaster(self.config.kronos)
        open_symbols = {s for s in self.market.bars if is_open(self.config.asset(s).kind, now)}
        try:
            update_forecasts(state.setdefault("kronos", {}), self.market.bars, self.config.kronos, now,
                             forecaster=self.forecaster, open_symbols=open_symbols, time_budget_s=40)
        except Exception as error:  # never let the model stop trading
            log.warning("Kronos update failed: %s", error)
        series = forecasts_as_series(state.get("kronos", {}))
        return {s: {"kronos": v, "kronos_threshold": self.config.kronos.entry_threshold} for s, v in series.items()}

    def _quotes(self, now: pd.Timestamp) -> dict[str, Quote]:
        quotes = {}
        max_age = pd.Timedelta(minutes=self.config.risk.max_bar_age_minutes)
        bar = pd.Timedelta(seconds=INTERVAL_SECONDS[self.config.interval])
        for symbol, frame in self.market.bars.items():
            if frame is None or frame.empty or symbol not in self.config.symbols:
                continue
            asset = self.config.asset(symbol)
            last_end = frame.index[-1] + bar
            fresh = now - last_end <= max_age
            tradable = fresh and is_open(asset.kind, now)
            quotes[symbol] = Quote(symbol, float(frame["close"].iloc[-1]), self.market.fx_to_gbp(asset.currency),
                                   self.config.cost_bps[asset.kind] / 1e4, tradable)
        return quotes

    def _reason_fn(self, name: str, research: Research):
        sleeve = research.sleeves[name]
        if sleeve.kind == "strategy":
            return lambda symbol, side: research.reason(name, symbol)
        if name.startswith("Agent"):
            picks = {}
            for row in research.selection:
                picks.setdefault(row["symbol"], []).append(row["strategy"])

            def reason(symbol, side):
                if side == "buy" and symbol in picks:
                    return "following " + ", ".join(picks[symbol])
                return "selected signal exited" if side == "sell" else ""
            return reason
        return lambda symbol, side: ""

    # ------------------------------------------------------------ one tick
    def tick(self, now: pd.Timestamp | None = None) -> dict:
        now = (now or pd.Timestamp.now(tz="UTC")).tz_convert("UTC")
        started = time.monotonic()
        with self.store.lock():
            state = self._load_state(now)
            errors = self.market.refresh(now)
            marker = tuple((s, f.index[-1]) for s, f in sorted(self.market.bars.items()) if not f.empty)
            if marker != self._data_marker or self.research is None:
                extra = self._kronos_extra(state, now)
                self.research = run_research(self.market.bars, self.config, self._strategies(), extra)
                self._data_marker = marker
            research = self.research
            quotes = self._quotes(now)
            now_iso, today = iso(now), now.strftime("%Y-%m-%d")
            all_trades = []
            for name in research.sleeves:
                data = state["sleeves"].get(name) or new_sleeve(name, self.config.starting_capital_gbp, now_iso)
                sleeve = Sleeve(data)
                trades = sleeve.rebalance(research.targets(name), quotes, self.config.risk, now_iso, today,
                                          self._reason_fn(name, research))
                state["sleeves"][name] = sleeve.data
                all_trades.extend(trades)
            broker_summary = self._sync_broker(research, quotes, now)
            if broker_summary is not None:
                state["broker"] = broker_summary
                self.store.append("broker.jsonl", [{"t": now_iso, **broker_summary}])
            self.store.append("trades.jsonl", all_trades)
            last_hist = state.get("last_history_at")
            if last_hist is None or now - pd.Timestamp(last_hist) >= HISTORY_EVERY:
                self.store.append("history.jsonl", [{"t": now_iso, "e": {n: round(d["equity_gbp"], 4) for n, d in state["sleeves"].items()}}])
                state["last_history_at"] = now_iso
            state["ticks"] = state.get("ticks", 0) + 1
            state["mode"] = self.config.broker.mode
            state["last_tick"] = {"at": now_iso, "seconds": round(time.monotonic() - started, 2),
                                  "data_errors": errors, "new_trades": len(all_trades),
                                  "latest_bar": max((iso(t) for t in research.last_bar.values()), default=None),
                                  "tradable": sorted(s for s, q in quotes.items() if q.tradable)}
            self.store.save(state)
            report.write_all(self.state_dir, state, research, self.config, now)
        return {"at": now_iso, "trades": all_trades, "errors": errors,
                "agent_equity_gbp": round(state["sleeves"].get("Agent", {}).get("equity_gbp", 0.0), 4),
                "broker": broker_summary}

    def _sync_broker(self, research: Research, quotes: dict[str, Quote], now: pd.Timestamp):
        if self.broker is None:
            return None
        from .live import sync_broker
        name = self.config.broker.sleeve
        if name not in research.sleeves:
            return {"ok": False, "error": f"Unknown sleeve {name}"}
        gbpusd = 1.0 / self.market.fx_to_gbp("USD")
        prices_usd = {s: q.price for s, q in quotes.items() if self.config.asset(s).currency == "USD"}
        stamp = iso(research.index[-1])
        try:
            wanted = research.targets(name)
            # explicit zeros so the broker exits anything the sleeve no longer holds
            targets = {s: wanted.get(s, 0.0) for s in self.config.symbols}
            return sync_broker(self.broker, targets, self.config, now, prices_usd, gbpusd, stamp)
        except Exception as error:  # the paper ledger must keep going
            log.exception("Broker sync failed")
            return {"ok": False, "error": str(error)[:500]}

    # ------------------------------------------------------------ loop
    def run(self, minutes: float | None = None, interval: float = 60.0, max_ticks: int | None = None) -> None:
        deadline = time.monotonic() + minutes * 60 if minutes else None
        ticks = 0
        while True:
            try:
                result = self.tick()
                log.info("tick %s: %d trades, Agent £%.2f, errors=%s", result["at"], len(result["trades"]),
                         result["agent_equity_gbp"], list(result["errors"]))
            except Exception:
                log.exception("Tick failed; continuing")
            ticks += 1
            if max_ticks and ticks >= max_ticks:
                return
            # wake shortly after the next bar boundary
            now = time.time()
            wait = interval - (now % interval) + 5 if interval >= 60 else interval
            if deadline and time.monotonic() + wait > deadline:
                return
            time.sleep(wait)
