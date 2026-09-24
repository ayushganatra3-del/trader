import math

import numpy as np
import pandas as pd
import pytest

from agent.config import KronosConfig
from agent.kronos import (
    KronosForecaster,
    KronosUnavailable,
    forecasts_as_series,
    kronos_available,
    update_forecasts,
)
from agent.kronos import forecaster as forecaster_module

NOW = pd.Timestamp("2026-09-24 15:00", tz="UTC")


def make_bars(n=120, end=NOW, minutes=5, seed=0, start_price=100.0):
    rng = np.random.default_rng(seed)
    index = pd.date_range(end=end, periods=n, freq=f"{minutes}min", tz="UTC")
    close = start_price * np.exp(np.cumsum(rng.normal(0, 0.002, n)))
    open_ = np.concatenate([[start_price], close[:-1]])
    high = np.maximum(open_, close) * (1 + rng.uniform(0, 0.001, n))
    low = np.minimum(open_, close) * (1 - rng.uniform(0, 0.001, n))
    volume = rng.uniform(1_000, 5_000, n)
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=index)


class FakeForecaster:
    """Records calls; returns a fixed value or raises for chosen symbols."""

    def __init__(self, value=0.01, fail=(), clock=None, cost=0.0):
        self.value = value
        self.fail = set(fail)
        self.calls = []
        self.clock = clock
        self.cost = cost

    def expected_return(self, bars, bar_minutes=5):
        symbol = bars.attrs.get("symbol")
        self.calls.append((symbol, bars.index[-1], bar_minutes))
        if self.clock is not None:
            self.clock.advance(self.cost)
        if symbol in self.fail:
            raise RuntimeError(f"boom {symbol}")
        return self.value


class FakeClock:
    def __init__(self):
        self.now = 0.0

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


def bars_for(symbols, end=NOW, n=120):
    out = {}
    for i, symbol in enumerate(symbols):
        bars = make_bars(n=n, end=end, seed=i)
        bars.attrs["symbol"] = symbol
        out[symbol] = bars
    return out


def cfg(**overrides):
    return KronosConfig(**overrides)


def test_first_run_forecasts_every_symbol_with_iso_keys():
    store = {}
    fake = FakeForecaster(value=0.0123)
    update_forecasts(store, bars_for(["AAA", "BBB"]), cfg(), NOW, forecaster=fake)
    assert set(store) == {"AAA", "BBB"}
    assert store["AAA"] == {"2026-09-24T15:00:00+00:00": 0.0123}
    assert [call[2] for call in fake.calls] == [5, 5]  # bar size inferred from the index


def test_throttled_by_every_minutes():
    store = {}
    fake = FakeForecaster()
    config = cfg(every_minutes=15)
    update_forecasts(store, bars_for(["AAA"], end=NOW), config, NOW, forecaster=fake)
    assert len(fake.calls) == 1

    # 10 minutes of new bars: not due yet.
    later = NOW + pd.Timedelta(minutes=10)
    update_forecasts(store, bars_for(["AAA"], end=later), config, later, forecaster=fake)
    assert len(fake.calls) == 1

    # 15 minutes after the last forecast's bar: due.
    later = NOW + pd.Timedelta(minutes=15)
    update_forecasts(store, bars_for(["AAA"], end=later), config, later, forecaster=fake)
    assert len(fake.calls) == 2
    assert sorted(store["AAA"]) == ["2026-09-24T15:00:00+00:00", "2026-09-24T15:15:00+00:00"]


def test_ignores_bars_after_now():
    store = {}
    fake = FakeForecaster()
    bars = bars_for(["AAA"], end=NOW + pd.Timedelta(hours=1))
    update_forecasts(store, bars, cfg(), NOW, forecaster=fake)
    assert fake.calls[0][1] == NOW
    assert list(store["AAA"]) == [NOW.isoformat()]


