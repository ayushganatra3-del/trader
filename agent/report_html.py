"""Self-contained HTML dashboard: one static page, inline SVG charts, no external assets.

``render(dashboard)`` takes the dict built by ``report.build_dashboard`` and returns the page.
Every string from the data is escaped and every field is optional, so a partial or
backtest-only dashboard still renders. Colours follow the dataviz reference palette
(validated for colour-blind separation in light and dark mode).
"""
from __future__ import annotations

import html
import json
import math
from bisect import bisect_right
from datetime import datetime, timezone

try:
    from zoneinfo import ZoneInfo
    UK = ZoneInfo("Europe/London")
except Exception:  # no tz database installed: show UTC instead
    UK = timezone.utc

FIXED = ("Agent", "Agent (aggressive)", "Consensus", "Hold SPY", "Hold BTC")  # colour slots 1-5
MAX_POINTS, CONTEXT_POINTS = 300, 150
W, H = 1000, 300  # SVG user space; the plot stretches to its box, strokes stay 2px
MINUS = "−"
DASH = ' stroke-dasharray="6 4"'  # benchmarks: dashed, so identity is not colour alone
MODES = {"paper": ("Paper money", ""), "alpaca-paper": ("Alpaca paper account", "info"),
         "alpaca-live": ("LIVE — real money", "live"), "backtest": ("Backtest only", "")}


# ------------------------------------------------------------------ formatting
def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def num(value):
    """A finite float, or None for anything else (None, text, NaN, inf)."""
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    return f if math.isfinite(f) else None


def fmt(value, digits=2, prefix="", suffix="", signed=False) -> str:
    v = num(value)
    if v is None:
        return "—"
    v = round(v, digits) or 0.0  # no "-0.00"
    sign = MINUS if v < 0 else ("+" if signed and v > 0 else "")
    return f"{sign}{prefix}{abs(v):,.{digits}f}{suffix}"


def money(value, digits=2, signed=False):
    return fmt(value, digits, "£", signed=signed)


def pct(value, digits=2, signed=True):
    return fmt(value, digits, suffix="%", signed=signed)


def tone(value, digits=2) -> str:
    v = num(value)
    v = round(v, digits) if v is not None else 0
    return "pos" if v > 0 else "neg" if v < 0 else ""


def parse_time(value):
    if not value:
        return None
    try:
        t = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else t.replace(tzinfo=timezone.utc)


def when(value, year=True, clock=True) -> str:
    """UK-time label such as '24 Sep 2026, 20:18 BST'."""
    t = parse_time(value)
    if t is None:
        return "—"
    t = t.astimezone(UK)
    return f"{t.day} {t:%b}" + (f" {t.year}" if year else "") + (f", {t:%H:%M %Z}" if clock else "")


def short_time(epoch) -> str:
    t = datetime.fromtimestamp(epoch, UK)
    return f"{t.day} {t:%b %H:%M}"


def start_label(start: float) -> str:
    return money(start, 0 if float(start).is_integer() else 2)


def weight(value) -> str:
    """A 0-1 portfolio weight as a percentage."""
    v = num(value)
    return pct(v * 100 if v is not None else None, 0, False)


def plural(n, word):
    return f"{n:,} {word}{'' if n == 1 else 's'}"


# ------------------------------------------------------------------ html pieces
def td(text, value=None, cls="", numeric=False, title=None) -> str:
    """A cell; numeric cells carry a sort key (blank = missing, sorted last)."""
    attrs = ""
    if numeric:
        v = num(value)
        attrs += f' data-v="{"" if v is None else round(v, 6)}"'
        cls = f"n {cls}".strip()
    if cls:
        attrs += f' class="{cls}"'
    if title:
        attrs += f' title="{esc(title)}"'
    return f"<td{attrs}>{text}</td>"


