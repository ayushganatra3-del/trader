# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T11:05:05.000124+00:00 · 75412 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £76.44 (-23.56%)

Closed trades 250, win rate 36.0%, fees £6.87, max drawdown -24.09%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, ANAB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 8727 decisions in 1746 calls, $0.1217 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T11:05 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-27T11:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T11:05 | 2 / 3 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.60 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.86 | 15.86 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.01 | 5.01 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.03 | -5.97 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.54 | -6.46 | 24 | 12.5 | -5.28 | -7.70 | -6.53 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.24 | -6.76 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.08 | -6.92 | 63 | 41.3 | -4.85 | -0.81 | -14.79 | 69 |
| 16 | Trend pullback · 1h | trend | 91.55 | -8.45 | 116 | 24.1 | -7.76 | -4.59 | -10.99 | 30 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.12 | -10.88 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.09 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.20 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.83 | -2.34 | -20.49 | 153 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.06 | -16.94 | 79 | 20.3 | -19.31 | -6.52 | -19.54 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 79.96 | -20.04 | 224 | 41.1 | -13.08 | -5.96 | -13.42 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.18 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.98 | -23.02 | 174 | 29.3 | -22.11 | -8.63 | -22.50 | 72 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -26.83 | -5.95 | -27.37 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -16.90 | -4.53 | -17.30 | 91 |
| 30 | Parabolic SAR · 1h | trend | 75.39 | -24.61 | 216 | 27.8 | -33.96 | -8.05 | -35.47 | 187 |
| 31 | Donchian 55/20 · 1h | breakout | 74.77 | -25.23 | 88 | 13.6 | -28.97 | -7.45 | -29.32 | 77 |
| 32 | Ichimoku · 1h | trend | 74.36 | -25.64 | 114 | 15.8 | -27.68 | -6.75 | -29.63 | 100 |
| 33 | Max aggression: 5-day momentum | meta | 73.95 | -26.05 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 34 | Keltner breakout · 1h | breakout | 72.84 | -27.16 | 143 | 24.5 | -27.32 | -6.63 | -27.48 | 150 |
| 35 | Daily: Momentum burst | daily | 71.05 | -28.95 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.98 | -29.02 | 3 | 0.0 | -27.19 | -4.65 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.97 | -30.03 | 272 | 19.9 | -37.58 | -6.97 | -38.53 | 290 |
| 38 | Bollinger breakout · 1h | breakout | 68.13 | -31.87 | 215 | 22.8 | -31.29 | -7.94 | -31.99 | 211 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.80 | -32.20 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.41 | -32.59 | 221 | 17.6 | -39.28 | -7.58 | -41.85 | 209 |
| 41 | Stochastic reversion · 1h | reversion | 66.62 | -33.38 | 411 | 39.9 | -32.79 | -3.38 | -42.70 | 435 |
| 42 | OBV trend · 1h | momentum | 66.39 | -33.61 | 325 | 19.7 | -39.91 | -9.56 | -41.12 | 225 |
| 43 | EMA 20/50 cross · 1h | trend | 66.17 | -33.83 | 126 | 9.5 | -36.92 | -9.66 | -38.46 | 116 |
| 44 | Triple EMA stack · 1h | trend | 65.90 | -34.10 | 172 | 15.1 | -40.07 | -9.42 | -41.96 | 168 |
| 45 | RSI momentum · 1h | momentum | 63.63 | -36.37 | 203 | 14.8 | -41.88 | -8.87 | -43.57 | 192 |
| 46 | MACD zero-line · 1h | trend | 63.03 | -36.98 | 206 | 16.5 | -36.36 | -9.93 | -36.92 | 198 |
| 47 | MFI reversion · 1h | reversion | 62.63 | -37.37 | 520 | 32.7 | -32.20 | -4.70 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.45 | -38.55 | 183 | 17.5 | -40.62 | -8.77 | -42.91 | 201 |
| 49 | Heikin-Ashi · 1h | trend | 60.75 | -39.25 | 561 | 21.7 | -49.12 | -9.89 | -49.54 | 648 |
| 50 | ROC + volume · 1h | momentum | 60.65 | -39.35 | 472 | 26.9 | -39.76 | -7.58 | -40.97 | 339 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.91 | -41.09 | 314 | 12.1 | -43.84 | -9.70 | -45.87 | 327 |
| 53 | MACD cross · 1h | trend | 57.34 | -42.66 | 497 | 21.1 | -52.72 | -10.42 | -54.55 | 511 |
| 54 | Agent (ML meta-label) | meta | 56.23 | -43.77 | 2074 | 25.4 | -25.12 | -3.34 | -31.64 | 319 |
| 55 | CCI reversion · 1h | reversion | 52.58 | -47.42 | 467 | 38.3 | -52.59 | -8.76 | -55.31 | 499 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 406 | 36.5 | -40.74 | -4.92 | -45.50 | 429 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.91 | -8.99 | -58.48 | 686 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.92 | -9.15 | -59.57 | 603 |
| 59 | VWAP momentum · 1h | momentum | 50.66 | -49.34 | 1112 | 21.3 | -60.38 | -12.96 | -60.83 | 1192 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -43.91 | -99.17 | 5393 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.10 | -29.26 | -83.41 | 1419 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.13 | -43.21 | -94.14 | 2398 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.93 | -28.35 | -90.25 | 1874 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.16 | -36.12 | -91.29 | 2215 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.69 | -26.21 | -88.69 | 1936 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.09 | -43.68 | -98.11 | 3399 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -47.99 | -96.85 | 3355 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -32.77 | -93.47 | 2118 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -34.07 | -82.03 | 1509 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -49.09 | -99.68 | 6267 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -35.38 | -92.70 | 2464 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.32 | -34.05 | -94.32 | 3151 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -57.92 | -99.81 | 6054 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.83 | -39.44 | -92.90 | 2247 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.21 | -18.64 | -51.40 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.17 | -22.98 | -78.28 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -52.46 | -97.67 | 3232 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -53.37 | -99.15 | 5101 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.74 | -23.11 | -69.92 | 1208 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -44.27 | -94.63 | 2663 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.75 | -6.46 | -51.25 | 287 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.34 | -32.91 | -84.35 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -60.48 | -99.76 | 6501 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.48 | -29.56 | -91.72 | 2493 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.74 | -19.52 | -83.23 | 1972 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.36 | -30.95 | -91.67 | 2146 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.18 | -44.91 | -98.19 | 4033 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.15 | -43.35 | -90.33 | 2196 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.41 | -28.89 | -68.44 | 787 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.37 | -26.31 | -72.62 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.35 | -18.41 | -84.75 | 1821 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -45.64 | -98.09 | 4392 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.74 | -99.94 | 8297 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.30 | -6.76 | -52.52 | 294 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T10:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.33 | -0.01 | exit signal |
| 2026-11-27T08:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.53 | 0.00 | exit signal |
| 2026-11-27T06:02 | Squeeze breakout · 1h | buy | XRP-USD | 4.16 | — | rebalance up |
| 2026-11-27T06:02 | Squeeze breakout · 1h | sell | SOL-USD | 4.16 | -0.01 | rebalance down |
| 2026-11-27T06:00 | Squeeze breakout · 1h | buy | XRP-USD | 12.47 | — | entry signal |
| 2026-11-27T06:00 | Squeeze breakout · 1h | buy | BTC-USD | 16.65 | — | entry signal |
| 2026-11-27T06:00 | Squeeze breakout · 1h | sell | ETH-USD | 4.16 | -0.00 | rebalance down |
| 2026-11-27T06:00 | Squeeze breakout · 1h | sell | DOGE-USD | 4.20 | 0.01 | rebalance down |
| 2026-11-27T06:00 | Keltner breakout · 1h | buy | XRP-USD | 10.64 | — | entry signal |
| 2026-11-27T06:00 | Keltner breakout · 1h | buy | ETH-USD | 14.60 | — | entry signal |
| 2026-11-27T06:00 | Keltner breakout · 1h | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-11-27T06:00 | Keltner breakout · 1h | sell | SOL-USD | 3.67 | -0.00 | rebalance down |
| 2026-11-27T06:00 | Donchian 55/20 · 1h | buy | XRP-USD | 18.58 | — | entry signal |
| 2026-11-27T06:00 | Donchian 55/20 · 1h | buy | ETH-USD | 18.72 | — | entry signal |
| 2026-11-27T05:00 | Squeeze breakout · 1h | buy | SOL-USD | 20.77 | — | entry signal |
| 2026-11-27T05:00 | Squeeze breakout · 1h | buy | ETH-USD | 20.77 | — | entry signal |
| 2026-11-27T05:00 | Squeeze breakout · 1h | buy | DOGE-USD | 20.77 | — | entry signal |
| 2026-11-27T05:00 | MACD cross · 1h | buy | XRP-USD | 2.49 | — | entry signal |
| 2026-11-27T04:00 | Keltner breakout · 1h | buy | SOL-USD | 18.24 | — | entry signal |
| 2026-11-27T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.33 | — | entry signal |
| 2026-11-27T04:00 | Heikin-Ashi · 1h | buy | BTC-USD | 2.33 | — | entry signal |
| 2026-11-27T04:00 | MACD cross · 1h | buy | DOGE-USD | 2.60 | — | entry signal |
| 2026-11-27T03:00 | CCI reversion · 1h | sell | XRP-USD | 3.51 | 0.01 | exit signal |
| 2026-11-27T03:00 | CCI reversion · 1h | sell | ETH-USD | 3.77 | 0.02 | exit signal |
| 2026-11-27T03:00 | CCI reversion · 1h | sell | DOGE-USD | 3.79 | 0.04 | exit signal |
| 2026-11-27T03:00 | Bollinger reversion · 1h | sell | XRP-USD | 10.49 | 0.06 | exit signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | ETH-USD | 19.13 | — | entry signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | DOGE-USD | 19.21 | — | entry signal |
| 2026-11-27T03:00 | Volume breakout · 1h | buy | BTC-USD | 19.21 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | XRP-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | SOL-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | ETH-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | DOGE-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Bollinger breakout · 1h | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-11-27T03:00 | Donchian 55/20 · 1h | buy | SOL-USD | 18.65 | — | entry signal |
| 2026-11-27T03:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 18.65 | — | entry signal |
| 2026-11-27T03:00 | Donchian 20/10 · 1h | buy | BTC-USD | 3.28 | — | entry signal |
| 2026-11-27T03:00 | Donchian 20/10 · 1h | sell | XRP-USD | 3.28 | 0.03 | rebalance down |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | SOL-USD | 10.01 | — | entry signal |
| 2026-11-27T03:00 | ROC + volume · 1h | buy | ETH-USD | 10.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 11:05:05.000124+00:00 -> 2026-11-27 11:15:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
