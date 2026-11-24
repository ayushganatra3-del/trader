# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T11:10:05.000173+00:00 · 71731 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 8865 decisions in 1773 calls, $0.1240 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T11:10 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-24T11:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T11:10 | 1 / 4 / 0 | ETH-USD 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.67 | +10.14% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.12 | 15.12 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 0.77 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.76 | 3.76 | 0 | — | 2.64 | 1.06 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.10 | 0.06 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.07 | 0.06 | -7.48 | 149 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 95.20 | -4.80 | 0 | — | -6.09 | -1.50 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.29 | -7.71 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.03 | -3.50 | -9.16 | 33 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.62 | -9.38 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 89.83 | -10.17 | 58 | 39.7 | -8.96 | -1.74 | -14.79 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.75 | -10.24 | 163 | 46.0 | -7.82 | -1.42 | -20.49 | 153 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -2.99 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.35 | -13.65 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.46 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.71 | -7.31 | -21.88 | 81 |
| 25 | Parabolic SAR · 1h | trend | 80.09 | -19.91 | 204 | 28.4 | -28.23 | -7.68 | -29.41 | 189 |
| 26 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.58 | -5.78 | -25.97 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -16.11 | -4.19 | -18.44 | 88 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.04 | -6.77 | -23.30 | 660 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.15 | -8.03 | -30.15 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.35 | -6.46 | -25.21 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Supertrend · 1h | trend | 70.70 | -29.30 | 204 | 18.6 | -34.62 | -6.86 | -37.07 | 206 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 70.23 | -29.77 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 36 | ADX DI cross · 1h | trend | 69.58 | -30.42 | 253 | 19.0 | -37.66 | -6.75 | -40.30 | 278 |
| 37 | Hold BTC | benchmark | 69.32 | -30.68 | 3 | 0.0 | -30.30 | -5.23 | -36.10 | 1 |
| 38 | Daily: Momentum burst | daily | 69.12 | -30.88 | 30 | 13.3 | -37.24 | -5.04 | -37.81 | 25 |
| 39 | Bollinger breakout · 1h | breakout | 68.60 | -31.40 | 207 | 22.2 | -32.73 | -8.61 | -33.88 | 211 |
| 40 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -38.36 | -9.80 | -38.85 | 171 |
| 41 | EMA 20/50 cross · 1h | trend | 67.71 | -32.29 | 121 | 9.9 | -38.02 | -10.53 | -38.57 | 116 |
| 42 | Stochastic reversion · 1h | reversion | 66.24 | -33.76 | 395 | 40.8 | -33.30 | -3.58 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 65.98 | -34.02 | 322 | 19.9 | -41.46 | -10.81 | -41.52 | 237 |
| 44 | MACD zero-line · 1h | trend | 65.80 | -34.20 | 198 | 16.7 | -35.10 | -9.59 | -35.21 | 204 |
| 45 | Heikin-Ashi · 1h | trend | 64.52 | -35.48 | 527 | 22.2 | -46.72 | -9.50 | -47.76 | 629 |
| 46 | RSI momentum · 1h | momentum | 64.21 | -35.79 | 200 | 15.0 | -40.63 | -9.41 | -40.82 | 199 |
| 47 | MFI reversion · 1h | reversion | 63.51 | -36.49 | 486 | 32.9 | -32.09 | -4.67 | -37.87 | 185 |
| 48 | Max aggression: 5-day momentum | meta | 62.66 | -37.34 | 25 | 36.0 | -62.80 | -4.13 | -66.53 | 23 |
| 49 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -43.06 | -8.64 | -43.20 | 342 |
| 50 | Donchian 20/10 · 1h | breakout | 60.97 | -39.03 | 181 | 17.7 | -40.46 | -8.73 | -41.99 | 193 |
| 51 | Agent (ML meta-label) | meta | 59.48 | -40.52 | 2049 | 25.0 | -16.13 | -1.86 | -28.33 | 325 |
| 52 | EMA 9/21 cross · 1h | trend | 59.32 | -40.68 | 307 | 12.4 | -44.93 | -10.65 | -45.88 | 336 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.65 | -3.86 | -54.72 | 38 |
| 54 | MACD cross · 1h | trend | 58.78 | -41.22 | 467 | 21.4 | -49.89 | -9.73 | -50.99 | 512 |
| 55 | CCI reversion · 1h | reversion | 57.93 | -42.07 | 430 | 40.0 | -49.36 | -8.20 | -51.92 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.92 | -42.08 | 391 | 37.6 | -37.42 | -4.46 | -45.42 | 430 |
| 57 | Williams %R · 1h | reversion | 53.76 | -46.24 | 500 | 38.4 | -53.88 | -8.79 | -55.78 | 587 |
| 58 | VWAP momentum · 1h | momentum | 53.40 | -46.60 | 1054 | 21.8 | -58.08 | -13.45 | -58.23 | 1186 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.60 | -8.68 | -54.29 | 665 |
| 60 | RSI(14) reversion · 1h | reversion | 50.93 | -49.07 | 241 | 32.0 | -50.06 | -8.02 | -52.23 | 290 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -49.13 | -99.16 | 5352 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.19 | -33.77 | -84.43 | 1439 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.51 | -49.64 | -94.51 | 2436 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.62 | -32.01 | -90.62 | 1913 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.79 | -41.73 | -91.79 | 2254 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.66 | -28.62 | -89.73 | 1966 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -48.08 | -98.19 | 3434 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.02 | -53.13 | -97.02 | 3386 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -38.49 | -93.51 | 2114 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.35 | -35.00 | -83.36 | 1556 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -57.15 | -99.68 | 6296 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.22 | -38.50 | -93.22 | 2495 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -36.88 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -68.40 | -99.82 | 6145 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.27 | -44.13 | -93.27 | 2274 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.62 | -22.15 | -51.62 | 640 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.34 | -23.88 | -78.34 | 1602 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -58.41 | -97.79 | 3287 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -61.64 | -99.19 | 5125 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.13 | -27.24 | -71.16 | 1201 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -47.52 | -94.98 | 2669 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.45 | -37.04 | -85.45 | 1666 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -74.52 | -99.77 | 6550 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.33 | -30.94 | -91.34 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.46 | -20.13 | -83.47 | 1961 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.01 | -31.31 | -92.01 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -49.31 | -98.13 | 4057 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.40 | -48.05 | -90.40 | 2199 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.97 | -30.24 | -67.97 | 790 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.44 | -28.22 | -73.44 | 1164 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.00 | -18.86 | -84.07 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -49.62 | -98.00 | 4412 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -98.36 | -99.94 | 8286 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T11:00 | Donchian 55/20 · 1h | sell | XRP-USD | 18.81 | -0.39 | exit signal |
| 2026-11-24T11:00 | Donchian 20/10 · 1h | sell | XRP-USD | 15.19 | -0.32 | exit signal |
| 2026-11-24T11:00 | OBV trend · 1h | sell | XRP-USD | 16.26 | -0.38 | exit signal |
| 2026-11-24T10:00 | RSI momentum · 1h | sell | XRP-USD | 12.76 | -0.18 | exit signal |
| 2026-11-24T10:00 | RSI momentum · 1h | sell | DOGE-USD | 12.75 | -0.26 | exit signal |
| 2026-11-24T09:55 | EMA 20/50 cross · 1h | buy | DOGE-USD | 3.40 | — | rebalance up |
| 2026-11-24T09:00 | Triple EMA stack · 1h | sell | XRP-USD | 16.95 | -0.31 | exit signal |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 3.45 | — | rebalance up |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 5.03 | — | rebalance up |
| 2026-11-24T09:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 14.30 | -0.20 | exit signal |
| 2026-11-24T09:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 8.37 | -0.15 | exit signal |
| 2026-11-24T08:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.52 | -0.09 | exit signal |
| 2026-11-24T08:00 | Triple EMA stack · 1h | sell | DOGE-USD | 16.98 | -0.30 | exit signal |
| 2026-11-24T08:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.33 | -0.13 | exit signal |
| 2026-11-24T06:00 | Heikin-Ashi · 1h | buy | XRP-USD | 4.61 | — | entry signal |
| 2026-11-24T06:00 | Triple EMA stack · 1h | buy | DOGE-USD | 17.28 | — | entry signal |
| 2026-11-24T06:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 7.46 | — | entry signal |
| 2026-11-24T05:00 | CCI reversion · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-24T05:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.26 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 8.53 | — | entry signal |
| 2026-11-24T05:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 7.39 | 0.12 | exit signal |
| 2026-11-24T04:00 | Triple EMA stack · 1h | sell | DOGE-USD | 17.22 | 0.05 | exit signal |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | ETH-USD | 3.96 | — | entry |
| 2026-11-24T03:10 | Stochastic reversion · 1h | buy | DOGE-USD | 4.12 | — | rebalance up |
| 2026-11-24T03:10 | Stochastic reversion · 1h | sell | BTC-USD | 8.08 | -0.27 | stop-loss |
| 2026-11-24T03:10 | Connors RSI(2) · 1h | sell | SOL-USD | 19.37 | -0.94 | stop-loss |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | XRP-USD | 6.31 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | buy | DOGE-USD | 4.88 | — | rebalance up |
| 2026-11-24T03:10 | EMA 20/50 cross · 1h | sell | ETH-USD | 14.13 | -0.38 | stop-loss |
| 2026-11-24T03:00 | Donchian 55/20 · 1h | sell | SOL-USD | 18.77 | -0.43 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | SOL-USD | 15.16 | -0.34 | exit signal |
| 2026-11-24T03:00 | Donchian 20/10 · 1h | sell | BTC-USD | 15.10 | -0.41 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | XRP-USD | 3.64 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | buy | DOGE-USD | 3.71 | — | rebalance up |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | SOL-USD | 9.09 | -0.21 | exit signal |
| 2026-11-24T03:00 | RSI momentum · 1h | sell | BTC-USD | 9.06 | -0.24 | exit signal |
| 2026-11-24T03:00 | ADX DI cross · 1h | sell | BTC-USD | 5.22 | -0.14 | exit signal |
| 2026-11-24T03:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.39 | -0.09 | exit signal |
| 2026-11-24T02:00 | ROC + volume · 1h | sell | DOGE-USD | 10.26 | -0.01 | exit signal |
| 2026-11-24T02:00 | Supertrend · 1h | sell | BTC-USD | 2.91 | 0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 11:10:05.000173+00:00 -> 2026-11-24 11:20:05.000173+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
