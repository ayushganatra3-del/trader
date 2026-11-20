# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-20T21:20:05.000132+00:00 · 67309 ticks

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
| Copy: Insider buying | 2026-11-20 | WWB 12%, PEPG 12%, FUN 12%, STWD 12%, ANAB 12%, PAM 12%, TEAM 12%, PSEC 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-20)

**Correction** since 2026-11-13 · level correction · 5 distribution days in 25 sessions · timing exposure 0% · VXN 47.40 · VIX 38.87 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.0, AAPL 2.5, AMZN 0.7, META -0.2, MSFT -0.3, TSLA -0.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 41142 decisions in 3288 calls, $0.5085 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-20T21:20 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-20T21:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-20T21:20 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | TSLA | 2.22 | +5.41% | 14 |
| Connors RSI(2) | SQQQ | 2.10 | +6.37% | 13 |
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| MFI reversion | META | 2.04 | +2.40% | 6 |
| CCI reversion | SOXL | 1.96 | +18.20% | 16 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 31.33 | 4.69 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.37 | 14.37 | 0 | — | 12.12 | 4.06 | -4.89 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.98 | 9.98 | 40 | 30.0 | 17.08 | 2.59 | -8.66 | 45 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.22 | 1.34 | -9.74 | 36 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.53 | 1.53 | 0 | — | 2.38 | 0.74 | -6.60 | 0 |
| 6 | Gap and go | momentum | 100.33 | 0.33 | 204 | 31.9 | 1.11 | 0.44 | -9.06 | 202 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.71 | -1.29 | 161 | 34.2 | -4.98 | -4.28 | -5.55 | 75 |
| 10 | Agent (rotation) | meta | 97.90 | -2.10 | 213 | 29.1 | 0.98 | 0.42 | -8.00 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 12 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.07 | -8.36 | -5.13 | 19 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.73 | -8.27 | 27 | 18.5 | -9.53 | -7.61 | -10.89 | 25 |
| 14 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.26 | -4.55 | -11.04 | 45 |
| 15 | Daily: Bullish score | daily | 90.93 | -9.07 | 19 | 15.8 | -11.44 | -2.72 | -19.56 | 14 |
| 16 | Hold SPY | benchmark | 90.90 | -9.10 | 0 | — | -10.23 | -3.21 | -11.71 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 89.40 | -10.60 | 0 | — | -11.06 | -2.89 | -11.99 | 1 |
| 18 | Squeeze breakout · 1h | breakout | 88.44 | -11.56 | 70 | 20.0 | -16.98 | -7.58 | -18.95 | 72 |
| 19 | Copy: Insider buying | copy | 87.90 | -12.10 | 56 | 39.3 | -8.65 | -1.68 | -14.79 | 66 |
| 20 | Opening range 30m | breakout | 87.39 | -12.61 | 452 | 33.6 | -10.64 | -3.47 | -14.87 | 552 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | VWAP reversion · 1h | reversion | 86.95 | -13.05 | 157 | 45.2 | -15.22 | -4.31 | -20.28 | 155 |
| 23 | Copy: Congress Democrats (NANC) | copy | 86.29 | -13.71 | 0 | — | -14.46 | -3.80 | -16.89 | 1 |
| 24 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 85.09 | -14.91 | 9 | 44.4 | -20.22 | -1.78 | -26.65 | 6 |
| 25 | Parabolic SAR · 1h | trend | 84.89 | -15.11 | 194 | 27.8 | -23.69 | -6.37 | -28.86 | 195 |
| 26 | Donchian 55/20 · 1h | breakout | 81.86 | -18.14 | 79 | 12.7 | -23.98 | -6.67 | -27.71 | 81 |
| 27 | Volume breakout · 1h | breakout | 81.67 | -18.33 | 163 | 28.8 | -14.53 | -4.43 | -21.55 | 74 |
| 28 | Keltner breakout · 1h | breakout | 80.52 | -19.48 | 126 | 26.2 | -21.08 | -5.67 | -25.34 | 144 |
| 29 | Agent ⏸ | meta | 80.18 | -19.82 | 238 | 36.1 | -21.80 | -5.25 | -22.15 | 212 |
| 30 | Connors RSI(2) · 1h | reversion | 79.80 | -20.20 | 218 | 40.4 | -15.28 | -6.90 | -15.31 | 71 |
| 31 | Agent (aggressive) ⏸ | meta | 78.30 | -21.70 | 110 | 32.7 | -16.63 | -4.27 | -19.15 | 98 |
| 32 | Opening range 15m | breakout | 77.69 | -22.31 | 562 | 31.1 | -21.01 | -6.44 | -23.60 | 673 |
| 33 | Ichimoku · 1h | trend | 76.82 | -23.18 | 107 | 14.0 | -28.01 | -7.61 | -32.08 | 109 |
| 34 | ADX DI cross · 1h | trend | 74.71 | -25.29 | 228 | 20.2 | -30.72 | -5.72 | -35.87 | 269 |
| 35 | Max aggression: 1-day momentum | meta | 73.00 | -27.00 | 33 | 27.3 | -48.95 | -3.41 | -58.27 | 39 |
| 36 | Bollinger breakout · 1h | breakout | 72.96 | -27.04 | 195 | 21.5 | -30.36 | -7.15 | -36.32 | 216 |
| 37 | Supertrend · 1h | trend | 72.92 | -27.08 | 198 | 16.7 | -33.54 | -6.53 | -37.64 | 199 |
| 38 | Triple EMA stack · 1h | trend | 72.89 | -27.11 | 161 | 14.3 | -32.14 | -7.62 | -37.24 | 170 |
| 39 | EMA 20/50 cross · 1h | trend | 72.58 | -27.42 | 119 | 10.1 | -35.75 | -9.72 | -40.64 | 122 |
| 40 | Heikin-Ashi · 1h | trend | 71.01 | -28.99 | 483 | 23.0 | -43.96 | -9.09 | -47.85 | 616 |
| 41 | RSI momentum · 1h | momentum | 70.69 | -29.31 | 184 | 14.1 | -36.96 | -7.87 | -41.81 | 202 |
| 42 | Copy: Cathie Wood (ARKK) ⏸ | copy | 70.36 | -29.64 | 3 | 0.0 | -29.03 | -4.11 | -32.18 | 1 |
| 43 | OBV trend · 1h | momentum | 70.31 | -29.69 | 316 | 19.6 | -39.78 | -10.87 | -41.25 | 240 |
| 44 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -36.56 | -5.18 | -37.91 | 31 |
| 45 | Max aggression: 5-day momentum ⏸ | meta | 68.98 | -31.02 | 24 | 37.5 | -49.31 | -3.20 | -60.06 | 22 |
| 46 | Hold BTC ⏸ | benchmark | 68.38 | -31.62 | 3 | 0.0 | -28.35 | -4.56 | -33.67 | 1 |
| 47 | MACD zero-line · 1h | trend | 68.12 | -31.88 | 190 | 17.4 | -32.63 | -8.99 | -32.94 | 202 |
| 48 | Donchian 20/10 · 1h | breakout | 67.33 | -32.67 | 165 | 17.6 | -34.92 | -6.47 | -43.26 | 192 |
| 49 | Stochastic reversion · 1h ⏸ | reversion | 66.92 | -33.08 | 378 | 39.9 | -43.13 | -6.07 | -43.86 | 446 |
| 50 | ROC + volume · 1h | momentum | 66.41 | -33.59 | 431 | 27.6 | -34.66 | -6.31 | -41.24 | 335 |
| 51 | MFI reversion · 1h ⏸ | reversion | 64.95 | -35.05 | 476 | 33.0 | -35.38 | -5.28 | -36.95 | 174 |
| 52 | EMA 9/21 cross · 1h | trend | 64.79 | -35.21 | 291 | 11.3 | -38.42 | -7.24 | -47.13 | 321 |
| 53 | MACD cross · 1h | trend | 63.02 | -36.98 | 444 | 20.9 | -49.67 | -9.92 | -51.07 | 496 |
| 54 | CCI reversion · 1h | reversion | 62.82 | -37.18 | 408 | 40.9 | -46.60 | -7.67 | -47.70 | 479 |
| 55 | Bollinger reversion · 1h ⏸ | reversion | 58.24 | -41.76 | 377 | 36.6 | -44.46 | -6.67 | -45.16 | 443 |
| 56 | Williams %R · 1h ⏸ | reversion | 57.63 | -42.37 | 470 | 38.5 | -52.17 | -8.51 | -52.91 | 582 |
| 57 | RSI(14) reversion · 1h | reversion | 55.41 | -44.59 | 225 | 32.9 | -43.22 | -6.33 | -46.04 | 267 |
| 58 | VWAP momentum · 1h | momentum | 55.25 | -44.75 | 1013 | 21.4 | -55.66 | -11.03 | -60.51 | 1192 |
| 59 | Agent (ML meta-label) | meta | 55.09 | -44.91 | 2005 | 24.6 | -30.45 | -5.38 | -31.81 | 320 |
| 60 | Z-score reversion · 1h ⏸ | reversion | 52.10 | -47.90 | 242 | 33.1 | -43.68 | -6.04 | -46.09 | 265 |
| 61 | Three white soldiers | momentum | 51.69 | -48.31 | 618 | 14.1 | -52.23 | -23.16 | -52.57 | 665 |
| 62 | Candlestick reversal · 1h ⏸ | reversion | 51.29 | -48.71 | 601 | 25.8 | -53.60 | -9.51 | -53.63 | 679 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.12 | -47.74 | -99.14 | 5327 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -83.44 | -30.44 | -84.01 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.37 | -46.66 | -94.42 | 2450 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -91.19 | -33.95 | -91.37 | 1950 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -92.00 | -44.71 | -92.21 | 2291 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -28.16 | -90.21 | 2024 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.25 | -49.92 | -98.25 | 3487 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -51.33 | -96.87 | 3387 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -39.47 | -93.86 | 2190 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.50 | -35.70 | -83.61 | 1579 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -55.34 | -99.67 | 6363 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.18 | -44.87 | -93.23 | 2536 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.59 | -37.50 | -94.63 | 3163 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.85 | -71.11 | -99.85 | 6291 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.49 | -46.71 | -93.49 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.87 | -26.91 | -79.02 | 1638 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -60.53 | -97.82 | 3379 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.16 | -58.42 | -99.16 | 5121 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.92 | -29.85 | -71.12 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.06 | -55.35 | -95.10 | 2729 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.69 | -39.14 | -85.98 | 1706 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.74 | -71.34 | -99.74 | 6565 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.75 | -31.41 | -91.77 | 2488 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -81.97 | -19.09 | -82.02 | 1944 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -92.54 | -33.49 | -92.54 | 2208 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.90 | -46.15 | -97.90 | 4052 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.57 | -52.68 | -90.61 | 2207 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -67.45 | -32.57 | -67.54 | 794 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.76 | -27.44 | -74.90 | 1204 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.95 | -18.95 | -83.98 | 1859 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.78 | -46.42 | -97.78 | 4451 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.95 | -117.21 | -99.95 | 8431 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-20T21:10 | RSI(14) reversion · 1h | sell | SOL-USD | 13.44 | -0.54 | stop-loss |
| 2026-11-20T20:55 | Agent (rotation) | sell | SQQQ | 42.05 | 2.51 | selected signal exited |
| 2026-11-20T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 109.37 | 9.74 | target is flat |
| 2026-11-20T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 128.32 | 6.58 | target is flat |
| 2026-11-20T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.73 | 0.70 | target is flat |
| 2026-11-20T20:55 | Opening range 30m | sell | SQQQ | 23.47 | 2.15 | end-of-day flatten |
| 2026-11-20T20:55 | Opening range 15m | sell | SQQQ | 20.96 | 1.92 | end-of-day flatten |
| 2026-11-20T20:55 | Gap and go | sell | SQQQ | 26.94 | 2.47 | end-of-day flatten |
| 2026-11-20T20:48 | Agent (ML meta-label) | buy | BTC-USD | 3.68 | — | entry |
| 2026-11-20T20:48 | Agent (ML meta-label) | sell | XRP-USD | 4.58 | -0.15 | selected signal exited |
| 2026-11-20T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.03 | — | entry |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | ETHU | 14.54 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | AMD | 14.60 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | buy | AAPL | 14.60 | — | entry signal |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | XRP-USD | 7.19 | -0.18 | rebalance down |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | DOGE-USD | 7.31 | -0.14 | rebalance down |
| 2026-11-20T20:30 | VWAP reversion · 1h | sell | BTC-USD | 7.28 | -0.02 | rebalance down |
| 2026-11-20T20:25 | OBV trend · 1h | buy | SQQQ | 17.53 | — | entry |
| 2026-11-20T20:05 | Copy: Cathie Wood (ARKK) | sell | ARKK | 70.36 | -9.70 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T20:05 | Three white soldiers | sell | AMD | 12.83 | -0.12 | exit signal |
| 2026-11-20T20:00 | VWAP reversion · 1h | buy | BTC-USD | 21.89 | — | entry signal |
| 2026-11-20T19:55 | Three white soldiers | buy | AMD | 12.95 | — | entry signal |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | TNA | 6.39 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | SOL-USD | 6.44 | -0.17 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | PLTR | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSTR | 6.46 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | MSFT | 6.55 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | IWM | 6.54 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | DOGE-USD | 5.81 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | COIN | 6.48 | -0.11 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | Bollinger reversion · 1h | sell | AMD | 6.41 | -0.18 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:35 | VWAP momentum · 1h | sell | SQQQ | 2.76 | 0.48 | rebalance down |
| 2026-11-20T19:30 | CCI reversion · 1h | sell | GOOGL | 15.49 | -0.49 | stop-loss |
| 2026-11-20T19:30 | Bollinger reversion · 1h | buy | DOGE-USD | 5.85 | — | entry |
| 2026-11-20T19:30 | Bollinger reversion · 1h | sell | GOOGL | 6.53 | -0.21 | stop-loss |
| 2026-11-20T19:25 | MFI reversion · 1h | sell | DOGE-USD | 16.01 | -0.31 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-20T19:25 | OBV trend · 1h | sell | SQQQ | 19.95 | 3.23 | target is flat |
| 2026-11-20T19:20 | VWAP reversion · 1h | sell | BTC-USD | 21.57 | -0.72 | stop-loss |
| 2026-11-20T19:00 | MFI reversion · 1h | buy | DOGE-USD | 16.32 | — | entry signal |
| 2026-11-20T18:50 | Hold BTC | sell | BTC-USD | 68.38 | -6.75 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-22 21:20:05.000132+00:00 -> 2026-11-20 21:30:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
