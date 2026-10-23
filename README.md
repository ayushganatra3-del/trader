# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T15:45:05.000140+00:00 · 33213 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.52 (-10.48%)

Closed trades 99, win rate 39.4%, fees £3.17, max drawdown -10.90%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.77 | -0.17 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 19995 decisions in 2406 calls, $0.2572 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T15:45 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-10-23T15:45 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-23T15:45 | 6 / 23 / 1 | MSTR 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.99 | 6.99 | 0 | — | 8.56 | 4.58 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.40 | 4.40 | 17 | 47.1 | 7.14 | 2.38 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.53 | -3.20 | -13.74 | 153 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.73 | 0.73 | 0 | — | 3.43 | 1.62 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.24 | -0.76 | 72 | 33.3 | 5.40 | 2.65 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.06 | -1.94 | 0 | — | -0.42 | -0.20 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.37 | -3.63 | 119 | 31.1 | -2.02 | -1.18 | -6.22 | 194 |
| 14 | Hold BTC | benchmark | 96.23 | -3.77 | 0 | — | 1.28 | 0.39 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.82 | -4.18 | 0 | — | -0.67 | -0.22 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.42 | -5.58 | 0 | — | -6.56 | -2.78 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.06 | -5.94 | 25 | 40.0 | -14.89 | -2.85 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.74 | -6.26 | 95 | 23.2 | -21.55 | -7.08 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.60 | -6.40 | 238 | 35.3 | -10.49 | -3.26 | -17.21 | 560 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -15.01 | -1.39 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 92.86 | -7.14 | 48 | 16.7 | -16.33 | -3.71 | -17.44 | 98 |
| 25 | Parabolic SAR · 1h | trend | 91.84 | -8.16 | 117 | 25.6 | -21.09 | -5.01 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 91.53 | -8.47 | 10 | 10.0 | -17.66 | -3.43 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.94 | -9.06 | 108 | 18.5 | -11.88 | -2.44 | -14.53 | 255 |
| 30 | Agent | meta | 89.52 | -10.48 | 99 | 39.4 | -10.75 | -7.51 | -11.47 | 204 |
| 31 | Daily: Bullish score | daily | 89.48 | -10.52 | 9 | 0.0 | -8.02 | -1.04 | -14.40 | 14 |
| 32 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.03 | -10.97 | 0 | — | -5.37 | -0.78 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.75 | -11.25 | 105 | 27.6 | -12.48 | -2.48 | -16.55 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.70 | -12.30 | 186 | 45.2 | -19.83 | -3.74 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.37 | -12.63 | 47 | 36.2 | -12.65 | -4.38 | -15.12 | 95 |
| 37 | Opening range 15m | breakout | 86.57 | -13.43 | 305 | 30.2 | -15.53 | -4.52 | -17.87 | 702 |
| 38 | EMA 20/50 cross · 1h | trend | 86.09 | -13.91 | 71 | 11.3 | -22.86 | -4.57 | -25.11 | 138 |
| 39 | Keltner breakout · 1h | breakout | 86.05 | -13.95 | 73 | 23.3 | -22.91 | -4.88 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 85.90 | -14.10 | 108 | 14.8 | -23.83 | -5.04 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.34 | -14.66 | 101 | 15.8 | -21.69 | -4.66 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.22 | -14.78 | 172 | 40.1 | -26.44 | -8.11 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 84.84 | -15.16 | 216 | 23.1 | -22.82 | -4.57 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 84.11 | -15.89 | 106 | 34.0 | -14.54 | -2.45 | -21.48 | 197 |
| 45 | Triple EMA stack · 1h | trend | 83.75 | -16.25 | 98 | 15.3 | -25.95 | -5.20 | -28.44 | 210 |
| 46 | Ichimoku · 1h | trend | 83.66 | -16.34 | 65 | 12.3 | -23.93 | -5.01 | -25.68 | 110 |
| 47 | MFI reversion · 1h | reversion | 82.19 | -17.81 | 256 | 31.6 | -17.41 | -2.85 | -20.54 | 143 |
| 48 | MACD zero-line · 1h | trend | 82.11 | -17.89 | 103 | 15.5 | -21.18 | -4.44 | -24.81 | 217 |
| 49 | Three white soldiers | momentum | 81.33 | -18.67 | 274 | 20.1 | -43.51 | -21.11 | -43.62 | 588 |
| 50 | Williams %R · 1h | reversion | 81.28 | -18.72 | 213 | 44.1 | -35.17 | -6.32 | -36.69 | 522 |
| 51 | Donchian 20/10 · 1h | breakout | 81.20 | -18.80 | 96 | 19.8 | -24.52 | -4.78 | -27.45 | 217 |
| 52 | OBV trend · 1h | momentum | 81.04 | -18.96 | 201 | 17.4 | -31.65 | -7.01 | -33.12 | 304 |
| 53 | Bollinger reversion · 1h | reversion | 80.55 | -19.45 | 171 | 34.5 | -30.81 | -6.42 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.41 | -19.59 | 198 | 42.9 | -26.22 | -3.95 | -28.17 | 448 |
| 55 | Agent (ML meta-label) | meta | 80.06 | -19.93 | 845 | 18.8 | -15.26 | -2.71 | -16.80 | 376 |
| 56 | Heikin-Ashi · 1h | trend | 79.61 | -20.39 | 264 | 23.5 | -42.52 | -9.95 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 78.23 | -21.77 | 239 | 23.8 | -30.85 | -6.20 | -31.99 | 379 |
| 58 | RSI(14) reversion · 1h | reversion | 78.08 | -21.92 | 91 | 23.1 | -14.87 | -2.74 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.65 | -22.35 | 252 | 29.0 | -34.59 | -6.55 | -36.06 | 539 |
| 60 | EMA 9/21 cross · 1h | trend | 77.22 | -22.78 | 158 | 12.0 | -30.01 | -6.18 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.19 | -23.81 | 504 | 21.6 | -50.01 | -11.66 | -50.26 | 1207 |
| 62 | Max aggression: 1-day momentum | meta | 66.58 | -33.42 | 18 | 27.8 | -43.12 | -3.05 | -50.31 | 42 |
| 63 | ROC + volume | momentum | 57.78 | -42.22 | 702 | 22.8 | -75.29 | -27.65 | -75.32 | 1549 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.90 | -26.38 | -60.90 | 766 |
| 65 | Squeeze breakout | breakout | 53.98 | -46.02 | 545 | 14.1 | -65.99 | -28.80 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 53.53 | -46.47 | 558 | 19.4 | -71.31 | -23.89 | -71.45 | 1250 |
| 67 | RSI(14) reversion | reversion | 53.08 | -46.92 | 817 | 26.2 | -76.49 | -19.73 | -76.81 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.15 | -47.85 | 606 | 20.3 | -78.67 | -23.90 | -78.97 | 1398 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.19 | -98.66 | 4990 |
| 70 | VWAP reversion | reversion | 50.57 | -49.43 | 813 | 25.0 | -74.63 | -17.57 | -74.81 | 1542 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -48.25 | -93.72 | 2491 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.28 | -30.22 | -88.50 | 1870 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.04 | -38.45 | -91.13 | 2296 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -31.55 | -90.29 | 2136 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.58 | -54.36 | -97.62 | 3419 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.93 | -63.07 | -95.94 | 3305 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -35.54 | -93.74 | 2424 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -36.48 | -82.52 | 1665 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.55 | -99.31 | 5624 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -42.19 | -92.20 | 2564 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.27 | -40.60 | -95.27 | 3343 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.96 | -99.74 | 6031 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -46.02 | -91.85 | 2291 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -66.50 | -97.48 | 3492 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.96 | -98.45 | 4675 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.13 | -60.18 | -94.15 | 2719 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.55 | -39.97 | -83.62 | 1766 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.42 | -99.52 | 6108 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.51 | -28.80 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.94 | -38.12 | -90.03 | 2210 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -47.12 | -95.87 | 3715 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.24 | -50.46 | -89.33 | 2076 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.99 | -47.86 | -96.06 | 4083 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -112.17 | -99.90 | 8081 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T15:45 | Three white soldiers | sell | UPRO | 20.34 | -0.05 | exit signal |
| 2026-10-23T15:45 | Three white soldiers | sell | SPY | 20.36 | -0.04 | exit signal |
| 2026-10-23T15:45 | ROC + volume | sell | TQQQ | 14.43 | -0.08 | exit signal |
| 2026-10-23T15:45 | ROC + volume | sell | TECL | 14.48 | -0.01 | exit signal |
| 2026-10-23T15:40 | Agent (ML meta-label) | buy | ETH-USD | 4.72 | — | entry |
| 2026-10-23T15:35 | Agent (ML meta-label) | sell | IWM | 4.72 | -0.00 | selected signal exited |
| 2026-10-23T15:30 | Agent (rotation) | sell | TQQQ | 32.03 | -0.15 | selected signal exited |
| 2026-10-23T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.40 | -0.50 | target is flat |
| 2026-10-23T15:30 | Agent (ML meta-label) | buy | IWM | 4.72 | — | entry |
| 2026-10-23T15:30 | MFI reversion · 1h | buy | TSLA | 20.57 | — | entry signal |
| 2026-10-23T15:30 | MFI reversion · 1h | buy | LABU | 20.57 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | UPRO | 4.70 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | TSLA | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | TQQQ | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | SPY | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | QQQ | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | PLTR | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | NVDA | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | MSFT | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | META | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | GOOGL | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | AMZN | 4.75 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | XRP-USD | 8.58 | -0.14 | rebalance down |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | TECL | 5.99 | 0.07 | rebalance down |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | SOXL | 8.79 | 0.10 | rebalance down |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | COIN | 8.72 | -0.12 | rebalance down |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | BITX | 11.43 | 0.03 | rebalance down |
| 2026-10-23T15:30 | CCI reversion · 1h | sell | AMD | 8.65 | 0.01 | rebalance down |
| 2026-10-23T15:30 | Williams %R · 1h | buy | UPRO | 5.07 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | TQQQ | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | TECL | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | SPY | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | QQQ | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | LABU | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | GOOGL | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | buy | ETHU | 5.09 | — | entry signal |
| 2026-10-23T15:30 | Williams %R · 1h | sell | TSLA | 5.14 | 0.07 | rebalance down |
| 2026-10-23T15:30 | Williams %R · 1h | sell | TNA | 5.23 | 0.05 | rebalance down |
| 2026-10-23T15:30 | Williams %R · 1h | sell | NVDA | 4.97 | -0.02 | rebalance down |
| 2026-10-23T15:30 | Williams %R · 1h | sell | MSTR | 5.16 | 0.06 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 15:45:05.000140+00:00 -> 2026-10-23 15:55:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
