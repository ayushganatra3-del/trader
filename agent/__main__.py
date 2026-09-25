"""Command line: ``python -m agent {backtest,tick,run,doctor}``."""
from __future__ import annotations

import argparse
import dataclasses
import json
import logging
import sys
from pathlib import Path

import pandas as pd

from .config import load_config
from .data import MarketData, StaticData, synthetic_bars
from .engine import Engine
from .research import leaderboard, run_research
from .strategies import all_strategies


def _market(args, config):
    if getattr(args, "synthetic", False):
        return StaticData(config, synthetic_bars(config, days=args.days, seed=args.seed), gbpusd=config.gbpusd_fallback)
    return MarketData(config, args.cache_dir)


def _copy_books(config, market):
    """Fetch copy-trading books and widen the universe to their tickers."""
    from .copytrade import CopyManager

    manager = CopyManager(config)
    books = manager.refresh({}, pd.Timestamp.now(tz="UTC"))
    for book in books:
        status = book.error or f"{len(book.current())} holdings"
        print(f"copy book {book.name:<34} as of {book.as_of or '—':<10} {status}", file=sys.stderr)
    config = dataclasses.replace(config, universe=config.universe + tuple(manager.assets(books)))
    market.set_universe(config)
    return config, books


def _daily_books(config, cache_dir):
    """Daily-bar sleeves (market timing, swing setups) and the market regime."""
    from .daily import DailyData, daily_books, daily_symbols

    daily = DailyData(daily_symbols(config), Path(cache_dir) / "daily" if cache_dir else None,
                      config.daily.history, config.daily.refresh_hours)
    error = daily.refresh(pd.Timestamp.now(tz="UTC"))
    if error:
        print(f"daily bars: {error}", file=sys.stderr)
    books, regime = daily_books(daily.bars, config, daily.fetched_at)
    if regime:
        print(f"market regime ({regime['index']}, {regime['session']}): {regime['state']} since {regime['since']}, "
              f"level {regime['level']}, "
              f"{regime['distribution_days']} distribution days, exposure {regime['exposure']:.0%}, "
              f"VXN {regime['vxn']}, VIX {regime['vix']}, last follow-through {regime['last_follow_through']}",
              file=sys.stderr)
    return books, regime


def cmd_backtest(args, config):
    market = _market(args, config)
    books, regime = [], None
    if config.copy.enabled and not args.synthetic:
        config, books = _copy_books(config, market)
    if config.daily.enabled and not args.synthetic:
        daily, regime = _daily_books(config, args.cache_dir)
        books += daily
    errors = market.refresh()
    for symbol, error in errors.items():
        print(f"! {symbol}: {error}", file=sys.stderr)
    research = run_research(market.bars, config, all_strategies(disabled=config.disabled_strategies), copy_books=books)
    board = leaderboard(research)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_rows", 200)
    cols = ["sleeve", "kind", "style", "return_pct", "per_day_pct", "sharpe", "max_drawdown_pct", "trades", "win_rate_pct", "profit_factor", "exposure_pct"]
    print(f"Backtest {research.index[0]:%Y-%m-%d %H:%M} -> {research.index[-1]:%Y-%m-%d %H:%M} UTC, "
          f"{len(research.symbols)} symbols, {len(research.pair_columns)} strategy/symbol pairs, £{config.starting_capital_gbp:.0f} each\n")
    print(board[cols].to_string(index=False))
    for book in books:
        if book.current():
            holdings = ", ".join(f"{t} {w:.0%}" for t, w in sorted(book.current().items(), key=lambda kv: -kv[1]))
            print(f"\n{book.name} ({book.source}, as of {book.as_of}): {holdings}")
    if research.selection:
        print("\nAgent's picks for today:")
        for row in research.selection:
            print(f"  {row['strategy']:<22} {row['symbol']:<9} score {row['score']:.2f}  look-back {row['lookback_return_pct']:+.2f}%")
    if args.out:
        from . import report
        out = Path(args.out)
        state = {"created_at": None, "mode": "backtest", "sleeves": {}, "ticks": 0, "regime": regime}
        report.write_all(out, state, research, config, pd.Timestamp.now(tz="UTC"))
        board.to_csv(out / "leaderboard.csv", index=False)
        print(f"\nReport written to {out}/ (README.md, dashboard.html, dashboard.json, leaderboard.csv)")


