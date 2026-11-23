# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T10:45:05.000751+00:00 · 70479 ticks

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

Today: 8000 decisions in 1603 calls, $0.1118 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T10:45 | 2 / 3 / 0 | XRP-USD 14% |  |
| Breezy | 2026-11-23T10:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T10:45 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.74 | +6.88% | 7 |
| VWAP momentum · 1h | SQQQ | 1.62 | +25.81% | 4 |
| Opening range 15m | SQQQ | 1.59 | +21.11% | 6 |
| Stochastic reversion | SQQQ | 1.47 | +7.85% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.65 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.17 | 14.17 | 0 | — | 12.16 | 4.58 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.33 | 1.33 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.37 | -2.43 | -2.96 | 67 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.21 | 0.49 | -7.48 | 143 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.66 | -3.85 | -9.77 | 34 |
| 15 | Daily: Bullish score | daily | 90.88 | -9.12 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 16 | Hold SPY | benchmark | 90.72 | -9.29 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 17 | Squeeze breakout · 1h | breakout | 88.42 | -11.58 | 70 | 20.0 | -16.38 | -7.17 | -19.12 | 73 |
| 18 | VWAP reversion · 1h | reversion | 87.79 | -12.21 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 87.72 | -12.28 | 56 | 39.3 | -19.63 | -3.91 | -22.56 | 66 |
| 20 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 87.32 | -12.68 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.73 | -14.27 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.39 | -15.61 | 197 | 27.4 | -23.17 | -6.17 | -27.61 | 194 |
| 26 | Donchian 55/20 · 1h | breakout | 81.76 | -18.24 | 79 | 12.7 | -23.32 | -6.39 | -26.62 | 82 |
| 27 | Volume breakout · 1h | breakout | 81.62 | -18.38 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.17 | -4.85 | -21.94 | 199 |
| 29 | Connors RSI(2) · 1h | reversion | 79.76 | -20.24 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 30 | Keltner breakout · 1h | breakout | 79.76 | -20.24 | 128 | 25.8 | -22.24 | -6.39 | -23.87 | 139 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.76 | -4.11 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 77.18 | -22.82 | 108 | 13.9 | -26.39 | -7.00 | -31.39 | 109 |
| 34 | Supertrend · 1h | trend | 74.24 | -25.76 | 198 | 16.7 | -32.06 | -6.05 | -37.64 | 204 |
| 35 | ADX DI cross · 1h | trend | 74.21 | -25.79 | 234 | 20.1 | -31.19 | -5.78 | -35.87 | 276 |
| 36 | Max aggression: 1-day momentum | meta | 72.85 | -27.15 | 33 | 27.3 | -50.88 | -3.79 | -57.07 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.77 | -27.23 | 161 | 14.3 | -31.94 | -7.65 | -36.13 | 170 |
| 38 | EMA 20/50 cross · 1h | trend | 72.76 | -27.24 | 119 | 10.1 | -35.53 | -9.46 | -40.43 | 126 |
| 39 | Bollinger breakout · 1h | breakout | 70.92 | -29.08 | 201 | 20.9 | -32.57 | -8.48 | -34.47 | 212 |
| 40 | Hold BTC | benchmark | 70.82 | -29.18 | 3 | 0.0 | -29.03 | -5.16 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 69.70 | -30.30 | 318 | 19.5 | -36.29 | -9.17 | -40.10 | 235 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.08 | -30.92 | 499 | 23.0 | -45.37 | -9.61 | -46.69 | 617 |
| 45 | RSI momentum · 1h | momentum | 69.07 | -30.93 | 187 | 13.9 | -36.74 | -7.96 | -39.81 | 205 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 388 | 40.2 | -43.29 | -6.11 | -43.89 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.79 | -9.55 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.91 | -34.09 | 171 | 17.0 | -39.22 | -8.68 | -41.67 | 194 |
| 50 | ROC + volume · 1h | momentum | 65.43 | -34.57 | 436 | 27.3 | -40.52 | -8.27 | -41.12 | 338 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.60 | -5.04 | -38.40 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.38 | -36.62 | 298 | 11.1 | -43.73 | -10.18 | -46.01 | 330 |
| 53 | MACD cross · 1h | trend | 61.01 | -38.99 | 460 | 21.1 | -49.58 | -9.71 | -49.99 | 508 |
| 54 | CCI reversion · 1h | reversion | 59.00 | -41.00 | 429 | 40.1 | -47.13 | -7.60 | -51.36 | 493 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.65 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.32 | -44.68 | 1031 | 21.6 | -58.66 | -13.45 | -60.47 | 1200 |
| 57 | Agent (ML meta-label) | meta | 55.02 | -44.98 | 2023 | 24.6 | -32.93 | -5.78 | -35.51 | 338 |
| 58 | Williams %R · 1h | reversion | 54.96 | -45.04 | 487 | 38.4 | -53.70 | -8.70 | -55.89 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.24 | -6.49 | -49.45 | 274 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.47 | -8.51 | -54.86 | 689 |
| 61 | Three white soldiers | momentum | 50.73 | -49.27 | 634 | 14.4 | -52.15 | -22.43 | -52.33 | 656 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -48.72 | -99.14 | 5372 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.58 | -35.55 | -84.68 | 1424 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.62 | -50.48 | -94.65 | 2456 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.04 | -32.25 | -91.10 | 1948 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.68 | -40.53 | -91.72 | 2277 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.46 | -27.95 | -89.48 | 1961 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -48.13 | -98.16 | 3466 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -53.28 | -97.01 | 3397 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -38.68 | -93.70 | 2188 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.61 | -35.96 | -83.76 | 1568 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.59 | -99.66 | 6341 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -39.99 | -92.91 | 2521 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.34 | -36.31 | -94.34 | 3130 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -64.14 | -99.83 | 6250 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.48 | -45.10 | -93.49 | 2282 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.78 | -24.44 | -79.09 | 1637 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -57.10 | -97.79 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -58.16 | -99.18 | 5134 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.60 | -28.07 | -70.82 | 1226 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.90 | -49.35 | -94.95 | 2719 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.77 | -6.18 | -49.04 | 269 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.46 | -37.14 | -85.62 | 1698 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.62 | -99.76 | 6569 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.70 | -30.87 | -91.74 | 2497 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.91 | -19.69 | -83.01 | 1966 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.10 | -30.65 | -92.19 | 2185 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -46.78 | -98.10 | 4079 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.12 | -47.44 | -90.24 | 2221 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.92 | -30.74 | -68.10 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.66 | -27.04 | -74.25 | 1189 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.75 | -18.70 | -83.84 | 1866 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.94 | -47.31 | -97.95 | 4468 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -94.68 | -99.94 | 8389 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-23T06:00 | MACD cross · 1h | buy | BTC-USD | 12.24 | — | entry signal |
| 2026-11-23T06:00 | MACD cross · 1h | sell | XRP-USD | 3.09 | 0.01 | rebalance down |
| 2026-11-23T06:00 | MACD cross · 1h | sell | SOL-USD | 3.07 | 0.00 | rebalance down |
| 2026-11-23T06:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 7.32 | — | entry signal |
| 2026-11-23T06:00 | EMA 20/50 cross · 1h | sell | ETH-USD | 3.65 | 0.01 | rebalance down |
| 2026-11-23T06:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 3.67 | 0.02 | rebalance down |
| 2026-11-23T05:00 | CCI reversion · 1h | sell | XRP-USD | 14.67 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 10:45:05.000751+00:00 -> 2026-11-23 10:55:05.000751+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