def table(headers, rows, cls="", caption="") -> str:
    """headers: [(label, numeric?)]; rows: ready-made <tr> strings."""
    head = "".join(f'<th scope="col"{" class=n" if n else ""}>{esc(h)}</th>' for h, n in headers)
    cap = f'<caption class="sr">{esc(caption)}</caption>' if caption else ""
    swipe = '<p class="swipe">Swipe sideways for more columns \u2192</p>' if len(headers) > 4 else ""
    return (f'{swipe}<div class="scroll"><table class="{cls}">{cap}<thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def tr(cells, cls="") -> str:
    return (f'<tr class="{cls}">' if cls else "<tr>") + "".join(cells) + "</tr>"


def card(title, body, sub="", cls="") -> str:
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<section class="card {cls}"><h2>{esc(title)}</h2>{sub_html}{body}</section>'


def note(text) -> str:
    return f'<p class="note">{esc(text)}</p>'


# ------------------------------------------------------------------ charts
def thin(points: list, limit: int) -> list:
    if len(points) <= limit:
        return points
    out = points[::math.ceil(len(points) / (limit - 1))]
    return out + [points[-1]] if out[-1] is not points[-1] else out


def curve_points(raw) -> list:
    points = []
    for item in raw or []:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            t, v = parse_time(item[0]), num(item[1])
            if t is not None and v is not None:
                points.append((t.timestamp(), v))
    return thin(sorted(points), MAX_POINTS)


def nice_ticks(lo, hi, count=5):
    raw = (hi - lo) / count
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw * 0.999)
    first, last = math.floor(lo / step) * step, math.ceil(hi / step) * step
    return [first + i * step for i in range(int(round((last - first) / step)) + 1)], step


def top_others(sleeves, metric, drawable=lambda s: True) -> list:
    """Names of the best three strategies outside the fixed five, by ``metric``."""
    pool = [(metric(s), s.get("name")) for s in sleeves if s.get("name") not in FIXED
            and s.get("kind", "strategy") == "strategy" and drawable(s) and metric(s) is not None]
    return [name for _, name in sorted(pool, key=lambda p: -p[0])[:3]]


def slot_maps(live_top, bt_top):
    """Colour follows the sleeve: the fixed five own slots 1-5; a strategy in both top-3
    lists gets the same slot (6-8) in both charts."""
    common = [n for n in live_top if n in bt_top]
    maps = []
    for top in (live_top, bt_top):
        slots = {name: i + 1 for i, name in enumerate(FIXED)}
        for i, name in enumerate(common + [n for n in top if n not in common]):
            slots[name] = 6 + i
        maps.append(slots)
    return maps


def chart(sleeves, key, slots, start, label) -> str:
    """Equity curves: highlighted sleeves in palette colours, the rest as faint context."""
    drawn = []
    for s in sleeves:
        pts = curve_points(s.get(key))
        if len(pts) >= 2:
            drawn.append({"name": str(s.get("name") or "?"), "pts": pts, "slot": slots.get(s.get("name")),
                          "dash": s.get("kind") == "benchmark" or str(s.get("name", "")).startswith("Hold ")})
    if not drawn:
        return ""
    t0, t1 = min(d["pts"][0][0] for d in drawn), max(d["pts"][-1][0] for d in drawn)
    t1 = t1 if t1 > t0 else t0 + 1
    values = [v for d in drawn for _, v in d["pts"]] + [start]
    lo, hi = min(values), max(values)
    lo, hi = (lo - 1, hi + 1) if hi - lo < 1e-6 else (lo - (hi - lo) * .04, hi + (hi - lo) * .04)
    ticks, step = nice_ticks(max(lo, 0) if min(values) >= 0 else lo, hi)
    lo, hi = ticks[0], ticks[-1]
    x = lambda t: (t - t0) / (t1 - t0) * W  # noqa: E731
    y = lambda v: (hi - v) / (hi - lo) * H  # noqa: E731
    path = lambda pts: "M" + " ".join(f"{x(t):.1f},{y(v):.1f}" for t, v in pts)  # noqa: E731
    hl = sorted((d for d in drawn if d["slot"]), key=lambda d: d["slot"])
    grey = [d for d in drawn if not d["slot"]]

    svg = ['<svg viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true"><g class="grid">']
    svg += [f'<line x1="0" x2="{W}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>' for v in ticks]
    svg.append(f'</g><line class="base" x1="0" x2="{W}" y1="{y(start):.1f}" y2="{y(start):.1f}"/><g class="ctx">')
    svg += [f'<path d="{path(thin(d["pts"], CONTEXT_POINTS))}"/>' for d in grey]
    svg.append("</g>")
    svg += [f'<path class="ln{" agent" if d["name"] == "Agent" else ""}" style="stroke:var(--s{d["slot"]})"'
            f'{DASH if d["dash"] else ""} d="{path(d["pts"])}"/>' for d in reversed(hl)]
    svg.append("</svg>")

    digits = next(n for n in range(4) if abs(step * 10 ** n - round(step * 10 ** n)) < 1e-6 or n == 3)
    over = [f'<span class="yl" style="top:{y(v) / H * 100:.2f}%">{money(v, digits)}</span>' for v in ticks]
    long_span = t1 - t0 >= 2 * 86400
    for i in range(5):
        t = datetime.fromtimestamp(t0 + i * (t1 - t0) / 4, UK)
        text = f"{t.day} {t:%b}" if long_span else f"{t:%H:%M}"
        edge = " first" if i == 0 else " last" if i == 4 else " odd" if i % 2 else ""
        over.append(f'<span class="xl{edge}" style="left:{i * 25}%">{text}</span>')
    agent = next((d for d in hl if d["name"] == "Agent"), None)
    if agent:
        t, v = agent["pts"][-1]
        top = f"{y(v) / H * 100:.2f}%"
        over.append(f'<span class="dot" style="left:{x(t) / W * 100:.2f}%;top:{top};background:var(--s1)"></span>'
                    f'<span class="endlbl" style="top:{top}">{money(v)}</span>')

    grid = thin(sorted({t for d in hl for t, _ in d["pts"]}), MAX_POINTS)
    series = []
    for d in hl:
        times = [t for t, _ in d["pts"]]
        index = [bisect_right(times, t) - 1 for t in grid]  # last point at or before each grid time
        vals = [round(d["pts"][i][1], 2) if i >= 0 else None for i in index]
        series.append({"n": d["name"], "c": f"var(--s{d['slot']})", "d": d["dash"], "v": vals})
    labels = [short_time(g) for g in grid]
    payload = json.dumps({"x": [round(x(g) / W, 4) for g in grid], "t": labels, "s": series},
                         separators=(",", ":"), allow_nan=False)

    legend = []
    for d in hl:
        ret = (d["pts"][-1][1] / start - 1) * 100 if start else None
        legend.append(f'<li><i class="key{" dash" if d["dash"] else ""}" style="border-color:var(--s{d["slot"]})">'
                      f'</i>{esc(d["name"])} <b class="{tone(ret)}">{pct(ret, 1)}</b></li>')
    if grey:
        legend.append(f'<li><i class="key ctx"></i>Other sleeves ({len(grey)})</li>')
    legend.append(f'<li><i class="key base"></i>Starting balance {start_label(start)}</li>')
    aria = f"{label}: {len(drawn)} equity curves" + (f"; Agent ends at {money(agent['pts'][-1][1])}" if agent else "")
    return (f'<ul class="legend">{"".join(legend)}</ul><div class="frame"><div class="plot" tabindex="0" role="img" '
            f'aria-label="{esc(aria)}" data-series="{esc(payload)}">{"".join(svg)}{"".join(over)}'
            f'<div class="cross"></div><div class="tip" aria-hidden="true"></div></div></div>')


