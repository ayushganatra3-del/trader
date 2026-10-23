# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T03:15:05.000124+00:00 · 32589 ticks

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

Today: 2670 decisions in 534 calls, $0.0373 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T03:15 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-23T03:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T03:15 | 1 / 4 / 0 | ETH-USD 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.24 | 7.24 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.84 | 0.84 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.35 | 0.35 | 82 | 43.9 | -10.06 | -2.70 | -13.79 | 141 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.36 | -0.64 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.21 | -1.79 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.61 | -3.39 | 0 | — | 4.17 | 0.79 | -8.68 | 1 |
| 15 | Agent (rotation) | meta | 96.56 | -3.44 | 118 | 31.4 | -3.72 | -1.62 | -7.58 | 234 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.81 | -4.19 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.03 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.46 | -4.54 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.29 | -5.71 | 25 | 40.0 | -13.46 | -2.31 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -22.28 | -6.89 | -22.80 | 120 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.95 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.98 | -7.02 | 115 | 26.1 | -16.63 | -3.65 | -20.59 | 265 |
| 26 | Daily: Momentum burst | daily | 92.58 | -7.42 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.40 | -7.60 | 103 | 19.4 | -10.54 | -2.03 | -12.90 | 254 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -13.06 | -6.00 | -13.56 | 249 |
| 31 | Daily: Bullish score | daily | 89.75 | -10.25 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.45 | -10.55 | 104 | 27.9 | -11.51 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -12.69 | -2.27 | -14.45 | 107 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.97 | -11.03 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -18.96 | -4.61 | -19.81 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.57 | -12.43 | 68 | 11.8 | -23.50 | -4.22 | -26.14 | 144 |
| 37 | Stochastic reversion · 1h | reversion | 87.32 | -12.68 | 182 | 45.6 | -16.25 | -2.67 | -22.24 | 388 |
| 38 | Supertrend · 1h | trend | 86.96 | -13.04 | 104 | 15.4 | -23.81 | -4.64 | -27.15 | 218 |
| 39 | RSI momentum · 1h | momentum | 86.68 | -13.32 | 96 | 16.7 | -20.70 | -3.94 | -23.12 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.23 | -13.78 | 73 | 23.3 | -23.21 | -4.48 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.07 | -14.93 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 85.01 | -14.99 | 216 | 23.1 | -27.30 | -4.99 | -29.35 | 468 |
| 44 | Triple EMA stack · 1h | trend | 84.39 | -15.61 | 96 | 15.6 | -26.48 | -4.90 | -28.98 | 213 |
| 45 | Ichimoku · 1h | trend | 83.83 | -16.17 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.29 | -16.71 | 104 | 33.7 | -13.84 | -2.01 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.70 | -17.30 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.29 | -17.71 | 198 | 17.7 | -29.31 | -5.46 | -31.65 | 297 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.78 | 103 | 15.5 | -24.21 | -4.67 | -25.07 | 226 |
| 50 | Williams %R · 1h | reversion | 82.17 | -17.83 | 207 | 44.9 | -33.07 | -5.20 | -37.94 | 527 |
| 51 | MFI reversion · 1h | reversion | 82.04 | -17.96 | 245 | 31.4 | -18.32 | -2.78 | -21.11 | 148 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.42 | -18.17 | -45.42 | 601 |
| 53 | CCI reversion · 1h | reversion | 80.97 | -19.02 | 193 | 43.0 | -23.55 | -3.16 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.29 | -19.71 | 828 | 19.1 | -15.10 | -2.92 | -16.73 | 375 |
| 55 | Bollinger reversion · 1h | reversion | 80.11 | -19.89 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.99 | -20.01 | 260 | 23.5 | -43.26 | -9.25 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.72 | -20.28 | 233 | 24.0 | -28.53 | -5.11 | -29.04 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 78.21 | -21.79 | 155 | 11.6 | -32.96 | -6.22 | -33.48 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 77.84 | -22.16 | 90 | 23.3 | -22.15 | -3.95 | -24.19 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 77.33 | -22.67 | 245 | 29.0 | -38.69 | -6.90 | -39.95 | 566 |
| 61 | VWAP momentum · 1h | momentum | 76.99 | -23.01 | 499 | 21.4 | -50.18 | -10.24 | -50.94 | 1239 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.63 | -41.37 | 693 | 23.1 | -78.97 | -22.51 | -78.97 | 1682 |
| 64 | Volume breakout | breakout | 57.94 | -42.06 | 410 | 13.4 | -65.05 | -20.61 | -65.15 | 853 |
| 65 | Donchian 55/20 | breakout | 55.39 | -44.60 | 546 | 19.8 | -72.82 | -20.49 | -72.83 | 1271 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -68.57 | -24.37 | -68.57 | 1202 |
| 67 | EMA 20/50 cross | trend | 54.05 | -45.95 | 591 | 20.5 | -79.71 | -20.72 | -79.87 | 1445 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.93 | -17.18 | -77.05 | 1679 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -73.42 | -14.43 | -73.85 | 1523 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.86 | -32.78 | -98.89 | 5254 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.99 | -34.09 | -94.03 | 2555 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.58 | -24.51 | -88.68 | 1887 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.58 | -29.28 | -91.65 | 2340 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.73 | -24.68 | -90.84 | 2202 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -35.29 | -97.85 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -37.52 | -96.97 | 3559 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.48 | -28.48 | -94.48 | 2549 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.27 | -28.34 | -83.27 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -35.88 | -99.49 | 5875 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -30.99 | -93.02 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.18 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.68 | -99.79 | 6201 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -32.00 | -92.35 | 2332 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -39.04 | -97.67 | 3575 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -37.52 | -98.66 | 4768 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -37.84 | -94.69 | 2792 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -29.44 | -84.30 | 1785 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.37 | -99.60 | 6228 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -23.39 | -88.13 | 2197 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.71 | -26.72 | -88.72 | 2175 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -33.58 | -96.30 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.81 | -33.76 | -89.85 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -33.87 | -96.22 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.15 | -99.91 | 8249 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-23T02:00 | Volume breakout | sell | DOGE-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Donchian 55/20 | sell | BTC-USD | 13.86 | -0.13 | stop-loss |
| 2026-10-23T01:50 | Volume breakout | buy | XRP-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Volume breakout | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | BTC-USD | 13.99 | — | entry signal |
| 2026-10-23T01:45 | Volume breakout | buy | ETH-USD | 14.60 | — | entry signal |
| 2026-10-23T01:40 | Squeeze breakout | sell | DOGE-USD | 13.61 | -0.11 | target is flat |
| 2026-10-23T01:40 | Squeeze breakout | sell | BTC-USD | 13.62 | -0.11 | stop-loss |
| 2026-10-23T01:30 | EMA 20/50 cross | buy | BTC-USD | 2.68 | — | rebalance up |
| 2026-10-23T01:30 | EMA 20/50 cross | sell | SOL-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-23T01:25 | EMA 20/50 cross | buy | BTC-USD | 2.68 | — | rebalance up |
| 2026-10-23T01:25 | EMA 20/50 cross | sell | XRP-USD | 2.68 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 03:15:05.000124+00:00 -> 2026-10-23 03:25:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
