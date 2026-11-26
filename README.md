# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T21:35:05.000121+00:00 · 74698 ticks

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
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 26.80 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 16077 decisions in 3216 calls, $0.2243 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T21:35 | 3 / 2 / 0 | SOL-USD 20%, BTC-USD 17% |  |
| Breezy | 2026-11-26T21:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T21:35 | 3 / 2 / 0 | ETH-USD 75% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 123.12 | 23.12 | 28 | 64.3 | 24.53 | 3.63 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.04 | 16.04 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.17 | 5.17 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.17 | -5.83 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.64 | -6.36 | 24 | 12.5 | -5.27 | -7.76 | -6.56 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.39 | -6.61 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.22 | -6.78 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.59 | -8.41 | 116 | 24.1 | -7.33 | -4.45 | -10.74 | 31 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.26 | -10.74 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.84 | -14.16 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.02 | -2.40 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.08 | -16.92 | 79 | 20.3 | -19.54 | -6.66 | -19.77 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.17 | -6.06 | -13.42 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.83 | -23.16 | 174 | 29.3 | -22.18 | -8.79 | -22.46 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.52 | -24.48 | 212 | 28.3 | -34.50 | -8.35 | -35.15 | 183 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.07 | -25.93 | 27 | 37.0 | -54.97 | -2.83 | -67.33 | 22 |
| 33 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 34 | Keltner breakout · 1h | breakout | 72.97 | -27.03 | 143 | 24.5 | -26.99 | -6.61 | -26.99 | 145 |
| 35 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.46 | -29.54 | 3 | 0.0 | -27.78 | -4.84 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.11 | -29.89 | 268 | 19.8 | -36.72 | -6.82 | -38.08 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.13 | -31.87 | 213 | 22.5 | -31.25 | -8.04 | -31.87 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.90 | -32.10 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.14 | -32.86 | 221 | 17.6 | -40.09 | -7.90 | -42.10 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.71 | -33.29 | 411 | 39.9 | -32.76 | -3.41 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.49 | -33.51 | 325 | 19.7 | -40.61 | -9.98 | -41.33 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.96 | -34.04 | 126 | 9.5 | -37.28 | -10.12 | -38.15 | 117 |
| 44 | Triple EMA stack · 1h | trend | 65.15 | -34.85 | 172 | 15.1 | -41.17 | -10.10 | -42.22 | 169 |
| 45 | MACD zero-line · 1h | trend | 63.10 | -36.90 | 206 | 16.5 | -37.30 | -10.36 | -37.60 | 201 |
| 46 | RSI momentum · 1h | momentum | 63.04 | -36.96 | 203 | 14.8 | -42.79 | -9.30 | -43.78 | 193 |
| 47 | MFI reversion · 1h | reversion | 62.71 | -37.28 | 520 | 32.7 | -32.25 | -4.75 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.41 | -38.59 | 183 | 17.5 | -40.80 | -8.98 | -42.84 | 199 |
| 49 | Heikin-Ashi · 1h | trend | 60.78 | -39.22 | 555 | 21.8 | -49.39 | -10.08 | -49.85 | 645 |
| 50 | ROC + volume · 1h | momentum | 60.52 | -39.48 | 472 | 26.9 | -40.35 | -7.83 | -41.14 | 335 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.63 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.51 | -41.49 | 314 | 12.1 | -44.61 | -10.08 | -46.12 | 329 |
| 53 | MACD cross · 1h | trend | 57.33 | -42.67 | 497 | 21.1 | -53.58 | -10.81 | -55.26 | 509 |
| 54 | Agent (ML meta-label) | meta | 56.27 | -43.73 | 2074 | 25.4 | -23.01 | -3.06 | -30.07 | 326 |
| 55 | CCI reversion · 1h | reversion | 52.54 | -47.46 | 463 | 37.8 | -52.31 | -8.75 | -55.31 | 500 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.86 | -4.98 | -45.49 | 431 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.08 | -8.88 | -58.27 | 680 |
| 58 | VWAP momentum · 1h | momentum | 50.76 | -49.24 | 1107 | 21.4 | -60.94 | -13.32 | -61.28 | 1194 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.10 | -9.30 | -59.57 | 605 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -47.66 | -99.18 | 5401 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.50 | -31.76 | -83.74 | 1424 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.18 | -46.00 | -94.21 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.31 | -30.35 | -90.60 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.49 | -39.81 | -91.52 | 2222 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.77 | -27.23 | -88.77 | 1933 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.16 | -47.41 | -98.16 | 3407 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -50.90 | -96.88 | 3353 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.34 | -34.74 | -93.34 | 2104 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.80 | -34.57 | -81.82 | 1503 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -51.59 | -99.68 | 6276 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -36.99 | -92.89 | 2467 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.30 | -34.91 | -94.30 | 3143 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -63.08 | -99.81 | 6070 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.03 | -42.57 | -93.04 | 2257 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.15 | -18.76 | -51.37 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.93 | -23.16 | -78.04 | 1603 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -55.87 | -97.70 | 3232 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.18 | -99.17 | 5112 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.89 | -22.63 | -69.94 | 1196 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -46.75 | -94.64 | 2655 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.44 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.42 | -34.38 | -84.43 | 1643 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -65.36 | -99.77 | 6512 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.47 | -30.25 | -91.80 | 2493 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.76 | -19.80 | -83.34 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.45 | -31.58 | -91.83 | 2153 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -47.08 | -98.23 | 4049 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.37 | -46.29 | -90.45 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.96 | -28.98 | -67.98 | 779 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.60 | -27.49 | -72.60 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.60 | -18.95 | -85.00 | 1827 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.08 | -47.72 | -98.11 | 4398 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.86 | -99.94 | 8293 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.42 | -6.86 | -52.52 | 288 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T21:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.53 | — | entry signal |
| 2026-11-26T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.52 | -0.02 | exit signal |
| 2026-11-26T20:00 | Bollinger breakout · 1h | buy | DOGE-USD | 17.02 | — | entry signal |
| 2026-11-26T20:00 | VWAP momentum · 1h | buy | BTC-USD | 1.88 | — | entry signal |
| 2026-11-26T20:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.53 | — | entry signal |
| 2026-11-26T20:00 | Heikin-Ashi · 1h | buy | SOL-USD | 2.53 | — | entry signal |
| 2026-11-26T20:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.53 | — | entry signal |
| 2026-11-26T20:00 | ADX DI cross · 1h | buy | ETH-USD | 3.71 | — | entry signal |
| 2026-11-26T20:00 | ADX DI cross · 1h | sell | DOGE-USD | 3.71 | 0.05 | rebalance down |
| 2026-11-26T19:00 | VWAP momentum · 1h | buy | ETH-USD | 1.95 | — | entry signal |
| 2026-11-26T19:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.95 | — | entry signal |
| 2026-11-26T19:00 | ADX DI cross · 1h | buy | SOL-USD | 6.12 | — | entry signal |
| 2026-11-26T19:00 | ADX DI cross · 1h | buy | BTC-USD | 7.00 | — | entry signal |
| 2026-11-26T19:00 | Parabolic SAR · 1h | buy | SOL-USD | 12.58 | — | entry signal |
| 2026-11-26T18:00 | VWAP momentum · 1h | buy | XRP-USD | 2.11 | — | entry signal |
| 2026-11-26T17:00 | CCI reversion · 1h | buy | ETH-USD | 4.04 | — | entry signal |
| 2026-11-26T17:00 | ADX DI cross · 1h | buy | XRP-USD | 8.75 | — | entry signal |
| 2026-11-26T16:00 | Bollinger breakout · 1h | sell | BTC-USD | 17.07 | -0.03 | exit signal |
| 2026-11-26T16:00 | ROC + volume · 1h | sell | BTC-USD | 15.16 | -0.00 | exit signal |
| 2026-11-26T16:00 | VWAP momentum · 1h | buy | SOL-USD | 2.21 | — | entry signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | buy | DOGE-USD | 3.59 | — | rebalance up |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | XRP-USD | 6.38 | 0.12 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | SOL-USD | 6.36 | 0.03 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | ETH-USD | 6.34 | -0.00 | exit signal |
| 2026-11-26T16:00 | ADX DI cross · 1h | sell | BTC-USD | 6.39 | 0.05 | exit signal |
| 2026-11-26T16:00 | Parabolic SAR · 1h | sell | DOGE-USD | 9.62 | 0.23 | exit signal |
| 2026-11-26T16:00 | MACD zero-line · 1h | sell | ETH-USD | 15.67 | -0.13 | exit signal |
| 2026-11-26T16:00 | MACD cross · 1h | sell | ETH-USD | 4.07 | 0.07 | exit signal |
| 2026-11-26T15:55 | ROC + volume · 1h | sell | DOGE-USD | 15.10 | -0.04 | target is flat |
| 2026-11-26T15:55 | VWAP momentum · 1h | sell | DOGE-USD | 2.20 | -0.01 | target is flat |
| 2026-11-26T15:50 | ROC + volume · 1h | buy | DOGE-USD | 15.15 | — | entry |
| 2026-11-26T15:50 | VWAP momentum · 1h | buy | DOGE-USD | 2.21 | — | entry |
| 2026-11-26T15:35 | ROC + volume · 1h | sell | DOGE-USD | 15.08 | -0.07 | target is flat |
| 2026-11-26T15:35 | VWAP momentum · 1h | sell | DOGE-USD | 2.20 | -0.01 | target is flat |
| 2026-11-26T15:30 | ROC + volume · 1h | buy | DOGE-USD | 15.15 | — | entry |
| 2026-11-26T15:30 | VWAP momentum · 1h | buy | DOGE-USD | 2.21 | — | entry |
| 2026-11-26T15:10 | Squeeze breakout · 1h | sell | ETH-USD | 20.58 | -0.22 | stop-loss |
| 2026-11-26T15:10 | Keltner breakout · 1h | sell | DOGE-USD | 18.08 | -0.31 | stop-loss |
| 2026-11-26T15:10 | Bollinger breakout · 1h | sell | ETH-USD | 16.87 | -0.21 | stop-loss |
| 2026-11-26T15:10 | Bollinger breakout · 1h | sell | DOGE-USD | 13.58 | -0.02 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 21:35:05.000121+00:00 -> 2026-11-26 21:45:05.000121+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
