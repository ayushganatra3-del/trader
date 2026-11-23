# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T04:45:05.000136+00:00 · 70186 ticks

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

Today: 3620 decisions in 724 calls, $0.0507 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T04:45 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-11-23T04:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-23T04:45 | 1 / 4 / 0 | cash |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.25 | 14.26 | 0 | — | 12.18 | 4.59 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.11 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.33 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.38 | 1.38 | 0 | — | 2.38 | 0.40 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 0.83 | 0.35 | -9.06 | 203 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -2.27 | -2.33 | -2.86 | 68 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 1.30 | 0.52 | -7.48 | 144 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.54 | -7.54 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -6.64 | -3.97 | -9.46 | 34 |
| 15 | Daily: Bullish score | daily | 90.89 | -9.11 | 19 | 15.8 | -11.44 | -3.21 | -19.56 | 18 |
| 16 | Hold SPY | benchmark | 90.76 | -9.24 | 0 | — | -10.23 | -3.35 | -11.71 | 1 |
| 17 | Squeeze breakout · 1h | breakout | 88.40 | -11.60 | 70 | 20.0 | -17.38 | -7.62 | -19.29 | 73 |
| 18 | VWAP reversion · 1h | reversion | 87.81 | -12.19 | 161 | 45.3 | -15.19 | -4.39 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 87.76 | -12.24 | 56 | 39.3 | -14.13 | -2.73 | -18.60 | 65 |
| 20 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.96 | -14.87 | 552 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 87.36 | -12.63 | 0 | — | -12.95 | -3.18 | -13.87 | 1 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Copy: Congress Democrats (NANC) | copy | 85.77 | -14.23 | 0 | — | -14.84 | -3.97 | -17.03 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.79 | -26.65 | 7 |
| 25 | Parabolic SAR · 1h | trend | 84.13 | -15.87 | 197 | 27.4 | -23.39 | -6.24 | -27.61 | 193 |
| 26 | Donchian 55/20 · 1h | breakout | 81.83 | -18.17 | 79 | 12.7 | -23.29 | -6.38 | -26.62 | 80 |
| 27 | Volume breakout · 1h | breakout | 81.63 | -18.37 | 163 | 28.8 | -17.82 | -7.59 | -20.00 | 67 |
| 28 | Agent | meta | 80.18 | -19.82 | 238 | 36.1 | -20.58 | -4.93 | -21.36 | 199 |
| 29 | Keltner breakout · 1h | breakout | 79.86 | -20.14 | 128 | 25.8 | -22.70 | -6.53 | -24.34 | 139 |
| 30 | Connors RSI(2) · 1h | reversion | 79.77 | -20.23 | 218 | 40.4 | -15.04 | -6.71 | -15.06 | 70 |
| 31 | Agent (aggressive) | meta | 78.30 | -21.70 | 110 | 32.7 | -15.50 | -3.92 | -18.44 | 91 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.63 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.90 | -23.10 | 108 | 13.9 | -26.72 | -7.13 | -31.39 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.17 | -25.83 | 234 | 20.1 | -31.24 | -5.79 | -35.87 | 276 |
| 35 | Supertrend · 1h | trend | 74.05 | -25.95 | 198 | 16.7 | -32.39 | -6.14 | -37.64 | 204 |
| 36 | Max aggression: 1-day momentum | meta | 72.89 | -27.11 | 33 | 27.3 | -50.89 | -3.79 | -57.08 | 38 |
| 37 | Triple EMA stack · 1h | trend | 72.67 | -27.33 | 161 | 14.3 | -31.68 | -7.52 | -36.02 | 168 |
| 38 | EMA 20/50 cross · 1h | trend | 72.64 | -27.36 | 119 | 10.1 | -35.33 | -9.39 | -40.32 | 124 |
| 39 | Bollinger breakout · 1h | breakout | 71.01 | -28.99 | 201 | 20.9 | -34.23 | -8.93 | -35.57 | 214 |
| 40 | Hold BTC | benchmark | 70.64 | -29.36 | 3 | 0.0 | -28.81 | -5.11 | -36.21 | 1 |
| 41 | Copy: Cathie Wood (ARKK) | copy | 70.36 | -29.64 | 3 | 0.0 | -29.02 | -4.11 | -32.18 | 1 |
| 42 | OBV trend · 1h | momentum | 69.60 | -30.40 | 318 | 19.5 | -36.26 | -9.14 | -40.13 | 233 |
| 43 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.36 | -37.91 | 32 |
| 44 | Heikin-Ashi · 1h | trend | 69.35 | -30.65 | 498 | 23.1 | -45.23 | -9.57 | -46.74 | 615 |
| 45 | Max aggression: 5-day momentum | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.18 | -60.06 | 22 |
| 46 | RSI momentum · 1h | momentum | 68.98 | -31.02 | 187 | 13.9 | -36.82 | -7.98 | -39.81 | 203 |
| 47 | Stochastic reversion · 1h | reversion | 66.99 | -33.01 | 388 | 40.2 | -43.29 | -6.11 | -43.89 | 448 |
| 48 | MACD zero-line · 1h | trend | 66.00 | -34.00 | 198 | 16.7 | -34.77 | -9.54 | -35.13 | 210 |
| 49 | Donchian 20/10 · 1h | breakout | 65.91 | -34.09 | 171 | 17.0 | -40.89 | -9.09 | -42.62 | 195 |
| 50 | ROC + volume · 1h | momentum | 65.41 | -34.59 | 435 | 27.4 | -41.34 | -8.64 | -41.92 | 340 |
| 51 | MFI reversion · 1h | reversion | 64.88 | -35.12 | 484 | 33.1 | -34.58 | -5.04 | -38.38 | 180 |
| 52 | EMA 9/21 cross · 1h | trend | 63.20 | -36.80 | 298 | 11.1 | -43.96 | -10.27 | -46.01 | 330 |
| 53 | MACD cross · 1h | trend | 60.98 | -39.02 | 460 | 21.1 | -49.72 | -9.75 | -50.05 | 506 |
| 54 | CCI reversion · 1h | reversion | 58.98 | -41.02 | 427 | 40.0 | -47.14 | -7.61 | -51.36 | 493 |
| 55 | Bollinger reversion · 1h | reversion | 57.91 | -42.09 | 383 | 36.6 | -44.47 | -6.65 | -45.42 | 445 |
| 56 | VWAP momentum · 1h | momentum | 55.16 | -44.84 | 1031 | 21.6 | -58.80 | -13.54 | -60.42 | 1202 |
| 57 | Agent (ML meta-label) | meta | 55.04 | -44.96 | 2023 | 24.6 | -31.89 | -6.21 | -35.33 | 327 |
| 58 | Williams %R · 1h | reversion | 54.95 | -45.05 | 485 | 38.4 | -53.72 | -8.71 | -55.89 | 592 |
| 59 | RSI(14) reversion · 1h | reversion | 51.76 | -48.24 | 234 | 31.6 | -44.02 | -6.43 | -49.45 | 276 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.32 | -8.50 | -54.64 | 687 |
| 61 | Three white soldiers | momentum | 50.84 | -49.16 | 633 | 14.4 | -52.59 | -22.58 | -52.61 | 659 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.11 | -47.60 | -99.12 | 5353 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.69 | -36.02 | -84.75 | 1426 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.69 | -49.61 | -94.73 | 2463 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.08 | -32.39 | -91.20 | 1951 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -40.94 | -91.85 | 2284 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.36 | -27.80 | -89.36 | 1963 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.19 | -47.65 | -98.20 | 3478 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -55.17 | -96.96 | 3393 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -38.49 | -93.55 | 2178 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.49 | -35.46 | -83.67 | 1569 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -54.20 | -99.67 | 6342 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.73 | -39.20 | -92.84 | 2519 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.35 | -36.29 | -94.36 | 3134 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -63.26 | -99.83 | 6259 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.47 | -44.73 | -93.48 | 2285 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.74 | -24.12 | -79.02 | 1635 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -56.26 | -97.79 | 3352 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -58.10 | -99.18 | 5135 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.34 | -27.25 | -70.56 | 1222 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.83 | -47.83 | -94.89 | 2714 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.29 | -6.07 | -49.04 | 272 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.45 | -36.63 | -85.58 | 1697 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.92 | -99.76 | 6569 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.71 | -31.01 | -91.76 | 2500 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -83.06 | -19.85 | -83.15 | 1968 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.22 | -31.20 | -92.30 | 2193 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -46.98 | -98.12 | 4082 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.06 | -46.80 | -90.24 | 2218 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.94 | -30.81 | -68.02 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.82 | -27.34 | -74.28 | 1192 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.82 | -18.66 | -83.90 | 1865 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.95 | -47.58 | -97.96 | 4468 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.85 | -99.94 | 8389 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T04:00 | CCI reversion · 1h | buy | DOGE-USD | 14.77 | — | entry signal |
| 2026-11-23T04:00 | CCI reversion · 1h | sell | SOL-USD | 14.86 | 0.17 | exit signal |
| 2026-11-23T04:00 | Williams %R · 1h | buy | XRP-USD | 13.76 | — | entry signal |
| 2026-11-23T04:00 | Williams %R · 1h | buy | DOGE-USD | 13.76 | — | entry signal |
| 2026-11-23T04:00 | Bollinger breakout · 1h | buy | SOL-USD | 17.77 | — | entry signal |
| 2026-11-23T04:00 | OBV trend · 1h | buy | SOL-USD | 17.43 | — | entry signal |
| 2026-11-23T04:00 | RSI momentum · 1h | buy | SOL-USD | 17.00 | — | entry signal |
| 2026-11-23T04:00 | ROC + volume · 1h | buy | XRP-USD | 15.05 | — | entry signal |
| 2026-11-23T04:00 | ROC + volume · 1h | buy | ETH-USD | 16.41 | — | entry signal |
| 2026-11-23T04:00 | ROC + volume · 1h | buy | BTC-USD | 16.41 | — | entry signal |
| 2026-11-23T04:00 | VWAP momentum · 1h | buy | XRP-USD | 4.51 | — | entry signal |
| 2026-11-23T04:00 | VWAP momentum · 1h | buy | SOL-USD | 9.22 | — | entry signal |
| 2026-11-23T04:00 | VWAP momentum · 1h | buy | ETH-USD | 9.22 | — | entry signal |
| 2026-11-23T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 9.22 | — | entry signal |
| 2026-11-23T04:00 | VWAP momentum · 1h | buy | BTC-USD | 9.22 | — | entry signal |
| 2026-11-23T04:00 | Ichimoku · 1h | buy | XRP-USD | 16.02 | — | entry signal |
| 2026-11-23T04:00 | Parabolic SAR · 1h | buy | XRP-USD | 9.11 | — | entry signal |
| 2026-11-23T04:00 | Parabolic SAR · 1h | buy | SOL-USD | 16.87 | — | entry signal |
| 2026-11-23T04:00 | Parabolic SAR · 1h | sell | ETH-USD | 4.40 | 0.01 | rebalance down |
| 2026-11-23T04:00 | Parabolic SAR · 1h | sell | BTC-USD | 4.27 | -0.01 | rebalance down |
| 2026-11-23T04:00 | MACD cross · 1h | buy | SOL-USD | 15.26 | — | entry signal |
| 2026-11-23T04:00 | Triple EMA stack · 1h | buy | SOL-USD | 18.00 | — | entry signal |
| 2026-11-23T04:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 10.56 | — | entry signal |
| 2026-11-23T04:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.35 | 0.08 | rebalance down |
| 2026-11-23T04:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.28 | -0.01 | rebalance down |
| 2026-11-23T03:30 | Three white soldiers | sell | BTC-USD | 12.60 | -0.15 | stop-loss |
| 2026-11-23T03:25 | Three white soldiers | buy | BTC-USD | 12.75 | — | entry signal |
| 2026-11-23T03:05 | Stochastic reversion · 1h | sell | DOGE-USD | 4.78 | -0.01 | target is flat |
| 2026-11-23T03:00 | Stochastic reversion · 1h | buy | DOGE-USD | 4.79 | — | entry signal |
| 2026-11-23T03:00 | Keltner breakout · 1h | sell | ETH-USD | 19.84 | -0.30 | exit signal |
| 2026-11-23T03:00 | Keltner breakout · 1h | sell | BTC-USD | 19.80 | -0.33 | exit signal |
| 2026-11-23T03:00 | Bollinger breakout · 1h | sell | ETH-USD | 17.66 | -0.26 | exit signal |
| 2026-11-23T03:00 | Bollinger breakout · 1h | sell | BTC-USD | 17.62 | -0.30 | exit signal |
| 2026-11-23T03:00 | Donchian 20/10 · 1h | sell | ETH-USD | 16.32 | -0.24 | exit signal |
| 2026-11-23T03:00 | OBV trend · 1h | sell | SOL-USD | 17.15 | -0.28 | exit signal |
| 2026-11-23T03:00 | OBV trend · 1h | sell | ETH-USD | 17.31 | -0.27 | exit signal |
| 2026-11-23T03:00 | ROC + volume · 1h | sell | ETH-USD | 16.25 | -0.24 | exit signal |
| 2026-11-23T03:00 | Parabolic SAR · 1h | sell | SOL-USD | 17.30 | -0.23 | exit signal |
| 2026-11-23T03:00 | MACD cross · 1h | sell | SOL-USD | 15.21 | -0.22 | exit signal |
| 2026-11-23T03:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.18 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 04:45:05.000136+00:00 -> 2026-11-23 04:55:05.000136+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
