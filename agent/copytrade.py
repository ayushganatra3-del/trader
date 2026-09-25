"""Copy trading: follow what famous investors and company insiders disclose.

Each source becomes a "book": a schedule of target portfolios, each one
effective only after the information behind it was public, so backtests of a
copy sleeve never use a filing before it was filed.

Sources (public and free):

* SEC EDGAR 13F-HR filings: the long US stock holdings of big managers
  (Buffett, Ackman, ...). Filed up to 45 days after each quarter ends, so they
  are always somewhat out of date. Options and bonds are skipped.
* OpenInsider: SEC Form 4 open-market purchases by company officers and
  directors, filed within two business days of the trade.
* AI-Trader (ai4trade.ai): live positions of the most profitable AI trading
  agents on its public leaderboard. No history is published, so this book
  only builds a track record from the day it starts.

Members of Congress are copied through the NANC ETF instead (see
config.COPY_ETFS), which do this professionally.
"""
from __future__ import annotations

import contextlib
import json
import logging
import os
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from html.parser import HTMLParser

import pandas as pd

from .config import Asset, Config

log = logging.getLogger(__name__)

NEW_YORK = "America/New_York"
OPENINSIDER = ("https://openinsider.com/screener", "http://openinsider.com/screener")
OPENFIGI = "https://api.openfigi.com/v3/mapping"
INSIDER_BOOK = "Copy: Insider buying"
AI_TRADER_API = "https://api.ai4trade.ai"
AI_TRADER_BOOK = "Copy: AI-Trader top agents"


class Http:
    """Minimal HTTP client (replaced by a fake in tests)."""

    def __init__(self, user_agent: str, timeout: float = 30.0, pause: float = 0.15):
        self.user_agent = user_agent
        self.timeout = timeout
        self.pause = pause

    def _open(self, request: urllib.request.Request) -> bytes:
        ipv4 = False
        for attempt in range(3):
            try:
                with _ipv4_only() if ipv4 else contextlib.nullcontext():
                    with urllib.request.urlopen(request, timeout=self.timeout) as response:
                        data = response.read(50_000_000)
                time.sleep(self.pause)  # stay well under SEC's 10 requests/second
                return data
            except urllib.error.HTTPError as error:
                if error.code == 403 and "sec.gov" in request.full_url:
                    raise RuntimeError("SEC refused the request (HTTP 403): set the repository variable "
                                       "SEC_USER_AGENT to 'Your Name your@email.com'") from error
                if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                    raise RuntimeError(f"{request.get_method()} {request.full_url.split('?')[0]}: HTTP {error.code}") from error
            except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
                if attempt == 2:
                    raise RuntimeError(f"{request.get_method()} {request.full_url.split('?')[0]}: {error}") from error
                # "Network is unreachable" usually means an IPv6 address on an IPv4-only host
                ipv4 = True
            time.sleep(2.0 * (attempt + 1))
        raise RuntimeError("unreachable")

    def get(self, url: str, headers: dict | None = None) -> bytes:
        return self._open(urllib.request.Request(url, headers={"User-Agent": self.user_agent, **(headers or {})}))

    def post_json(self, url: str, body) -> bytes:
        return self._open(urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers={
            "User-Agent": self.user_agent, "Content-Type": "application/json"}))


@contextlib.contextmanager
def _ipv4_only():
    original = socket.getaddrinfo

    def ipv4(host, port, family=0, *args, **kwargs):
        return original(host, port, socket.AF_INET, *args, **kwargs)

    socket.getaddrinfo = ipv4
    try:
        yield
    finally:
        socket.getaddrinfo = original


@dataclass
class CopyBook:
    name: str
    description: str
    source: str
    schedule: list = field(default_factory=list)  # [[ISO UTC effective time, {ticker: weight}], ...]
    as_of: str | None = None  # date of the newest disclosure used
    updated_at: str | None = None
    error: str | None = None
    stale: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "CopyBook":
        return cls(**{key: data.get(key) for key in cls.__dataclass_fields__ if key in data})

    def tickers(self) -> set[str]:
        return {ticker for _, weights in self.schedule for ticker in weights}

    def current(self) -> dict[str, float]:
        return dict(self.schedule[-1][1]) if self.schedule else {}


