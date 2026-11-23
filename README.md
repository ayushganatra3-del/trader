# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T20:15:05.000138+00:00 · 70937 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.83 (-21.17%)

Closed trades 240, win rate 35.8%, fees £6.51, max drawdown -21.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 15.74 | -0.04 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-23 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, STWD 12%, ANAB 12%, FUN 12%, TEAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 45.25 · VIX 35.89 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 33380 decisions in 2977 calls, $0.4153 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T20:15 | 12 / 16 / 2 | cash |  |
| Breezy | 2026-11-23T20:15 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-23T20:15 | 7 / 22 / 1 | COIN 64% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.46 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.66 | 15.66 | 0 | — | 12.60 | 4.26 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.40 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.39 | 4.39 | 0 | — | 2.94 | 0.86 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.40 | -0.03 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.72 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.80 | -0.18 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.67 | -4.33 | 0 | — | -5.92 | -1.47 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.19 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.75 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.54 | -7.46 | 0 | — | -8.65 | -1.76 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.70 | -6.95 | -10.08 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.25 | -3.26 | -8.41 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.65 | -9.35 | 0 | — | -10.85 | -2.35 | -17.03 | 1 |
| 18 | VWAP reversion · 1h | reversion | 90.45 | -9.55 | 163 | 46.0 | -7.00 | -1.16 | -20.49 | 156 |
| 19 | Copy: Insider buying | copy | 89.31 | -10.70 | 57 | 40.4 | -18.38 | -3.58 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.28 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 86.96 | -13.04 | 9 | 44.4 | -10.67 | -0.56 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.64 | -13.37 | 457 | 33.3 | -12.91 | -4.31 | -14.39 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -16.55 | -3.77 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -20.50 | -6.75 | -21.26 | 81 |
| 25 | Connors RSI(2) · 1h | reversion | 80.83 | -19.17 | 220 | 40.9 | -13.90 | -6.02 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.58 | -19.43 | 203 | 28.1 | -27.99 | -7.56 | -30.34 | 190 |
| 27 | Agent | meta | 78.83 | -21.17 | 240 | 35.8 | -26.42 | -5.75 | -26.81 | 199 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -26.36 | -4.46 | -26.36 | 94 |
| 29 | Opening range 15m | breakout | 77.51 | -22.49 | 567 | 30.9 | -21.88 | -6.75 | -23.30 | 660 |
| 30 | Donchian 55/20 · 1h ⏸ | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.01 | -7.72 | -29.50 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.82 | -6.99 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.15 | -6.34 | -25.01 | 143 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.92 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 71.31 | -28.69 | 3 | 0.0 | -29.18 | -5.20 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.04 | -28.96 | 200 | 17.0 | -35.02 | -6.76 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.35 | -29.65 | 3 | 0.0 | -23.37 | -2.84 | -32.18 | 1 |
| 37 | Triple EMA stack · 1h | trend | 69.91 | -30.09 | 162 | 14.8 | -36.93 | -9.43 | -38.76 | 169 |
| 38 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -37.53 | -6.66 | -40.30 | 277 |
| 39 | EMA 20/50 cross · 1h | trend | 69.70 | -30.30 | 119 | 10.1 | -37.22 | -10.13 | -40.18 | 118 |
| 40 | Daily: Momentum burst | daily | 69.09 | -30.91 | 30 | 13.3 | -37.34 | -5.34 | -37.81 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.70 | -31.30 | 207 | 22.2 | -32.50 | -8.45 | -33.70 | 211 |
| 42 | Stochastic reversion · 1h | reversion | 66.98 | -33.02 | 394 | 40.9 | -34.00 | -3.61 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 66.89 | -33.11 | 320 | 19.7 | -39.29 | -9.99 | -40.77 | 234 |
| 44 | MACD zero-line · 1h | trend | 66.01 | -33.99 | 198 | 16.7 | -35.10 | -9.51 | -35.49 | 206 |
| 45 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -39.24 | -8.84 | -40.90 | 201 |
| 46 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.95 | -9.46 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum ⏸ | meta | 64.49 | -35.51 | 25 | 36.0 | -61.31 | -3.98 | -65.46 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.67 | -36.33 | 486 | 32.9 | -32.15 | -4.63 | -37.87 | 185 |
| 49 | Donchian 20/10 · 1h ⏸ | breakout | 62.04 | -37.97 | 178 | 18.0 | -39.25 | -8.39 | -41.23 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.61 | -8.57 | -42.87 | 344 |
| 51 | EMA 9/21 cross · 1h | trend | 60.06 | -39.94 | 299 | 11.4 | -44.24 | -10.32 | -45.46 | 332 |
| 52 | Agent (ML meta-label) | meta | 59.65 | -40.35 | 2048 | 25.0 | -12.09 | -1.28 | -25.18 | 314 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.10 | -3.85 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 59.01 | -40.99 | 466 | 21.2 | -49.33 | -9.43 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.15 | -41.85 | 430 | 40.0 | -49.47 | -8.16 | -52.09 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.87 | -42.13 | 391 | 37.6 | -37.77 | -4.51 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 54.14 | -45.86 | 500 | 38.4 | -54.79 | -8.99 | -56.11 | 588 |
| 58 | VWAP momentum · 1h | momentum | 53.55 | -46.45 | 1053 | 21.8 | -57.78 | -13.13 | -58.29 | 1179 |
| 59 | RSI(14) reversion · 1h | reversion | 51.09 | -48.91 | 240 | 31.7 | -49.87 | -7.89 | -52.23 | 291 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.82 | -8.64 | -54.67 | 667 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -47.82 | -99.13 | 5334 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.85 | -32.38 | -84.44 | 1433 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -47.25 | -94.50 | 2428 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -31.63 | -90.86 | 1915 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.77 | -40.41 | -91.80 | 2254 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.55 | -27.61 | -89.66 | 1959 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -47.30 | -98.16 | 3420 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.01 | -50.51 | -97.04 | 3371 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.64 | -37.65 | -93.64 | 2123 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.17 | -22.43 | -52.18 | 645 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.37 | -34.27 | -83.49 | 1559 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.27 | -99.67 | 6285 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.24 | -39.22 | -93.24 | 2492 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.46 | -35.36 | -94.46 | 3177 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.83 | -60.73 | -99.83 | 6135 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.17 | -42.33 | -93.35 | 2261 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.47 | -24.13 | -78.60 | 1615 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -54.67 | -97.79 | 3289 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -56.47 | -99.18 | 5121 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.86 | -27.55 | -70.87 | 1198 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -47.89 | -94.98 | 2672 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.76 | -6.16 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.60 | -36.99 | -85.60 | 1673 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -68.62 | -99.76 | 6547 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.45 | -29.44 | -91.69 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.84 | -19.80 | -82.96 | 1955 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.87 | -29.92 | -92.06 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -47.21 | -98.15 | 4055 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.20 | -46.14 | -90.31 | 2195 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.46 | -29.66 | -68.46 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.81 | -27.97 | -74.02 | 1169 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.35 | -19.14 | -84.47 | 1834 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.96 | -47.32 | -97.98 | 4414 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -89.55 | -99.94 | 8287 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T20:05 | Agent (ML meta-label) | buy | SQQQ | 14.91 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T20:00 | Agent (ML meta-label) | buy | BITX | 14.93 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | QQQ | 1.17 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | MSFT | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | AMZN | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | buy | AMD | 2.56 | — | entry |
| 2026-11-23T20:00 | MACD cross · 1h | sell | XRP-USD | 4.40 | 0.05 | exit signal |
| 2026-11-23T20:00 | MACD cross · 1h | sell | SOL-USD | 4.47 | 0.11 | exit signal |
| 2026-11-23T19:55 | Agent (ML meta-label) | sell | SQQQ | 14.79 | -0.09 | selected signal exited |
| 2026-11-23T19:55 | Agent (ML meta-label) | sell | BITX | 15.04 | 0.16 | selected signal exited |
| 2026-11-23T19:51 | VWAP momentum · 1h | sell | TQQQ | 4.12 | 0.00 | target is flat |
| 2026-11-23T19:46 | Agent (ML meta-label) | buy | SQQQ | 14.88 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T19:40 | Max aggression: 5-day momentum | sell | SOL-USD | 64.49 | -4.49 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Agent (ML meta-label) | buy | BITX | 14.88 | — | entry |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | XRP-USD | 15.48 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | SOL-USD | 15.42 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | NVDA | 12.60 | -0.32 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:40 | Donchian 20/10 · 1h | sell | BTC-USD | 15.51 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:35 | Agent (ML meta-label) | sell | SQQQ | 15.01 | -0.01 | selected signal exited |
| 2026-11-23T19:35 | Donchian 55/20 · 1h | sell | XRP-USD | 18.83 | -0.19 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:35 | Donchian 55/20 · 1h | sell | SOL-USD | 19.08 | 0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:30 | Agent | buy | SQQQ | 15.77 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T19:30 | Williams %R · 1h | sell | TNA | 5.44 | 0.02 | exit signal |
| 2026-11-23T19:30 | Connors RSI(2) · 1h | sell | SQQQ | 20.65 | 0.56 | exit signal |
| 2026-11-23T19:30 | VWAP momentum · 1h | buy | SQQQ | 4.88 | — | entry signal |
| 2026-11-23T19:30 | VWAP momentum · 1h | sell | QQQ | 4.88 | -0.01 | exit signal |
| 2026-11-23T19:30 | MACD zero-line · 1h | buy | TSLA | 16.50 | — | entry signal |
| 2026-11-23T19:25 | Agent (ML meta-label) | sell | BITX | 14.90 | -0.08 | selected signal exited |
| 2026-11-23T19:20 | Agent (ML meta-label) | buy | BITX | 14.98 | — | entry |
| 2026-11-23T19:17 | Agent (ML meta-label) | sell | BITX | 14.97 | -0.03 | selected signal exited |
| 2026-11-23T19:15 | Agent (ML meta-label) | buy | BITX | 15.00 | — | entry |
| 2026-11-23T19:11 | Agent (ML meta-label) | buy | SQQQ | 15.01 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T19:11 | Agent (ML meta-label) | sell | BITX | 14.99 | -0.03 | selected signal exited |
| 2026-11-23T19:00 | Agent (ML meta-label) | sell | SQQQ | 15.02 | 0.06 | selected signal exited |
| 2026-11-23T19:00 | Connors RSI(2) · 1h | buy | SOL-USD | 20.31 | — | entry signal |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | XRP-USD | 7.96 | -0.50 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | TSLA | 5.48 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | SOL-USD | 8.06 | 0.21 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | PLTR | 8.27 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | NVDA | 8.13 | -0.29 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 20:15:05.000138+00:00 -> 2026-11-23 20:25:05.000138+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