def test_time_budget_stops_and_stalest_go_first(monkeypatch):
    clock = FakeClock()
    monkeypatch.setattr(forecaster_module, "_clock", clock)
    symbols = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    earlier = NOW - pd.Timedelta(hours=1)
    store = {
        "AAA": {(earlier + pd.Timedelta(minutes=30)).isoformat(): 0.0},  # newest forecast
        "BBB": {earlier.isoformat(): 0.0},  # oldest forecast
        "CCC": {(earlier + pd.Timedelta(minutes=10)).isoformat(): 0.0},
        # DDD and EEE have never been forecast.
    }
    fake = FakeForecaster(clock=clock, cost=10.0)
    update_forecasts(store, bars_for(symbols), cfg(), NOW, forecaster=fake, time_budget_s=25)
    # Budget is checked before each forecast: t=0, 10, 20 run; t=30 stops.
    assert [call[0] for call in fake.calls] == ["DDD", "EEE", "BBB"]
    assert NOW.isoformat() not in store["AAA"] and NOW.isoformat() not in store["CCC"]

    # The next call picks up where the last one stopped.
    fake.calls.clear()
    update_forecasts(store, bars_for(symbols), cfg(), NOW, forecaster=fake, time_budget_s=25)
    assert [call[0] for call in fake.calls] == ["CCC", "AAA"]


def test_errors_are_isolated_per_symbol(caplog):
    store = {}
    fake = FakeForecaster(value=0.02, fail={"BBB"})
    with caplog.at_level("WARNING"):
        update_forecasts(store, bars_for(["AAA", "BBB", "CCC"]), cfg(), NOW, forecaster=fake)
    assert set(store) == {"AAA", "CCC"}
    assert len(fake.calls) == 3
    assert "BBB" in caplog.text


def test_non_finite_forecast_not_stored():
    store = {}
    update_forecasts(store, bars_for(["AAA"]), cfg(), NOW, forecaster=FakeForecaster(value=float("nan")))
    assert store == {}


def test_model_load_failure_stops_the_run():
    class Unavailable(FakeForecaster):
        def expected_return(self, bars, bar_minutes=5):
            self.calls.append(bars.attrs.get("symbol"))
            raise KronosUnavailable("no weights")

    fake = Unavailable()
    store = {}
    update_forecasts(store, bars_for(["AAA", "BBB", "CCC"]), cfg(), NOW, forecaster=fake)
    assert fake.calls == ["AAA"]
    assert store == {}


def test_trims_entries_older_than_ten_days():
    old = (NOW - pd.Timedelta(days=11)).isoformat()
    recent = (NOW - pd.Timedelta(days=9)).isoformat()
    store = {
        "AAA": {old: 0.01, recent: 0.02},
        "ZZZ": {old: 0.03},  # no bars any more: still trimmed, and dropped once empty
    }
    # No bars passed, so only trimming happens.
    update_forecasts(store, {}, cfg(), NOW, forecaster=FakeForecaster())
    assert store == {"AAA": {recent: 0.02}}


def test_open_symbols_filter_and_max_symbols():
    fake = FakeForecaster()
    store = {}
    update_forecasts(store, bars_for(["AAA", "BBB", "CCC"]), cfg(), NOW, forecaster=fake,
                     open_symbols={"BBB", "CCC"})
    assert set(store) == {"BBB", "CCC"}

    fake = FakeForecaster()
    store = {}
    update_forecasts(store, bars_for(["AAA", "BBB", "CCC"]), cfg(max_symbols=2), NOW, forecaster=fake)
    assert set(store) == {"AAA", "BBB"}


def test_accepts_full_config_and_naive_now():
    from agent.config import Config

    store = {}
    update_forecasts(store, bars_for(["AAA"]), Config(), NOW.tz_localize(None), forecaster=FakeForecaster())
    assert list(store["AAA"]) == [NOW.isoformat()]


