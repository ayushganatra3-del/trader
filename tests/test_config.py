from pathlib import Path

import pytest

from agent.config import load_config

ROOT = Path(__file__).resolve().parents[1]


def test_example_config_loads(monkeypatch):
    monkeypatch.delenv("AGENT_MODE", raising=False)
    config = load_config(ROOT / "config.example.toml")
    assert config.broker.mode == "paper"
    assert config.risk.slots == 4
    assert config.cost_bps["crypto"] == 30.0 and "uk_equity" in config.cost_bps


def test_env_overrides_and_validation(tmp_path, monkeypatch):
    path = tmp_path / "c.toml"
    path.write_text('universe = ["AAPL", "BTC-USD", "VUSA.L"]\n[meta]\ntop_k = 3\n')
    monkeypatch.setenv("AGENT_MODE", "alpaca-paper")
    config = load_config(path)
    assert [a.kind for a in config.universe] == ["us_equity", "crypto", "uk_equity"]
    assert config.asset("BTC-USD").alpaca == "BTC/USD"
    assert config.meta.top_k == 3 and config.broker.mode == "alpaca-paper"
    monkeypatch.setenv("AGENT_MODE", "yolo")
    with pytest.raises(ValueError):
        load_config(path)
    path.write_text("nonsense = 1\n")
    monkeypatch.delenv("AGENT_MODE")
    with pytest.raises(ValueError):
        load_config(path)