# ------------------------------------------------------------------ page sections
def header(d: dict) -> str:
    mode = str(d.get("mode") or "paper")
    text, cls = MODES.get(mode, (mode, ""))
    ticks = int(num(d.get("ticks")) or 0)
    banner = ""
    if mode == "alpaca-live":
        banner = ('<div class="banner" role="alert"><b>⚠ Live trading with real money.</b> '
                  "The Agent is placing real orders in your Alpaca account. Losses are real.</div>")
    started = f' · started {esc(when(d.get("started_at")))}' if d.get("started_at") else ""
    return (f'{banner}<header><div class="title"><h1>Trading agent</h1><span class="badge mode {cls}">{esc(text)}</span>'
            f'</div><p class="meta">Updated <time data-ts="{esc(d.get("generated_at"))}">{esc(when(d.get("generated_at")))}</time>'
            f'<span class="ago"></span>{started} · {plural(ticks, "tick")}</p></header>')


def hero(agent, start: float) -> str:
    live, bt = (agent or {}).get("live"), (agent or {}).get("backtest")
    if not live and not bt:
        return card("Agent", note("No results for the Agent yet."))
    if live:
        source, equity, ret, trades = "Live", live.get("equity_gbp"), live.get("return_pct"), live.get("closed_trades")
        win, dd, extra = live.get("win_rate_pct"), live.get("max_drawdown_pct"), f"fees paid {money(live.get('fees_gbp'))}"
    else:
        source, equity, ret, trades = "Backtest", bt.get("final_gbp"), bt.get("return_pct"), bt.get("trades")
        win, dd, extra = bt.get("win_rate_pct"), bt.get("max_drawdown_pct"), f"over {fmt(bt.get('days'), 0)} days"
    if num(equity) is None and num(ret) is not None:
        equity = start * (1 + num(ret) / 100)
    profit = num(equity) - start if num(equity) is not None else None
    tiles = [("Return", pct(ret), tone(ret), f"since starting with {start_label(start)}"),
             ("Closed trades", fmt(trades, 0), "", extra),
             ("Win rate", pct(win, 1, signed=False), "", "share of closed trades in profit"),
             ("Max drawdown", pct(dd, 1), "", "biggest fall from a high point")]
    html_tiles = "".join(f'<div class="tile"><div class="lbl">{esc(a)}</div><div class="val {c}">{esc(b)}</div>'
                         f'<div class="hint">{esc(h)}</div></div>' for a, b, c, h in tiles)
    warn = ""
    if live and (live.get("halted") or live.get("disabled")):
        why = live.get("halt_reason") or ("disabled" if live.get("disabled") else "halted")
        warn = f'<p class="alert">⚠ The Agent is paused: {esc(why)}</p>'
    return (f'<section class="card"><h2>Agent <span class="badge">{source}</span></h2>{warn}'
            f'<div class="kpis"><div class="tile hero"><div class="lbl">Balance</div><div class="big">{esc(money(equity))}</div>'
            f'<div class="hint {tone(profit)}">{esc(money(profit, signed=True))} since start</div></div>{html_tiles}</div></section>')


