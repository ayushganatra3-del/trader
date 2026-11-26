# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T12:35:05.000125+00:00 · 74237 ticks

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

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 9162 decisions in 1833 calls, $0.1278 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T12:35 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-26T12:35 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T12:35 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 116.10 | 16.11 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.23 | 5.23 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.31 | 0.50 | -5.49 | 185 |
| 12 | Hold SPY | benchmark | 94.22 | -5.78 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.68 | -6.32 | 24 | 12.5 | -5.29 | -7.77 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.44 | -6.56 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.27 | -6.73 | 63 | 41.3 | -4.95 | -0.83 | -14.79 | 72 |
| 16 | Trend pullback · 1h | trend | 91.60 | -8.40 | 116 | 24.1 | -7.10 | -4.52 | -10.42 | 29 |
| 17 | Copy: Congress Democrats (NANC) | copy | 89.31 | -10.69 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.85 | -14.15 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.87 | -2.37 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.60 | -16.40 | 77 | 19.5 | -19.18 | -6.48 | -19.85 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.28 | -6.11 | -13.46 | 60 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.85 | -23.15 | 174 | 29.3 | -22.18 | -8.79 | -22.46 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.55 | -24.45 | 211 | 28.0 | -34.48 | -8.35 | -35.15 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 74.11 | -25.89 | 27 | 37.0 | -56.74 | -3.00 | -67.33 | 23 |
| 33 | Keltner breakout · 1h | breakout | 73.52 | -26.48 | 141 | 24.8 | -26.58 | -6.49 | -26.71 | 145 |
| 34 | Ichimoku · 1h | trend | 73.34 | -26.66 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 35 | Daily: Momentum burst | daily | 71.09 | -28.91 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | Hold BTC | benchmark | 70.15 | -29.85 | 3 | 0.0 | -28.13 | -4.92 | -36.10 | 1 |
| 37 | ADX DI cross · 1h | trend | 70.14 | -29.86 | 264 | 18.9 | -37.22 | -6.94 | -38.28 | 288 |
| 38 | Bollinger breakout · 1h | breakout | 68.69 | -31.31 | 209 | 22.5 | -30.91 | -7.88 | -31.80 | 207 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.94 | -32.06 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 67.03 | -32.97 | 221 | 17.6 | -40.27 | -7.96 | -42.12 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.74 | -33.26 | 411 | 39.9 | -32.92 | -3.43 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.53 | -33.47 | 325 | 19.7 | -40.77 | -10.13 | -40.92 | 224 |
| 43 | EMA 20/50 cross · 1h | trend | 65.92 | -34.09 | 126 | 9.5 | -38.01 | -10.38 | -38.32 | 117 |
| 44 | Triple EMA stack · 1h | trend | 64.87 | -35.13 | 172 | 15.1 | -41.03 | -10.19 | -41.22 | 168 |
| 45 | MACD zero-line · 1h | trend | 63.37 | -36.63 | 202 | 16.3 | -37.00 | -10.22 | -37.67 | 202 |
| 46 | RSI momentum · 1h | momentum | 62.81 | -37.19 | 203 | 14.8 | -43.03 | -9.46 | -43.61 | 193 |
| 47 | MFI reversion · 1h | reversion | 62.74 | -37.26 | 520 | 32.7 | -32.79 | -4.85 | -38.15 | 194 |
| 48 | Donchian 20/10 · 1h | breakout | 61.40 | -38.60 | 183 | 17.5 | -40.96 | -9.05 | -42.84 | 199 |
| 49 | ROC + volume · 1h | momentum | 61.06 | -38.94 | 465 | 26.7 | -40.13 | -7.75 | -41.16 | 335 |
| 50 | Heikin-Ashi · 1h | trend | 60.82 | -39.18 | 553 | 21.9 | -49.35 | -10.07 | -49.85 | 640 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.88 | -4.63 | -63.62 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 58.35 | -41.65 | 314 | 12.1 | -45.00 | -10.27 | -46.32 | 332 |
| 53 | MACD cross · 1h | trend | 57.43 | -42.58 | 493 | 20.5 | -54.04 | -10.90 | -55.75 | 514 |
| 54 | Agent (ML meta-label) | meta | 56.29 | -43.71 | 2074 | 25.4 | -22.15 | -2.96 | -29.57 | 332 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.13 | -8.97 | -55.52 | 502 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.77 | -4.96 | -45.50 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.33 | -9.22 | -58.69 | 692 |
| 58 | VWAP momentum · 1h | momentum | 50.83 | -49.17 | 1102 | 21.5 | -61.57 | -13.51 | -61.93 | 1196 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.22 | -9.34 | -59.57 | 606 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -48.98 | -99.17 | 5402 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.64 | -31.72 | -84.05 | 1425 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.27 | -47.00 | -94.27 | 2397 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.43 | -30.56 | -90.82 | 1885 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -40.15 | -91.54 | 2222 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.49 | -26.93 | -88.49 | 1915 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -48.22 | -98.19 | 3415 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -51.34 | -96.85 | 3344 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.37 | -35.77 | -93.37 | 2104 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.19 | -35.79 | -82.19 | 1511 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -51.84 | -99.68 | 6280 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -37.85 | -93.02 | 2471 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.26 | -35.22 | -94.26 | 3140 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -64.96 | -99.82 | 6075 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.07 | -43.00 | -93.16 | 2260 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.26 | -18.73 | -51.64 | 658 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.11 | -23.63 | -78.23 | 1604 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -55.47 | -97.68 | 3229 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -56.74 | -99.17 | 5116 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.97 | -22.79 | -70.38 | 1193 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -47.48 | -94.61 | 2652 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.41 | -6.44 | -51.26 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -34.51 | -84.41 | 1643 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -69.30 | -99.77 | 6524 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -30.18 | -91.80 | 2492 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.81 | -19.87 | -83.37 | 1968 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.57 | -32.24 | -91.88 | 2158 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.21 | -46.94 | -98.22 | 4048 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.29 | -46.52 | -90.50 | 2192 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.97 | -29.25 | -68.00 | 778 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.73 | -27.75 | -72.74 | 1150 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.84 | -19.28 | -85.04 | 1827 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.11 | -49.03 | -98.12 | 4405 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -99.76 | -99.94 | 8285 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -47.65 | -7.15 | -52.53 | 298 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T12:00 | VWAP momentum · 1h | buy | ETH-USD | 2.12 | — | entry signal |
| 2026-11-26T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry signal |
| 2026-11-26T12:00 | MACD cross · 1h | sell | SOL-USD | 2.49 | 0.07 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | SOL-USD | 1.93 | -0.03 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | ETH-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T11:00 | VWAP momentum · 1h | sell | BTC-USD | 1.93 | -0.03 | exit signal |
| 2026-11-26T11:00 | Parabolic SAR · 1h | sell | XRP-USD | 9.59 | 0.20 | exit signal |
| 2026-11-26T10:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.01 | target is flat |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | ETH-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 1.96 | — | entry signal |
| 2026-11-26T10:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T09:00 | VWAP reversion · 1h | sell | ETH-USD | 21.18 | 0.01 | exit signal |
| 2026-11-26T09:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.01 | 0.02 | exit signal |
| 2026-11-26T08:00 | VWAP reversion · 1h | buy | ETH-USD | 21.17 | — | entry signal |
| 2026-11-26T07:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 19.99 | — | entry signal |
| 2026-11-26T07:00 | Three white soldiers · 1h | sell | DOGE-USD | 18.80 | 0.21 | exit signal |
| 2026-11-26T07:00 | Volume breakout · 1h | sell | DOGE-USD | 19.21 | 0.08 | exit signal |
| 2026-11-26T07:00 | VWAP momentum · 1h | sell | XRP-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 2.40 | -0.03 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 2.43 | -0.00 | exit signal |
| 2026-11-26T07:00 | Heikin-Ashi · 1h | sell | BTC-USD | 2.43 | -0.01 | exit signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-26T07:00 | Triple EMA stack · 1h | sell | DOGE-USD | 5.33 | -0.06 | rebalance down |
| 2026-11-26T06:25 | VWAP momentum · 1h | sell | DOGE-USD | 2.11 | -0.01 | target is flat |
| 2026-11-26T06:25 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.42 | -0.01 | target is flat |
| 2026-11-26T06:20 | VWAP momentum · 1h | buy | DOGE-USD | 2.12 | — | entry |
| 2026-11-26T06:20 | Heikin-Ashi · 1h | buy | DOGE-USD | 2.43 | — | entry |
| 2026-11-26T06:05 | VWAP momentum · 1h | sell | DOGE-USD | 1.95 | -0.02 | target is flat |
| 2026-11-26T06:05 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.44 | 0.01 | target is flat |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | SOL-USD | 1.94 | -0.02 | exit signal |
| 2026-11-26T06:00 | VWAP momentum · 1h | sell | BTC-USD | 1.95 | -0.02 | exit signal |
| 2026-11-26T05:00 | MFI reversion · 1h | sell | SOL-USD | 4.81 | 0.18 | exit signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | SOL-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | VWAP momentum · 1h | buy | BTC-USD | 1.96 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | SOL-USD | 6.49 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-11-26T05:00 | Triple EMA stack · 1h | sell | XRP-USD | 3.30 | 0.00 | rebalance down |
| 2026-11-26T04:00 | VWAP momentum · 1h | sell | SOL-USD | 1.95 | -0.01 | exit signal |
| 2026-11-26T04:00 | Heikin-Ashi · 1h | buy | XRP-USD | 2.44 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 12:35:05.000125+00:00 -> 2026-11-26 12:45:05.000125+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
