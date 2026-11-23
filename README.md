# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T12:45:05.000129+00:00 · 70593 ticks

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
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 9698 decisions in 1945 calls, $0.1355 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T12:45 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-23T12:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T12:45 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.80% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.65 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.34 | 14.35 | 0 | — | 12.18 | 4.59 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.46 | 1.46 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.33 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.52 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.88 | -3.67 | -9.02 | 32 |
| 15 | Daily: Bullish score | daily | 90.91 | -9.09 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 16 | Hold SPY | benchmark | 90.83 | -9.17 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 17 | Squeeze breakout · 1h | breakout | 88.43 | -11.57 | 70 | 20.0 | -16.04 | -7.04 | -18.73 | 72 |
| 18 | VWAP reversion · 1h | reversion | 87.84 | -12.16 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 87.83 | -12.17 | 56 | 39.3 | -19.64 | -3.92 | -22.56 | 66 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.43 | -12.57 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.84 | -14.16 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.40 | -15.60 | 197 | 27.4 | -23.25 | -6.19 | -27.61 | 194 |
| 26 | Donchian 55/20 · 1h | breakout | 81.76 | -18.24 | 79 | 12.7 | -23.39 | -6.42 | -26.62 | 82 |
| 27 | Volume breakout · 1h | breakout | 81.65 | -18.35 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.59 | -4.94 | -21.36 | 199 |
| 29 | Connors RSI(2) · 1h | reversion | 79.79 | -20.21 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 30 | Keltner breakout · 1h | breakout | 79.76 | -20.24 | 128 | 25.8 | -21.92 | -6.28 | -23.52 | 138 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.92 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 77.17 | -22.83 | 108 | 13.9 | -26.57 | -7.07 | -31.39 | 110 |
| 34 | Supertrend · 1h | trend | 74.28 | -25.72 | 198 | 16.7 | -32.18 | -6.09 | -37.64 | 204 |
| 35 | ADX DI cross · 1h | trend | 74.23 | -25.77 | 234 | 20.1 | -31.21 | -5.79 | -35.87 | 276 |
| 36 | Max aggression: 1-day momentum | meta | 72.95 | -27.05 | 33 | 27.3 | -50.89 | -3.79 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.80 | -27.20 | 161 | 14.3 | -31.98 | -7.63 | -36.10 | 170 |
| 38 | EMA 20/50 cross · 1h | trend | 72.78 | -27.22 | 119 | 10.1 | -35.59 | -9.54 | -40.35 | 126 |
| 39 | Bollinger breakout · 1h | breakout | 70.95 | -29.05 | 201 | 20.9 | -32.63 | -8.50 | -34.47 | 212 |
| 40 | Hold BTC | benchmark | 70.83 | -29.18 | 3 | 0.0 | -29.16 | -5.19 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 69.72 | -30.28 | 318 | 19.5 | -36.44 | -9.25 | -40.12 | 235 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | RSI momentum · 1h | momentum | 69.10 | -30.90 | 187 | 13.9 | -36.69 | -7.91 | -39.81 | 205 |
| 45 | Heikin-Ashi · 1h | trend | 69.08 | -30.91 | 499 | 23.0 | -45.42 | -9.63 | -46.70 | 617 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 388 | 40.2 | -43.29 | -6.11 | -43.89 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.79 | -9.55 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.91 | -34.09 | 171 | 17.0 | -39.30 | -8.70 | -41.67 | 194 |
| 50 | ROC + volume · 1h | momentum | 65.45 | -34.55 | 436 | 27.3 | -40.17 | -8.33 | -40.75 | 337 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.58 | -5.04 | -38.38 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.40 | -36.60 | 298 | 11.1 | -43.74 | -10.19 | -46.01 | 330 |
| 53 | MACD cross · 1h | trend | 61.00 | -39.00 | 461 | 21.0 | -49.74 | -9.76 | -49.99 | 508 |
| 54 | CCI reversion · 1h | reversion | 59.00 | -41.00 | 429 | 40.1 | -47.13 | -7.60 | -51.36 | 493 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.65 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.34 | -44.66 | 1031 | 21.6 | -58.80 | -13.49 | -60.35 | 1198 |
| 57 | Agent (ML meta-label) | meta | 55.08 | -44.92 | 2023 | 24.6 | -32.95 | -5.91 | -35.76 | 338 |
| 58 | Williams %R · 1h | reversion | 54.96 | -45.04 | 487 | 38.4 | -53.60 | -8.69 | -55.79 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.04 | -6.44 | -49.45 | 273 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.18 | -8.24 | -53.65 | 683 |
| 61 | Three white soldiers | momentum | 50.64 | -49.36 | 635 | 14.3 | -52.36 | -22.59 | -52.50 | 657 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.14 | -48.98 | -99.15 | 5375 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.68 | -35.86 | -84.72 | 1429 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.65 | -50.66 | -94.68 | 2457 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.07 | -32.33 | -91.10 | 1948 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.72 | -40.75 | -91.76 | 2278 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.48 | -27.89 | -89.49 | 1961 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.17 | -48.70 | -98.18 | 3470 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -54.61 | -96.97 | 3392 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -38.94 | -93.68 | 2187 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.57 | -35.88 | -83.72 | 1566 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -54.00 | -99.66 | 6341 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -40.30 | -92.97 | 2521 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.40 | -36.54 | -94.40 | 3136 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -64.78 | -99.83 | 6247 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.52 | -45.46 | -93.52 | 2285 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.73 | -24.55 | -79.00 | 1633 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -57.15 | -97.79 | 3353 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -58.07 | -99.18 | 5134 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.66 | -28.22 | -70.85 | 1224 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -49.89 | -95.00 | 2718 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.77 | -6.18 | -49.04 | 269 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.60 | -37.52 | -85.71 | 1698 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.74 | -99.76 | 6572 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.69 | -30.90 | -91.73 | 2497 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -19.69 | -83.01 | 1966 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.12 | -30.67 | -92.21 | 2188 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -46.67 | -98.10 | 4078 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.17 | -47.72 | -90.28 | 2225 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.82 | -30.52 | -67.97 | 801 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.64 | -26.99 | -74.25 | 1188 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.83 | -18.68 | -83.91 | 1864 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.95 | -47.41 | -97.95 | 4470 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.57 | -99.94 | 8384 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T12:00 | Ichimoku · 1h | buy | DOGE-USD | 4.23 | — | entry signal |
| 2026-11-23T12:00 | Ichimoku · 1h | sell | SOL-USD | 4.23 | 0.10 | rebalance down |
| 2026-11-23T12:00 | Three white soldiers | sell | SOL-USD | 12.59 | -0.09 | exit signal |
| 2026-11-23T11:31 | Three white soldiers | buy | SOL-USD | 12.68 | — | entry signal |
| 2026-11-23T11:00 | MACD cross · 1h | buy | XRP-USD | 3.05 | — | rebalance up |
| 2026-11-23T11:00 | MACD cross · 1h | buy | DOGE-USD | 5.12 | — | rebalance up |
| 2026-11-23T11:00 | MACD cross · 1h | sell | BTC-USD | 12.11 | -0.13 | exit signal |
| 2026-11-23T10:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 17.11 | -0.22 | exit signal |
| 2026-11-23T09:35 | Three white soldiers | sell | BTC-USD | 12.60 | -0.11 | exit signal |
| 2026-11-23T09:15 | Three white soldiers | buy | BTC-USD | 12.71 | — | entry signal |
| 2026-11-23T09:00 | Keltner breakout · 1h | buy | SOL-USD | 19.96 | — | entry signal |
| 2026-11-23T09:00 | Triple EMA stack · 1h | buy | XRP-USD | 5.87 | — | entry |
| 2026-11-23T09:00 | Triple EMA stack · 1h | buy | DOGE-USD | 12.16 | — | entry signal |
| 2026-11-23T09:00 | Triple EMA stack · 1h | sell | SOL-USD | 6.01 | 0.04 | rebalance down |
| 2026-11-23T09:00 | Triple EMA stack · 1h | sell | ETH-USD | 6.01 | -0.03 | rebalance down |
| 2026-11-23T09:00 | Triple EMA stack · 1h | sell | BTC-USD | 6.01 | -0.03 | rebalance down |
| 2026-11-23T07:00 | Squeeze breakout · 1h | buy | SOL-USD | 22.09 | — | entry signal |
| 2026-11-23T07:00 | OBV trend · 1h | buy | DOGE-USD | 7.17 | — | entry signal |
| 2026-11-23T07:00 | OBV trend · 1h | sell | SOL-USD | 3.55 | 0.01 | rebalance down |
| 2026-11-23T07:00 | OBV trend · 1h | sell | BTC-USD | 3.62 | -0.01 | rebalance down |
| 2026-11-23T07:00 | EMA 20/50 cross · 1h | buy | DOGE-USD | 5.25 | — | entry signal |
| 2026-11-23T07:00 | EMA 20/50 cross · 1h | sell | SOL-USD | 5.25 | 0.05 | rebalance down |
| 2026-11-23T06:00 | CCI reversion · 1h | sell | DOGE-USD | 14.77 | 0.00 | exit signal |
| 2026-11-23T06:00 | Williams %R · 1h | sell | DOGE-USD | 13.76 | 0.00 | exit signal |
| 2026-11-23T06:00 | Bollinger breakout · 1h | buy | XRP-USD | 8.02 | — | entry signal |
| 2026-11-23T06:00 | Bollinger breakout · 1h | buy | DOGE-USD | 14.23 | — | entry signal |
| 2026-11-23T06:00 | Bollinger breakout · 1h | buy | BTC-USD | 14.23 | — | entry signal |
| 2026-11-23T06:00 | Bollinger breakout · 1h | sell | SOL-USD | 3.59 | 0.00 | rebalance down |
| 2026-11-23T06:00 | Donchian 55/20 · 1h | buy | XRP-USD | 20.46 | — | entry signal |
| 2026-11-23T06:00 | Donchian 55/20 · 1h | buy | SOL-USD | 20.46 | — | entry signal |
| 2026-11-23T06:00 | Donchian 20/10 · 1h | buy | XRP-USD | 14.06 | — | entry signal |
| 2026-11-23T06:00 | Donchian 20/10 · 1h | buy | SOL-USD | 16.51 | — | entry signal |
| 2026-11-23T06:00 | OBV trend · 1h | buy | XRP-USD | 17.04 | — | entry signal |
| 2026-11-23T06:00 | RSI momentum · 1h | buy | DOGE-USD | 11.38 | — | entry signal |
| 2026-11-23T06:00 | RSI momentum · 1h | sell | SOL-USD | 5.49 | 0.00 | rebalance down |
| 2026-11-23T06:00 | RSI momentum · 1h | sell | BTC-USD | 5.89 | 0.01 | rebalance down |
| 2026-11-23T06:00 | Heikin-Ashi · 1h | buy | XRP-USD | 14.46 | — | entry signal |
| 2026-11-23T06:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.34 | — | entry signal |
| 2026-11-23T06:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 17.34 | — | entry signal |
| 2026-11-23T06:00 | MACD cross · 1h | buy | DOGE-USD | 10.22 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 12:45:05.000129+00:00 -> 2026-11-23 12:55:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