def leaderboard(sleeves) -> str:
    rows = []
    for rank, s in enumerate(sleeves, 1):
        live, bt = s.get("live") or {}, s.get("backtest") or {}
        badges = ('<span class="badge off">Disabled</span>' if live.get("disabled") else
                  f'<span class="badge halt" title="{esc(live.get("halt_reason"))}">Halted</span>' if live.get("halted") else "")
        name = f'{esc(s.get("name"))} {badges}'.strip()
        rows.append(tr([
            td(rank, rank, numeric=True),
            td(name, cls="name", title=s.get("description") or None),
            td(money(live.get("equity_gbp")), live.get("equity_gbp"), tone(live.get("return_pct")), True),
            td(pct(live.get("return_pct")), live.get("return_pct"), tone(live.get("return_pct")), True),
            td(fmt(live.get("closed_trades"), 0), live.get("closed_trades"), numeric=True),
            td(pct(live.get("win_rate_pct"), 1, False), live.get("win_rate_pct"), numeric=True),
            td(pct(bt.get("return_pct")), bt.get("return_pct"), tone(bt.get("return_pct")), True),
            td(fmt(bt.get("sharpe")), bt.get("sharpe"), numeric=True),
            td(pct(bt.get("max_drawdown_pct"), 1), bt.get("max_drawdown_pct"), numeric=True),
            td(fmt(bt.get("trades"), 0), bt.get("trades"), numeric=True),
            td(esc(s.get("style") or "")),
        ], "hl" if s.get("name") in FIXED else ""))
    heads = [("#", True), ("Sleeve", False), ("Live £", True), ("Live %", True), ("Trades", True), ("Win %", True),
             ("Backtest %", True), ("Sharpe", True), ("Max DD", True), ("BT trades", True), ("Style", False)]
    return table(heads, rows, "sortable board", "All sleeves") if rows else note("No sleeves yet.")


def picks(selection) -> str:
    rows = [tr([td(esc(p.get("strategy"))), td(esc(p.get("symbol"))),
                td(fmt(p.get("score")), p.get("score"), numeric=True),
                td(pct(p.get("lookback_return_pct")), p.get("lookback_return_pct"), tone(p.get("lookback_return_pct")), True),
                td(fmt(p.get("lookback_trades"), 0), p.get("lookback_trades"), numeric=True),
                td("Yes" if p.get("holding") else "No")])
            for p in selection if isinstance(p, dict)]
    heads = [("Strategy", False), ("Symbol", False), ("Score", True), ("Look-back return", True),
             ("Look-back trades", True), ("Holding now", False)]
    return table(heads, rows, "sortable") if rows else note("No picks today — the Agent is staying in cash.")


def holdings(agent) -> str:
    live, targets = (agent or {}).get("live"), (agent or {}).get("targets") or {}
    if not live:
        wanted = ", ".join(f"{esc(k)} {weight(v)}" for k, v in targets.items())
        return note("No live trading yet.") + (f'<p class="sub">Backtest target now: {wanted}</p>' if wanted else "")
    rows = [tr([td(esc(p.get("symbol"))), td(money(p.get("value_gbp")), p.get("value_gbp"), numeric=True),
                td(money(p.get("pnl_gbp"), signed=True), p.get("pnl_gbp"), tone(p.get("pnl_gbp")), True),
                td(weight(targets.get(p.get("symbol"))), targets.get(p.get("symbol")), numeric=True),
                td(esc(when(p.get("opened_at"), year=False)))])
            for p in live.get("positions") or [] if isinstance(p, dict)]
    cash = f'<p class="sub">Cash {esc(money(live.get("cash_gbp")))}</p>'
    heads = [("Symbol", False), ("Value", True), ("Profit/loss", True), ("Target", True), ("Opened", False)]
    return cash + (table(heads, rows, "sortable") if rows else note("Not holding anything right now (all cash)."))