def _next_open_utc(day: pd.Timestamp) -> pd.Timestamp:
    """09:30 New York on the first weekday after ``day`` (information is
    treated as usable only from the next session)."""
    local = pd.Timestamp(day.date(), tz=NEW_YORK) + pd.Timedelta(days=1)
    while local.dayofweek >= 5:
        local += pd.Timedelta(days=1)
    return (local + pd.Timedelta(hours=9, minutes=30)).tz_convert("UTC")


def yahoo_ticker(ticker: str) -> str:
    return ticker.strip().upper().replace("/", "-").replace(".", "-")


# ------------------------------------------------------------------ 13F

def parse_13f_table(xml_bytes: bytes) -> dict[str, dict]:
    """Aggregate a 13F information table by CUSIP: long share positions only."""
    root = ET.fromstring(xml_bytes)
    holdings: dict[str, dict] = {}
    for row in root.iter():
        if not row.tag.endswith("infoTable"):
            continue
        fields = {child.tag.split("}")[-1]: (child.text or "").strip() for child in row.iter()}
        if fields.get("putCall") or fields.get("sshPrnamtType", "SH").upper() != "SH":
            continue
        cusip = fields.get("cusip", "").upper()
        try:
            value = float(fields.get("value", "0").replace(",", ""))
        except ValueError:
            continue
        if not cusip or value <= 0:
            continue
        entry = holdings.setdefault(cusip, {"name": fields.get("nameOfIssuer", ""), "value": 0.0})
        entry["value"] += value
    return holdings


def map_cusips(cusips: list[str], http: Http, cache: dict) -> dict[str, str | None]:
    """CUSIP -> Yahoo ticker via OpenFIGI (free: 25 requests/min, 10 per request)."""
    missing = [c for c in dict.fromkeys(cusips) if c not in cache]
    for start in range(0, len(missing), 10):
        chunk = missing[start:start + 10]
        body = [{"idType": "ID_CUSIP", "idValue": c, "exchCode": "US"} for c in chunk]
        try:
            response = json.loads(http.post_json(OPENFIGI, body))
        except Exception as error:
            log.warning("OpenFIGI lookup failed: %s", error)
            break
        for cusip, item in zip(chunk, response):
            data = item.get("data") or []
            equity = [d for d in data if "Stock" in (d.get("securityType") or "") or d.get("securityType2") == "Common Stock"]
            pick = (equity or data or [{}])[0]
            cache[cusip] = yahoo_ticker(pick["ticker"]) if pick.get("ticker") else None
        if start + 10 < len(missing):
            time.sleep(2.6)
    return {c: cache.get(c) for c in cusips}


def _normalise(weights: dict[str, float], cap: float, total: float = 1.0) -> dict[str, float]:
    """Scale ``weights`` to sum to ``total``, capping single names at ``cap``
    and handing the excess to the others (the sum can end below ``total`` when
    every name is at the cap)."""
    size = sum(weights.values())
    if size <= 0 or total <= 0:
        return {}
    out = {k: total * v / size for k, v in weights.items()}
    for _ in range(10):
        over = {k: v for k, v in out.items() if v > cap}
        if not over:
            break
        excess = sum(v - cap for v in over.values())
        under = {k: v for k, v in out.items() if v < cap}
        room = sum(under.values())
        for k in over:
            out[k] = cap
        if room <= 0:
            break
        for k, v in under.items():
            out[k] = v + excess * v / room
    return {k: round(min(v, cap), 6) for k, v in out.items()}


