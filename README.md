# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T15:25:05.000125+00:00 · 20335 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.44 (-4.56%)

Closed trades 55, win rate 52.7%, fees £2.15, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TNA | 19.07 | -0.03 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 16059 decisions in 2232 calls, $0.2110 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T15:25 | 0 / 20 / 9 | NANC 18%, META 15% |  |
| Breezy | 2026-10-12T15:25 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-12T15:25 | 1 / 26 / 2 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.40 | 2.40 | 0 | — | -0.85 | -0.34 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.33 | 2.33 | 39 | 41.0 | -8.29 | -2.51 | -13.79 | 116 |
| 3 | Copy: Insider buying | copy | 102.14 | 2.15 | 14 | 57.1 | -12.51 | -2.05 | -20.64 | 71 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 5.20 | 2.31 | -3.27 | 16 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.26 | 1.26 | 0 | — | 1.81 | 0.88 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.25 | 1.25 | 0 | — | 0.75 | 0.49 | -3.66 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.46 | 0.46 | 0 | — | -5.75 | -0.96 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.45 | 0.45 | 0 | — | -1.44 | -0.77 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 6 | 50.0 | -3.90 | -1.29 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 10 | 30.0 | 4.56 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.76 | -0.24 | 0 | — | -4.06 | -1.87 | -5.36 | 1 |
| 15 | Daily: SMA 20/50 cross · AAPL | daily | 99.72 | -0.28 | 0 | — | 2.76 | 1.11 | -5.18 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.83 | -1.17 | 0 | — | 29.68 | 3.49 | -8.68 | 1 |
| 19 | Max aggression: 1-day momentum | meta | 98.72 | -1.28 | 11 | 36.4 | -15.97 | -0.57 | -37.31 | 42 |
| 20 | Donchian 55/20 · 1h | breakout | 98.16 | -1.84 | 31 | 12.9 | 12.34 | 1.53 | -16.84 | 116 |
| 21 | Trend pullback · 1h | trend | 97.85 | -2.15 | 78 | 23.1 | -22.86 | -6.35 | -25.60 | 167 |
| 22 | Stochastic reversion · 1h | reversion | 97.76 | -2.24 | 96 | 53.1 | -11.89 | -2.33 | -14.36 | 335 |
| 23 | Daily: Bullish score | daily | 97.53 | -2.47 | 4 | 0.0 | 0.43 | 0.25 | -12.76 | 11 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.38 | -2.62 | 0 | — | 9.84 | 1.62 | -8.33 | 1 |
| 25 | Three white soldiers · 1h | momentum | 97.21 | -2.79 | 7 | 0.0 | -3.31 | -2.55 | -4.50 | 27 |
| 26 | Z-score reversion · 1h | reversion | 97.14 | -2.86 | 44 | 43.2 | 3.78 | 0.88 | -8.60 | 156 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.99 | -0.29 | -17.67 | 39 |
| 28 | Agent (rotation) | meta | 96.56 | -3.44 | 82 | 29.3 | -10.58 | -3.38 | -15.50 | 269 |
| 29 | ADX DI cross · 1h | trend | 96.42 | -3.58 | 61 | 19.7 | -0.09 | 0.14 | -13.84 | 259 |
| 30 | MACD cross · 1h | trend | 96.17 | -3.83 | 120 | 24.2 | -12.95 | -2.12 | -17.27 | 466 |
| 31 | Parabolic SAR · 1h | trend | 96.04 | -3.96 | 83 | 21.7 | 1.96 | 0.44 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.55 | -4.45 | 44 | 13.6 | 3.63 | 0.62 | -22.69 | 133 |
| 33 | Agent | meta | 95.44 | -4.56 | 55 | 52.7 | -9.15 | -5.11 | -10.29 | 234 |
| 34 | Supertrend · 1h | trend | 94.86 | -5.14 | 58 | 13.8 | 1.20 | 0.34 | -18.27 | 212 |
| 35 | MFI reversion · 1h | reversion | 93.92 | -6.08 | 122 | 34.4 | -7.20 | -1.07 | -16.91 | 125 |
| 36 | Gap and go | momentum | 93.88 | -6.12 | 58 | 12.1 | 8.49 | 2.16 | -6.20 | 202 |
| 37 | Squeeze breakout · 1h | breakout | 93.64 | -6.36 | 39 | 23.1 | 14.96 | 2.40 | -9.37 | 106 |
| 38 | Agent (aggressive) | meta | 93.44 | -6.56 | 26 | 42.3 | -6.12 | -2.68 | -8.60 | 108 |
| 39 | Agent (ML meta-label) | meta | 92.67 | -7.33 | 418 | 18.4 | -0.96 | -0.03 | -13.03 | 425 |
| 40 | RSI momentum · 1h | momentum | 92.56 | -7.44 | 66 | 15.2 | 0.65 | 0.28 | -21.53 | 228 |
| 41 | RSI(14) reversion · 1h | reversion | 92.27 | -7.73 | 30 | 30.0 | -3.14 | -0.57 | -9.03 | 141 |
| 42 | Connors RSI(2) · 1h | reversion | 92.21 | -7.79 | 114 | 43.0 | -18.83 | -6.21 | -21.02 | 252 |
| 43 | Volume breakout · 1h | breakout | 91.74 | -8.26 | 62 | 21.0 | 8.44 | 1.30 | -12.60 | 119 |
| 44 | Bollinger reversion · 1h | reversion | 91.43 | -8.57 | 82 | 37.8 | -22.04 | -5.27 | -23.14 | 315 |
| 45 | Bollinger breakout · 1h | breakout | 91.02 | -8.98 | 74 | 28.4 | 7.67 | 1.13 | -13.96 | 278 |
| 46 | Ichimoku · 1h | trend | 90.91 | -9.09 | 47 | 17.0 | 0.84 | 0.31 | -22.17 | 125 |
| 47 | Triple EMA stack · 1h | trend | 90.78 | -9.22 | 71 | 15.5 | -7.84 | -0.64 | -32.16 | 229 |
| 48 | Opening range 30m | breakout | 90.07 | -9.93 | 149 | 22.1 | -15.10 | -4.58 | -15.49 | 566 |
| 49 | Williams %R · 1h | reversion | 89.75 | -10.25 | 130 | 46.9 | -25.94 | -4.39 | -27.33 | 503 |
| 50 | CCI reversion · 1h | reversion | 89.23 | -10.77 | 111 | 45.9 | -6.43 | -0.75 | -14.35 | 406 |
| 51 | Candlestick reversal · 1h | reversion | 88.71 | -11.29 | 126 | 31.7 | -28.69 | -5.62 | -29.13 | 504 |
| 52 | OBV trend · 1h | momentum | 88.64 | -11.37 | 150 | 18.7 | -9.57 | -0.91 | -28.82 | 322 |
| 53 | VWAP momentum · 1h | momentum | 88.58 | -11.42 | 297 | 23.2 | -33.07 | -4.93 | -39.99 | 1265 |
| 54 | MACD zero-line · 1h | trend | 88.28 | -11.72 | 67 | 17.9 | -14.22 | -2.24 | -20.98 | 232 |
| 55 | Donchian 20/10 · 1h | breakout | 88.25 | -11.75 | 63 | 17.5 | -0.95 | 0.09 | -19.17 | 218 |
| 56 | Heikin-Ashi · 1h | trend | 88.23 | -11.77 | 147 | 27.2 | -29.82 | -4.93 | -37.33 | 686 |
| 57 | EMA 9/21 cross · 1h | trend | 87.64 | -12.36 | 106 | 13.2 | -8.84 | -0.99 | -22.59 | 333 |
| 58 | Opening range 15m | breakout | 87.42 | -12.58 | 175 | 20.6 | -17.50 | -4.91 | -18.65 | 688 |
| 59 | Max aggression: 5-day momentum | meta | 87.39 | -12.61 | 7 | 28.6 | -14.89 | -1.10 | -34.64 | 28 |
| 60 | Keltner breakout · 1h | breakout | 86.89 | -13.11 | 45 | 20.0 | -11.75 | -1.29 | -26.55 | 219 |
| 61 | Three white soldiers | momentum | 86.62 | -13.38 | 148 | 16.9 | -48.53 | -23.19 | -48.67 | 586 |
| 62 | ROC + volume · 1h | momentum | 86.12 | -13.88 | 135 | 21.5 | -9.69 | -1.14 | -24.55 | 412 |
| 63 | ROC + volume | momentum | 73.05 | -26.95 | 410 | 22.9 | -73.03 | -16.55 | -74.41 | 1678 |
| 64 | RSI(14) reversion | reversion | 70.98 | -29.02 | 395 | 26.1 | -72.75 | -17.96 | -72.76 | 1483 |
| 65 | Squeeze breakout | breakout | 69.95 | -30.05 | 345 | 15.1 | -62.04 | -17.81 | -62.36 | 1224 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.14 | -17.64 | -62.29 | 899 |
| 67 | EMA 20/50 cross | trend | 68.12 | -31.88 | 351 | 19.7 | -76.38 | -15.00 | -76.42 | 1434 |
| 68 | Donchian 55/20 | breakout | 67.30 | -32.70 | 355 | 17.7 | -68.22 | -14.42 | -68.81 | 1295 |
| 69 | VWAP reversion | reversion | 66.28 | -33.72 | 415 | 25.3 | -71.12 | -15.69 | -71.19 | 1416 |
| 70 | Keltner breakout | breakout | 60.82 | -39.18 | 474 | 14.3 | -83.59 | -27.49 | -83.62 | 1851 |
| 71 | Supertrend | trend | 60.59 | -39.41 | 492 | 19.3 | -85.92 | -20.72 | -86.00 | 1897 |
| 72 | AI bee: Boozy | ai | 60.37 | -39.63 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.64 | -42.36 | 429 | 10.0 | -82.10 | -22.94 | -82.14 | 1745 |
| 74 | MFI reversion | reversion | 56.07 | -43.93 | 546 | 20.1 | -87.76 | -28.11 | -87.76 | 2108 |
| 75 | Z-score reversion | reversion | 55.89 | -44.11 | 538 | 21.4 | -85.57 | -22.87 | -85.57 | 2064 |
| 76 | AI bee: Bizzy | ai | 55.86 | -44.14 | 874 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.32 | -45.68 | 570 | 10.0 | -89.16 | -34.41 | -89.16 | 2103 |
| 78 | Donchian 20/10 | breakout | 52.54 | -47.46 | 666 | 17.7 | -90.81 | -25.73 | -90.83 | 2650 |
| 79 | MACD zero-line | trend | 51.61 | -48.39 | 615 | 14.5 | -91.31 | -29.12 | -91.34 | 2338 |
| 80 | RSI momentum | momentum | 51.14 | -48.86 | 642 | 16.5 | -90.41 | -25.33 | -90.51 | 2370 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -30.27 | -98.61 | 5352 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.39 | -26.87 | -91.39 | 2339 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -29.63 | -93.21 | 2597 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -32.74 | -97.34 | 3513 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -35.01 | -96.41 | 3601 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -25.82 | -94.41 | 2656 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.22 | -99.35 | 5612 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.40 | -96.39 | 3596 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.22 | -99.73 | 6137 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -37.31 | -97.33 | 3672 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.57 | -98.49 | 4671 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.41 | -32.58 | -93.42 | 2794 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.53 | -99.53 | 6104 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.94 | -95.87 | 3721 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -34.18 | -95.70 | 4046 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.25 | -99.89 | 8230 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T15:25 | Agent (ML meta-label) | buy | UPRO | 3.98 | — | entry |
| 2026-10-12T15:25 | Agent (ML meta-label) | buy | LABU | 6.18 | — | following Donchian 20/10 |
| 2026-10-12T15:25 | Agent (ML meta-label) | sell | TECL | 3.80 | -0.01 | selected signal exited |
| 2026-10-12T15:25 | Agent (ML meta-label) | sell | QQQ | 5.55 | -0.01 | selected signal exited |
| 2026-10-12T15:25 | Volume breakout · 1h | sell | MSFT | 22.96 | 0.02 | target is flat |
| 2026-10-12T15:25 | MFI reversion | buy | GOOGL | 9.35 | — | entry signal |
| 2026-10-12T15:25 | Volume breakout | sell | META | 17.50 | 0.07 | exit signal |
| 2026-10-12T15:25 | ROC + volume | buy | MSFT | 18.26 | — | entry |
| 2026-10-12T15:20 | Agent (ML meta-label) | buy | TQQQ | 4.73 | — | rebalance up |
| 2026-10-12T15:20 | Agent (ML meta-label) | sell | LABU | 5.55 | -0.01 | selected signal exited |
| 2026-10-12T15:20 | Opening range 30m | buy | META | 22.55 | — | entry signal |
| 2026-10-12T15:20 | ROC + volume | buy | META | 18.30 | — | entry |
| 2026-10-12T15:15 | AI bee: Bizzy | buy | META | 8.36 | — | Jev: buy (buy p=0.60) |
| 2026-10-12T15:15 | Agent (ML meta-label) | buy | TQQQ | 1.06 | — | entry |
| 2026-10-12T15:15 | Agent (ML meta-label) | buy | TECL | 3.80 | — | entry |
| 2026-10-12T15:15 | Agent (ML meta-label) | buy | QQQ | 5.56 | — | entry |
| 2026-10-12T15:15 | Agent (ML meta-label) | buy | LABU | 5.56 | — | following Donchian 20/10 |
| 2026-10-12T15:15 | Agent (ML meta-label) | buy | IWM | 5.56 | — | entry |
| 2026-10-12T15:15 | Volume breakout · 1h | buy | MSFT | 22.94 | — | entry |
| 2026-10-12T15:15 | RSI momentum | buy | ETHU | 7.65 | — | entry signal |
| 2026-10-12T15:15 | RSI momentum | sell | MSFT | 2.58 | 0.00 | rebalance down |
| 2026-10-12T15:15 | RSI momentum | sell | GOOGL | 2.58 | 0.00 | rebalance down |
| 2026-10-12T15:15 | Trend pullback | sell | UPRO | 12.64 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T15:15 | Trend pullback | sell | SPY | 12.64 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T15:15 | Trend pullback | sell | PLTR | 12.61 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-12T15:10 | Agent (ML meta-label) | sell | UPRO | 6.61 | 0.00 | selected signal exited |
| 2026-10-12T15:10 | Agent (ML meta-label) | sell | QQQ | 2.82 | -0.00 | selected signal exited |
| 2026-10-12T15:10 | Agent (ML meta-label) | sell | LABU | 6.65 | 0.05 | selected signal exited |
| 2026-10-12T15:10 | Agent (ML meta-label) | sell | IWM | 5.45 | -0.00 | selected signal exited |
| 2026-10-12T15:10 | Volume breakout · 1h | sell | MSFT | 22.92 | -0.03 | target is flat |
| 2026-10-12T15:10 | Opening range 15m | buy | META | 21.86 | — | entry signal |
| 2026-10-12T15:10 | ROC + volume | sell | SQQQ | 14.83 | 0.16 | exit signal |
| 2026-10-12T15:05 | Agent (ML meta-label) | buy | QQQ | 2.82 | — | entry |
| 2026-10-12T15:05 | Agent (ML meta-label) | buy | IWM | 5.46 | — | entry |
| 2026-10-12T15:05 | Agent (ML meta-label) | sell | TECL | 7.71 | -0.01 | selected signal exited |
| 2026-10-12T15:05 | Volume breakout · 1h | buy | MSFT | 22.95 | — | entry |
| 2026-10-12T15:05 | ROC + volume · 1h | buy | TSLA | 6.62 | — | entry |
| 2026-10-12T15:05 | MFI reversion | sell | SPY | 9.35 | -0.01 | target is flat |
| 2026-10-12T15:05 | Keltner breakout | buy | GOOGL | 15.21 | — | entry signal |
| 2026-10-12T15:05 | Opening range 15m | buy | GOOGL | 21.87 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 15:25:05.000125+00:00 -> 2026-10-12 15:35:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
