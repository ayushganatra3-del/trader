import numpy as np
import pandas as pd
import pytest

from agent.config import Config
from agent.data import synthetic_bars
from agent.indicators import Features
from agent.research import AGGRESSIVE, CONSENSUS, META, ROTATION, leaderboard, run_positions, run_research
from agent.sessions import session_frame
from agent.strategies import BENCHMARKS, STRATEGIES, all_strategies

from conftest import END


def test_every_strategy_is_causal(small_config, small_bars):
    """Signals up to bar t must not change when later bars are added."""
    for symbol in ("NVDA", "BTC-USD"):
        bars = small_bars[symbol]
        cut = len(bars) - 137
        kind = small_config.asset(symbol).kind
        full, part = Features(bars, kind), Features(bars.iloc[:cut], kind)
        for strategy in STRATEGIES:
            if kind not in strategy.kinds:
                continue
            e_full, x_full = strategy.fn(full)
            e_part, x_part = strategy.fn(part)
            assert (e_full.iloc[:cut].fillna(False).astype(bool) == e_part.fillna(False).astype(bool)).all(), strategy.name
            assert (x_full.iloc[:cut].fillna(False).astype(bool) == x_part.fillna(False).astype(bool)).all(), strategy.name


def test_research_weights_are_causal(small_config, small_bars):
    cut_time = END - pd.Timedelta(hours=30)
    partial = {s: b[b.index < cut_time] for s, b in small_bars.items()}
    full = run_research(small_bars, small_config, all_strategies())
    part = run_research(partial, small_config, all_strategies())
    for name, sleeve in part.sleeves.items():
        a = full.sleeves[name].weights.loc[: part.index[-1]]
        assert np.allclose(a.to_numpy(), sleeve.weights.to_numpy(), atol=1e-6), name


def test_no_edge_on_a_pure_random_walk():
    """If there were look-ahead bias the meta agent would 'profit' here."""
    config = Config()
    bars = synthetic_bars(config, days=40, seed=1, end=END, random_walk=True)
    board = leaderboard(run_research(bars, config, all_strategies())).set_index("sleeve")
    for name in (META, AGGRESSIVE, CONSENSUS, ROTATION):
        assert board.loc[name, "return_pct"] < 10, name
    strategies = board[board["kind"] == "strategy"]
    assert (strategies["return_pct"] < 15).all()


def test_intraday_stock_positions_are_flat_overnight(small_config, small_bars):
    research = run_research(small_bars, small_config, all_strategies())
    sess = session_frame(small_bars["NVDA"].index, "us_equity")
    last_bars = sess.groupby("session")["to_close"].idxmin()
    last_bars = last_bars[sess.loc[last_bars, "to_close"].to_numpy() <= 0]  # completed sessions only
    assert len(last_bars) >= 5
    swing_overnight = 0
    for name, sleeve in research.sleeves.items():
        if sleeve.kind != "strategy":
            continue
        held = sleeve.weights.loc[last_bars, "NVDA"]
        if sleeve.strategy.intraday:
            assert (held == 0).all(), name
        else:
            swing_overnight += int((held > 0).sum())
    assert swing_overnight > 0  # hourly swing sleeves are allowed to carry positions


def test_sleeve_weights_respect_limits(small_config, small_bars):
    research = run_research(small_bars, small_config, all_strategies())
    for name, sleeve in research.sleeves.items():
        total = sleeve.weights.sum(axis=1)
        assert (total <= 1 + 1e-6).all(), name
        if sleeve.kind == "strategy":
            assert (sleeve.weights.max(axis=1) <= small_config.risk.max_symbol_weight + 1e-6).all()


def test_meta_selection_uses_only_past_days(small_config, small_bars):
    research = run_research(small_bars, small_config, all_strategies())
    history = research.selection_history["picks"]
    first_day = research.index[0].normalize()
    lookback = small_config.meta.lookback_days
    for day, picks in history.items():
        if day < first_day + pd.Timedelta(days=lookback):
            assert picks == [], day


