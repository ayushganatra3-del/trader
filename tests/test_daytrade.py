import numpy as np
import pandas as pd
import pytest

from agent import daytrade
from agent.config import Config
from agent.data import synthetic_bars


def session_day(day: str, path, volume=1e5, first_volume=None):
    """One regular session of 5-minute bars following ``path`` (78 closes)."""
    start = pd.Timestamp(f"{day} 09:30", tz="America/New_York")
    index = pd.date_range(start, periods=78, freq="5min").tz_convert("UTC")
    close = np.asarray(path, float)
    open_ = np.r_[close[0] * (1.001 if close[1] < close[0] else 1 / 1.001), close[:-1]]  # first candle follows the path
    vol = np.full(78, volume)
    if first_volume:
        vol[0] = first_volume
    return pd.DataFrame({"open": open_, "high": np.maximum(open_, close) * 1.0005,
                         "low": np.minimum(open_, close) * 0.9995, "close": close, "volume": vol}, index=index)


def days(n, start="2026-02-02"):
    return [d.strftime("%Y-%m-%d") for d in pd.bdate_range(start, periods=n)]


def test_orb_follows_the_first_candle_and_flattens_before_the_close():
    up = session_day("2026-02-02", np.linspace(100, 103, 78))  # green first candle, never stopped
    down = session_day("2026-02-03", np.linspace(103, 100, 78))
    qqq = pd.concat([up, down])
    bars = {"QQQ": qqq, "TQQQ": qqq, "SQQQ": qqq}
    symbols = ["QQQ", "TQQQ", "SQQQ"]
    w = pd.DataFrame(daytrade.orb_5m(bars, qqq.index, symbols, "QQQ", "TQQQ", "SQQQ"), index=qqq.index, columns=symbols)
    local = w.index.tz_convert("America/New_York")
    mon, tue = local.day == 2, local.day == 3
    assert w.loc[mon & (local.hour * 60 + local.minute == 570), "TQQQ"].iloc[0] == 1.0  # from the first candle's close
    assert w.loc[mon & (local.hour * 60 + local.minute >= 950), "TQQQ"].eq(0).all()  # flat from 15:50
    assert w.loc[tue, "TQQQ"].eq(0).all() and w.loc[tue & (local.hour == 11), "SQQQ"].eq(1.0).all()


def test_orb_stop_at_the_first_candle_low():
    path = np.r_[[100.5], [101, 100.2, 99.0], np.full(74, 99.0)]  # green first candle, then breaks its low
    qqq = session_day("2026-02-02", path)
    bars = {"QQQ": qqq, "TQQQ": qqq}
    w = daytrade.orb_5m(bars, qqq.index, ["QQQ", "TQQQ"], "QQQ", "TQQQ", None)
    held = np.flatnonzero(w[:, 1])
    assert held.max() < 4  # stopped out within the first few bars


def test_stocks_in_play_buys_the_high_relative_volume_breakout():
    frames = {"A": [], "B": []}
    for i, day in enumerate(days(16)):
        last = i == 15
        frames["A"].append(session_day(day, np.r_[[100.2], [100.25], np.linspace(100.5, 102, 76)],
                                       first_volume=5e5 if last else 1e5))
        frames["B"].append(session_day(day, np.r_[[100.2], np.linspace(100.3, 101, 77)], first_volume=1e5))
    bars = {s: pd.concat(f) for s, f in frames.items()}
    index = bars["A"].index
    w = pd.DataFrame(daytrade.stocks_in_play(bars, index, ["A", "B"], ["A", "B"], top_n=1, min_relvol=1.5), index=index, columns=["A", "B"])
    last_day = w.index.tz_convert("America/New_York").normalize() == pd.Timestamp(days(16)[-1], tz="America/New_York")
    assert w.loc[last_day, "A"].max() == 1.0 and w.loc[last_day, "B"].eq(0).all()
    assert w.loc[~last_day].to_numpy().sum() == 0  # no relative-volume spike before