def trades_table(trades, show_sleeve=True, empty="No trades yet.") -> str:
    rows = [tr(([td(esc(t.get("sleeve")))] if show_sleeve else []) + [
                td(esc(when(t.get("t"), year=False))), td(esc(str(t.get("side") or "").capitalize())),
                td(esc(t.get("symbol"))), td(money(t.get("value_gbp")), t.get("value_gbp"), numeric=True),
                td(money(t.get("fee_gbp")), t.get("fee_gbp"), numeric=True),
                td(money(t.get("pnl_gbp"), signed=True), t.get("pnl_gbp"), tone(t.get("pnl_gbp")), True),
                td(esc(t.get("reason") or ""), cls="wrap")])
            for t in trades[:50]]
    heads = ([("Sleeve", False)] if show_sleeve else []) + [
        ("Time", False), ("Side", False), ("Symbol", False), ("Value", True), ("Fee", True), ("Profit/loss", True), ("Why", False)]
    return table(heads, rows) if rows else note(empty)


def items(value) -> list[dict]:
    """Dict rows from a list, or from a dict's values (broker positions are keyed by symbol)."""
    rows = value.values() if isinstance(value, dict) else value if isinstance(value, list) else []
    return [row for row in rows if isinstance(row, dict)]


def bullets(title, lines) -> str:
    return f"<h3>{esc(title)}</h3><ul>" + "".join(f"<li>{esc(line)}</li>" for line in lines) + "</ul>" if lines else ""


def broker_section(b: dict) -> str:
    usd = lambda v: fmt(v, 2, "$")  # noqa: E731
    facts = [("Status", "OK" if b.get("ok") else "\u26a0 Problem"), ("Mode", b.get("mode") or "—"),
             ("Checked", when(b.get("time"))), ("Equity", usd(b.get("equity_usd"))), ("Cash", usd(b.get("cash_usd"))),
             ("Budget", usd(b.get("budget_usd"))), ("Market open", {True: "Yes", False: "No"}.get(b.get("market_open"), "—"))]
    body = '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{esc(v)}</dd></div>" for k, v in facts) + "</dl>"
    if b.get("error"):
        body += f'<p class="alert">\u26a0 {esc(b["error"])}</p>'
    rows = [tr([td(esc(p.get("symbol"))), td(fmt(p.get("qty"), 4), p.get("qty"), numeric=True),
                td(usd(p.get("market_value")), p.get("market_value"), numeric=True),
                td(usd(p.get("unrealized_pl")), p.get("unrealized_pl"), tone(p.get("unrealized_pl")), True)])
            for p in items(b.get("positions"))]
    if rows:
        body += "<h3>Positions</h3>" + table([("Symbol", False), ("Quantity", True), ("Value", True), ("Unrealised P/L", True)], rows)
    rows = [tr([td(esc(o.get("symbol"))), td(esc(o.get("side"))), td(esc(o.get("action"))),
                td(usd(o["notional"]), o["notional"], numeric=True) if o.get("notional") is not None
                else td(fmt(o.get("qty"), 4), o.get("qty"), numeric=True), td(esc(o.get("status")))])
            for o in items(b.get("orders"))]
    if rows:
        body += "<h3>Orders this tick</h3>" + table(
            [("Symbol", False), ("Side", False), ("Action", False), ("Size", True), ("Status", False)], rows)
    body += bullets("Order errors", [f"{e.get('symbol', '')}: {e.get('error', '')}" for e in items(b.get("errors"))])
    body += bullets("Skipped", [f"{e.get('symbol', '')}: {e.get('reason', '')}" for e in items(b.get("skipped"))])
    return card("Broker account", body, "What the real broker account reports (amounts in US dollars).")


def data_problems(errors) -> str:
    items = errors.items() if isinstance(errors, dict) else enumerate(errors or [])
    lis = "".join(f"<li><b>{esc(k)}</b>: {esc(v)}</li>" for k, v in items)
    return card("Data problems on the last update", f"<ul>{lis}</ul>",
                "Prices for these could not be fetched, so they were skipped this time.", "warn") if lis else ""


