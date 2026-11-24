# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T12:40:05.000130+00:00 · 71818 ticks

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

Today: 10167 decisions in 2034 calls, $0.1422 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T12:40 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-24T12:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-24T12:40 | 2 / 3 / 0 | ETH-USD 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.12 | +6.57% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.67 | +10.14% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.92 | 14.92 | 0 | — | 12.43 | 4.42 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 0.77 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.60 | 3.60 | 0 | — | 2.66 | 1.07 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.51 | -0.07 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.20 | 0.02 | -7.48 | 149 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 95.03 | -4.97 | 0 | — | -6.09 | -1.50 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.13 | -7.87 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.21 | -3.62 | -9.41 | 34 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.46 | -9.54 | 0 | — | -10.60 | -2.27 | -17.03 | 1 |
| 18 | Copy: Insider buying | copy | 89.67 | -10.33 | 58 | 39.7 | -8.96 | -1.74 | -14.79 | 68 |
| 19 | VWAP reversion · 1h | reversion | 89.64 | -10.36 | 163 | 46.0 | -7.82 | -1.42 | -20.49 | 153 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -2.99 | -20.94 | 1 |
| 21 | Opening range 30m | breakout | 86.41 | -13.59 | 463 | 33.3 | -13.08 | -4.39 | -14.39 | 542 |
| 22 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.20 | -13.80 | 9 | 44.4 | -10.93 | -0.60 | -26.65 | 6 |
| 23 | Daily: Bullish score | daily | 85.32 | -14.68 | 20 | 20.0 | -16.45 | -3.46 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -21.66 | -7.29 | -21.83 | 82 |
| 25 | Parabolic SAR · 1h | trend | 79.97 | -20.03 | 204 | 28.4 | -28.23 | -7.68 | -29.41 | 189 |
| 26 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -26.14 | -5.70 | -26.50 | 195 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -25.32 | -4.29 | -25.84 | 91 |
| 29 | Opening range 15m | breakout | 77.30 | -22.70 | 574 | 31.0 | -22.46 | -6.90 | -23.30 | 660 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.88 | -7.04 | -23.25 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.15 | -8.03 | -30.15 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.55 | -6.51 | -25.41 | 145 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Supertrend · 1h | trend | 70.59 | -29.41 | 204 | 18.6 | -34.84 | -6.91 | -37.27 | 207 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 70.11 | -29.89 | 3 | 0.0 | -23.26 | -2.75 | -32.18 | 1 |
| 36 | Hold BTC | benchmark | 69.75 | -30.25 | 3 | 0.0 | -30.05 | -5.13 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.58 | -30.42 | 253 | 19.0 | -38.08 | -6.93 | -40.20 | 277 |
| 38 | Daily: Momentum burst | daily | 69.09 | -30.91 | 30 | 13.3 | -37.24 | -5.04 | -37.81 | 25 |
| 39 | Bollinger breakout · 1h | breakout | 68.57 | -31.43 | 207 | 22.2 | -32.58 | -8.56 | -33.72 | 211 |
| 40 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -38.76 | -9.98 | -38.93 | 172 |
| 41 | EMA 20/50 cross · 1h | trend | 67.57 | -32.43 | 121 | 9.9 | -38.03 | -10.52 | -38.57 | 116 |
| 42 | Stochastic reversion · 1h | reversion | 66.12 | -33.88 | 395 | 40.8 | -33.17 | -3.55 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 65.91 | -34.09 | 322 | 19.9 | -40.69 | -10.56 | -40.79 | 236 |
| 44 | MACD zero-line · 1h | trend | 65.74 | -34.26 | 198 | 16.7 | -34.99 | -9.55 | -35.11 | 204 |
| 45 | Heikin-Ashi · 1h | trend | 64.52 | -35.48 | 527 | 22.2 | -46.72 | -9.50 | -47.76 | 629 |
| 46 | RSI momentum · 1h | momentum | 64.21 | -35.79 | 200 | 15.0 | -40.61 | -9.41 | -40.80 | 199 |
| 47 | MFI reversion · 1h | reversion | 63.40 | -36.60 | 486 | 32.9 | -31.96 | -4.64 | -37.87 | 187 |
| 48 | Max aggression: 5-day momentum | meta | 62.70 | -37.30 | 25 | 36.0 | -62.72 | -4.12 | -66.58 | 23 |
| 49 | ROC + volume · 1h | momentum | 61.61 | -38.39 | 452 | 27.0 | -42.62 | -8.52 | -42.93 | 341 |
| 50 | Donchian 20/10 · 1h | breakout | 60.97 | -39.03 | 181 | 17.7 | -40.46 | -8.73 | -41.99 | 193 |
| 51 | Agent (ML meta-label) | meta | 59.38 | -40.62 | 2049 | 25.0 | -20.53 | -2.57 | -31.87 | 327 |
| 52 | EMA 9/21 cross · 1h | trend | 59.28 | -40.72 | 307 | 12.4 | -44.92 | -10.65 | -45.88 | 336 |
| 53 | Max aggression: 1-day momentum | meta | 59.16 | -40.84 | 34 | 26.5 | -52.64 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 58.68 | -41.32 | 467 | 21.4 | -49.89 | -9.73 | -50.99 | 512 |
| 55 | Bollinger reversion · 1h | reversion | 57.90 | -42.10 | 391 | 37.6 | -37.41 | -4.46 | -45.42 | 430 |
| 56 | CCI reversion · 1h | reversion | 57.85 | -42.15 | 430 | 40.0 | -49.32 | -8.19 | -51.92 | 501 |
| 57 | Williams %R · 1h | reversion | 53.66 | -46.34 | 500 | 38.4 | -53.85 | -8.79 | -55.78 | 588 |
| 58 | VWAP momentum · 1h | momentum | 53.31 | -46.69 | 1054 | 21.8 | -58.21 | -13.49 | -58.29 | 1189 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.78 | -8.41 | -54.03 | 663 |
| 60 | RSI(14) reversion · 1h | reversion | 50.87 | -49.13 | 241 | 32.0 | -49.79 | -7.95 | -52.23 | 285 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -49.34 | -99.15 | 5344 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.23 | -33.85 | -84.43 | 1441 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.52 | -49.78 | -94.52 | 2439 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.61 | -32.20 | -90.61 | 1916 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.85 | -42.03 | -91.85 | 2258 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -28.61 | -89.73 | 1966 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -48.63 | -98.19 | 3436 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.04 | -53.05 | -97.04 | 3390 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -38.50 | -93.39 | 2103 |
| 70 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.37 | -35.07 | -83.38 | 1557 |
| 71 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -56.81 | -99.68 | 6291 |
| 72 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.25 | -38.60 | -93.25 | 2497 |
| 73 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.47 | -36.89 | -94.47 | 3179 |
| 74 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -68.43 | -99.82 | 6142 |
| 75 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.28 | -44.44 | -93.29 | 2277 |
| 76 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.72 | -22.34 | -51.72 | 641 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.47 | -24.05 | -78.47 | 1606 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.79 | -58.41 | -97.79 | 3287 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.51 | -99.18 | 5119 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.18 | -27.37 | -71.22 | 1203 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.99 | -48.18 | -94.99 | 2672 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.79 | -6.22 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.44 | -37.15 | -85.45 | 1667 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -74.47 | -99.77 | 6543 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.33 | -30.88 | -91.38 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.99 | -20.12 | -83.05 | 1955 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.99 | -31.80 | -92.03 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -49.36 | -98.13 | 4053 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.33 | -48.32 | -90.34 | 2199 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.08 | -30.47 | -68.08 | 792 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.55 | -28.12 | -73.55 | 1164 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.85 | -18.82 | -84.01 | 1828 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.99 | -49.72 | -98.00 | 4410 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.37 | -99.94 | 8284 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 12:40:05.000130+00:00 -> 2026-11-24 12:50:05.000130+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
