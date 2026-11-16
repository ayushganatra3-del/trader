# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T15:40:05.000145+00:00 · 62073 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.06 (-14.94%)

Closed trades 196, win rate 35.7%, fees £5.66, max drawdown -15.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 16.79 | -0.25 |
| TSLA | 17.14 | +0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16557 decisions in 2517 calls, $0.2203 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T15:40 | 4 / 14 / 11 | cash |  |
| Breezy | 2026-11-16T15:40 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-11-16T15:40 | 3 / 24 / 2 | COIN 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.56 | 18.56 | 0 | — | 15.65 | 5.17 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 15.38 | 3.13 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.26 | 4.26 | 0 | — | 6.03 | 1.65 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.40 | 3.40 | 33 | 42.4 | 2.53 | 0.71 | -9.64 | 31 |
| 6 | Gap and go | momentum | 100.48 | 0.48 | 193 | 33.2 | 6.90 | 1.92 | -9.06 | 230 |
| 7 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -2.55 | -2.21 | -3.69 | 74 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 1.38 | 0.44 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.24 | -2.76 | 0 | — | -1.75 | -0.53 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 94.71 | -5.29 | 0 | — | -5.69 | -1.50 | -8.27 | 1 |
| 14 | Agent (rotation) | meta | 94.08 | -5.92 | 194 | 29.9 | -2.82 | -0.96 | -8.11 | 153 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 16 | Copy: Insider buying | copy | 92.53 | -7.47 | 47 | 42.6 | -9.25 | -1.86 | -14.95 | 62 |
| 17 | Copy: Congress Democrats (NANC) | copy | 92.19 | -7.81 | 0 | — | -6.31 | -1.68 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.46 | -9.54 | 112 | 23.2 | -15.50 | -7.02 | -17.47 | 66 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -7.37 | -2.07 | -15.48 | 74 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.73 | -13.27 | 16 | 18.8 | -6.50 | -1.07 | -19.56 | 15 |
| 24 | Opening range 30m | breakout | 85.86 | -14.14 | 436 | 33.5 | -10.94 | -3.50 | -14.11 | 583 |
| 25 | Agent | meta | 85.06 | -14.94 | 196 | 35.7 | -14.49 | -7.22 | -15.66 | 196 |
| 26 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -13.54 | -3.64 | -16.59 | 95 |
| 27 | Parabolic SAR · 1h | trend | 83.11 | -16.89 | 180 | 28.3 | -18.29 | -3.97 | -24.82 | 215 |
| 28 | Connors RSI(2) · 1h | reversion | 80.68 | -19.32 | 212 | 40.1 | -14.12 | -6.20 | -14.84 | 98 |
| 29 | Donchian 55/20 · 1h | breakout | 80.58 | -19.42 | 75 | 13.3 | -22.65 | -4.79 | -30.02 | 87 |
| 30 | Keltner breakout · 1h | breakout | 80.32 | -19.68 | 121 | 25.6 | -18.27 | -4.00 | -25.25 | 163 |
| 31 | Volume breakout · 1h | breakout | 79.49 | -20.51 | 161 | 28.6 | -16.48 | -5.21 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 77.92 | -22.08 | 530 | 31.5 | -17.99 | -4.85 | -21.36 | 702 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 77.55 | -22.45 | 2 | 0.0 | -14.60 | -1.79 | -24.26 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 77.10 | -22.90 | 21 | 42.9 | -49.27 | -3.28 | -55.24 | 23 |
| 35 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 36 | Stochastic reversion · 1h | reversion | 75.18 | -24.82 | 322 | 45.3 | -31.04 | -4.64 | -32.19 | 399 |
| 37 | Hold BTC | benchmark | 75.09 | -24.91 | 2 | 0.0 | -16.17 | -2.28 | -28.91 | 1 |
| 38 | ADX DI cross · 1h | trend | 74.49 | -25.51 | 207 | 19.3 | -23.53 | -3.58 | -33.61 | 264 |
| 39 | Bollinger breakout · 1h | breakout | 74.07 | -25.93 | 184 | 22.3 | -24.06 | -5.01 | -31.66 | 234 |
| 40 | Max aggression: 1-day momentum | meta | 73.96 | -26.04 | 30 | 26.7 | -24.41 | -0.91 | -57.50 | 40 |
| 41 | MACD zero-line · 1h | trend | 72.48 | -27.52 | 173 | 18.5 | -23.41 | -4.49 | -30.89 | 195 |
| 42 | MFI reversion · 1h ⏸ | reversion | 72.14 | -27.86 | 419 | 34.1 | -22.51 | -3.07 | -28.69 | 162 |
| 43 | Heikin-Ashi · 1h | trend | 71.25 | -28.75 | 459 | 23.3 | -38.99 | -7.15 | -43.26 | 656 |
| 44 | RSI momentum · 1h | momentum | 71.11 | -28.89 | 174 | 13.8 | -28.82 | -4.76 | -38.29 | 204 |
| 45 | Supertrend · 1h | trend | 70.81 | -29.19 | 186 | 15.6 | -33.07 | -5.63 | -39.67 | 200 |
| 46 | Triple EMA stack · 1h | trend | 70.77 | -29.23 | 153 | 14.4 | -26.68 | -4.30 | -37.83 | 194 |
| 47 | MACD cross · 1h | trend | 70.69 | -29.32 | 399 | 22.8 | -33.11 | -4.71 | -42.72 | 468 |
| 48 | ROC + volume · 1h | momentum | 70.60 | -29.40 | 403 | 28.5 | -27.42 | -4.36 | -37.74 | 356 |
| 49 | EMA 20/50 cross · 1h | trend | 70.43 | -29.57 | 111 | 9.9 | -33.93 | -7.88 | -40.16 | 114 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.98 | -4.97 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.65 | -31.35 | 301 | 19.3 | -30.77 | -5.33 | -39.92 | 265 |
| 52 | CCI reversion · 1h | reversion | 68.02 | -31.98 | 372 | 41.7 | -39.27 | -6.30 | -41.88 | 459 |
| 53 | Donchian 20/10 · 1h | breakout | 67.37 | -32.63 | 157 | 18.5 | -29.03 | -4.46 | -39.11 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 67.05 | -32.95 | 319 | 40.4 | -34.58 | -5.29 | -35.58 | 392 |
| 55 | EMA 9/21 cross · 1h | trend | 64.50 | -35.50 | 269 | 11.5 | -34.49 | -5.66 | -44.00 | 317 |
| 56 | Williams %R · 1h | reversion | 64.16 | -35.84 | 413 | 41.4 | -44.51 | -7.54 | -44.76 | 539 |
| 57 | Agent (ML meta-label) ⏸ | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.42 | -4.17 | -27.10 | 339 |
| 58 | RSI(14) reversion · 1h | reversion | 60.26 | -39.73 | 201 | 32.3 | -40.13 | -5.96 | -40.82 | 242 |
| 59 | Z-score reversion · 1h | reversion | 59.86 | -40.14 | 221 | 35.7 | -34.51 | -4.73 | -35.77 | 237 |
| 60 | VWAP momentum · 1h ⏸ | momentum | 58.65 | -41.35 | 942 | 21.8 | -53.94 | -10.22 | -56.84 | 1212 |
| 61 | Candlestick reversal · 1h | reversion | 57.58 | -42.42 | 526 | 27.2 | -43.88 | -7.73 | -45.27 | 620 |
| 62 | Three white soldiers | momentum | 57.15 | -42.85 | 562 | 14.8 | -49.56 | -22.12 | -49.63 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.54 | -99.02 | 5331 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.22 | -25.91 | -81.22 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -43.70 | -93.85 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.06 | -32.81 | -90.06 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -41.15 | -91.50 | 2333 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.93 | -30.34 | -89.93 | 2152 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -49.07 | -97.91 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -54.91 | -96.31 | 3427 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.52 | -36.00 | -93.52 | 2276 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.66 | -32.65 | -82.67 | 1642 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.46 | -99.60 | 6016 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -43.33 | -92.18 | 2597 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.21 | -35.62 | -95.21 | 3380 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.90 | -99.81 | 6111 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.44 | -42.95 | -92.44 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.45 | -26.41 | -76.47 | 1663 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -56.09 | -97.60 | 3468 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -55.97 | -99.00 | 4945 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.44 | -26.86 | -68.76 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.08 | -94.70 | 2770 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.84 | -37.60 | -84.86 | 1765 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -68.27 | -99.70 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.54 | -30.11 | -90.54 | 2330 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.01 | -18.91 | -80.15 | 1804 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.06 | -36.04 | -91.06 | 2171 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.46 | -44.35 | -97.47 | 3906 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -61.55 | -89.18 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.62 | -29.85 | -66.67 | 830 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.29 | -23.03 | -72.29 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.42 | -17.57 | -80.94 | 1750 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.55 | -45.06 | -97.57 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -96.78 | -99.93 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T15:40 | Three white soldiers | buy | MSFT | 14.29 | — | entry signal |
| 2026-11-16T15:38 | Copy: Insider buying | buy | STWD | 3.05 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | PSEC | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | MDGL | 8.04 | — | rebalance up |
| 2026-11-16T15:38 | Copy: Insider buying | buy | FUN | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | buy | BH | 11.58 | — | entry |
| 2026-11-16T15:38 | Copy: Insider buying | sell | MGM | 11.88 | 0.68 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | KNOP | 11.72 | 0.34 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | BBTX | 11.07 | -0.01 | target is flat |
| 2026-11-16T15:38 | Copy: Insider buying | sell | ASPE | 11.17 | 0.32 | target is flat |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | XRP-USD | 4.58 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | DOGE-USD | 4.57 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | buy | BTC-USD | 4.55 | — | rebalance up |
| 2026-11-16T15:35 | CCI reversion · 1h | sell | AMD | 6.78 | -0.22 | stop-loss |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | NVDA | 4.78 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | MSFT | 4.72 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | buy | AMD | 2.93 | — | rebalance up |
| 2026-11-16T15:35 | Candlestick reversal · 1h | sell | LABU | 11.47 | -0.07 | stop-loss |
| 2026-11-16T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 103.88 | — | entry |
| 2026-11-16T15:30 | Williams %R · 1h | buy | XRP-USD | 3.86 | — | rebalance up |
| 2026-11-16T15:30 | Williams %R · 1h | buy | SOL-USD | 3.90 | — | rebalance up |
| 2026-11-16T15:30 | Williams %R · 1h | buy | ETH-USD | 3.83 | — | rebalance up |
| 2026-11-16T15:30 | Williams %R · 1h | buy | DOGE-USD | 3.29 | — | rebalance up |
| 2026-11-16T15:30 | Williams %R · 1h | sell | TECL | 4.29 | -0.07 | stop-loss |
| 2026-11-16T15:30 | Stochastic reversion · 1h | buy | TNA | 4.28 | — | rebalance up |
| 2026-11-16T15:30 | Stochastic reversion · 1h | buy | AMD | 4.33 | — | rebalance up |
| 2026-11-16T15:30 | Stochastic reversion · 1h | sell | TECL | 12.49 | -0.16 | stop-loss |
| 2026-11-16T15:30 | Connors RSI(2) · 1h | buy | AMZN | 20.13 | — | entry signal |
| 2026-11-16T15:30 | Keltner breakout · 1h | buy | SQQQ | 20.10 | — | entry signal |
| 2026-11-16T15:30 | Bollinger breakout · 1h | buy | SQQQ | 18.55 | — | entry signal |
| 2026-11-16T15:30 | Donchian 20/10 · 1h | buy | SQQQ | 16.87 | — | entry signal |
| 2026-11-16T15:30 | Donchian 20/10 · 1h | sell | AAPL | 17.14 | -0.13 | exit signal |
| 2026-11-16T15:30 | OBV trend · 1h | sell | AAPL | 17.36 | -0.06 | exit signal |
| 2026-11-16T15:30 | RSI momentum · 1h | buy | SQQQ | 17.79 | — | entry signal |
| 2026-11-16T15:30 | RSI momentum · 1h | sell | GOOGL | 17.66 | -0.43 | exit signal |
| 2026-11-16T15:30 | Trend pullback · 1h | sell | AMZN | 23.54 | 0.43 | exit signal |
| 2026-11-16T15:30 | Heikin-Ashi · 1h | sell | MSFT | 14.29 | -0.16 | exit signal |
| 2026-11-16T15:30 | ADX DI cross · 1h | sell | TSLA | 18.36 | -0.27 | exit signal |
| 2026-11-16T15:30 | Parabolic SAR · 1h | sell | AAPL | 21.13 | -0.17 | exit signal |
| 2026-11-16T15:30 | Supertrend · 1h | buy | XRP-USD | 3.78 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 15:40:05.000145+00:00 -> 2026-11-16 15:50:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-18 15:40:05.000145+00:00 -> 2026-11-16 15:50:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