# ------------------------------------------------------------------ page
def render(dashboard: dict) -> str:
    d = dashboard if isinstance(dashboard, dict) else {}
    sleeves = [s for s in d.get("sleeves") or [] if isinstance(s, dict) and s.get("name") is not None]
    start = num(d.get("starting_capital_gbp")) or 100.0
    agent = next((s for s in sleeves if s.get("name") == "Agent"), None)
    live_ret = lambda s: num((s.get("live") or {}).get("return_pct"))  # noqa: E731
    bt_ret = lambda s: num((s.get("backtest") or {}).get("return_pct"))  # noqa: E731
    live_slots, bt_slots = slot_maps(top_others(sleeves, live_ret, lambda s: len(s.get("live_curve") or []) >= 2),
                                     top_others(sleeves, bt_ret))

    live_chart = chart(sleeves, "live_curve", live_slots, start, "Live equity")
    live_sub = (f"Balance of each sleeve since the agent started ({esc(start_label(start))} each). Coloured lines: the "
                "Agent, its variants, the benchmarks and the three best strategies; grey lines: the rest.") if live_chart else ""
    if not live_chart:
        points = max((len(s.get("live_curve") or []) for s in sleeves), default=0)
        live_chart = note("Collecting data — the live chart appears once there are at least two updates "
                          f"({plural(points, 'point')} so far)." if d.get("mode") != "backtest" else
                          "No live trading yet: this report was made from a backtest only.")
    window = d.get("backtest_window") or {}
    bt_sub = "Each sleeve replayed on past prices from the same starting balance, after modelled costs."
    if window.get("from"):
        bt_sub = f"{esc(when(window['from'], clock=False))} to {esc(when(window.get('to'), clock=False))}. {bt_sub}"
    bt_chart = chart(sleeves, "backtest_curve", bt_slots, start, "Backtest equity") or note("No backtest curves available.")

    trades = [t for t in d.get("recent_trades") or [] if isinstance(t, dict)]
    agent_trades = [t for t in trades if t.get("sleeve") == "Agent"]
    last_tick = d.get("last_tick") if isinstance(d.get("last_tick"), dict) else {}
    body = [
        header(d),
        hero(agent, start),
        card("Live performance", live_chart, live_sub),
        card("Backtest", bt_chart, bt_sub),
        card("Leaderboard", leaderboard(sleeves), "Every sleeve is an independent paper portfolio. Tap a column heading to sort; "
             "hover a name for what the strategy does. Max DD = biggest fall from a high point."),
        card("Today's picks", picks([p for p in d.get("selection") or [] if isinstance(p, dict)]),
             "The strategy/symbol pairs the Agent trades today, chosen by recent risk-adjusted results."),
        card("Agent holdings", holdings(agent)),
        card("Recent trades", trades_table(agent_trades, False, f"No Agent trades among the latest {len(trades)} trades.")
             + (f'<details><summary>All sleeves ({min(len(trades), 50)} most recent)</summary>{trades_table(trades)}</details>'
                if trades else ""), "The Agent's latest trades, newest first. Times are UK time."),
        broker_section(d["broker"]) if isinstance(d.get("broker"), dict) else "",
        data_problems(last_tick.get("data_errors")),
        f'<footer><p>{esc(d.get("disclaimer") or "")}</p></footer>',
    ]
    return (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">'
            f'<title>Trading agent</title><style>{CSS}</style></head><body><main>{"".join(body)}</main>'
            f'<script>{JS}</script></body></html>\n')


