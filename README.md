# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-23T19:15:05.000121+00:00 · 70889 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.86 (-21.14%)

Closed trades 240, win rate 35.8%, fees £6.50, max drawdown -21.99%.

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

Today: 29063 decisions in 2833 calls, $0.3648 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-23T19:15 | 3 / 18 / 9 | TNA 15%, LABU 14% |  |
| Breezy | 2026-11-23T19:15 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-23T19:15 | 5 / 25 / 0 | BITX 64% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 32.17 | 4.75 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.41 | 15.41 | 0 | — | 13.05 | 4.43 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.44 | 1.36 | -9.74 | 35 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.69 | 4.68 | 41 | 29.3 | 6.00 | 1.04 | -11.74 | 44 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.32 | 4.32 | 0 | — | 2.85 | 0.84 | -6.60 | 0 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.15 | -0.85 | 217 | 31.8 | -0.90 | -0.19 | -8.58 | 209 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 164 | 33.5 | -3.78 | -3.55 | -4.60 | 64 |
| 10 | Agent (rotation) | meta | 96.01 | -3.99 | 227 | 28.6 | -0.97 | -0.23 | -7.48 | 154 |
| 11 | Hold SPY | benchmark | 95.72 | -4.28 | 0 | — | -6.23 | -1.56 | -11.71 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.44 | -3.29 | -7.38 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.20 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.62 | -7.38 | 0 | — | -8.65 | -1.76 | -13.87 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -8.98 | -7.15 | -10.34 | 24 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -4.94 | -3.08 | -8.11 | 30 |
| 17 | VWAP reversion · 1h | reversion | 90.85 | -9.15 | 163 | 46.0 | -6.62 | -1.06 | -20.49 | 156 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.66 | -9.34 | 0 | — | -10.73 | -2.33 | -17.03 | 1 |
| 19 | Copy: Insider buying | copy | 89.28 | -10.72 | 57 | 40.4 | -18.31 | -3.57 | -22.56 | 68 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -16.42 | -3.40 | -20.94 | 1 |
| 21 | Daily: Connors RSI(2) · 3x ETFs | daily | 87.04 | -12.96 | 9 | 44.4 | -10.66 | -0.55 | -26.65 | 6 |
| 22 | Opening range 30m | breakout | 86.89 | -13.11 | 457 | 33.3 | -12.79 | -4.28 | -14.52 | 544 |
| 23 | Daily: Bullish score ⏸ | daily | 85.32 | -14.68 | 20 | 20.0 | -17.47 | -3.96 | -19.56 | 14 |
| 24 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -17.33 | -6.35 | -18.12 | 71 |
| 25 | Connors RSI(2) · 1h | reversion | 80.89 | -19.11 | 219 | 40.6 | -13.87 | -6.00 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 80.58 | -19.41 | 203 | 28.1 | -27.89 | -7.50 | -30.20 | 190 |
| 27 | Agent | meta | 78.86 | -21.14 | 240 | 35.8 | -26.02 | -5.64 | -26.44 | 200 |
| 28 | Opening range 15m | breakout | 77.73 | -22.27 | 567 | 30.9 | -22.39 | -6.92 | -23.54 | 663 |
| 29 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -26.39 | -4.46 | -26.39 | 96 |
| 30 | Donchian 55/20 · 1h | breakout | 77.10 | -22.90 | 83 | 12.0 | -28.87 | -7.73 | -29.15 | 84 |
| 31 | Volume breakout · 1h ⏸ | breakout | 76.53 | -23.47 | 169 | 27.8 | -22.97 | -6.94 | -23.25 | 72 |
| 32 | Keltner breakout · 1h ⏸ | breakout | 75.67 | -24.33 | 137 | 24.8 | -26.55 | -6.88 | -27.26 | 149 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.59 | -8.02 | -31.46 | 105 |
| 34 | Hold BTC | benchmark | 71.66 | -28.34 | 3 | 0.0 | -28.90 | -5.12 | -36.21 | 1 |
| 35 | Supertrend · 1h | trend | 71.22 | -28.78 | 200 | 17.0 | -33.83 | -6.43 | -38.10 | 218 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 70.37 | -29.63 | 3 | 0.0 | -24.36 | -2.99 | -32.18 | 1 |
| 37 | Triple EMA stack · 1h | trend | 70.23 | -29.77 | 162 | 14.8 | -36.08 | -9.17 | -38.25 | 166 |
| 38 | EMA 20/50 cross · 1h | trend | 70.00 | -30.00 | 119 | 10.1 | -36.18 | -10.07 | -39.05 | 124 |
| 39 | ADX DI cross · 1h ⏸ | trend | 69.72 | -30.28 | 252 | 19.0 | -36.24 | -6.56 | -39.10 | 282 |
| 40 | Daily: Momentum burst | daily | 69.13 | -30.87 | 30 | 13.3 | -37.95 | -5.43 | -38.52 | 25 |
| 41 | Bollinger breakout · 1h | breakout | 68.59 | -31.41 | 207 | 22.2 | -33.40 | -8.76 | -34.45 | 213 |
| 42 | OBV trend · 1h | momentum | 67.15 | -32.85 | 320 | 19.7 | -39.11 | -10.09 | -40.43 | 233 |
| 43 | Stochastic reversion · 1h | reversion | 67.09 | -32.91 | 394 | 40.9 | -35.09 | -3.77 | -43.64 | 435 |
| 44 | MACD zero-line · 1h | trend | 65.92 | -34.08 | 198 | 16.7 | -33.90 | -9.07 | -34.14 | 209 |
| 45 | Max aggression: 5-day momentum | meta | 65.49 | -34.51 | 24 | 37.5 | -61.25 | -3.97 | -65.11 | 23 |
| 46 | RSI momentum · 1h ⏸ | momentum | 65.10 | -34.90 | 196 | 15.3 | -39.35 | -8.90 | -40.78 | 204 |
| 47 | Heikin-Ashi · 1h ⏸ | trend | 64.61 | -35.39 | 526 | 22.2 | -46.90 | -9.47 | -47.64 | 632 |
| 48 | MFI reversion · 1h | reversion | 63.75 | -36.25 | 486 | 32.9 | -31.52 | -4.53 | -37.45 | 185 |
| 49 | Donchian 20/10 · 1h | breakout | 62.73 | -37.27 | 174 | 16.7 | -39.15 | -8.34 | -40.83 | 193 |
| 50 | ROC + volume · 1h ⏸ | momentum | 61.62 | -38.38 | 451 | 27.1 | -42.51 | -8.57 | -42.68 | 345 |
| 51 | EMA 9/21 cross · 1h | trend | 60.32 | -39.68 | 299 | 11.4 | -44.89 | -10.51 | -46.07 | 328 |
| 52 | Agent (ML meta-label) | meta | 59.98 | -40.02 | 2043 | 25.0 | -27.00 | -3.23 | -37.70 | 335 |
| 53 | MACD cross · 1h | trend | 59.24 | -40.76 | 464 | 20.9 | -48.98 | -9.39 | -50.63 | 518 |
| 54 | Max aggression: 1-day momentum ⏸ | meta | 59.16 | -40.84 | 34 | 26.5 | -53.24 | -3.85 | -54.71 | 38 |
| 55 | CCI reversion · 1h | reversion | 58.30 | -41.70 | 430 | 40.0 | -49.30 | -8.20 | -52.02 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 57.94 | -42.06 | 391 | 37.6 | -37.70 | -4.48 | -45.42 | 434 |
| 57 | Williams %R · 1h | reversion | 54.26 | -45.74 | 499 | 38.3 | -54.58 | -8.92 | -55.97 | 592 |
| 58 | VWAP momentum · 1h | momentum | 53.82 | -46.18 | 1051 | 21.8 | -57.65 | -13.18 | -58.37 | 1191 |
| 59 | RSI(14) reversion · 1h | reversion | 51.16 | -48.84 | 240 | 31.7 | -44.71 | -6.47 | -50.33 | 314 |
| 60 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -50.93 | -8.32 | -53.80 | 688 |
| 61 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.13 | -48.02 | -99.13 | 5331 |
| 62 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.90 | -32.44 | -84.52 | 1433 |
| 63 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.45 | -47.63 | -94.50 | 2426 |
| 64 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.83 | -31.40 | -91.02 | 1924 |
| 65 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.76 | -40.39 | -91.81 | 2252 |
| 66 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.45 | -27.51 | -89.58 | 1947 |
| 67 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.14 | -47.65 | -98.14 | 3414 |
| 68 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.98 | -50.95 | -97.01 | 3361 |
| 69 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.63 | -38.22 | -93.63 | 2150 |
| 70 | Three white soldiers | momentum | 50.31 | -49.69 | 637 | 14.3 | -52.26 | -22.44 | -52.27 | 647 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.38 | -34.29 | -83.46 | 1559 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.66 | -53.25 | -99.66 | 6291 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.20 | -39.46 | -93.21 | 2488 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.40 | -35.52 | -94.43 | 3163 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -61.03 | -99.82 | 6121 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.19 | -42.48 | -93.41 | 2262 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.27 | -24.02 | -78.61 | 1612 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -55.12 | -97.79 | 3288 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -57.61 | -99.17 | 5111 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.62 | -27.54 | -70.62 | 1191 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.95 | -48.04 | -94.96 | 2670 |
| 83 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -44.72 | -6.15 | -48.78 | 280 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.62 | -37.09 | -85.63 | 1677 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -69.40 | -99.77 | 6539 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.51 | -29.83 | -91.69 | 2460 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.65 | -19.65 | -82.69 | 1952 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.85 | -29.59 | -92.07 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -47.15 | -98.13 | 4050 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.36 | -47.57 | -90.37 | 2205 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.33 | -29.90 | -68.34 | 796 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.93 | -27.89 | -74.18 | 1168 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -84.15 | -19.09 | -84.24 | 1846 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.98 | -47.83 | -97.99 | 4426 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.42 | -99.94 | 8275 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-23T19:00 | RSI momentum · 1h | sell | ETH-USD | 10.93 | 0.14 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | DOGE-USD | 8.12 | 0.20 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | RSI momentum · 1h | sell | BTC-USD | 8.15 | 0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-23T19:00 | Ichimoku · 1h | sell | DOGE-USD | 19.86 | 0.52 | exit signal |
| 2026-11-23T19:00 | Supertrend · 1h | buy | AMZN | 2.86 | — | entry |
| 2026-11-23T19:00 | Supertrend · 1h | sell | XRP-USD | 2.86 | -0.08 | exit signal |
| 2026-11-23T18:55 | Agent (ML meta-label) | buy | SQQQ | 14.96 | — | following Connors RSI(2), Squeeze breakout, VWAP momentum · 1h, Opening range 15m, Stochastic reversion |
| 2026-11-23T18:51 | Agent (ML meta-label) | sell | SQQQ | 14.32 | -0.04 | selected signal exited |
| 2026-11-23T18:40 | Donchian 55/20 · 1h | sell | DOGE-USD | 19.24 | -0.48 | stop-loss |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | XRP-USD | 4.74 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | SOL-USD | 4.70 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | buy | BTC-USD | 4.67 | — | rebalance up |
| 2026-11-23T18:40 | Donchian 20/10 · 1h | sell | DOGE-USD | 11.15 | -0.27 | stop-loss |
| 2026-11-23T18:30 | Agent (ML meta-label) | buy | BITX | 10.96 | — | rebalance up |
| 2026-11-23T18:30 | Agent (ML meta-label) | sell | TECL | 14.08 | 0.79 | selected signal exited |
| 2026-11-23T18:30 | Williams %R · 1h | buy | TNA | 2.92 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | SOXL | 3.02 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | MSTR | 3.03 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | MSFT | 2.96 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | ETHU | 3.04 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | COIN | 2.97 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | BITX | 3.06 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AMZN | 2.92 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AMD | 2.96 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | buy | AAPL | 2.95 | — | rebalance up |
| 2026-11-23T18:30 | Williams %R · 1h | sell | TQQQ | 2.46 | -0.04 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | TECL | 2.43 | -0.07 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | META | 2.53 | 0.03 | exit signal |
| 2026-11-23T18:30 | Williams %R · 1h | sell | IWM | 2.50 | 0.00 | exit signal |
| 2026-11-23T18:30 | Stochastic reversion · 1h | buy | MSTR | 3.48 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-25 19:15:05.000121+00:00 -> 2026-11-23 19:25:05.000121+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
