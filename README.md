# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T19:43:05.000183+00:00 · 33405 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 37020 decisions in 2982 calls, $0.4563 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T19:43 | 3 / 6 / 21 | LABU 16%, AAPL 14% |  |
| Breezy | 2026-10-23T19:43 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-23T19:43 | 3 / 25 / 2 | COIN 60% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.64 | 6.64 | 0 | — | 8.10 | 4.29 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.41 | -3.16 | -13.74 | 155 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.69 | 0.69 | 0 | — | 3.29 | 1.55 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 73 | 34.2 | 5.01 | 2.45 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.90 | -2.10 | 0 | — | -0.68 | -0.36 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.13 | -3.87 | 0 | — | 1.08 | 0.36 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.09 | -3.91 | 120 | 30.8 | -2.36 | -1.38 | -6.22 | 195 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.90 | -0.32 | -5.99 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.81 | -5.18 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.59 | -5.41 | 25 | 40.0 | -14.40 | -2.74 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.73 | -6.27 | 95 | 23.2 | -21.58 | -7.09 | -21.85 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.14 | -6.86 | 48 | 16.7 | -16.10 | -3.65 | -17.44 | 98 |
| 23 | Opening range 30m | breakout | 93.02 | -6.97 | 242 | 34.7 | -11.08 | -3.45 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -14.61 | -1.34 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.97 | -4.98 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 91.79 | -8.21 | 10 | 10.0 | -17.48 | -3.40 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.22 | -8.78 | 108 | 18.5 | -11.63 | -2.39 | -14.53 | 255 |
| 30 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 31 | Daily: Bullish score | daily | 89.37 | -10.63 | 9 | 0.0 | -8.21 | -1.07 | -14.40 | 14 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.09 | -7.62 | -11.81 | 206 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.08 | -10.92 | 0 | — | -5.41 | -0.79 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 89.03 | -10.97 | 105 | 27.6 | -12.23 | -2.43 | -16.56 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.23 | -12.77 | 186 | 45.2 | -20.25 | -3.84 | -22.47 | 385 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.70 | -4.82 | -24.32 | 190 |
| 38 | EMA 20/50 cross · 1h | trend | 86.21 | -13.79 | 71 | 11.3 | -22.75 | -4.55 | -25.11 | 138 |
| 39 | Opening range 15m | breakout | 86.20 | -13.80 | 306 | 30.1 | -15.97 | -4.68 | -17.87 | 703 |
| 40 | Supertrend · 1h | trend | 85.95 | -14.05 | 108 | 14.8 | -23.85 | -5.04 | -26.47 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.59 | -14.41 | 101 | 15.8 | -21.50 | -4.62 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 84.72 | -15.28 | 217 | 23.0 | -23.11 | -4.64 | -26.28 | 454 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.72 | -4.95 | -25.68 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.69 | -16.30 | 106 | 34.0 | -15.04 | -2.56 | -21.48 | 197 |
| 46 | Triple EMA stack · 1h | trend | 83.57 | -16.43 | 98 | 15.3 | -26.17 | -5.25 | -28.44 | 211 |
| 47 | MFI reversion · 1h | reversion | 82.19 | -17.81 | 258 | 31.8 | -17.58 | -2.88 | -20.54 | 144 |
| 48 | MACD zero-line · 1h | trend | 81.67 | -18.33 | 103 | 15.5 | -21.64 | -4.55 | -25.14 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 81.36 | -18.64 | 96 | 19.8 | -24.42 | -4.76 | -27.45 | 217 |
| 50 | Three white soldiers | momentum | 81.27 | -18.73 | 275 | 20.0 | -43.55 | -21.16 | -43.66 | 589 |
| 51 | OBV trend · 1h | momentum | 81.16 | -18.84 | 203 | 17.2 | -31.95 | -7.07 | -33.48 | 303 |
| 52 | Williams %R · 1h | reversion | 81.03 | -18.97 | 213 | 44.1 | -35.42 | -6.37 | -36.69 | 522 |
| 53 | Bollinger reversion · 1h | reversion | 80.25 | -19.75 | 171 | 34.5 | -31.08 | -6.51 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.03 | -19.97 | 198 | 42.9 | -26.60 | -4.02 | -28.17 | 451 |
| 55 | Agent (ML meta-label) | meta | 79.57 | -20.43 | 856 | 18.7 | -13.50 | -2.54 | -15.37 | 373 |
| 56 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 271 | 22.9 | -43.24 | -10.17 | -43.93 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.16 | -21.84 | 240 | 23.8 | -31.13 | -6.25 | -32.25 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 77.71 | -22.29 | 91 | 23.1 | -15.35 | -2.85 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.32 | -22.68 | 254 | 28.7 | -34.94 | -6.64 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.19 | -22.82 | 158 | 12.0 | -30.09 | -6.19 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 75.50 | -24.50 | 525 | 21.0 | -50.50 | -11.75 | -50.70 | 1217 |
| 62 | Max aggression: 1-day momentum | meta | 67.39 | -32.61 | 18 | 27.8 | -42.49 | -2.98 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.60 | -42.40 | 706 | 22.7 | -74.64 | -27.21 | -74.74 | 1545 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.55 | -26.14 | -60.55 | 758 |
| 65 | Squeeze breakout | breakout | 53.90 | -46.10 | 547 | 14.3 | -66.04 | -28.84 | -66.19 | 1139 |
| 66 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.55 | -23.69 | -71.69 | 1251 |
| 67 | RSI(14) reversion | reversion | 53.04 | -46.96 | 823 | 26.5 | -76.54 | -19.79 | -76.81 | 1668 |
| 68 | EMA 20/50 cross | trend | 51.92 | -48.08 | 619 | 19.9 | -78.81 | -23.90 | -79.12 | 1408 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.04 | -98.66 | 5010 |
| 70 | VWAP reversion | reversion | 50.57 | -49.43 | 814 | 25.1 | -74.57 | -17.62 | -74.75 | 1549 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -47.50 | -93.82 | 2510 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.36 | -30.42 | -88.50 | 1873 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -38.64 | -91.17 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.35 | -31.57 | -90.40 | 2149 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.93 | -97.66 | 3453 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.98 | -61.95 | -95.99 | 3324 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.70 | -35.46 | -93.74 | 2425 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.65 | -36.41 | -82.71 | 1679 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -55.76 | -99.32 | 5673 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -42.38 | -92.20 | 2571 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3349 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.64 | -99.74 | 6083 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.94 | -46.37 | -91.95 | 2307 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -65.72 | -97.52 | 3517 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -59.90 | -98.47 | 4712 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.15 | -60.14 | -94.17 | 2725 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -67.03 | -99.53 | 6165 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.57 | -28.98 | -87.65 | 2186 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.19 | -39.03 | -90.25 | 2219 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -48.09 | -95.91 | 3747 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -50.75 | -89.36 | 2078 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.03 | -48.57 | -96.07 | 4116 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.89 | -99.90 | 8121 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T19:40 | MFI reversion · 1h | sell | GOOGL | 20.48 | -0.05 | target is flat |
| 2026-10-23T19:40 | EMA 20/50 cross | sell | AMD | 12.93 | -0.06 | exit signal |
| 2026-10-23T19:35 | Agent | sell | BITX | 17.73 | -0.13 | selected signal exited |
| 2026-10-23T19:35 | MFI reversion · 1h | buy | GOOGL | 20.53 | — | entry |
| 2026-10-23T19:30 | Agent (ML meta-label) | buy | IWM | 4.19 | — | entry |
| 2026-10-23T19:30 | Candlestick reversal · 1h | buy | TNA | 1.79 | — | entry |
| 2026-10-23T19:30 | Candlestick reversal · 1h | sell | PLTR | 1.79 | -0.00 | exit signal |
| 2026-10-23T19:30 | OBV trend · 1h | buy | IWM | 20.25 | — | entry signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | buy | TNA | 6.01 | — | rebalance up |
| 2026-10-23T19:30 | VWAP momentum · 1h | buy | SQQQ | 10.78 | — | entry signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | buy | PLTR | 4.47 | — | rebalance up |
| 2026-10-23T19:30 | VWAP momentum · 1h | buy | LABU | 5.37 | — | rebalance up |
| 2026-10-23T19:30 | VWAP momentum · 1h | buy | IWM | 5.37 | — | rebalance up |
| 2026-10-23T19:30 | VWAP momentum · 1h | sell | SOXL | 6.25 | -0.06 | exit signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | sell | MSTR | 8.25 | -0.15 | exit signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | sell | MSFT | 8.44 | -0.03 | exit signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | sell | ETHU | 8.39 | -0.08 | exit signal |
| 2026-10-23T19:30 | VWAP momentum · 1h | sell | AMD | 5.39 | -0.03 | exit signal |
| 2026-10-23T19:30 | Heikin-Ashi · 1h | sell | MSTR | 19.29 | -0.50 | exit signal |
| 2026-10-23T19:30 | Heikin-Ashi · 1h | sell | MSFT | 19.72 | -0.05 | exit signal |
| 2026-10-23T19:30 | RSI(14) reversion | buy | DOGE-USD | 13.29 | — | entry signal |
| 2026-10-23T19:30 | Opening range 15m | buy | SPY | 3.39 | — | entry |
| 2026-10-23T19:30 | Opening range 15m | buy | MSTR | 6.17 | — | entry |
| 2026-10-23T19:30 | Opening range 15m | sell | GOOGL | 9.56 | -0.05 | exit signal |
| 2026-10-23T19:27 | VWAP reversion | buy | XRP-USD | 2.53 | — | rebalance up |
| 2026-10-23T19:27 | VWAP reversion | sell | AAPL | 2.54 | 0.00 | rebalance down |
| 2026-10-23T19:25 | VWAP reversion | buy | XRP-USD | 7.61 | — | entry signal |
| 2026-10-23T19:25 | VWAP reversion | buy | SOL-USD | 10.14 | — | entry signal |
| 2026-10-23T19:25 | VWAP reversion | buy | DOGE-USD | 10.14 | — | entry signal |
| 2026-10-23T19:25 | VWAP reversion | buy | BITX | 10.14 | — | entry signal |
| 2026-10-23T19:25 | RSI(14) reversion | buy | XRP-USD | 13.31 | — | entry signal |
| 2026-10-23T19:25 | RSI(14) reversion | buy | SOL-USD | 13.31 | — | entry signal |
| 2026-10-23T19:21 | Agent (ML meta-label) | buy | SPY | 4.42 | — | entry |
| 2026-10-23T19:21 | RSI(14) reversion | sell | XRP-USD | 13.16 | -0.17 | stop-loss |
| 2026-10-23T19:17 | EMA 20/50 cross | buy | TNA | 2.60 | — | rebalance up |
| 2026-10-23T19:17 | EMA 20/50 cross | buy | SQQQ | 4.31 | — | rebalance up |
| 2026-10-23T19:17 | EMA 20/50 cross | buy | AMD | 2.60 | — | rebalance up |
| 2026-10-23T19:17 | EMA 20/50 cross | sell | MSFT | 10.37 | -0.03 | exit signal |
| 2026-10-23T19:10 | EMA 20/50 cross | buy | TNA | 2.96 | — | rebalance up |
| 2026-10-23T19:10 | EMA 20/50 cross | buy | MSFT | 2.96 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 19:43:05.000183+00:00 -> 2026-10-23 19:53:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
