# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T01:15:05.000120+00:00 · 70014 ticks

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

Today: 1040 decisions in 208 calls, $0.0146 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T01:15 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-23T01:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T01:15 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.58 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.37 | -2.43 | -2.96 | 67 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.21 | 0.49 | -7.48 | 143 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.64 | -3.97 | -9.46 | 34 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -16.98 | -7.51 | -18.95 | 72 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -14.12 | -2.73 | -18.60 | 65 |
| 19 | VWAP reversion · 1h | reversion | 87.90 | -12.10 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.50 | -15.50 | 194 | 27.8 | -23.09 | -6.15 | -27.61 | 191 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -23.29 | -6.38 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Keltner breakout · 1h | breakout | 80.40 | -19.60 | 126 | 26.2 | -22.39 | -6.42 | -24.07 | 138 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.17 | -4.85 | -21.94 | 199 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -24.77 | -4.11 | -25.44 | 94 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.77 | -23.23 | 108 | 13.9 | -26.95 | -7.21 | -31.39 | 108 |
| 34 | ADX DI cross · 1h | trend | 74.22 | -25.78 | 234 | 20.1 | -31.26 | -5.80 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 73.87 | -26.13 | 198 | 16.7 | -32.79 | -6.25 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -50.88 | -3.79 | -57.07 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.73 | -27.27 | 161 | 14.3 | -31.82 | -7.55 | -36.10 | 167 |
| 38 | EMA 20/50 cross · 1h | trend | 72.51 | -27.49 | 119 | 10.1 | -35.64 | -9.54 | -40.32 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 71.56 | -28.44 | 199 | 21.1 | -33.84 | -8.79 | -35.58 | 213 |
| 40 | Hold BTC | benchmark | 70.70 | -29.30 | 3 | 0.0 | -28.95 | -5.14 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 70.12 | -29.88 | 316 | 19.6 | -35.98 | -9.06 | -40.13 | 232 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.39 | -30.61 | 498 | 23.1 | -45.23 | -9.57 | -46.74 | 615 |
| 45 | RSI momentum · 1h | momentum | 69.20 | -30.80 | 186 | 14.0 | -36.82 | -8.02 | -39.81 | 202 |
| 46 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 387 | 40.3 | -43.39 | -6.12 | -43.99 | 448 |
| 48 | Donchian 20/10 · 1h | breakout | 66.16 | -33.84 | 170 | 17.1 | -40.73 | -9.05 | -42.59 | 195 |
| 49 | MACD zero-line · 1h | trend | 66.14 | -33.86 | 197 | 16.8 | -34.66 | -9.49 | -35.13 | 210 |
| 50 | ROC + volume · 1h | momentum | 65.86 | -34.14 | 434 | 27.4 | -41.37 | -8.49 | -42.27 | 338 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.60 | -5.04 | -38.40 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.27 | -36.73 | 296 | 11.1 | -43.98 | -10.28 | -46.01 | 328 |
| 53 | MACD cross · 1h | trend | 61.51 | -38.49 | 457 | 21.2 | -49.38 | -9.65 | -49.82 | 505 |
| 54 | CCI reversion · 1h | reversion | 58.81 | -41.19 | 426 | 39.9 | -47.36 | -7.66 | -51.36 | 492 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.55 | -6.67 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.74 | -44.26 | 1028 | 21.6 | -58.46 | -13.38 | -60.44 | 1198 |
| 57 | Agent (ML meta-label) | meta | 55.14 | -44.86 | 2023 | 24.6 | -28.74 | -5.02 | -32.52 | 333 |
| 58 | Williams %R · 1h | reversion | 55.03 | -44.97 | 485 | 38.4 | -53.67 | -8.68 | -55.91 | 589 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.47 | -6.52 | -49.45 | 279 |
| 60 | Three white soldiers | momentum | 50.98 | -49.02 | 632 | 14.4 | -52.43 | -22.40 | -52.45 | 658 |
| 61 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -52.02 | -8.61 | -55.32 | 690 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -47.97 | -99.13 | 5353 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.52 | -35.38 | -84.59 | 1425 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.66 | -48.47 | -94.69 | 2459 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.13 | -32.53 | -91.26 | 1950 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -40.86 | -91.81 | 2280 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -28.32 | -89.67 | 1978 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.21 | -47.31 | -98.23 | 3480 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.94 | -52.33 | -96.96 | 3392 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -37.48 | -93.46 | 2171 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.41 | -34.80 | -83.56 | 1565 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -52.87 | -99.66 | 6352 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -39.11 | -92.88 | 2515 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.40 | -36.60 | -94.40 | 3142 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.18 | -99.83 | 6262 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.47 | -44.32 | -93.48 | 2283 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.73 | -23.84 | -79.08 | 1633 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -56.19 | -97.79 | 3353 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -56.60 | -99.18 | 5133 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.32 | -27.37 | -70.59 | 1222 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.80 | -47.42 | -94.88 | 2710 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.07 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.40 | -36.37 | -85.56 | 1693 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -68.14 | -99.76 | 6572 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.66 | -30.64 | -91.67 | 2498 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.07 | -19.86 | -83.21 | 1972 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.32 | -31.87 | -92.34 | 2192 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.09 | -46.09 | -98.09 | 4082 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.21 | -47.32 | -90.32 | 2221 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.62 | -30.08 | -67.83 | 799 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.67 | -27.05 | -74.36 | 1190 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.67 | -18.60 | -83.84 | 1863 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.92 | -46.42 | -97.92 | 4467 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.49 | -99.94 | 8391 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-22T21:00 | MACD cross · 1h | buy | XRP-USD | 6.05 | — | rebalance up |
| 2026-11-22T21:00 | MACD cross · 1h | sell | SOL-USD | 10.26 | -0.14 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 01:15:05.000120+00:00 -> 2026-11-23 01:25:05.000120+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
