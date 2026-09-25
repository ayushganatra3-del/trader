"""Meta-labeling: a machine-learning filter on top of proven signals.

From Lopez de Prado, *Advances in Financial Machine Learning* (2018), ch. 3.
A primary rule decides the side: here the hourly strategies, which are the
ones that survive costs. A secondary model then learns which of those
signals tend to win. Every past trade is labelled by its real outcome (its
own stop, target, time limit and exit rule act as the "triple barrier",
costs included). A gradient-boosted tree classifier is retrained each day,
walk-forward, only on trades that had already closed before that day
(purged), then scores that day's new signals. Signals with no edge are
skipped. The rest are sized at half-Kelly, with at most 2% of equity at risk
and 25% of equity per position.
"""
from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from .indicators import Features

log = logging.getLogger(__name__)

FEATURES = ["strategy", "crypto", "atr_pct", "rsi", "dist_ema", "ret_1h", "ret_day", "vol_ratio", "bb_pos",
            "hour", "weekday", "mkt_qqq", "mkt_btc", "pair_winrate", "strategy_winrate"]


def symbol_features(f: Features, index: pd.DatetimeIndex) -> pd.DataFrame:
    """Per-bar features for one symbol, known at each bar's close, on the research index."""
    atr = f.atr(14).replace(0, np.nan)
    lower, _, upper = f.bollinger(20, 2.0)
    frame = pd.DataFrame({
        "atr_pct": atr / f.close,
        "rsi": f.rsi(14),
        "dist_ema": (f.close - f.ema(50)) / atr,
        "ret_1h": f.roc(12),
        "ret_day": f.roc(78),
        "vol_ratio": f.volume_ratio(20),
        "bb_pos": (f.close - lower) / (upper - lower).replace(0, np.nan),
    }, index=f.index)
    return frame.reindex(index).ffill()


def trade_events(pos: np.ndarray, close: np.ndarray, cost: np.ndarray, cols: list[int]) -> pd.DataFrame:
    """Every trade of the given (strategy, symbol) columns: entry bar, exit bar (-1 while open) and
    net return (entry and exit at bar closes, costs on both sides)."""
    rows = []
    for j in cols:
        p = pos[:, j].astype(np.int8)
        change = np.diff(np.r_[0, p])
        entries, exits = np.flatnonzero(change == 1), np.flatnonzero(change == -1)
        for t0 in entries:
            later = exits[exits > t0]
            t1 = int(later[0]) if len(later) else -1
            ret = close[t1, j] / close[t0, j] - 1 - 2 * cost[j] if t1 >= 0 else np.nan
            rows.append((j, int(t0), t1, ret))
    return pd.DataFrame(rows, columns=["col", "entry", "exit", "ret"])


def _rolling_winrates(events: pd.DataFrame, key: str, n: int) -> np.ndarray:
    """Win rate of the last ``n`` trades of the same ``key`` that had closed before each entry."""
    out = np.full(len(events), np.nan)
    for _, group in events.groupby(key):
        closed = group[group["exit"] >= 0].sort_values("exit")
        exits, wins = closed["exit"].to_numpy(), (closed["ret"] > 0).to_numpy()
        for i, t0 in zip(group.index, group["entry"]):
            k = np.searchsorted(exits, t0, side="right")  # trades closed at or before this entry bar
            if k:
                out[events.index.get_loc(i)] = wins[max(0, k - n):k].mean()
    return out


def _payoffs(train: pd.DataFrame, min_trades: int = 20) -> dict:
    """(average win, average loss) per strategy from closed training trades; ``None`` = all strategies."""
    def pair(frame):
        wins, losses = frame.loc[frame["ret"] > 0, "ret"], -frame.loc[frame["ret"] <= 0, "ret"]
        if wins.empty or losses.empty:
            return None
        return max(float(wins.mean()), 1e-4), max(float(losses.mean()), 1e-4)

    out = {None: pair(train) or (1e-3, 1e-3)}
    for strategy, group in train.groupby("strategy"):
        if len(group) >= min_trades and (value := pair(group)):
            out[strategy] = value
    return out


