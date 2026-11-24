# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T00:46:05.000183+00:00 · 71182 ticks

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
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 630 decisions in 126 calls, $0.0088 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T00:46 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-24T00:46 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T00:46 | 0 / 5 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.46 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.41 | 15.41 | 0 | — | 12.43 | 4.21 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.02 | 4.02 | 0 | — | 2.64 | 0.79 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.40 | -0.03 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.72 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.82 | -0.18 | -7.48 | 155 |
| 11 | Hold SPY | benchmark | 95.44 | -4.56 | 0 | — | -6.09 | -1.54 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.16 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.53 | -7.47 | 0 | — | -8.61 | -1.75 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.43 | -3.34 | -8.58 | 31 |
| 16 | Copy: Congress Democrats (NANC) | copy | 90.85 | -9.14 | 0 | — | -10.60 | -2.26 | -17.03 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.47 | -10.08 | 25 |
| 18 | Copy: Insider buying | copy | 90.06 | -9.94 | 58 | 39.7 | -17.15 | -3.23 | -22.56 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.92 | -10.08 | 163 | 46.0 | -7.76 | -1.40 | -20.49 | 158 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.27 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.57 | -13.43 | 9 | 44.4 | -10.93 | -0.59 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.35 | -14.39 | 542 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.76 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -22.06 | -7.36 | -22.23 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 80.54 | -19.46 | 220 | 40.9 | -14.20 | -6.25 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.26 | -19.74 | 204 | 28.4 | -28.25 | -7.57 | -30.34 | 190 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.39 | -5.68 | -25.99 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -15.50 | -3.96 | -18.44 | 88 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.04 | -6.80 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.25 | -7.64 | -29.77 | 84 |
| 31 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -6.97 | -23.25 | 72 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.39 | -6.41 | -25.26 | 144 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.92 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 71.25 | -28.75 | 3 | 0.0 | -29.19 | -5.18 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 70.87 | -29.13 | 203 | 18.2 | -35.11 | -6.78 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.41 | -29.59 | 3 | 0.0 | -23.26 | -2.81 | -32.18 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.71 | -30.29 | 252 | 19.0 | -37.55 | -6.66 | -40.30 | 278 |
| 38 | Triple EMA stack · 1h | trend | 69.33 | -30.67 | 165 | 14.5 | -37.67 | -9.49 | -38.75 | 169 |
| 39 | EMA 20/50 cross · 1h | trend | 69.31 | -30.69 | 119 | 10.1 | -37.26 | -10.15 | -39.68 | 118 |
| 40 | Daily: Momentum burst | daily | 69.17 | -30.83 | 30 | 13.3 | -37.24 | -5.32 | -37.81 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.65 | -31.35 | 207 | 22.2 | -32.55 | -8.46 | -33.70 | 211 |
| 42 | Stochastic reversion · 1h | reversion | 66.80 | -33.20 | 394 | 40.9 | -32.76 | -3.47 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 66.73 | -33.27 | 321 | 19.9 | -39.69 | -10.05 | -40.93 | 234 |
| 44 | MACD zero-line · 1h | trend | 65.88 | -34.12 | 198 | 16.7 | -35.16 | -9.53 | -35.51 | 206 |
| 45 | RSI momentum · 1h | momentum | 65.09 | -34.91 | 196 | 15.3 | -39.62 | -8.93 | -40.95 | 201 |
| 46 | Heikin-Ashi · 1h | trend | 64.61 | -35.39 | 526 | 22.2 | -46.88 | -9.47 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum | meta | 64.44 | -35.56 | 25 | 36.0 | -61.85 | -3.98 | -65.82 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.67 | -36.33 | 486 | 32.9 | -32.17 | -4.64 | -37.87 | 186 |
| 49 | Donchian 20/10 · 1h | breakout | 62.00 | -38.00 | 178 | 18.0 | -39.51 | -8.36 | -41.33 | 193 |
| 50 | ROC + volume · 1h | momentum | 61.63 | -38.37 | 451 | 27.1 | -42.77 | -8.55 | -42.88 | 344 |
| 51 | EMA 9/21 cross · 1h | trend | 59.91 | -40.09 | 301 | 12.0 | -44.37 | -10.32 | -45.50 | 333 |
| 52 | Agent (ML meta-label) | meta | 59.63 | -40.37 | 2049 | 25.0 | -17.03 | -2.10 | -28.51 | 329 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.65 | -3.83 | -54.72 | 38 |
| 54 | MACD cross · 1h | trend | 58.92 | -41.08 | 467 | 21.4 | -49.28 | -9.39 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.11 | -41.89 | 430 | 40.0 | -49.03 | -8.02 | -52.01 | 499 |
| 56 | Bollinger reversion · 1h | reversion | 57.96 | -42.04 | 391 | 37.6 | -37.42 | -4.42 | -45.42 | 430 |
| 57 | Williams %R · 1h | reversion | 54.00 | -46.00 | 500 | 38.4 | -54.00 | -8.77 | -55.78 | 586 |
| 58 | VWAP momentum · 1h | momentum | 53.54 | -46.46 | 1054 | 21.8 | -57.84 | -13.14 | -58.29 | 1182 |
| 59 | RSI(14) reversion · 1h | reversion | 51.02 | -48.98 | 241 | 32.0 | -50.41 | -8.04 | -52.23 | 290 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.62 | -8.59 | -54.66 | 665 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.10 | -45.93 | -99.11 | 5323 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.82 | -32.44 | -84.38 | 1431 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -46.87 | -94.46 | 2433 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.67 | -31.56 | -90.81 | 1913 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.73 | -40.26 | -91.73 | 2249 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.58 | -27.61 | -89.66 | 1961 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -46.78 | -98.19 | 3432 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.03 | -50.81 | -97.03 | 3369 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -37.17 | -93.68 | 2130 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -33.86 | -83.27 | 1553 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -53.67 | -99.67 | 6286 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -37.84 | -93.23 | 2494 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.45 | -35.38 | -94.46 | 3178 |
| 74 | Three white soldiers | momentum | 50.23 | -49.77 | 638 | 14.3 | -51.94 | -22.23 | -52.00 | 643 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -62.04 | -99.83 | 6143 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.21 | -42.70 | -93.30 | 2268 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.13 | -23.71 | -78.38 | 1611 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -53.76 | -97.77 | 3282 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.19 | -56.76 | -99.19 | 5121 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.84 | -26.76 | -70.87 | 1197 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.97 | -46.46 | -94.97 | 2671 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.17 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.41 | -36.28 | -85.41 | 1667 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.25 | -99.77 | 6546 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.56 | -30.21 | -91.68 | 2469 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.14 | -20.05 | -83.14 | 1953 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.95 | -30.37 | -92.06 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.14 | -47.09 | -98.14 | 4052 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.27 | -46.13 | -90.30 | 2192 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.20 | -29.31 | -68.20 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.19 | -27.67 | -73.33 | 1161 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.64 | -19.19 | -84.64 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.98 | -47.17 | -97.99 | 4412 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.62 | -99.94 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T00:00 | Max aggression: 5-day momentum | buy | SOL-USD | 64.49 | — | entry |
| 2026-11-24T00:00 | Williams %R · 1h | buy | DOGE-USD | 5.44 | — | entry signal |
| 2026-11-24T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 19.20 | — | entry |
| 2026-11-24T00:00 | Donchian 55/20 · 1h | buy | SOL-USD | 19.20 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | SOL-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | Donchian 20/10 · 1h | buy | BTC-USD | 15.51 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | XRP-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | SOL-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | DOGE-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | RSI momentum · 1h | buy | BTC-USD | 9.30 | — | entry |
| 2026-11-24T00:00 | ROC + volume · 1h | buy | DOGE-USD | 10.27 | — | entry |
| 2026-11-24T00:00 | ADX DI cross · 1h | buy | BTC-USD | 5.36 | — | entry |
| 2026-11-24T00:00 | Triple EMA stack · 1h | sell | XRP-USD | 17.28 | -0.17 | exit signal |
| 2026-11-24T00:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 7.37 | 0.07 | exit signal |
| 2026-11-24T00:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 7.51 | 0.03 | exit signal |
| 2026-11-23T23:35 | Three white soldiers | sell | BTC-USD | 12.49 | -0.08 | exit signal |
| 2026-11-23T23:05 | Three white soldiers | buy | BTC-USD | 12.58 | — | entry signal |
| 2026-11-23T23:00 | Parabolic SAR · 1h | sell | DOGE-USD | 13.08 | -0.09 | exit signal |
| 2026-11-23T23:00 | Supertrend · 1h | sell | DOGE-USD | 2.87 | 0.04 | exit signal |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | XRP-USD | 3.47 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | SOL-USD | 5.16 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | buy | DOGE-USD | 5.01 | — | rebalance up |
| 2026-11-23T23:00 | Triple EMA stack · 1h | sell | ETH-USD | 12.12 | -0.07 | exit signal |
| 2026-11-23T23:00 | Triple EMA stack · 1h | sell | BTC-USD | 12.16 | -0.02 | exit signal |
| 2026-11-23T22:00 | Stochastic reversion · 1h | buy | XRP-USD | 7.42 | — | entry signal |
| 2026-11-23T21:00 | Stochastic reversion · 1h | buy | BTC-USD | 8.35 | — | entry signal |
| 2026-11-23T21:00 | OBV trend · 1h | sell | SOL-USD | 14.15 | 0.27 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | SOL-USD | 2.88 | 0.08 | exit signal |
| 2026-11-23T21:00 | Supertrend · 1h | sell | ETH-USD | 2.92 | 0.12 | exit signal |
| 2026-11-23T21:00 | MACD cross · 1h | sell | DOGE-USD | 4.47 | 0.07 | exit signal |
| 2026-11-23T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 90.60 | -1.14 | target is flat |
| 2026-11-23T20:55 | Opening range 30m | sell | UPRO | 14.43 | -0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | TSLA | 14.27 | -0.12 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | SPY | 14.36 | -0.05 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | NVDA | 14.41 | -0.33 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | META | 14.44 | 0.10 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 30m | sell | LABU | 14.50 | 0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | UPRO | 12.89 | -0.13 | end-of-day flatten |
| 2026-11-23T20:55 | Opening range 15m | sell | TSLA | 12.79 | -0.12 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 00:46:05.000183+00:00 -> 2026-11-24 00:56:05.000183+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
