# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T04:45:05.000159+00:00 · 32668 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 3855 decisions in 771 calls, $0.0538 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T04:45 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-23T04:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T04:45 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| VWAP momentum | NVDA | 1.72 | +2.48% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.21 | 7.21 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.34 | 0.34 | 82 | 43.9 | -9.55 | -2.54 | -13.79 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.33 | -0.67 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.55 | -3.45 | 118 | 31.4 | -3.69 | -1.56 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 96.34 | -3.66 | 0 | — | 5.10 | 0.93 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.79 | -4.21 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.03 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.44 | -4.56 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.27 | -5.73 | 25 | 40.0 | -14.11 | -2.47 | -20.50 | 73 |
| 22 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.63 | -6.86 | -22.15 | 119 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.95 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.96 | -7.04 | 115 | 26.1 | -16.86 | -3.72 | -20.59 | 263 |
| 26 | Daily: Momentum burst | daily | 92.56 | -7.44 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.25 | -7.75 | 103 | 19.4 | -11.78 | -2.29 | -12.90 | 259 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -12.00 | -6.05 | -12.51 | 249 |
| 31 | Daily: Bullish score | daily | 89.73 | -10.27 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.44 | -10.56 | 104 | 27.9 | -11.51 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -12.69 | -2.27 | -14.45 | 107 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.95 | -11.05 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -16.52 | -4.68 | -17.40 | 127 |
| 36 | EMA 20/50 cross · 1h | trend | 87.55 | -12.45 | 68 | 11.8 | -23.34 | -4.21 | -25.78 | 143 |
| 37 | Stochastic reversion · 1h | reversion | 87.30 | -12.70 | 182 | 45.6 | -16.26 | -2.67 | -22.24 | 388 |
| 38 | Supertrend · 1h | trend | 86.95 | -13.05 | 104 | 15.4 | -23.81 | -4.64 | -27.15 | 218 |
| 39 | RSI momentum · 1h | momentum | 86.67 | -13.33 | 96 | 16.7 | -20.81 | -3.97 | -22.09 | 212 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.22 | -13.78 | 73 | 23.3 | -23.75 | -4.61 | -24.51 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.06 | -14.94 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.83 | -15.17 | 216 | 23.1 | -27.08 | -4.94 | -29.35 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.37 | -15.63 | 96 | 15.6 | -26.46 | -4.89 | -28.98 | 213 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.18 | -16.82 | 104 | 33.7 | -13.93 | -2.02 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.68 | -17.32 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.27 | -17.73 | 198 | 17.7 | -28.86 | -5.39 | -31.02 | 296 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.78 | 103 | 15.5 | -23.86 | -4.62 | -25.07 | 226 |
| 50 | Williams %R · 1h | reversion | 82.11 | -17.89 | 207 | 44.9 | -33.11 | -5.21 | -37.94 | 527 |
| 51 | MFI reversion · 1h | reversion | 81.99 | -18.01 | 245 | 31.4 | -18.39 | -2.79 | -21.11 | 148 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.42 | -18.17 | -45.42 | 601 |
| 53 | CCI reversion · 1h | reversion | 80.71 | -19.29 | 194 | 42.8 | -23.78 | -3.20 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.24 | -19.76 | 829 | 19.1 | -17.45 | -3.28 | -18.46 | 400 |
| 55 | Bollinger reversion · 1h | reversion | 80.09 | -19.91 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.90 | -20.11 | 260 | 23.5 | -43.31 | -9.27 | -44.09 | 670 |
| 57 | ROC + volume · 1h | momentum | 79.71 | -20.29 | 233 | 24.0 | -27.99 | -4.99 | -29.05 | 379 |
| 58 | EMA 9/21 cross · 1h | trend | 78.19 | -21.81 | 155 | 11.6 | -32.03 | -6.02 | -33.29 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 77.76 | -22.24 | 90 | 23.3 | -23.52 | -4.26 | -24.65 | 197 |
| 60 | Candlestick reversal · 1h | reversion | 77.25 | -22.75 | 245 | 29.0 | -39.90 | -7.13 | -41.06 | 575 |
| 61 | VWAP momentum · 1h | momentum | 76.97 | -23.03 | 499 | 21.4 | -50.47 | -10.33 | -50.94 | 1241 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.45 | -41.55 | 696 | 23.0 | -78.26 | -22.81 | -78.26 | 1680 |
| 64 | Volume breakout | breakout | 57.88 | -42.12 | 411 | 13.4 | -65.09 | -20.64 | -65.19 | 853 |
| 65 | Donchian 55/20 | breakout | 55.05 | -44.95 | 550 | 19.6 | -72.99 | -20.61 | -72.99 | 1271 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -68.57 | -24.37 | -68.57 | 1202 |
| 67 | EMA 20/50 cross | trend | 53.88 | -46.12 | 591 | 20.5 | -79.77 | -20.81 | -79.86 | 1445 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -77.22 | -17.40 | -77.54 | 1683 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -73.44 | -14.45 | -73.81 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -32.84 | -98.87 | 5264 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.95 | -34.08 | -93.95 | 2554 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.46 | -24.50 | -88.51 | 1886 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.51 | -29.26 | -91.52 | 2339 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.72 | -24.75 | -90.85 | 2201 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -35.48 | -97.84 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -37.72 | -96.95 | 3558 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.62 | -28.53 | -94.62 | 2560 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.27 | -28.34 | -83.27 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.50 | -36.14 | -99.50 | 5879 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.86 | -31.46 | -92.86 | 2621 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -30.21 | -95.65 | 3421 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.93 | -99.78 | 6200 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -31.73 | -92.26 | 2330 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -39.38 | -97.69 | 3575 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -37.76 | -98.66 | 4767 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -38.03 | -94.72 | 2792 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -29.56 | -84.39 | 1785 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.47 | -99.60 | 6225 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -23.39 | -88.13 | 2197 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.70 | -26.70 | -88.71 | 2175 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.31 | -33.84 | -96.31 | 3800 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.86 | -34.00 | -89.87 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.24 | -34.09 | -96.24 | 4137 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.43 | -99.91 | 8248 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T04:30 | Donchian 55/20 | sell | ETH-USD | 13.74 | -0.15 | exit signal |
| 2026-10-23T04:30 | Donchian 55/20 | sell | BTC-USD | 13.76 | -0.12 | exit signal |
| 2026-10-23T04:20 | Donchian 55/20 | sell | DOGE-USD | 14.00 | -0.01 | target is flat |
| 2026-10-23T04:05 | Agent (ML meta-label) | buy | XRP-USD | 3.82 | — | entry |
| 2026-10-23T04:00 | CCI reversion · 1h | buy | XRP-USD | 9.27 | — | rebalance up |
| 2026-10-23T04:00 | CCI reversion · 1h | sell | DOGE-USD | 11.61 | 0.04 | exit signal |
| 2026-10-23T04:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.00 | — | entry signal |
| 2026-10-23T03:45 | Agent (ML meta-label) | sell | XRP-USD | 2.27 | -0.01 | selected signal exited |
| 2026-10-23T03:40 | Agent (ML meta-label) | buy | XRP-USD | 2.28 | — | entry |
| 2026-10-23T03:35 | ROC + volume | sell | ETH-USD | 14.61 | -0.09 | exit signal |
| 2026-10-23T03:35 | ROC + volume | sell | BTC-USD | 14.60 | -0.09 | exit signal |
| 2026-10-23T03:20 | Volume breakout | sell | BTC-USD | 14.39 | -0.11 | exit signal |
| 2026-10-23T03:20 | Donchian 55/20 | sell | XRP-USD | 13.55 | -0.14 | stop-loss |
| 2026-10-23T03:20 | ROC + volume | sell | XRP-USD | 14.54 | -0.15 | stop-loss |
| 2026-10-23T03:05 | EMA 20/50 cross | buy | SOL-USD | 2.70 | — | rebalance up |
| 2026-10-23T03:00 | Agent (ML meta-label) | sell | ETH-USD | 3.99 | 0.03 | selected signal exited |
| 2026-10-23T03:00 | Williams %R · 1h | sell | ETH-USD | 8.23 | 0.06 | exit signal |
| 2026-10-23T03:00 | Williams %R · 1h | sell | DOGE-USD | 8.24 | 0.08 | exit signal |
| 2026-10-23T03:00 | Williams %R · 1h | sell | BTC-USD | 8.18 | 0.02 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | ETH-USD | 8.04 | 0.06 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | DOGE-USD | 7.42 | -0.01 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.85 | 0.01 | exit signal |
| 2026-10-23T03:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.16 | — | entry signal |
| 2026-10-23T03:00 | ADX DI cross · 1h | buy | ETH-USD | 22.29 | — | entry signal |
| 2026-10-23T02:35 | Volume breakout | buy | BTC-USD | 14.50 | — | entry signal |
| 2026-10-23T02:35 | Donchian 55/20 | buy | XRP-USD | 13.69 | — | entry signal |
| 2026-10-23T02:35 | Donchian 55/20 | buy | ETH-USD | 13.88 | — | entry signal |
| 2026-10-23T02:35 | Donchian 55/20 | buy | BTC-USD | 13.88 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | XRP-USD | 14.70 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | ETH-USD | 14.70 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | BTC-USD | 14.70 | — | entry signal |
| 2026-10-23T02:05 | Donchian 55/20 | sell | XRP-USD | 13.77 | -0.16 | stop-loss |
| 2026-10-23T02:05 | Donchian 55/20 | sell | SOL-USD | 13.83 | -0.15 | stop-loss |
| 2026-10-23T02:05 | EMA 20/50 cross | sell | BTC-USD | 8.04 | -0.07 | stop-loss |
| 2026-10-23T02:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.11 | -0.04 | exit signal |
| 2026-10-23T02:00 | MACD cross · 1h | buy | SOL-USD | 9.65 | — | entry |
| 2026-10-23T02:00 | MACD cross · 1h | sell | DOGE-USD | 4.88 | -0.00 | rebalance down |
| 2026-10-23T02:00 | MACD cross · 1h | sell | BTC-USD | 4.77 | -0.03 | rebalance down |
| 2026-10-23T02:00 | Volume breakout | sell | XRP-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Volume breakout | sell | ETH-USD | 14.48 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 04:45:05.000159+00:00 -> 2026-10-23 04:55:05.000159+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
