# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T19:25:05.000130+00:00 · 27531 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 14688 decisions in 2940 calls, $0.2054 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T19:25 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-18T19:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T19:25 | 0 / 5 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.51 | -0.49 | 60 | 38.3 | -11.55 | -3.35 | -13.80 | 137 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.92 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | -2.87 | -0.22 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.06 | -2.62 | -6.31 | 279 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 19 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.52 | -5.88 | -19.70 | 140 |
| 20 | Hold BTC | benchmark | 96.13 | -3.87 | 0 | — | 25.40 | 3.06 | -8.68 | 1 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 82 | 19.5 | -12.24 | -2.39 | -13.31 | 251 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 2.93 | 0.72 | -9.46 | 98 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -9.90 | -1.53 | -22.55 | 270 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.16 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.79 | -2.00 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.35 | -5.91 | -12.52 | 233 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.89 | -9.11 | 77 | 16.9 | -17.00 | -2.97 | -27.38 | 216 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.03 | 1.08 | -14.21 | 266 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -16.65 | -1.95 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.81 | -0.93 | -27.05 | 201 |
| 41 | Supertrend · 1h | trend | 88.87 | -11.13 | 85 | 11.8 | -22.71 | -4.71 | -26.17 | 208 |
| 42 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.24 | -7.43 | -25.57 | 226 |
| 43 | OBV trend · 1h | momentum | 87.64 | -12.36 | 170 | 18.2 | -15.89 | -1.82 | -33.85 | 317 |
| 44 | MACD cross · 1h | trend | 87.56 | -12.44 | 181 | 21.5 | -16.45 | -2.13 | -30.43 | 459 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.42 | -13.58 | 143 | 44.1 | -21.22 | -3.89 | -22.11 | 371 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.46 | -14.54 | 82 | 15.9 | -21.19 | -3.99 | -24.00 | 217 |
| 49 | Donchian 20/10 · 1h | breakout | 84.68 | -15.32 | 79 | 17.7 | 1.42 | 0.38 | -21.63 | 212 |
| 50 | MFI reversion · 1h | reversion | 83.75 | -16.25 | 205 | 30.2 | -21.94 | -3.48 | -22.26 | 145 |
| 51 | Three white soldiers | momentum | 83.56 | -16.44 | 216 | 18.5 | -47.43 | -19.44 | -47.71 | 603 |
| 52 | Z-score reversion · 1h | reversion | 82.75 | -17.25 | 89 | 30.3 | -16.92 | -2.98 | -21.06 | 186 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -13.62 | -1.80 | -27.31 | 395 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -12.10 | -1.84 | -20.97 | 364 |
| 55 | EMA 9/21 cross · 1h | trend | 80.97 | -19.03 | 131 | 11.5 | -11.35 | -1.37 | -30.34 | 313 |
| 56 | Heikin-Ashi · 1h | trend | 80.95 | -19.05 | 206 | 22.3 | -32.42 | -5.33 | -42.19 | 678 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.58 | -5.87 | -36.68 | 528 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.99 | -2.68 | -21.89 | 164 |
| 59 | Bollinger reversion · 1h | reversion | 79.83 | -20.17 | 146 | 31.5 | -30.89 | -6.45 | -32.75 | 353 |
| 60 | VWAP momentum · 1h | momentum | 79.78 | -20.22 | 408 | 20.1 | -37.82 | -5.77 | -46.73 | 1253 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.99 | -2.76 | -27.23 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.46 | -6.61 | -37.11 | 540 |
| 63 | Volume breakout | breakout | 62.76 | -37.24 | 335 | 12.8 | -62.98 | -18.17 | -63.54 | 877 |
| 64 | ROC + volume | momentum | 62.11 | -37.89 | 560 | 21.6 | -75.91 | -17.88 | -77.81 | 1726 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.77 | -17.92 | -64.76 | 1212 |
| 66 | Donchian 55/20 | breakout | 59.13 | -40.87 | 455 | 17.1 | -69.05 | -14.66 | -72.67 | 1279 |
| 67 | RSI(14) reversion | reversion | 59.11 | -40.90 | 682 | 25.2 | -74.61 | -16.79 | -74.67 | 1632 |
| 68 | EMA 20/50 cross | trend | 56.85 | -43.15 | 480 | 18.3 | -76.88 | -15.21 | -80.07 | 1437 |
| 69 | VWAP reversion | reversion | 53.39 | -46.61 | 709 | 23.6 | -73.51 | -15.70 | -73.53 | 1523 |
| 70 | Keltner breakout | breakout | 52.35 | -47.65 | 633 | 15.5 | -83.02 | -27.15 | -83.06 | 1818 |
| 71 | AI bee: Boozy | ai | 52.17 | -47.83 | 333 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.35 | -98.65 | 5326 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -30.72 | -93.52 | 2588 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.58 | -20.58 | -87.74 | 1910 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.35 | -24.87 | -90.87 | 2356 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.18 | -26.64 | -91.18 | 2299 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.49 | -33.11 | -97.49 | 3527 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.77 | -37.05 | -96.77 | 3613 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.19 | -26.89 | -94.54 | 2571 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -23.45 | -82.50 | 1724 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -37.56 | -99.40 | 5823 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.31 | -26.20 | -91.59 | 2636 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.14 | -32.45 | -96.14 | 3526 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.20 | -99.74 | 6235 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -29.67 | -91.75 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -39.14 | -97.47 | 3649 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.51 | -98.52 | 4772 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -33.84 | -93.70 | 2804 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.52 | -99.54 | 6248 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.89 | -22.59 | -86.90 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.64 | -88.22 | 2176 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -33.12 | -95.91 | 3812 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -34.05 | -89.28 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.86 | -34.45 | -95.86 | 4159 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.55 | -99.90 | 8319 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T19:25 | Z-score reversion · 1h | buy | BTC-USD | 11.72 | — | entry |
| 2026-10-18T19:25 | Z-score reversion · 1h | sell | ETH-USD | 11.72 | -0.14 | stop-loss |
| 2026-10-18T19:00 | MFI reversion · 1h | buy | XRP-USD | 20.98 | — | entry signal |
| 2026-10-18T19:00 | Stochastic reversion · 1h | buy | ETH-USD | 4.12 | — | entry signal |
| 2026-10-18T18:10 | RSI(14) reversion | sell | BTC-USD | 14.74 | -0.08 | exit signal |
| 2026-10-18T18:00 | MFI reversion · 1h | buy | DOGE-USD | 21.00 | — | entry signal |
| 2026-10-18T18:00 | Stochastic reversion · 1h | buy | XRP-USD | 4.33 | — | entry signal |
| 2026-10-18T18:00 | Stochastic reversion · 1h | buy | SOL-USD | 4.33 | — | entry signal |
| 2026-10-18T17:40 | Agent (ML meta-label) | sell | DOGE-USD | 7.43 | -0.05 | selected signal exited |
| 2026-10-18T17:35 | Agent (ML meta-label) | buy | DOGE-USD | 7.48 | — | entry |
| 2026-10-18T17:27 | Agent (ML meta-label) | sell | DOGE-USD | 8.19 | -0.04 | selected signal exited |
| 2026-10-18T17:10 | Agent (ML meta-label) | buy | DOGE-USD | 8.23 | — | entry |
| 2026-10-18T17:05 | Stochastic reversion · 1h | buy | DOGE-USD | 4.81 | — | entry |
| 2026-10-18T17:05 | RSI(14) reversion | sell | DOGE-USD | 14.83 | 0.02 | exit signal |
| 2026-10-18T16:35 | VWAP reversion | buy | ETH-USD | 10.62 | — | entry signal |
| 2026-10-18T16:35 | VWAP reversion | sell | DOGE-USD | 2.67 | -0.02 | rebalance down |
| 2026-10-18T16:30 | VWAP reversion | buy | DOGE-USD | 2.69 | — | rebalance up |
| 2026-10-18T16:30 | VWAP reversion | sell | ETH-USD | 10.64 | -0.12 | stop-loss |
| 2026-10-18T16:30 | RSI(14) reversion | sell | ETH-USD | 14.71 | -0.17 | stop-loss |
| 2026-10-18T16:05 | Agent (ML meta-label) | sell | DOGE-USD | 7.43 | -0.05 | selected signal exited |
| 2026-10-18T16:00 | Stochastic reversion · 1h | buy | BTC-USD | 5.09 | — | entry signal |
| 2026-10-18T16:00 | VWAP reversion · 1h | buy | SOL-USD | 2.31 | — | entry signal |
| 2026-10-18T16:00 | VWAP reversion · 1h | buy | ETH-USD | 7.66 | — | entry signal |
| 2026-10-18T16:00 | Bollinger reversion · 1h | buy | ETH-USD | 1.45 | — | entry signal |
| 2026-10-18T16:00 | Bollinger reversion · 1h | buy | BTC-USD | 7.26 | — | entry signal |
| 2026-10-18T15:50 | RSI(14) reversion | buy | DOGE-USD | 14.81 | — | entry signal |
| 2026-10-18T15:40 | Agent (ML meta-label) | buy | DOGE-USD | 7.49 | — | entry |
| 2026-10-18T15:40 | Z-score reversion · 1h | buy | ETH-USD | 11.86 | — | entry |
| 2026-10-18T15:40 | Z-score reversion · 1h | sell | DOGE-USD | 11.74 | -0.13 | stop-loss |
| 2026-10-18T15:40 | RSI(14) reversion | sell | XRP-USD | 14.82 | -0.16 | stop-loss |
| 2026-10-18T15:40 | RSI(14) reversion | sell | DOGE-USD | 14.81 | -0.19 | stop-loss |
| 2026-10-18T15:30 | Z-score reversion · 1h | buy | DOGE-USD | 11.87 | — | entry |
| 2026-10-18T15:30 | Z-score reversion · 1h | sell | XRP-USD | 11.98 | -0.32 | stop-loss |
| 2026-10-18T15:05 | RSI(14) reversion | buy | BTC-USD | 14.83 | — | entry signal |
| 2026-10-18T15:00 | Supertrend · 1h | sell | BTC-USD | 21.84 | -0.42 | exit signal |
| 2026-10-18T15:00 | MACD cross · 1h | sell | BTC-USD | 21.82 | -0.22 | exit signal |
| 2026-10-18T14:45 | VWAP reversion | buy | XRP-USD | 10.76 | — | entry signal |
| 2026-10-18T14:45 | VWAP reversion | buy | SOL-USD | 10.76 | — | entry signal |
| 2026-10-18T14:45 | VWAP reversion | buy | ETH-USD | 10.76 | — | entry signal |
| 2026-10-18T14:45 | VWAP reversion | buy | DOGE-USD | 10.76 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 19:25:05.000130+00:00 -> 2026-10-18 19:35:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
