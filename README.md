# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T13:50:05.000137+00:00 · 66925 ticks

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

Today: 10680 decisions in 2136 calls, $0.1495 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T13:50 | 3 / 2 / 0 | ETH-USD 18%, XRP-USD 15%, BTC-USD 14% |  |
| Breezy | 2026-11-20T13:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T13:50 | 4 / 1 / 0 | ETH-USD 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.03 | +18.56% | 16 |
| Bollinger reversion | TSLA | 1.75 | +3.29% | 12 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 121.75 | 21.75 | 26 | 65.4 | 24.79 | 4.02 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.57 | 14.57 | 0 | — | 12.51 | 4.16 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.50 | 12.50 | 39 | 30.8 | 19.76 | 2.94 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.27 | 3.27 | 0 | — | 4.30 | 1.23 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: Stocks in Play ORB | daytrade | 99.77 | -0.23 | 155 | 35.5 | -4.23 | -3.70 | -4.86 | 71 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 99.63 | -0.37 | 40 | 42.5 | -2.13 | -0.35 | -9.74 | 35 |
| 9 | Gap and go | momentum | 97.85 | -2.15 | 203 | 31.5 | -1.53 | -0.42 | -9.06 | 202 |
| 10 | Agent (rotation) | meta | 96.11 | -3.89 | 211 | 28.9 | -1.59 | -0.48 | -8.24 | 163 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 94.01 | -5.99 | 0 | — | -7.00 | -2.35 | -8.40 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.28 | -5.13 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 91.18 | -8.82 | 0 | — | -8.86 | -2.30 | -10.09 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.03 | -8.97 | 26 | 15.4 | -10.18 | -8.41 | -10.18 | 24 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 90.47 | -9.53 | 8 | 50.0 | -10.85 | -0.86 | -18.69 | 6 |
| 17 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.28 | -3.59 | -18.48 | 148 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.83 | -10.18 | 0 | — | -10.81 | -3.01 | -13.10 | 1 |
| 19 | Trend pullback · 1h | trend | 89.79 | -10.21 | 115 | 23.5 | -10.75 | -6.35 | -11.98 | 47 |
| 20 | Copy: Insider buying | copy | 89.31 | -10.69 | 55 | 40.0 | -6.73 | -1.27 | -14.79 | 65 |
| 21 | Daily: Bullish score | daily | 87.50 | -12.50 | 17 | 17.6 | -14.48 | -3.80 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Opening range 30m | breakout | 86.41 | -13.59 | 449 | 33.6 | -11.54 | -3.81 | -14.87 | 549 |
| 24 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -18.89 | -9.51 | -18.94 | 71 |
| 25 | Agent | meta | 85.36 | -14.64 | 233 | 36.9 | -13.84 | -6.29 | -16.51 | 214 |
| 26 | Agent (aggressive) | meta | 83.60 | -16.40 | 107 | 33.6 | -15.34 | -3.94 | -19.68 | 101 |
| 27 | Parabolic SAR · 1h | trend | 81.36 | -18.64 | 194 | 27.8 | -26.95 | -8.20 | -28.86 | 196 |
| 28 | Connors RSI(2) · 1h | reversion | 80.42 | -19.58 | 217 | 40.6 | -15.15 | -6.74 | -15.33 | 71 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.50 | -5.34 | -21.55 | 73 |
| 30 | Keltner breakout · 1h | breakout | 78.59 | -21.41 | 126 | 26.2 | -22.60 | -6.17 | -25.33 | 145 |
| 31 | Donchian 55/20 · 1h | breakout | 78.58 | -21.42 | 79 | 12.7 | -28.77 | -8.98 | -29.81 | 85 |
| 32 | Opening range 15m | breakout | 77.33 | -22.67 | 547 | 31.8 | -21.22 | -6.47 | -23.60 | 658 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 74.88 | -25.12 | 2 | 0.0 | -23.95 | -3.42 | -27.37 | 1 |
| 34 | Ichimoku · 1h | trend | 73.63 | -26.37 | 107 | 14.0 | -30.75 | -9.41 | -32.08 | 109 |
| 35 | ADX DI cross · 1h | trend | 72.85 | -27.15 | 226 | 20.4 | -28.26 | -4.43 | -35.87 | 277 |
| 36 | Hold BTC | benchmark | 72.67 | -27.33 | 2 | 0.0 | -24.45 | -4.02 | -29.74 | 1 |
| 37 | Max aggression: 5-day momentum | meta | 71.40 | -28.60 | 22 | 40.9 | -54.20 | -3.82 | -59.00 | 21 |
| 38 | Stochastic reversion · 1h | reversion | 70.99 | -29.01 | 357 | 42.0 | -35.65 | -5.34 | -36.94 | 424 |
| 39 | Triple EMA stack · 1h | trend | 70.25 | -29.75 | 161 | 14.3 | -34.44 | -8.92 | -37.34 | 170 |
| 40 | Bollinger breakout · 1h | breakout | 70.03 | -29.97 | 195 | 21.5 | -33.88 | -9.23 | -36.32 | 217 |
| 41 | Supertrend · 1h | trend | 69.88 | -30.12 | 198 | 16.7 | -33.42 | -5.57 | -39.93 | 204 |
| 42 | EMA 20/50 cross · 1h | trend | 69.54 | -30.46 | 119 | 10.1 | -38.19 | -11.62 | -40.64 | 122 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.14 | -37.91 | 31 |
| 44 | MFI reversion · 1h | reversion | 68.24 | -31.76 | 470 | 33.4 | -31.73 | -4.78 | -33.67 | 173 |
| 45 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -28.42 | -5.90 | -33.99 | 205 |
| 46 | Heikin-Ashi · 1h | trend | 68.11 | -31.89 | 483 | 23.0 | -46.09 | -10.17 | -47.85 | 616 |
| 47 | RSI momentum · 1h | momentum | 67.80 | -32.20 | 184 | 14.1 | -39.37 | -9.01 | -41.81 | 202 |
| 48 | OBV trend · 1h | momentum | 67.73 | -32.27 | 315 | 19.4 | -38.70 | -10.55 | -41.22 | 240 |
| 49 | CCI reversion · 1h | reversion | 66.39 | -33.61 | 398 | 42.0 | -42.29 | -7.00 | -44.42 | 482 |
| 50 | Max aggression: 1-day momentum | meta | 65.56 | -34.44 | 33 | 27.3 | -47.44 | -3.22 | -57.50 | 38 |
| 51 | ROC + volume · 1h | momentum | 64.82 | -35.18 | 431 | 27.6 | -37.87 | -6.66 | -43.31 | 341 |
| 52 | Donchian 20/10 · 1h | breakout | 64.63 | -35.37 | 165 | 17.6 | -37.12 | -7.15 | -43.26 | 192 |
| 53 | MACD cross · 1h | trend | 64.52 | -35.48 | 434 | 21.4 | -48.24 | -9.50 | -48.67 | 496 |
| 54 | EMA 9/21 cross · 1h | trend | 62.09 | -37.91 | 291 | 11.3 | -40.95 | -7.94 | -47.32 | 323 |
| 55 | Williams %R · 1h | reversion | 61.23 | -38.77 | 448 | 40.4 | -47.53 | -8.21 | -48.29 | 575 |
| 56 | Bollinger reversion · 1h | reversion | 61.23 | -38.77 | 362 | 37.8 | -40.83 | -6.25 | -41.59 | 417 |
| 57 | Agent (ML meta-label) | meta | 57.98 | -42.02 | 1995 | 24.7 | -25.33 | -4.79 | -27.09 | 301 |
| 58 | RSI(14) reversion · 1h | reversion | 57.86 | -42.14 | 219 | 33.8 | -39.94 | -5.70 | -43.68 | 269 |
| 59 | Z-score reversion · 1h | reversion | 55.38 | -44.62 | 233 | 34.3 | -39.91 | -5.57 | -42.60 | 262 |
| 60 | Candlestick reversal · 1h | reversion | 54.32 | -45.68 | 584 | 26.5 | -49.31 | -9.13 | -49.64 | 675 |
| 61 | VWAP momentum · 1h | momentum | 53.65 | -46.35 | 1011 | 21.5 | -57.21 | -11.49 | -60.86 | 1193 |
| 62 | Three white soldiers | momentum | 52.63 | -47.37 | 611 | 14.2 | -51.53 | -22.92 | -51.57 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -46.91 | -99.15 | 5325 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.40 | -29.78 | -83.87 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.38 | -45.02 | -94.38 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.98 | -34.62 | -91.03 | 1946 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.17 | -43.42 | -92.17 | 2288 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -28.64 | -90.21 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.87 | -98.20 | 3484 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.74 | -51.98 | -96.74 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -39.34 | -94.05 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.46 | -34.40 | -83.46 | 1575 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.65 | -57.06 | -99.65 | 6251 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -45.60 | -92.94 | 2528 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -36.09 | -94.64 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -68.91 | -99.83 | 6237 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.34 | -46.26 | -93.34 | 2280 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.76 | -25.49 | -78.82 | 1635 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.84 | -57.12 | -97.84 | 3380 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.11 | -57.34 | -99.11 | 5035 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.53 | -28.73 | -70.53 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.91 | -54.37 | -94.91 | 2717 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.97 | -39.29 | -85.97 | 1704 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.72 | -70.90 | -99.72 | 6480 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.23 | -31.82 | -91.26 | 2418 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.44 | -19.21 | -80.51 | 1879 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.95 | -37.84 | -91.99 | 2177 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.73 | -46.38 | -97.74 | 3985 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -52.62 | -90.21 | 2178 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.58 | -31.73 | -67.58 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.37 | -28.26 | -74.89 | 1203 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -82.73 | -18.89 | -82.82 | 1806 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.64 | -46.16 | -97.66 | 4381 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -102.14 | -99.94 | 8408 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T13:50 | Three white soldiers | buy | ETH-USD | 13.17 | — | entry signal |
| 2026-11-20T13:35 | MFI reversion · 1h | sell | XRP-USD | 11.07 | -0.34 | stop-loss |
| 2026-11-20T13:35 | MFI reversion · 1h | sell | DOGE-USD | 3.36 | -0.12 | stop-loss |
| 2026-11-20T13:35 | Stochastic reversion · 1h | sell | XRP-USD | 6.25 | -0.23 | stop-loss |
| 2026-11-20T13:25 | Bollinger reversion · 1h | sell | DOGE-USD | 14.78 | -0.28 | stop-loss |
| 2026-11-20T13:00 | VWAP momentum · 1h | sell | ETH-USD | 13.34 | -0.10 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 13:50:05.000137+00:00 -> 2026-11-20 14:00:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