CSS = """
:root{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;
--axis:#c3c2b7;--border:rgba(11,11,11,.1);--pos:#006300;--neg:#c62f2f;--crit:#d03b3b;--warn:#fab219;--info:#2a78d6;
--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#e87ba4;--s6:#008300;--s7:#4a3aa7;--s8:#e34948}
@media (prefers-color-scheme:dark){:root{color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;
--grid:#2c2c2a;--axis:#4a4a46;--border:rgba(255,255,255,.1);--pos:#0ca30c;--neg:#f07272;--info:#3987e5;
--s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767}}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:1120px;margin:0 auto;padding:16px}
header{margin:4px 0 16px}.title{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
h1{font-size:26px;margin:0;line-height:1.2}h2{font-size:18px;margin:0 0 4px;display:flex;gap:8px;align-items:center}
h3{font-size:15px;margin:16px 0 6px}.meta,.sub,footer{color:var(--ink2);font-size:14px}.meta{margin:4px 0 0}.sub{margin:0 0 12px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;margin:0 0 16px;min-width:0}
.card.warn{border-color:var(--warn)}
.badge{display:inline-block;padding:1px 9px;border-radius:999px;font-size:12px;font-weight:600;border:1px solid var(--border);
color:var(--ink2);white-space:nowrap;vertical-align:middle}
.badge.mode{font-size:13px;padding:2px 10px}.badge.info{border-color:var(--info);color:var(--ink)}
.badge.live,.badge.off{background:var(--crit);border-color:var(--crit);color:#fff}.badge.halt{background:var(--warn);color:#0b0b0b}
.badge.live{font-size:15px;padding:4px 12px}
.banner{background:var(--crit);color:#fff;border-radius:12px;padding:12px 16px;margin:0 0 12px}
.alert{border-left:4px solid var(--warn);padding:6px 10px;margin:8px 0}
.stale{color:var(--neg);font-weight:600}
.swipe{display:none;font-size:12px;color:var(--ink2);margin:0 0 6px}
.note{color:var(--ink2);background:var(--page);border-radius:8px;padding:16px;margin:0}
.kpis{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.tile{border:1px solid var(--border);border-radius:10px;padding:10px 12px;min-width:0}
.tile.hero{grid-column:1/-1}.lbl{font-size:13px;color:var(--ink2)}.val{font-size:24px;font-weight:600;line-height:1.3}
.big{font-size:48px;font-weight:600;line-height:1.1}.hint{font-size:12px;color:var(--ink2)}.hint.pos,.hint.neg{font-size:16px;font-weight:600}
@media (min-width:760px){.kpis{grid-template-columns:1.5fr repeat(4,minmax(0,1fr))}.tile.hero{grid-column:auto}}
.pos{color:var(--pos)}.neg{color:var(--neg)}
.scroll{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{padding:6px 10px;text-align:left;white-space:nowrap;border-bottom:1px solid var(--grid)}
th{font-size:12px;font-weight:600;color:var(--ink2);border-bottom-color:var(--axis)}
.n{text-align:right;font-variant-numeric:tabular-nums}td.wrap{white-space:normal;min-width:180px}
tr.hl td{font-weight:600}
.sortable th{cursor:pointer;user-select:none}.sortable th[aria-sort=ascending]::after{content:" \\25B2"}
.sortable th[aria-sort=descending]::after{content:" \\25BC"}
.board td.name,.board th:nth-child(2){position:sticky;left:0;background:var(--surface)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
details{margin-top:12px}summary{cursor:pointer;color:var(--ink2);font-weight:600}
.facts{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px;margin:0}
.facts dt{font-size:12px;color:var(--ink2)}.facts dd{margin:0;font-weight:600}
.legend{list-style:none;display:flex;flex-wrap:wrap;gap:4px 16px;padding:0;margin:0 0 8px;font-size:13px}
.legend li{display:flex;align-items:center;gap:6px}.legend b{font-weight:600}
.key{display:inline-block;width:18px;border-top:2px solid}.key.dash{border-top-style:dashed}
.key.ctx{border-color:var(--muted);opacity:.5}.key.base{border-color:var(--axis)}
.frame{padding:6px 68px 28px 48px}
.plot{position:relative;height:280px;touch-action:pan-y;outline-offset:6px}
.plot svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.plot path,.plot line{fill:none;vector-effect:non-scaling-stroke}
.grid line{stroke:var(--grid);stroke-width:1}.plot .base{stroke:var(--axis);stroke-width:1.5}
.ctx path{stroke:var(--muted);stroke-width:1;opacity:.3}
.ln{stroke-width:2;stroke-linejoin:round;stroke-linecap:round}.ln.agent{stroke-width:3}
.yl,.xl{position:absolute;font-size:11px;color:var(--muted);white-space:nowrap;font-variant-numeric:tabular-nums}
.yl{right:calc(100% + 8px);transform:translateY(-50%)}.xl{top:calc(100% + 8px);transform:translateX(-50%)}
.xl.first{transform:none}.xl.last{transform:translateX(-100%)}
.dot{position:absolute;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 2px var(--surface)}
.endlbl{position:absolute;left:calc(100% + 10px);transform:translateY(-50%);font-size:12px;font-weight:600;white-space:nowrap}
.cross{position:absolute;top:0;bottom:0;width:1px;background:var(--ink2);display:none;pointer-events:none}
.tip{position:absolute;top:0;display:none;z-index:2;pointer-events:none;background:var(--surface);color:var(--ink);
border:1px solid var(--border);border-radius:8px;padding:8px 10px;font-size:12px;box-shadow:0 4px 16px rgba(0,0,0,.15)}
.plot.on .cross,.plot.on .tip{display:block}.tip div{display:flex;align-items:center;gap:6px;white-space:nowrap}
.tip .tt{color:var(--ink2);margin-bottom:2px}.tip i{width:12px;border-top:2px solid}.tip span{color:var(--ink2)}
footer{padding:8px 4px 24px}
@media (max-width:520px){main{padding:16px 12px}.card{padding:12px}.frame{padding:6px 58px 28px 40px}.plot{height:220px}
h1{font-size:22px}th,td{padding:6px 8px}.xl.odd{display:none}.swipe{display:block}}
"""

