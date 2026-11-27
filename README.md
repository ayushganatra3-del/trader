# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T06:35:05.000132+00:00 · 75178 ticks

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

Today: 5220 decisions in 1044 calls, $0.0727 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T06:35 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-27T06:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T06:35 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.87 | 15.87 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.02 | 5.02 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.04 | -5.96 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.54 | -6.46 | 24 | 12.5 | -5.28 | -7.70 | -6.53 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.25 | -6.75 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.09 | -6.91 | 63 | 41.3 | -4.85 | -0.81 | -14.79 | 69 |
| 16 | Trend pullback · 1h | trend | 91.55 | -8.45 | 116 | 24.1 | -7.63 | -4.50 | -10.99 | 31 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.13 | -10.87 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.09 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.81 | -14.19 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.25 | -2.43 | -20.49 | 154 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.07 | -16.93 | 79 | 20.3 | -19.23 | -6.50 | -19.46 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 79.96 | -20.04 | 224 | 41.1 | -13.15 | -5.99 | -13.46 | 61 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.18 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 77.12 | -22.88 | 174 | 29.3 | -21.94 | -8.53 | -22.48 | 72 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -26.37 | -5.84 | -26.91 | 194 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -15.29 | -4.23 | -16.03 | 90 |
| 30 | Parabolic SAR · 1h | trend | 75.43 | -24.57 | 216 | 27.8 | -33.95 | -8.05 | -35.47 | 187 |
| 31 | Donchian 55/20 · 1h | breakout | 74.70 | -25.30 | 88 | 13.6 | -29.05 | -7.48 | -29.32 | 77 |
| 32 | Ichimoku · 1h | trend | 74.31 | -25.69 | 114 | 15.8 | -27.69 | -6.75 | -29.63 | 100 |
| 33 | Max aggression: 5-day momentum | meta | 73.96 | -26.04 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 34 | Keltner breakout · 1h | breakout | 72.81 | -27.19 | 143 | 24.5 | -27.11 | -6.59 | -27.16 | 149 |
| 35 | Hold BTC | benchmark | 71.29 | -28.71 | 3 | 0.0 | -26.78 | -4.54 | -36.10 | 1 |
| 36 | Daily: Momentum burst | daily | 71.06 | -28.95 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 37 | ADX DI cross · 1h | trend | 69.96 | -30.04 | 272 | 19.9 | -37.03 | -6.84 | -38.08 | 290 |
| 38 | Bollinger breakout · 1h | breakout | 68.13 | -31.87 | 215 | 22.8 | -31.39 | -7.97 | -32.11 | 212 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.80 | -32.20 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.36 | -32.64 | 221 | 17.6 | -39.70 | -7.70 | -42.10 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.62 | -33.38 | 411 | 39.9 | -32.79 | -3.38 | -42.70 | 435 |
| 42 | OBV trend · 1h | momentum | 66.39 | -33.61 | 325 | 19.7 | -40.15 | -9.61 | -41.34 | 226 |
| 43 | EMA 20/50 cross · 1h | trend | 66.14 | -33.86 | 126 | 9.5 | -36.06 | -9.50 | -37.60 | 115 |
| 44 | Triple EMA stack · 1h | trend | 65.87 | -34.13 | 172 | 15.1 | -40.82 | -9.47 | -42.69 | 170 |
| 45 | RSI momentum · 1h | momentum | 63.56 | -36.44 | 203 | 14.8 | -41.86 | -8.87 | -43.57 | 192 |
| 46 | MACD zero-line · 1h | trend | 63.03 | -36.97 | 206 | 16.5 | -36.56 | -10.01 | -36.92 | 199 |
| 47 | MFI reversion · 1h | reversion | 62.64 | -37.36 | 520 | 32.7 | -32.20 | -4.70 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.44 | -38.56 | 183 | 17.5 | -40.59 | -8.76 | -42.89 | 201 |
| 49 | Heikin-Ashi · 1h | trend | 60.75 | -39.25 | 559 | 21.6 | -49.28 | -9.94 | -49.71 | 650 |
| 50 | ROC + volume · 1h | momentum | 60.72 | -39.28 | 472 | 26.9 | -39.70 | -7.57 | -40.92 | 339 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.89 | -41.11 | 314 | 12.1 | -43.85 | -9.71 | -46.18 | 328 |
| 53 | MACD cross · 1h | trend | 57.35 | -42.65 | 497 | 21.1 | -53.04 | -10.54 | -54.79 | 512 |
| 54 | Agent (ML meta-label) | meta | 56.23 | -43.77 | 2074 | 25.4 | -23.03 | -2.99 | -30.51 | 312 |
| 55 | CCI reversion · 1h | reversion | 52.58 | -47.42 | 467 | 38.3 | -52.18 | -8.63 | -55.31 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 406 | 36.5 | -40.74 | -4.92 | -45.50 | 429 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.37 | -8.85 | -58.35 | 682 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.87 | -9.14 | -59.57 | 603 |
| 59 | VWAP momentum · 1h | momentum | 50.66 | -49.34 | 1112 | 21.3 | -60.54 | -12.98 | -60.84 | 1195 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -44.11 | -99.20 | 5412 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.21 | -29.37 | -83.57 | 1423 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.10 | -42.19 | -94.19 | 2397 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.00 | -28.31 | -90.39 | 1878 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.17 | -35.84 | -91.36 | 2218 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.61 | -25.87 | -88.72 | 1934 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.08 | -42.84 | -98.13 | 3397 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -46.57 | -96.84 | 3351 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.32 | -32.43 | -93.42 | 2112 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.91 | -33.65 | -81.96 | 1505 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -48.74 | -99.68 | 6268 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -35.45 | -92.79 | 2469 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.34 | -33.70 | -94.34 | 3150 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -55.99 | -99.80 | 6050 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.86 | -39.51 | -92.95 | 2251 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.21 | -18.64 | -51.40 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.11 | -22.88 | -78.27 | 1612 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -50.12 | -97.64 | 3225 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.15 | -53.05 | -99.15 | 5104 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.30 | -22.83 | -70.00 | 1203 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -43.43 | -94.62 | 2660 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.38 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.27 | -32.34 | -84.33 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -59.80 | -99.76 | 6507 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.49 | -29.59 | -91.73 | 2494 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.68 | -19.47 | -83.17 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.41 | -30.95 | -91.75 | 2151 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.19 | -44.88 | -98.21 | 4038 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.14 | -42.54 | -90.40 | 2196 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.31 | -28.74 | -68.33 | 786 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.46 | -26.30 | -72.82 | 1154 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.38 | -18.43 | -84.78 | 1821 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.07 | -45.29 | -98.08 | 4394 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -87.38 | -99.94 | 8300 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.21 | -6.74 | -52.52 | 289 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-27T03:00 | ROC + volume · 1h | buy | BTC-USD | 10.09 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 06:35:05.000132+00:00 -> 2026-11-27 06:45:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
