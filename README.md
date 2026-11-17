# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T15:39:05.000158+00:00 · 63323 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.50 (-15.50%)

Closed trades 205, win rate 36.1%, fees £5.83, max drawdown -15.89%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 16.90 | -0.63 |

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

Today: 16443 decisions in 2478 calls, $0.2188 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T15:39 | 1 / 6 / 23 | cash |  |
| Breezy | 2026-11-17T15:39 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-17T15:39 | 3 / 19 / 8 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.68 | 17.68 | 0 | — | 13.88 | 4.63 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.72 | 10.72 | 24 | 62.5 | 15.99 | 3.25 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.90 | 3.90 | 0 | — | 6.17 | 1.68 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 149 | 34.9 | -2.71 | -2.27 | -4.30 | 71 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.39 | -2.61 | 8 | 50.0 | -1.82 | 0.11 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.85 | -4.15 | 0 | — | -3.41 | -1.08 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.87 | -6.13 | 197 | 29.9 | -1.87 | -0.60 | -8.15 | 159 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.80 | -6.21 | 0 | — | -6.92 | -1.80 | -8.27 | 1 |
| 16 | Copy: Insider buying | copy | 91.88 | -8.12 | 47 | 42.6 | -8.62 | -1.70 | -14.79 | 62 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.05 | -8.95 | 0 | — | -7.69 | -2.07 | -11.36 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.36 | -6.94 | -17.30 | 65 |
| 21 | Daily: Bullish score | daily | 87.41 | -12.59 | 17 | 17.6 | -3.36 | -0.46 | -19.56 | 14 |
| 22 | Squeeze breakout · 1h | breakout | 87.32 | -12.68 | 67 | 20.9 | -11.00 | -4.31 | -15.99 | 72 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 24 | Opening range 30m | breakout | 86.25 | -13.75 | 438 | 33.6 | -9.87 | -3.13 | -14.11 | 575 |
| 25 | Agent | meta | 84.50 | -15.50 | 205 | 36.1 | -15.66 | -7.42 | -16.00 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.67 | -17.33 | 181 | 28.2 | -25.24 | -6.95 | -26.80 | 203 |
| 27 | Agent (aggressive) | meta | 81.42 | -18.58 | 98 | 33.7 | -17.78 | -4.84 | -18.11 | 96 |
| 28 | Keltner breakout · 1h | breakout | 81.17 | -18.83 | 121 | 25.6 | -18.82 | -4.10 | -27.10 | 157 |
| 29 | Max aggression: 5-day momentum | meta | 80.35 | -19.65 | 21 | 42.9 | -47.77 | -3.15 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 31 | Donchian 55/20 · 1h | breakout | 80.28 | -19.72 | 76 | 13.2 | -24.96 | -6.49 | -29.05 | 84 |
| 32 | Volume breakout · 1h | breakout | 79.83 | -20.17 | 162 | 28.4 | -16.03 | -5.09 | -22.00 | 81 |
| 33 | Opening range 15m | breakout | 78.21 | -21.79 | 532 | 31.6 | -16.62 | -4.45 | -21.37 | 686 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.11 | -22.89 | 2 | 0.0 | -14.83 | -1.82 | -24.84 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 77.08 | -22.93 | 30 | 26.7 | -23.95 | -0.90 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.67 | -24.34 | 2 | 0.0 | -14.78 | -2.06 | -28.91 | 1 |
| 37 | ADX DI cross · 1h | trend | 75.25 | -24.75 | 207 | 19.3 | -28.30 | -4.54 | -35.87 | 261 |
| 38 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.39 | -8.54 | -29.91 | 112 |
| 39 | Bollinger breakout · 1h | breakout | 74.40 | -25.60 | 186 | 22.0 | -25.39 | -5.47 | -33.12 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.94 | -27.06 | 338 | 43.5 | -33.28 | -4.95 | -33.90 | 417 |
| 41 | Supertrend · 1h | trend | 71.90 | -28.10 | 187 | 16.0 | -31.96 | -5.39 | -39.67 | 200 |
| 42 | MACD zero-line · 1h | trend | 71.74 | -28.26 | 178 | 18.0 | -25.73 | -5.09 | -32.37 | 199 |
| 43 | Triple EMA stack · 1h | trend | 71.50 | -28.50 | 154 | 14.9 | -30.39 | -6.09 | -36.59 | 191 |
| 44 | RSI momentum · 1h | momentum | 71.50 | -28.50 | 175 | 14.3 | -31.56 | -5.80 | -38.25 | 202 |
| 45 | MFI reversion · 1h | reversion | 71.34 | -28.66 | 421 | 34.2 | -25.06 | -3.60 | -28.35 | 163 |
| 46 | Heikin-Ashi · 1h | trend | 71.03 | -28.97 | 461 | 23.2 | -39.07 | -7.45 | -43.59 | 638 |
| 47 | EMA 20/50 cross · 1h | trend | 70.75 | -29.25 | 112 | 9.8 | -35.52 | -9.74 | -38.77 | 114 |
| 48 | ROC + volume · 1h | momentum | 70.54 | -29.46 | 405 | 28.4 | -28.14 | -4.60 | -37.76 | 354 |
| 49 | MACD cross · 1h | trend | 70.27 | -29.73 | 409 | 22.2 | -34.44 | -5.03 | -43.85 | 476 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.15 | -30.85 | 304 | 19.1 | -34.27 | -7.26 | -39.32 | 262 |
| 52 | Donchian 20/10 · 1h | breakout | 67.74 | -32.26 | 158 | 18.4 | -30.51 | -5.09 | -39.11 | 206 |
| 53 | CCI reversion · 1h | reversion | 66.95 | -33.05 | 378 | 42.1 | -41.23 | -6.75 | -42.69 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 65.41 | -34.59 | 340 | 38.2 | -37.54 | -5.71 | -37.93 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 63.74 | -36.26 | 278 | 11.2 | -40.04 | -7.97 | -45.67 | 320 |
| 56 | Williams %R · 1h | reversion | 63.55 | -36.45 | 425 | 41.2 | -45.33 | -7.68 | -45.67 | 546 |
| 57 | Agent (ML meta-label) | meta | 60.16 | -39.84 | 1882 | 24.4 | -22.29 | -3.76 | -26.75 | 316 |
| 58 | Z-score reversion · 1h | reversion | 58.78 | -41.22 | 221 | 35.7 | -35.76 | -4.94 | -37.11 | 244 |
| 59 | RSI(14) reversion · 1h | reversion | 58.69 | -41.31 | 204 | 31.9 | -40.95 | -6.02 | -42.30 | 241 |
| 60 | VWAP momentum · 1h | momentum | 57.80 | -42.20 | 952 | 21.7 | -52.88 | -9.52 | -57.56 | 1201 |
| 61 | Candlestick reversal · 1h | reversion | 56.21 | -43.79 | 540 | 26.9 | -46.59 | -8.47 | -46.61 | 614 |
| 62 | Three white soldiers | momentum | 55.89 | -44.12 | 578 | 14.7 | -49.38 | -22.03 | -49.45 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.40 | -99.01 | 5290 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.24 | -25.32 | -81.85 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.99 | -43.61 | -93.99 | 2496 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.17 | -31.69 | -90.22 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -39.33 | -91.32 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -30.80 | -90.03 | 2135 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -47.23 | -97.91 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -52.99 | -96.52 | 3429 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -37.60 | -93.73 | 2247 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -33.16 | -82.74 | 1634 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.14 | -99.59 | 6055 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.01 | -41.18 | -92.03 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.13 | -37.72 | -95.14 | 3332 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.87 | -99.81 | 6134 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -42.23 | -92.25 | 2249 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.63 | -26.10 | -76.63 | 1669 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -57.91 | -97.65 | 3459 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -55.26 | -99.01 | 4956 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.50 | -27.05 | -68.54 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -54.56 | -94.64 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.60 | -37.71 | -84.61 | 1750 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.41 | -99.69 | 6392 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.64 | -30.06 | -90.64 | 2333 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.69 | -18.60 | -79.84 | 1814 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.92 | -35.20 | -90.92 | 2158 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -45.22 | -97.54 | 3934 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -59.23 | -89.60 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.59 | -30.53 | -66.59 | 830 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.70 | -22.94 | -72.51 | 1241 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.45 | -17.66 | -80.49 | 1765 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.05 | -97.57 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -98.45 | -99.94 | 8392 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T15:35 | Agent (rotation) | buy | SQQQ | 31.29 | — | entry |
| 2026-11-17T15:35 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 110.78 | — | entry |
| 2026-11-17T15:35 | Agent (ML meta-label) | buy | SQQQ | 15.04 | — | entry |
| 2026-11-17T15:35 | Agent (ML meta-label) | sell | AMD | 14.91 | -0.30 | selected signal exited |
| 2026-11-17T15:35 | Agent | sell | SOXL | 16.11 | -0.61 | rebalance down |
| 2026-11-17T15:35 | Agent | sell | BITX | 17.00 | -0.11 | selected signal exited |
| 2026-11-17T15:35 | Williams %R · 1h | buy | ETH-USD | 3.53 | — | rebalance up |
| 2026-11-17T15:35 | Williams %R · 1h | sell | TQQQ | 7.82 | -0.27 | stop-loss |
| 2026-11-17T15:35 | Williams %R · 1h | sell | QQQ | 7.95 | -0.10 | stop-loss |
| 2026-11-17T15:35 | Stochastic reversion · 1h | buy | LABU | 4.86 | — | entry |
| 2026-11-17T15:35 | Stochastic reversion · 1h | sell | TQQQ | 4.01 | -0.10 | stop-loss |
| 2026-11-17T15:35 | Stochastic reversion · 1h | sell | TECL | 3.94 | -0.17 | stop-loss |
| 2026-11-17T15:35 | Stochastic reversion · 1h | sell | QQQ | 4.08 | -0.04 | stop-loss |
| 2026-11-17T15:35 | Stochastic reversion · 1h | sell | AMD | 4.03 | -0.08 | stop-loss |
| 2026-11-17T15:35 | Bollinger reversion · 1h | sell | TQQQ | 5.40 | -0.14 | stop-loss |
| 2026-11-17T15:35 | Bollinger reversion · 1h | sell | TECL | 5.31 | -0.23 | stop-loss |
| 2026-11-17T15:35 | Bollinger reversion · 1h | sell | QQQ | 5.49 | -0.05 | stop-loss |
| 2026-11-17T15:35 | Opening range 30m | sell | AMZN | 21.34 | -0.16 | stop-loss |
| 2026-11-17T15:35 | Opening range 15m | sell | AMZN | 19.40 | -0.13 | exit signal |
| 2026-11-17T15:31 | Agent (ML meta-label) | sell | NVDA | 15.00 | -0.21 | selected signal exited |
| 2026-11-17T15:31 | Agent | buy | BITX | 17.12 | — | following MFI reversion |
| 2026-11-17T15:31 | MFI reversion · 1h | buy | ETHU | 8.44 | — | entry signal |
| 2026-11-17T15:31 | CCI reversion · 1h | buy | SOXL | 9.59 | — | entry signal |
| 2026-11-17T15:31 | CCI reversion · 1h | buy | AMZN | 9.66 | — | entry signal |
| 2026-11-17T15:31 | CCI reversion · 1h | buy | AAPL | 9.66 | — | entry signal |
| 2026-11-17T15:31 | CCI reversion · 1h | sell | ETH-USD | 7.13 | -0.10 | rebalance down |
| 2026-11-17T15:31 | CCI reversion · 1h | sell | DOGE-USD | 7.22 | -0.07 | rebalance down |
| 2026-11-17T15:31 | CCI reversion · 1h | sell | BTC-USD | 7.28 | -0.04 | rebalance down |
| 2026-11-17T15:31 | CCI reversion · 1h | sell | AMD | 7.09 | -0.10 | rebalance down |
| 2026-11-17T15:31 | Williams %R · 1h | buy | TSLA | 7.60 | — | entry signal |
| 2026-11-17T15:31 | Stochastic reversion · 1h | buy | GOOGL | 3.87 | — | entry signal |
| 2026-11-17T15:31 | Stochastic reversion · 1h | sell | MSFT | 4.06 | -0.06 | stop-loss |
| 2026-11-17T15:31 | Connors RSI(2) · 1h | sell | AMZN | 20.04 | -0.09 | exit signal |
| 2026-11-17T15:31 | Candlestick reversal · 1h | buy | AMZN | 8.09 | — | entry signal |
| 2026-11-17T15:31 | Candlestick reversal · 1h | sell | NVDA | 8.05 | -0.11 | exit signal |
| 2026-11-17T15:31 | Volume breakout · 1h | buy | SQQQ | 19.90 | — | entry signal |
| 2026-11-17T15:31 | VWAP momentum · 1h | buy | AAPL | 9.65 | — | entry signal |
| 2026-11-17T15:31 | VWAP momentum · 1h | sell | COIN | 7.20 | -0.03 | exit signal |
| 2026-11-17T15:31 | VWAP momentum · 1h | sell | BITX | 7.24 | 0.00 | exit signal |
| 2026-11-17T15:31 | ADX DI cross · 1h | buy | AAPL | 18.76 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 15:39:05.000158+00:00 -> 2026-11-17 15:49:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 15:39:05.000158+00:00 -> 2026-11-17 15:49:05.000158+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
