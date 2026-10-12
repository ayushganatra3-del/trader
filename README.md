# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T17:52:05.000133+00:00 · 20438 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.33 (-4.67%)

Closed trades 57, win rate 50.9%, fees £2.24, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.07 | +0.00 |
| TNA | 19.04 | -0.05 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 25254 decisions in 2541 calls, $0.3188 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T17:52 | 5 / 16 / 9 | cash |  |
| Breezy | 2026-10-12T17:52 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-12T17:52 | 2 / 27 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.76 | 2.76 | 0 | — | -0.55 | -0.20 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.23 | 2.23 | 14 | 57.1 | -12.41 | -2.04 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.67 | 1.67 | 39 | 41.0 | -8.92 | -2.68 | -13.79 | 118 |
| 5 | Hold SPY | benchmark | 101.41 | 1.41 | 0 | — | 0.92 | 0.59 | -3.66 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.32 | 1.32 | 6 | 50.0 | 4.74 | 2.11 | -3.27 | 17 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.15 | 1.15 | 0 | — | 1.49 | 0.73 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.65 | 0.65 | 0 | — | -4.99 | -0.82 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.64 | 0.64 | 0 | — | -1.19 | -0.62 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 6 | 50.0 | -3.90 | -1.29 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.32 | 0.32 | 10 | 30.0 | 4.56 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 2.77 | 1.12 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.56 | -0.44 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.77 | -1.23 | 0 | — | 29.82 | 3.50 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.02 | -1.98 | 31 | 12.9 | 14.81 | 1.73 | -16.92 | 113 |
| 20 | Trend pullback · 1h | trend | 97.80 | -2.20 | 78 | 23.1 | -22.95 | -6.41 | -25.52 | 169 |
| 21 | Daily: Bullish score | daily | 97.52 | -2.48 | 4 | 0.0 | 0.41 | 0.25 | -12.76 | 11 |
| 22 | Stochastic reversion · 1h | reversion | 97.35 | -2.65 | 96 | 53.1 | -11.57 | -2.24 | -13.97 | 335 |
| 23 | Max aggression: 1-day momentum | meta | 97.33 | -2.67 | 11 | 36.4 | -17.29 | -0.66 | -37.31 | 42 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Z-score reversion · 1h | reversion | 96.89 | -3.11 | 44 | 43.2 | 3.77 | 0.88 | -8.60 | 157 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 96.76 | -3.24 | 0 | — | 9.14 | 1.51 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.45 | -0.21 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.47 | -3.52 | 62 | 19.4 | -7.69 | -1.31 | -14.13 | 252 |
| 29 | Agent (rotation) | meta | 96.29 | -3.71 | 82 | 29.3 | -13.08 | -4.36 | -17.59 | 298 |
| 30 | MACD cross · 1h | trend | 95.83 | -4.17 | 121 | 24.0 | -13.47 | -2.24 | -17.27 | 469 |
| 31 | EMA 20/50 cross · 1h | trend | 95.58 | -4.42 | 45 | 15.6 | 5.89 | 0.85 | -23.27 | 135 |
| 32 | Parabolic SAR · 1h | trend | 95.47 | -4.53 | 84 | 21.4 | 1.30 | 0.36 | -21.52 | 291 |
| 33 | Agent | meta | 95.33 | -4.67 | 57 | 50.9 | -9.19 | -4.51 | -9.39 | 259 |
| 34 | Supertrend · 1h | trend | 94.42 | -5.58 | 58 | 13.8 | 0.66 | 0.28 | -18.58 | 212 |
| 35 | Squeeze breakout · 1h | breakout | 93.76 | -6.24 | 39 | 23.1 | 3.35 | 0.78 | -9.46 | 104 |
| 36 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.44 | 2.15 | -6.20 | 202 |
| 37 | Agent (aggressive) | meta | 93.30 | -6.70 | 28 | 39.3 | -9.92 | -3.38 | -10.04 | 124 |
| 38 | MFI reversion · 1h | reversion | 93.14 | -6.86 | 131 | 33.6 | -8.10 | -1.23 | -16.95 | 127 |
| 39 | RSI momentum · 1h | momentum | 92.57 | -7.43 | 66 | 15.2 | -0.13 | 0.19 | -22.75 | 228 |
| 40 | Connors RSI(2) · 1h | reversion | 92.55 | -7.45 | 114 | 43.0 | -18.72 | -6.17 | -21.04 | 254 |
| 41 | Agent (ML meta-label) | meta | 92.38 | -7.62 | 425 | 18.4 | -1.13 | -0.07 | -12.57 | 397 |
| 42 | RSI(14) reversion · 1h | reversion | 91.96 | -8.04 | 30 | 30.0 | -1.03 | -0.12 | -9.03 | 134 |
| 43 | Volume breakout · 1h | breakout | 91.81 | -8.19 | 65 | 20.0 | 9.16 | 1.39 | -12.60 | 118 |
| 44 | Bollinger reversion · 1h | reversion | 91.45 | -8.55 | 83 | 37.3 | -23.61 | -5.84 | -24.63 | 315 |
| 45 | Ichimoku · 1h | trend | 91.18 | -8.82 | 47 | 17.0 | 0.96 | 0.32 | -22.34 | 126 |
| 46 | Bollinger breakout · 1h | breakout | 91.11 | -8.89 | 74 | 28.4 | 7.74 | 1.15 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.77 | -9.23 | 71 | 15.5 | -7.34 | -0.65 | -26.89 | 239 |
| 48 | Opening range 30m | breakout | 89.74 | -10.26 | 152 | 21.7 | -15.49 | -4.68 | -15.87 | 569 |
| 49 | Williams %R · 1h | reversion | 89.69 | -10.31 | 131 | 46.6 | -26.47 | -4.49 | -27.56 | 506 |
| 50 | CCI reversion · 1h | reversion | 88.76 | -11.23 | 111 | 45.9 | -7.70 | -0.94 | -14.35 | 406 |
| 51 | VWAP momentum · 1h | momentum | 88.60 | -11.40 | 306 | 23.2 | -33.41 | -4.98 | -40.12 | 1255 |
| 52 | OBV trend · 1h | momentum | 88.55 | -11.45 | 150 | 18.7 | -8.57 | -0.77 | -28.73 | 324 |
| 53 | Candlestick reversal · 1h | reversion | 88.18 | -11.82 | 127 | 31.5 | -30.09 | -5.90 | -30.12 | 499 |
| 54 | Heikin-Ashi · 1h | trend | 88.01 | -11.98 | 151 | 27.8 | -29.52 | -4.91 | -37.05 | 682 |
| 55 | MACD zero-line · 1h | trend | 87.93 | -12.07 | 67 | 17.9 | -19.76 | -3.58 | -21.38 | 232 |
| 56 | Donchian 20/10 · 1h | breakout | 87.67 | -12.33 | 63 | 17.5 | -0.51 | 0.14 | -19.48 | 214 |
| 57 | EMA 9/21 cross · 1h | trend | 87.27 | -12.73 | 107 | 13.1 | -10.84 | -1.29 | -23.35 | 332 |
| 58 | Max aggression: 5-day momentum | meta | 87.21 | -12.79 | 7 | 28.6 | -15.22 | -1.13 | -34.64 | 28 |
| 59 | Opening range 15m | breakout | 86.97 | -13.03 | 180 | 20.0 | -18.04 | -5.00 | -19.41 | 692 |
| 60 | Keltner breakout · 1h | breakout | 86.92 | -13.08 | 45 | 20.0 | -10.95 | -1.26 | -26.77 | 216 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.73 | -14.27 | 146 | 20.5 | -9.26 | -1.09 | -24.83 | 401 |
| 63 | ROC + volume | momentum | 72.92 | -27.08 | 416 | 22.6 | -72.90 | -16.48 | -74.41 | 1676 |
| 64 | RSI(14) reversion | reversion | 70.84 | -29.16 | 404 | 26.7 | -72.79 | -17.82 | -72.79 | 1471 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.01 | -17.81 | -62.16 | 1219 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.23 | -17.69 | -62.26 | 898 |
| 67 | EMA 20/50 cross | trend | 68.29 | -31.71 | 351 | 19.7 | -76.22 | -14.94 | -76.31 | 1430 |
| 68 | Donchian 55/20 | breakout | 67.07 | -32.93 | 357 | 17.6 | -68.04 | -14.27 | -68.90 | 1288 |
| 69 | VWAP reversion | reversion | 65.65 | -34.35 | 427 | 25.5 | -71.34 | -15.68 | -71.36 | 1401 |
| 70 | Keltner breakout | breakout | 60.72 | -39.28 | 478 | 14.6 | -83.43 | -27.21 | -83.51 | 1846 |
| 71 | Supertrend | trend | 60.33 | -39.67 | 495 | 19.2 | -86.01 | -20.74 | -86.01 | 1895 |
| 72 | AI bee: Boozy | ai | 59.93 | -40.07 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.42 | -42.58 | 432 | 10.0 | -82.20 | -22.89 | -82.20 | 1741 |
| 74 | Z-score reversion | reversion | 55.78 | -44.22 | 548 | 21.4 | -85.67 | -22.82 | -85.67 | 2065 |
| 75 | MFI reversion | reversion | 55.76 | -44.23 | 573 | 19.5 | -87.82 | -27.89 | -87.84 | 2113 |
| 76 | AI bee: Bizzy | ai | 55.70 | -44.30 | 881 | 8.4 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.05 | -45.95 | 586 | 9.9 | -89.09 | -33.84 | -89.10 | 2099 |
| 78 | Donchian 20/10 | breakout | 52.21 | -47.79 | 673 | 17.5 | -90.83 | -25.39 | -90.94 | 2642 |
| 79 | MACD zero-line | trend | 51.25 | -48.75 | 625 | 14.4 | -91.43 | -29.29 | -91.43 | 2340 |
| 80 | RSI momentum | momentum | 50.62 | -49.38 | 651 | 16.6 | -90.56 | -25.47 | -90.57 | 2372 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.09 | -98.63 | 5366 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.33 | -26.56 | -91.36 | 2333 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.25 | -29.98 | -93.26 | 2612 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -32.45 | -97.36 | 3511 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.40 | -35.50 | -96.41 | 3599 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -25.52 | -94.34 | 2636 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -36.03 | -99.36 | 5627 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.25 | -96.37 | 3610 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.88 | -99.73 | 6131 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -37.41 | -97.35 | 3672 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.29 | -98.50 | 4656 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.44 | -32.57 | -93.47 | 2794 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.22 | -99.53 | 6098 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.71 | -95.89 | 3715 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -33.86 | -95.71 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.15 | -99.89 | 8225 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T17:50 | Agent (aggressive) | sell | AAPL | 46.65 | -0.01 | selected signal exited |
| 2026-10-12T17:50 | Agent | sell | AAPL | 19.07 | -0.01 | rebalance down |
| 2026-10-12T17:50 | MFI reversion · 1h | sell | SOXL | 18.44 | -0.05 | target is flat |
| 2026-10-12T17:50 | MFI reversion · 1h | sell | BITX | 18.65 | 0.01 | target is flat |
| 2026-10-12T17:50 | ROC + volume · 1h | buy | TSLA | 4.17 | — | entry |
| 2026-10-12T17:50 | MFI reversion | buy | TSLA | 4.65 | — | entry |
| 2026-10-12T17:50 | MFI reversion | buy | TNA | 4.65 | — | entry |
| 2026-10-12T17:50 | MFI reversion | sell | UPRO | 4.65 | -0.00 | target is flat |
| 2026-10-12T17:50 | MFI reversion | sell | AAPL | 4.65 | -0.00 | target is flat |
| 2026-10-12T17:50 | VWAP reversion | buy | ETH-USD | 6.26 | — | entry signal |
| 2026-10-12T17:50 | Z-score reversion | buy | ETH-USD | 1.32 | — | entry signal |
| 2026-10-12T17:50 | RSI(14) reversion | buy | ETH-USD | 7.09 | — | entry signal |
| 2026-10-12T17:50 | Ichimoku | buy | META | 14.36 | — | entry signal |
| 2026-10-12T17:50 | MACD zero-line | buy | MSFT | 12.81 | — | entry signal |
| 2026-10-12T17:48 | MFI reversion · 1h | buy | SOXL | 4.66 | — | rebalance up |
| 2026-10-12T17:48 | MFI reversion · 1h | sell | AMD | 4.66 | -0.01 | rebalance down |
| 2026-10-12T17:46 | Agent (aggressive) | buy | AAPL | 46.65 | — | following MFI reversion, CCI reversion |
| 2026-10-12T17:46 | Agent | buy | AAPL | 19.05 | — | rebalance up |
| 2026-10-12T17:46 | MFI reversion · 1h | buy | SOXL | 13.82 | — | entry |
| 2026-10-12T17:46 | MFI reversion · 1h | buy | QQQ | 18.64 | — | entry |
| 2026-10-12T17:46 | MFI reversion · 1h | buy | BITX | 18.64 | — | entry |
| 2026-10-12T17:46 | MFI reversion · 1h | sell | NVDA | 23.30 | -0.03 | target is flat |
| 2026-10-12T17:46 | ROC + volume · 1h | buy | PLTR | 6.59 | — | entry |
| 2026-10-12T17:46 | ROC + volume · 1h | buy | AMZN | 6.59 | — | entry |
| 2026-10-12T17:46 | ROC + volume · 1h | sell | TSLA | 6.59 | -0.00 | target is flat |
| 2026-10-12T17:46 | MFI reversion | buy | UPRO | 4.65 | — | entry |
| 2026-10-12T17:46 | MFI reversion | buy | QQQ | 4.65 | — | entry |
| 2026-10-12T17:46 | MFI reversion | buy | AAPL | 4.65 | — | entry |
| 2026-10-12T17:46 | MFI reversion | sell | TSLA | 2.54 | -0.00 | target is flat |
| 2026-10-12T17:46 | MFI reversion | sell | TNA | 6.20 | -0.00 | target is flat |
| 2026-10-12T17:46 | MFI reversion | sell | ETH-USD | 3.98 | -0.04 | stop-loss |
| 2026-10-12T17:46 | MFI reversion | sell | AMZN | 3.99 | -0.00 | target is flat |
| 2026-10-12T17:46 | VWAP reversion | buy | SOL-USD | 8.20 | — | entry signal |
| 2026-10-12T17:46 | VWAP reversion | sell | TECL | 7.17 | -0.01 | target is flat |
| 2026-10-12T17:46 | VWAP reversion | sell | PLTR | 7.29 | -0.01 | target is flat |
| 2026-10-12T17:46 | Z-score reversion | buy | XRP-USD | 3.30 | — | rebalance up |
| 2026-10-12T17:46 | Z-score reversion | sell | ETH-USD | 4.62 | -0.03 | stop-loss |
| 2026-10-12T17:40 | MFI reversion · 1h | buy | NVDA | 7.78 | — | rebalance up |
| 2026-10-12T17:40 | MFI reversion · 1h | buy | AMD | 7.78 | — | rebalance up |
| 2026-10-12T17:40 | MFI reversion · 1h | sell | SOXL | 15.55 | -0.03 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 17:52:05.000133+00:00 -> 2026-10-12 18:02:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
