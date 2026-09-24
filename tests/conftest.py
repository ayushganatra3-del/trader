import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent.config import Config, _crypto, _us  # noqa: E402
from agent.data import synthetic_bars  # noqa: E402

END = pd.Timestamp("2026-09-24 19:00", tz="UTC")  # a Thursday, US market open


@pytest.fixture
def small_config():
    return Config(universe=(_us("SPY"), _us("NVDA"), _crypto("BTC-USD"), _crypto("ETH-USD")))


@pytest.fixture
def small_bars(small_config):
    return synthetic_bars(small_config, days=15, seed=3, end=END)
