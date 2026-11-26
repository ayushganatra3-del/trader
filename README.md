# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T22:05:05.000154+00:00 · 74722 ticks

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

Today: 16437 decisions in 3288 calls, $0.2293 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T22:05 | 1 / 0 / 4 | cash |  |
| Breezy | 2026-11-26T22:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T22:05 | 1 / 4 / 0 | cash |  |

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
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | 0.39 | 0.21 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.44 | 0.54 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.16 | -5.84 | 0 | — | -6.75 | -1.73 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.64 | -6.36 | 24 | 12.5 | -5.32 | -7.73 | -6.57 | 25 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.39 | -6.61 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.22 | -6.78 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.59 | -8.41 | 116 | 24.1 | -6.53 | -4.26 | -9.96 | 29 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.26 | -10.74 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.29 | -3.14 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.84 | -14.16 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -13.02 | -2.40 | -20.49 | 155 |
| 23 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 24 | Squeeze breakout · 1h | breakout | 83.08 | -16.92 | 79 | 20.3 | -19.71 | -6.71 | -19.85 | 79 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.17 | -6.06 | -13.42 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.41 | -5.13 | -23.63 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.83 | -23.16 | 174 | 29.3 | -22.21 | -8.80 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.39 | -24.61 | 212 | 28.3 | -34.62 | -8.40 | -35.15 | 184 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.07 | -25.93 | 27 | 37.0 | -54.97 | -2.83 | -67.33 | 22 |
| 33 | Ichimoku · 1h | trend | 73.32 | -26.68 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 34 | Keltner breakout · 1h | breakout | 72.97 | -27.03 | 143 | 24.5 | -27.07 | -6.63 | -27.07 | 145 |
| 35 | Daily: Momentum burst | daily | 71.08 | -28.92 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.12 | -29.88 | 3 | 0.0 | -28.13 | -4.92 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 69.96 | -30.04 | 268 | 19.8 | -37.23 | -6.95 | -38.13 | 290 |
| 38 | Bollinger breakout · 1h | breakout | 67.97 | -32.03 | 213 | 22.5 | -31.48 | -8.12 | -31.94 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.90 | -32.10 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.07 | -32.94 | 221 | 17.6 | -39.78 | -7.81 | -41.85 | 209 |
| 41 | Stochastic reversion · 1h | reversion | 66.70 | -33.30 | 411 | 39.9 | -32.91 | -3.43 | -42.70 | 437 |
| 42 | OBV trend · 1h | momentum | 66.49 | -33.51 | 325 | 19.7 | -40.74 | -10.05 | -41.29 | 223 |
| 43 | EMA 20/50 cross · 1h | trend | 65.89 | -34.11 | 126 | 9.5 | -37.99 | -10.34 | -38.68 | 117 |
| 44 | Triple EMA stack · 1h | trend | 64.92 | -35.08 | 172 | 15.1 | -41.13 | -10.16 | -41.95 | 168 |
| 45 | MACD zero-line · 1h | trend | 63.10 | -36.90 | 206 | 16.5 | -37.15 | -10.32 | -37.39 | 200 |
| 46 | RSI momentum · 1h | momentum | 62.88 | -37.12 | 203 | 14.8 | -42.77 | -9.36 | -43.57 | 192 |
| 47 | MFI reversion · 1h | reversion | 62.71 | -37.29 | 520 | 32.7 | -32.68 | -4.83 | -37.91 | 193 |
| 48 | Donchian 20/10 · 1h | breakout | 61.37 | -38.63 | 183 | 17.5 | -40.91 | -9.02 | -42.86 | 199 |
| 49 | Heikin-Ashi · 1h | trend | 60.73 | -39.27 | 556 | 21.8 | -49.43 | -10.10 | -49.85 | 646 |
| 50 | ROC + volume · 1h | momentum | 60.52 | -39.48 | 472 | 26.9 | -40.24 | -7.78 | -40.98 | 335 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.63 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.38 | -41.62 | 314 | 12.1 | -44.43 | -10.06 | -46.03 | 329 |
| 53 | MACD cross · 1h | trend | 57.33 | -42.67 | 497 | 21.1 | -52.78 | -10.55 | -54.55 | 506 |
| 54 | Agent (ML meta-label) | meta | 56.27 | -43.73 | 2074 | 25.4 | -18.77 | -2.40 | -25.91 | 320 |
| 55 | CCI reversion · 1h | reversion | 52.51 | -47.49 | 464 | 37.9 | -52.42 | -8.78 | -55.31 | 500 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.39 | -4.90 | -45.49 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -55.85 | -9.06 | -58.40 | 685 |
| 58 | VWAP momentum · 1h | momentum | 50.71 | -49.28 | 1107 | 21.4 | -61.19 | -13.25 | -61.49 | 1193 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -55.97 | -9.28 | -59.57 | 604 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.18 | -47.61 | -99.18 | 5405 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.51 | -31.74 | -83.66 | 1422 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.22 | -46.29 | -94.23 | 2396 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.39 | -30.45 | -90.61 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -39.73 | -91.53 | 2222 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.85 | -27.24 | -88.85 | 1934 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -47.51 | -98.17 | 3407 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.88 | -50.58 | -96.88 | 3348 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -34.12 | -93.45 | 2116 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -34.65 | -81.90 | 1503 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -51.49 | -99.68 | 6270 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.84 | -37.33 | -92.87 | 2467 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.31 | -34.90 | -94.31 | 3146 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -63.28 | -99.82 | 6071 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.07 | -42.64 | -93.08 | 2258 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -48.96 | -18.27 | -51.37 | 655 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -77.84 | -23.11 | -77.95 | 1602 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -55.94 | -97.69 | 3230 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -56.26 | -99.17 | 5111 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.16 | -22.75 | -70.01 | 1198 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -46.66 | -94.68 | 2655 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.44 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.47 | -34.36 | -84.48 | 1643 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -65.58 | -99.77 | 6513 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -30.24 | -91.79 | 2493 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.76 | -19.80 | -83.34 | 1971 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.42 | -31.42 | -91.79 | 2152 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -47.11 | -98.23 | 4049 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.36 | -46.21 | -90.44 | 2193 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.22 | -29.28 | -68.25 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.66 | -27.69 | -72.66 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.60 | -18.95 | -85.00 | 1827 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.08 | -47.73 | -98.11 | 4398 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.55 | -99.94 | 8294 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.42 | -7.10 | -52.52 | 294 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T22:00 | CCI reversion · 1h | sell | ETH-USD | 4.05 | 0.01 | exit signal |
| 2026-11-26T22:00 | Heikin-Ashi · 1h | buy | BTC-USD | 2.53 | — | entry signal |
| 2026-11-26T22:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.51 | -0.02 | exit signal |
| 2026-11-26T22:00 | Parabolic SAR · 1h | buy | ETH-USD | 10.78 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 22:05:05.000154+00:00 -> 2026-11-26 22:15:05.000154+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
