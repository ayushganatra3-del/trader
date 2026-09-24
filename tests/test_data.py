import pandas as pd
import pytest

from agent.config import Config, _crypto, _us
from agent.data import MarketData, merge_bars, parse_yahoo

NOW = pd.Timestamp("2026-09-24 14:00:30", tz="UTC")


def yahoo_payload(times, closes, currency="USD", volume=100):
    return {"chart": {"error": None, "result": [{
        "meta": {"currency": currency, "symbol": "X"},
        "timestamp": times,
        "indicators": {"quote": [{"open": closes, "high": [c and c + 1 for c in closes],
                                  "low": [c and c - 1 for c in closes], "close": closes,
                                  "volume": [volume] * len(closes)}]}}]}}


def test_parse_yahoo_keeps_completed_aligned_bars():
    base = int(pd.Timestamp("2026-09-24 13:30", tz="UTC").timestamp())
    times = [base, base + 300, base + 600, base + 900, base + 1250, base + 1500, base + 1800]
    closes = [100.0, 101.0, None, 102.0, 103.0, 104.0, 105.0]
    frame, currency = parse_yahoo(yahoo_payload(times, closes), "5m", NOW)
    # None row dropped (one bad bar must not discard the symbol), irregular
    # 1250s row dropped, and the 14:00 bar is still forming at 14:00:30
    assert list(frame["close"]) == [100.0, 101.0, 102.0, 104.0]
    assert frame.index[0] == pd.Timestamp("2026-09-24 13:30", tz="UTC")
    assert currency == "USD"


def test_parse_yahoo_converts_pence():
    base = int(pd.Timestamp("2026-09-24 08:00", tz="UTC").timestamp())
    frame, currency = parse_yahoo(yahoo_payload([base], [5000.0], currency="GBp"), "5m", NOW)
    assert frame["close"].iloc[0] == pytest.approx(50.0)
    assert currency == "GBP"


def test_merge_bars_prefers_new_rows():
    idx = pd.date_range("2026-09-24 13:30", periods=3, freq="5min", tz="UTC")
    old = pd.DataFrame({"open": 1.0, "high": 1.0, "low": 1.0, "close": [1.0, 2.0, 3.0], "volume": 1.0}, index=idx)
    new = pd.DataFrame({"open": 1.0, "high": 1.0, "low": 1.0, "close": [9.0, 4.0], "volume": 1.0}, index=idx[2:].append(idx[2:] + pd.Timedelta(minutes=5)))
    merged = merge_bars(old, new)
    assert list(merged["close"]) == [1.0, 2.0, 9.0, 4.0]


def test_market_data_cache_and_fallback_errors(tmp_path):
    config = Config(universe=(_us("AAPL"), _crypto("BTC-USD")))
    idx = pd.date_range("2026-09-24 13:30", periods=4, freq="5min", tz="UTC")
    bars = pd.DataFrame({"open": 1.0, "high": 2.0, "low": 0.5, "close": [1.0, 1.1, 1.2, 1.3], "volume": 5.0}, index=idx)

    def fetcher(symbol, interval, range_, now=None):
        if symbol == "AAPL":
            return bars
        if symbol == "GBPUSD=X":
            return bars.assign(close=1.25)
        raise RuntimeError("boom")

    market = MarketData(config, tmp_path, fetcher=fetcher)
    errors = market.refresh(NOW)
    assert "BTC-USD" in errors and "AAPL" not in errors
    assert market.fx_to_gbp("USD") == pytest.approx(0.8)
    reloaded = MarketData(config, tmp_path, fetcher=fetcher)
    assert list(reloaded.bars["AAPL"]["close"]) == [1.0, 1.1, 1.2, 1.3]


def test_refresh_only_fetches_when_a_new_bar_is_due(tmp_path):
    config = Config(universe=(_crypto("BTC-USD"),))
    calls = []
    idx = pd.date_range("2026-09-24 13:00", "2026-09-24 13:55", freq="5min", tz="UTC")
    bars = pd.DataFrame({"open": 1.0, "high": 2.0, "low": 0.5, "close": 1.0, "volume": 5.0}, index=idx)

    def fetcher(symbol, interval, range_, now=None):
        calls.append((symbol, range_))
        return bars[bars.index + pd.Timedelta(minutes=5) <= now]

    market = MarketData(config, None, fetcher=fetcher)
    market.refresh(pd.Timestamp("2026-09-24 14:00:10", tz="UTC"))
    assert calls[0] == ("BTC-USD", "60d")
    calls.clear()
    market.refresh(pd.Timestamp("2026-09-24 14:01:10", tz="UTC"))  # 14:00 bar not finished
    assert [c for c in calls if c[0] == "BTC-USD"] == []
    market.refresh(pd.Timestamp("2026-09-24 14:05:10", tz="UTC"))
    assert ("BTC-USD", "1d") in calls
