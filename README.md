# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T16:29:05.000157+00:00 · 64626 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.72 (-15.28%)

Closed trades 219, win rate 35.6%, fees £6.08, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 16.99 | +0.06 |

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

Today: 20226 decisions in 2592 calls, $0.2630 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T16:29 | 0 / 13 / 17 | cash |  |
| Breezy | 2026-11-18T16:29 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-18T16:29 | 5 / 23 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.89 | +5.32% | 12 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.20 | 15.20 | 0 | — | 13.22 | 4.52 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.22 | 4.21 | 0 | — | 5.09 | 1.37 | -6.60 | 0 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 7.96 | 2.22 | -9.06 | 214 |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.89 | -0.11 | 150 | 34.7 | -3.85 | -3.43 | -4.83 | 70 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 8 | 50.0 | -5.50 | -0.20 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.57 | -4.43 | 0 | — | -4.28 | -1.43 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.26 | -1.50 | -8.80 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.93 | -6.28 | -6.34 | 23 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.49 | -7.51 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 91.31 | -8.69 | 50 | 42.0 | -9.37 | -1.88 | -14.79 | 64 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.98 | -9.02 | 0 | — | -7.97 | -2.16 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.30 | -9.70 | 113 | 23.9 | -12.73 | -6.99 | -13.02 | 57 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Daily: Bullish score | daily | 87.44 | -12.56 | 17 | 17.6 | -5.36 | -0.77 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Opening range 30m | breakout | 85.18 | -14.82 | 442 | 33.5 | -10.34 | -3.28 | -14.16 | 562 |
| 25 | Agent | meta | 84.72 | -15.28 | 219 | 35.6 | -15.24 | -7.42 | -17.02 | 200 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.46 | -18.54 | 188 | 28.2 | -24.74 | -7.01 | -27.46 | 204 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Max aggression: 5-day momentum | meta | 80.21 | -19.79 | 21 | 42.9 | -47.30 | -3.13 | -55.24 | 21 |
| 30 | Keltner breakout · 1h | breakout | 80.11 | -19.89 | 124 | 25.8 | -22.63 | -5.80 | -27.42 | 157 |
| 31 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -14.79 | -4.64 | -21.17 | 77 |
| 32 | Donchian 55/20 · 1h | breakout | 78.93 | -21.07 | 78 | 12.8 | -25.54 | -6.71 | -30.46 | 84 |
| 33 | Opening range 15m | breakout | 77.58 | -22.41 | 535 | 31.6 | -17.10 | -4.61 | -21.44 | 674 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 76.72 | -23.28 | 2 | 0.0 | -18.49 | -2.49 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 74.63 | -25.37 | 209 | 19.1 | -27.80 | -4.56 | -35.45 | 268 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.44 | -8.60 | -30.50 | 111 |
| 37 | Hold BTC | benchmark | 73.48 | -26.52 | 2 | 0.0 | -18.78 | -2.58 | -28.91 | 1 |
| 38 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.02 | -7.92 | -34.15 | 221 |
| 39 | Stochastic reversion · 1h | reversion | 72.55 | -27.45 | 350 | 42.3 | -34.79 | -5.31 | -35.59 | 426 |
| 40 | Supertrend · 1h | trend | 71.82 | -28.18 | 189 | 15.9 | -32.16 | -5.43 | -39.50 | 202 |
| 41 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -40.37 | -2.49 | -57.50 | 39 |
| 42 | Triple EMA stack · 1h | trend | 71.12 | -28.88 | 155 | 14.8 | -31.92 | -6.41 | -37.84 | 178 |
| 43 | RSI momentum · 1h | momentum | 70.59 | -29.41 | 178 | 14.6 | -30.69 | -5.57 | -37.50 | 198 |
| 44 | MFI reversion · 1h | reversion | 70.29 | -29.71 | 443 | 33.6 | -27.61 | -4.12 | -30.08 | 163 |
| 45 | MACD zero-line · 1h | trend | 70.25 | -29.75 | 183 | 17.5 | -27.36 | -5.46 | -33.83 | 202 |
| 46 | EMA 20/50 cross · 1h | trend | 69.59 | -30.41 | 116 | 10.3 | -35.95 | -9.26 | -39.97 | 117 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | Heikin-Ashi · 1h | trend | 68.95 | -31.05 | 474 | 23.0 | -45.51 | -10.07 | -45.70 | 637 |
| 49 | OBV trend · 1h | momentum | 68.53 | -31.47 | 310 | 19.4 | -35.92 | -7.72 | -40.17 | 256 |
| 50 | ROC + volume · 1h | momentum | 68.33 | -31.67 | 413 | 28.1 | -33.38 | -5.99 | -39.42 | 345 |
| 51 | MACD cross · 1h | trend | 67.47 | -32.53 | 416 | 22.1 | -41.26 | -6.75 | -46.31 | 481 |
| 52 | CCI reversion · 1h | reversion | 66.91 | -33.09 | 384 | 41.4 | -42.11 | -7.03 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.83 | -33.17 | 161 | 18.0 | -35.46 | -6.62 | -41.17 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 63.82 | -36.18 | 346 | 37.6 | -38.90 | -5.93 | -39.52 | 413 |
| 55 | Williams %R · 1h | reversion | 63.34 | -36.66 | 434 | 40.8 | -46.85 | -8.20 | -47.53 | 564 |
| 56 | EMA 9/21 cross · 1h | trend | 63.13 | -36.87 | 283 | 11.0 | -40.42 | -7.95 | -46.37 | 323 |
| 57 | Agent (ML meta-label) | meta | 59.73 | -40.27 | 1914 | 24.5 | -27.89 | -5.35 | -28.08 | 305 |
| 58 | RSI(14) reversion · 1h | reversion | 58.57 | -41.43 | 206 | 32.0 | -41.40 | -6.16 | -43.22 | 254 |
| 59 | Z-score reversion · 1h | reversion | 57.22 | -42.78 | 226 | 35.0 | -37.41 | -5.20 | -39.49 | 253 |
| 60 | VWAP momentum · 1h | momentum | 55.78 | -44.22 | 973 | 21.8 | -55.83 | -11.21 | -59.35 | 1193 |
| 61 | Candlestick reversal · 1h | reversion | 55.01 | -44.99 | 551 | 26.5 | -47.46 | -8.75 | -48.31 | 639 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.82 | -21.86 | -50.71 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -43.63 | -99.05 | 5320 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.56 | -26.23 | -82.44 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -42.34 | -93.95 | 2449 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.01 | -31.87 | -90.26 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -39.14 | -91.45 | 2283 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.61 | -90.05 | 2099 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -48.41 | -97.91 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -53.72 | -96.43 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -39.17 | -93.62 | 2213 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.57 | -35.05 | -82.82 | 1580 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.18 | -99.61 | 6114 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.99 | -42.75 | -92.15 | 2541 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.91 | -39.46 | -94.92 | 3275 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.56 | -99.81 | 6179 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.48 | -44.11 | -92.61 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.14 | -25.81 | -76.70 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.34 | -97.71 | 3420 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.08 | -58.42 | -99.08 | 4973 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.76 | -27.52 | -69.39 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -57.12 | -94.66 | 2746 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -38.28 | -84.83 | 1722 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.72 | -99.70 | 6392 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.98 | -31.54 | -91.01 | 2373 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.33 | -19.10 | -80.33 | 1856 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.60 | -36.94 | -91.62 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.59 | -46.33 | -97.59 | 3928 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -57.76 | -89.26 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.16 | -30.11 | -67.04 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.56 | -23.85 | -73.04 | 1217 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.62 | -18.37 | -81.67 | 1761 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.60 | -46.51 | -97.61 | 4330 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.61 | -99.94 | 8438 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T16:25 | VWAP momentum · 1h | sell | AMZN | 14.32 | 0.30 | target is flat |
| 2026-11-18T16:21 | Williams %R · 1h | buy | PLTR | 2.76 | — | entry |
| 2026-11-18T16:21 | Williams %R · 1h | buy | ETHU | 3.51 | — | entry |
| 2026-11-18T16:21 | Williams %R · 1h | sell | DOGE-USD | 3.14 | -0.06 | stop-loss |
| 2026-11-18T16:21 | Williams %R · 1h | sell | BTC-USD | 3.13 | -0.07 | stop-loss |
| 2026-11-18T16:21 | Stochastic reversion · 1h | sell | DOGE-USD | 4.50 | -0.10 | stop-loss |
| 2026-11-18T16:21 | Z-score reversion · 1h | buy | MSFT | 3.60 | — | rebalance up |
| 2026-11-18T16:21 | Z-score reversion · 1h | sell | ETHU | 4.17 | -0.28 | stop-loss |
| 2026-11-18T16:21 | Donchian 55/20 · 1h | sell | SOL-USD | 19.27 | -0.68 | stop-loss |
| 2026-11-18T16:21 | Ichimoku · 1h | sell | SOL-USD | 18.19 | -0.60 | stop-loss |
| 2026-11-18T16:21 | Opening range 15m | buy | SQQQ | 18.89 | — | entry signal |
| 2026-11-18T16:15 | Agent (rotation) | sell | AMZN | 7.83 | -0.01 | selected signal exited |
| 2026-11-18T16:15 | Agent (ML meta-label) | buy | SPY | 3.42 | — | rebalance up |
| 2026-11-18T16:15 | Agent (ML meta-label) | sell | ETHU | 3.43 | -0.02 | selected signal exited |
| 2026-11-18T16:15 | CCI reversion · 1h | buy | PLTR | 4.46 | — | entry |
| 2026-11-18T16:15 | CCI reversion · 1h | sell | BTC-USD | 4.71 | -0.06 | stop-loss |
| 2026-11-18T16:15 | Bollinger reversion · 1h | sell | BITX | 7.78 | -0.36 | stop-loss |
| 2026-11-18T16:15 | Candlestick reversal · 1h | sell | BITX | 2.85 | -0.08 | stop-loss |
| 2026-11-18T16:15 | Gap and go | sell | AMZN | 24.98 | -0.02 | exit signal |
| 2026-11-18T16:11 | Agent (ML meta-label) | buy | ETHU | 3.45 | — | entry |
| 2026-11-18T16:11 | Agent (ML meta-label) | sell | GOOGL | 3.45 | 0.00 | selected signal exited |
| 2026-11-18T16:11 | MFI reversion · 1h | sell | ETHU | 11.72 | -0.05 | target is flat |
| 2026-11-18T16:05 | OBV trend · 1h | buy | AAPL | 17.13 | — | entry |
| 2026-11-18T16:00 | Agent (rotation) | buy | AMZN | 7.83 | — | entry |
| 2026-11-18T16:00 | Agent (ML meta-label) | buy | GOOGL | 3.45 | — | entry |
| 2026-11-18T16:00 | Donchian 20/10 · 1h | sell | XRP-USD | 15.92 | -0.16 | exit signal |
| 2026-11-18T16:00 | OBV trend · 1h | sell | XRP-USD | 17.17 | 0.07 | exit signal |
| 2026-11-18T16:00 | RSI momentum · 1h | sell | SOL-USD | 17.89 | 0.08 | exit signal |
| 2026-11-18T16:00 | ROC + volume · 1h | sell | XRP-USD | 16.86 | -0.27 | exit signal |
| 2026-11-18T16:00 | Ichimoku · 1h | sell | XRP-USD | 18.70 | -0.09 | exit signal |
| 2026-11-18T16:00 | Ichimoku · 1h | sell | DOGE-USD | 18.41 | -0.38 | exit signal |
| 2026-11-18T16:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 17.22 | -0.37 | exit signal |
| 2026-11-18T16:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 15.73 | -0.22 | exit signal |
| 2026-11-18T16:00 | Gap and go | buy | AMZN | 25.00 | — | entry signal |
| 2026-11-18T15:55 | Agent (ML meta-label) | sell | SPY | 3.45 | -0.02 | rebalance down |
| 2026-11-18T15:55 | Agent | buy | TSLA | 16.93 | — | following Stochastic reversion |
| 2026-11-18T15:50 | Stochastic reversion · 1h | sell | BITX | 4.15 | -0.17 | stop-loss |
| 2026-11-18T15:50 | Candlestick reversal · 1h | buy | LABU | 3.23 | — | entry |
| 2026-11-18T15:50 | Candlestick reversal · 1h | sell | META | 3.03 | -0.04 | stop-loss |
| 2026-11-18T15:50 | Candlestick reversal · 1h | sell | BTC-USD | 2.82 | -0.09 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 16:29:05.000157+00:00 -> 2026-11-18 16:39:05.000157+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 16:29:05.000157+00:00 -> 2026-11-18 16:39:05.000157+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