def meta_label(pos: np.ndarray, columns: list[tuple[str, str]], col_sym: np.ndarray, primary: list[int],
               close_ff: pd.DataFrame, cost_sym: np.ndarray, features: dict[str, Features], kinds: dict[str, str],
               days: int = 25, min_train: int = 150, cap: float = 0.25, max_risk: float = 0.02,
               min_prob: float = 0.5) -> tuple[np.ndarray, dict] | None:
    try:
        from sklearn.ensemble import HistGradientBoostingClassifier
    except ImportError:
        log.warning("scikit-learn not installed: meta-labeling sleeve skipped")
        return None
    if not primary:
        return None
    index, symbols = close_ff.index, list(close_ff.columns)
    close = close_ff.to_numpy()[:, col_sym]
    cost = cost_sym[col_sym]
    events = trade_events(pos, close, cost, primary)
    if len(events) < min_train:
        return None
    strategies = sorted({columns[j][0] for j in primary})
    events["strategy"] = [strategies.index(columns[j][0]) for j in events["col"]]
    events["symbol"] = [symbols[col_sym[j]] for j in events["col"]]
    events["crypto"] = [float(kinds.get(s) == "crypto") for s in events["symbol"]]
    events["pair_winrate"] = _rolling_winrates(events, "col", 10)
    events["strategy_winrate"] = _rolling_winrates(events, "strategy", 30)
    columns_f = ["atr_pct", "rsi", "dist_ema", "ret_1h", "ret_day", "vol_ratio", "bb_pos"]
    values = np.full((len(events), len(columns_f)), np.nan)
    for s, group in events.groupby("symbol"):
        if s in features:
            table = symbol_features(features[s], index).to_numpy()
            values[events.index.get_indexer(group.index)] = table[group["entry"].to_numpy()]
    events[columns_f] = values
    stamps = index[events["entry"].to_numpy()]
    events["hour"], events["weekday"] = stamps.hour, stamps.dayofweek
    market = {}
    for key, symbol, bars in (("mkt_qqq", "QQQ", 78), ("mkt_btc", "BTC-USD", 288)):
        series = close_ff[symbol] / close_ff[symbol].shift(bars) - 1 if symbol in close_ff else pd.Series(np.nan, index=index)
        market[key] = series.to_numpy()[events["entry"].to_numpy()]
    events = events.assign(**market)
    events["day"] = stamps.normalize()
    events["exit_time"] = [index[t] if t >= 0 else pd.NaT for t in events["exit"]]

    weights = np.zeros((len(index), len(symbols)))
    scored = []
    for day in sorted(events["day"].unique())[-days:]:
        train = events[(events["exit"] >= 0) & (events["exit_time"] < day)]
        today = events[events["day"] == day]
        labels = (train["ret"] > 0).astype(int)
        if len(train) < min_train or labels.nunique() < 2 or today.empty:
            continue
        model = HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=150, min_samples_leaf=20,
                                               l2_regularization=1.0, random_state=0)
        usable = [c for c in FEATURES if np.isfinite(train[c].to_numpy(dtype=float)).any()]  # e.g. no QQQ data
        model.fit(train[usable].to_numpy(dtype=float), labels.to_numpy())
        prob = model.predict_proba(today[usable].to_numpy(dtype=float))[:, 1]
        payoffs = _payoffs(train)
        for (i, row), p in zip(today.iterrows(), prob):
            # each strategy's own win/loss sizes: a likely-but-tiny win is not worth a big bet
            avg_win, avg_loss = payoffs.get(row["strategy"], payoffs[None])
            kelly = p - (1 - p) * avg_loss / avg_win  # fraction of risk capital (Kelly for a win/lose bet)
            size = min(cap, max_risk / avg_loss, 0.5 * kelly / avg_loss) if p >= min_prob and kelly > 0 else 0.0
            scored.append((p, size > 0, row["ret"]))
            if size <= 0:
                continue
            t0, t1 = int(row["entry"]), int(row["exit"])
            weights[t0:(t1 if t1 >= 0 else len(index)), col_sym[int(row["col"])]] += size
    total = weights.sum(axis=1, keepdims=True)
    weights = np.where(total > 1.0, weights / np.maximum(total, 1e-12), weights)
    stats = {}
    if scored:
        frame = pd.DataFrame(scored, columns=["p", "taken", "ret"]).dropna()
        taken = frame[frame["taken"]]
        stats = {"signals": len(frame), "taken": len(taken),
                 "win_rate_all": round(100 * float((frame["ret"] > 0).mean()), 1) if len(frame) else None,
                 "win_rate_taken": round(100 * float((taken["ret"] > 0).mean()), 1) if len(taken) else None,
                 "avg_ret_all_pct": round(100 * float(frame["ret"].mean()), 3) if len(frame) else None,
                 "avg_ret_taken_pct": round(100 * float(taken["ret"].mean()), 3) if len(taken) else None}
    return weights, stats
