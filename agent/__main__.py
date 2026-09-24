"""Command line: ``python -m agent {backtest,tick,run,doctor}``."""
from __future__ import annotations

import argparse
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


def cmd_backtest(args, config):
    market = _market(args, config)
    errors = market.refresh()
    for symbol, error in errors.items():
        print(f"! {symbol}: {error}", file=sys.stderr)
    research = run_research(market.bars, config, all_strategies(disabled=config.disabled_strategies))
    board = leaderboard(research)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_rows", 200)
    cols = ["sleeve", "kind", "style", "return_pct", "per_day_pct", "sharpe", "max_drawdown_pct", "trades", "win_rate_pct", "profit_factor", "exposure_pct"]
    print(f"Backtest {research.index[0]:%Y-%m-%d %H:%M} -> {research.index[-1]:%Y-%m-%d %H:%M} UTC, "
          f"{len(research.symbols)} symbols, {len(research.pair_columns)} strategy/symbol pairs, £{config.starting_capital_gbp:.0f} each\n")
    print(board[cols].to_string(index=False))
    if research.selection:
        print("\nAgent's picks for today:")
        for row in research.selection:
            print(f"  {row['strategy']:<22} {row['symbol']:<9} score {row['score']:.2f}  look-back {row['lookback_return_pct']:+.2f}%")
    if args.out:
        from . import report
        out = Path(args.out)
        state = {"created_at": None, "mode": "backtest", "sleeves": {}, "ticks": 0}
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
