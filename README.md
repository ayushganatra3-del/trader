# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T12:20:05.000128+00:00 · 66850 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.36 (-14.64%)

Closed trades 233, win rate 36.9%, fees £6.31, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-19)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.48 · VIX 28.44 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.4, AAPL 4.7, AMZN 4.0, META 1.7, AMD 1.4, TSLA 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 9555 decisions in 1911 calls, $0.1337 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T12:20 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-11-20T12:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T12:20 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| CCI reversion | SOXL | 1.96 | +18.18% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.02 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.64 | 14.64 | 0 | — | 12.51 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.94 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.33 | 3.33 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.10 | -3.61 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.76 | -0.50 | -9.06 | 201 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.67 | -0.51 | -8.24 | 162 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.08 | -5.92 | 0 | — | -7.00 | -2.35 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.24 | -8.76 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.53 | -9.47 | 8 | 50.0 | -10.85 | -0.86 | -18.69 | 6 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.88 | -10.12 | 0 | — | -10.81 | -3.01 | -13.10 | 1 |
| 18 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.28 | -3.59 | -18.48 | 148 |
| 19 | Trend pullback · 1h | trend | 89.80 | -10.20 | 115 | 23.5 | -10.75 | -6.35 | -11.98 | 47 |
| 20 | Copy: Insider buying | copy | 89.37 | -10.63 | 55 | 40.0 | -6.73 | -1.27 | -14.79 | 65 |
| 21 | Daily: Bullish score | daily | 87.55 | -12.46 | 17 | 17.6 | -14.48 | -3.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.72 | -6.23 | -16.36 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.49 | -3.98 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.37 | -18.63 | 194 | 27.8 | -26.95 | -8.20 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.44 | -19.56 | 217 | 40.6 | -15.15 | -6.75 | -15.33 | 71 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.34 | -21.55 | 73 |
| 30 | Donchian 55/20 · 1h | breakout | 78.59 | -21.41 | 79 | 12.7 | -28.74 | -8.97 | -29.80 | 85 |
| 31 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.37 | -6.02 | -25.33 | 143 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.47 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.93 | -25.07 | 2 | 0.0 | -23.95 | -3.42 | -27.37 | 1 |
| 34 | Ichimoku · 1h | trend | 73.64 | -26.36 | 107 | 14.0 | -30.75 | -9.41 | -32.08 | 109 |
| 35 | ADX DI cross · 1h | trend | 72.87 | -27.13 | 226 | 20.4 | -28.26 | -4.43 | -35.87 | 277 |
| 36 | Hold BTC | benchmark | 72.42 | -27.58 | 2 | 0.0 | -24.55 | -4.04 | -29.74 | 1 |
| 37 | Max aggression: 5-day momentum | meta | 71.51 | -28.49 | 22 | 40.9 | -54.16 | -3.82 | -58.77 | 21 |
| 38 | Stochastic reversion · 1h | reversion | 71.12 | -28.88 | 356 | 42.1 | -35.55 | -5.32 | -36.85 | 424 |
| 39 | Triple EMA stack · 1h | trend | 70.26 | -29.74 | 161 | 14.3 | -34.63 | -8.98 | -37.24 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.04 | -29.96 | 195 | 21.5 | -33.92 | -9.26 | -36.32 | 217 |
| 41 | Supertrend · 1h | trend | 69.89 | -30.11 | 198 | 16.7 | -33.61 | -6.01 | -38.94 | 203 |
| 42 | EMA 20/50 cross · 1h | trend | 69.55 | -30.45 | 119 | 10.1 | -38.19 | -11.62 | -40.64 | 122 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 68.46 | -31.54 | 468 | 33.5 | -30.86 | -4.64 | -32.78 | 173 |
| 45 | Heikin-Ashi · 1h | trend | 68.12 | -31.88 | 483 | 23.0 | -46.09 | -10.17 | -47.85 | 616 |
| 46 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.42 | -5.90 | -33.99 | 205 |
| 47 | RSI momentum · 1h | momentum | 67.81 | -32.19 | 184 | 14.1 | -39.37 | -9.03 | -41.77 | 202 |
| 48 | OBV trend · 1h | momentum | 67.74 | -32.26 | 315 | 19.4 | -38.33 | -10.26 | -41.22 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.43 | -33.57 | 398 | 42.0 | -42.32 | -7.02 | -44.29 | 483 |
| 50 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.22 | -57.50 | 38 |
| 51 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -38.27 | -6.67 | -43.62 | 342 |
| 52 | Donchian 20/10 · 1h | breakout | 64.64 | -35.36 | 165 | 17.6 | -37.12 | -7.15 | -43.26 | 192 |
| 53 | MACD cross · 1h | trend | 64.49 | -35.51 | 434 | 21.4 | -48.30 | -9.52 | -48.66 | 496 |
| 54 | EMA 9/21 cross · 1h | trend | 62.10 | -37.90 | 291 | 11.3 | -40.92 | -7.93 | -47.32 | 323 |
| 55 | Bollinger reversion · 1h | reversion | 61.33 | -38.66 | 361 | 38.0 | -40.77 | -6.24 | -41.49 | 417 |
| 56 | Williams %R · 1h | reversion | 61.26 | -38.74 | 448 | 40.4 | -47.47 | -8.19 | -48.20 | 575 |
| 57 | Agent (ML meta-label) | meta | 58.02 | -41.98 | 1995 | 24.7 | -25.58 | -4.74 | -27.57 | 300 |
| 58 | RSI(14) reversion · 1h | reversion | 57.90 | -42.10 | 219 | 33.8 | -39.96 | -5.70 | -43.68 | 271 |
| 59 | Z-score reversion · 1h | reversion | 55.39 | -44.61 | 233 | 34.3 | -39.82 | -5.55 | -42.43 | 262 |
| 60 | Candlestick reversal · 1h | reversion | 54.33 | -45.66 | 584 | 26.5 | -49.59 | -9.15 | -49.97 | 675 |
| 61 | VWAP momentum · 1h | momentum | 53.69 | -46.31 | 1010 | 21.5 | -57.24 | -11.49 | -60.92 | 1194 |
| 62 | Three white soldiers | momentum | 52.67 | -47.33 | 611 | 14.2 | -51.52 | -22.83 | -51.61 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.23 | -99.15 | 5332 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.49 | -30.09 | -83.87 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.43 | -45.76 | -94.43 | 2456 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.94 | -34.46 | -91.02 | 1944 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.21 | -43.99 | -92.21 | 2290 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -28.63 | -90.21 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -50.16 | -98.21 | 3486 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -51.47 | -96.82 | 3392 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.02 | -39.11 | -94.05 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.56 | -34.77 | -83.58 | 1578 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -56.95 | -99.65 | 6246 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -45.94 | -92.97 | 2528 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -36.09 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -69.44 | -99.83 | 6234 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.36 | -46.52 | -93.36 | 2282 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.79 | -25.36 | -78.85 | 1636 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -57.57 | -97.84 | 3380 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.10 | -56.33 | -99.10 | 5026 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.75 | -29.26 | -70.75 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.97 | -55.64 | -94.97 | 2720 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -86.08 | -39.74 | -86.08 | 1706 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -70.64 | -99.72 | 6479 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.16 | -31.56 | -91.16 | 2413 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.41 | -19.17 | -80.46 | 1878 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.87 | -37.47 | -91.87 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.71 | -46.03 | -97.71 | 3981 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.18 | -52.53 | -90.18 | 2176 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.58 | -31.73 | -67.58 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.52 | -28.62 | -74.89 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.58 | -18.75 | -82.70 | 1805 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.64 | -46.11 | -97.64 | 4376 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -104.92 | -99.95 | 8414 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T12:10 | Bollinger reversion · 1h | buy | DOGE-USD | 7.01 | — | rebalance up |
| 2026-11-20T12:10 | Bollinger reversion · 1h | buy | BTC-USD | 3.10 | — | rebalance up |
| 2026-11-20T12:10 | Bollinger reversion · 1h | sell | SOL-USD | 10.12 | -0.25 | stop-loss |
| 2026-11-20T12:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.44 | — | entry |
| 2026-11-20T12:00 | Candlestick reversal · 1h | sell | DOGE-USD | 4.86 | -0.08 | exit signal |
| 2026-11-20T12:00 | MACD cross · 1h | sell | XRP-USD | 1.19 | -0.02 | exit signal |
| 2026-11-20T11:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.28 | — | rebalance up |
| 2026-11-20T11:00 | Bollinger reversion · 1h | buy | BTC-USD | 3.53 | — | rebalance up |
| 2026-11-20T11:00 | Bollinger reversion · 1h | sell | ETH-USD | 8.81 | -0.08 | exit signal |
| 2026-11-20T11:00 | MACD cross · 1h | buy | XRP-USD | 1.21 | — | entry signal |
| 2026-11-20T11:00 | MACD cross · 1h | buy | BTC-USD | 5.88 | — | entry signal |
| 2026-11-20T10:55 | Three white soldiers | sell | SOL-USD | 13.06 | -0.14 | stop-loss |
| 2026-11-20T10:45 | Three white soldiers | buy | SOL-USD | 13.20 | — | entry signal |
| 2026-11-20T10:00 | MACD cross · 1h | buy | ETH-USD | 5.79 | — | rebalance up |
| 2026-11-20T10:00 | MACD cross · 1h | sell | XRP-USD | 7.04 | -0.16 | exit signal |
| 2026-11-20T10:00 | MACD cross · 1h | sell | BTC-USD | 5.83 | -0.05 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | buy | ETH-USD | 4.42 | — | rebalance up |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | XRP-USD | 8.90 | -0.10 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | SOL-USD | 10.73 | -0.09 | exit signal |
| 2026-11-20T09:00 | VWAP momentum · 1h | sell | DOGE-USD | 8.93 | -0.10 | exit signal |
| 2026-11-20T09:00 | MACD cross · 1h | buy | ETH-USD | 1.40 | — | entry signal |
| 2026-11-20T09:00 | MACD cross · 1h | buy | BTC-USD | 5.88 | — | entry signal |
| 2026-11-20T08:55 | Three white soldiers | sell | ETH-USD | 13.16 | -0.05 | exit signal |
| 2026-11-20T08:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.95 | — | entry signal |
| 2026-11-20T08:00 | Candlestick reversal · 1h | sell | XRP-USD | 5.91 | -0.03 | exit signal |
| 2026-11-20T08:00 | VWAP momentum · 1h | buy | SOL-USD | 7.15 | — | rebalance up |
| 2026-11-20T08:00 | VWAP momentum · 1h | sell | BTC-USD | 8.96 | -0.07 | exit signal |
| 2026-11-20T07:50 | Three white soldiers | buy | ETH-USD | 13.21 | — | entry signal |
| 2026-11-20T07:00 | MACD cross · 1h | buy | XRP-USD | 7.20 | — | entry signal |
| 2026-11-20T06:00 | MFI reversion · 1h | buy | DOGE-USD | 3.48 | — | entry signal |
| 2026-11-20T06:00 | MFI reversion · 1h | sell | BTC-USD | 3.48 | -0.02 | rebalance down |
| 2026-11-20T06:00 | Bollinger reversion · 1h | buy | DOGE-USD | 2.76 | — | entry |
| 2026-11-20T06:00 | Bollinger reversion · 1h | sell | XRP-USD | 2.76 | 0.04 | exit signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | SOL-USD | 3.67 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | ETH-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | buy | BTC-USD | 9.03 | — | entry signal |
| 2026-11-20T06:00 | VWAP momentum · 1h | sell | XRP-USD | 4.58 | 0.00 | rebalance down |
| 2026-11-20T05:00 | VWAP momentum · 1h | sell | BTC-USD | 13.34 | -0.26 | exit signal |
| 2026-11-20T04:36 | MFI reversion · 1h | buy | XRP-USD | 2.90 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 12:20:05.000128+00:00 -> 2026-11-20 12:30:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
