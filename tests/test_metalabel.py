import dataclasses

import numpy as np
import pandas as pd

from agent.config import Config, _crypto, _us
from agent.data import synthetic_bars
from agent.metalabel import _rolling_winrates, trade_events
from agent.research import META_LABEL, run_research
from agent.strategies import all_strategies


def test_trade_events_measure_each_trade_net_of_costs():
    pos = np.array([[0], [1], [1], [0], [1], [1]], dtype=bool)
    close = np.array([[100.0], [100], [105], [110], [110], [99]])
    events = trade_events(pos, close, np.array([0.001]), [0])
    assert list(events["entry"]) == [1, 4] and list(events["exit"]) == [3, -1]
    assert abs(events["ret"].iloc[0] - (1.10 - 1 - 0.002)) < 1e-12
    assert np.isnan(events["ret"].iloc[1])  # still open: no label yet


def test_win_rates_only_use_trades_closed_before_entry():
    events = pd.DataFrame({"col": [0, 0, 0], "entry": [1, 5, 6], "exit": [4, 8, 9], "ret": [0.01, -0.01, 0.02]})
    rates = _rolling_winrates(events, "col", 10)
    assert np.isnan(rates[0]) and rates[1] == 1.0 and rates[2] == 1.0  # the trade closing at 8 is unknown at 6


def small():
    return Config(universe=(_us("SPY"), _us("QQQ"), _us("NVDA"), _us("TSLA"), _crypto("BTC-USD"), _crypto("ETH-USD")))


def test_meta_label_sleeve_never_looks_ahead():
    config = small()
    # score every day in both runs (a "last N days" window would shift with the cut)
    config = dataclasses.replace(config, meta=dataclasses.replace(config.meta, meta_label_days=1000))
    full = synthetic_bars(config, days=30, seed=5, end=pd.Timestamp("2026-02-24T21:00Z"))
    cut = pd.Timestamp("2026-02-19T18:00Z")
    part = {s: f[f.index <= cut] for s, f in full.items()}
    strategies = all_strategies()
    a = run_research(full, config, strategies).sleeves[META_LABEL].weights
    b = run_research(part, config, strategies).sleeves[META_LABEL].weights
    common = b.index[:-1]  # the newest row can change once an exit bar exists
    assert np.allclose(a.loc[common].to_numpy(), b.loc[common].to_numpy())
    assert a.to_numpy().sum() > 0
    assert a.to_numpy().max() <= 0.25 + 1e-9 and a.sum(axis=1).max() <= 1 + 1e-9  # per-position and total caps


def test_meta_label_finds_no_edge_in_a_random_walk():
    config = small()
    bars = synthetic_bars(config, days=40, seed=11, end=pd.Timestamp("2026-02-24T21:00Z"), random_walk=True)
    sleeve = run_research(bars, config, all_strategies()).sleeves.get(META_LABEL)
    assert sleeve is None or sleeve.stats["return_pct"] < 5
