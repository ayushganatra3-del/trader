# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T15:56:05.000109+00:00 · 23775 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.05 (-6.95%)

Closed trades 73, win rate 41.1%, fees £2.58, max drawdown -7.41%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 20517 decisions in 2355 calls, $0.2633 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T15:56 | 2 / 11 / 17 | cash |  |
| Breezy | 2026-10-15T15:56 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-15T15:56 | 3 / 26 / 1 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.77 | 4.77 | 0 | — | 4.30 | 2.04 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.95 | 3.95 | 1 | 100.0 | 4.55 | 1.22 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.34 | 1.94 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.42 | -0.73 | -9.61 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.39 | 0.39 | 0 | — | 3.93 | 1.55 | -5.18 | 1 |
| 6 | Hold SPY | benchmark | 100.01 | 0.01 | 0 | — | -0.82 | -0.43 | -3.31 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 10 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 58 | 39.7 | -11.45 | -3.20 | -13.89 | 116 |
| 11 | Copy: Insider buying | copy | 99.76 | -0.24 | 20 | 45.0 | -16.33 | -2.60 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.54 | -1.46 | 0 | — | -1.18 | -0.46 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 98.34 | -1.66 | 0 | — | 30.18 | 3.47 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.65 | -2.35 | 0 | — | -5.22 | -2.86 | -6.38 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Donchian 55/20 · 1h | breakout | 97.52 | -2.48 | 36 | 16.7 | 6.98 | 0.97 | -22.11 | 112 |
| 18 | Trend pullback · 1h | trend | 96.87 | -3.13 | 86 | 24.4 | -24.24 | -7.19 | -25.18 | 163 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.73 | -3.27 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | ADX DI cross · 1h | trend | 96.36 | -3.65 | 70 | 21.4 | -10.54 | -1.92 | -15.50 | 254 |
| 21 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 22 | Daily: Momentum burst | daily | 96.08 | -3.92 | 5 | 20.0 | -4.73 | -0.57 | -17.67 | 39 |
| 23 | Agent (rotation) | meta | 95.87 | -4.13 | 105 | 31.4 | -12.32 | -4.17 | -13.47 | 267 |
| 24 | Max aggression: 5-day momentum | meta | 93.90 | -6.10 | 8 | 37.5 | -5.80 | -0.22 | -34.64 | 26 |
| 25 | Parabolic SAR · 1h | trend | 93.79 | -6.21 | 93 | 22.6 | 2.27 | 0.47 | -22.46 | 282 |
| 26 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.87 | 0.90 | -9.46 | 102 |
| 27 | Gap and go | momentum | 93.58 | -6.42 | 65 | 12.3 | 9.17 | 2.30 | -6.78 | 202 |
| 28 | EMA 20/50 cross · 1h | trend | 93.58 | -6.42 | 51 | 15.7 | 5.83 | 0.83 | -23.13 | 134 |
| 29 | Daily: Bullish score | daily | 93.17 | -6.83 | 7 | 0.0 | -4.34 | -0.36 | -12.76 | 13 |
| 30 | Agent | meta | 93.05 | -6.95 | 73 | 41.1 | -8.23 | -3.95 | -8.99 | 244 |
| 31 | MACD cross · 1h | trend | 92.81 | -7.19 | 154 | 22.1 | -12.35 | -1.68 | -22.53 | 465 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 92.76 | -7.24 | 0 | — | 4.01 | 0.76 | -13.89 | 1 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 92.51 | -7.49 | 0 | — | -16.09 | -3.03 | -19.22 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 92.41 | -7.59 | 79 | 30.4 | 7.88 | 1.17 | -14.21 | 273 |
| 35 | RSI momentum · 1h | momentum | 92.09 | -7.91 | 73 | 17.8 | 1.78 | 0.41 | -25.51 | 222 |
| 36 | Supertrend · 1h | trend | 91.93 | -8.07 | 74 | 13.5 | 3.83 | 0.65 | -23.22 | 207 |
| 37 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | 10.63 | 1.48 | -12.68 | 118 |
| 38 | Opening range 30m | breakout | 90.80 | -9.20 | 169 | 23.1 | -12.58 | -3.61 | -17.60 | 567 |
| 39 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 77 | 16.9 | -6.89 | -0.51 | -32.35 | 232 |
| 40 | Ichimoku · 1h | trend | 90.41 | -9.59 | 51 | 15.7 | 0.89 | 0.31 | -22.64 | 123 |
| 41 | Stochastic reversion · 1h | reversion | 90.37 | -9.62 | 128 | 44.5 | -18.86 | -3.49 | -21.33 | 354 |
| 42 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -13.10 | -4.21 | -14.89 | 129 |
| 43 | MFI reversion · 1h | reversion | 89.84 | -10.16 | 183 | 29.0 | -17.47 | -3.02 | -20.20 | 145 |
| 44 | Connors RSI(2) · 1h | reversion | 89.60 | -10.40 | 141 | 39.7 | -23.30 | -6.97 | -24.89 | 248 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -17.22 | -0.64 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.42 | -11.57 | 164 | 18.9 | -10.99 | -0.94 | -35.23 | 319 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.42 | -1.85 | -28.05 | 210 |
| 48 | MACD zero-line · 1h | trend | 87.76 | -12.24 | 74 | 16.2 | -21.89 | -4.18 | -22.81 | 225 |
| 49 | Z-score reversion · 1h | reversion | 87.71 | -12.29 | 70 | 32.9 | -11.17 | -1.99 | -17.27 | 178 |
| 50 | Agent (ML meta-label) | meta | 87.01 | -12.99 | 568 | 18.5 | -8.13 | -1.12 | -16.00 | 433 |
| 51 | ROC + volume · 1h | momentum | 86.68 | -13.32 | 180 | 21.7 | -8.96 | -1.12 | -25.35 | 400 |
| 52 | Opening range 15m | breakout | 86.63 | -13.37 | 216 | 20.4 | -17.89 | -4.78 | -21.40 | 707 |
| 53 | Donchian 20/10 · 1h | breakout | 86.58 | -13.42 | 72 | 19.4 | 0.03 | 0.20 | -20.38 | 216 |
| 54 | Three white soldiers | momentum | 86.34 | -13.65 | 189 | 16.4 | -46.87 | -17.51 | -48.93 | 600 |
| 55 | VWAP momentum · 1h | momentum | 86.13 | -13.87 | 353 | 21.8 | -35.78 | -5.31 | -43.07 | 1251 |
| 56 | Heikin-Ashi · 1h | trend | 85.97 | -14.03 | 169 | 26.0 | -30.31 | -4.91 | -39.17 | 660 |
| 57 | EMA 9/21 cross · 1h | trend | 85.05 | -14.95 | 120 | 12.5 | -9.28 | -1.01 | -28.05 | 320 |
| 58 | Bollinger reversion · 1h | reversion | 83.87 | -16.12 | 130 | 30.8 | -27.90 | -6.04 | -31.47 | 338 |
| 59 | Williams %R · 1h | reversion | 83.42 | -16.58 | 164 | 42.1 | -32.20 | -5.30 | -34.97 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 82.97 | -17.03 | 60 | 21.7 | -14.48 | -2.64 | -18.95 | 173 |
| 61 | CCI reversion · 1h | reversion | 82.95 | -17.05 | 137 | 40.1 | -18.30 | -2.42 | -23.38 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 80.05 | -19.95 | 180 | 25.0 | -32.99 | -6.12 | -34.19 | 526 |
| 63 | ROC + volume | momentum | 67.65 | -32.34 | 493 | 21.7 | -73.86 | -16.29 | -76.44 | 1685 |
| 64 | RSI(14) reversion | reversion | 66.40 | -33.60 | 567 | 28.4 | -73.65 | -16.50 | -74.44 | 1566 |
| 65 | Volume breakout | breakout | 65.34 | -34.66 | 311 | 13.5 | -63.33 | -17.78 | -63.42 | 888 |
| 66 | Squeeze breakout | breakout | 64.75 | -35.25 | 404 | 14.6 | -62.71 | -17.32 | -63.39 | 1208 |
| 67 | Donchian 55/20 | breakout | 63.64 | -36.36 | 400 | 16.8 | -68.56 | -14.08 | -71.15 | 1278 |
| 68 | EMA 20/50 cross | trend | 61.87 | -38.13 | 421 | 18.8 | -76.93 | -14.85 | -78.49 | 1441 |
| 69 | VWAP reversion | reversion | 58.27 | -41.73 | 581 | 24.6 | -72.69 | -15.13 | -72.89 | 1433 |
| 70 | AI bee: Boozy | ai | 57.90 | -42.10 | 277 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.72 | -43.28 | 559 | 14.1 | -83.10 | -25.47 | -83.52 | 1842 |
| 72 | Supertrend | trend | 54.78 | -45.22 | 581 | 18.6 | -86.38 | -19.95 | -86.62 | 1907 |
| 73 | Ichimoku | trend | 53.93 | -46.07 | 493 | 9.7 | -81.84 | -22.12 | -82.11 | 1702 |
| 74 | AI bee: Bizzy | ai | 51.15 | -48.85 | 1017 | 8.4 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.91 | -98.64 | 5355 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.30 | -28.41 | -93.43 | 2573 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.49 | -23.83 | -90.69 | 2350 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.43 | -25.81 | -91.45 | 2315 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -31.30 | -97.47 | 3504 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.49 | -33.77 | -96.55 | 3558 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -24.33 | -94.38 | 2612 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.39 | -99.42 | 5752 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.04 | -24.77 | -91.21 | 2626 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.17 | -29.90 | -96.18 | 3540 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.29 | -99.73 | 6162 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.81 | -28.59 | -91.95 | 2361 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -36.07 | -97.45 | 3632 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.60 | -98.55 | 4695 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.38 | -30.81 | -93.54 | 2776 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.85 | -99.56 | 6167 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.23 | -21.89 | -86.50 | 2120 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.81 | -26.43 | -88.12 | 2123 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -31.93 | -96.14 | 3781 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -32.61 | -89.50 | 2117 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -32.85 | -95.91 | 4068 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.43 | -99.89 | 8197 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T15:50 | Supertrend · 1h | buy | MSTR | 13.44 | — | rebalance up |
| 2026-10-15T15:50 | Supertrend · 1h | sell | LABU | 18.25 | -0.18 | target is flat |
| 2026-10-15T15:45 | ROC + volume | sell | TNA | 6.12 | 0.06 | exit signal |
| 2026-10-15T15:35 | Volume breakout | sell | QQQ | 16.28 | -0.04 | exit signal |
| 2026-10-15T15:32 | AI bee: Bizzy | sell | MSTR | 7.99 | 0.26 | Jev: sell (sell p=0.60) after 50 min |
| 2026-10-15T15:30 | Agent (rotation) | sell | MSFT | 8.01 | 0.03 | selected signal exited |
| 2026-10-15T15:30 | Agent (ML meta-label) | buy | AMZN | 1.09 | — | entry |
| 2026-10-15T15:30 | Agent (ML meta-label) | buy | AMD | 3.35 | — | entry |
| 2026-10-15T15:30 | Agent (ML meta-label) | sell | GOOGL | 4.44 | -0.00 | rebalance down |
| 2026-10-15T15:30 | Agent | sell | AAPL | 18.57 | -0.05 | selected signal exited |
| 2026-10-15T15:30 | MFI reversion · 1h | buy | QQQ | 6.25 | — | entry signal |
| 2026-10-15T15:30 | MFI reversion · 1h | buy | PLTR | 8.97 | — | entry signal |
| 2026-10-15T15:30 | MFI reversion · 1h | buy | ETHU | 8.97 | — | entry signal |
| 2026-10-15T15:30 | MFI reversion · 1h | buy | AMZN | 8.97 | — | entry signal |
| 2026-10-15T15:30 | MFI reversion · 1h | sell | SOL-USD | 5.97 | 0.17 | rebalance down |
| 2026-10-15T15:30 | MFI reversion · 1h | sell | LABU | 9.29 | 0.69 | rebalance down |
| 2026-10-15T15:30 | MFI reversion · 1h | sell | IWM | 5.87 | 0.02 | rebalance down |
| 2026-10-15T15:30 | MFI reversion · 1h | sell | ETH-USD | 6.00 | 0.04 | rebalance down |
| 2026-10-15T15:30 | MFI reversion · 1h | sell | DOGE-USD | 6.03 | 0.07 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | UPRO | 1.63 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | SPY | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | MSTR | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | META | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | GOOGL | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | ETHU | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | COIN | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | BITX | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | buy | AMZN | 4.61 | — | entry signal |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | TNA | 6.23 | 0.08 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | SOL-USD | 4.59 | 0.01 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | MSFT | 4.58 | 0.02 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | LABU | 4.63 | 0.27 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | IWM | 4.56 | 0.02 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | ETH-USD | 4.66 | 0.14 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | DOGE-USD | 4.66 | 0.08 | rebalance down |
| 2026-10-15T15:30 | CCI reversion · 1h | sell | BTC-USD | 4.58 | 0.00 | rebalance down |
| 2026-10-15T15:30 | Williams %R · 1h | buy | MSFT | 3.38 | — | entry signal |
| 2026-10-15T15:30 | Williams %R · 1h | buy | AMD | 4.16 | — | entry signal |
| 2026-10-15T15:30 | Williams %R · 1h | sell | LABU | 7.01 | 0.34 | exit signal |
| 2026-10-15T15:30 | Stochastic reversion · 1h | buy | SOXL | 7.06 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 15:56:05.000109+00:00 -> 2026-10-15 16:06:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