def fetch_13f_book(name: str, cik: str, config: Config, http: Http, cusip_cache: dict,
                   now: pd.Timestamp, filings: int = 3) -> CopyBook:
    cfg = config.copy
    book = CopyBook(f"Copy: {name} 13F", f"Top {cfg.top_n} long holdings from {name}'s latest SEC 13F filing, "
                    "bought the session after it is filed (13Fs lag the quarter end by up to 45 days)", "SEC EDGAR 13F-HR")
    cik10 = str(int(cik)).zfill(10)
    submissions = json.loads(http.get(f"https://data.sec.gov/submissions/CIK{cik10}.json"))
    recent = submissions.get("filings", {}).get("recent", {})
    rows = [i for i, form in enumerate(recent.get("form", [])) if form == "13F-HR"][:filings]
    schedule = []
    for i in sorted(rows, key=lambda i: recent["filingDate"][i]):
        accession = recent["accessionNumber"][i]
        folder = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}"
        index = json.loads(http.get(folder + "/index.json"))
        xmls = [item for item in index.get("directory", {}).get("item", [])
                if item.get("name", "").lower().endswith(".xml") and item["name"].lower() != "primary_doc.xml"]
        if not xmls:
            continue
        table = max(xmls, key=lambda item: int(item.get("size") or 0))
        holdings = parse_13f_table(http.get(f"{folder}/{table['name']}"))
        ranked = sorted(holdings.items(), key=lambda kv: -kv[1]["value"])[: cfg.top_n * 2]
        tickers = map_cusips([c for c, _ in ranked], http, cusip_cache)
        weights: dict[str, float] = {}
        for cusip, info in ranked:
            ticker = tickers.get(cusip)
            if ticker and len(weights) < cfg.top_n:
                weights[ticker] = weights.get(ticker, 0.0) + info["value"]
        if weights:
            filed = pd.Timestamp(recent["filingDate"][i], tz="UTC")
            schedule.append([_next_open_utc(filed).isoformat(), _normalise(weights, config.risk.max_symbol_weight)])
            book.as_of = recent["filingDate"][i]
    book.schedule = schedule
    if not schedule:
        book.error = "No 13F-HR holdings found"
    elif now - pd.Timestamp(book.as_of, tz="UTC") > pd.Timedelta(days=cfg.stale_days):
        book.stale = True
        book.error = f"Latest 13F is from {book.as_of}; too old to copy"
    book.description = f"{submissions.get('name', name)}: " + book.description
    return book


# ------------------------------------------------------------------ insiders

class _TableParser(HTMLParser):
    """Collects the rows of the first <table class="tinytable">."""

    def __init__(self):
        super().__init__()
        self.rows: list[list[str]] = []
        self._in_table = self._in_cell = False
        self._depth = 0
        self._row: list[str] | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and not self.rows and "tinytable" in (attrs.get("class") or ""):
            self._in_table = True
        elif self._in_table and tag == "tr":
            self._row = []
        elif self._in_table and tag in ("td", "th") and self._row is not None:
            self._in_cell, self._text = True, []

    def handle_endtag(self, tag):
        if not self._in_table:
            return
        if tag in ("td", "th") and self._in_cell and self._row is not None:
            self._row.append(" ".join("".join(self._text).split()))
            self._in_cell = False
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None
        elif tag == "table":
            self._in_table = False

    def handle_data(self, data):
        if self._in_cell:
            self._text.append(data)


def parse_openinsider(html: str) -> list[dict]:
    parser = _TableParser()
    parser.feed(html)
    if not parser.rows:
        return []
    header = [h.replace("\xa0", " ").strip().lower() for h in parser.rows[0]]

    def col(*names):
        for name in names:
            if name in header:
                return header.index(name)
        return None

    i_filed, i_ticker, i_type, i_value = col("filing date"), col("ticker"), col("trade type"), col("value")
    if None in (i_filed, i_ticker, i_value):
        raise ValueError(f"Unexpected OpenInsider columns: {header}")
    trades = []
    for row in parser.rows[1:]:
        if len(row) <= max(i_filed, i_ticker, i_value):
            continue
        if i_type is not None and not row[i_type].upper().startswith("P"):
            continue
        value = re.sub(r"[^0-9.\-]", "", row[i_value])
        try:
            filed = pd.Timestamp(row[i_filed]).tz_localize(NEW_YORK).tz_convert("UTC")
            trades.append({"filed": filed, "ticker": yahoo_ticker(row[i_ticker]), "value": abs(float(value))})
        except (ValueError, TypeError):
            continue
    return trades


def fetch_insider_book(config: Config, http: Http, now: pd.Timestamp, days: int = 60) -> CopyBook:
    cfg = config.copy
    book = CopyBook(INSIDER_BOOK, f"Stocks where company officers/directors made the largest open-market purchases "
                    f"(over ${cfg.insider_min_value_k}k) in the last {cfg.insider_window_days} days; top "
                    f"{cfg.insider_top_n}, equal weight", "SEC Form 4 via OpenInsider")
    params = {"fd": days, "xp": 1, "vl": cfg.insider_min_value_k, "isofficer": 1, "iscob": 1, "isceo": 1,
              "ispres": 1, "iscoo": 1, "iscfo": 1, "isdirector": 1, "grp": 0, "sortcol": 0, "cnt": 1000, "page": 1}
    html, errors = None, []
    for base in OPENINSIDER:  # some hosting networks only reach one of the two
        try:
            html = http.get(f"{base}?{urllib.parse.urlencode(params)}").decode("utf-8", "replace")
            break
        except RuntimeError as error:
            errors.append(str(error))
    if html is None:
        raise RuntimeError("OpenInsider unreachable: " + " | ".join(errors))
    trades = parse_openinsider(html)
    book.schedule = insider_schedule(trades, now, days, cfg.insider_window_days, cfg.insider_top_n)
    if trades:
        book.as_of = max(t["filed"] for t in trades).date().isoformat()
    else:
        book.error = "No insider purchases returned"
    return book


