# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-22T14:20:05.000139+00:00 · 69457 ticks

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
| Copy: Insider buying | 2026-11-21 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 11565 decisions in 2313 calls, $0.1617 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-22T14:20 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-11-22T14:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-22T14:20 | 1 / 4 / 0 | cash |  |

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
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -3.14 | -2.96 | -3.73 | 72 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.53 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.41 | -4.12 | -10.21 | 36 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.38 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.24 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -17.02 | -7.64 | -19.69 | 73 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.13 | -2.75 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -14.56 | -4.21 | -20.40 | 157 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -4.00 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -4.01 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.80 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.24 | -15.76 | 194 | 27.8 | -23.34 | -6.26 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.43 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -19.82 | -9.62 | -20.09 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.96 | -5.11 | -21.26 | 199 |
| 29 | Keltner breakout · 1h | breakout | 80.15 | -19.85 | 126 | 26.2 | -21.86 | -6.31 | -24.03 | 138 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.77 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.95 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.69 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -26.88 | -7.25 | -31.39 | 105 |
| 34 | ADX DI cross · 1h | trend | 74.11 | -25.89 | 234 | 20.1 | -31.50 | -5.90 | -35.87 | 277 |
| 35 | Supertrend · 1h | trend | 73.64 | -26.36 | 198 | 16.7 | -33.00 | -6.37 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.89 | -3.82 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -31.65 | -7.57 | -36.21 | 165 |
| 38 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.66 | -9.60 | -40.43 | 121 |
| 39 | Bollinger breakout · 1h | breakout | 71.34 | -28.66 | 199 | 21.1 | -33.76 | -8.90 | -35.61 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.14 | -32.18 | 1 |
| 41 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -35.73 | -9.04 | -40.09 | 229 |
| 42 | Hold BTC | benchmark | 70.27 | -29.73 | 3 | 0.0 | -29.64 | -5.47 | -36.23 | 1 |
| 43 | Heikin-Ashi · 1h | trend | 69.58 | -30.42 | 497 | 23.1 | -45.08 | -9.63 | -46.74 | 614 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.41 | -37.91 | 32 |
| 45 | RSI momentum · 1h | momentum | 69.01 | -30.99 | 186 | 14.0 | -36.93 | -8.05 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.31 | -6.16 | -44.02 | 449 |
| 48 | MACD zero-line · 1h | trend | 66.11 | -33.89 | 195 | 16.9 | -34.68 | -9.57 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.95 | -34.05 | 170 | 17.1 | -40.66 | -9.16 | -42.61 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.75 | -34.25 | 433 | 27.5 | -41.08 | -8.80 | -42.02 | 339 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -35.78 | -5.29 | -39.51 | 179 |
| 52 | EMA 9/21 cross · 1h | trend | 63.12 | -36.88 | 296 | 11.1 | -44.77 | -10.63 | -46.01 | 332 |
| 53 | MACD cross · 1h | trend | 61.82 | -38.19 | 452 | 21.5 | -49.26 | -9.73 | -50.47 | 503 |
| 54 | CCI reversion · 1h | reversion | 58.71 | -41.29 | 426 | 39.9 | -47.41 | -7.76 | -51.36 | 493 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.73 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.70 | -44.30 | 1026 | 21.6 | -58.61 | -13.63 | -60.39 | 1200 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -31.63 | -5.43 | -33.17 | 320 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.60 | -8.75 | -55.96 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -43.87 | -6.45 | -49.45 | 277 |
| 60 | Three white soldiers | momentum | 51.16 | -48.84 | 630 | 14.4 | -52.69 | -22.57 | -52.91 | 661 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.11 | -8.54 | -54.48 | 686 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -48.89 | -99.15 | 5344 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.28 | -35.71 | -84.48 | 1415 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.60 | -48.41 | -94.66 | 2453 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.94 | -32.26 | -91.35 | 1939 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.60 | -40.54 | -91.96 | 2273 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.42 | -28.79 | -89.42 | 1969 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.18 | -47.60 | -98.20 | 3472 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -53.79 | -96.86 | 3386 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -39.61 | -93.50 | 2165 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.42 | -35.26 | -83.56 | 1566 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -56.93 | -99.67 | 6347 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -39.39 | -92.92 | 2513 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.28 | -37.91 | -94.28 | 3123 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -66.83 | -99.84 | 6271 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.41 | -45.15 | -93.46 | 2276 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.38 | -24.06 | -79.44 | 1642 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -58.61 | -97.79 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -60.91 | -99.18 | 5134 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.74 | -27.49 | -70.47 | 1219 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -49.03 | -94.77 | 2708 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.54 | -6.18 | -49.04 | 275 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.42 | -37.01 | -85.53 | 1696 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.07 | -99.76 | 6575 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.71 | -31.89 | -91.72 | 2495 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.03 | -20.16 | -83.15 | 1964 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.50 | -33.11 | -92.54 | 2199 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.09 | -48.75 | -98.09 | 4078 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.09 | -48.64 | -90.18 | 2213 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.48 | -31.18 | -67.48 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.11 | -27.66 | -74.90 | 1196 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.13 | -19.23 | -84.30 | 1867 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.90 | -48.58 | -97.90 | 4468 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.83 | -99.94 | 8405 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | ETH-USD | 4.89 | 0.13 | exit signal |
| 2026-11-22T10:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.28 | 0.12 | exit signal |
| 2026-11-22T10:00 | Keltner breakout · 1h | buy | ETH-USD | 20.13 | — | entry signal |
| 2026-11-22T10:00 | Keltner breakout · 1h | buy | BTC-USD | 20.13 | — | entry signal |
| 2026-11-22T10:00 | Bollinger breakout · 1h | buy | ETH-USD | 17.92 | — | entry signal |
| 2026-11-22T10:00 | Bollinger breakout · 1h | buy | BTC-USD | 17.92 | — | entry signal |
| 2026-11-22T10:00 | Donchian 20/10 · 1h | buy | ETH-USD | 16.57 | — | entry signal |
| 2026-11-22T10:00 | Donchian 20/10 · 1h | buy | BTC-USD | 16.57 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | ETH-USD | 14.57 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | DOGE-USD | 17.38 | — | entry signal |
| 2026-11-22T10:00 | RSI momentum · 1h | buy | BTC-USD | 17.38 | — | entry signal |
| 2026-11-22T10:00 | ROC + volume · 1h | buy | ETH-USD | 16.50 | — | entry signal |
| 2026-11-22T10:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.59 | — | entry signal |
| 2026-11-22T10:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.59 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-24 14:20:05.000139+00:00 -> 2026-11-22 14:30:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
