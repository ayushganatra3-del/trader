# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T02:10:05.000123+00:00 · 56361 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 17.49 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 1545 decisions in 309 calls, $0.0216 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T02:10 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-12T02:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-12T02:10 | 1 / 4 / 0 | ETH-USD 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.33 | 16.33 | 0 | — | 16.04 | 5.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.61 | 15.61 | 20 | 70.0 | 17.89 | 3.60 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.74 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.91 | 3.91 | 0 | — | 6.40 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.64 | 1.88 | -9.06 | 232 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.31 | 3.58 | -3.28 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | 0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.53 | -1.47 | 0 | — | -0.64 | -0.12 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.06 | -1.94 | 188 | 30.3 | -2.36 | -0.84 | -8.79 | 162 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.06 | -2.94 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.19 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 95.50 | -4.50 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.41 | -5.59 | 0 | — | -3.37 | -0.85 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Trend pullback · 1h | trend | 91.71 | -8.29 | 109 | 22.9 | -12.91 | -4.84 | -16.41 | 75 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.80 | -11.20 | 404 | 33.2 | -12.12 | -3.50 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -4.89 | -0.99 | -17.04 | 78 |
| 24 | Max aggression: 5-day momentum | meta | 87.60 | -12.40 | 19 | 47.4 | -27.43 | -1.45 | -45.81 | 25 |
| 25 | Hold BTC | benchmark | 86.61 | -13.39 | 1 | 0.0 | -4.40 | -0.56 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.47 | -13.53 | 168 | 26.8 | -13.80 | -2.93 | -21.94 | 223 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 28 | Daily: Bullish score | daily | 84.39 | -15.61 | 16 | 18.8 | -9.91 | -1.69 | -19.56 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.18 | -15.82 | 2 | 0.0 | -6.49 | -0.62 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 82.95 | -17.05 | 72 | 13.9 | -22.99 | -4.88 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.26 | -17.74 | 186 | 18.8 | -21.91 | -3.73 | -29.87 | 274 |
| 33 | Stochastic reversion · 1h | reversion | 82.18 | -17.82 | 292 | 48.3 | -23.75 | -3.47 | -27.08 | 391 |
| 34 | Keltner breakout · 1h | breakout | 81.99 | -18.01 | 111 | 24.3 | -16.80 | -3.44 | -24.55 | 169 |
| 35 | Max aggression: 1-day momentum | meta | 81.19 | -18.80 | 27 | 25.9 | -17.50 | -0.43 | -57.50 | 40 |
| 36 | Opening range 15m | breakout | 80.85 | -19.15 | 501 | 31.3 | -18.42 | -4.93 | -21.11 | 722 |
| 37 | Volume breakout · 1h | breakout | 80.78 | -19.22 | 149 | 27.5 | -12.79 | -2.93 | -21.11 | 95 |
| 38 | Connors RSI(2) · 1h | reversion | 80.30 | -19.70 | 208 | 39.9 | -20.31 | -6.82 | -20.74 | 121 |
| 39 | Heikin-Ashi · 1h | trend | 80.24 | -19.76 | 418 | 24.6 | -34.80 | -6.42 | -38.20 | 658 |
| 40 | MFI reversion · 1h | reversion | 79.35 | -20.65 | 374 | 35.6 | -16.02 | -2.05 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.07 | -21.93 | 366 | 22.1 | -27.42 | -3.98 | -39.83 | 462 |
| 42 | CCI reversion · 1h | reversion | 77.98 | -22.02 | 332 | 45.2 | -28.01 | -4.33 | -31.08 | 449 |
| 43 | Bollinger breakout · 1h | breakout | 76.98 | -23.02 | 176 | 22.2 | -21.58 | -4.59 | -28.24 | 240 |
| 44 | Bollinger reversion · 1h | reversion | 75.98 | -24.02 | 286 | 41.6 | -27.67 | -4.22 | -34.84 | 367 |
| 45 | MACD zero-line · 1h | trend | 75.73 | -24.27 | 162 | 16.7 | -20.72 | -4.06 | -30.74 | 210 |
| 46 | Supertrend · 1h | trend | 75.39 | -24.61 | 168 | 13.1 | -28.51 | -5.00 | -36.14 | 220 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | RSI momentum · 1h | momentum | 74.94 | -25.06 | 159 | 12.6 | -25.79 | -3.90 | -37.48 | 215 |
| 49 | Daily: Momentum burst | daily | 74.82 | -25.18 | 27 | 11.1 | -33.22 | -4.55 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.42 | -25.58 | 103 | 10.7 | -27.06 | -4.58 | -37.26 | 117 |
| 51 | Triple EMA stack · 1h | trend | 74.07 | -25.93 | 144 | 14.6 | -25.00 | -4.12 | -35.90 | 206 |
| 52 | ROC + volume · 1h | momentum | 72.91 | -27.09 | 377 | 27.6 | -32.06 | -5.86 | -38.40 | 379 |
| 53 | Williams %R · 1h | reversion | 72.35 | -27.65 | 353 | 46.2 | -35.48 | -5.49 | -36.33 | 525 |
| 54 | Donchian 20/10 · 1h | breakout | 71.93 | -28.07 | 144 | 19.4 | -28.32 | -5.20 | -35.64 | 209 |
| 55 | OBV trend · 1h | momentum | 71.77 | -28.23 | 281 | 19.2 | -28.26 | -4.91 | -37.06 | 290 |
| 56 | Z-score reversion · 1h | reversion | 71.12 | -28.88 | 197 | 38.6 | -23.07 | -3.19 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.08 | -30.92 | 175 | 32.6 | -26.66 | -3.83 | -32.54 | 229 |
| 58 | VWAP momentum · 1h | momentum | 67.91 | -32.09 | 865 | 22.7 | -50.37 | -10.31 | -51.57 | 1221 |
| 59 | EMA 9/21 cross · 1h | trend | 67.20 | -32.80 | 254 | 9.8 | -33.53 | -6.34 | -41.65 | 338 |
| 60 | Agent (ML meta-label) | meta | 66.30 | -33.70 | 1750 | 24.7 | -12.26 | -1.44 | -26.41 | 362 |
| 61 | Candlestick reversal · 1h | reversion | 65.35 | -34.65 | 461 | 28.9 | -38.20 | -6.80 | -40.65 | 581 |
| 62 | Three white soldiers | momentum | 60.27 | -39.73 | 520 | 15.0 | -49.03 | -22.00 | -49.16 | 652 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.41 | -99.01 | 5277 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.74 | -25.17 | -80.39 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -43.29 | -93.66 | 2527 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.35 | -31.58 | -89.56 | 1924 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -39.51 | -91.33 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.34 | -32.45 | -90.35 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -51.52 | -97.84 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -54.24 | -96.42 | 3439 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -32.94 | -93.57 | 2354 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -33.64 | -83.50 | 1667 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -53.02 | -99.55 | 5985 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -42.21 | -92.37 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.53 | -37.38 | -95.53 | 3460 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.42 | -99.80 | 6133 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -42.35 | -92.03 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.58 | -24.81 | -75.85 | 1629 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -57.84 | -97.71 | 3520 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -58.61 | -98.83 | 4897 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.40 | -26.44 | -68.91 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -54.79 | -94.78 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.87 | -85.18 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -68.24 | -99.64 | 6332 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.53 | -31.51 | -89.55 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.61 | -19.59 | -77.65 | 1749 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.65 | -35.33 | -90.68 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -49.52 | -96.77 | 3843 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -56.04 | -89.22 | 2141 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.80 | -29.47 | -66.45 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.36 | -22.71 | -72.14 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.99 | -18.25 | -78.38 | 1683 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -47.01 | -97.28 | 4297 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.03 | -99.93 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T02:00 | Candlestick reversal · 1h | buy | XRP-USD | 6.13 | — | entry |
| 2026-11-12T02:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.79 | — | rebalance up |
| 2026-11-12T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 9.28 | -0.08 | exit signal |
| 2026-11-12T02:00 | MACD cross · 1h | sell | BTC-USD | 4.40 | -0.01 | exit signal |
| 2026-11-12T01:00 | Agent (ML meta-label) | buy | ETH-USD | 9.48 | — | entry |
| 2026-11-12T01:00 | CCI reversion · 1h | buy | XRP-USD | 3.98 | — | entry signal |
| 2026-11-12T01:00 | CCI reversion · 1h | buy | ETH-USD | 15.62 | — | entry signal |
| 2026-11-12T01:00 | MACD cross · 1h | sell | ETH-USD | 4.42 | 0.01 | exit signal |
| 2026-11-12T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 9.36 | — | entry signal |
| 2026-11-12T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 9.36 | — | entry signal |
| 2026-11-12T00:00 | MACD cross · 1h | sell | SOL-USD | 3.78 | -0.03 | exit signal |
| 2026-11-11T23:15 | Donchian 20/10 · 1h | sell | BTC-USD | 6.39 | -0.08 | stop-loss |
| 2026-11-11T23:15 | MACD zero-line · 1h | sell | BTC-USD | 4.27 | -0.04 | stop-loss |
| 2026-11-11T23:15 | EMA 9/21 cross · 1h | sell | SOL-USD | 4.68 | -0.11 | stop-loss |
| 2026-11-11T23:10 | MACD zero-line · 1h | buy | BTC-USD | 4.30 | — | entry |
| 2026-11-11T23:10 | MACD zero-line · 1h | sell | SOL-USD | 4.30 | -0.12 | stop-loss |
| 2026-11-11T23:00 | Squeeze breakout · 1h | sell | BTC-USD | 21.86 | -0.29 | exit signal |
| 2026-11-11T23:00 | Bollinger breakout · 1h | sell | BTC-USD | 10.95 | -0.13 | exit signal |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | buy | BTC-USD | 6.46 | — | entry |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | sell | SOL-USD | 6.46 | -0.10 | exit signal |
| 2026-11-11T23:00 | ROC + volume · 1h | sell | SOL-USD | 7.19 | -0.10 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | SOL-USD | 4.75 | -0.06 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | ETH-USD | 6.76 | -0.08 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | BTC-USD | 4.24 | -0.03 | exit signal |
| 2026-11-11T23:00 | ADX DI cross · 1h | sell | SOL-USD | 8.98 | -0.12 | exit signal |
| 2026-11-11T23:00 | MACD cross · 1h | buy | SOL-USD | 3.81 | — | entry |
| 2026-11-11T23:00 | MACD cross · 1h | sell | DOGE-USD | 3.81 | -0.07 | exit signal |
| 2026-11-11T22:46 | Squeeze breakout · 1h | sell | SOL-USD | 21.77 | -0.41 | stop-loss |
| 2026-11-11T22:46 | Bollinger breakout · 1h | buy | BTC-USD | 3.94 | — | rebalance up |
| 2026-11-11T22:46 | Bollinger breakout · 1h | sell | SOL-USD | 7.00 | -0.09 | stop-loss |
| 2026-11-11T22:46 | Bollinger breakout · 1h | sell | ETH-USD | 7.01 | -0.10 | stop-loss |
| 2026-11-11T22:46 | VWAP momentum · 1h | buy | ETH-USD | 3.73 | — | rebalance up |
| 2026-11-11T22:46 | VWAP momentum · 1h | sell | DOGE-USD | 6.09 | -0.13 | stop-loss |
| 2026-11-11T22:40 | Bollinger breakout · 1h | sell | DOGE-USD | 7.00 | -0.16 | stop-loss |
| 2026-11-11T22:14 | Volume breakout · 1h | sell | ETH-USD | 13.47 | -0.11 | target is flat |
| 2026-11-11T22:14 | Squeeze breakout · 1h | buy | BTC-USD | 22.15 | — | entry |
| 2026-11-11T22:14 | VWAP momentum · 1h | buy | DOGE-USD | 4.19 | — | rebalance up |
| 2026-11-11T20:15 | Agent (rotation) | sell | TSLA | 8.14 | -0.04 | selected signal exited |
| 2026-11-11T20:15 | Day trade: Stocks in Play ORB | sell | TSLA | 24.90 | -0.13 | target is flat |
| 2026-11-11T20:15 | Agent (ML meta-label) | sell | TQQQ | 9.48 | -0.03 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 02:10:05.000123+00:00 -> 2026-11-12 02:20:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