def test_forecasts_as_series_round_trip_sorted_utc():
    store = {
        "AAA": {
            "2026-09-24T15:10:00+00:00": 0.3,
            "2026-09-24T15:00:00+00:00": 0.1,
            "2026-09-24T11:05:00-04:00": 0.2,  # 15:05 UTC
        },
        "BBB": {"2026-09-24T15:00:00": -0.01},  # naive keys are UTC
    }
    series = forecasts_as_series(store)
    aaa = series["AAA"]
    assert str(aaa.index.tz) == "UTC"
    assert aaa.index.is_monotonic_increasing
    assert list(aaa.values) == [0.1, 0.2, 0.3]
    assert aaa.index[1] == pd.Timestamp("2026-09-24 15:05", tz="UTC")
    assert aaa.dtype == float
    assert series["BBB"].index[0] == NOW


def test_store_is_json_serialisable():
    import json

    store = {}
    update_forecasts(store, bars_for(["AAA"]), cfg(), NOW, forecaster=FakeForecaster(value=np.float32(0.5)))
    assert json.loads(json.dumps(store)) == store


def test_expected_return_with_injected_predictor_builds_timestamps():
    captured = {}

    class Predictor:
        def predict(self, df, x_timestamp, y_timestamp, pred_len, T, top_k, top_p, sample_count, verbose):
            captured.update(df=df, x=x_timestamp, y=y_timestamp, pred_len=pred_len, T=T, top_p=top_p,
                            sample_count=sample_count, verbose=verbose)
            close = df["close"].iloc[-1] * 1.01
            return pd.DataFrame({"close": [close] * pred_len}, index=y_timestamp)

    config = cfg(lookback=100, pred_len=6, sample_count=3)
    bars = make_bars(n=150)
    result = KronosForecaster(config, predictor=Predictor()).expected_return(bars, bar_minutes=5)
    assert result == pytest.approx(0.01)
    assert len(captured["df"]) == 100
    assert list(captured["df"].columns) == ["open", "high", "low", "close", "volume", "amount"]
    assert np.allclose(captured["df"]["amount"], captured["df"]["close"] * captured["df"]["volume"])
    assert captured["x"].dt.tz is None and captured["x"].iloc[-1] == NOW.tz_localize(None)
    assert list(captured["y"]) == [NOW.tz_localize(None) + pd.Timedelta(minutes=5 * k) for k in range(1, 7)]
    assert (captured["pred_len"], captured["T"], captured["top_p"], captured["sample_count"], captured["verbose"]) == (
        6, 1.0, 0.9, 3, False)


def test_expected_return_needs_64_bars():
    forecaster = KronosForecaster(cfg(), predictor=object())
    with pytest.raises(ValueError):
        forecaster.expected_return(make_bars(n=63))


@pytest.mark.skipif(not kronos_available(), reason="torch/einops/huggingface_hub/safetensors not installed")
def test_real_kronos_tiny_random_model():
    import torch

    from agent.kronos.model import Kronos, KronosPredictor, KronosTokenizer

    torch.manual_seed(0)
    tokenizer = KronosTokenizer(
        d_in=6, d_model=32, n_heads=4, ff_dim=64, n_enc_layers=2, n_dec_layers=2,
        ffn_dropout_p=0.0, attn_dropout_p=0.0, resid_dropout_p=0.0,
        s1_bits=4, s2_bits=4, beta=0.05, gamma0=1.0, gamma=1.1, zeta=0.05, group_size=4,
    ).eval()
    model = Kronos(
        s1_bits=4, s2_bits=4, n_layers=2, d_model=32, n_heads=4, ff_dim=64,
        ffn_dropout_p=0.0, attn_dropout_p=0.0, resid_dropout_p=0.0, token_dropout_p=0.0, learn_te=True,
    ).eval()
    predictor = KronosPredictor(model, tokenizer, device="cpu", max_context=512)
    config = cfg(lookback=128, pred_len=4, sample_count=2)
    forecaster = KronosForecaster(config, predictor=predictor)

    result = forecaster.expected_return(make_bars(n=200), bar_minutes=5)
    assert isinstance(result, float) and math.isfinite(result)

    # And through update_forecasts.
    store = update_forecasts({}, bars_for(["AAA"]), config, NOW, forecaster=forecaster)
    assert math.isfinite(store["AAA"][NOW.isoformat()])
