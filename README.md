# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T02:25:05.000160+00:00 · 26674 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1845 decisions in 369 calls, $0.0258 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T02:25 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-18T02:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T02:25 | 4 / 1 / 0 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -7.38 | -3.63 | -8.80 | 275 |
| 17 | Hold BTC | benchmark | 96.91 | -3.09 | 0 | — | 28.58 | 3.38 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.22 | -6.11 | -20.39 | 142 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.48 | -1.51 | -13.33 | 253 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.49 | 0.98 | -9.46 | 103 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.84 | -0.33 | -22.92 | 127 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.41 | -1.86 | -8.25 | 117 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.61 | -5.71 | -13.53 | 236 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.57 | -0.07 | -14.55 | 114 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.44 | 0.38 | -26.55 | 216 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.87 | 1.07 | -14.21 | 267 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.32 | -0.55 | -33.23 | 228 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -22.34 | -4.62 | -26.17 | 207 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.07 | -0.97 | -27.05 | 202 |
| 42 | MACD cross · 1h | trend | 88.15 | -11.85 | 177 | 22.0 | -15.69 | -2.05 | -29.51 | 459 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.24 | -7.73 | -25.57 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.78 | -0.60 | -33.87 | 316 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.55 | -13.45 | 142 | 43.7 | -20.96 | -3.83 | -22.11 | 368 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.78 | -4.50 | -23.64 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 2.18 | 0.47 | -21.63 | 212 |
| 50 | MFI reversion · 1h | reversion | 84.02 | -15.98 | 204 | 30.4 | -21.67 | -3.59 | -22.26 | 142 |
| 51 | Three white soldiers | momentum | 83.80 | -16.20 | 214 | 18.7 | -47.63 | -20.17 | -47.71 | 607 |
| 52 | Z-score reversion · 1h | reversion | 83.33 | -16.67 | 86 | 31.4 | -15.82 | -2.76 | -20.30 | 185 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.59 | -1.65 | -27.12 | 395 |
| 54 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -14.08 | -2.23 | -21.58 | 390 |
| 55 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -6.82 | -0.60 | -30.05 | 315 |
| 56 | VWAP momentum · 1h | momentum | 81.60 | -18.40 | 398 | 20.6 | -37.58 | -5.75 | -45.40 | 1258 |
| 57 | Heikin-Ashi · 1h | trend | 81.43 | -18.57 | 201 | 22.9 | -32.14 | -5.27 | -41.90 | 678 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.51 | -2.58 | -21.70 | 162 |
| 60 | Bollinger reversion · 1h | reversion | 79.86 | -20.14 | 144 | 30.6 | -30.78 | -6.42 | -32.71 | 350 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.20 | -2.64 | -26.49 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.61 | -6.45 | -36.31 | 538 |
| 63 | Volume breakout | breakout | 63.14 | -36.86 | 331 | 13.0 | -63.46 | -18.37 | -63.46 | 883 |
| 64 | ROC + volume | momentum | 62.66 | -37.34 | 555 | 21.8 | -75.75 | -17.74 | -77.58 | 1722 |
| 65 | Squeeze breakout | breakout | 62.03 | -37.97 | 440 | 14.5 | -62.95 | -18.02 | -64.60 | 1214 |
| 66 | RSI(14) reversion | reversion | 60.91 | -39.09 | 667 | 25.5 | -74.20 | -16.55 | -74.31 | 1628 |
| 67 | Donchian 55/20 | breakout | 60.27 | -39.73 | 445 | 17.5 | -68.99 | -14.60 | -72.10 | 1280 |
| 68 | EMA 20/50 cross | trend | 57.73 | -42.27 | 470 | 18.7 | -77.24 | -15.32 | -79.76 | 1449 |
| 69 | VWAP reversion | reversion | 54.51 | -45.49 | 701 | 23.8 | -73.07 | -15.51 | -73.26 | 1511 |
| 70 | Keltner breakout | breakout | 53.15 | -46.85 | 623 | 15.7 | -83.37 | -27.21 | -83.37 | 1831 |
| 71 | AI bee: Boozy | ai | 52.99 | -47.01 | 324 | 6.2 | — | — | — | — |
| 72 | Ichimoku | trend | 50.65 | -49.35 | 568 | 11.4 | -82.11 | -23.42 | -82.19 | 1733 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.17 | -98.65 | 5330 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -30.77 | -93.65 | 2604 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.57 | -20.48 | -87.54 | 1916 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -25.00 | -90.71 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.36 | -26.90 | -91.36 | 2312 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -32.73 | -97.47 | 3526 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.84 | -37.39 | -96.84 | 3639 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -26.18 | -94.32 | 2587 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.90 | -99.39 | 5817 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.41 | -26.03 | -91.42 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.13 | -32.03 | -96.13 | 3529 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.94 | -99.74 | 6238 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -29.78 | -91.78 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -39.36 | -97.51 | 3663 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.97 | -98.48 | 4770 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.78 | -33.82 | -93.78 | 2814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.90 | -99.53 | 6247 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.40 | -86.77 | 2171 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.14 | -27.18 | -88.16 | 2164 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.02 | -95.93 | 3818 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -34.26 | -89.40 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -34.06 | -95.86 | 4163 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.88 | -99.89 | 8307 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T02:05 | Squeeze breakout | sell | XRP-USD | 15.44 | -0.15 | exit signal |
| 2026-10-18T02:05 | ROC + volume | sell | SOL-USD | 15.55 | -0.16 | stop-loss |
| 2026-10-18T02:05 | Ichimoku | sell | XRP-USD | 12.63 | -0.04 | exit signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | XRP-USD | 11.18 | — | entry signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | SOL-USD | 16.34 | — | entry signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | ETH-USD | 16.34 | — | entry signal |
| 2026-10-18T02:00 | VWAP momentum · 1h | buy | BTC-USD | 16.34 | — | entry signal |
| 2026-10-18T02:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.32 | — | entry signal |
| 2026-10-18T02:00 | Heikin-Ashi · 1h | buy | ETH-USD | 20.39 | — | entry signal |
| 2026-10-18T02:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.39 | — | entry signal |
| 2026-10-18T02:00 | Three white soldiers | sell | XRP-USD | 20.89 | -0.20 | stop-loss |
| 2026-10-18T02:00 | Volume breakout | sell | BTC-USD | 15.76 | -0.07 | exit signal |
| 2026-10-18T02:00 | Squeeze breakout | sell | SOL-USD | 15.47 | -0.12 | stop-loss |
| 2026-10-18T02:00 | Squeeze breakout | sell | BTC-USD | 15.53 | -0.06 | stop-loss |
| 2026-10-18T02:00 | Keltner breakout | sell | SOL-USD | 13.23 | -0.15 | stop-loss |
| 2026-10-18T02:00 | Keltner breakout | sell | ETH-USD | 13.25 | -0.13 | stop-loss |
| 2026-10-18T02:00 | Keltner breakout | sell | BTC-USD | 13.30 | -0.08 | stop-loss |
| 2026-10-18T01:55 | AI bee: Boozy | sell | ETH-USD | 15.94 | -0.10 | Jev: sell |
| 2026-10-18T01:55 | Three white soldiers | sell | ETH-USD | 20.91 | -0.18 | stop-loss |
| 2026-10-18T01:55 | Three white soldiers | sell | DOGE-USD | 20.91 | -0.18 | exit signal |
| 2026-10-18T01:55 | Volume breakout | sell | SOL-USD | 15.71 | -0.12 | exit signal |
| 2026-10-18T01:45 | Three white soldiers | buy | XRP-USD | 21.09 | — | entry signal |
| 2026-10-18T01:45 | Three white soldiers | buy | ETH-USD | 21.09 | — | entry signal |
| 2026-10-18T01:45 | Three white soldiers | buy | DOGE-USD | 21.09 | — | entry signal |
| 2026-10-18T01:45 | Squeeze breakout | buy | XRP-USD | 15.60 | — | entry signal |
| 2026-10-18T01:45 | Keltner breakout | buy | SOL-USD | 13.37 | — | entry signal |
| 2026-10-18T01:45 | Keltner breakout | buy | ETH-USD | 13.37 | — | entry signal |
| 2026-10-18T01:40 | Volume breakout | buy | SOL-USD | 15.83 | — | entry signal |
| 2026-10-18T01:40 | Donchian 55/20 | buy | BTC-USD | 15.08 | — | entry signal |
| 2026-10-18T01:40 | ROC + volume | buy | SOL-USD | 15.70 | — | entry signal |
| 2026-10-18T01:39 | AI bee: Boozy | buy | ETH-USD | 16.04 | — | Jev: buy (buy p=0.72) |
| 2026-10-18T01:35 | AI bee: Boozy | sell | SOL-USD | 16.04 | -0.11 | Jev: sell |
| 2026-10-18T01:20 | AI bee: Boozy | buy | SOL-USD | 16.14 | — | Jev: buy (buy p=0.71) |
| 2026-10-18T01:20 | Keltner breakout | buy | BTC-USD | 13.38 | — | entry signal |
| 2026-10-18T01:11 | AI bee: Boozy | sell | ETH-USD | 16.14 | -0.10 | Jev: sell |
| 2026-10-18T01:05 | Squeeze breakout | buy | SOL-USD | 15.58 | — | entry signal |
| 2026-10-18T01:05 | EMA 20/50 cross | sell | SOL-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-18T01:01 | EMA 20/50 cross | buy | ETH-USD | 5.76 | — | rebalance up |
| 2026-10-18T01:01 | EMA 20/50 cross | sell | XRP-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-18T01:01 | EMA 20/50 cross | sell | BTC-USD | 2.88 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 02:25:05.000160+00:00 -> 2026-10-18 02:35:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
