# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-26T15:05:05.000120+00:00 · 74374 ticks

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
| Copy: Insider buying | 2026-11-25 | SHMD 12%, PLTR 12%, WWB 12%, COHR 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-25)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 38.53 · VIX 28.29 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 5.2, LABU 3.8, TSLA 2.1, PLTR 1.1, META 0.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 11217 decisions in 2244 calls, $0.1565 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-26T15:05 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-26T15:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-26T15:05 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.92 | 15.92 | 0 | — | 14.88 | 4.99 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.27 | 9.27 | 42 | 42.9 | 5.81 | 1.11 | -9.74 | 33 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 105.07 | 5.07 | 0 | — | 6.08 | 1.61 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.22 | 1.22 | 43 | 27.9 | -1.71 | -0.07 | -14.66 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 97.99 | -2.01 | 221 | 31.2 | -0.01 | 0.09 | -7.91 | 208 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.04 | -3.09 | -7.38 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 95.09 | -4.91 | 171 | 32.7 | -4.91 | -4.27 | -5.47 | 54 |
| 11 | Agent (rotation) | meta | 94.63 | -5.37 | 232 | 28.4 | 1.30 | 0.49 | -5.49 | 186 |
| 12 | Hold SPY | benchmark | 94.08 | -5.92 | 0 | — | -6.75 | -1.72 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.57 | -6.43 | 24 | 12.5 | -5.29 | -7.77 | -6.57 | 26 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.29 | -6.71 | 0 | — | -7.99 | -1.60 | -13.91 | 1 |
| 15 | Copy: Insider buying | copy | 93.13 | -6.87 | 63 | 41.3 | -4.98 | -0.83 | -14.79 | 73 |
| 16 | Trend pullback · 1h | trend | 91.56 | -8.44 | 116 | 24.1 | -7.57 | -4.49 | -10.99 | 32 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 89.28 | -10.72 | 29 | 17.2 | -10.69 | -7.58 | -11.13 | 23 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.17 | -10.83 | 0 | — | -12.17 | -2.63 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.03 | -3.16 | -20.94 | 1 |
| 20 | Opening range 30m | breakout | 86.89 | -13.11 | 489 | 33.9 | -10.23 | -3.11 | -15.56 | 552 |
| 21 | Daily: Bullish score | daily | 85.82 | -14.18 | 20 | 20.0 | -13.31 | -2.94 | -19.56 | 14 |
| 22 | VWAP reversion · 1h | reversion | 84.70 | -15.30 | 174 | 44.8 | -12.87 | -2.37 | -20.49 | 156 |
| 23 | Squeeze breakout · 1h | breakout | 83.24 | -16.76 | 78 | 20.5 | -19.63 | -6.67 | -19.91 | 79 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.87 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.99 | -20.01 | 222 | 41.0 | -13.17 | -6.06 | -13.42 | 59 |
| 26 | Opening range 15m | breakout | 79.14 | -20.86 | 616 | 32.0 | -18.81 | -5.22 | -24.05 | 678 |
| 27 | Volume breakout · 1h | breakout | 76.82 | -23.18 | 174 | 29.3 | -22.21 | -8.80 | -22.48 | 69 |
| 28 | Agent | meta | 76.44 | -23.56 | 250 | 36.0 | -27.16 | -6.06 | -27.61 | 196 |
| 29 | Agent (aggressive) | meta | 75.83 | -24.17 | 115 | 33.0 | -17.75 | -4.58 | -18.54 | 93 |
| 30 | Parabolic SAR · 1h | trend | 75.39 | -24.61 | 211 | 28.0 | -34.34 | -8.27 | -35.47 | 182 |
| 31 | Donchian 55/20 · 1h | breakout | 74.60 | -25.40 | 88 | 13.6 | -29.07 | -7.62 | -29.10 | 73 |
| 32 | Max aggression: 5-day momentum | meta | 73.99 | -26.01 | 27 | 37.0 | -54.97 | -2.83 | -67.33 | 22 |
| 33 | Ichimoku · 1h | trend | 73.31 | -26.70 | 114 | 15.8 | -28.79 | -7.26 | -29.63 | 95 |
| 34 | Keltner breakout · 1h | breakout | 73.08 | -26.92 | 142 | 24.6 | -26.53 | -6.48 | -26.54 | 143 |
| 35 | Daily: Momentum burst | daily | 71.06 | -28.94 | 31 | 16.1 | -33.19 | -4.55 | -35.97 | 25 |
| 36 | ADX DI cross · 1h | trend | 69.80 | -30.20 | 264 | 18.9 | -37.04 | -6.91 | -38.08 | 285 |
| 37 | Hold BTC | benchmark | 69.70 | -30.30 | 3 | 0.0 | -28.39 | -4.99 | -36.10 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 68.07 | -31.93 | 210 | 22.9 | -31.32 | -8.06 | -31.81 | 206 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 67.83 | -32.17 | 3 | 0.0 | -25.48 | -3.15 | -33.66 | 1 |
| 40 | Supertrend · 1h | trend | 66.82 | -33.18 | 221 | 17.6 | -40.45 | -8.01 | -42.06 | 210 |
| 41 | Stochastic reversion · 1h | reversion | 66.65 | -33.35 | 411 | 39.9 | -33.01 | -3.44 | -42.70 | 438 |
| 42 | OBV trend · 1h | momentum | 66.42 | -33.58 | 325 | 19.7 | -40.96 | -10.16 | -40.96 | 223 |
| 43 | EMA 20/50 cross · 1h | trend | 65.71 | -34.30 | 126 | 9.5 | -37.53 | -10.33 | -37.68 | 116 |
| 44 | Triple EMA stack · 1h | trend | 64.43 | -35.57 | 172 | 15.1 | -42.54 | -10.52 | -42.54 | 172 |
| 45 | MACD zero-line · 1h | trend | 63.01 | -36.99 | 205 | 16.6 | -36.89 | -10.24 | -37.23 | 200 |
| 46 | MFI reversion · 1h | reversion | 62.66 | -37.34 | 520 | 32.7 | -32.25 | -4.75 | -38.15 | 193 |
| 47 | RSI momentum · 1h | momentum | 62.49 | -37.51 | 203 | 14.8 | -43.15 | -9.51 | -43.57 | 192 |
| 48 | Donchian 20/10 · 1h | breakout | 61.22 | -38.78 | 183 | 17.5 | -41.12 | -9.10 | -42.86 | 199 |
| 49 | Heikin-Ashi · 1h | trend | 60.80 | -39.20 | 554 | 21.8 | -49.37 | -10.08 | -49.85 | 641 |
| 50 | ROC + volume · 1h | momentum | 60.59 | -39.41 | 469 | 26.9 | -40.41 | -7.84 | -41.18 | 335 |
| 51 | Max aggression: 1-day momentum | meta | 60.11 | -39.90 | 35 | 28.6 | -61.92 | -4.63 | -63.62 | 39 |
| 52 | EMA 9/21 cross · 1h | trend | 58.06 | -41.94 | 314 | 12.1 | -45.68 | -10.44 | -46.81 | 332 |
| 53 | MACD cross · 1h | trend | 57.28 | -42.72 | 496 | 21.0 | -53.86 | -10.88 | -55.66 | 510 |
| 54 | Agent (ML meta-label) | meta | 56.24 | -43.76 | 2074 | 25.4 | -18.28 | -2.22 | -26.33 | 313 |
| 55 | CCI reversion · 1h | reversion | 52.50 | -47.50 | 463 | 37.8 | -53.12 | -8.97 | -55.52 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 52.13 | -47.87 | 405 | 36.3 | -40.76 | -4.96 | -45.49 | 430 |
| 57 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -56.28 | -9.21 | -58.65 | 688 |
| 58 | VWAP momentum · 1h | momentum | 50.73 | -49.27 | 1105 | 21.4 | -61.25 | -13.43 | -61.58 | 1193 |
| 59 | Williams %R · 1h ⛔ | reversion | 50.67 | -49.33 | 518 | 37.1 | -56.26 | -9.35 | -59.57 | 606 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.17 | -48.65 | -99.17 | 5401 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.77 | -32.10 | -83.97 | 1424 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.31 | -47.42 | -94.31 | 2400 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.46 | -30.42 | -90.72 | 1882 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.61 | -40.36 | -91.61 | 2225 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -88.68 | -27.22 | -88.68 | 1924 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -48.18 | -98.19 | 3411 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -51.61 | -96.87 | 3348 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.29 | -35.32 | -93.29 | 2096 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.16 | -35.67 | -82.17 | 1509 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.68 | -51.57 | -99.68 | 6274 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -37.81 | -93.02 | 2472 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.32 | -35.23 | -94.32 | 3145 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.04 | -99.81 | 6071 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.06 | -43.01 | -93.13 | 2259 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -49.33 | -18.90 | -51.64 | 658 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.22 | -23.66 | -78.34 | 1606 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -56.53 | -97.71 | 3232 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -56.90 | -99.17 | 5114 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.18 | -22.95 | -70.38 | 1196 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -47.72 | -94.67 | 2657 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.40 | -6.44 | -51.25 | 291 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.57 | -35.04 | -84.58 | 1646 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.77 | -67.04 | -99.77 | 6518 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.47 | -30.25 | -91.80 | 2491 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.81 | -19.87 | -83.37 | 1968 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.47 | -31.67 | -91.85 | 2154 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.22 | -47.30 | -98.23 | 4048 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.25 | -46.00 | -90.47 | 2190 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.04 | -29.23 | -68.06 | 780 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.89 | -28.00 | -72.89 | 1152 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.63 | -18.98 | -85.00 | 1824 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.10 | -48.49 | -98.11 | 4404 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -100.00 | -99.94 | 8287 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.93 | -6.98 | -52.52 | 293 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-26T15:05 | Keltner breakout · 1h | sell | XRP-USD | 18.08 | -0.32 | stop-loss |
| 2026-11-26T15:05 | ROC + volume · 1h | sell | DOGE-USD | 15.06 | -0.11 | target is flat |
| 2026-11-26T15:05 | VWAP momentum · 1h | sell | DOGE-USD | 2.08 | -0.03 | target is flat |
| 2026-11-26T15:00 | Squeeze breakout · 1h | sell | XRP-USD | 20.90 | 0.10 | exit signal |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | SOL-USD | 3.44 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | ETH-USD | 3.46 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | buy | BTC-USD | 3.45 | — | rebalance up |
| 2026-11-26T15:00 | Bollinger breakout · 1h | sell | XRP-USD | 13.69 | 0.07 | exit signal |
| 2026-11-26T15:00 | ROC + volume · 1h | buy | DOGE-USD | 5.07 | — | rebalance up |
| 2026-11-26T15:00 | ROC + volume · 1h | buy | BTC-USD | 5.08 | — | rebalance up |
| 2026-11-26T15:00 | ROC + volume · 1h | sell | SOL-USD | 8.20 | 0.09 | exit signal |
| 2026-11-26T15:00 | ROC + volume · 1h | sell | ETH-USD | 12.12 | -0.03 | exit signal |
| 2026-11-26T15:00 | VWAP momentum · 1h | sell | SOL-USD | 2.01 | -0.02 | exit signal |
| 2026-11-26T15:00 | VWAP momentum · 1h | sell | ETH-USD | 2.10 | -0.02 | exit signal |
| 2026-11-26T15:00 | Heikin-Ashi · 1h | sell | ETH-USD | 2.74 | -0.03 | exit signal |
| 2026-11-26T15:00 | MACD zero-line · 1h | buy | ETH-USD | 15.80 | — | entry |
| 2026-11-26T15:00 | MACD zero-line · 1h | sell | DOGE-USD | 7.90 | -0.06 | exit signal |
| 2026-11-26T15:00 | MACD zero-line · 1h | sell | BTC-USD | 7.90 | 0.02 | exit signal |
| 2026-11-26T15:00 | MACD cross · 1h | sell | DOGE-USD | 4.16 | 0.10 | exit signal |
| 2026-11-26T15:00 | MACD cross · 1h | sell | BTC-USD | 2.90 | 0.03 | exit signal |
| 2026-11-26T14:00 | ROC + volume · 1h | buy | SOL-USD | 1.44 | — | rebalance up |
| 2026-11-26T14:00 | ROC + volume · 1h | buy | ETH-USD | 5.40 | — | rebalance up |
| 2026-11-26T14:00 | ROC + volume · 1h | sell | XRP-USD | 6.83 | 0.15 | exit signal |
| 2026-11-26T14:00 | VWAP momentum · 1h | buy | SOL-USD | 2.03 | — | entry signal |
| 2026-11-26T14:00 | Heikin-Ashi · 1h | buy | ETH-USD | 2.76 | — | entry signal |
| 2026-11-26T13:00 | MACD zero-line · 1h | buy | DOGE-USD | 7.97 | — | entry |
| 2026-11-26T13:00 | MACD zero-line · 1h | sell | XRP-USD | 7.97 | 0.04 | exit signal |
| 2026-11-26T13:00 | MACD cross · 1h | sell | XRP-USD | 2.52 | 0.06 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-28 15:05:05.000120+00:00 -> 2026-11-26 15:15:05.000120+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
