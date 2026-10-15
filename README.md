# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T18:25:05.000151+00:00 · 23884 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.93 (-7.07%)

Closed trades 75, win rate 40.0%, fees £2.63, max drawdown -7.49%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 30306 decisions in 2682 calls, $0.3777 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T18:25 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-10-15T18:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-15T18:25 | 3 / 25 / 2 | COIN 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 1.76 | +3.30% | 6 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.49 | 4.49 | 0 | — | 4.32 | 2.07 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.64 | 3.64 | 1 | 100.0 | 4.31 | 1.17 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.01 | 1.79 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 101.58 | 1.58 | 9 | 66.7 | -4.34 | -1.35 | -9.61 | 27 |
| 5 | Copy: Insider buying | copy | 100.25 | 0.25 | 20 | 45.0 | -15.89 | -2.52 | -21.97 | 76 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.98 | -0.02 | 0 | — | 3.40 | 1.35 | -5.18 | 1 |
| 9 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 10 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 58 | 39.7 | -11.77 | -3.24 | -14.08 | 115 |
| 11 | Hold SPY | benchmark | 99.90 | -0.10 | 0 | — | -0.92 | -0.50 | -3.33 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.54 | -1.46 | 0 | — | -0.96 | -0.36 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 97.86 | -2.14 | 0 | — | 30.07 | 3.46 | -8.68 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.60 | -2.40 | 0 | — | -5.31 | -2.91 | -6.38 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 97.53 | -2.47 | 36 | 16.7 | 7.00 | 0.98 | -22.11 | 112 |
| 18 | Trend pullback · 1h | trend | 96.70 | -3.29 | 86 | 24.4 | -21.60 | -6.05 | -23.43 | 157 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.67 | -3.33 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 21 | Daily: Momentum burst | daily | 96.09 | -3.91 | 5 | 20.0 | -4.40 | -0.51 | -17.67 | 39 |
| 22 | ADX DI cross · 1h | trend | 95.88 | -4.12 | 70 | 21.4 | -10.25 | -1.86 | -15.09 | 254 |
| 23 | Agent (rotation) | meta | 95.50 | -4.50 | 105 | 31.4 | -15.20 | -5.27 | -15.91 | 281 |
| 24 | Max aggression: 5-day momentum | meta | 93.94 | -6.06 | 8 | 37.5 | -5.70 | -0.21 | -34.64 | 26 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.89 | 1.07 | -9.46 | 102 |
| 26 | Parabolic SAR · 1h | trend | 93.63 | -6.37 | 93 | 22.6 | 3.30 | 0.60 | -21.82 | 282 |
| 27 | EMA 20/50 cross · 1h | trend | 93.57 | -6.43 | 51 | 15.7 | -1.40 | 0.04 | -23.73 | 132 |
| 28 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 8.94 | 2.25 | -6.78 | 202 |
| 29 | Daily: Bullish score | daily | 93.19 | -6.81 | 7 | 0.0 | -4.38 | -0.37 | -12.76 | 13 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 93.09 | -6.92 | 0 | — | 4.72 | 0.86 | -13.89 | 1 |
| 31 | Agent | meta | 92.93 | -7.07 | 75 | 40.0 | -9.31 | -5.27 | -9.63 | 244 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 92.42 | -7.58 | 0 | — | -16.33 | -3.08 | -19.22 | 1 |
| 33 | MACD cross · 1h | trend | 92.26 | -7.74 | 154 | 22.1 | -13.47 | -1.83 | -24.65 | 462 |
| 34 | Bollinger breakout · 1h | breakout | 91.96 | -8.04 | 79 | 30.4 | 6.34 | 0.99 | -14.21 | 273 |
| 35 | RSI momentum · 1h | momentum | 91.74 | -8.26 | 73 | 17.8 | 1.09 | 0.34 | -25.77 | 222 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.61 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.49 | -8.51 | 74 | 13.5 | 0.18 | 0.21 | -22.72 | 215 |
| 38 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 77 | 16.9 | -5.93 | -0.40 | -31.52 | 235 |
| 39 | Opening range 30m | breakout | 90.48 | -9.52 | 170 | 22.9 | -12.79 | -3.70 | -17.60 | 570 |
| 40 | Stochastic reversion · 1h | reversion | 90.34 | -9.66 | 128 | 44.5 | -16.52 | -3.08 | -19.84 | 350 |
| 41 | Ichimoku · 1h | trend | 90.31 | -9.69 | 51 | 15.7 | 0.97 | 0.32 | -22.64 | 122 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -5.99 | -2.27 | -7.17 | 120 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.15 | -6.89 | -24.89 | 248 |
| 44 | MFI reversion · 1h | reversion | 89.39 | -10.61 | 188 | 29.8 | -17.19 | -2.98 | -19.64 | 145 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -17.13 | -0.64 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.29 | -11.71 | 164 | 18.9 | -11.47 | -1.00 | -35.22 | 322 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.66 | -2.07 | -29.15 | 211 |
| 48 | MACD zero-line · 1h | trend | 87.77 | -12.23 | 74 | 16.2 | -21.32 | -4.10 | -22.27 | 225 |
| 49 | Z-score reversion · 1h | reversion | 87.41 | -12.59 | 72 | 34.7 | -11.52 | -2.04 | -17.27 | 183 |
| 50 | Agent (ML meta-label) | meta | 86.78 | -13.22 | 568 | 18.5 | -6.60 | -0.92 | -15.54 | 434 |
| 51 | Opening range 15m | breakout | 86.32 | -13.68 | 216 | 20.4 | -18.05 | -4.84 | -21.40 | 709 |
| 52 | ROC + volume · 1h | momentum | 86.12 | -13.88 | 180 | 21.7 | -8.55 | -1.02 | -25.31 | 398 |
| 53 | Donchian 20/10 · 1h | breakout | 86.08 | -13.92 | 72 | 19.4 | -0.12 | 0.19 | -20.56 | 218 |
| 54 | VWAP momentum · 1h | momentum | 85.82 | -14.18 | 354 | 21.8 | -35.48 | -5.23 | -43.06 | 1251 |
| 55 | Heikin-Ashi · 1h | trend | 85.67 | -14.33 | 170 | 26.5 | -30.51 | -4.96 | -39.15 | 671 |
| 56 | Three white soldiers | momentum | 85.61 | -14.39 | 196 | 18.4 | -47.54 | -19.03 | -48.92 | 600 |
| 57 | EMA 9/21 cross · 1h | trend | 84.52 | -15.48 | 120 | 12.5 | -5.82 | -0.46 | -29.09 | 319 |
| 58 | Bollinger reversion · 1h | reversion | 83.70 | -16.30 | 132 | 31.8 | -28.16 | -6.09 | -31.47 | 340 |
| 59 | Williams %R · 1h | reversion | 83.22 | -16.78 | 167 | 42.5 | -32.09 | -5.27 | -34.85 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 82.74 | -17.26 | 61 | 23.0 | -11.98 | -2.09 | -18.95 | 172 |
| 61 | CCI reversion · 1h | reversion | 82.71 | -17.29 | 141 | 41.8 | -16.22 | -2.09 | -23.38 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 79.86 | -20.14 | 182 | 25.3 | -32.43 | -5.99 | -33.66 | 519 |
| 63 | RSI(14) reversion | reversion | 66.68 | -33.32 | 570 | 28.8 | -73.26 | -16.18 | -74.17 | 1560 |
| 64 | ROC + volume | momentum | 66.17 | -33.83 | 515 | 22.1 | -74.60 | -16.86 | -76.47 | 1688 |
| 65 | Volume breakout | breakout | 65.01 | -34.99 | 313 | 13.4 | -63.56 | -17.88 | -63.56 | 888 |
| 66 | Squeeze breakout | breakout | 64.37 | -35.63 | 416 | 14.7 | -63.04 | -17.61 | -63.44 | 1214 |
| 67 | Donchian 55/20 | breakout | 63.31 | -36.69 | 403 | 17.4 | -68.98 | -14.25 | -71.15 | 1273 |
| 68 | EMA 20/50 cross | trend | 61.65 | -38.35 | 423 | 18.7 | -77.13 | -14.90 | -78.49 | 1442 |
| 69 | VWAP reversion | reversion | 58.34 | -41.66 | 583 | 24.5 | -72.42 | -14.97 | -72.66 | 1427 |
| 70 | AI bee: Boozy | ai | 57.81 | -42.19 | 278 | 5.4 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.11 | -43.89 | 578 | 15.2 | -83.46 | -26.18 | -83.60 | 1842 |
| 72 | Supertrend | trend | 54.63 | -45.37 | 590 | 19.2 | -86.34 | -19.91 | -86.59 | 1908 |
| 73 | Ichimoku | trend | 53.41 | -46.59 | 509 | 10.4 | -82.06 | -22.36 | -82.14 | 1713 |
| 74 | AI bee: Bizzy | ai | 50.95 | -49.05 | 1026 | 8.6 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.84 | -98.63 | 5314 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -28.55 | -93.48 | 2578 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -23.96 | -90.66 | 2353 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.56 | -26.17 | -91.56 | 2320 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -31.28 | -97.46 | 3510 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -33.89 | -96.61 | 3566 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -24.10 | -94.36 | 2607 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -34.83 | -99.40 | 5732 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.13 | -24.93 | -91.19 | 2625 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.19 | -30.20 | -96.19 | 3549 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.89 | -99.73 | 6157 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -28.54 | -91.87 | 2365 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -36.08 | -97.47 | 3638 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -35.17 | -98.53 | 4683 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -31.50 | -93.53 | 2789 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.41 | -99.55 | 6153 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.08 | -21.74 | -86.37 | 2104 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.40 | -26.05 | -87.79 | 2104 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -31.52 | -96.08 | 3773 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -32.59 | -89.35 | 2105 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -32.39 | -95.85 | 4064 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.53 | -99.89 | 8206 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T18:25 | MFI reversion · 1h | buy | TNA | 9.93 | — | entry |
| 2026-10-15T18:25 | Squeeze breakout | sell | IWM | 12.87 | -0.03 | exit signal |
| 2026-10-15T18:25 | Donchian 55/20 | buy | META | 5.76 | — | entry |
| 2026-10-15T18:25 | Donchian 55/20 | sell | SOL-USD | 6.28 | 0.05 | exit signal |
| 2026-10-15T18:25 | Supertrend | sell | SOL-USD | 3.02 | 0.04 | exit signal |
| 2026-10-15T18:21 | Agent (aggressive) | sell | META | 45.02 | -0.14 | selected signal exited |
| 2026-10-15T18:21 | Agent | sell | META | 18.57 | -0.06 | selected signal exited |
| 2026-10-15T18:21 | ROC + volume | sell | META | 16.56 | -0.03 | exit signal |
| 2026-10-15T18:21 | ROC + volume | sell | DOGE-USD | 16.49 | -0.12 | exit signal |
| 2026-10-15T18:21 | Ichimoku | sell | AMZN | 13.34 | -0.04 | exit signal |
| 2026-10-15T18:21 | Supertrend | sell | AMZN | 3.02 | 0.00 | exit signal |
| 2026-10-15T18:15 | ROC + volume | buy | META | 8.25 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | buy | DOGE-USD | 7.10 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | buy | AMD | 8.23 | — | rebalance up |
| 2026-10-15T18:15 | ROC + volume | sell | SOXL | 8.16 | -0.21 | stop-loss |
| 2026-10-15T18:15 | ROC + volume | sell | ETH-USD | 8.32 | -0.10 | exit signal |
| 2026-10-15T18:15 | ROC + volume | sell | COIN | 8.31 | -0.05 | stop-loss |
| 2026-10-15T18:15 | Ichimoku | buy | TNA | 8.00 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | IWM | 8.02 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | AMZN | 8.90 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | buy | AMD | 6.69 | — | rebalance up |
| 2026-10-15T18:15 | Ichimoku | sell | XRP-USD | 4.45 | 0.04 | exit signal |
| 2026-10-15T18:15 | Ichimoku | sell | META | 4.45 | 0.00 | exit signal |
| 2026-10-15T18:15 | Ichimoku | sell | GOOGL | 5.35 | -0.01 | stop-loss |
| 2026-10-15T18:15 | Ichimoku | sell | DOGE-USD | 5.32 | -0.04 | exit signal |
| 2026-10-15T18:15 | Supertrend | buy | TSLA | 3.21 | — | entry |
| 2026-10-15T18:15 | Supertrend | buy | SQQQ | 3.21 | — | entry signal |
| 2026-10-15T18:15 | Supertrend | sell | TQQQ | 3.01 | -0.00 | exit signal |
| 2026-10-15T18:15 | Supertrend | sell | SPY | 3.01 | -0.00 | exit signal |
| 2026-10-15T18:15 | Supertrend | sell | QQQ | 3.01 | -0.00 | exit signal |
| 2026-10-15T18:15 | Supertrend | sell | COIN | 3.08 | 0.06 | exit signal |
| 2026-10-15T18:10 | AI bee: Bizzy | sell | NANC | 9.76 | -0.03 | Jev: sell (sell p=0.58) after 17 min |
| 2026-10-15T18:10 | Agent | sell | META | 18.54 | -0.05 | rebalance down |
| 2026-10-15T18:10 | Squeeze breakout | sell | NVDA | 12.87 | -0.04 | exit signal |
| 2026-10-15T18:10 | Squeeze breakout | sell | META | 12.88 | -0.03 | stop-loss |
| 2026-10-15T18:10 | Squeeze breakout | sell | COIN | 12.85 | -0.04 | stop-loss |
| 2026-10-15T18:10 | Keltner breakout | sell | MSTR | 11.18 | 0.02 | stop-loss |
| 2026-10-15T18:10 | Keltner breakout | sell | META | 11.25 | -0.03 | stop-loss |
| 2026-10-15T18:10 | Keltner breakout | sell | ETHU | 11.24 | -0.11 | exit signal |
| 2026-10-15T18:10 | Keltner breakout | sell | ETH-USD | 11.22 | -0.11 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 18:25:05.000151+00:00 -> 2026-10-15 18:35:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
