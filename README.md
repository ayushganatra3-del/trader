# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T15:34:05.000113+00:00 · 75648 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.02 (-23.98%)

Closed trades 250, win rate 36.0%, fees £6.89, max drawdown -24.34%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 15.07 | -0.22 |
| SQQQ | 15.06 | -0.21 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-27 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 15117 decisions in 2454 calls, $0.2027 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T15:34 | 2 / 21 / 7 | cash |  |
| Breezy | 2026-11-27T15:34 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-27T15:34 | 4 / 23 / 3 | COIN 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| EMA 20/50 cross | TECL | 1.74 | +5.81% | 3 |
| Bollinger reversion · 1h | MSFT | 1.74 | +7.75% | 3 |
| Z-score reversion | SQQQ | 1.74 | +8.59% | 5 |
| EMA 20/50 cross | TQQQ | 1.64 | +4.16% | 4 |
| OBV trend | COIN | 1.45 | +1.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.21 | 3.56 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.10 | 16.10 | 0 | — | 14.66 | 4.88 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.99 | 5.99 | 0 | — | 4.83 | 1.32 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.81 | 0.81 | 43 | 27.9 | -1.67 | -0.06 | -15.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.91 | -2.09 | 222 | 31.1 | -0.28 | 0.00 | -7.66 | 210 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.51 | -2.81 | -7.38 | 1 |
| 10 | Hold SPY | benchmark | 94.95 | -5.05 | 0 | — | -5.71 | -1.42 | -11.71 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 94.79 | -5.21 | 172 | 32.6 | -4.95 | -4.22 | -5.79 | 52 |
| 12 | Agent (rotation) | meta | 94.57 | -5.43 | 233 | 28.3 | 0.80 | 0.34 | -6.10 | 182 |
| 13 | Three white soldiers · 1h | momentum | 94.56 | -5.44 | 24 | 12.5 | -3.94 | -4.23 | -6.53 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.52 | -5.48 | 0 | — | -5.20 | -0.97 | -13.24 | 1 |
| 15 | Copy: Insider buying | copy | 93.62 | -6.38 | 63 | 41.3 | -3.20 | -0.47 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 90.76 | -9.24 | 117 | 23.9 | -6.97 | -4.58 | -9.32 | 26 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.86 | -10.14 | 0 | — | -10.94 | -2.31 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.47 | -7.34 | -11.13 | 22 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -13.56 | -2.89 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.92 | -13.08 | 489 | 33.9 | -9.20 | -2.78 | -15.30 | 541 |
| 21 | Daily: Bullish score | daily | 85.06 | -14.94 | 20 | 20.0 | -13.92 | -3.09 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.10 | -2.40 | -20.49 | 152 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 81.80 | -18.20 | 84 | 19.0 | -17.42 | -6.03 | -17.45 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.17 | -20.83 | 226 | 40.7 | -13.80 | -6.39 | -14.44 | 63 |
| 26 | Opening range 15m | breakout | 78.80 | -21.20 | 617 | 31.9 | -18.55 | -5.11 | -24.20 | 667 |
| 27 | Volume breakout · 1h | breakout | 76.67 | -23.33 | 178 | 29.2 | -21.68 | -8.53 | -21.72 | 71 |
| 28 | Agent | meta | 76.02 | -23.98 | 250 | 36.0 | -26.58 | -5.89 | -26.92 | 208 |
| 29 | Parabolic SAR · 1h | trend | 75.88 | -24.12 | 221 | 27.1 | -31.59 | -7.88 | -33.18 | 183 |
| 30 | Agent (aggressive) | meta | 75.29 | -24.71 | 115 | 33.0 | -15.39 | -4.24 | -16.35 | 92 |
| 31 | Max aggression: 5-day momentum | meta | 73.54 | -26.46 | 27 | 37.0 | -52.91 | -2.63 | -67.33 | 21 |
| 32 | Donchian 55/20 · 1h | breakout | 72.93 | -27.07 | 91 | 13.2 | -31.01 | -8.11 | -31.23 | 80 |
| 33 | Ichimoku · 1h | trend | 72.18 | -27.82 | 119 | 15.1 | -30.05 | -7.54 | -30.50 | 100 |
| 34 | Keltner breakout · 1h | breakout | 71.90 | -28.10 | 147 | 23.8 | -27.59 | -6.75 | -27.79 | 152 |
| 35 | Daily: Momentum burst | daily | 70.95 | -29.05 | 31 | 16.1 | -32.26 | -4.36 | -35.32 | 25 |
| 36 | ADX DI cross · 1h | trend | 70.13 | -29.87 | 274 | 19.7 | -38.91 | -7.42 | -40.17 | 281 |
| 37 | Hold BTC | benchmark | 69.09 | -30.91 | 3 | 0.0 | -29.21 | -5.12 | -36.10 | 1 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 68.99 | -31.01 | 3 | 0.0 | -23.27 | -2.79 | -33.66 | 1 |
| 39 | Stochastic reversion · 1h | reversion | 67.59 | -32.41 | 416 | 40.4 | -31.29 | -3.16 | -42.39 | 428 |
| 40 | Supertrend · 1h | trend | 67.50 | -32.50 | 225 | 18.7 | -39.12 | -7.56 | -41.51 | 214 |
| 41 | Bollinger breakout · 1h | breakout | 67.05 | -32.95 | 220 | 23.2 | -30.57 | -7.91 | -31.73 | 211 |
| 42 | OBV trend · 1h | momentum | 65.77 | -34.23 | 332 | 19.6 | -40.10 | -9.71 | -40.27 | 213 |
| 43 | EMA 20/50 cross · 1h | trend | 65.31 | -34.69 | 128 | 9.4 | -38.38 | -10.39 | -38.86 | 119 |
| 44 | Triple EMA stack · 1h | trend | 64.51 | -35.49 | 174 | 14.9 | -40.96 | -10.11 | -41.63 | 164 |
| 45 | MACD zero-line · 1h | trend | 64.29 | -35.71 | 206 | 16.5 | -35.62 | -9.33 | -37.39 | 188 |
| 46 | MFI reversion · 1h | reversion | 62.92 | -37.08 | 528 | 33.7 | -32.45 | -4.75 | -38.15 | 194 |
| 47 | RSI momentum · 1h | momentum | 62.65 | -37.35 | 208 | 15.4 | -42.27 | -9.13 | -42.76 | 191 |
| 48 | Donchian 20/10 · 1h | breakout | 62.10 | -37.90 | 188 | 17.0 | -38.45 | -8.36 | -40.84 | 196 |
| 49 | Max aggression: 1-day momentum | meta | 60.66 | -39.34 | 35 | 28.6 | -59.70 | -4.24 | -63.62 | 38 |
| 50 | Heikin-Ashi · 1h | trend | 60.43 | -39.57 | 564 | 22.0 | -48.89 | -9.70 | -49.90 | 644 |
| 51 | ROC + volume · 1h | momentum | 59.84 | -40.16 | 477 | 26.8 | -40.68 | -7.87 | -40.85 | 341 |
| 52 | EMA 9/21 cross · 1h | trend | 58.98 | -41.02 | 315 | 12.1 | -44.32 | -9.97 | -46.70 | 308 |
| 53 | MACD cross · 1h | trend | 57.53 | -42.47 | 502 | 20.9 | -53.48 | -10.41 | -55.66 | 507 |
| 54 | Agent (ML meta-label) | meta | 55.28 | -44.72 | 2075 | 25.4 | -26.00 | -3.32 | -30.98 | 302 |
| 55 | CCI reversion · 1h | reversion | 52.39 | -47.61 | 467 | 38.3 | -51.61 | -8.38 | -55.11 | 494 |
| 56 | Bollinger reversion · 1h | reversion | 51.99 | -48.01 | 407 | 36.6 | -40.08 | -4.79 | -45.50 | 428 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -57.15 | -9.48 | -59.72 | 687 |
| 58 | VWAP momentum · 1h | momentum | 50.83 | -49.17 | 1126 | 21.2 | -60.74 | -12.91 | -61.75 | 1173 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.49 | -8.97 | -59.48 | 594 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -43.60 | -99.15 | 5324 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.26 | -29.57 | -83.39 | 1401 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.12 | -42.52 | -94.12 | 2382 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.02 | -28.60 | -90.25 | 1857 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -36.03 | -91.31 | 2195 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.52 | -26.09 | -88.52 | 1914 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -43.29 | -98.08 | 3352 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -47.43 | -96.91 | 3345 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.40 | -33.30 | -93.40 | 2079 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.06 | -33.94 | -82.22 | 1522 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.69 | -49.98 | -99.69 | 6218 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -35.40 | -92.70 | 2440 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.40 | -34.36 | -94.43 | 3124 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -57.94 | -99.81 | 6013 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.73 | -38.59 | -92.74 | 2220 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.04 | -18.50 | -51.19 | 653 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.72 | -22.33 | -78.03 | 1599 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -51.30 | -97.66 | 3197 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -54.38 | -99.15 | 5062 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -22.64 | -69.60 | 1204 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -42.92 | -94.55 | 2636 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -45.93 | -6.22 | -51.27 | 284 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.19 | -32.09 | -84.48 | 1641 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -63.29 | -99.77 | 6459 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.53 | -29.86 | -91.63 | 2471 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.57 | -19.43 | -82.86 | 1951 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.28 | -31.68 | -91.46 | 2128 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -45.54 | -98.21 | 4006 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.97 | -41.88 | -90.10 | 2182 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.97 | -28.23 | -67.97 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.72 | -26.41 | -72.86 | 1149 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.75 | -19.00 | -84.89 | 1835 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -46.34 | -98.10 | 4359 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -80.93 | -99.94 | 8220 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -44.98 | -6.46 | -52.59 | 301 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T15:30 | Agent (ML meta-label) | sell | SQQQ | 13.50 | -0.56 | selected signal exited |
| 2026-11-27T15:30 | Stochastic reversion · 1h | buy | NVDA | 10.43 | — | rebalance up |
| 2026-11-27T15:30 | Stochastic reversion · 1h | buy | MSTR | 10.01 | — | rebalance up |
| 2026-11-27T15:30 | Stochastic reversion · 1h | buy | MSFT | 10.52 | — | rebalance up |
| 2026-11-27T15:30 | Stochastic reversion · 1h | buy | AMD | 10.22 | — | rebalance up |
| 2026-11-27T15:30 | Stochastic reversion · 1h | sell | TECL | 7.12 | 0.79 | exit signal |
| 2026-11-27T15:30 | Stochastic reversion · 1h | sell | SOXL | 7.84 | 1.51 | exit signal |
| 2026-11-27T15:30 | Stochastic reversion · 1h | sell | COIN | 6.76 | 0.60 | exit signal |
| 2026-11-27T15:30 | Stochastic reversion · 1h | sell | AMZN | 5.22 | 0.25 | exit signal |
| 2026-11-27T15:30 | Bollinger reversion · 1h | sell | AMZN | 13.19 | 0.14 | exit signal |
| 2026-11-27T15:30 | Connors RSI(2) · 1h | buy | SQQQ | 19.79 | — | entry signal |
| 2026-11-27T15:30 | Volume breakout · 1h | buy | TSLA | 19.17 | — | entry signal |
| 2026-11-27T15:30 | Volume breakout · 1h | buy | META | 19.17 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | buy | TSLA | 11.99 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | buy | TNA | 11.99 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | buy | PLTR | 11.99 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | buy | META | 11.99 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | buy | IWM | 11.99 | — | entry signal |
| 2026-11-27T15:30 | Keltner breakout · 1h | sell | LABU | 6.44 | 0.03 | rebalance down |
| 2026-11-27T15:30 | Bollinger breakout · 1h | buy | TNA | 13.42 | — | entry signal |
| 2026-11-27T15:30 | Bollinger breakout · 1h | buy | PLTR | 13.42 | — | entry signal |
| 2026-11-27T15:30 | Bollinger breakout · 1h | buy | META | 13.42 | — | entry signal |
| 2026-11-27T15:30 | Bollinger breakout · 1h | buy | IWM | 13.42 | — | entry signal |
| 2026-11-27T15:30 | Bollinger breakout · 1h | buy | AAPL | 13.42 | — | entry signal |
| 2026-11-27T15:30 | Donchian 55/20 · 1h | buy | TSLA | 17.94 | — | entry signal |
| 2026-11-27T15:30 | Donchian 55/20 · 1h | buy | PLTR | 18.24 | — | entry signal |
| 2026-11-27T15:30 | Donchian 55/20 · 1h | buy | AAPL | 18.24 | — | entry signal |
| 2026-11-27T15:30 | OBV trend · 1h | buy | TSLA | 16.45 | — | entry signal |
| 2026-11-27T15:30 | OBV trend · 1h | sell | SQQQ | 16.15 | -0.54 | exit signal |
| 2026-11-27T15:30 | RSI momentum · 1h | buy | TSLA | 10.44 | — | entry signal |
| 2026-11-27T15:30 | RSI momentum · 1h | buy | TNA | 10.45 | — | entry signal |
| 2026-11-27T15:30 | RSI momentum · 1h | buy | IWM | 10.45 | — | entry signal |
| 2026-11-27T15:30 | RSI momentum · 1h | buy | AAPL | 10.45 | — | entry signal |
| 2026-11-27T15:30 | RSI momentum · 1h | sell | PLTR | 5.36 | 0.12 | rebalance down |
| 2026-11-27T15:30 | RSI momentum · 1h | sell | LABU | 5.36 | 0.27 | rebalance down |
| 2026-11-27T15:30 | ROC + volume · 1h | buy | UPRO | 5.98 | — | entry signal |
| 2026-11-27T15:30 | ROC + volume · 1h | buy | TSLA | 5.99 | — | entry signal |
| 2026-11-27T15:30 | ROC + volume · 1h | buy | TQQQ | 5.99 | — | entry signal |
| 2026-11-27T15:30 | ROC + volume · 1h | buy | TNA | 5.99 | — | entry signal |
| 2026-11-27T15:30 | ROC + volume · 1h | buy | SOXL | 5.99 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 15:34:05.000113+00:00 -> 2026-11-27 15:44:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
