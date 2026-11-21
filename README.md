# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-21T02:20:05.000115+00:00 · 67572 ticks

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

Today: 1905 decisions in 381 calls, $0.0266 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-21T02:20 | 2 / 0 / 3 | cash |  |
| Breezy | 2026-11-21T02:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-21T02:20 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.07 | +6.48% | 13 |
| Squeeze breakout | SQQQ | 1.82 | +7.13% | 8 |
| VWAP momentum · 1h | SQQQ | 1.76 | +27.55% | 6 |
| Opening range 30m | SQQQ | 1.44 | +19.43% | 6 |
| Opening range 15m | SQQQ | 1.43 | +19.52% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.46 | 14.46 | 0 | — | 12.16 | 4.07 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.58 | 1.58 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.59 | 0.27 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.85 | -4.19 | -5.43 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.66 | 0.31 | -7.76 | 152 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -9.71 | -5.05 | -12.45 | 51 |
| 15 | Hold SPY | benchmark | 90.94 | -9.05 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 16 | Daily: Bullish score | daily | 90.94 | -9.06 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 17 | Squeeze breakout · 1h | breakout | 88.45 | -11.55 | 70 | 20.0 | -13.93 | -4.60 | -20.27 | 75 |
| 18 | Copy: Insider buying | copy | 87.94 | -12.06 | 56 | 39.3 | -8.22 | -1.59 | -14.79 | 66 |
| 19 | VWAP reversion · 1h | reversion | 87.77 | -12.23 | 160 | 45.0 | -14.66 | -4.24 | -20.40 | 156 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 87.54 | -12.46 | 0 | — | -12.95 | -3.21 | -13.87 | 1 |
| 21 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.95 | -14.05 | 0 | — | -14.84 | -3.84 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.90 | -15.10 | 194 | 27.8 | -23.69 | -6.37 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.87 | -18.12 | 79 | 12.7 | -24.30 | -6.76 | -28.01 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.68 | -18.32 | 163 | 28.8 | -16.48 | -5.37 | -21.55 | 73 |
| 28 | Keltner breakout · 1h | breakout | 80.53 | -19.47 | 126 | 26.2 | -19.34 | -4.85 | -25.05 | 141 |
| 29 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -21.63 | -5.04 | -22.26 | 204 |
| 30 | Connors RSI(2) · 1h | reversion | 79.81 | -20.19 | 218 | 40.4 | -15.04 | -6.78 | -15.07 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -25.05 | -4.20 | -25.48 | 96 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.83 | -23.17 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.04 | -26.96 | 33 | 27.3 | -48.95 | -3.41 | -58.27 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.97 | -27.03 | 195 | 21.5 | -28.42 | -5.84 | -36.37 | 212 |
| 37 | Supertrend · 1h | trend | 72.93 | -27.07 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.90 | -27.10 | 161 | 14.3 | -32.53 | -7.79 | -37.44 | 171 |
| 39 | EMA 20/50 cross · 1h | trend | 72.59 | -27.41 | 119 | 10.1 | -35.74 | -9.72 | -40.64 | 122 |
| 40 | Heikin-Ashi · 1h | trend | 70.88 | -29.12 | 485 | 22.9 | -44.01 | -8.93 | -47.85 | 620 |
| 41 | RSI momentum · 1h | momentum | 70.70 | -29.30 | 184 | 14.1 | -36.95 | -7.99 | -40.97 | 201 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 43 | OBV trend · 1h | momentum | 70.32 | -29.68 | 316 | 19.6 | -36.96 | -9.45 | -41.22 | 238 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | Hold BTC | benchmark | 68.22 | -31.78 | 3 | 0.0 | -27.06 | -4.47 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 165 | 17.6 | -34.80 | -6.39 | -43.26 | 191 |
| 49 | Stochastic reversion · 1h | reversion | 66.91 | -33.09 | 378 | 39.9 | -43.21 | -6.14 | -43.86 | 445 |
| 50 | ROC + volume · 1h | momentum | 66.42 | -33.58 | 431 | 27.6 | -37.54 | -6.53 | -43.73 | 341 |
| 51 | EMA 9/21 cross · 1h | trend | 64.80 | -35.20 | 291 | 11.3 | -42.42 | -9.85 | -46.01 | 318 |
| 52 | MFI reversion · 1h | reversion | 64.76 | -35.24 | 476 | 33.0 | -34.72 | -5.22 | -36.23 | 175 |
| 53 | MACD cross · 1h | trend | 63.01 | -36.99 | 444 | 20.9 | -49.72 | -9.93 | -51.09 | 497 |
| 54 | CCI reversion · 1h | reversion | 62.20 | -37.80 | 413 | 40.4 | -46.88 | -7.64 | -48.16 | 484 |
| 55 | Bollinger reversion · 1h | reversion | 58.22 | -41.78 | 377 | 36.6 | -44.26 | -6.66 | -45.16 | 444 |
| 56 | Williams %R · 1h | reversion | 57.53 | -42.47 | 470 | 38.5 | -52.77 | -8.67 | -53.06 | 582 |
| 57 | RSI(14) reversion · 1h | reversion | 55.36 | -44.64 | 225 | 32.9 | -43.27 | -6.32 | -46.29 | 271 |
| 58 | Agent (ML meta-label) | meta | 55.26 | -44.74 | 2005 | 24.6 | -30.24 | -5.27 | -31.85 | 321 |
| 59 | VWAP momentum · 1h | momentum | 54.99 | -45.01 | 1015 | 21.4 | -56.58 | -11.60 | -60.99 | 1201 |
| 60 | Z-score reversion · 1h | reversion | 52.02 | -47.98 | 242 | 33.1 | -43.87 | -6.04 | -46.40 | 270 |
| 61 | Three white soldiers | momentum | 51.39 | -48.61 | 621 | 14.0 | -52.63 | -22.31 | -52.96 | 670 |
| 62 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -53.63 | -9.54 | -53.93 | 680 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.15 | -47.42 | -99.15 | 5358 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.55 | -29.70 | -84.15 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -45.65 | -94.51 | 2459 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.15 | -33.23 | -91.39 | 1953 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.03 | -42.36 | -92.21 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.85 | -27.62 | -90.17 | 2022 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -47.14 | -98.25 | 3494 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.87 | -52.54 | -96.89 | 3407 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.79 | -39.97 | -93.92 | 2197 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.72 | -34.67 | -83.72 | 1588 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -52.00 | -99.66 | 6349 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.17 | -42.45 | -93.17 | 2538 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.56 | -36.59 | -94.60 | 3156 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.84 | -65.37 | -99.84 | 6291 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.56 | -43.58 | -93.56 | 2292 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -79.61 | -24.69 | -79.79 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.87 | -58.27 | -97.87 | 3392 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.14 | -55.11 | -99.14 | 5119 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.95 | -28.84 | -71.03 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.07 | -51.25 | -95.08 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.71 | -37.95 | -85.93 | 1708 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.73 | -65.22 | -99.73 | 6553 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.50 | -30.73 | -91.60 | 2480 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.75 | -18.97 | -81.95 | 1942 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.63 | -32.64 | -92.64 | 2204 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.87 | -44.73 | -97.87 | 4046 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.38 | -49.68 | -90.46 | 2204 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.33 | -31.13 | -67.49 | 793 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.85 | -27.34 | -74.90 | 1205 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.23 | -18.88 | -83.52 | 1850 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.71 | -44.52 | -97.72 | 4441 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -93.95 | -99.95 | 8435 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-21T02:15 | MFI reversion · 1h | sell | SOL-USD | 5.35 | -0.04 | rebalance down |
| 2026-11-21T02:00 | MFI reversion · 1h | buy | ETH-USD | 9.73 | — | entry signal |
| 2026-11-21T02:00 | MFI reversion · 1h | sell | XRP-USD | 3.26 | -0.02 | rebalance down |
| 2026-11-21T02:00 | MFI reversion · 1h | sell | DOGE-USD | 3.26 | -0.01 | rebalance down |
| 2026-11-21T02:00 | VWAP reversion · 1h | sell | XRP-USD | 21.92 | -0.12 | exit signal |
| 2026-11-21T02:00 | VWAP momentum · 1h | buy | XRP-USD | 13.50 | — | entry signal |
| 2026-11-21T02:00 | VWAP momentum · 1h | buy | ETH-USD | 13.79 | — | entry signal |
| 2026-11-21T02:00 | VWAP momentum · 1h | sell | SOL-USD | 13.55 | -0.11 | exit signal |
| 2026-11-21T02:00 | VWAP momentum · 1h | sell | BTC-USD | 13.73 | -0.08 | exit signal |
| 2026-11-21T02:00 | Heikin-Ashi · 1h | sell | XRP-USD | 15.10 | -0.08 | exit signal |
| 2026-11-21T02:00 | MACD cross · 1h | buy | DOGE-USD | 15.76 | — | entry signal |
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | XRP-USD | 12.68 | -0.14 | Kill switch: down 50% from peak |
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | ETH-USD | 12.72 | -0.10 | Kill switch: down 50% from peak |
| 2026-11-21T01:35 | Candlestick reversal · 1h | sell | DOGE-USD | 12.74 | -0.09 | Kill switch: down 50% from peak |
| 2026-11-21T01:20 | MFI reversion · 1h | buy | SOL-USD | 3.25 | — | rebalance up |
| 2026-11-21T01:15 | MFI reversion · 1h | buy | XRP-USD | 3.28 | — | rebalance up |
| 2026-11-21T01:15 | MFI reversion · 1h | buy | DOGE-USD | 3.25 | — | rebalance up |
| 2026-11-21T01:00 | VWAP reversion · 1h | buy | XRP-USD | 7.12 | — | rebalance up |
| 2026-11-21T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 14.87 | 0.03 | exit signal |
| 2026-11-21T01:00 | VWAP reversion · 1h | sell | BTC-USD | 14.63 | 0.03 | exit signal |
| 2026-11-21T01:00 | Z-score reversion · 1h | buy | ETH-USD | 8.67 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | SOL-USD | 13.66 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.81 | — | entry signal |
| 2026-11-21T01:00 | VWAP momentum · 1h | buy | BTC-USD | 13.81 | — | entry signal |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | XRP-USD | 7.03 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | ETH-USD | 3.56 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 3.55 | — | rebalance up |
| 2026-11-21T01:00 | Heikin-Ashi · 1h | sell | SOL-USD | 14.14 | -0.06 | exit signal |
| 2026-11-21T00:00 | Hold BTC | buy | BTC-USD | 68.38 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | XRP-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | SOL-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | DOGE-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | MFI reversion · 1h | buy | BTC-USD | 12.99 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | XRP-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | SOL-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | ETH-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | DOGE-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | CCI reversion · 1h | buy | BTC-USD | 12.46 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | XRP-USD | 11.53 | — | entry |
| 2026-11-21T00:00 | Williams %R · 1h | buy | SOL-USD | 11.53 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-23 02:20:05.000115+00:00 -> 2026-11-21 02:30:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