def test_noise_area_goes_long_on_a_breakout_and_is_flat_overnight():
    frames = [session_day(day, 100 + 0.2 * np.sin(np.linspace(0, 6, 78))) for day in days(15)]
    frames.append(session_day(days(16)[-1], np.linspace(100, 104, 78)))  # strong trend day
    qqq = pd.concat(frames)
    bars = {"QQQ": qqq, "TQQQ": qqq, "SQQQ": qqq}
    symbols = ["QQQ", "TQQQ", "SQQQ"]
    w = pd.DataFrame(daytrade.noise_area(bars, qqq.index, symbols, "QQQ", "TQQQ", "SQQQ"), index=qqq.index, columns=symbols)
    local = w.index.tz_convert("America/New_York")
    trend = local.normalize() == pd.Timestamp(days(16)[-1], tz="America/New_York")
    minutes = local.hour * 60 + local.minute
    assert w.loc[trend & (minutes == 13 * 60), "TQQQ"].iloc[0] == 1.0
    assert w.loc[trend & (minutes >= 950)].to_numpy().sum() == 0
    assert w.loc[~trend].to_numpy().sum() == 0  # quiet days stay inside the noise area


@pytest.mark.parametrize("builder", ["orb", "sip", "noise"])
def test_day_trade_sleeves_never_look_ahead(builder):
    config = Config()
    full = synthetic_bars(config, days=20, end=pd.Timestamp("2026-02-24T21:00Z"))
    cut = pd.Timestamp("2026-02-20T17:00Z")
    part = {s: f[f.index <= cut] for s, f in full.items()}
    symbols = ["QQQ", "TQQQ", "SQQQ", "NVDA", "TSLA", "AMD", "META"]

    def run(bars):
        index = bars["QQQ"].index
        for s in symbols:
            index = index.union(bars[s].index)
        if builder == "orb":
            return index, daytrade.orb_5m(bars, index, symbols, "QQQ", "TQQQ", "SQQQ")
        if builder == "noise":
            return index, daytrade.noise_area(bars, index, symbols, "QQQ", "TQQQ", "SQQQ")
        return index, daytrade.stocks_in_play(bars, index, symbols, symbols[3:], top_n=2)

    index_full, w_full = run(full)
    index_part, w_part = run(part)
    known = len(index_part) - 1  # the last bar's weight may change once a stop/exit bar exists
    assert np.allclose(w_full[:known], w_part[:known])


def test_open_positions_stay_in_the_latest_target_during_the_session():
    """Live: no exit bar exists yet, so the newest row must still hold the trade."""
    qqq = session_day("2026-02-02", np.linspace(100, 103, 78)).iloc[:20]  # 11:10 New York, still trading
    bars = {"QQQ": qqq, "TQQQ": qqq, "SQQQ": qqq}
    orb = daytrade.orb_5m(bars, qqq.index, ["QQQ", "TQQQ", "SQQQ"], "QQQ", "TQQQ", "SQQQ")
    assert orb[-1, 1] == 1.0

    frames = {"A": [], "B": []}
    for i, day in enumerate(days(16)):
        last = i == 15
        frames["A"].append(session_day(day, np.r_[[100.2], [100.25], np.linspace(100.5, 102, 76)],
                                       first_volume=5e5 if last else 1e5))
        frames["B"].append(session_day(day, np.r_[[100.2], np.linspace(100.3, 101, 77)], first_volume=1e5))
    bars = {s: pd.concat(f).iloc[:-60] for s, f in frames.items()}  # last day cut at 11:00
    sip = daytrade.stocks_in_play(bars, bars["A"].index, ["A", "B"], ["A", "B"], top_n=1, min_relvol=1.5)
    assert sip[-1, 0] == 1.0


def test_rotation_can_pick_day_trade_sleeves():
    from agent.research import ROTATION, run_research
    from agent.strategies import all_strategies

    config = Config()
    research = run_research(synthetic_bars(config, days=6, end=pd.Timestamp("2026-02-24T20:00Z")), config, all_strategies())
    names = list(research.sleeves)
    assert any(n.startswith("Day trade") for n in names)
    assert max(i for i, n in enumerate(names) if n.startswith("Day trade")) < names.index(ROTATION)
