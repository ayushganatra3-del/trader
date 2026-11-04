# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T01:55:05.000122+00:00 · 46770 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 143, win rate 38.5%, fees £3.99, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 1380 decisions in 276 calls, $0.0194 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T01:55 | 4 / 1 / 0 | cash |  |
| Breezy | 2026-11-04T01:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T01:55 | 5 / 0 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.87 | 8.87 | 0 | — | 10.13 | 4.43 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.33 | -3.00 | -13.06 | 141 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.68 | -3.32 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.78 | 2.31 | -3.26 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.75 | -4.25 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 0.63 | 0.28 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.13 | -4.87 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.71 | -5.75 | -8.61 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.09 | -5.91 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -1.75 | -0.54 | -8.78 | 213 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Hold BTC | benchmark | 90.64 | -9.36 | 0 | — | -1.38 | -0.06 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 90.58 | -9.42 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.49 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.11 | -3.15 | -14.15 | 90 |
| 25 | Daily: Bullish score | daily | 88.41 | -11.59 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Copy: Insider buying | copy | 88.15 | -11.85 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 27 | Donchian 55/20 · 1h | breakout | 88.11 | -11.89 | 61 | 13.1 | -14.86 | -3.36 | -18.06 | 100 |
| 28 | Parabolic SAR · 1h | trend | 87.73 | -12.27 | 153 | 26.8 | -15.46 | -3.60 | -18.00 | 236 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.26 | -13.74 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.35 | -14.65 | 15 | 40.0 | -29.00 | -1.90 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -15.32 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.55 | -15.45 | 242 | 47.1 | -23.25 | -4.67 | -25.31 | 387 |
| 34 | MFI reversion · 1h | reversion | 84.03 | -15.97 | 310 | 33.9 | -15.59 | -2.47 | -17.89 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.00 | -16.00 | 90 | 23.3 | -21.37 | -4.48 | -22.20 | 164 |
| 36 | Connors RSI(2) · 1h | reversion | 83.87 | -16.13 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 37 | ADX DI cross · 1h | trend | 82.66 | -17.34 | 153 | 17.6 | -19.80 | -3.83 | -22.27 | 256 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 39 | Ichimoku · 1h | trend | 81.28 | -18.72 | 84 | 13.1 | -17.75 | -3.59 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 80.65 | -19.35 | 145 | 24.1 | -18.45 | -3.76 | -23.80 | 231 |
| 41 | EMA 20/50 cross · 1h | trend | 79.02 | -20.98 | 91 | 11.0 | -18.51 | -3.30 | -27.05 | 130 |
| 42 | CCI reversion · 1h | reversion | 78.82 | -21.18 | 268 | 44.8 | -24.99 | -3.86 | -27.71 | 450 |
| 43 | Bollinger reversion · 1h | reversion | 78.13 | -21.87 | 226 | 38.9 | -27.19 | -5.32 | -29.70 | 375 |
| 44 | Z-score reversion · 1h | reversion | 77.29 | -22.71 | 142 | 34.5 | -14.60 | -2.13 | -23.02 | 218 |
| 45 | Supertrend · 1h | trend | 77.17 | -22.83 | 141 | 12.8 | -30.23 | -5.52 | -31.63 | 218 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.80 | -4.36 | -33.56 | 33 |
| 47 | MACD zero-line · 1h | trend | 76.67 | -23.33 | 141 | 15.6 | -26.40 | -5.91 | -28.29 | 213 |
| 48 | Williams %R · 1h | reversion | 76.55 | -23.45 | 279 | 46.6 | -36.31 | -6.54 | -37.32 | 525 |
| 49 | MACD cross · 1h | trend | 76.53 | -23.47 | 303 | 23.4 | -32.29 | -6.29 | -34.56 | 484 |
| 50 | RSI momentum · 1h | momentum | 75.60 | -24.40 | 139 | 12.2 | -29.06 | -5.63 | -30.93 | 215 |
| 51 | Heikin-Ashi · 1h | trend | 75.52 | -24.48 | 370 | 22.7 | -42.74 | -9.67 | -43.46 | 662 |
| 52 | Triple EMA stack · 1h | trend | 75.50 | -24.50 | 130 | 13.8 | -28.42 | -5.53 | -32.09 | 203 |
| 53 | OBV trend · 1h | momentum | 74.76 | -25.25 | 245 | 17.1 | -30.30 | -6.50 | -32.23 | 293 |
| 54 | Donchian 20/10 · 1h | breakout | 74.47 | -25.53 | 123 | 19.5 | -27.58 | -5.02 | -30.98 | 203 |
| 55 | ROC + volume · 1h | momentum | 72.88 | -27.12 | 313 | 25.2 | -35.79 | -7.05 | -36.42 | 373 |
| 56 | RSI(14) reversion · 1h | reversion | 72.79 | -27.21 | 130 | 26.2 | -21.02 | -3.96 | -26.28 | 195 |
| 57 | Candlestick reversal · 1h | reversion | 70.66 | -29.34 | 361 | 28.5 | -33.81 | -6.42 | -36.96 | 537 |
| 58 | Agent (ML meta-label) | meta | 69.72 | -30.27 | 1372 | 21.8 | -12.47 | -2.45 | -15.89 | 283 |
| 59 | Max aggression: 1-day momentum | meta | 68.76 | -31.23 | 23 | 30.4 | -32.21 | -1.80 | -50.32 | 42 |
| 60 | Three white soldiers | momentum | 68.41 | -31.59 | 423 | 15.8 | -46.74 | -21.43 | -46.82 | 623 |
| 61 | EMA 9/21 cross · 1h | trend | 68.36 | -31.64 | 221 | 9.5 | -38.28 | -7.81 | -39.89 | 329 |
| 62 | VWAP momentum · 1h | momentum | 68.08 | -31.92 | 716 | 21.9 | -56.40 | -12.11 | -56.42 | 1225 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.52 | -98.96 | 5161 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.61 | -23.00 | -80.56 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.30 | -41.84 | -93.52 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.71 | -29.20 | -89.17 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.89 | -34.63 | -91.20 | 2313 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.94 | -32.00 | -90.95 | 2222 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.13 | -97.75 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -52.22 | -96.32 | 3370 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -32.65 | -93.74 | 2428 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.69 | -33.45 | -82.24 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.14 | -99.49 | 5892 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.85 | -40.61 | -93.07 | 2612 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.48 | -37.69 | -95.48 | 3381 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.44 | -99.80 | 6185 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -43.14 | -91.84 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.38 | -25.68 | -75.04 | 1546 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -56.74 | -97.79 | 3513 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.71 | -61.46 | -98.71 | 4830 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.47 | -28.07 | -70.45 | 1205 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -49.14 | -94.79 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.46 | -35.04 | -84.96 | 1784 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.45 | -99.63 | 6322 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.33 | -30.56 | -88.36 | 2246 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.80 | -19.20 | -76.88 | 1702 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.45 | -36.80 | -90.47 | 2247 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.54 | -51.88 | -96.55 | 3830 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -53.40 | -89.52 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.16 | -26.92 | -65.71 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.28 | -23.83 | -74.29 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.94 | -18.83 | -77.15 | 1607 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.95 | -51.93 | -96.95 | 4248 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -90.09 | -99.92 | 8193 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T01:35 | EMA 9/21 cross · 1h | buy | ETH-USD | 4.77 | — | rebalance up |
| 2026-11-04T01:35 | EMA 9/21 cross · 1h | sell | DOGE-USD | 6.77 | -0.16 | stop-loss |
| 2026-11-04T01:00 | OBV trend · 1h | sell | XRP-USD | 18.70 | -0.08 | exit signal |
| 2026-11-04T01:00 | VWAP momentum · 1h | sell | XRP-USD | 4.82 | -0.00 | exit signal |
| 2026-11-04T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 4.84 | -0.00 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | SOL-USD | 9.15 | -0.13 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | DOGE-USD | 9.15 | -0.05 | exit signal |
| 2026-11-04T01:00 | ADX DI cross · 1h | sell | BTC-USD | 9.19 | -0.09 | exit signal |
| 2026-11-04T01:00 | Parabolic SAR · 1h | sell | XRP-USD | 21.75 | -0.38 | exit signal |
| 2026-11-04T01:00 | MACD zero-line · 1h | sell | XRP-USD | 19.19 | -0.02 | exit signal |
| 2026-11-04T01:00 | MACD zero-line · 1h | sell | ETH-USD | 19.22 | -0.20 | exit signal |
| 2026-11-04T01:00 | MACD cross · 1h | sell | XRP-USD | 4.45 | -0.10 | exit signal |
| 2026-11-04T01:00 | MACD cross · 1h | sell | ETH-USD | 4.49 | -0.07 | exit signal |
| 2026-11-04T00:35 | OBV trend · 1h | buy | XRP-USD | 3.77 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | buy | ETH-USD | 3.78 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | buy | BTC-USD | 3.80 | — | rebalance up |
| 2026-11-04T00:35 | RSI momentum · 1h | sell | DOGE-USD | 12.55 | -0.26 | stop-loss |
| 2026-11-04T00:35 | ROC + volume · 1h | sell | BTC-USD | 18.15 | -0.23 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | buy | XRP-USD | 3.89 | — | rebalance up |
| 2026-11-04T00:35 | MACD zero-line · 1h | buy | ETH-USD | 3.85 | — | rebalance up |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | SOL-USD | 11.43 | -0.30 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | DOGE-USD | 12.74 | -0.26 | stop-loss |
| 2026-11-04T00:35 | MACD zero-line · 1h | sell | BTC-USD | 15.34 | -0.26 | stop-loss |
| 2026-11-04T00:35 | EMA 9/21 cross · 1h | sell | SOL-USD | 9.64 | -0.21 | stop-loss |
| 2026-11-04T00:25 | Bollinger breakout · 1h | sell | DOGE-USD | 16.08 | -0.25 | stop-loss |
| 2026-11-04T00:25 | Donchian 55/20 · 1h | sell | XRP-USD | 21.88 | -0.47 | stop-loss |
| 2026-11-04T00:25 | Donchian 20/10 · 1h | sell | XRP-USD | 18.17 | -0.39 | stop-loss |
| 2026-11-04T00:25 | Donchian 20/10 · 1h | sell | SOL-USD | 18.45 | -0.38 | stop-loss |
| 2026-11-04T00:25 | OBV trend · 1h | sell | DOGE-USD | 14.79 | -0.24 | stop-loss |
| 2026-11-04T00:25 | RSI momentum · 1h | buy | ETH-USD | 5.58 | — | rebalance up |
| 2026-11-04T00:25 | RSI momentum · 1h | buy | BTC-USD | 4.36 | — | rebalance up |
| 2026-11-04T00:25 | RSI momentum · 1h | sell | XRP-USD | 11.99 | -0.25 | stop-loss |
| 2026-11-04T00:25 | RSI momentum · 1h | sell | SOL-USD | 8.16 | -0.15 | stop-loss |
| 2026-11-04T00:25 | ROC + volume · 1h | buy | BTC-USD | 6.10 | — | rebalance up |
| 2026-11-04T00:25 | ROC + volume · 1h | sell | XRP-USD | 12.12 | -0.24 | stop-loss |
| 2026-11-04T00:25 | ROC + volume · 1h | sell | SOL-USD | 12.07 | -0.28 | stop-loss |
| 2026-11-04T00:25 | ROC + volume · 1h | sell | ETH-USD | 12.15 | -0.20 | stop-loss |
| 2026-11-04T00:25 | ROC + volume · 1h | sell | DOGE-USD | 12.16 | -0.18 | stop-loss |
| 2026-11-04T00:25 | Triple EMA stack · 1h | sell | XRP-USD | 18.75 | -0.39 | stop-loss |
| 2026-11-04T00:25 | Triple EMA stack · 1h | sell | ETH-USD | 18.31 | -0.36 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 01:55:05.000122+00:00 -> 2026-11-04 02:05:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 01:55:05.000122+00:00 -> 2026-11-04 02:05:05.000122+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 01:55:05.000122+00:00 -> 2026-11-04 02:05:05.000122+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
