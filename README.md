# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T03:10:05.000132+00:00 · 62663 ticks

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

Today: 2490 decisions in 498 calls, $0.0349 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T03:10 | 3 / 2 / 0 | DOGE-USD 17%, SOL-USD 16% |  |
| Breezy | 2026-11-17T03:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T03:10 | 4 / 1 / 0 | SOL-USD 66% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.12 | 18.12 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.78 | 3.78 | 0 | — | 5.47 | 1.51 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.69 | -3.31 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 93.89 | -6.11 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 15 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.73 | -8.27 | 47 | 42.6 | -10.04 | -2.01 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.63 | -8.37 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -10.76 | -3.99 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.71 | -13.29 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.28 | -16.72 | 180 | 28.3 | -22.88 | -6.17 | -24.65 | 212 |
| 28 | Keltner breakout · 1h | breakout | 80.60 | -19.40 | 121 | 25.6 | -18.88 | -4.19 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -24.61 | -6.13 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.67 | 213 | 39.9 | -14.54 | -6.43 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Max aggression: 5-day momentum | meta | 78.16 | -21.84 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 33 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.36 | -22.64 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.65 | -24.35 | 2 | 0.0 | -15.04 | -2.11 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.03 | -8.26 | -31.55 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.97 | -25.03 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.75 | -25.25 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.36 | -25.64 | 185 | 22.2 | -24.53 | -5.24 | -31.78 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | MFI reversion · 1h | reversion | 72.08 | -27.92 | 419 | 34.1 | -25.55 | -3.62 | -29.02 | 162 |
| 42 | MACD zero-line · 1h | trend | 72.01 | -27.99 | 176 | 18.2 | -25.48 | -5.03 | -31.93 | 196 |
| 43 | Heikin-Ashi · 1h | trend | 71.80 | -28.20 | 459 | 23.3 | -39.07 | -7.45 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.65 | -28.35 | 187 | 16.0 | -32.31 | -5.48 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.27 | -28.73 | 175 | 14.3 | -31.19 | -5.64 | -38.07 | 202 |
| 46 | Triple EMA stack · 1h | trend | 71.24 | -28.76 | 154 | 14.9 | -28.81 | -5.30 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.95 | -29.05 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.84 | -29.16 | 405 | 22.5 | -33.60 | -4.81 | -43.23 | 474 |
| 49 | ROC + volume · 1h | momentum | 70.59 | -29.41 | 405 | 28.4 | -27.96 | -4.57 | -37.95 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.23 | -30.77 | 303 | 19.1 | -30.89 | -5.85 | -39.29 | 259 |
| 52 | CCI reversion · 1h | reversion | 68.00 | -32.00 | 377 | 41.9 | -40.14 | -6.50 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.73 | -32.27 | 157 | 18.5 | -30.05 | -4.91 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | Williams %R · 1h | reversion | 64.18 | -35.82 | 418 | 41.1 | -44.43 | -7.45 | -45.12 | 544 |
| 56 | EMA 9/21 cross · 1h | trend | 64.10 | -35.90 | 275 | 11.3 | -38.65 | -7.57 | -44.88 | 317 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -20.81 | -2.91 | -25.58 | 333 |
| 58 | Z-score reversion · 1h | reversion | 59.64 | -40.36 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.31 | -40.69 | 204 | 31.9 | -40.69 | -5.98 | -42.13 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.58 | -41.42 | 944 | 21.7 | -53.14 | -9.27 | -57.70 | 1207 |
| 61 | Candlestick reversal · 1h | reversion | 57.30 | -42.70 | 537 | 27.0 | -45.57 | -8.22 | -45.68 | 614 |
| 62 | Three white soldiers | momentum | 56.30 | -43.70 | 572 | 14.7 | -49.27 | -21.88 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.94 | -99.01 | 5298 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.32 | -25.39 | -81.40 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.93 | -42.55 | -93.94 | 2506 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.91 | -30.83 | -89.98 | 1932 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -39.63 | -91.40 | 2319 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.16 | -30.28 | -90.17 | 2155 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -46.55 | -97.92 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -52.08 | -96.48 | 3440 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.59 | -36.92 | -93.59 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.72 | -32.85 | -82.73 | 1633 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.80 | -99.59 | 6046 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.12 | -41.45 | -92.13 | 2582 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.24 | -35.84 | -95.24 | 3359 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.10 | -99.81 | 6152 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -42.77 | -92.40 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.43 | -25.78 | -76.43 | 1647 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -57.76 | -97.60 | 3467 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -53.24 | -98.99 | 4942 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.73 | -27.36 | -68.73 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -54.34 | -94.71 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.59 | -36.97 | -84.59 | 1742 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.84 | -99.69 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.49 | -29.86 | -90.49 | 2338 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.55 | -18.45 | -79.57 | 1813 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.99 | -35.11 | -91.00 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -43.81 | -97.45 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -57.84 | -89.27 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -29.64 | -66.44 | 827 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.03 | -23.10 | -72.04 | 1247 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.45 | -17.57 | -80.72 | 1759 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -44.72 | -97.57 | 4355 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -93.97 | -99.94 | 8390 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T03:00 | ROC + volume · 1h | sell | DOGE-USD | 17.26 | -0.35 | exit signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | buy | SOL-USD | 18.01 | — | entry signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | sell | ETH-USD | 17.97 | -0.16 | exit signal |
| 2026-11-17T03:00 | MACD zero-line · 1h | sell | BTC-USD | 17.84 | -0.33 | exit signal |
| 2026-11-17T03:00 | MACD cross · 1h | sell | ETH-USD | 14.10 | -0.19 | exit signal |
| 2026-11-17T03:00 | MACD cross · 1h | sell | BTC-USD | 14.08 | -0.14 | exit signal |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 5.31 | — | rebalance up |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.34 | — | rebalance up |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.61 | -0.21 | exit signal |
| 2026-11-17T03:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 10.59 | -0.15 | exit signal |
| 2026-11-17T02:15 | Three white soldiers | sell | XRP-USD | 14.01 | -0.14 | stop-loss |
| 2026-11-17T01:50 | Three white soldiers | sell | ETH-USD | 14.01 | -0.14 | stop-loss |
| 2026-11-17T01:45 | Three white soldiers | buy | XRP-USD | 14.14 | — | entry signal |
| 2026-11-17T01:45 | Three white soldiers | buy | ETH-USD | 14.14 | — | entry signal |
| 2026-11-17T01:00 | Bollinger breakout · 1h | sell | ETH-USD | 18.24 | -0.41 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.88 | — | rebalance up |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | ETH-USD | 9.69 | -0.09 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | BTC-USD | 9.68 | -0.09 | exit signal |
| 2026-11-17T01:00 | MACD zero-line · 1h | sell | DOGE-USD | 17.82 | -0.31 | exit signal |
| 2026-11-17T01:00 | MACD cross · 1h | buy | XRP-USD | 4.13 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | SOL-USD | 4.00 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | ETH-USD | 4.06 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | BTC-USD | 4.03 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | sell | DOGE-USD | 9.99 | -0.13 | exit signal |
| 2026-11-17T00:00 | MFI reversion · 1h | buy | ETH-USD | 7.21 | — | entry |
| 2026-11-17T00:00 | MFI reversion · 1h | buy | BTC-USD | 7.21 | — | entry |
| 2026-11-17T00:00 | Volume breakout · 1h | sell | ETH-USD | 19.61 | -0.38 | exit signal |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | SOL-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | ETH-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | BTC-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.53 | -0.08 | exit signal |
| 2026-11-16T23:00 | CCI reversion · 1h | sell | SOL-USD | 13.71 | 0.09 | exit signal |
| 2026-11-16T22:00 | CCI reversion · 1h | sell | BTC-USD | 17.12 | 0.08 | exit signal |
| 2026-11-16T22:00 | RSI(14) reversion · 1h | sell | BTC-USD | 12.34 | -0.01 | exit signal |
| 2026-11-16T22:00 | MACD zero-line · 1h | buy | BTC-USD | 18.17 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.61 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 10.76 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.38 | -0.00 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.22 | -0.05 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.39 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 03:10:05.000132+00:00 -> 2026-11-17 03:20:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 03:10:05.000132+00:00 -> 2026-11-17 03:20:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
