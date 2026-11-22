# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T18:14:05.000136+00:00 · 69661 ticks

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

Today: 14625 decisions in 2925 calls, $0.2043 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T18:14 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-11-22T18:14 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T18:14 | 1 / 4 / 0 | ETH-USD 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.73 | +27.25% | 5 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.56 | +8.27% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.49 | 14.49 | 0 | — | 12.18 | 4.63 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.12 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.34 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.53 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.14 | -4.05 | -9.95 | 35 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -17.38 | -7.69 | -19.29 | 73 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.13 | -2.75 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -14.65 | -4.23 | -20.49 | 157 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.40 | -15.60 | 194 | 27.8 | -23.10 | -6.20 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.82 | -7.66 | -20.00 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.22 | -19.78 | 126 | 26.2 | -22.57 | -6.54 | -24.07 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.80 | -5.06 | -21.36 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -14.87 | -3.73 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.73 | -23.27 | 107 | 14.0 | -26.98 | -7.28 | -31.39 | 107 |
| 34 | ADX DI cross · 1h | trend | 74.09 | -25.91 | 234 | 20.1 | -31.56 | -5.92 | -35.87 | 277 |
| 35 | Supertrend · 1h | trend | 73.78 | -26.22 | 198 | 16.7 | -32.80 | -6.32 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.89 | -3.82 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.57 | -27.43 | 161 | 14.3 | -32.07 | -7.72 | -36.10 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.41 | -27.59 | 119 | 10.1 | -35.77 | -9.69 | -40.34 | 123 |
| 39 | Bollinger breakout · 1h | breakout | 71.40 | -28.60 | 199 | 21.1 | -34.00 | -8.90 | -35.59 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 41 | Hold BTC | benchmark | 70.22 | -29.78 | 3 | 0.0 | -29.81 | -5.48 | -36.23 | 1 |
| 42 | OBV trend · 1h | momentum | 70.22 | -29.78 | 316 | 19.6 | -35.90 | -9.12 | -40.12 | 230 |
| 43 | Heikin-Ashi · 1h | trend | 69.43 | -30.57 | 497 | 23.1 | -45.20 | -9.66 | -46.74 | 615 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 32 |
| 45 | RSI momentum · 1h | momentum | 69.13 | -30.87 | 186 | 14.0 | -36.86 | -8.04 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.39 | -6.17 | -43.99 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.19 | -33.81 | 195 | 16.9 | -34.59 | -9.56 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 66.01 | -33.99 | 170 | 17.1 | -40.87 | -9.16 | -42.59 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.80 | -34.20 | 433 | 27.5 | -40.81 | -8.71 | -42.02 | 339 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.77 | -5.11 | -38.55 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 63.30 | -36.70 | 296 | 11.1 | -44.29 | -10.47 | -46.01 | 330 |
| 53 | MACD cross · 1h | trend | 61.89 | -38.12 | 452 | 21.5 | -48.79 | -9.58 | -49.69 | 501 |
| 54 | CCI reversion · 1h | reversion | 58.87 | -41.13 | 426 | 39.9 | -47.31 | -7.72 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.77 | -44.23 | 1026 | 21.6 | -58.78 | -13.69 | -60.42 | 1201 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -32.32 | -5.93 | -35.24 | 317 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.62 | -8.76 | -55.96 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -43.66 | -6.41 | -49.45 | 277 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.84 | -22.81 | -52.86 | 662 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.70 | -8.65 | -55.03 | 688 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -49.27 | -99.16 | 5364 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.33 | -35.87 | -84.48 | 1419 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.67 | -49.26 | -94.71 | 2455 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.03 | -32.70 | -91.38 | 1944 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.73 | -41.30 | -91.98 | 2275 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.58 | -28.95 | -89.58 | 1973 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -48.45 | -98.20 | 3474 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -54.75 | -96.92 | 3382 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -38.90 | -93.34 | 2161 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.33 | -35.26 | -83.48 | 1562 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -57.08 | -99.66 | 6346 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.75 | -40.01 | -92.96 | 2517 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.31 | -38.07 | -94.31 | 3132 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -67.44 | -99.84 | 6265 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.46 | -45.82 | -93.47 | 2279 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.48 | -24.13 | -79.75 | 1645 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -59.31 | -97.79 | 3352 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.01 | -99.18 | 5132 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.07 | -27.93 | -70.47 | 1220 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -49.86 | -94.89 | 2713 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.52 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.51 | -37.46 | -85.62 | 1696 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.36 | -99.76 | 6574 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.71 | -31.88 | -91.73 | 2495 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.03 | -20.16 | -83.15 | 1964 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.43 | -32.95 | -92.47 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.08 | -48.85 | -98.09 | 4076 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.15 | -48.80 | -90.25 | 2216 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.53 | -31.09 | -67.59 | 797 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.69 | -27.59 | -74.59 | 1189 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.71 | -18.82 | -83.89 | 1863 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.90 | -48.63 | -97.90 | 4467 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -109.73 | -99.94 | 8395 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | SOL-USD | 4.24 | 0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 18:14:05.000136+00:00 -> 2026-11-22 18:24:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
