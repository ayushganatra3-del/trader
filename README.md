# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T09:10:05.000137+00:00 · 62980 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 203, win rate 36.5%, fees £5.77, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 7206 decisions in 1449 calls, $0.1008 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T09:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-17T09:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T09:10 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.05 | 18.05 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.75 | 3.75 | 0 | — | 5.51 | 1.52 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.63 | -3.37 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.83 | -6.17 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.67 | -8.32 | 47 | 42.6 | -8.37 | -1.64 | -14.79 | 59 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.57 | -8.43 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Squeeze breakout · 1h | breakout | 87.12 | -12.88 | 67 | 20.9 | -10.88 | -4.03 | -16.34 | 78 |
| 23 | Daily: Bullish score | daily | 86.68 | -13.32 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.10 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 82.99 | -17.01 | 180 | 28.3 | -23.14 | -6.26 | -24.82 | 213 |
| 28 | Keltner breakout · 1h | breakout | 80.58 | -19.42 | 121 | 25.6 | -18.44 | -3.95 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -26.33 | -6.86 | -28.90 | 87 |
| 30 | Connors RSI(2) · 1h | reversion | 80.31 | -19.69 | 213 | 39.9 | -14.53 | -6.42 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.38 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.11 | -21.89 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.31 | -22.69 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -31.15 | -8.78 | -31.74 | 116 |
| 36 | Hold BTC | benchmark | 75.15 | -24.85 | 2 | 0.0 | -15.62 | -2.20 | -28.91 | 1 |
| 37 | Max aggression: 1-day momentum | meta | 74.93 | -25.07 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 40 | Bollinger breakout · 1h | breakout | 73.85 | -26.15 | 186 | 22.0 | -24.86 | -5.33 | -31.89 | 234 |
| 41 | MFI reversion · 1h | reversion | 72.06 | -27.94 | 420 | 34.3 | -25.90 | -3.67 | -29.33 | 163 |
| 42 | MACD zero-line · 1h | trend | 71.50 | -28.50 | 177 | 18.1 | -25.98 | -5.14 | -32.34 | 198 |
| 43 | Heikin-Ashi · 1h | trend | 71.47 | -28.53 | 461 | 23.2 | -38.61 | -7.34 | -43.26 | 636 |
| 44 | Supertrend · 1h | trend | 71.40 | -28.60 | 187 | 16.0 | -32.52 | -5.53 | -39.67 | 200 |
| 45 | Triple EMA stack · 1h | trend | 71.23 | -28.77 | 154 | 14.9 | -31.11 | -6.09 | -37.77 | 192 |
| 46 | RSI momentum · 1h | momentum | 71.07 | -28.93 | 175 | 14.3 | -31.38 | -5.68 | -38.07 | 203 |
| 47 | EMA 20/50 cross · 1h | trend | 70.93 | -29.07 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | ROC + volume · 1h | momentum | 70.58 | -29.42 | 405 | 28.4 | -28.30 | -4.65 | -37.95 | 355 |
| 49 | MACD cross · 1h | trend | 70.32 | -29.68 | 407 | 22.4 | -34.07 | -4.91 | -43.61 | 476 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.21 | -30.79 | 303 | 19.1 | -32.04 | -6.27 | -39.75 | 261 |
| 52 | CCI reversion · 1h | reversion | 68.06 | -31.94 | 378 | 42.1 | -40.07 | -6.48 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.45 | -32.55 | 157 | 18.5 | -31.02 | -5.17 | -39.25 | 207 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | Williams %R · 1h | reversion | 64.16 | -35.84 | 420 | 41.4 | -44.60 | -7.50 | -45.09 | 543 |
| 56 | EMA 9/21 cross · 1h | trend | 63.57 | -36.43 | 277 | 11.2 | -39.19 | -7.72 | -45.29 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -25.00 | -4.06 | -29.62 | 338 |
| 58 | Z-score reversion · 1h | reversion | 59.60 | -40.40 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.29 | -40.71 | 204 | 31.9 | -40.74 | -5.99 | -42.17 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.10 | -41.90 | 948 | 21.6 | -53.10 | -9.37 | -57.76 | 1208 |
| 61 | Candlestick reversal · 1h | reversion | 57.16 | -42.84 | 538 | 27.0 | -45.61 | -8.25 | -45.63 | 617 |
| 62 | Three white soldiers | momentum | 56.30 | -43.70 | 572 | 14.7 | -49.15 | -21.85 | -49.15 | 656 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.28 | -98.99 | 5282 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.41 | -25.72 | -81.65 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.00 | -43.62 | -94.00 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.07 | -31.49 | -90.10 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -40.03 | -91.37 | 2318 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.16 | -30.33 | -90.16 | 2154 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -47.78 | -97.94 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -51.98 | -96.42 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -37.19 | -93.61 | 2266 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.80 | -33.35 | -82.80 | 1636 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -53.67 | -99.60 | 6060 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.08 | -41.58 | -92.09 | 2581 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.23 | -36.36 | -95.24 | 3355 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.55 | -99.81 | 6144 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.39 | -43.43 | -92.39 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.66 | -26.31 | -76.66 | 1653 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -59.00 | -97.62 | 3468 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -54.80 | -99.00 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.86 | -27.52 | -68.86 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -55.50 | -94.72 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.62 | -84.65 | 1744 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.12 | -99.70 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.52 | -30.02 | -90.52 | 2338 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.67 | -18.58 | -79.67 | 1818 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.05 | -35.62 | -91.07 | 2169 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.48 | -44.97 | -97.48 | 3912 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -58.84 | -89.25 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.52 | -30.01 | -66.52 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.91 | -23.21 | -72.18 | 1245 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.23 | -17.46 | -80.51 | 1753 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.58 | -45.50 | -97.58 | 4357 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.94 | -99.94 | 8392 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T09:05 | Candlestick reversal · 1h | sell | BTC-USD | 7.02 | -0.14 | stop-loss |
| 2026-11-17T09:00 | Bollinger breakout · 1h | sell | XRP-USD | 18.28 | -0.30 | exit signal |
| 2026-11-17T09:00 | VWAP momentum · 1h | buy | SOL-USD | 2.92 | — | rebalance up |
| 2026-11-17T09:00 | VWAP momentum · 1h | sell | ETH-USD | 11.59 | -0.13 | exit signal |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 3.19 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 5.27 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.29 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.55 | -0.17 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | SOL-USD | 4.35 | — | rebalance up |
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | ETH-USD | 4.38 | — | rebalance up |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | XRP-USD | 7.22 | -0.11 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.23 | -0.11 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | BTC-USD | 7.23 | -0.11 | exit signal |
| 2026-11-17T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 17.82 | -0.12 | exit signal |
| 2026-11-17T07:00 | Heikin-Ashi · 1h | sell | ETH-USD | 17.75 | -0.20 | exit signal |
| 2026-11-17T07:00 | Ichimoku · 1h | sell | ETH-USD | 18.63 | -0.21 | exit signal |
| 2026-11-17T07:00 | MACD zero-line · 1h | sell | BTC-USD | 17.34 | -0.24 | exit signal |
| 2026-11-17T07:00 | MACD cross · 1h | buy | ETH-USD | 3.53 | — | rebalance up |
| 2026-11-17T07:00 | MACD cross · 1h | sell | DOGE-USD | 3.40 | -0.04 | exit signal |
| 2026-11-17T07:00 | MACD cross · 1h | sell | BTC-USD | 14.00 | -0.21 | exit signal |
| 2026-11-17T07:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.31 | — | rebalance up |
| 2026-11-17T07:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 10.56 | -0.16 | exit signal |
| 2026-11-17T06:00 | MFI reversion · 1h | sell | ETH-USD | 7.22 | 0.01 | exit signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Ichimoku · 1h | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-11-17T05:00 | Williams %R · 1h | sell | XRP-USD | 7.25 | 0.08 | exit signal |
| 2026-11-17T05:00 | Squeeze breakout · 1h | buy | SOL-USD | 21.85 | — | entry signal |
| 2026-11-17T05:00 | Donchian 20/10 · 1h | buy | SOL-USD | 16.96 | — | entry signal |
| 2026-11-17T05:00 | MACD zero-line · 1h | buy | BTC-USD | 17.59 | — | entry signal |
| 2026-11-17T05:00 | MACD cross · 1h | buy | DOGE-USD | 3.44 | — | entry signal |
| 2026-11-17T04:00 | CCI reversion · 1h | sell | XRP-USD | 17.19 | 0.16 | exit signal |
| 2026-11-17T04:00 | Williams %R · 1h | sell | SOL-USD | 7.36 | 0.15 | exit signal |
| 2026-11-17T04:00 | Candlestick reversal · 1h | buy | BTC-USD | 7.16 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | RSI momentum · 1h | buy | SOL-USD | 17.81 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | XRP-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | ETH-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.34 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 09:10:05.000137+00:00 -> 2026-11-17 09:20:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 09:10:05.000137+00:00 -> 2026-11-17 09:20:05.000137+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
