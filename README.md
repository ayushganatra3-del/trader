# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-27T13:05:05.000141+00:00 · 75520 ticks

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

Today: 10347 decisions in 2070 calls, $0.1443 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-27T13:05 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-27T13:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-27T13:05 | 4 / 1 / 0 | ETH-USD 56% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.83 | 15.83 | 0 | — | 14.88 | 4.95 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.10 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.98 | 4.98 | 0 | — | 6.08 | 1.60 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.06 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.23 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.00 | -6.00 | 0 | — | -6.75 | -1.71 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.52 | -6.48 | 24 | 12.5 | -5.31 | -7.71 | -6.56 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.22 | -6.78 | 0 | — | -7.99 | -1.59 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.05 | -6.95 | 63 | 41.3 | -4.85 | -0.81 | -14.79 | 69 |
| 16 | Trend pullback · 1h | trend | 91.54 | -8.46 | 116 | 24.1 | -7.76 | -4.59 | -10.99 | 30 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.52 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.10 | -10.90 | 0 | — | -12.17 | -2.61 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.14 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.09 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.80 | -14.20 | 20 | 20.0 | -13.31 | -2.92 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.83 | -2.34 | -20.49 | 153 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.04 | -16.96 | 79 | 20.3 | -18.84 | -6.34 | -19.10 | 81 |
| 25 | Connors RSI(2) · 1h | reversion | 79.96 | -20.04 | 224 | 41.1 | -13.06 | -5.95 | -13.42 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.18 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.98 | -23.02 | 175 | 29.1 | -21.61 | -8.43 | -22.03 | 71 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -26.37 | -5.84 | -26.91 | 194 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -15.29 | -4.23 | -16.03 | 90 |
| 30 | Parabolic SAR · 1h | trend | 75.41 | -24.59 | 216 | 27.8 | -33.66 | -7.98 | -35.47 | 186 |
| 31 | Donchian 55/20 · 1h | breakout | 74.74 | -25.26 | 88 | 13.6 | -28.98 | -7.46 | -29.32 | 77 |
| 32 | Ichimoku · 1h | trend | 74.34 | -25.66 | 114 | 15.8 | -27.68 | -6.75 | -29.63 | 100 |
| 33 | Max aggression: 5-day momentum | meta | 73.93 | -26.07 | 27 | 37.0 | -54.97 | -2.81 | -67.33 | 22 |
| 34 | Keltner breakout · 1h | breakout | 72.83 | -27.17 | 143 | 24.5 | -26.50 | -6.42 | -26.65 | 147 |
| 35 | Daily: Momentum burst | daily | 71.05 | -28.95 | 31 | 16.1 | -33.19 | -4.51 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 71.02 | -28.98 | 3 | 0.0 | -26.94 | -4.59 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.96 | -30.04 | 272 | 19.9 | -37.51 | -6.94 | -38.46 | 292 |
| 38 | Bollinger breakout · 1h | breakout | 68.11 | -31.89 | 215 | 22.8 | -30.76 | -7.77 | -31.72 | 209 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.78 | -32.22 | 3 | 0.0 | -25.48 | -3.13 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.40 | -32.60 | 221 | 17.6 | -39.27 | -7.58 | -41.85 | 209 |
| 41 | Stochastic reversion · 1h | reversion | 66.60 | -33.40 | 411 | 39.9 | -32.79 | -3.38 | -42.70 | 435 |
| 42 | OBV trend · 1h | momentum | 66.37 | -33.63 | 325 | 19.7 | -40.26 | -9.55 | -41.46 | 226 |
| 43 | EMA 20/50 cross · 1h | trend | 66.18 | -33.82 | 126 | 9.5 | -36.37 | -9.48 | -37.93 | 116 |
| 44 | Triple EMA stack · 1h | trend | 65.88 | -34.12 | 172 | 15.1 | -40.61 | -9.48 | -42.49 | 169 |
| 45 | RSI momentum · 1h | momentum | 63.61 | -36.39 | 203 | 14.8 | -42.10 | -8.90 | -43.78 | 193 |
| 46 | MACD zero-line · 1h | trend | 63.01 | -36.99 | 206 | 16.5 | -36.39 | -9.93 | -36.92 | 198 |
| 47 | MFI reversion · 1h | reversion | 62.62 | -37.38 | 520 | 32.7 | -32.20 | -4.70 | -38.15 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.41 | -38.59 | 183 | 17.5 | -40.07 | -8.61 | -42.38 | 199 |
| 49 | Heikin-Ashi · 1h | trend | 60.74 | -39.26 | 563 | 22.0 | -49.13 | -9.90 | -49.54 | 648 |
| 50 | ROC + volume · 1h | momentum | 60.68 | -39.32 | 472 | 26.9 | -39.81 | -7.59 | -41.02 | 339 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.59 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.89 | -41.11 | 314 | 12.1 | -43.02 | -9.47 | -45.14 | 324 |
| 53 | MACD cross · 1h | trend | 57.32 | -42.68 | 498 | 21.1 | -52.64 | -10.40 | -54.47 | 510 |
| 54 | Agent (ML meta-label) | meta | 56.22 | -43.78 | 2074 | 25.4 | -24.00 | -3.12 | -31.11 | 315 |
| 55 | CCI reversion · 1h | reversion | 52.58 | -47.42 | 467 | 38.3 | -52.67 | -8.77 | -55.31 | 499 |
| 56 | Bollinger reversion · 1h | reversion | 52.20 | -47.80 | 406 | 36.5 | -40.65 | -4.90 | -45.50 | 428 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.30 | -8.85 | -58.35 | 682 |
| 58 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.94 | -9.16 | -59.57 | 603 |
| 59 | VWAP momentum · 1h | momentum | 50.64 | -49.36 | 1113 | 21.3 | -60.15 | -12.93 | -60.83 | 1189 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -43.93 | -99.16 | 5392 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.10 | -29.30 | -83.38 | 1418 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -42.53 | -94.08 | 2393 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.84 | -28.07 | -90.16 | 1869 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -35.81 | -91.23 | 2211 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.70 | -26.31 | -88.70 | 1935 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.09 | -43.52 | -98.10 | 3395 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -47.25 | -96.82 | 3349 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.29 | -32.65 | -93.29 | 2106 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.07 | -34.21 | -82.08 | 1510 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -49.21 | -99.68 | 6265 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -35.56 | -92.72 | 2465 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -34.24 | -94.35 | 3155 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -58.55 | -99.81 | 6057 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.80 | -39.20 | -92.88 | 2242 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.21 | -18.64 | -51.40 | 656 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.21 | -22.98 | -78.32 | 1613 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -51.96 | -97.66 | 3230 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -53.46 | -99.14 | 5098 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.78 | -23.19 | -69.98 | 1209 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -44.52 | -94.65 | 2665 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.75 | -6.46 | -51.25 | 287 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.35 | -32.93 | -84.36 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -60.12 | -99.76 | 6497 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.69 | -91.72 | 2497 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.67 | -19.46 | -83.15 | 1970 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.37 | -31.00 | -91.67 | 2145 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.18 | -45.13 | -98.20 | 4035 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.10 | -43.10 | -90.29 | 2191 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.41 | -28.89 | -68.43 | 787 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.38 | -26.33 | -72.57 | 1151 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.24 | -18.27 | -84.66 | 1817 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.06 | -45.35 | -98.07 | 4386 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -88.19 | -99.94 | 8296 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.21 | -6.74 | -52.52 | 289 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-27T13:00 | MACD cross · 1h | sell | ETH-USD | 2.71 | -0.02 | exit signal |
| 2026-11-27T12:00 | Volume breakout · 1h | sell | ETH-USD | 19.02 | -0.12 | exit signal |
| 2026-11-27T12:00 | VWAP momentum · 1h | sell | ETH-USD | 1.86 | -0.01 | exit signal |
| 2026-11-27T12:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.35 | 0.02 | exit signal |
| 2026-11-27T12:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.54 | 0.01 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-29 13:05:05.000141+00:00 -> 2026-11-27 13:15:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
