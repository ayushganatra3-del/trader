# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T02:15:05.000125+00:00 · 70060 ticks

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

Today: 1730 decisions in 346 calls, $0.0243 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T02:15 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-23T02:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T02:15 | 4 / 1 / 0 | ETH-USD 53% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.28 | 14.28 | 0 | — | 12.18 | 4.59 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.40 | 1.40 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.33 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.52 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -7.41 | -4.09 | -10.21 | 36 |
| 15 | Daily: Bullish score | daily | 90.89 | -9.11 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 16 | Hold SPY | benchmark | 90.78 | -9.22 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 17 | Squeeze breakout · 1h | breakout | 88.41 | -11.59 | 70 | 20.0 | -16.87 | -7.48 | -18.95 | 72 |
| 18 | VWAP reversion · 1h | reversion | 87.82 | -12.18 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 87.78 | -12.22 | 56 | 39.3 | -14.13 | -2.73 | -18.60 | 65 |
| 20 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 87.38 | -12.62 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.79 | -14.21 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.02 | -15.97 | 196 | 27.6 | -23.47 | -6.26 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.83 | -18.17 | 79 | 12.7 | -23.29 | -6.38 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.64 | -18.36 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.59 | -4.94 | -21.36 | 199 |
| 29 | Keltner breakout · 1h | breakout | 80.13 | -19.87 | 126 | 26.2 | -22.55 | -6.48 | -24.07 | 138 |
| 30 | Connors RSI(2) · 1h | reversion | 79.78 | -20.22 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.92 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.51 | -23.49 | 108 | 13.9 | -27.09 | -7.25 | -31.39 | 108 |
| 34 | ADX DI cross · 1h | trend | 74.08 | -25.92 | 234 | 20.1 | -31.33 | -5.82 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 73.56 | -26.45 | 198 | 16.7 | -32.96 | -6.29 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 72.90 | -27.10 | 33 | 27.3 | -50.89 | -3.79 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.48 | -27.52 | 161 | 14.3 | -32.11 | -7.69 | -36.16 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.17 | -27.83 | 119 | 10.1 | -35.85 | -9.63 | -40.32 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 71.32 | -28.68 | 199 | 21.1 | -33.98 | -8.84 | -35.59 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 41 | Hold BTC | benchmark | 70.29 | -29.71 | 3 | 0.0 | -29.15 | -5.18 | -36.21 | 1 |
| 42 | OBV trend · 1h | momentum | 69.79 | -30.21 | 316 | 19.6 | -36.18 | -9.13 | -40.13 | 232 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.35 | -30.65 | 498 | 23.1 | -45.23 | -9.57 | -46.74 | 615 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 46 | RSI momentum · 1h | momentum | 68.83 | -31.17 | 187 | 13.9 | -36.99 | -8.03 | -39.81 | 202 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.39 | -6.12 | -43.99 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.77 | -9.54 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.93 | -34.07 | 170 | 17.1 | -40.85 | -9.09 | -42.59 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.73 | -34.27 | 434 | 27.4 | -41.08 | -8.56 | -41.93 | 337 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.58 | -5.04 | -38.38 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 62.95 | -37.05 | 297 | 11.1 | -44.18 | -10.36 | -46.01 | 328 |
| 53 | MACD cross · 1h | trend | 61.13 | -38.87 | 459 | 21.1 | -49.64 | -9.73 | -49.94 | 505 |
| 54 | CCI reversion · 1h | reversion | 58.68 | -41.32 | 426 | 39.9 | -47.43 | -7.68 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.67 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.35 | -44.65 | 1031 | 21.6 | -58.66 | -13.48 | -60.42 | 1198 |
| 57 | Agent (ML meta-label) | meta | 55.05 | -44.95 | 2023 | 24.6 | -32.97 | -6.18 | -35.90 | 346 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.62 | -8.66 | -55.86 | 588 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.20 | -6.48 | -49.45 | 275 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.46 | -22.38 | -52.48 | 658 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.33 | -8.50 | -54.68 | 688 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -48.04 | -99.13 | 5353 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.56 | -35.57 | -84.63 | 1425 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.67 | -48.64 | -94.70 | 2459 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.16 | -32.65 | -91.26 | 1950 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -40.99 | -91.81 | 2280 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.62 | -28.37 | -89.62 | 1973 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -47.53 | -98.21 | 3478 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -53.85 | -96.91 | 3387 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.45 | -37.97 | -93.45 | 2170 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.44 | -35.00 | -83.59 | 1566 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -53.86 | -99.67 | 6351 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.75 | -39.18 | -92.88 | 2515 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.40 | -36.61 | -94.40 | 3141 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.32 | -99.83 | 6260 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.47 | -44.32 | -93.48 | 2283 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.70 | -23.93 | -79.01 | 1632 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -56.45 | -97.80 | 3354 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -57.44 | -99.18 | 5134 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.39 | -27.36 | -70.53 | 1221 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.81 | -47.49 | -94.88 | 2710 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.07 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.40 | -36.37 | -85.55 | 1693 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.57 | -99.76 | 6574 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.69 | -30.92 | -91.70 | 2496 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.09 | -19.89 | -83.16 | 1969 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.33 | -31.78 | -92.36 | 2196 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.10 | -46.52 | -98.10 | 4081 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -47.61 | -90.31 | 2220 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.62 | -30.08 | -67.83 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.67 | -27.05 | -74.36 | 1190 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.63 | -18.42 | -83.78 | 1864 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.94 | -46.97 | -97.94 | 4470 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.41 | -99.94 | 8384 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T02:05 | RSI momentum · 1h | sell | DOGE-USD | 17.00 | -0.38 | target is flat |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | SOL-USD | 13.80 | -0.06 | exit signal |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | ETH-USD | 13.81 | -0.01 | exit signal |
| 2026-11-23T02:00 | VWAP momentum · 1h | sell | BTC-USD | 13.79 | 0.02 | exit signal |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | SOL-USD | 3.38 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | ETH-USD | 7.01 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | buy | BTC-USD | 7.01 | — | rebalance up |
| 2026-11-23T02:00 | Parabolic SAR · 1h | sell | XRP-USD | 3.55 | -0.10 | exit signal |
| 2026-11-23T02:00 | Parabolic SAR · 1h | sell | DOGE-USD | 13.85 | -0.30 | exit signal |
| 2026-11-23T02:00 | MACD zero-line · 1h | sell | BTC-USD | 16.46 | -0.20 | exit signal |
| 2026-11-23T02:00 | MACD cross · 1h | sell | ETH-USD | 15.23 | -0.20 | exit signal |
| 2026-11-23T02:00 | MACD cross · 1h | sell | BTC-USD | 15.26 | -0.17 | exit signal |
| 2026-11-23T02:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 10.27 | — | rebalance up |
| 2026-11-23T02:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 10.36 | -0.18 | exit signal |
| 2026-11-23T01:20 | MACD cross · 1h | buy | BTC-USD | 3.07 | — | rebalance up |
| 2026-11-23T01:00 | OBV trend · 1h | buy | SOL-USD | 17.43 | — | entry signal |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.61 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | ETH-USD | 4.56 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | buy | BTC-USD | 4.51 | — | rebalance up |
| 2026-11-23T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.24 | -0.02 | exit signal |
| 2026-11-23T01:00 | Ichimoku · 1h | sell | XRP-USD | 16.02 | -0.09 | exit signal |
| 2026-11-23T01:00 | MACD cross · 1h | buy | ETH-USD | 3.10 | — | rebalance up |
| 2026-11-23T01:00 | MACD cross · 1h | sell | DOGE-USD | 7.27 | -0.07 | exit signal |
| 2026-11-23T00:05 | MACD cross · 1h | buy | DOGE-USD | 7.35 | — | entry |
| 2026-11-23T00:05 | MACD cross · 1h | sell | ETH-USD | 3.13 | -0.01 | rebalance down |
| 2026-11-23T00:05 | MACD cross · 1h | sell | BTC-USD | 3.11 | -0.01 | rebalance down |
| 2026-11-23T00:00 | MACD cross · 1h | buy | SOL-USD | 15.44 | — | entry signal |
| 2026-11-23T00:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 17.19 | — | entry signal |
| 2026-11-22T23:00 | OBV trend · 1h | buy | BTC-USD | 17.57 | — | entry signal |
| 2026-11-22T23:00 | VWAP momentum · 1h | sell | XRP-USD | 4.44 | -0.05 | exit signal |
| 2026-11-22T23:00 | Ichimoku · 1h | buy | XRP-USD | 16.11 | — | entry signal |
| 2026-11-22T23:00 | MACD zero-line · 1h | sell | DOGE-USD | 16.45 | -0.22 | exit signal |
| 2026-11-22T23:00 | MACD cross · 1h | buy | ETH-USD | 5.06 | — | rebalance up |
| 2026-11-22T23:00 | MACD cross · 1h | buy | BTC-USD | 5.08 | — | rebalance up |
| 2026-11-22T23:00 | MACD cross · 1h | sell | SOL-USD | 12.27 | -0.10 | exit signal |
| 2026-11-22T23:00 | MACD cross · 1h | sell | DOGE-USD | 10.26 | -0.13 | exit signal |
| 2026-11-22T22:00 | ROC + volume · 1h | sell | BTC-USD | 16.39 | -0.07 | exit signal |
| 2026-11-22T22:00 | MACD cross · 1h | buy | SOL-USD | 12.37 | — | entry signal |
| 2026-11-22T22:00 | MACD cross · 1h | sell | XRP-USD | 12.31 | -0.11 | exit signal |
| 2026-11-22T21:00 | MACD zero-line · 1h | sell | SOL-USD | 16.43 | -0.23 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 02:15:05.000125+00:00 -> 2026-11-23 02:25:05.000125+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
