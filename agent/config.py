"""Configuration: trading universe, costs, risk limits and run mode.

Defaults live here. An optional ``config.toml`` (see ``config.example.toml``)
overrides any field; environment variables override the run mode.
"""
from __future__ import annotations

import dataclasses
import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Asset:
    symbol: str  # Yahoo Finance symbol, e.g. "AAPL", "BTC-USD", "VUSA.L"
    kind: str  # "us_equity" | "crypto" | "uk_equity"
    currency: str  # quote currency after scaling: "USD" | "GBP"
    broker_symbol: str = ""  # Alpaca symbol, e.g. "AAPL" or "BTC/USD"
    trade_strategies: bool = True  # False: only held by copy/benchmark sleeves
    cost_bps: float | None = None  # overrides the per-kind cost

    @property
    def alpaca(self) -> str:
        return self.broker_symbol or self.symbol


def _us(symbol: str) -> Asset:
    return Asset(symbol, "us_equity", "USD", symbol)


def _crypto(symbol: str) -> Asset:
    return Asset(symbol, "crypto", "USD", symbol.replace("-", "/"))


DEFAULT_UNIVERSE: tuple[Asset, ...] = (
    # Broad index / leveraged / inverse ETFs (inverse ETFs let a long-only
    # cash account profit from falls).
    _us("SPY"), _us("QQQ"), _us("IWM"), _us("TQQQ"), _us("SQQQ"), _us("SOXL"),
    # Liquid, volatile large caps.
    _us("NVDA"), _us("TSLA"), _us("AAPL"), _us("MSFT"), _us("AMD"), _us("META"),
    _us("AMZN"), _us("GOOGL"), _us("PLTR"), _us("COIN"),
    # Crypto trades 24/7, so the agent is never idle.
    _crypto("BTC-USD"), _crypto("ETH-USD"), _crypto("SOL-USD"),
    _crypto("XRP-USD"), _crypto("DOGE-USD"),
)

# Funds that copy famous traders, held by "Copy" sleeves only:
# NANC / KRUZ track stock trades disclosed by Democratic / Republican members
# of Congress, GURU holds top hedge-fund 13F picks, ARKK is Cathie Wood's
# flagship fund and BRK-B is Warren Buffett's Berkshire Hathaway.
COPY_ETFS: tuple[Asset, ...] = tuple(
    Asset(symbol, "us_equity", "USD", alpaca, trade_strategies=False)
    for symbol, alpaca in (("NANC", "NANC"), ("KRUZ", "KRUZ"), ("GURU", "GURU"), ("ARKK", "ARKK"), ("BRK-B", "BRK.B")))

DEFAULT_UNIVERSE = DEFAULT_UNIVERSE + COPY_ETFS

UK_ETFS: tuple[Asset, ...] = (
    Asset("ISF.L", "uk_equity", "GBP"), Asset("VUSA.L", "uk_equity", "GBP"),
    Asset("EQQQ.L", "uk_equity", "GBP"),
)

# Regular trading sessions: (timezone, open "HH:MM", close "HH:MM").
SESSIONS = {
    "us_equity": ("America/New_York", "09:30", "16:00"),
    "uk_equity": ("Europe/London", "08:00", "16:30"),
    "crypto": None,  # always open
}

# Round-trip friction per side, in basis points of notional: commission +
# spread + slippage. Alpaca crypto taker fee is 25 bps at the lowest tier.
DEFAULT_COST_BPS = {"us_equity": 5.0, "uk_equity": 10.0, "crypto": 30.0}


@dataclass
class RiskConfig:
    slots: int = 4  # positions per sleeve; each gets 1/slots of equity
    max_symbol_weight: float = 0.35
    rebalance_band: float = 0.05  # ignore weight drifts smaller than this
    min_trade_gbp: float = 1.0
    daily_loss_limit: float = 0.06  # sleeve stops for the day after -6%
    kill_drawdown: float = 0.5  # sleeve disabled after -50% from peak
    flatten_minutes_before_close: int = 10  # day trader: no overnight stock risk
    no_entry_minutes_before_close: int = 30
    no_entry_minutes_after_open: int = 5
    max_bar_age_minutes: int = 20  # older quotes can't drive trades


@dataclass
class MetaConfig:
    lookback_days: int = 10
    top_k: int = 5
    min_trades: int = 3
    symbol_cap: float = 0.4
    aggressive_top_k: int = 2
    aggressive_symbol_cap: float = 1.0
    consensus_threshold: float = 0.34
    rotation_lookback_days: int = 20  # "Agent (rotation)": ranks whole strategy sleeves
    rotation_top_k: int = 3


@dataclass
class KronosConfig:
    enabled: bool = False
    model: str = "NeoQuasar/Kronos-small"
    tokenizer: str = "NeoQuasar/Kronos-Tokenizer-base"
    lookback: int = 400
    pred_len: int = 12
    sample_count: int = 5
    every_minutes: int = 15
    entry_threshold: float = 0.004  # predicted return needed to go long
    max_symbols: int = 21