def cmd_tick(args, config):
    engine = Engine(config, Path(args.state_dir), market=_market(args, config) if args.synthetic else None,
                    cache_dir=Path(args.cache_dir))
    result = engine.tick()
    print(json.dumps({k: v for k, v in result.items() if k != "trades"} | {"trades": len(result["trades"])}, default=str, indent=1))


def cmd_run(args, config):
    engine = Engine(config, Path(args.state_dir), cache_dir=Path(args.cache_dir))
    engine.run(minutes=args.minutes, interval=args.interval)


def cmd_doctor(args, config):
    from . import data

    now = pd.Timestamp.now(tz="UTC")
    for name, provider, symbol in (("yfinance", data.fetch_yfinance, "SPY"), ("yahoo", data.fetch_yahoo, "SPY"),
                                   ("coinbase", data.fetch_coinbase_range, "BTC-USD"),
                                   ("yfinance", data.fetch_yfinance, "BTC-USD")):
        try:
            frame = provider(symbol, config.interval, "2d", now=now)
            print(f"provider {name:<9} {symbol:<8} ok   {len(frame)} bars, last {frame.index[-1] if len(frame) else None}")
        except Exception as error:
            print(f"provider {name:<9} {symbol:<8} FAIL {str(error)[:200]}")
    if config.daily.enabled:
        try:
            books, _ = _daily_books(config, None)
            for book in books:
                print(f"daily sleeve {book.name:<30} {len(book.schedule)} changes, now {book.current() or 'flat'}")
        except Exception as error:
            print(f"daily sleeves FAIL {str(error)[:200]}")
    market = MarketData(config, None)
    ok = True
    for asset in config.universe:
        try:
            frame = market._fetch(asset, "5d", pd.Timestamp.now(tz="UTC"))
            last = frame.index[-1] if not frame.empty else None
            print(f"ok   {asset.symbol:<9} {len(frame):>5} bars, last {last}")
        except Exception as error:
            ok = False
            print(f"FAIL {asset.symbol:<9} {error}")
    if config.broker.mode != "paper":
        from .live import make_broker
        try:
            broker = make_broker(config)
            account = broker.account()
            print(f"broker ok: {config.broker.mode}, equity {account.get('equity')} {account.get('currency', 'USD')}")
        except Exception as error:
            ok = False
            print(f"broker FAIL: {error}")
    sys.exit(0 if ok else 1)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m agent", description=__doc__)
    parser.add_argument("--config", default=None, help="TOML config (default: config.toml if present)")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    def common(p, state=True):
        p.add_argument("--cache-dir", default=".cache/bars")
        if state:
            p.add_argument("--state-dir", default="state")

    p = sub.add_parser("backtest", help="Backtest every strategy on recent data and print the leaderboard")
    common(p, state=False)
    p.add_argument("--synthetic", action="store_true", help="Use generated data (offline demo)")
    p.add_argument("--days", type=int, default=60)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--out", default=None, help="Write a report folder here")
    p.set_defaults(fn=cmd_backtest)

    p = sub.add_parser("tick", help="Run one trading cycle and exit")
    common(p)
    p.add_argument("--synthetic", action="store_true")
    p.add_argument("--days", type=int, default=20)
    p.add_argument("--seed", type=int, default=7)
    p.set_defaults(fn=cmd_tick)

    p = sub.add_parser("run", help="Trade continuously")
    common(p)
    p.add_argument("--minutes", type=float, default=None, help="Stop after this long (default: forever)")
    p.add_argument("--interval", type=float, default=60.0, help="Seconds between ticks")
    p.set_defaults(fn=cmd_run)

    p = sub.add_parser("doctor", help="Check market data and broker connectivity")
    p.set_defaults(fn=cmd_doctor)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    config = load_config(args.config)
    args.fn(args, config)


if __name__ == "__main__":
    main()
