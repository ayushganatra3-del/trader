# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T19:45:05.000138+00:00 · 69730 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £80.18 (-19.82%)

Closed trades 238, win rate 36.1%, fees £6.46, max drawdown -20.19%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, KNOP 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 15660 decisions in 3132 calls, $0.2188 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T19:45 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-22T19:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T19:45 | 2 / 3 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.26% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.62 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.37 | -2.45 | -2.96 | 67 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.21 | 0.50 | -7.48 | 143 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.41 | -4.12 | -10.21 | 36 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -17.27 | -7.66 | -19.30 | 73 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.12 | -2.75 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -14.66 | -4.23 | -20.49 | 157 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.40 | -15.60 | 194 | 27.8 | -23.12 | -6.20 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.82 | -7.66 | -20.00 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.26 | -19.74 | 126 | 26.2 | -22.53 | -6.53 | -24.07 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.18 | -4.89 | -21.94 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.76 | -4.14 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.74 | -23.26 | 107 | 14.0 | -26.97 | -7.28 | -31.39 | 107 |
| 34 | ADX DI cross · 1h | trend | 74.11 | -25.89 | 234 | 20.1 | -31.36 | -5.87 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 73.78 | -26.22 | 198 | 16.7 | -32.82 | -6.32 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.88 | -3.82 | -57.07 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.60 | -27.40 | 161 | 14.3 | -32.00 | -7.69 | -36.22 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.44 | -27.56 | 119 | 10.1 | -35.75 | -9.69 | -40.34 | 123 |
| 39 | Bollinger breakout · 1h | breakout | 71.44 | -28.56 | 199 | 21.1 | -33.97 | -8.89 | -35.59 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 41 | Hold BTC | benchmark | 70.30 | -29.70 | 3 | 0.0 | -30.39 | -5.46 | -36.21 | 1 |
| 42 | OBV trend · 1h | momentum | 70.23 | -29.77 | 316 | 19.6 | -35.90 | -9.12 | -40.12 | 230 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.39 | -30.61 | 498 | 23.1 | -45.23 | -9.67 | -46.74 | 615 |
| 45 | RSI momentum · 1h | momentum | 69.14 | -30.86 | 186 | 14.0 | -36.80 | -8.03 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.23 | -6.15 | -43.86 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.18 | -33.82 | 195 | 16.9 | -34.60 | -9.57 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 66.04 | -33.96 | 170 | 17.1 | -40.89 | -9.16 | -42.63 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.84 | -34.16 | 433 | 27.5 | -41.75 | -8.68 | -42.61 | 341 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.85 | -5.13 | -38.63 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 63.29 | -36.71 | 296 | 11.1 | -44.31 | -10.48 | -46.01 | 330 |
| 53 | MACD cross · 1h | trend | 61.88 | -38.12 | 452 | 21.5 | -48.80 | -9.58 | -49.69 | 501 |
| 54 | CCI reversion · 1h | reversion | 58.83 | -41.17 | 426 | 39.9 | -47.34 | -7.73 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.71 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.77 | -44.23 | 1026 | 21.6 | -59.07 | -13.80 | -60.53 | 1202 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -32.70 | -5.65 | -35.66 | 339 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.62 | -8.76 | -55.96 | 590 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.01 | -6.49 | -49.45 | 275 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.67 | -22.83 | -52.81 | 661 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.86 | -8.47 | -54.24 | 685 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -49.30 | -99.15 | 5356 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.42 | -36.13 | -84.50 | 1419 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.61 | -49.34 | -94.64 | 2451 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.02 | -32.82 | -91.33 | 1943 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.63 | -41.43 | -91.86 | 2272 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.60 | -28.92 | -89.62 | 1975 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -48.52 | -98.19 | 3471 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -53.65 | -96.91 | 3382 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -38.75 | -93.48 | 2171 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.33 | -35.34 | -83.48 | 1562 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -56.93 | -99.67 | 6357 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -40.13 | -92.93 | 2514 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.36 | -38.18 | -94.36 | 3138 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -67.70 | -99.84 | 6269 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.46 | -45.82 | -93.47 | 2279 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.18 | -24.07 | -79.45 | 1638 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -59.78 | -97.79 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.24 | -99.18 | 5133 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.17 | -27.93 | -70.47 | 1219 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -49.86 | -94.85 | 2709 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.52 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.41 | -37.42 | -85.52 | 1692 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.35 | -99.76 | 6573 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.73 | -31.86 | -91.74 | 2496 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.04 | -20.16 | -83.15 | 1964 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.41 | -33.03 | -92.44 | 2198 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.09 | -48.93 | -98.09 | 4077 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.15 | -48.80 | -90.25 | 2216 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.38 | -31.09 | -67.59 | 795 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.69 | -27.59 | -74.59 | 1189 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.63 | -18.84 | -83.82 | 1865 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.90 | -48.61 | -97.90 | 4466 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.74 | -99.94 | 8392 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-22T19:00 | Heikin-Ashi · 1h | sell | ETH-USD | 17.21 | -0.19 | exit signal |
| 2026-11-22T17:00 | VWAP momentum · 1h | buy | XRP-USD | 4.49 | — | entry signal |
| 2026-11-22T17:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.39 | — | entry signal |
| 2026-11-22T17:00 | MACD cross · 1h | buy | XRP-USD | 6.38 | — | entry signal |
| 2026-11-22T17:00 | Triple EMA stack · 1h | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-11-22T16:00 | OBV trend · 1h | buy | ETH-USD | 17.58 | — | entry signal |
| 2026-11-22T16:00 | Triple EMA stack · 1h | buy | ETH-USD | 18.23 | — | entry signal |
| 2026-11-22T16:00 | Three white soldiers | sell | DOGE-USD | 12.72 | -0.07 | exit signal |
| 2026-11-22T15:21 | Three white soldiers | sell | XRP-USD | 12.68 | -0.11 | exit signal |
| 2026-11-22T15:00 | Ichimoku · 1h | buy | SOL-USD | 19.21 | — | entry signal |
| 2026-11-22T15:00 | Ichimoku · 1h | buy | ETH-USD | 19.21 | — | entry signal |
| 2026-11-22T15:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 18.15 | — | entry signal |
| 2026-11-22T15:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 18.15 | — | entry signal |
| 2026-11-22T14:45 | Three white soldiers | buy | XRP-USD | 12.79 | — | entry signal |
| 2026-11-22T14:45 | Three white soldiers | buy | DOGE-USD | 12.79 | — | entry signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | SOL-USD | 11.53 | -0.16 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | ETH-USD | 11.62 | -0.16 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 11.52 | -0.21 | exit signal |
| 2026-11-22T14:00 | Heikin-Ashi · 1h | sell | BTC-USD | 11.60 | -0.09 | exit signal |
| 2026-11-22T14:00 | ADX DI cross · 1h | sell | DOGE-USD | 18.39 | -0.10 | exit signal |
| 2026-11-22T14:00 | MACD cross · 1h | sell | XRP-USD | 6.38 | -0.15 | exit signal |
| 2026-11-22T13:00 | ROC + volume · 1h | buy | BTC-USD | 16.46 | — | entry signal |
| 2026-11-22T13:00 | VWAP momentum · 1h | sell | XRP-USD | 4.49 | -0.05 | exit signal |
| 2026-11-22T13:00 | Heikin-Ashi · 1h | sell | XRP-USD | 3.04 | -0.05 | exit signal |
| 2026-11-22T11:00 | CCI reversion · 1h | sell | DOGE-USD | 14.75 | 0.06 | exit signal |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | buy | XRP-USD | 3.09 | — | entry signal |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | buy | SOL-USD | 11.69 | — | entry signal |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | buy | BTC-USD | 11.69 | — | entry signal |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | sell | ETH-USD | 5.74 | -0.06 | rebalance down |
| 2026-11-22T11:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 5.83 | -0.03 | rebalance down |
| 2026-11-22T10:00 | CCI reversion · 1h | buy | XRP-USD | 3.04 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | buy | SOL-USD | 3.00 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | buy | DOGE-USD | 2.99 | — | rebalance up |
| 2026-11-22T10:00 | CCI reversion · 1h | sell | ETH-USD | 11.87 | 0.29 | exit signal |
| 2026-11-22T10:00 | CCI reversion · 1h | sell | BTC-USD | 11.88 | 0.19 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | XRP-USD | 13.64 | 0.15 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | SOL-USD | 5.57 | 0.06 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | ETH-USD | 11.06 | 0.28 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | DOGE-USD | 13.71 | 0.26 | exit signal |
| 2026-11-22T10:00 | Williams %R · 1h | sell | BTC-USD | 11.05 | 0.30 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 19:45:05.000138+00:00 -> 2026-11-22 19:55:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
