# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T05:05:05.000138+00:00 · 64035 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 4089 decisions in 819 calls, $0.0573 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T05:05 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-18T05:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T05:05 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |
| Squeeze breakout | SQQQ | 1.74 | +6.13% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.80 | 16.80 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.39 | 3.39 | 0 | — | 5.76 | 1.26 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.44 | -3.56 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.55 | -4.45 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.35 | -7.65 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.74 | -9.26 | 153 | 46.4 | -11.59 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.48 | -9.52 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.38 | -7.28 | -13.38 | 58 |
| 20 | Copy: Insider buying | copy | 90.12 | -9.88 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.13 | -12.87 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.51 | -13.49 | 68 | 20.6 | -16.77 | -7.06 | -19.74 | 77 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.35 | -16.95 | 199 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.77 | -18.23 | 184 | 27.7 | -25.53 | -7.14 | -28.05 | 203 |
| 28 | Keltner breakout · 1h | breakout | 80.61 | -19.39 | 122 | 26.2 | -18.94 | -4.04 | -27.13 | 154 |
| 29 | Connors RSI(2) · 1h | reversion | 80.43 | -19.57 | 215 | 40.0 | -14.39 | -6.40 | -14.66 | 90 |
| 30 | Max aggression: 5-day momentum | meta | 79.77 | -20.23 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 31 | Volume breakout · 1h | breakout | 79.69 | -20.31 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 32 | Donchian 55/20 · 1h | breakout | 79.55 | -20.45 | 77 | 13.0 | -25.31 | -6.66 | -29.99 | 85 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.54 | -23.46 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.52 | -23.48 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.19 | -24.81 | 2 | 0.0 | -16.06 | -2.25 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 74.84 | -25.16 | 101 | 14.9 | -29.06 | -8.54 | -29.95 | 112 |
| 38 | ADX DI cross · 1h | trend | 74.70 | -25.30 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Stochastic reversion · 1h | reversion | 73.29 | -26.71 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 40 | Bollinger breakout · 1h | breakout | 73.05 | -26.95 | 189 | 22.2 | -26.68 | -5.89 | -34.16 | 224 |
| 41 | Supertrend · 1h | trend | 72.30 | -27.70 | 189 | 15.9 | -31.60 | -5.32 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.48 | -28.52 | 155 | 14.8 | -32.11 | -6.50 | -38.00 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.04 | -28.96 | 176 | 14.2 | -31.32 | -5.72 | -37.63 | 199 |
| 44 | MFI reversion · 1h | reversion | 70.95 | -29.05 | 434 | 33.6 | -28.31 | -4.25 | -30.36 | 165 |
| 45 | MACD zero-line · 1h | trend | 70.38 | -29.62 | 181 | 17.7 | -27.33 | -5.48 | -33.53 | 203 |
| 46 | EMA 20/50 cross · 1h | trend | 69.91 | -30.09 | 115 | 10.4 | -36.21 | -10.16 | -39.23 | 115 |
| 47 | MACD cross · 1h | trend | 69.60 | -30.40 | 413 | 22.3 | -39.17 | -6.41 | -44.56 | 477 |
| 48 | Heikin-Ashi · 1h | trend | 69.44 | -30.56 | 470 | 23.0 | -43.46 | -9.30 | -45.14 | 638 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 50 | ROC + volume · 1h | momentum | 69.16 | -30.84 | 410 | 28.0 | -31.16 | -5.19 | -39.54 | 355 |
| 51 | OBV trend · 1h | momentum | 68.86 | -31.14 | 306 | 19.0 | -34.98 | -7.50 | -39.70 | 255 |
| 52 | Donchian 20/10 · 1h | breakout | 67.31 | -32.69 | 159 | 18.2 | -32.74 | -5.54 | -41.07 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.18 | -32.82 | 382 | 41.6 | -41.29 | -6.83 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 64.02 | -35.98 | 344 | 37.8 | -38.41 | -5.83 | -39.42 | 413 |
| 55 | EMA 9/21 cross · 1h | trend | 63.77 | -36.23 | 280 | 11.1 | -41.16 | -7.96 | -47.20 | 323 |
| 56 | Williams %R · 1h | reversion | 63.36 | -36.64 | 430 | 40.7 | -45.48 | -7.77 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.13 | -39.87 | 1906 | 24.3 | -26.63 | -5.30 | -27.33 | 314 |
| 58 | RSI(14) reversion · 1h | reversion | 58.50 | -41.50 | 205 | 31.7 | -41.06 | -6.10 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.37 | -42.63 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.94 | -43.06 | 962 | 21.9 | -53.05 | -9.43 | -58.63 | 1191 |
| 61 | Candlestick reversal · 1h | reversion | 55.43 | -44.57 | 547 | 26.7 | -46.59 | -8.48 | -48.43 | 642 |
| 62 | Three white soldiers | momentum | 55.07 | -44.93 | 585 | 14.5 | -49.55 | -21.31 | -50.37 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -42.52 | -99.03 | 5275 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.54 | -25.06 | -82.11 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.82 | -41.15 | -93.85 | 2461 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.09 | -31.43 | -90.26 | 1935 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -39.33 | -91.36 | 2289 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.65 | -30.84 | -89.68 | 2108 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -46.96 | -97.86 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.46 | -52.25 | -96.46 | 3398 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -39.21 | -93.52 | 2230 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.77 | -33.11 | -82.79 | 1596 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.41 | -99.60 | 6079 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.02 | -41.44 | -92.02 | 2560 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.87 | -39.01 | -94.87 | 3288 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.09 | -99.80 | 6184 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.44 | -41.81 | -92.45 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.48 | -25.65 | -76.51 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -58.06 | -97.65 | 3426 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -54.91 | -99.01 | 4952 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.78 | -26.90 | -68.95 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -53.97 | -94.62 | 2743 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.52 | -36.88 | -84.52 | 1719 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -66.55 | -99.70 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -30.36 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.51 | -18.69 | -79.91 | 1837 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.24 | -35.47 | -91.28 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -45.01 | -97.53 | 3908 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -56.66 | -89.42 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.34 | -29.32 | -66.55 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.67 | -22.68 | -72.62 | 1224 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.83 | -18.06 | -80.83 | 1732 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.32 | -97.57 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -98.65 | -99.94 | 8461 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T05:00 | VWAP momentum · 1h | buy | XRP-USD | 14.25 | — | entry signal |
| 2026-11-18T05:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.38 | — | entry signal |
| 2026-11-18T02:00 | ROC + volume · 1h | sell | XRP-USD | 17.28 | -0.03 | exit signal |
| 2026-11-18T02:00 | ROC + volume · 1h | sell | DOGE-USD | 17.18 | -0.15 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | XRP-USD | 13.89 | -0.02 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | SOL-USD | 13.84 | 0.07 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.28 | -0.12 | exit signal |
| 2026-11-18T02:00 | Heikin-Ashi · 1h | sell | BTC-USD | 7.54 | -0.08 | exit signal |
| 2026-11-18T02:00 | ADX DI cross · 1h | sell | ETH-USD | 18.44 | -0.32 | exit signal |
| 2026-11-18T01:50 | Heikin-Ashi · 1h | buy | BTC-USD | 3.49 | — | rebalance up |
| 2026-11-18T01:50 | Heikin-Ashi · 1h | sell | XRP-USD | 3.49 | 0.00 | rebalance down |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | XRP-USD | 6.38 | 0.05 | exit signal |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | SOL-USD | 6.47 | 0.15 | exit signal |
| 2026-11-18T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.37 | 0.05 | exit signal |
| 2026-11-18T01:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.13 | — | entry |
| 2026-11-18T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 3.68 | 0.05 | rebalance down |
| 2026-11-18T01:00 | Ichimoku · 1h | buy | XRP-USD | 18.79 | — | entry signal |
| 2026-11-18T01:00 | Ichimoku · 1h | buy | SOL-USD | 18.79 | — | entry signal |
| 2026-11-18T01:00 | Ichimoku · 1h | buy | DOGE-USD | 18.79 | — | entry signal |
| 2026-11-18T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 2.92 | — | entry |
| 2026-11-18T00:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.12 | 0.05 | exit signal |
| 2026-11-18T00:00 | Squeeze breakout · 1h | buy | SOL-USD | 21.76 | — | entry signal |
| 2026-11-18T00:00 | Squeeze breakout · 1h | buy | DOGE-USD | 21.76 | — | entry signal |
| 2026-11-18T00:00 | Keltner breakout · 1h | buy | SOL-USD | 20.18 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Bollinger breakout · 1h | buy | DOGE-USD | 18.41 | — | entry signal |
| 2026-11-18T00:00 | Donchian 55/20 · 1h | buy | XRP-USD | 19.95 | — | entry signal |
| 2026-11-18T00:00 | Donchian 55/20 · 1h | buy | SOL-USD | 19.95 | — | entry signal |
| 2026-11-18T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 16.08 | — | entry signal |
| 2026-11-18T00:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 16.94 | — | entry signal |
| 2026-11-18T00:00 | RSI momentum · 1h | buy | XRP-USD | 17.03 | — | entry signal |
| 2026-11-18T00:00 | RSI momentum · 1h | buy | DOGE-USD | 17.88 | — | entry signal |
| 2026-11-18T00:00 | ADX DI cross · 1h | buy | ETH-USD | 18.75 | — | entry signal |
| 2026-11-18T00:00 | Parabolic SAR · 1h | buy | BTC-USD | 20.39 | — | entry signal |
| 2026-11-17T23:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.63 | — | entry signal |
| 2026-11-17T23:00 | Triple EMA stack · 1h | buy | XRP-USD | 17.80 | — | entry signal |
| 2026-11-17T22:00 | OBV trend · 1h | buy | XRP-USD | 17.10 | — | entry signal |
| 2026-11-17T22:00 | ROC + volume · 1h | buy | XRP-USD | 17.31 | — | entry signal |
| 2026-11-17T22:00 | Heikin-Ashi · 1h | buy | XRP-USD | 17.40 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 05:05:05.000138+00:00 -> 2026-11-18 05:15:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 05:05:05.000138+00:00 -> 2026-11-18 05:15:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
