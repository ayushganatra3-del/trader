# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T06:35:05.000145+00:00 · 64115 ticks

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

Today: 5289 decisions in 1059 calls, $0.0740 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T06:35 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-18T06:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-18T06:35 | 1 / 3 / 1 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.87 | 16.87 | 0 | — | 14.89 | 5.37 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 3.01 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 16.87 | 3.44 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.44 | 3.44 | 0 | — | 5.76 | 1.26 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.49 | -3.51 | 8 | 50.0 | -3.91 | -0.08 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.60 | -4.40 | 0 | — | -3.89 | -1.30 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.05 | -5.95 | 198 | 30.3 | -4.26 | -1.51 | -8.84 | 149 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.61 | -5.91 | -6.03 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.40 | -7.60 | 0 | — | -8.38 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.76 | -9.24 | 153 | 46.4 | -11.59 | -3.41 | -18.48 | 149 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.53 | -9.47 | 0 | — | -8.30 | -2.26 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -13.38 | -7.28 | -13.38 | 58 |
| 20 | Copy: Insider buying | copy | 90.17 | -9.83 | 50 | 42.0 | -9.31 | -1.86 | -14.79 | 62 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.16 | -12.84 | 17 | 17.6 | -4.97 | -0.80 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.61 | -13.39 | 68 | 20.6 | -16.65 | -6.98 | -19.74 | 77 |
| 24 | Opening range 30m | breakout | 86.38 | -13.62 | 439 | 33.7 | -9.03 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.21 | -7.35 | -16.95 | 199 |
| 26 | Parabolic SAR · 1h | trend | 82.11 | -17.89 | 184 | 27.7 | -25.27 | -7.06 | -28.05 | 203 |
| 27 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 28 | Keltner breakout · 1h | breakout | 80.64 | -19.36 | 122 | 26.2 | -20.44 | -4.87 | -27.13 | 153 |
| 29 | Connors RSI(2) · 1h | reversion | 80.44 | -19.56 | 215 | 40.0 | -14.39 | -6.40 | -14.66 | 90 |
| 30 | Max aggression: 5-day momentum | meta | 79.81 | -20.19 | 21 | 42.9 | -48.12 | -3.22 | -55.24 | 22 |
| 31 | Volume breakout · 1h | breakout | 79.70 | -20.30 | 162 | 28.4 | -15.91 | -5.00 | -22.20 | 78 |
| 32 | Donchian 55/20 · 1h | breakout | 79.70 | -20.30 | 77 | 13.0 | -24.69 | -6.46 | -29.99 | 84 |
| 33 | Opening range 15m | breakout | 78.30 | -21.70 | 534 | 31.6 | -16.06 | -4.36 | -21.37 | 680 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.58 | -23.42 | 2 | 0.0 | -18.43 | -2.47 | -26.43 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 76.56 | -23.44 | 30 | 26.7 | -24.46 | -0.95 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.56 | -24.44 | 2 | 0.0 | -15.71 | -2.18 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.06 | -24.94 | 101 | 14.9 | -28.88 | -8.47 | -29.95 | 112 |
| 38 | ADX DI cross · 1h | trend | 74.72 | -25.29 | 209 | 19.1 | -27.58 | -4.47 | -35.42 | 263 |
| 39 | Stochastic reversion · 1h | reversion | 73.33 | -26.67 | 345 | 42.6 | -34.28 | -5.22 | -36.02 | 424 |
| 40 | Bollinger breakout · 1h | breakout | 73.26 | -26.74 | 189 | 22.2 | -28.12 | -6.91 | -34.16 | 224 |
| 41 | Supertrend · 1h | trend | 72.52 | -27.48 | 189 | 15.9 | -31.43 | -5.28 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.62 | -28.38 | 155 | 14.8 | -31.97 | -6.45 | -38.00 | 183 |
| 43 | RSI momentum · 1h | momentum | 71.25 | -28.75 | 176 | 14.2 | -31.15 | -5.68 | -37.63 | 199 |
| 44 | MFI reversion · 1h | reversion | 71.02 | -28.98 | 434 | 33.6 | -28.27 | -4.24 | -30.36 | 165 |
| 45 | MACD zero-line · 1h | trend | 70.45 | -29.55 | 181 | 17.7 | -27.27 | -5.47 | -33.53 | 203 |
| 46 | EMA 20/50 cross · 1h | trend | 70.04 | -29.96 | 115 | 10.4 | -36.11 | -10.12 | -39.23 | 115 |
| 47 | MACD cross · 1h | trend | 69.65 | -30.35 | 413 | 22.3 | -39.03 | -6.38 | -44.56 | 477 |
| 48 | Heikin-Ashi · 1h | trend | 69.46 | -30.54 | 470 | 23.0 | -43.46 | -9.30 | -45.15 | 638 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 50 | ROC + volume · 1h | momentum | 69.17 | -30.83 | 410 | 28.0 | -31.16 | -5.19 | -39.54 | 355 |
| 51 | OBV trend · 1h | momentum | 69.00 | -31.00 | 306 | 19.0 | -34.84 | -7.46 | -39.70 | 255 |
| 52 | Donchian 20/10 · 1h | breakout | 67.51 | -32.49 | 159 | 18.2 | -32.92 | -5.65 | -41.07 | 203 |
| 53 | CCI reversion · 1h | reversion | 67.21 | -32.78 | 382 | 41.6 | -41.25 | -6.82 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 64.06 | -35.94 | 344 | 37.8 | -38.41 | -5.83 | -39.42 | 413 |
| 55 | EMA 9/21 cross · 1h | trend | 63.96 | -36.04 | 280 | 11.1 | -41.02 | -7.92 | -47.20 | 323 |
| 56 | Williams %R · 1h | reversion | 63.40 | -36.60 | 430 | 40.7 | -45.47 | -7.76 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 60.14 | -39.86 | 1906 | 24.3 | -22.11 | -4.25 | -22.26 | 308 |
| 58 | RSI(14) reversion · 1h | reversion | 58.53 | -41.47 | 205 | 31.7 | -41.06 | -6.10 | -43.29 | 251 |
| 59 | Z-score reversion · 1h | reversion | 57.40 | -42.60 | 224 | 35.3 | -37.41 | -5.22 | -39.23 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.99 | -43.01 | 962 | 21.9 | -53.11 | -9.45 | -58.63 | 1195 |
| 61 | Candlestick reversal · 1h | reversion | 55.47 | -44.53 | 547 | 26.7 | -46.60 | -8.48 | -48.43 | 642 |
| 62 | Three white soldiers | momentum | 54.97 | -45.03 | 586 | 14.5 | -49.64 | -21.43 | -50.46 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -42.66 | -99.03 | 5277 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.58 | -25.11 | -82.11 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -41.36 | -93.78 | 2459 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.09 | -31.40 | -90.26 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -39.49 | -91.36 | 2291 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.66 | -30.93 | -89.70 | 2110 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -47.07 | -97.87 | 3479 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -52.74 | -96.44 | 3397 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -39.99 | -93.53 | 2236 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.75 | -33.17 | -82.76 | 1596 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.40 | -99.60 | 6076 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.99 | -41.67 | -91.99 | 2559 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.87 | -39.14 | -94.87 | 3290 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.03 | -99.80 | 6185 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -42.34 | -92.48 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.41 | -25.72 | -76.41 | 1640 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -58.70 | -97.66 | 3430 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -54.89 | -99.01 | 4953 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.29 | -68.94 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -54.80 | -94.62 | 2744 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.49 | -37.04 | -84.49 | 1719 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -66.35 | -99.69 | 6373 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.74 | -30.36 | -90.89 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.50 | -18.69 | -79.91 | 1835 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.22 | -35.33 | -91.28 | 2166 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -45.01 | -97.53 | 3908 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -56.66 | -89.42 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.38 | -29.56 | -66.66 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.78 | -22.79 | -72.62 | 1226 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.86 | -18.04 | -80.89 | 1735 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -45.32 | -97.57 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -101.31 | -99.94 | 8457 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T06:01 | VWAP momentum · 1h | buy | DOGE-USD | 4.98 | — | entry signal |
| 2026-11-18T06:01 | VWAP momentum · 1h | buy | BTC-USD | 7.13 | — | entry signal |
| 2026-11-18T06:01 | VWAP momentum · 1h | sell | XRP-USD | 7.13 | -0.01 | rebalance down |
| 2026-11-18T05:50 | MFI reversion · 1h | buy | BTC-USD | 3.88 | — | rebalance up |
| 2026-11-18T05:50 | Three white soldiers | sell | BTC-USD | 13.67 | -0.10 | exit signal |
| 2026-11-18T05:20 | Three white soldiers | buy | BTC-USD | 13.77 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 06:35:05.000145+00:00 -> 2026-11-18 06:45:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 06:35:05.000145+00:00 -> 2026-11-18 06:45:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