@dataclass
class CopyConfig:
    """Copy-trading sleeves built from public disclosures (see agent/copytrade.py)."""
    enabled: bool = True
    # 13F filers: name -> SEC CIK. Holdings are public up to 45 days after quarter end.
    managers: dict = field(default_factory=lambda: {
        "Buffett (Berkshire)": "0001067983",
        "Burry (Scion)": "0001649339",
        "Ackman (Pershing Square)": "0001336528",
        "Druckenmiller (Duquesne)": "0001536411",
        "Tepper (Appaloosa)": "0001656456",
        "Cathie Wood (ARK)": "0001697748",
    })
    top_n: int = 10  # largest holdings copied per manager
    stale_days: int = 200  # a manager with no 13F this recent is not copied
    insider_min_value_k: int = 250  # $ thousands: ignore smaller insider purchases
    insider_window_days: int = 10  # hold names bought by insiders in this window
    insider_top_n: int = 8
    cost_bps: float = 15.0  # smaller, less liquid names than the core universe
    refresh_hours_13f: float = 12.0
    refresh_hours_insider: float = 1.0
    sec_user_agent: str = "trader-agent research bot (github.com/ayushganatra3-del/trader)"


@dataclass
class BrokerConfig:
    # "paper" = internal simulation only (default, no account needed)
    # "alpaca-paper" = also mirror the Agent sleeve into an Alpaca paper account
    # "alpaca-live" = REAL MONEY; also needs AGENT_LIVE_CONFIRM=I-ACCEPT-REAL-MONEY-RISK
    mode: str = "paper"
    sleeve: str = "Agent"  # which sleeve the broker account follows
    capital_gbp: float = 100.0  # never deploy more than this, even if the account holds more
    max_orders_per_tick: int = 10
    trade_crypto: bool = True
    trade_stocks: bool = True


@dataclass
class Config:
    universe: tuple[Asset, ...] = DEFAULT_UNIVERSE
    interval: str = "5m"
    history_range: str = "60d"
    starting_capital_gbp: float = 100.0
    gbpusd_fallback: float = 1.34
    cost_bps: dict = field(default_factory=lambda: dict(DEFAULT_COST_BPS))
    risk: RiskConfig = field(default_factory=RiskConfig)
    meta: MetaConfig = field(default_factory=MetaConfig)
    kronos: KronosConfig = field(default_factory=KronosConfig)
    broker: BrokerConfig = field(default_factory=BrokerConfig)
    copy: CopyConfig = field(default_factory=CopyConfig)
    disabled_strategies: tuple[str, ...] = ()

    def cost(self, asset: Asset) -> float:
        """Cost per side as a fraction of notional."""
        bps = asset.cost_bps if asset.cost_bps is not None else self.cost_bps[asset.kind]
        return bps / 1e4

    def asset(self, symbol: str) -> Asset:
        for asset in self.universe:
            if asset.symbol == symbol:
                return asset
        raise KeyError(symbol)

    @property
    def symbols(self) -> list[str]:
        return [asset.symbol for asset in self.universe]


def _merge(obj, overrides: dict):
    changes = {}
    for key, value in overrides.items():
        if not hasattr(obj, key):
            raise ValueError(f"Unknown config key: {key}")
        current = getattr(obj, key)
        if dataclasses.is_dataclass(current) and isinstance(value, dict):
            changes[key] = _merge(current, value)
        elif key == "universe":
            changes[key] = tuple(_parse_asset(item) for item in value)
        elif key == "cost_bps":
            changes[key] = {**current, **value}
        elif isinstance(current, tuple):
            changes[key] = tuple(value)
        else:
            changes[key] = value
    return dataclasses.replace(obj, **changes)


def _parse_asset(item) -> Asset:
    if isinstance(item, str):
        if item.endswith("-USD"):
            return _crypto(item)
        if item.endswith(".L"):
            return Asset(item, "uk_equity", "GBP")
        return _us(item)
    return Asset(**item)


def load_config(path: str | os.PathLike | None = None) -> Config:
    config = Config()
    candidate = Path(path) if path else Path(os.environ.get("AGENT_CONFIG", "config.toml"))
    if candidate.exists():
        with candidate.open("rb") as handle:
            config = _merge(config, tomllib.load(handle))
    mode = os.environ.get("AGENT_MODE")
    if mode:
        config = dataclasses.replace(config, broker=dataclasses.replace(config.broker, mode=mode))
    if os.environ.get("AGENT_KRONOS", "").lower() in ("1", "true", "yes"):
        config = dataclasses.replace(config, kronos=dataclasses.replace(config.kronos, enabled=True))
    if config.broker.mode not in ("paper", "alpaca-paper", "alpaca-live"):
        raise ValueError(f"Unknown broker mode {config.broker.mode!r}")
    return config
