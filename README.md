# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T08:35:05.000133+00:00 · 75286 ticks

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

Today: 6837 decisions in 1368 calls, $0.0953 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T08:35 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-27T08:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T08:35 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.90 | 15.90 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.04 | 5.04 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.44 | 0.54 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.05 | -5.95 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.56 | -6.44 | 24 | 12.5 | -5.31 | -7.68 | -6.53 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.27 | -6.73 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.11 | -6.89 | 63 | 41.3 | -4.85 | -0.81 | -14.79 | 69 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -7.50 | -4.53 | -10.74 | 29 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.15 | -10.85 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.19 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.83 | -2.34 | -20.49 | 153 |
| 23 | Squeeze breakout · 1h | breakout | 83.17 | -16.83 | 79 | 20.3 | -19.16 | -6.46 | -19.46 | 82 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.96 | -20.04 | 224 | 41.1 | -13.12 | -5.98 | -13.43 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.09 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 77.05 | -22.95 | 174 | 29.3 | -22.02 | -8.59 | -22.48 | 72 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -26.83 | -5.95 | -27.37 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -16.90 | -4.53 | -17.30 | 91 |
| 30 | Parabolic SAR · 1h | trend | 75.43 | -24.57 | 216 | 27.8 | -34.42 | -8.19 | -35.47 | 188 |
| 31 | Donchian 55/20 · 1h | breakout | 74.81 | -25.19 | 88 | 13.6 | -28.95 | -7.45 | -29.32 | 77 |
| 32 | Ichimoku · 1h | trend | 74.41 | -25.59 | 114 | 15.8 | -27.62 | -6.72 | -29.63 | 100 |
| 33 | Max aggression: 5-day momentum | meta | 73.98 | -26.02 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 34 | Keltner breakout · 1h | breakout | 72.87 | -27.13 | 143 | 24.5 | -27.03 | -6.57 | -27.21 | 149 |
| 35 | Hold BTC | benchmark | 71.28 | -28.72 | 3 | 0.0 | -26.78 | -4.54 | -36.10 | 1 |
| 36 | Daily: Momentum burst | daily | 71.06 | -28.94 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 37 | ADX DI cross · 1h | trend | 69.99 | -30.01 | 272 | 19.9 | -37.09 | -6.85 | -38.08 | 289 |
| 38 | Bollinger breakout · 1h | breakout | 68.21 | -31.79 | 215 | 22.8 | -31.29 | -7.93 | -32.08 | 212 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.82 | -32.18 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.41 | -32.59 | 221 | 17.6 | -39.68 | -7.69 | -42.10 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.63 | -33.37 | 411 | 39.9 | -32.79 | -3.39 | -42.70 | 435 |
| 42 | OBV trend · 1h | momentum | 66.41 | -33.59 | 325 | 19.7 | -39.99 | -9.59 | -41.12 | 226 |
| 43 | EMA 20/50 cross · 1h | trend | 66.17 | -33.83 | 126 | 9.5 | -36.90 | -9.72 | -38.47 | 116 |
| 44 | Triple EMA stack · 1h | trend | 65.96 | -34.04 | 172 | 15.1 | -40.50 | -9.45 | -42.43 | 169 |
| 45 | RSI momentum · 1h | momentum | 63.65 | -36.35 | 203 | 14.8 | -41.84 | -8.85 | -43.57 | 192 |
| 46 | MACD zero-line · 1h | trend | 63.04 | -36.96 | 206 | 16.5 | -36.35 | -9.93 | -36.92 | 198 |
| 47 | MFI reversion · 1h | reversion | 62.65 | -37.35 | 520 | 32.7 | -32.63 | -4.78 | -37.91 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.49 | -38.51 | 183 | 17.5 | -40.58 | -8.75 | -42.90 | 201 |
| 49 | Heikin-Ashi · 1h | trend | 60.76 | -39.24 | 560 | 21.8 | -49.28 | -9.94 | -49.71 | 650 |
| 50 | ROC + volume · 1h | momentum | 60.70 | -39.30 | 472 | 26.9 | -39.86 | -7.61 | -40.93 | 340 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.93 | -41.06 | 314 | 12.1 | -43.87 | -9.71 | -46.18 | 328 |
| 53 | MACD cross · 1h | trend | 57.37 | -42.63 | 497 | 21.1 | -52.88 | -10.49 | -54.64 | 511 |
| 54 | Agent (ML meta-label) | meta | 56.24 | -43.76 | 2074 | 25.4 | -24.62 | -3.29 | -31.68 | 323 |
| 55 | CCI reversion · 1h | reversion | 52.58 | -47.42 | 467 | 38.3 | -52.25 | -8.64 | -55.31 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 406 | 36.5 | -40.65 | -4.90 | -45.50 | 428 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.78 | -8.94 | -58.60 | 684 |
| 58 | VWAP momentum · 1h | momentum | 50.68 | -49.32 | 1112 | 21.3 | -60.76 | -12.89 | -61.06 | 1195 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.92 | -9.15 | -59.57 | 603 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.16 | -43.86 | -99.18 | 5405 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.19 | -29.21 | -83.57 | 1424 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.11 | -42.82 | -94.15 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.86 | -28.11 | -90.25 | 1873 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.16 | -36.11 | -91.30 | 2216 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.62 | -26.05 | -88.64 | 1933 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.10 | -43.60 | -98.13 | 3402 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -46.86 | -96.81 | 3349 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -32.40 | -93.42 | 2119 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -33.92 | -81.98 | 1508 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -48.96 | -99.68 | 6263 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -35.69 | -92.70 | 2466 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.32 | -33.82 | -94.32 | 3147 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -57.08 | -99.80 | 6052 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.84 | -39.56 | -92.91 | 2248 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.92 | -18.07 | -51.40 | 654 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.06 | -22.89 | -78.18 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -51.84 | -97.66 | 3234 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -53.18 | -99.15 | 5101 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.49 | -22.97 | -69.92 | 1205 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -43.76 | -94.60 | 2661 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.38 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.26 | -32.63 | -84.27 | 1645 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -60.11 | -99.76 | 6505 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.48 | -29.58 | -91.72 | 2494 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.74 | -19.52 | -83.22 | 1973 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.36 | -30.72 | -91.71 | 2148 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.20 | -45.05 | -98.21 | 4036 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.22 | -43.07 | -90.43 | 2200 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.66 | -29.17 | -68.68 | 788 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.30 | -26.56 | -72.55 | 1153 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.33 | -18.38 | -84.73 | 1818 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -45.48 | -98.09 | 4394 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -87.85 | -99.94 | 8301 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.61 | -6.84 | -52.52 | 297 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T03:00 | ROC + volume · 1h | buy | DOGE-USD | 10.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 08:35:05.000133+00:00 -> 2026-11-27 08:45:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
