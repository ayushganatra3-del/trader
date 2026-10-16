# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T16:25:05.000146+00:00 · 24966 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.55 (-8.45%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.28 | -0.10 |
| SQQQ | 18.61 | +0.24 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 23261 decisions in 2449 calls, $0.2956 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T16:25 | 5 / 16 / 10 | cash |  |
| Breezy | 2026-10-16T16:25 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-10-16T16:25 | 3 / 25 / 3 | BITX 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.41 | 4.41 | 9 | 66.7 | 6.05 | 2.60 | -3.27 | 19 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.16 | 4.16 | 0 | — | 5.46 | 2.63 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 10 | 70.0 | -1.72 | -0.49 | -9.61 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 102.56 | 2.56 | 14 | 35.7 | 5.01 | 1.51 | -7.55 | 44 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.14 | 1.14 | 1 | 100.0 | 2.50 | 0.68 | -7.93 | 9 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.18 | 0.18 | 0 | — | 4.47 | 1.74 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | VWAP reversion · 1h | reversion | 99.84 | -0.16 | 59 | 39.0 | -11.47 | -3.33 | -13.79 | 124 |
| 10 | Hold SPY | benchmark | 99.01 | -0.99 | 0 | — | -0.99 | -0.53 | -3.23 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 12 | Copy: Insider buying | copy | 98.23 | -1.77 | 20 | 45.0 | -12.15 | -2.07 | -20.62 | 75 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 98.09 | -1.91 | 51 | 31.4 | 1.35 | 0.78 | -2.96 | 69 |
| 14 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 36 | 16.7 | 8.26 | 1.12 | -22.12 | 109 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.08 | -2.92 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.91 | -3.09 | 0 | — | -1.93 | -0.77 | -4.50 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 96.83 | -3.17 | 0 | — | -6.11 | -3.38 | -6.38 | 1 |
| 18 | Hold BTC | benchmark | 96.64 | -3.36 | 0 | — | 29.04 | 3.38 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 96.28 | -3.72 | 87 | 24.1 | -21.55 | -6.39 | -22.30 | 152 |
| 20 | Max aggression: 5-day momentum | meta | 95.83 | -4.17 | 8 | 37.5 | -19.46 | -1.71 | -34.64 | 26 |
| 21 | Agent (rotation) | meta | 95.77 | -4.23 | 107 | 32.7 | -10.57 | -3.64 | -13.20 | 297 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.73 | -5.27 | 80 | 20.0 | -8.80 | -1.56 | -13.33 | 258 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.80 | 0.86 | -9.46 | 100 |
| 25 | Daily: Momentum burst | daily | 93.42 | -6.58 | 5 | 20.0 | -6.54 | -0.85 | -19.50 | 42 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 92.70 | -7.30 | 95 | 22.1 | 2.82 | 0.54 | -22.55 | 278 |
| 28 | EMA 20/50 cross · 1h | trend | 92.53 | -7.47 | 53 | 15.1 | -4.63 | -0.44 | -22.92 | 129 |
| 29 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.80 | -0.11 | -14.55 | 118 |
| 30 | Agent | meta | 91.55 | -8.45 | 77 | 39.0 | -11.36 | -6.27 | -12.01 | 245 |
| 31 | Daily: Bullish score | daily | 90.83 | -9.17 | 7 | 0.0 | -5.69 | -0.54 | -12.76 | 13 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 90.82 | -9.18 | 0 | — | -18.43 | -3.55 | -19.22 | 1 |
| 33 | RSI momentum · 1h | momentum | 90.80 | -9.20 | 75 | 17.3 | 0.46 | 0.27 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.48 | 0.89 | -14.21 | 274 |
| 35 | Agent (aggressive) | meta | 90.76 | -9.24 | 38 | 31.6 | -7.48 | -2.76 | -9.42 | 123 |
| 36 | Opening range 30m | breakout | 90.64 | -9.36 | 192 | 29.7 | -12.65 | -3.49 | -17.60 | 572 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 38 | MACD cross · 1h | trend | 90.27 | -9.73 | 166 | 23.5 | -13.63 | -1.81 | -26.80 | 458 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 90.11 | -9.89 | 0 | — | 1.01 | 0.32 | -13.89 | 1 |
| 40 | Triple EMA stack · 1h | trend | 89.65 | -10.35 | 80 | 16.2 | -8.94 | -0.73 | -33.23 | 235 |
| 41 | Supertrend · 1h | trend | 89.55 | -10.45 | 79 | 12.7 | -3.02 | -0.14 | -29.43 | 213 |
| 42 | Stochastic reversion · 1h | reversion | 88.78 | -11.22 | 132 | 44.7 | -18.73 | -3.52 | -20.19 | 349 |
| 43 | Connors RSI(2) · 1h | reversion | 88.71 | -11.29 | 144 | 40.3 | -24.20 | -7.29 | -25.04 | 242 |
| 44 | Keltner breakout · 1h | breakout | 88.42 | -11.58 | 52 | 23.1 | -10.01 | -1.26 | -27.05 | 210 |
| 45 | Max aggression: 1-day momentum | meta | 88.02 | -11.98 | 14 | 35.7 | -8.38 | -0.09 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 87.57 | -12.43 | 168 | 18.5 | -9.24 | -0.76 | -34.01 | 321 |
| 47 | Opening range 15m | breakout | 86.20 | -13.80 | 241 | 25.3 | -17.62 | -4.58 | -21.40 | 709 |
| 48 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.25 | -4.56 | -23.33 | 224 |
| 49 | Z-score reversion · 1h | reversion | 85.65 | -14.35 | 78 | 34.6 | -12.79 | -2.33 | -17.34 | 178 |
| 50 | MFI reversion · 1h | reversion | 85.40 | -14.60 | 200 | 30.5 | -19.94 | -3.45 | -20.49 | 141 |
| 51 | Three white soldiers | momentum | 84.72 | -15.28 | 207 | 18.8 | -47.86 | -19.97 | -48.52 | 609 |
| 52 | Agent (ML meta-label) | meta | 84.64 | -15.36 | 584 | 19.0 | -3.98 | -0.45 | -15.95 | 395 |
| 53 | Donchian 20/10 · 1h | breakout | 84.58 | -15.42 | 77 | 18.2 | 0.39 | 0.26 | -21.63 | 219 |
| 54 | VWAP momentum · 1h | momentum | 83.29 | -16.71 | 386 | 21.2 | -36.58 | -5.53 | -43.85 | 1253 |
| 55 | Heikin-Ashi · 1h | trend | 83.27 | -16.73 | 189 | 24.3 | -31.62 | -5.15 | -40.33 | 673 |
| 56 | ROC + volume · 1h | momentum | 82.77 | -17.23 | 190 | 21.6 | -12.47 | -1.65 | -26.33 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.71 | -17.29 | 125 | 12.0 | -6.94 | -0.62 | -29.26 | 321 |
| 58 | Williams %R · 1h | reversion | 82.13 | -17.87 | 177 | 42.9 | -32.70 | -5.41 | -34.85 | 523 |
| 59 | Bollinger reversion · 1h | reversion | 82.09 | -17.91 | 136 | 31.6 | -28.54 | -6.13 | -31.36 | 335 |
| 60 | RSI(14) reversion · 1h | reversion | 81.41 | -18.59 | 66 | 22.7 | -13.13 | -2.39 | -19.96 | 164 |
| 61 | CCI reversion · 1h | reversion | 81.01 | -18.99 | 149 | 41.6 | -17.07 | -2.24 | -23.38 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 78.02 | -21.98 | 196 | 26.0 | -33.24 | -6.15 | -33.95 | 516 |
| 63 | RSI(14) reversion | reversion | 64.19 | -35.80 | 599 | 27.9 | -74.13 | -16.81 | -74.20 | 1594 |
| 64 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.45 | -18.18 | -63.45 | 892 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.95 | -17.80 | -63.91 | 1217 |
| 66 | ROC + volume | momentum | 63.23 | -36.77 | 546 | 21.8 | -75.75 | -17.43 | -77.33 | 1716 |
| 67 | Donchian 55/20 | breakout | 61.03 | -38.97 | 434 | 17.7 | -69.49 | -14.58 | -71.84 | 1287 |
| 68 | EMA 20/50 cross | trend | 59.56 | -40.44 | 452 | 19.2 | -77.46 | -15.25 | -79.04 | 1455 |
| 69 | AI bee: Boozy | ai | 56.65 | -43.35 | 290 | 5.5 | — | — | — | — |
| 70 | VWAP reversion | reversion | 56.58 | -43.42 | 608 | 23.7 | -73.05 | -15.36 | -73.11 | 1458 |
| 71 | Keltner breakout | breakout | 54.35 | -45.65 | 606 | 16.0 | -83.72 | -26.88 | -83.74 | 1846 |
| 72 | Supertrend | trend | 51.88 | -48.12 | 631 | 19.8 | -86.50 | -20.44 | -86.84 | 1914 |
| 73 | Ichimoku | trend | 51.63 | -48.37 | 551 | 11.6 | -82.14 | -22.92 | -82.16 | 1735 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.58 | -98.65 | 5316 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -29.96 | -93.54 | 2600 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -24.67 | -90.62 | 2371 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.80 | -27.13 | -91.83 | 2344 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -32.24 | -97.47 | 3530 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -35.89 | -96.72 | 3611 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -26.22 | -94.48 | 2624 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.87 | -99.40 | 5767 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.46 | -25.75 | -91.47 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.69 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.78 | -99.73 | 6190 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -29.45 | -91.86 | 2375 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -37.67 | -97.47 | 3655 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.28 | -98.48 | 4727 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.71 | -32.74 | -93.72 | 2808 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.21 | -99.54 | 6221 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.38 | -22.25 | -86.42 | 2140 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.74 | -27.02 | -87.76 | 2134 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -32.38 | -95.98 | 3795 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -33.76 | -89.33 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.82 | -33.73 | -95.83 | 4122 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.09 | -99.89 | 8261 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T16:25 | Agent (ML meta-label) | sell | COIN | 2.15 | -0.00 | selected signal exited |
| 2026-10-16T16:25 | RSI(14) reversion | buy | SOL-USD | 3.21 | — | entry |
| 2026-10-16T16:25 | RSI(14) reversion | sell | AMD | 3.21 | 0.01 | rebalance down |
| 2026-10-16T16:25 | ROC + volume | sell | SQQQ | 15.75 | -0.08 | exit signal |
| 2026-10-16T16:25 | EMA 20/50 cross | buy | NVDA | 14.89 | — | entry signal |
| 2026-10-16T16:20 | Agent (ML meta-label) | buy | NVDA | 4.23 | — | entry |
| 2026-10-16T16:20 | Ichimoku | buy | NVDA | 12.91 | — | entry signal |
| 2026-10-16T16:15 | RSI(14) reversion | buy | META | 1.50 | — | entry |
| 2026-10-16T16:15 | RSI(14) reversion | sell | ETHU | 1.50 | 0.01 | target is flat |
| 2026-10-16T16:10 | AI bee: Boozy | buy | BITX | 29.90 | — | Jev: buy (buy p=0.53) |
| 2026-10-16T16:10 | Z-score reversion · 1h | sell | TECL | 7.08 | -0.20 | stop-loss |
| 2026-10-16T16:10 | VWAP reversion | buy | BTC-USD | 1.49 | — | entry signal |
| 2026-10-16T16:10 | RSI(14) reversion | buy | ETHU | 1.49 | — | entry signal |
| 2026-10-16T16:10 | RSI(14) reversion | buy | ETH-USD | 4.92 | — | entry signal |
| 2026-10-16T16:10 | RSI(14) reversion | buy | BTC-USD | 4.92 | — | entry signal |
| 2026-10-16T16:10 | RSI(14) reversion | buy | BITX | 4.92 | — | entry signal |
| 2026-10-16T16:05 | Agent (ML meta-label) | sell | NVDA | 4.54 | -0.04 | selected signal exited |
| 2026-10-16T16:05 | Agent (ML meta-label) | sell | BITX | 3.52 | -0.11 | selected signal exited |
| 2026-10-16T16:05 | MFI reversion · 1h | buy | ETHU | 4.26 | — | rebalance up |
| 2026-10-16T16:05 | CCI reversion · 1h | buy | TSLA | 4.23 | — | rebalance up |
| 2026-10-16T16:05 | CCI reversion · 1h | sell | GOOGL | 4.48 | -0.12 | stop-loss |
| 2026-10-16T16:05 | Williams %R · 1h | buy | TSLA | 4.96 | — | rebalance up |
| 2026-10-16T16:05 | Williams %R · 1h | buy | SOXL | 4.15 | — | rebalance up |
| 2026-10-16T16:05 | Williams %R · 1h | buy | META | 5.08 | — | rebalance up |
| 2026-10-16T16:05 | Williams %R · 1h | buy | AMZN | 4.96 | — | rebalance up |
| 2026-10-16T16:05 | Williams %R · 1h | buy | AAPL | 6.47 | — | rebalance up |
| 2026-10-16T16:05 | Williams %R · 1h | sell | TQQQ | 6.76 | -0.18 | stop-loss |
| 2026-10-16T16:05 | Williams %R · 1h | sell | QQQ | 9.11 | -0.11 | stop-loss |
| 2026-10-16T16:05 | Bollinger reversion · 1h | buy | TSLA | 7.33 | — | rebalance up |
| 2026-10-16T16:05 | Bollinger reversion · 1h | buy | TECL | 7.51 | — | rebalance up |
| 2026-10-16T16:05 | Bollinger reversion · 1h | buy | SOXL | 7.41 | — | rebalance up |
| 2026-10-16T16:05 | Bollinger reversion · 1h | buy | NVDA | 7.14 | — | rebalance up |
| 2026-10-16T16:05 | Bollinger reversion · 1h | buy | AMD | 7.24 | — | rebalance up |
| 2026-10-16T16:05 | Bollinger reversion · 1h | sell | TQQQ | 8.91 | -0.41 | stop-loss |
| 2026-10-16T16:05 | Bollinger reversion · 1h | sell | QQQ | 9.13 | -0.19 | stop-loss |
| 2026-10-16T16:05 | Candlestick reversal · 1h | buy | TSLA | 5.83 | — | rebalance up |
| 2026-10-16T16:05 | Candlestick reversal · 1h | buy | TQQQ | 4.48 | — | rebalance up |
| 2026-10-16T16:05 | Candlestick reversal · 1h | buy | SPY | 5.85 | — | rebalance up |
| 2026-10-16T16:05 | Candlestick reversal · 1h | buy | AMZN | 5.86 | — | rebalance up |
| 2026-10-16T16:05 | Candlestick reversal · 1h | buy | AMD | 4.42 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 16:25:05.000146+00:00 -> 2026-10-16 16:35:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
