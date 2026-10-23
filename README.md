# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T19:14:05.000126+00:00 · 33384 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.23 (-10.77%)

Closed trades 101, win rate 38.6%, fees £3.20, max drawdown -11.18%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.79 | -0.07 |

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

Today: 35148 decisions in 2919 calls, $0.4344 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T19:14 | 1 / 14 / 14 | cash |  |
| Breezy | 2026-10-23T19:14 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-23T19:14 | 2 / 23 / 4 | COIN 62% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.35 | 6.35 | 0 | — | 7.79 | 4.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.41 | -3.16 | -13.74 | 155 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.58 | 0.58 | 0 | — | 3.16 | 1.49 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.10 | -0.90 | 73 | 34.2 | 5.19 | 2.54 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.98 | -2.02 | 0 | — | -0.61 | -0.32 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.23 | -3.77 | 0 | — | 1.18 | 0.37 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.05 | -3.95 | 120 | 30.8 | -2.41 | -1.41 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.77 | -4.23 | 0 | — | -0.83 | -0.29 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.83 | -5.17 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.82 | -5.18 | 25 | 40.0 | -14.21 | -2.70 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.70 | -6.30 | 95 | 23.2 | -21.60 | -7.10 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.18 | -6.82 | 242 | 34.7 | -10.95 | -3.41 | -17.21 | 562 |
| 23 | Donchian 55/20 · 1h | breakout | 93.09 | -6.91 | 48 | 16.7 | -16.15 | -3.66 | -17.44 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -15.57 | -1.45 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 91.98 | -8.02 | 118 | 25.4 | -21.02 | -4.99 | -24.17 | 254 |
| 26 | Daily: Momentum burst | daily | 91.60 | -8.40 | 10 | 10.0 | -17.69 | -3.44 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.16 | -8.84 | 108 | 18.5 | -11.69 | -2.40 | -14.53 | 255 |
| 30 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 31 | Daily: Bullish score | daily | 89.32 | -10.68 | 9 | 0.0 | -8.29 | -1.09 | -14.40 | 14 |
| 32 | Agent | meta | 89.23 | -10.77 | 101 | 38.6 | -11.04 | -7.61 | -11.75 | 206 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.09 | -10.91 | 0 | — | -5.41 | -0.79 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.97 | -11.03 | 105 | 27.6 | -12.29 | -2.44 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.42 | -12.58 | 186 | 45.2 | -20.16 | -3.82 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | Opening range 15m | breakout | 86.38 | -13.62 | 305 | 30.2 | -15.82 | -4.63 | -17.87 | 703 |
| 38 | Keltner breakout · 1h | breakout | 86.25 | -13.74 | 73 | 23.3 | -22.75 | -4.84 | -24.32 | 190 |
| 39 | EMA 20/50 cross · 1h | trend | 86.25 | -13.75 | 71 | 11.3 | -22.72 | -4.55 | -25.11 | 138 |
| 40 | Supertrend · 1h | trend | 85.99 | -14.01 | 108 | 14.8 | -23.82 | -5.04 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.51 | -14.48 | 101 | 15.8 | -21.57 | -4.63 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 84.85 | -15.15 | 217 | 23.0 | -23.00 | -4.62 | -26.17 | 454 |
| 44 | Z-score reversion · 1h | reversion | 83.91 | -16.09 | 106 | 34.0 | -14.83 | -2.51 | -21.48 | 197 |
| 45 | Ichimoku · 1h | trend | 83.86 | -16.14 | 65 | 12.3 | -23.77 | -4.96 | -25.68 | 110 |
| 46 | Triple EMA stack · 1h | trend | 83.52 | -16.48 | 98 | 15.3 | -26.23 | -5.26 | -28.44 | 211 |
| 47 | MFI reversion · 1h | reversion | 82.03 | -17.97 | 257 | 31.9 | -17.63 | -2.89 | -20.54 | 144 |
| 48 | MACD zero-line · 1h | trend | 81.84 | -18.16 | 103 | 15.5 | -21.49 | -4.51 | -24.94 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 81.38 | -18.62 | 96 | 19.8 | -24.39 | -4.76 | -27.45 | 217 |
| 50 | Three white soldiers | momentum | 81.27 | -18.73 | 275 | 20.0 | -43.55 | -21.16 | -43.66 | 589 |
| 51 | OBV trend · 1h | momentum | 81.16 | -18.84 | 203 | 17.2 | -31.98 | -7.07 | -33.50 | 303 |
| 52 | Williams %R · 1h | reversion | 81.08 | -18.92 | 213 | 44.1 | -35.39 | -6.36 | -36.69 | 522 |
| 53 | Bollinger reversion · 1h | reversion | 80.34 | -19.66 | 171 | 34.5 | -31.04 | -6.49 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.20 | -19.80 | 198 | 42.9 | -26.53 | -4.00 | -28.17 | 451 |
| 55 | Agent (ML meta-label) | meta | 79.72 | -20.28 | 856 | 18.7 | -11.81 | -2.11 | -16.06 | 362 |
| 56 | Heikin-Ashi · 1h | trend | 78.73 | -21.27 | 269 | 23.0 | -43.17 | -10.16 | -43.85 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.10 | -21.90 | 240 | 23.8 | -31.19 | -6.26 | -32.25 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 77.93 | -22.07 | 91 | 23.1 | -15.11 | -2.80 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.49 | -22.51 | 253 | 28.9 | -34.82 | -6.61 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.27 | -22.73 | 158 | 12.0 | -30.03 | -6.18 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 75.52 | -24.48 | 520 | 21.2 | -50.49 | -11.75 | -50.64 | 1216 |
| 62 | Max aggression: 1-day momentum | meta | 67.23 | -32.77 | 18 | 27.8 | -42.64 | -3.00 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.60 | -42.40 | 706 | 22.7 | -75.15 | -27.76 | -75.16 | 1548 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.80 | -26.34 | -60.80 | 764 |
| 65 | Squeeze breakout | breakout | 53.90 | -46.10 | 547 | 14.3 | -66.04 | -28.84 | -66.19 | 1139 |
| 66 | RSI(14) reversion | reversion | 53.33 | -46.67 | 822 | 26.5 | -76.42 | -19.64 | -76.81 | 1665 |
| 67 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.55 | -23.69 | -71.69 | 1251 |
| 68 | EMA 20/50 cross | trend | 51.91 | -48.09 | 617 | 19.9 | -78.83 | -23.90 | -79.11 | 1408 |
| 69 | VWAP reversion | reversion | 50.70 | -49.30 | 814 | 25.1 | -74.51 | -17.56 | -74.75 | 1545 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -45.07 | -98.67 | 5010 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.78 | -47.41 | -93.82 | 2510 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.35 | -30.39 | -88.50 | 1873 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -38.66 | -91.17 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.37 | -31.56 | -90.40 | 2149 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.93 | -97.66 | 3451 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.98 | -61.81 | -95.99 | 3325 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.55 | -93.75 | 2427 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.66 | -36.39 | -82.71 | 1679 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -55.49 | -99.32 | 5668 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.15 | -42.38 | -92.21 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3349 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.64 | -99.74 | 6081 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -46.37 | -91.94 | 2305 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -65.75 | -97.51 | 3513 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -59.73 | -98.46 | 4710 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.15 | -60.13 | -94.17 | 2723 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -66.68 | -99.53 | 6159 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.48 | -28.69 | -87.65 | 2179 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.04 | -38.58 | -90.10 | 2217 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -47.83 | -95.89 | 3740 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -50.67 | -89.36 | 2077 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.02 | -48.32 | -96.06 | 4110 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.83 | -99.90 | 8116 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T19:10 | EMA 20/50 cross | buy | TNA | 2.96 | — | rebalance up |
| 2026-10-23T19:10 | EMA 20/50 cross | buy | MSFT | 2.96 | — | rebalance up |
| 2026-10-23T19:10 | EMA 20/50 cross | buy | IWM | 2.96 | — | rebalance up |
| 2026-10-23T19:10 | EMA 20/50 cross | buy | AMD | 2.97 | — | rebalance up |
| 2026-10-23T19:10 | EMA 20/50 cross | sell | TECL | 7.39 | -0.08 | stop-loss |
| 2026-10-23T19:05 | Agent (ML meta-label) | buy | ETH-USD | 4.69 | — | entry |
| 2026-10-23T19:05 | RSI(14) reversion | sell | AAPL | 13.35 | 0.01 | exit signal |
| 2026-10-23T19:00 | Agent (ML meta-label) | sell | IWM | 4.44 | -0.01 | selected signal exited |
| 2026-10-23T19:00 | Agent (ML meta-label) | sell | ETH-USD | 4.41 | -0.03 | selected signal exited |
| 2026-10-23T19:00 | ROC + volume · 1h | sell | DOGE-USD | 19.28 | -0.26 | exit signal |
| 2026-10-23T19:00 | VWAP momentum · 1h | buy | TNA | 4.76 | — | entry |
| 2026-10-23T19:00 | VWAP momentum · 1h | buy | SOXL | 6.31 | — | entry |
| 2026-10-23T19:00 | VWAP momentum · 1h | buy | PLTR | 6.31 | — | entry |
| 2026-10-23T19:00 | VWAP momentum · 1h | sell | SOL-USD | 8.38 | -0.08 | exit signal |
| 2026-10-23T19:00 | VWAP momentum · 1h | sell | ETH-USD | 8.41 | -0.06 | exit signal |
| 2026-10-23T19:00 | EMA 20/50 cross | buy | SQQQ | 2.88 | — | rebalance up |
| 2026-10-23T19:00 | EMA 20/50 cross | sell | ETH-USD | 7.39 | -0.06 | exit signal |
| 2026-10-23T18:45 | OBV trend · 1h | sell | IWM | 20.25 | -0.04 | target is flat |
| 2026-10-23T18:40 | Three white soldiers | sell | TECL | 20.27 | -0.07 | exit signal |
| 2026-10-23T18:40 | Opening range 30m | buy | UPRO | 2.83 | — | entry |
| 2026-10-23T18:40 | Opening range 30m | buy | TNA | 4.80 | — | rebalance up |
| 2026-10-23T18:40 | Opening range 30m | sell | MSTR | 7.63 | -0.15 | stop-loss |
| 2026-10-23T18:35 | Agent | buy | BITX | 17.86 | — | following Stochastic reversion |
| 2026-10-23T18:30 | Agent (ML meta-label) | buy | IWM | 4.45 | — | entry |
| 2026-10-23T18:30 | Agent (ML meta-label) | buy | ETH-USD | 4.45 | — | entry |
| 2026-10-23T18:30 | Agent (ML meta-label) | sell | SPY | 1.32 | -0.00 | selected signal exited |
| 2026-10-23T18:30 | MFI reversion · 1h | buy | META | 20.52 | — | entry signal |
| 2026-10-23T18:30 | OBV trend · 1h | buy | IWM | 20.28 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | LABU | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | IWM | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | buy | AMD | 5.42 | — | entry signal |
| 2026-10-23T18:30 | VWAP momentum · 1h | sell | BITX | 8.43 | -0.03 | exit signal |
| 2026-10-23T18:30 | Heikin-Ashi · 1h | sell | TECL | 19.87 | -0.01 | exit signal |
| 2026-10-23T18:30 | MACD cross · 1h | buy | MSFT | 5.38 | — | entry signal |
| 2026-10-23T18:30 | MACD cross · 1h | buy | AMD | 9.44 | — | entry signal |
| 2026-10-23T18:30 | MACD cross · 1h | sell | SOL-USD | 4.68 | -0.02 | rebalance down |
| 2026-10-23T18:25 | Donchian 55/20 | sell | MSTR | 13.25 | -0.12 | exit signal |
| 2026-10-23T18:16 | Agent (ML meta-label) | sell | IWM | 4.71 | -0.01 | selected signal exited |
| 2026-10-23T18:16 | Agent (ML meta-label) | sell | ETH-USD | 4.35 | -0.02 | selected signal exited |
| 2026-10-23T18:15 | Three white soldiers | buy | TECL | 20.33 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 19:14:05.000126+00:00 -> 2026-10-23 19:24:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