def insider_schedule(trades: list[dict], now: pd.Timestamp, days: int, window: int, top_n: int) -> list:
    """One target portfolio per weekday, from filings made before that open."""
    schedule = []
    start = (now - pd.Timedelta(days=days)).normalize()
    for day in pd.date_range(start, now.normalize(), freq="D", tz="UTC"):
        effective = _next_open_utc(day - pd.Timedelta(days=1))  # this weekday's open
        if effective > now + pd.Timedelta(days=1) or (schedule and schedule[-1][0] == effective.isoformat()):
            continue
        totals: dict[str, float] = {}
        for trade in trades:
            if effective - pd.Timedelta(days=window) <= trade["filed"] < effective:
                totals[trade["ticker"]] = totals.get(trade["ticker"], 0.0) + trade["value"]
        top = sorted(totals, key=lambda t: -totals[t])[:top_n]
        schedule.append([effective.isoformat(), {t: round(1.0 / top_n, 6) for t in top}])
    return schedule


# ------------------------------------------------------------------ AI-Trader

def _ai_trader_ticker(symbol: str, market: str) -> str | None:
    symbol = (symbol or "").strip().upper()
    if not symbol:
        return None
    if market == "us-stock":
        return yahoo_ticker(symbol)
    if market == "crypto":
        for suffix in ("-USD", "/USD", "-USDT", "/USDT", "USDT"):
            if symbol.endswith(suffix) and len(symbol) > len(suffix):
                symbol = symbol[: -len(suffix)]
                break
        return f"{symbol}-USD"
    return None  # prediction markets, forex, ... are not tradable here


def fetch_ai_trader_targets(config: Config, http: Http) -> tuple[dict[str, float], list[str]]:
    """Blend the long stock/crypto positions of the top AI-Trader agents.

    Leaders are ranked by open-position profit on the public leaderboard; each
    leader gets an equal share, split by the value of their positions."""
    cfg = config.copy
    board = json.loads(http.get(f"{AI_TRADER_API}/api/leaderboard/position-pnl?limit={cfg.ai_trader_agents * 3}"))
    leaders = [a for a in board.get("top_agents", []) if (a.get("position_pnl") or 0) > 0][: cfg.ai_trader_agents]
    blend: dict[str, float] = {}
    names = []
    for leader in leaders:
        data = json.loads(http.get(f"{AI_TRADER_API}/api/agents/{int(leader['agent_id'])}/positions"))
        book: dict[str, float] = {}
        for position in data.get("positions", []):
            if (position.get("side") or "").lower() != "long":
                continue
            ticker = _ai_trader_ticker(position.get("symbol"), (position.get("market") or "").lower())
            price = position.get("current_price") or position.get("entry_price")
            try:
                value = abs(float(position.get("quantity") or 0)) * float(price or 0)
            except (TypeError, ValueError):
                continue
            if ticker and value > 0:
                book[ticker] = book.get(ticker, 0.0) + value
        total = sum(book.values())
        if total <= 0:
            continue
        names.append(str(leader.get("name") or leader["agent_id"]))
        for ticker, value in book.items():
            blend[ticker] = blend.get(ticker, 0.0) + value / total
    top = dict(sorted(blend.items(), key=lambda kv: -kv[1])[: cfg.top_n])
    return _normalise(top, config.risk.max_symbol_weight), names