def test_benchmarks_hold_their_symbol(small_config, small_bars):
    research = run_research(small_bars, small_config, all_strategies())
    spy = research.sleeves["Hold SPY"].weights
    assert spy["SPY"].iloc[-1] == pytest.approx(1.0)
    assert spy.drop(columns="SPY").to_numpy().sum() == 0
    expected = {b.name for b in BENCHMARKS if set(b.params["symbols"]) <= set(small_config.symbols)}
    assert expected and expected <= set(research.sleeves)


def _engine(close, entries, exits=None, stop=np.nan, take=np.nan, trail=np.nan, limit=np.nan, flat=None, noent=None, atr=1.0):
    close = np.asarray(close, float)[:, None]
    steps = len(close)
    as_col = lambda values: np.asarray(values, bool)[:, None]
    return run_positions(
        as_col(entries), as_col(exits if exits is not None else [False] * steps), close, np.full_like(close, atr),
        as_col(flat if flat is not None else [False] * steps), as_col(noent if noent is not None else [False] * steps),
        np.array([stop]), np.array([take]), np.array([trail]), np.array([limit]))[0][:, 0]


def test_stop_loss_and_take_profit():
    pos = _engine([10, 10, 9.5, 8.9, 9, 9], [True, False, False, False, False, False], stop=1.0)
    assert pos.tolist() == [True, True, True, False, False, False]
    pos = _engine([10, 11, 12.1, 12], [True, False, False, False], take=2.0)
    assert pos.tolist() == [True, True, False, False]


def test_trailing_stop_ratchets_up():
    pos = _engine([10, 12, 14, 13.5, 12.9], [True] + [False] * 4, trail=1.0)
    # stop trails to 13 after the 14 close, so 12.9 exits
    assert pos.tolist() == [True, True, True, True, False]


def test_time_stop_flatten_and_no_entry():
    assert _engine([1] * 5, [True] + [False] * 4, limit=2).tolist() == [True, True, False, False, False]
    assert _engine([1] * 3, [True, True, True], flat=[False, True, False]).tolist() == [True, False, True]
    assert _engine([1] * 3, [True, True, False], noent=[True, False, False]).tolist() == [False, True, True]


def test_missing_bars_do_not_trade():
    pos = _engine([10, np.nan, np.nan, 10], [False, True, True, False])
    assert pos.tolist() == [False, False, False, False]


def test_hourly_signals_only_fire_when_the_hour_completes(small_config, small_bars):
    swing = next(s for s in STRATEGIES if s.timeframe == 60 and s.family == "ema_cross")
    f = Features(small_bars["BTC-USD"], "crypto")
    entry, exit_ = swing.fn(f)
    fired = entry[entry].index.append(exit_[exit_].index)
    assert len(fired) > 0
    # the 5-minute bar that completes an hour starts at :55
    assert set(fired.minute) == {55}


def test_rotation_waits_for_its_lookback(small_config, small_bars):
    research = run_research(small_bars, small_config, all_strategies())
    weights = research.sleeves[ROTATION].weights
    lookback = small_config.meta.rotation_lookback_days
    first_day = research.index[0].normalize()
    early = weights[weights.index < first_day + pd.Timedelta(days=min(lookback, 14))]
    assert early.to_numpy().sum() == 0
    assert (weights.sum(axis=1) <= 1 + 1e-9).all()


def test_by_day_table_starts_each_day_from_capital():
    import pandas as pd
    from agent.__main__ import by_day
    from agent.config import Config
    from agent.data import synthetic_bars
    from agent.research import run_research
    from agent.strategies import all_strategies

    config = Config()
    research = run_research(synthetic_bars(config, days=4, end=pd.Timestamp("2026-02-24T15:00Z")), config, all_strategies())
    table = by_day(research, 100.0, 2)
    assert list(table.columns)[-1].endswith("(so far)") and len(table.columns) == 2
    sleeve = research.sleeves["Hold SPY"].returns
    day = sleeve[sleeve.index.normalize() == pd.Timestamp("2026-02-23", tz="UTC")]
    assert abs(table.loc["Hold SPY"].iloc[0] - round(100 * (1 + day).prod(), 2)) < 0.011
