# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T13:46:05.000139+00:00 · 33122 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.10 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.15, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSTR | 18.01 | -0.01 |

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

Today: 11811 decisions in 2133 calls, $0.1617 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T13:46 | 8 / 13 / 9 | AMD 15%, SOXL 15% |  |
| Breezy | 2026-10-23T13:46 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-23T13:46 | 7 / 19 / 4 | MSTR 79% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.23 | 7.23 | 0 | — | 8.80 | 4.73 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.18 | 1.18 | 0 | — | 3.89 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.54 | 0.55 | 83 | 43.4 | -11.81 | -3.32 | -13.74 | 153 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.82 | -1.18 | 69 | 34.8 | 5.31 | 2.60 | -2.20 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.85 | -2.15 | 0 | — | -0.63 | -0.33 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.82 | -3.18 | 0 | — | 1.91 | 0.49 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.67 | -3.33 | 118 | 31.4 | -1.75 | -1.01 | -6.22 | 193 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 95.53 | -4.47 | 0 | — | -5.46 | -2.33 | -7.04 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 95.30 | -4.70 | 0 | — | -1.21 | -0.46 | -5.87 | 1 |
| 19 | Gap and go | momentum | 94.47 | -5.53 | 90 | 22.2 | 5.30 | 1.77 | -8.69 | 183 |
| 20 | Copy: Insider buying | copy | 94.06 | -5.94 | 25 | 40.0 | -14.85 | -2.84 | -20.68 | 71 |
| 21 | Trend pullback · 1h | trend | 93.84 | -6.16 | 95 | 23.2 | -21.46 | -7.04 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -10.42 | -3.24 | -17.21 | 545 |
| 23 | Max aggression: 5-day momentum | meta | 93.68 | -6.32 | 10 | 50.0 | -16.29 | -1.52 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 93.13 | -6.87 | 48 | 16.7 | -16.09 | -3.65 | -17.30 | 98 |
| 25 | Parabolic SAR · 1h | trend | 92.46 | -7.54 | 115 | 26.1 | -20.54 | -4.88 | -24.17 | 254 |
| 26 | ADX DI cross · 1h | trend | 91.37 | -8.63 | 107 | 18.7 | -11.45 | -2.36 | -13.98 | 255 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | Daily: Momentum burst | daily | 91.15 | -8.85 | 10 | 10.0 | -18.14 | -3.53 | -20.49 | 40 |
| 30 | Agent | meta | 90.10 | -9.89 | 98 | 39.8 | -10.00 | -7.05 | -11.03 | 203 |
| 31 | Bollinger breakout · 1h | breakout | 89.42 | -10.57 | 104 | 27.9 | -11.80 | -2.33 | -16.00 | 241 |
| 32 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 33 | Daily: Bullish score | daily | 88.72 | -11.29 | 9 | 0.0 | -8.71 | -1.15 | -14.37 | 14 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.07 | -11.93 | 0 | — | -6.39 | -0.97 | -14.52 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -11.87 | -4.10 | -14.77 | 94 |
| 36 | Stochastic reversion · 1h | reversion | 87.64 | -12.36 | 185 | 45.4 | -19.91 | -3.76 | -22.47 | 382 |
| 37 | EMA 20/50 cross · 1h | trend | 86.84 | -13.16 | 70 | 11.4 | -22.15 | -4.43 | -24.42 | 137 |
| 38 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.69 | -4.58 | -17.87 | 683 |
| 39 | Keltner breakout · 1h | breakout | 86.30 | -13.70 | 73 | 23.3 | -22.69 | -4.82 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.27 | -13.73 | 105 | 15.2 | -23.45 | -4.96 | -26.06 | 212 |
| 41 | RSI momentum · 1h | momentum | 86.12 | -13.88 | 98 | 16.3 | -20.90 | -4.49 | -22.50 | 216 |
| 42 | MACD cross · 1h | trend | 85.47 | -14.54 | 216 | 23.1 | -22.24 | -4.42 | -26.08 | 451 |
| 43 | Connors RSI(2) · 1h | reversion | 84.66 | -15.34 | 170 | 39.4 | -26.95 | -8.32 | -27.04 | 193 |
| 44 | Triple EMA stack · 1h | trend | 84.13 | -15.88 | 97 | 15.5 | -25.56 | -5.12 | -27.76 | 210 |
| 45 | Ichimoku · 1h | trend | 83.90 | -16.10 | 65 | 12.3 | -23.71 | -4.95 | -25.41 | 110 |
| 46 | Z-score reversion · 1h | reversion | 83.82 | -16.18 | 105 | 33.3 | -14.76 | -2.50 | -21.48 | 192 |
| 47 | MACD zero-line · 1h | trend | 82.33 | -17.67 | 103 | 15.5 | -20.95 | -4.38 | -24.69 | 217 |
| 48 | MFI reversion · 1h | reversion | 82.16 | -17.84 | 255 | 31.4 | -17.59 | -2.89 | -20.54 | 142 |
| 49 | Donchian 20/10 · 1h | breakout | 82.14 | -17.86 | 94 | 20.2 | -23.61 | -4.60 | -26.52 | 216 |
| 50 | OBV trend · 1h | momentum | 81.79 | -18.21 | 199 | 17.6 | -31.19 | -6.89 | -32.68 | 303 |
| 51 | Williams %R · 1h | reversion | 81.71 | -18.29 | 212 | 44.3 | -34.77 | -6.23 | -36.69 | 510 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -43.35 | -20.91 | -43.46 | 584 |
| 53 | CCI reversion · 1h | reversion | 81.23 | -18.77 | 195 | 43.1 | -25.48 | -3.80 | -28.17 | 434 |
| 54 | Agent (ML meta-label) | meta | 80.18 | -19.82 | 839 | 18.8 | -15.22 | -3.06 | -16.67 | 381 |
| 55 | Bollinger reversion · 1h | reversion | 80.11 | -19.89 | 171 | 34.5 | -31.27 | -6.56 | -32.19 | 356 |
| 56 | Heikin-Ashi · 1h | trend | 79.98 | -20.02 | 262 | 23.3 | -42.26 | -9.85 | -43.38 | 646 |
| 57 | ROC + volume · 1h | momentum | 79.57 | -20.43 | 235 | 23.8 | -29.73 | -5.93 | -31.24 | 377 |
| 58 | RSI(14) reversion · 1h | reversion | 78.09 | -21.91 | 90 | 23.3 | -14.82 | -2.73 | -23.51 | 184 |
| 59 | Candlestick reversal · 1h | reversion | 77.67 | -22.33 | 251 | 29.1 | -34.54 | -6.53 | -36.06 | 533 |
| 60 | EMA 9/21 cross · 1h | trend | 77.57 | -22.43 | 157 | 11.5 | -29.72 | -6.11 | -32.99 | 316 |
| 61 | VWAP momentum · 1h | momentum | 76.68 | -23.32 | 499 | 21.4 | -49.49 | -11.54 | -49.71 | 1193 |
| 62 | Max aggression: 1-day momentum | meta | 67.35 | -32.65 | 18 | 27.8 | -42.47 | -2.98 | -49.42 | 42 |
| 63 | ROC + volume | momentum | 58.28 | -41.72 | 697 | 23.0 | -74.76 | -27.32 | -74.76 | 1539 |
| 64 | Volume breakout | breakout | 57.33 | -42.67 | 415 | 13.3 | -60.38 | -26.14 | -60.38 | 757 |
| 65 | Donchian 55/20 | breakout | 54.74 | -45.26 | 552 | 19.6 | -70.67 | -23.96 | -70.81 | 1244 |
| 66 | Squeeze breakout | breakout | 54.23 | -45.77 | 541 | 14.2 | -65.85 | -28.66 | -65.91 | 1135 |
| 67 | EMA 20/50 cross | trend | 53.52 | -46.48 | 598 | 20.6 | -78.02 | -23.41 | -78.40 | 1386 |
| 68 | RSI(14) reversion | reversion | 52.97 | -47.03 | 810 | 25.9 | -76.52 | -19.76 | -76.67 | 1655 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -74.46 | -17.56 | -74.66 | 1540 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -45.01 | -98.64 | 4951 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -48.05 | -93.51 | 2476 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.26 | -30.16 | -88.42 | 1856 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.98 | -38.16 | -91.08 | 2284 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.09 | -31.29 | -90.14 | 2129 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.58 | -54.16 | -97.61 | 3394 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.82 | -61.75 | -95.85 | 3285 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.65 | -35.29 | -93.68 | 2416 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.33 | -36.35 | -82.37 | 1660 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.15 | -99.31 | 5609 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -41.80 | -92.10 | 2554 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.21 | -40.55 | -95.22 | 3333 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -84.71 | -99.74 | 6009 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -45.87 | -91.77 | 2273 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -66.47 | -97.43 | 3484 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.42 | -58.45 | -98.45 | 4651 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.04 | -59.81 | -94.07 | 2713 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.34 | -40.19 | -83.41 | 1762 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.06 | -99.52 | 6089 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.56 | -28.94 | -87.58 | 2156 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.93 | -38.46 | -90.00 | 2221 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.83 | -46.97 | -95.84 | 3703 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -49.52 | -89.25 | 2058 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.99 | -47.72 | -96.02 | 4072 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.44 | -99.90 | 8039 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T13:45 | Day trade: Stocks in Play ORB | buy | UPRO | 24.71 | — | entry |
| 2026-10-23T13:45 | Day trade: Stocks in Play ORB | buy | SPY | 24.71 | — | entry |
| 2026-10-23T13:45 | Day trade: Stocks in Play ORB | buy | SOXL | 24.71 | — | entry |
| 2026-10-23T13:45 | Agent | buy | MSTR | 18.02 | — | following Keltner breakout |
| 2026-10-23T13:45 | RSI(14) reversion | buy | TNA | 13.25 | — | entry signal |
| 2026-10-23T13:45 | RSI(14) reversion | buy | PLTR | 13.25 | — | entry signal |
| 2026-10-23T13:45 | RSI(14) reversion | buy | IWM | 13.25 | — | entry signal |
| 2026-10-23T13:45 | Volume breakout | buy | ETH-USD | 14.35 | — | entry signal |
| 2026-10-23T13:45 | Volume breakout | buy | BTC-USD | 14.35 | — | entry signal |
| 2026-10-23T13:45 | Squeeze breakout | buy | ETH-USD | 13.58 | — | entry signal |
| 2026-10-23T13:45 | Squeeze breakout | buy | BTC-USD | 13.58 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | buy | SOL-USD | 9.12 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | buy | MSTR | 9.14 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | buy | ETHU | 9.14 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | buy | ETH-USD | 9.14 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | buy | BITX | 9.14 | — | entry signal |
| 2026-10-23T13:45 | Donchian 55/20 | sell | BTC-USD | 4.54 | -0.02 | rebalance down |
| 2026-10-23T13:45 | Gap and go | buy | ETHU | 23.62 | — | entry signal |
| 2026-10-23T13:45 | ROC + volume | buy | BITX | 14.57 | — | entry signal |
| 2026-10-23T13:40 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 103.59 | -0.13 | target is flat |
| 2026-10-23T13:40 | Agent (ML meta-label) | sell | MSFT | 4.18 | -0.02 | selected signal exited |
| 2026-10-23T13:40 | Williams %R · 1h | buy | TNA | 8.24 | — | rebalance up |
| 2026-10-23T13:40 | Williams %R · 1h | buy | MSTR | 6.11 | — | rebalance up |
| 2026-10-23T13:40 | Williams %R · 1h | buy | LABU | 6.21 | — | rebalance up |
| 2026-10-23T13:40 | Williams %R · 1h | buy | IWM | 8.14 | — | rebalance up |
| 2026-10-23T13:40 | Williams %R · 1h | buy | COIN | 6.12 | — | rebalance up |
| 2026-10-23T13:40 | Williams %R · 1h | sell | UPRO | 8.10 | -0.18 | stop-loss |
| 2026-10-23T13:40 | Williams %R · 1h | sell | SPY | 8.15 | -0.07 | stop-loss |
| 2026-10-23T13:40 | Williams %R · 1h | sell | MSFT | 8.10 | -0.15 | stop-loss |
| 2026-10-23T13:40 | Stochastic reversion · 1h | buy | UPRO | 6.70 | — | entry |
| 2026-10-23T13:40 | Stochastic reversion · 1h | sell | AMZN | 7.22 | -0.17 | stop-loss |
| 2026-10-23T13:40 | Z-score reversion · 1h | sell | MSFT | 11.79 | -0.23 | stop-loss |
| 2026-10-23T13:40 | Bollinger reversion · 1h | sell | UPRO | 7.10 | -0.18 | stop-loss |
| 2026-10-23T13:40 | Connors RSI(2) · 1h | sell | MSFT | 21.12 | -0.32 | stop-loss |
| 2026-10-23T13:40 | Volume breakout · 1h | sell | SQQQ | 22.84 | 0.65 | target is flat |
| 2026-10-23T13:40 | Donchian 20/10 · 1h | sell | PLTR | 20.24 | -0.78 | stop-loss |
| 2026-10-23T13:40 | OBV trend · 1h | sell | IWM | 20.39 | -0.12 | stop-loss |
| 2026-10-23T13:40 | ADX DI cross · 1h | sell | TNA | 22.53 | -0.69 | stop-loss |
| 2026-10-23T13:40 | ADX DI cross · 1h | sell | IWM | 23.09 | -0.25 | stop-loss |
| 2026-10-23T13:40 | Triple EMA stack · 1h | buy | TSLA | 4.47 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 13:46:05.000139+00:00 -> 2026-10-23 13:56:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
