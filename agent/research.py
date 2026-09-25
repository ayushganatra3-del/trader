"""Vectorised strategy engine: signals -> positions -> sleeve weights -> returns.

One pass computes, for every strategy x symbol pair, the position it would
hold on every bar of the look-back window. From that we derive

* each strategy's sleeve (its own £100 portfolio, up to ``slots`` positions),
* the walk-forward meta sleeves ("Agent", "Agent (aggressive)") that each day
  pick the pairs with the best risk-adjusted results over the previous
  ``lookback_days`` (never using that day's data),
* a "Consensus" sleeve that goes long when enough strategies agree,
* backtest statistics for all of them.

The live engine takes the *last row* of each sleeve's weights as its target,
so paper trading and backtests share exactly the same logic.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import Config
from .copytrade import CopyBook, book_weights
from .indicators import Features
from .strategies import Strategy

log = logging.getLogger(__name__)

# exit / entry reason codes produced by the position engine
REASONS = {0: "", 1: "exit signal", 2: "stop-loss", 3: "take-profit", 4: "time stop",
           5: "end-of-day flatten", 10: "entry signal"}

META = "Agent"
AGGRESSIVE = "Agent (aggressive)"
CONSENSUS = "Consensus"
ROTATION = "Agent (rotation)"
META_LABEL = "Agent (ML meta-label)"
MOMENTUM = "Max aggression: {days}-day momentum"


@dataclass
class SleeveResult:
    name: str
    kind: str  # "strategy" | "meta" | "benchmark" | "copy"
    weights: pd.DataFrame  # T x symbols, fraction of sleeve equity
    returns: pd.Series  # per-bar net return
    strategy: Strategy | None = None
    stats: dict = field(default_factory=dict)
    description: str = ""


@dataclass
class Research:
    index: pd.DatetimeIndex
    symbols: list[str]
    close: pd.DataFrame  # forward-filled closes (quote currency)
    last_bar: dict[str, pd.Timestamp]
    sleeves: dict[str, SleeveResult]
    pair_columns: list[tuple[str, str]]  # (strategy, symbol)
    pair_pos: np.ndarray  # T x P bool
    last_reason: dict[tuple[str, str], str]
    selection: list[dict]  # today's meta picks
    selection_history: pd.DataFrame | None = None

    def targets(self, sleeve: str) -> dict[str, float]:
        row = self.sleeves[sleeve].weights.iloc[-1]
        return {symbol: float(weight) for symbol, weight in row.items() if weight > 1e-9}

    def reason(self, strategy: str, symbol: str) -> str:
        return self.last_reason.get((strategy, symbol), "")


# --------------------------------------------------------------- position engine

def run_positions(entries, exits, close, atr, force_flat, no_entry, stop_mult, take_mult, trail_mult, max_bars):
    """Long-only state machine evaluated on bar closes, vectorised over columns.

    All matrices are T x N; ``*_mult``/``max_bars`` are length-N (NaN = off).
    Returns (positions T x N bool, reason-of-last-change N int, last-change-bar N int).
    """
    steps, width = close.shape
    pos = np.zeros(width, dtype=bool)
    stop = np.full(width, np.nan)
    take = np.full(width, np.nan)
    held = np.zeros(width)
    out = np.zeros((steps, width), dtype=bool)
    reason = np.zeros(width, dtype=np.int16)
    changed_at = np.full(width, -1)
    has_trail = ~np.isnan(trail_mult)
    has_limit = ~np.isnan(max_bars)
    for t in range(steps):
        c = close[t]
        valid = ~np.isnan(c)
        a = atr[t]
        live = pos & valid
        if has_trail.any():
            trail = c - trail_mult * a
            upd = live & has_trail & ~np.isnan(trail)
            stop[upd] = np.fmax(stop[upd], trail[upd])
        held += live
        sig = live & exits[t]
        stopped = live & (c <= stop)
        took = live & (c >= take)
        timed = live & has_limit & (held >= max_bars)
        flat = live & force_flat[t]
        leaving = sig | stopped | took | timed | flat
        if leaving.any():
            code = np.where(flat, 5, np.where(stopped, 2, np.where(took, 3, np.where(timed, 4, 1))))
            reason[leaving] = code[leaving]
            changed_at[leaving] = t
            pos &= ~leaving
        entering = ~pos & ~leaving & valid & entries[t] & ~no_entry[t] & ~force_flat[t] & ~np.isnan(a)
        if entering.any():
            pos |= entering
            stop[entering] = (c - stop_mult * a)[entering]
            if has_trail.any():
                stop[entering & has_trail] = np.fmax(stop[entering & has_trail], (c - trail_mult * a)[entering & has_trail])
            take[entering] = (c + take_mult * a)[entering]
            held[entering] = 0
            reason[entering] = 10
            changed_at[entering] = t
        out[t] = pos
    return out, reason, changed_at


def _atr_on_index(f: Features, timeframe: int, index: pd.DatetimeIndex) -> np.ndarray:
    """ATR(14) of the strategy's timeframe, known from each bar's close onward."""
    if timeframe == f.bar_minutes:
        atr = f.atr(14)
    else:
        higher, anchor = f.resampled(timeframe)
        atr = f.on_base(higher.atr(14), anchor, events=False)
    return atr.reindex(index).to_numpy()


def _scatter(series: pd.Series, loc: np.ndarray, steps: int) -> np.ndarray:
    out = np.zeros(steps, dtype=bool)
    out[loc] = series.fillna(False).to_numpy(dtype=bool)
    return out


def _nan(value):
    return np.nan if value is None else float(value)


# --------------------------------------------------------------- statistics

def trade_list(active: np.ndarray, close: np.ndarray, cost: np.ndarray) -> list[float]:
    """Round-trip returns for boolean holdings (T x N) using forward-filled closes."""
    trades = []
    padded = np.vstack([np.zeros((1, active.shape[1]), bool), active, np.zeros((1, active.shape[1]), bool)])
    diff = np.diff(padded.astype(np.int8), axis=0)
    for column in range(active.shape[1]):
        starts = np.flatnonzero(diff[:, column] == 1)
        ends = np.flatnonzero(diff[:, column] == -1)
        for start, end in zip(starts, ends):
            exit_bar = min(end, len(close) - 1)
            entry_price, exit_price = close[start, column], close[exit_bar, column]
            if np.isfinite(entry_price) and np.isfinite(exit_price) and entry_price > 0:
                trades.append(exit_price / entry_price - 1 - 2 * cost[column])
    return trades


def sleeve_stats(returns: pd.Series, trades: list[float], exposure: float, capital: float) -> dict:
    if returns.empty:
        return {}
    equity = capital * (1 + returns).cumprod()
    daily = equity.resample("1D").last().dropna()
    daily_ret = daily.pct_change().dropna()
    sharpe = float(daily_ret.mean() / daily_ret.std() * np.sqrt(365)) if len(daily_ret) > 2 and daily_ret.std() > 0 else 0.0
    peak = equity.cummax()
    drawdown = float((equity / peak - 1).min())
    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t <= 0]
    days = max((returns.index[-1] - returns.index[0]).total_seconds() / 86400, 1e-9)
    total = float(equity.iloc[-1] / capital - 1)
    return {
        "return_pct": round(total * 100, 2),
        "final_gbp": round(float(equity.iloc[-1]), 2),
        "sharpe": round(sharpe, 2),
        "max_drawdown_pct": round(drawdown * 100, 2),
        "trades": len(trades),
        "win_rate_pct": round(100 * len(wins) / len(trades), 1) if trades else 0.0,
        "avg_trade_pct": round(100 * float(np.mean(trades)), 3) if trades else 0.0,
        "profit_factor": round(sum(wins) / abs(sum(losses)), 2) if losses and sum(losses) != 0 else (99.0 if wins else 0.0),
        "exposure_pct": round(100 * exposure, 1),
        "days": round(days, 1),
        "per_day_pct": round(((1 + total) ** (1 / days) - 1) * 100, 3) if total > -1 else -100.0,
    }


def curve(returns: pd.Series, capital: float, points: int = 150) -> list[list]:
    if returns.empty:
        return []
    equity = capital * (1 + returns).cumprod()
    step = max(1, len(equity) // points)
    sampled = equity.iloc[::step]
    if sampled.index[-1] != equity.index[-1]:
        sampled = pd.concat([sampled, equity.iloc[-1:]])
    return [[ts.isoformat(), round(float(value), 2)] for ts, value in sampled.items()]


# --------------------------------------------------------------- main entry

def slot_weights(active: np.ndarray, slots: int, cap: float) -> np.ndarray:
    count = active.sum(axis=1, keepdims=True)
    return np.minimum(active / np.maximum(count, slots), cap)


def run_research(bars: dict[str, pd.DataFrame], config: Config, strategies: list[Strategy],
                 extra: dict[str, dict] | None = None, min_bars: int = 60,
                 copy_books: list[CopyBook] | None = None) -> Research:
    risk, meta_cfg = config.risk, config.meta
    usable = {s: b for s, b in bars.items() if b is not None and len(b) >= min_bars and s in config.symbols}
    symbols = [s for s in config.symbols if s in usable]
    if not symbols:
        raise ValueError("No symbol has enough bars to trade")
    index = usable[symbols[0]].index
    for symbol in symbols[1:]:
        index = index.union(usable[symbol].index)
    steps, n_sym = len(index), len(symbols)
    sym_pos = {s: i for i, s in enumerate(symbols)}
    locs = {s: index.get_indexer(usable[s].index) for s in symbols}

    close_raw = pd.DataFrame({s: usable[s]["close"] for s in symbols}).reindex(index)
    atr_cols: dict[tuple[str, int], np.ndarray] = {}  # (symbol, timeframe) -> ATR on the union index
    force_flat_sym = {}
    no_entry_sym = {}
    features = {}
    for s in symbols:
        asset = config.asset(s)
        f = Features(usable[s], asset.kind, extra=(extra or {}).get(s))
        features[s] = f
        if asset.kind == "crypto":
            force_flat_sym[s] = np.zeros(steps, bool)
            no_entry_sym[s] = np.zeros(steps, bool)
        else:
            sess = f.session
            ff = (sess["to_close"] < risk.flatten_minutes_before_close).reindex(index, fill_value=False).to_numpy()
            ne = ((sess["to_close"] < risk.no_entry_minutes_before_close) |
                  (sess["since_open"] < risk.no_entry_minutes_after_open)).reindex(index, fill_value=False).to_numpy()
            force_flat_sym[s] = ff
            no_entry_sym[s] = ne

    # ---- signals for every applicable (strategy, symbol) pair
    columns: list[tuple[str, str]] = []
    entries_cols, exits_cols, flat_cols, noent_cols, col_sym = [], [], [], [], []
    stop_m, take_m, trail_m, limit_m, col_atr = [], [], [], [], []
    for strategy in strategies:
        wanted = strategy.params.get("symbols") if strategy.benchmark else None
        for s in symbols:
            asset = config.asset(s)
            if asset.kind not in strategy.kinds or (wanted and s not in wanted):
                continue
            if not strategy.benchmark and not asset.trade_strategies:
                continue
            try:
                entry, exit_ = strategy.fn(features[s])
            except Exception as error:  # a broken rule must not stop the others
                log.warning("Strategy %s failed on %s: %s", strategy.name, s, error)
                continue
            columns.append((strategy.name, s))
            entries_cols.append(_scatter(entry, locs[s], steps))
            exits_cols.append(_scatter(exit_, locs[s], steps))
            intraday_flat = strategy.intraday and asset.kind != "crypto"
            flat_cols.append(force_flat_sym[s] if intraday_flat else np.zeros(steps, bool))
            noent_cols.append(no_entry_sym[s] if asset.kind != "crypto" and not strategy.benchmark else np.zeros(steps, bool))
            col_sym.append(sym_pos[s])
            key = (s, strategy.timeframe)
            if key not in atr_cols:
                atr_cols[key] = _atr_on_index(features[s], strategy.timeframe, index)
            col_atr.append(key)
            stop_m.append(_nan(strategy.stop_atr))
            take_m.append(_nan(strategy.take_atr))
            trail_m.append(_nan(strategy.trail_atr))
            scale = strategy.timeframe / 5  # max_bars counts the strategy's own bars
            limit_m.append(_nan(strategy.max_bars * scale if strategy.max_bars else None))
    if not columns:
        raise ValueError("No strategy produced signals")
    col_sym_arr = np.asarray(col_sym)
    close_np = close_raw.to_numpy()
    pos, reasons, changed_at = run_positions(
        np.column_stack(entries_cols), np.column_stack(exits_cols), close_np[:, col_sym_arr],
        np.column_stack([atr_cols[key] for key in col_atr]),
        np.column_stack(flat_cols), np.column_stack(noent_cols),
        np.asarray(stop_m), np.asarray(take_m), np.asarray(trail_m), np.asarray(limit_m))
    last_reason = {}
    for j, pair in enumerate(columns):
        if changed_at[j] == steps - 1:
            last_reason[pair] = REASONS[int(reasons[j])]

    # ---- returns and costs
    close_ff = close_raw.ffill()
    ret = close_ff.pct_change().fillna(0.0).to_numpy()
    cost_sym = np.array([config.cost(config.asset(s)) for s in symbols])
    capital = config.starting_capital_gbp
    close_ff_np = close_ff.to_numpy()

    def portfolio_returns(weights: np.ndarray) -> pd.Series:
        prev = np.vstack([np.zeros((1, n_sym)), weights[:-1]])
        gross = (prev * ret).sum(axis=1)
        turnover = (np.abs(weights - prev) * cost_sym).sum(axis=1)
        return pd.Series(gross - turnover, index=index)

    def make_sleeve(name, kind, weights, strategy=None):
        rets = portfolio_returns(weights)
        active = weights > 1e-9
        stats = sleeve_stats(rets, trade_list(active, close_ff_np, cost_sym), float(active.any(axis=1).mean()), capital)
        return SleeveResult(name, kind, pd.DataFrame(weights, index=index, columns=symbols), rets, strategy, stats)

    sleeves: dict[str, SleeveResult] = {}
    strat_cols: dict[str, list[int]] = {}
    for j, (name, _) in enumerate(columns):
        strat_cols.setdefault(name, []).append(j)
    for strategy in strategies:
        cols = strat_cols.get(strategy.name)
        if not cols:
            continue
        active = np.zeros((steps, n_sym), bool)
        active[:, col_sym_arr[cols]] = pos[:, cols]
        if strategy.benchmark:
            weights = active / np.maximum(active.sum(axis=1, keepdims=True), 1)
            sleeves[strategy.name] = make_sleeve(strategy.name, "benchmark", weights, strategy)
        else:
            weights = slot_weights(active, risk.slots, risk.max_symbol_weight)
            sleeves[strategy.name] = make_sleeve(strategy.name, "strategy", weights, strategy)

    # ---- schedule books: copy trading (famous investors, insiders) and daily-bar sleeves
    for book in copy_books or []:
        weights = book_weights(book, index, symbols, book.cap or risk.max_symbol_weight)
        if weights.any() or (book.kind in ("daily", "ai") and book.schedule):  # may sit in cash for weeks
            sleeve = make_sleeve(book.name, book.kind, weights)
            sleeve.description = book.description
            sleeves[book.name] = sleeve

    # ---- walk-forward meta selection over (strategy, symbol) pairs
    bench_names = {s.name for s in strategies if s.benchmark}
    trade_cols = np.array([j for j, (name, _) in enumerate(columns) if name not in bench_names])
    selection: list[dict] = []
    history = None
    if len(trade_cols):
        p_pos = pos[:, trade_cols].astype(np.float32)
        p_sym = col_sym_arr[trade_cols]
        prev = np.vstack([np.zeros((1, len(trade_cols)), np.float32), p_pos[:-1]])
        pair_ret = prev * ret[:, p_sym] - np.abs(p_pos - prev) * cost_sym[p_sym]
        pair_entries = (p_pos > prev).astype(np.float32)
        day_idx, day_keys = pd.factorize(index.normalize(), sort=True)
        n_days = len(day_keys)
        daily = pd.DataFrame(pair_ret).groupby(day_idx).sum().to_numpy(dtype=float)
        daily_entries = pd.DataFrame(pair_entries).groupby(day_idx).sum().to_numpy(dtype=float)
        lookback = meta_cfg.lookback_days
        d_frame = pd.DataFrame(daily)
        mean = d_frame.rolling(lookback, min_periods=lookback).mean().shift(1).to_numpy()
        std = d_frame.rolling(lookback, min_periods=lookback).std().shift(1).to_numpy()
        total = d_frame.rolling(lookback, min_periods=lookback).sum().shift(1).to_numpy()
        n_trades = pd.DataFrame(daily_entries).rolling(lookback, min_periods=lookback).sum().shift(1).to_numpy()
        with np.errstate(divide="ignore", invalid="ignore"):
            score = mean / std * np.sqrt(lookback)
        eligible = (n_trades >= meta_cfg.min_trades) & (total > 0) & (score > 0) & np.isfinite(score)
        score = np.where(eligible, score, -np.inf)

        def choose(k: int) -> np.ndarray:
            chosen = np.zeros_like(eligible)
            if k <= 0:
                return chosen
            top = np.argsort(-score, axis=1)[:, :k]
            rows = np.arange(n_days)[:, None]
            chosen[rows, top] = True
            return chosen & eligible

        one_hot = np.zeros((len(trade_cols), n_sym), np.float32)
        one_hot[np.arange(len(trade_cols)), p_sym] = 1.0
        for name, k, cap in ((META, meta_cfg.top_k, meta_cfg.symbol_cap),
                             (AGGRESSIVE, meta_cfg.aggressive_top_k, meta_cfg.aggressive_symbol_cap)):
            chosen = choose(k)
            live = p_pos * chosen[day_idx]
            weights = np.minimum((live @ one_hot) / k, cap)
            sleeves[name] = make_sleeve(name, "meta", weights.astype(float))
            if name == META:
                today = chosen[-1]
                for c in np.flatnonzero(today):
                    strategy_name, symbol = columns[trade_cols[c]]
                    selection.append({"strategy": strategy_name, "symbol": symbol,
                                      "score": round(float(score[-1, c]), 3),
                                      "lookback_return_pct": round(100 * float(total[-1, c]), 2),
                                      "lookback_trades": int(n_trades[-1, c]),
                                      "holding": bool(p_pos[-1, c])})
                selection.sort(key=lambda row: -row["score"])
                picks = {}
                for d in range(n_days):
                    picks[day_keys[d]] = [
                        f"{columns[trade_cols[c]][0]} | {columns[trade_cols[c]][1]}" for c in np.flatnonzero(chosen[d])]
                history = pd.Series(picks)

        # consensus: long when enough strategies agree on a symbol
        votes = (p_pos @ one_hot) / np.maximum(one_hot.sum(axis=0), 1)
        agree = votes >= meta_cfg.consensus_threshold
        sleeves[CONSENSUS] = make_sleeve(CONSENSUS, "meta", slot_weights(agree, risk.slots, risk.max_symbol_weight))

        # meta-labeling: an ML filter deciding which hourly-strategy signals to take, and how big
        if meta_cfg.meta_label:
            from .metalabel import meta_label

            by_name = {s.name: s for s in strategies}
            primary = [j for j, (name, _) in enumerate(columns)
                       if by_name[name].timeframe >= 60 and not by_name[name].benchmark]
            labelled = meta_label(pos, columns, col_sym_arr, primary, close_ff, cost_sym, features,
                                  {s: config.asset(s).kind for s in symbols}, days=meta_cfg.meta_label_days)
            if labelled is not None:
                weights, stats = labelled
                sleeve = make_sleeve(META_LABEL, "meta", weights)
                sleeve.description = (
                    "Meta-labeling (Lopez de Prado): a gradient-boosted tree model, retrained daily on past trades "
                    "only, decides which hourly-strategy signals to take and sizes them at half-Kelly (max 2% of "
                    "equity at risk, 25% per position)."
                    + (f" Out of sample: took {stats['taken']} of {stats['signals']} signals; win rate "
                       f"{stats['win_rate_taken']}% vs {stats['win_rate_all']}% for all; average trade "
                       f"{stats['avg_ret_taken_pct']}% vs {stats['avg_ret_all_pct']}%." if stats else ""))
                sleeves[META_LABEL] = sleeve

    for name, weights, text in _daytrade_sleeves(usable, index, symbols, config):
        if weights is not None:
            sleeve = make_sleeve(name, "daytrade", weights)
            sleeve.description = text
            sleeves[name] = sleeve
    rotation = _rotation_sleeve(sleeves, index, meta_cfg)
    if rotation is not None:
        sleeves[ROTATION] = make_sleeve(ROTATION, "meta", rotation)
    for days in meta_cfg.momentum_lookbacks:
        weights = _momentum_sleeve(close_ff, symbols, meta_cfg.momentum_symbols, days, meta_cfg.momentum_top_k)
        if weights is not None:
            sleeves[MOMENTUM.format(days=days)] = make_sleeve(MOMENTUM.format(days=days), "meta", weights)

    last_bar = {s: usable[s].index[-1] for s in symbols}
    return Research(index, symbols, close_ff, last_bar, sleeves, columns, pos, last_reason, selection,
                    history.to_frame("picks") if history is not None else None)


def _daytrade_sleeves(bars, index, symbols, config: Config):
    from . import daytrade

    cfg = config.daytrade
    if not cfg.enabled:
        return []
    out = []
    for signal, long, short in cfg.pairs:
        pair = "/".join(s for s in (long, short) if s)
        out.append((f"Day trade: ORB 5m · {pair}",
                    daytrade.orb_5m(bars, index, symbols, signal, long, short, cfg.orb_target_r),
                    f"Zarattini & Aziz (2023) opening-range breakout: trades the direction of {signal}'s first 5-minute "
                    f"candle ({long} if up, {short} if down), stop at the other end of that candle, target "
                    f"{cfg.orb_target_r:g}R, flat before the close"))
        out.append((f"Day trade: Last half hour · {pair}",
                    daytrade.last_half_hour(bars, index, symbols, signal, long, short),
                    f"Market intraday momentum (Gao, Han, Li & Zhou 2018): at 15:30 buys {long} if {signal} is up "
                    f"since yesterday's close by more than half its usual move ({short} if down); sells at 15:55"))
        out.append((f"Day trade: Open breakout · {pair}",
                    daytrade.open_breakout(bars, index, symbols, signal, long, short),
                    f"Volatility breakout (Larry Williams / Crabel): {long} when {signal} closes a 5-minute bar half "
                    f"of yesterday's range above today's open at a new session high ({short} below); stop at the "
                    "open; flat before the close"))
        out.append((f"Day trade: Noise-area momentum · {pair}",
                    daytrade.noise_area(bars, index, symbols, signal, long, short, cfg.noise_lookback),
                    f"Zarattini, Aziz & Barbon (2024) intraday momentum: every half hour, {long} if {signal} is above "
                    f"its {cfg.noise_lookback}-day 'noise area' around the open, {short} if below; exits through the "
                    "band or VWAP; flat before the close"))
    candidates = [a.symbol for a in config.universe if a.kind == "us_equity" and a.trade_strategies]
    out.append(("Day trade: Stocks in Play ORB",
                daytrade.stocks_in_play(bars, index, symbols, candidates, cfg.sip_top_n, cfg.sip_min_relvol,
                                        cfg.sip_stop_atr),
                f"Zarattini, Barbon & Aziz (2024): each morning buys a break of the opening-range high in the "
                f"{cfg.sip_top_n} stocks with the highest first-5-minute relative volume and a green first candle; "
                f"stop {cfg.sip_stop_atr:.0%} of the daily ATR below; flat before the close"))
    return out


def _momentum_sleeve(close: pd.DataFrame, symbols: list[str], candidates, days: int, top_k: int) -> np.ndarray | None:
    """All-in momentum: at 09:35 New York each weekday (the close of the
    session's first 5-minute bar), hold the ``top_k`` candidates with the
    biggest gain over the previous ``days`` days (only those that are up;
    otherwise cash) until the next morning."""
    cols = [s for s in candidates if s in symbols]
    if not cols or top_k <= 0:
        return None
    index = close.index
    local = index.tz_convert("America/New_York")
    minutes = np.asarray(local.hour * 60 + local.minute)
    # bars are labelled by their start: the 09:30 bar is the one complete at 09:35
    session = (np.asarray(local.dayofweek) < 5) & (minutes >= 9 * 60 + 30) & (minutes < 16 * 60)
    day_keys = np.asarray(local.normalize())
    weights = np.zeros((len(index), len(symbols)))
    position = {s: j for j, s in enumerate(symbols)}
    prices = close[cols]
    starts = []
    for key in pd.unique(day_keys[session]):
        starts.append(int(np.flatnonzero(session & (day_keys == key))[0]))
    for n, t in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(index)
        past = prices.asof(index[t] - pd.Timedelta(days=days))
        if past.isna().all():
            continue
        change = (prices.iloc[t] / past - 1).replace([np.inf, -np.inf], np.nan).dropna()
        winners = change[change > 0].sort_values(ascending=False).head(top_k)
        for symbol in winners.index:
            weights[t:end, position[symbol]] = 1.0 / top_k
    return weights  # all zeros is a real answer (cash): the sleeve must stay so it can sell


def _rotation_sleeve(sleeves: dict[str, SleeveResult], index: pd.DatetimeIndex, meta_cfg) -> np.ndarray | None:
    """Each UTC day, copy the top-k strategy, copy-trading or daily sleeves by
    risk-adjusted return over the previous ``rotation_lookback_days`` days
    (whole sleeves, not strategy/symbol pairs, so far fewer candidates and
    less luck-chasing)."""
    names = [n for n, s in sleeves.items() if s.kind in ("strategy", "copy", "daily", "ai", "daytrade")]
    k, lookback = meta_cfg.rotation_top_k, meta_cfg.rotation_lookback_days
    if len(names) < k or k <= 0:
        return None
    day_idx, _ = pd.factorize(index.normalize(), sort=True)
    returns = pd.DataFrame({n: sleeves[n].returns.to_numpy() for n in names})
    daily = returns.groupby(day_idx).sum()
    mean = daily.rolling(lookback, min_periods=lookback).mean().shift(1)
    std = daily.rolling(lookback, min_periods=lookback).std().shift(1)
    total = daily.rolling(lookback, min_periods=lookback).sum().shift(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        score = (mean / std).where((total > 0) & (std > 0)).to_numpy()
    score = np.where(np.isfinite(score), score, -np.inf)
    top = np.argsort(-score, axis=1)[:, :k]
    chosen = np.zeros_like(score, dtype=bool)
    chosen[np.arange(len(score))[:, None], top] = True
    chosen &= np.isfinite(score)
    weights = np.zeros(sleeves[names[0]].weights.shape)
    bar_choice = chosen[day_idx]
    for j, name in enumerate(names):
        pick = bar_choice[:, j]
        if pick.any():
            weights[pick] += sleeves[name].weights.to_numpy()[pick] / k
    return weights


def leaderboard(research: Research) -> pd.DataFrame:
    rows = []
    for sleeve in research.sleeves.values():
        rows.append({"sleeve": sleeve.name, "kind": sleeve.kind,
                     "style": sleeve.strategy.style if sleeve.strategy else "meta", **sleeve.stats})
    frame = pd.DataFrame(rows)
    return frame.sort_values("return_pct", ascending=False).reset_index(drop=True)
