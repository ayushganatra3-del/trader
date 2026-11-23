# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T20:45:05.000132+00:00 · 70956 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

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

Today: 35099 decisions in 3034 calls, $0.4354 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T20:45 | 4 / 21 / 5 | cash |  |
| Breezy | 2026-11-23T20:45 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-23T20:45 | 5 / 23 / 2 | COIN 75% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 29.80 | 4.50 | -5.42 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.50 | 15.49 | 0 | — | 12.53 | 4.27 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.05 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.55 | 4.55 | 0 | — | 3.19 | 0.92 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.83 | -0.17 | -8.58 | 208 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.91 | -3.75 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.95 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.68 | -4.32 | 0 | — | -5.83 | -1.45 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.23 | -3.19 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.75 | -7.82 | -4.87 | 18 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.47 | -7.53 | 0 | — | -8.65 | -1.78 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.85 | -8.15 | 27 | 18.5 | -8.58 | -6.89 | -10.08 | 25 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -5.25 | -3.29 | -8.41 | 31 |
| 17 | Copy: Congress Democrats (NANC) | copy | 90.64 | -9.36 | 0 | — | -10.79 | -2.35 | -17.03 | 1 |
| 18 | VWAP reversion · 1h | reversion | 90.17 | -9.83 | 163 | 46.0 | -7.27 | -1.25 | -20.49 | 157 |
| 19 | Copy: Insider buying | copy | 89.35 | -10.65 | 58 | 39.7 | -18.03 | -3.51 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.66 | -3.29 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 87.12 | -12.88 | 9 | 44.4 | -10.35 | -0.53 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.85 | -13.15 | 457 | 33.3 | -12.63 | -4.26 | -14.39 | 542 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -16.74 | -3.81 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -22.06 | -7.43 | -22.23 | 82 |
| 25 | Connors RSI(2) · 1h | reversion | 80.74 | -19.26 | 220 | 40.9 | -13.98 | -6.13 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.70 | -19.30 | 203 | 28.1 | -27.81 | -7.61 | -30.34 | 190 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -26.08 | -5.68 | -26.44 | 195 |
| 28 | Opening range 15m | breakout | 77.69 | -22.31 | 567 | 30.9 | -22.06 | -6.87 | -23.30 | 660 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -25.29 | -4.28 | -25.84 | 91 |
| 30 | Donchian 55/20 · 1h ⏸ | breakout | 76.80 | -23.20 | 85 | 14.1 | -29.16 | -7.78 | -29.50 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.81 | -7.06 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -24.17 | -6.48 | -25.26 | 144 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.32 | -7.99 | -31.19 | 102 |
| 34 | Hold BTC | benchmark | 71.19 | -28.81 | 3 | 0.0 | -29.30 | -5.20 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.13 | -28.88 | 200 | 17.0 | -34.85 | -6.78 | -39.07 | 211 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.50 | -29.50 | 3 | 0.0 | -23.15 | -2.81 | -32.18 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -37.31 | -6.72 | -40.30 | 278 |
| 38 | Triple EMA stack · 1h | trend | 69.65 | -30.36 | 162 | 14.8 | -37.14 | -9.53 | -38.76 | 169 |
| 39 | EMA 20/50 cross · 1h | trend | 69.35 | -30.65 | 119 | 10.1 | -37.49 | -10.26 | -40.18 | 118 |
| 40 | Daily: Momentum burst | daily | 68.92 | -31.08 | 30 | 13.3 | -37.47 | -5.41 | -37.81 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.70 | -31.30 | 207 | 22.2 | -32.50 | -8.53 | -33.70 | 211 |
| 42 | Stochastic reversion · 1h | reversion | 66.91 | -33.09 | 394 | 40.9 | -33.98 | -3.63 | -42.70 | 431 |
| 43 | OBV trend · 1h | momentum | 66.52 | -33.48 | 320 | 19.7 | -39.61 | -10.07 | -40.77 | 234 |
| 44 | MACD zero-line · 1h | trend | 66.03 | -33.97 | 198 | 16.7 | -35.05 | -9.58 | -35.49 | 206 |
| 45 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -39.27 | -8.93 | -40.90 | 201 |
| 46 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.72 | -9.58 | -47.76 | 630 |
| 47 | Max aggression: 5-day momentum ⏸ | meta | 64.49 | -35.51 | 25 | 36.0 | -61.45 | -4.01 | -65.46 | 23 |
| 48 | MFI reversion · 1h | reversion | 63.94 | -36.06 | 486 | 32.9 | -31.80 | -4.58 | -37.87 | 184 |
| 49 | Donchian 20/10 · 1h ⏸ | breakout | 62.04 | -37.97 | 178 | 18.0 | -39.39 | -8.48 | -41.23 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.50 | -8.65 | -42.80 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 60.03 | -39.97 | 299 | 11.4 | -44.21 | -10.43 | -45.46 | 333 |
| 52 | Agent (ML meta-label) | meta | 59.46 | -40.54 | 2049 | 25.0 | -13.96 | -1.59 | -25.98 | 314 |
| 53 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -52.53 | -3.86 | -54.71 | 38 |
| 54 | MACD cross · 1h | trend | 59.06 | -40.94 | 466 | 21.2 | -49.19 | -9.50 | -51.01 | 516 |
| 55 | CCI reversion · 1h | reversion | 58.28 | -41.72 | 430 | 40.0 | -49.31 | -8.20 | -52.09 | 501 |
| 56 | Bollinger reversion · 1h | reversion | 57.94 | -42.06 | 391 | 37.6 | -37.69 | -4.51 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 54.18 | -45.82 | 500 | 38.4 | -54.71 | -9.06 | -56.11 | 588 |
| 58 | VWAP momentum · 1h | momentum | 53.65 | -46.35 | 1054 | 21.8 | -57.59 | -13.24 | -58.29 | 1180 |
| 59 | RSI(14) reversion · 1h | reversion | 51.15 | -48.85 | 241 | 32.0 | -49.71 | -7.93 | -52.23 | 291 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.69 | -8.68 | -54.67 | 669 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -49.06 | -99.13 | 5340 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.81 | -33.02 | -84.49 | 1434 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.46 | -50.30 | -94.50 | 2441 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.70 | -32.35 | -90.85 | 1915 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.75 | -42.27 | -91.80 | 2256 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.51 | -28.31 | -89.66 | 1961 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.15 | -49.73 | -98.16 | 3432 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.98 | -54.26 | -97.02 | 3369 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.60 | -39.59 | -93.63 | 2133 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.27 | -22.75 | -52.27 | 646 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.37 | -35.49 | -83.49 | 1559 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -57.20 | -99.67 | 6285 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.26 | -39.98 | -93.28 | 2499 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.45 | -36.72 | -94.47 | 3178 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -66.99 | -99.83 | 6146 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.11 | -43.61 | -93.32 | 2267 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.43 | -24.22 | -78.60 | 1615 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -58.65 | -97.79 | 3289 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.18 | -61.17 | -99.18 | 5119 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.65 | -27.85 | -70.74 | 1198 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.98 | -50.01 | -94.99 | 2676 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.55 | -6.16 | -48.79 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.63 | -37.76 | -85.64 | 1675 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.93 | -99.76 | 6546 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.46 | -30.32 | -91.69 | 2466 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.92 | -20.23 | -82.96 | 1957 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.86 | -30.63 | -92.06 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.13 | -49.89 | -98.14 | 4051 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.20 | -48.74 | -90.31 | 2195 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.39 | -30.51 | -68.40 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.71 | -28.75 | -74.05 | 1169 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.42 | -19.48 | -84.50 | 1835 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.96 | -50.08 | -97.98 | 4415 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -106.09 | -99.94 | 8298 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-23T20:45 | Agent (ML meta-label) | buy | SQQQ | 14.87 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T20:36 | Agent (ML meta-label) | sell | SQQQ | 14.65 | -0.26 | selected signal exited |
| 2026-11-23T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | TQQQ | 91.73 | — | entry |
| 2026-11-23T20:30 | Agent | sell | SQQQ | 15.60 | -0.17 | selected signal exited |
| 2026-11-23T20:30 | VWAP reversion · 1h | buy | MSTR | 22.55 | — | entry signal |
| 2026-11-23T20:30 | RSI(14) reversion · 1h | sell | AAPL | 2.35 | 0.00 | exit signal |
| 2026-11-23T20:30 | VWAP momentum · 1h | buy | QQQ | 4.47 | — | entry signal |
| 2026-11-23T20:30 | VWAP momentum · 1h | sell | SQQQ | 4.83 | -0.05 | exit signal |
| 2026-11-23T20:24 | Copy: Insider buying | buy | WWB | 1.31 | — | entry |
| 2026-11-23T20:22 | Copy: Insider buying | buy | KNOP | 9.91 | — | rebalance up |
| 2026-11-23T20:20 | Copy: Insider buying | sell | PAM | 11.21 | -0.07 | target is flat |
| 2026-11-23T20:20 | VWAP momentum · 1h | buy | TQQQ | 4.12 | — | entry |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 20:45:05.000132+00:00 -> 2026-11-23 20:55:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
