"""Human-readable outputs: dashboard.json, README.md leaderboard, dashboard.html."""
from __future__ import annotations

import json
import logging
from pathlib import Path

import pandas as pd

from .config import Config
from .research import Research, curve
from .state import StateStore, atomic_write

log = logging.getLogger(__name__)

DISCLAIMER = ("Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars "
              "with modelled costs; past results do not predict future returns, and most day-trading strategies "
              "lose money after costs.")


def _live_curves(history: list[dict], names: list[str], points: int = 200) -> dict[str, list]:
    if not history:
        return {}
    step = max(1, len(history) // points)
    sampled = history[::step]
    if sampled[-1] is not history[-1]:
        sampled.append(history[-1])
    return {name: [[row["t"], row["e"][name]] for row in sampled if name in row["e"]] for name in names}


def build_dashboard(state: dict, research: Research, config: Config, now: pd.Timestamp,
                    store: StateStore | None = None) -> dict:
    history = store.read_jsonl("history.jsonl") if store else []
    trades = store.read_jsonl("trades.jsonl", tail=150) if store else []
    names = list(research.sleeves)
    live_curves = _live_curves(history, names)
    from .portfolio import Sleeve

    sleeves = []
    for name, result in research.sleeves.items():
        strategy = result.strategy
        data = state["sleeves"].get(name)
        fallback = result.kind if result.kind in ("copy", "daily", "ai") else "meta"
        sleeves.append({
            "name": name,
            "kind": result.kind,
            "style": strategy.style if strategy else fallback,
            "family": strategy.family if strategy else fallback,
            "description": result.description or (strategy.description if strategy else _meta_description(name, config)),
            "live": Sleeve(data).summary() if data else None,
            "backtest": result.stats,
            "targets": {s: round(w, 4) for s, w in research.targets(name).items()},
            "live_curve": live_curves.get(name, []),
            "backtest_curve": curve(result.returns, config.starting_capital_gbp),
        })
    sleeves.sort(key=lambda row: (-(row["live"] or {}).get("return_pct", 0.0), -(row["backtest"] or {}).get("return_pct", 0.0)))
    return {
        "generated_at": now.isoformat(),
        "started_at": state.get("created_at"),
        "mode": state.get("mode", "paper"),
        "starting_capital_gbp": config.starting_capital_gbp,
        "ticks": state.get("ticks", 0),
        "last_tick": state.get("last_tick"),
        "universe": [{"symbol": a.symbol, "kind": a.kind} for a in config.universe],
        "backtest_window": {"from": research.index[0].isoformat(), "to": research.index[-1].isoformat(),
                            "bars": len(research.index)},
        "selection": research.selection,
        "copy_books": _copy_books(state),
        "regime": state.get("regime"),
        "analyst": {k: v for k, v in ((state.get("analyst") or {}).get("latest") or {}).items() if k != "analysis"} or None,
        "sleeves": sleeves,
        "recent_trades": list(reversed(trades)),
        "broker": state.get("broker"),
        "disclaimer": DISCLAIMER,
    }


def _copy_books(state: dict) -> list[dict]:
    books = []
    for book in (state.get("copy") or {}).get("books", {}).values():
        current = book.get("schedule", [[None, {}]])[-1] if book.get("schedule") else [None, {}]
        books.append({"name": book.get("name"), "source": book.get("source"), "as_of": book.get("as_of"),
                      "updated_at": book.get("updated_at"), "error": book.get("error"), "stale": book.get("stale"),
                      "effective": current[0], "holdings": dict(sorted(current[1].items(), key=lambda kv: -kv[1]))})
    return books


def _meta_description(name: str, config: Config) -> str:
    meta = config.meta
    if name == "Agent":
        return (f"Walk-forward selector: each UTC day trades the top {meta.top_k} strategy/symbol pairs by "
                f"{meta.lookback_days}-day risk-adjusted return (min {meta.min_trades} trades)")
    if name == "Agent (aggressive)":
        return f"Concentrated selector: top {meta.aggressive_top_k} pairs, up to 100% in one symbol"
    if name == "Agent (rotation)":
        return (f"Strategy rotation: each UTC day copies the top {meta.rotation_top_k} strategy sleeves by "
                f"{meta.rotation_lookback_days}-day risk-adjusted return")
    if name.startswith("Max aggression"):
        return (f"All-in momentum: each US morning puts 100% into the high-volatility name (3x ETFs, crypto, COIN, MSTR, "
                f"...) with the biggest gain over the past {name.split(':')[1].split('-')[0].strip()} day(s); cash if nothing is up")
    if name == "Consensus":
        return f"Long when at least {meta.consensus_threshold:.0%} of strategies agree on a symbol"
    return ""


def _fmt(value, suffix="", digits=2):
    if value is None:
        return "—"
    return f"{value:,.{digits}f}{suffix}"


def markdown(dashboard: dict) -> str:
    lines = ["# Trading agent — live leaderboard", "",
             f"Mode: **{dashboard['mode']}** · started {dashboard['started_at']} · updated {dashboard['generated_at']} · "
             f"{dashboard['ticks']} ticks", "", f"> {dashboard['disclaimer']}", ""]
    agent = next((s for s in dashboard["sleeves"] if s["name"] == "Agent"), None)
    if agent and agent["live"]:
        live = agent["live"]
        lines += [f"## Agent: £{live['equity_gbp']:.2f} ({live['return_pct']:+.2f}%)", "",
                  f"Closed trades {live['closed_trades']}, win rate {_fmt(live['win_rate_pct'], '%', 1)}, "
                  f"fees £{live['fees_gbp']:.2f}, max drawdown {live['max_drawdown_pct']:.2f}%.", ""]
        if live["positions"]:
            lines += ["| Holding | Value £ | P/L £ |", "|---|---:|---:|"]
            lines += [f"| {p['symbol']} | {p['value_gbp']:.2f} | {p['pnl_gbp']:+.2f} |" for p in live["positions"]]
            lines.append("")
    if dashboard.get("copy_books"):
        lines += ["### Copy trading: what famous investors and insiders disclosed", "",
                  "| Book | Latest disclosure | Holdings copied (weight) | Status |", "|---|---|---|---|"]
        for book in dashboard["copy_books"]:
            holdings = ", ".join(f"{t} {w:.0%}" for t, w in list(book["holdings"].items())[:10]) or "—"
            status = book.get("error") or "ok"
            lines.append(f"| {book['name']} | {book.get('as_of') or '—'} | {holdings} | {status} |")
        lines.append("")
    regime = dashboard.get("regime") or {}
    if regime.get("state"):
        lines += [f"### Market regime ({regime['index']}, {regime['session']})", "",
                  f"**{regime['state'].capitalize()}** since {regime.get('since') or '—'} · level {regime['level']} · {regime['distribution_days']} distribution "
                  f"days in 25 sessions · timing exposure {regime['exposure']:.0%} · VXN {_fmt(regime.get('vxn'))} · "
                  f"VIX {_fmt(regime.get('vix'))} · last follow-through day {regime.get('last_follow_through') or '—'}", ""]
        if regime.get("top_scores"):
            lines += ["Best bullish scores: " + ", ".join(f"{k} {v:.1f}" for k, v in regime["top_scores"].items()), ""]
    elif regime.get("error"):
        lines += ["### Market regime", "", f"Daily data unavailable: {regime['error']}", ""]
    analyst = dashboard.get("analyst") or {}
    if analyst.get("session"):
        picks = ", ".join(f"{p['symbol']} {p['weight']:.0%}" for p in analyst.get("positions") or []) or "all cash"
        lines += [f"### AI analyst ({analyst.get('model')}, after the {analyst['session']} close)", "",
                  f"{analyst.get('market_view') or ''}", "", f"Holding from {analyst.get('effective', '')[:16]} UTC: {picks}", ""]
        lines += [f"- **{p['symbol']}**: {p['reason']}" for p in analyst.get("positions") or []]
        lines.append("")
    if dashboard["selection"]:
        lines += ["### Today's picks (walk-forward)", "", "| Strategy | Symbol | Score | Look-back return | Trades |",
                  "|---|---|---:|---:|---:|"]
        lines += [f"| {r['strategy']} | {r['symbol']} | {r['score']:.2f} | {r['lookback_return_pct']:+.2f}% | {r['lookback_trades']} |"
                  for r in dashboard["selection"]]
        lines.append("")
    lines += ["## Every sleeve (each started with £%.0f)" % dashboard["starting_capital_gbp"], "",
              "| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |",
              "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for rank, row in enumerate(dashboard["sleeves"], 1):
        live, bt = row["live"] or {}, row["backtest"] or {}
        flag = " ⛔" if live.get("disabled") else (" ⏸" if live.get("halted") else "")
        lines.append(f"| {rank} | {row['name']}{flag} | {row['style']} | {_fmt(live.get('equity_gbp'))} | "
                     f"{_fmt(live.get('return_pct'), '', 2)} | {live.get('closed_trades', '—')} | "
                     f"{_fmt(live.get('win_rate_pct'), '', 1)} | {_fmt(bt.get('return_pct'))} | {_fmt(bt.get('sharpe'))} | "
                     f"{_fmt(bt.get('max_drawdown_pct'))} | {bt.get('trades', '—')} |")
    lines += ["", "## Recent trades", "", "| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |", "|---|---|---|---|---:|---:|---|"]
    for trade in dashboard["recent_trades"][:40]:
        lines.append(f"| {trade['t'][:16]} | {trade['sleeve']} | {trade['side']} | {trade['symbol']} | "
                     f"{trade['value_gbp']:.2f} | {_fmt(trade.get('pnl_gbp'))} | {trade.get('reason', '')} |")
    broker = dashboard.get("broker")
    if broker:
        lines += ["", "## Broker", "", "```", json.dumps(broker, indent=1, default=str)[:3000], "```"]
    last = dashboard.get("last_tick") or {}
    if last.get("data_errors"):
        lines += ["", "## Data problems on the last tick", ""]
        lines += [f"- {symbol}: {error}" for symbol, error in last["data_errors"].items()]
    lines += ["", "Open `dashboard.html` (download it or use a raw HTML viewer) for charts.", ""]
    return "\n".join(lines)


def write_all(folder: Path, state: dict, research: Research, config: Config, now: pd.Timestamp) -> dict:
    store = StateStore(folder)
    dashboard = build_dashboard(state, research, config, now, store)
    atomic_write(Path(folder) / "dashboard.json", json.dumps(dashboard, allow_nan=False, default=str) + "\n")
    atomic_write(Path(folder) / "README.md", markdown(dashboard))
    try:
        from .report_html import render
        atomic_write(Path(folder) / "dashboard.html", render(dashboard))
    except ImportError:
        pass
    except Exception as error:  # a chart bug must never stop trading
        log.warning("HTML dashboard failed: %s", error)
    return dashboard