def fetch_ai_trader_book(config: Config, http: Http, now: pd.Timestamp, old: dict | None) -> CopyBook:
    """AI-Trader has no position history, so the schedule is built forward:
    each refresh appends the leaders' current holdings when they change."""
    targets, names = fetch_ai_trader_targets(config, http)
    book = CopyBook.from_dict(old) if old else CopyBook(AI_TRADER_BOOK, "", "")
    book.name, book.source = AI_TRADER_BOOK, "ai4trade.ai public leaderboard"
    book.description = ("Long stock/crypto positions of the top AI agents on AI-Trader (ai4trade.ai) by open "
                        "profit, blended equally: " + (", ".join(names) or "none yet"))
    book.error = None if targets else "No copyable positions among the leaders"
    previous = book.schedule[-1][1] if book.schedule else None
    changed = previous is None or set(previous) != set(targets) or any(
        abs(previous[t] - targets[t]) > 0.02 for t in targets)
    if targets and changed:
        book.schedule = (book.schedule + [[now.ceil("5min").isoformat(), targets]])[-500:]
    book.as_of = now.date().isoformat()
    return book


# ------------------------------------------------------------------ manager

class CopyManager:
    """Refreshes books on their own schedules and keeps them in agent state."""

    def __init__(self, config: Config, http: Http | None = None):
        self.config = config
        # SEC asks automated clients to identify themselves (ideally with a contact email)
        self.http = http or Http(os.environ.get("SEC_USER_AGENT") or config.copy.sec_user_agent)

    def refresh(self, state: dict, now: pd.Timestamp) -> list[CopyBook]:
        cfg = self.config.copy
        store = state.setdefault("copy", {"books": {}, "cusips": {}})
        if not cfg.enabled:
            return []
        jobs = [(f"Copy: {name} 13F", cfg.refresh_hours_13f, lambda n=name, c=cik: fetch_13f_book(
                    n, c, self.config, self.http, store["cusips"], now)) for name, cik in cfg.managers.items()]
        jobs.append((INSIDER_BOOK, cfg.refresh_hours_insider, lambda: fetch_insider_book(self.config, self.http, now)))
        if cfg.ai_trader:
            jobs.append((AI_TRADER_BOOK, cfg.refresh_hours_ai_trader, lambda: fetch_ai_trader_book(
                self.config, self.http, now, store["books"].get(AI_TRADER_BOOK))))
        attempts = store.setdefault("attempts", {})
        for key, hours, fetch in jobs:
            old = store["books"].get(key)
            fresh = old and old.get("updated_at") and not (old.get("error") or "").startswith("Refresh failed")
            wait = pd.Timedelta(hours=hours) if fresh else pd.Timedelta(hours=1)  # retry failures sooner
            last = attempts.get(key)
            if last and now - pd.Timestamp(last) < wait:
                continue
            attempts[key] = now.isoformat()
            try:
                book = fetch()
            except Exception as error:  # keep the last good schedule
                log.warning("Copy source %s failed: %s", key, error)
                book = CopyBook.from_dict(old) if old else CopyBook(key, "", "")
                book.error = f"Refresh failed: {str(error)[:300]}"
            book.updated_at = now.isoformat()
            store["books"][key] = book.to_dict()
        return [CopyBook.from_dict(data) for data in store["books"].values()]

    def assets(self, books: list[CopyBook]) -> list[Asset]:
        known = set(self.config.symbols)
        tickers = sorted({t for book in books if not book.stale for t in book.tickers()} - known)
        assets = []
        for t in tickers:
            if t.endswith("-USD"):  # crypto from AI-Trader agents: 24/7, crypto costs
                assets.append(Asset(t, "crypto", "USD", t.replace("-", "/"), trade_strategies=False))
            else:
                assets.append(Asset(t, "us_equity", "USD", t.replace("-", "."), trade_strategies=False,
                                    cost_bps=self.config.copy.cost_bps))
        return assets


def book_weights(book: CopyBook, index: pd.DatetimeIndex, symbols: list[str], cap: float):
    """Target weights (T x symbols) from a book's schedule; zero before its first entry."""
    import numpy as np

    weights = np.zeros((len(index), len(symbols)))
    if book.stale or not book.schedule:
        return weights
    column = {s: j for j, s in enumerate(symbols)}
    entries = sorted(book.schedule, key=lambda entry: entry[0])
    starts = [pd.Timestamp(t) for t, _ in entries] + [None]
    for (when, targets), end in zip(entries, starts[1:]):
        available = {t: w for t, w in targets.items() if t in column}
        if not available:
            continue
        # a ticker without prices hands its weight to the others instead of sitting in cash
        scaled = _normalise(available, cap, total=min(sum(targets.values()), 1.0))
        rows = index >= pd.Timestamp(when)
        if end is not None:
            rows &= index < end
        for ticker, weight in scaled.items():
            weights[rows, column[ticker]] = weight
    return weights