JS = """
document.querySelectorAll("table.sortable th").forEach(th => {
  th.tabIndex = 0;
  const sort = () => {
    const table = th.closest("table"), col = th.cellIndex;
    const dir = th.dataset.dir ? (th.dataset.dir === "asc" ? "desc" : "asc") : (th.classList.contains("n") ? "desc" : "asc");
    table.querySelectorAll("th").forEach(h => { delete h.dataset.dir; h.removeAttribute("aria-sort"); });
    th.dataset.dir = dir; th.setAttribute("aria-sort", dir === "asc" ? "ascending" : "descending");
    const key = row => { const c = row.cells[col], v = c.dataset.v;
      return v === undefined ? c.textContent.trim().toLowerCase() : (v === "" ? null : +v); };
    const rows = [...table.tBodies[0].rows].sort((a, b) => {
      const x = key(a), y = key(b);
      if (x === null || y === null) return (x === null) - (y === null);
      return (x < y ? -1 : x > y ? 1 : 0) * (dir === "asc" ? 1 : -1);
    });
    table.tBodies[0].append(...rows);
  };
  th.addEventListener("click", sort);
  th.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); sort(); } });
});
document.querySelectorAll(".plot[data-series]").forEach(plot => {
  const d = JSON.parse(plot.dataset.series), tip = plot.querySelector(".tip"), cross = plot.querySelector(".cross");
  if (!d.x.length) return;
  let idx = d.x.length - 1;
  const show = i => {
    idx = Math.max(0, Math.min(d.x.length - 1, i));
    const head = document.createElement("div");
    head.className = "tt"; head.textContent = d.t[idx];
    tip.replaceChildren(head);
    d.s.filter(s => s.v[idx] !== null).sort((a, b) => b.v[idx] - a.v[idx]).forEach(s => {
      const row = document.createElement("div"), key = document.createElement("i"),
            val = document.createElement("b"), name = document.createElement("span");
      key.style.borderTopColor = s.c; if (s.d) key.style.borderTopStyle = "dashed";
      val.textContent = "\\u00a3" + s.v[idx].toFixed(2); name.textContent = s.n;
      row.append(key, val, name); tip.append(row);
    });
    plot.classList.add("on");
    const w = plot.clientWidth, px = d.x[idx] * w, box = plot.parentElement.getBoundingClientRect(),
          own = plot.getBoundingClientRect(), tw = tip.offsetWidth;
    let left = px + 12 + tw > box.right - own.left ? px - 12 - tw : px + 12;
    left = Math.max(box.left - own.left, Math.min(left, box.right - own.left - tw));
    cross.style.left = px + "px"; tip.style.left = left + "px";
  };
  const nearest = e => { const r = plot.getBoundingClientRect(), f = (e.clientX - r.left) / r.width;
    let best = 0; d.x.forEach((x, i) => { if (Math.abs(x - f) < Math.abs(d.x[best] - f)) best = i; }); return best; };
  plot.addEventListener("pointermove", e => show(nearest(e)));
  plot.addEventListener("pointerdown", e => show(nearest(e)));
  plot.addEventListener("pointerleave", () => plot.classList.remove("on"));
  plot.addEventListener("focus", () => show(idx));
  plot.addEventListener("blur", () => plot.classList.remove("on"));
  plot.addEventListener("keydown", e => {
    const step = { ArrowLeft: -1, ArrowRight: 1 }[e.key];
    if (step) { e.preventDefault(); show(idx + step * Math.max(1, Math.round(d.x.length / 50))); }
  });
});
document.querySelectorAll("time[data-ts]").forEach(el => {
  const mins = Math.round((Date.now() - Date.parse(el.dataset.ts)) / 60000), out = el.nextElementSibling;
  if (!isFinite(mins) || mins < 0 || !out) return;
  out.textContent = mins < 60 ? ` (${mins} min ago)` : ` (${Math.round(mins / 60)} h ago)`;
  if (mins > 30) { out.className = "ago stale"; out.textContent += " \\u2014 no recent update; is the agent running?"; }
});
"""
