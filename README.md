# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T20:25:05.000216+00:00 · 25158 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.01 (-7.99%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.16 | -0.21 |
| SQQQ | 19.19 | +0.82 |

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

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 22.89 · VIX 20.03 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 39107 decisions in 3025 calls, $0.4823 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T20:25 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-16T20:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T20:25 | 0 / 4 / 1 | COIN 66% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.87 | 4.87 | 0 | — | 5.91 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.00 | -0.00 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.60 | -0.40 | 59 | 39.0 | -11.41 | -3.32 | -13.79 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.85 | -1.15 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.81 | -1.19 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Hold SPY | benchmark | 98.68 | -1.32 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 15 | Copy: Insider buying | copy | 98.23 | -1.77 | 20 | 45.0 | -12.32 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.15 | -2.85 | 108 | 33.3 | -7.63 | -2.84 | -11.55 | 290 |
| 17 | Hold BTC | benchmark | 96.85 | -3.15 | 0 | — | 28.83 | 3.38 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.59 | -3.41 | 0 | — | -2.51 | -1.00 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.46 | -3.54 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.23 | -3.77 | 87 | 24.1 | -21.17 | -6.32 | -22.47 | 151 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.46 | -4.54 | 0 | — | -6.69 | -2.61 | -7.75 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.81 | -5.19 | 81 | 19.8 | -9.12 | -1.64 | -13.33 | 260 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Parabolic SAR · 1h | trend | 93.26 | -6.74 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 27 | EMA 20/50 cross · 1h | trend | 92.93 | -7.07 | 54 | 14.8 | -4.00 | -0.35 | -22.92 | 128 |
| 28 | Daily: Momentum burst | daily | 92.88 | -7.12 | 5 | 20.0 | -7.36 | -0.98 | -20.58 | 42 |
| 29 | Agent (aggressive) | meta | 92.18 | -7.82 | 38 | 31.6 | -6.04 | -2.09 | -9.30 | 121 |
| 30 | Agent | meta | 92.01 | -7.99 | 77 | 39.0 | -11.05 | -6.17 | -12.05 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.80 | -0.11 | -14.55 | 118 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.21 | -8.79 | 76 | 17.1 | 0.88 | 0.32 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.72 | 0.92 | -14.21 | 273 |
| 35 | Daily: Bullish score | daily | 90.71 | -9.29 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.40 | -9.60 | 80 | 16.2 | -7.40 | -0.56 | -33.23 | 233 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.50 | -10.50 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.34 | -10.66 | 84 | 11.9 | -3.70 | -0.22 | -30.09 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.34 | -10.66 | 0 | — | -0.11 | 0.16 | -14.37 | 1 |
| 41 | MACD cross · 1h | trend | 89.18 | -10.82 | 171 | 22.8 | -14.53 | -1.93 | -27.78 | 453 |
| 42 | Keltner breakout · 1h | breakout | 89.11 | -10.89 | 52 | 23.1 | -9.24 | -1.15 | -27.05 | 210 |
| 43 | Connors RSI(2) · 1h | reversion | 88.03 | -11.97 | 145 | 40.0 | -25.14 | -7.57 | -26.03 | 239 |
| 44 | OBV trend · 1h | momentum | 88.01 | -11.99 | 169 | 18.3 | -8.61 | -0.69 | -33.94 | 319 |
| 45 | Stochastic reversion · 1h | reversion | 86.73 | -13.27 | 136 | 43.4 | -20.68 | -3.75 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.09 | -4.55 | -23.33 | 220 |
| 48 | Max aggression: 1-day momentum | meta | 86.01 | -13.99 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.98 | -15.02 | 78 | 17.9 | 0.91 | 0.32 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.68 | -20.07 | -48.37 | 609 |
| 51 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -21.87 | -3.67 | -22.58 | 143 |
| 52 | Heikin-Ashi · 1h | trend | 83.92 | -16.08 | 189 | 24.3 | -31.13 | -5.13 | -40.33 | 673 |
| 53 | VWAP momentum · 1h | momentum | 83.90 | -16.10 | 387 | 21.2 | -35.96 | -5.47 | -43.85 | 1251 |
| 54 | Z-score reversion · 1h | reversion | 83.43 | -16.57 | 86 | 31.4 | -15.49 | -2.68 | -19.86 | 182 |
| 55 | Agent (ML meta-label) | meta | 83.19 | -16.81 | 609 | 19.2 | -6.87 | -0.92 | -16.97 | 379 |
| 56 | ROC + volume · 1h | momentum | 82.99 | -17.01 | 192 | 21.4 | -12.42 | -1.65 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.26 | -17.74 | 127 | 11.8 | -6.92 | -0.62 | -29.70 | 318 |
| 58 | Bollinger reversion · 1h | reversion | 80.17 | -19.83 | 138 | 31.2 | -30.35 | -6.26 | -32.42 | 345 |
| 59 | Williams %R · 1h | reversion | 80.14 | -19.86 | 180 | 42.2 | -34.58 | -5.64 | -35.92 | 528 |
| 60 | RSI(14) reversion · 1h | reversion | 80.07 | -19.93 | 74 | 20.3 | -14.37 | -2.55 | -21.70 | 163 |
| 61 | CCI reversion · 1h | reversion | 79.09 | -20.91 | 161 | 38.5 | -19.38 | -2.52 | -25.42 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 76.16 | -23.84 | 205 | 25.4 | -34.99 | -6.30 | -35.88 | 531 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.04 | -18.12 | -63.05 | 878 |
| 64 | ROC + volume | momentum | 63.28 | -36.72 | 548 | 21.9 | -76.03 | -17.80 | -77.59 | 1696 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.94 | -18.04 | -63.96 | 1217 |
| 66 | RSI(14) reversion ⏸ | reversion | 62.42 | -37.58 | 646 | 25.9 | -74.71 | -16.73 | -74.79 | 1635 |
| 67 | Donchian 55/20 | breakout | 61.53 | -38.47 | 435 | 17.9 | -69.06 | -14.57 | -71.81 | 1283 |
| 68 | EMA 20/50 cross | trend | 59.91 | -40.09 | 455 | 19.3 | -77.25 | -15.29 | -79.04 | 1453 |
| 69 | AI bee: Boozy | ai | 55.72 | -44.28 | 299 | 6.7 | — | — | — | — |
| 70 | VWAP reversion | reversion | 55.59 | -44.41 | 674 | 23.6 | -73.67 | -15.64 | -73.75 | 1503 |
| 71 | Keltner breakout | breakout | 54.72 | -45.28 | 607 | 16.1 | -83.48 | -27.11 | -83.60 | 1841 |
| 72 | Ichimoku | trend | 52.02 | -47.98 | 553 | 11.8 | -82.02 | -23.20 | -82.15 | 1735 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.56 | -20.53 | -87.07 | 1916 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -29.92 | -98.63 | 5312 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -30.35 | -93.50 | 2598 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -24.86 | -90.54 | 2367 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.73 | -91.83 | 2346 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.81 | -97.46 | 3532 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -36.67 | -96.71 | 3574 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -26.69 | -94.45 | 2616 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -36.91 | -99.41 | 5841 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.39 | -26.13 | -91.43 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -32.56 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.90 | -99.74 | 6232 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.71 | -91.77 | 2370 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -38.70 | -97.46 | 3654 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.10 | -98.52 | 4778 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.66 | -33.40 | -93.68 | 2807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.38 | -99.55 | 6263 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.41 | -86.74 | 2165 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.20 | -27.50 | -88.24 | 2160 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -33.11 | -96.06 | 3830 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -34.41 | -89.45 | 2117 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -34.41 | -95.88 | 4160 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.53 | -99.89 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T20:25 | EMA 20/50 cross | buy | BTC-USD | 14.99 | — | entry signal |
| 2026-10-16T20:15 | Agent (ML meta-label) | sell | ETH-USD | 7.08 | -0.05 | selected signal exited |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | ETH-USD | 7.13 | — | entry |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | BTC-USD | 8.33 | — | entry |
| 2026-10-16T20:05 | ROC + volume | buy | SOL-USD | 15.83 | — | entry signal |
| 2026-10-16T20:00 | Z-score reversion · 1h | buy | XRP-USD | 12.31 | — | entry signal |
| 2026-10-16T19:55 | Agent (rotation) | sell | SQQQ | 66.05 | 2.53 | selected signal exited |
| 2026-10-16T19:55 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.67 | 1.26 | target is flat |
| 2026-10-16T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 107.79 | 4.69 | target is flat |
| 2026-10-16T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 107.08 | 3.54 | target is flat |
| 2026-10-16T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 99.09 | 0.36 | target is flat |
| 2026-10-16T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 105.88 | 5.95 | target is flat |
| 2026-10-16T19:55 | Agent (ML meta-label) | buy | ETHU | 9.26 | — | entry |
| 2026-10-16T19:55 | Agent (ML meta-label) | sell | SQQQ | 9.33 | 0.03 | selected signal exited |
| 2026-10-16T19:55 | VWAP reversion | buy | XRP-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | SOL-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | ETH-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | DOGE-USD | 8.82 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | BTC-USD | 8.90 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | sell | UPRO | 2.42 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TSLA | 2.33 | 0.02 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TQQQ | 2.41 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TNA | 2.22 | -0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TECL | 2.42 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | SPY | 2.32 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | QQQ | 2.41 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | PLTR | 2.24 | -0.02 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | NVDA | 2.42 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | MSTR | 2.44 | 0.03 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | MSFT | 2.24 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | META | 2.32 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | LABU | 2.24 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | IWM | 2.23 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | GOOGL | 2.33 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | ETHU | 2.26 | 0.03 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | COIN | 2.34 | 0.04 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | AMZN | 2.24 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | AAPL | 2.18 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | Opening range 30m | sell | SQQQ | 23.58 | 0.98 | end-of-day flatten |
| 2026-10-16T19:55 | Opening range 15m | sell | SQQQ | 18.28 | 0.83 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 20:25:05.000216+00:00 -> 2026-10-16 20:35:05.000216+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
