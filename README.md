# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T17:15:05.000148+00:00 · 33286 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.51%)

Closed trades 100, win rate 39.0%, fees £3.18, max drawdown -11.04%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSTR | 17.92 | +0.03 |

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

Today: 26481 decisions in 2625 calls, $0.3330 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T17:15 | 5 / 15 / 9 | cash |  |
| Breezy | 2026-10-23T17:15 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-10-23T17:15 | 6 / 21 / 2 | MSTR 84% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.54 | 6.54 | 0 | — | 8.03 | 4.25 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.54 | -3.21 | -13.74 | 152 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.40 | 0.40 | 0 | — | 3.02 | 1.43 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 72 | 33.3 | 5.23 | 2.56 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.92 | -2.08 | 0 | — | -0.63 | -0.33 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.67 | -3.33 | 0 | — | 1.68 | 0.46 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 95.99 | -4.01 | 120 | 30.8 | -2.45 | -1.43 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.89 | -4.11 | 0 | — | -0.67 | -0.22 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.79 | -5.21 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 93.99 | -6.01 | 25 | 40.0 | -14.98 | -2.87 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.66 | -6.34 | 95 | 23.2 | -21.63 | -7.11 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.35 | -6.65 | 239 | 35.1 | -10.73 | -3.34 | -17.21 | 562 |
| 23 | Donchian 55/20 · 1h | breakout | 93.01 | -6.99 | 48 | 16.7 | -16.21 | -3.68 | -17.44 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -14.37 | -1.32 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 92.21 | -7.79 | 10 | 10.0 | -17.02 | -3.30 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.91 | -8.09 | 117 | 25.6 | -21.06 | -5.00 | -24.17 | 254 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.09 | -8.91 | 108 | 18.5 | -11.75 | -2.42 | -14.53 | 255 |
| 30 | Agent | meta | 89.49 | -10.51 | 100 | 39.0 | -10.78 | -7.52 | -11.62 | 205 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 32 | Daily: Bullish score | daily | 89.33 | -10.67 | 9 | 0.0 | -8.27 | -1.08 | -14.40 | 14 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.22 | -10.78 | 0 | — | -5.24 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.90 | -11.10 | 105 | 27.6 | -12.35 | -2.45 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.60 | -12.40 | 186 | 45.2 | -19.90 | -3.76 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | EMA 20/50 cross · 1h | trend | 86.82 | -13.18 | 71 | 11.3 | -22.21 | -4.44 | -25.11 | 138 |
| 38 | Opening range 15m | breakout | 86.39 | -13.61 | 305 | 30.2 | -15.64 | -4.57 | -17.87 | 703 |
| 39 | Keltner breakout · 1h | breakout | 86.18 | -13.81 | 73 | 23.3 | -22.80 | -4.85 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.04 | -13.96 | 108 | 14.8 | -23.74 | -5.02 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.41 | -14.59 | 101 | 15.8 | -21.66 | -4.65 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.36 | -14.64 | 172 | 40.1 | -26.33 | -8.06 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 85.15 | -14.85 | 216 | 23.1 | -22.58 | -4.51 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 83.93 | -16.07 | 106 | 34.0 | -14.77 | -2.50 | -21.48 | 197 |
| 45 | Triple EMA stack · 1h | trend | 83.79 | -16.21 | 98 | 15.3 | -25.95 | -5.20 | -28.44 | 210 |
| 46 | Ichimoku · 1h | trend | 83.79 | -16.21 | 65 | 12.3 | -23.82 | -4.98 | -25.68 | 110 |
| 47 | MFI reversion · 1h | reversion | 82.24 | -17.76 | 257 | 31.9 | -17.40 | -2.85 | -20.54 | 143 |
| 48 | MACD zero-line · 1h | trend | 82.08 | -17.92 | 103 | 15.5 | -21.25 | -4.45 | -24.81 | 218 |
| 49 | OBV trend · 1h | momentum | 81.65 | -18.35 | 201 | 17.4 | -31.50 | -6.96 | -33.46 | 303 |
| 50 | Donchian 20/10 · 1h | breakout | 81.42 | -18.58 | 96 | 19.8 | -24.34 | -4.75 | -27.45 | 217 |
| 51 | Williams %R · 1h | reversion | 81.39 | -18.61 | 213 | 44.1 | -35.13 | -6.31 | -36.69 | 522 |
| 52 | Three white soldiers | momentum | 81.33 | -18.67 | 274 | 20.1 | -43.50 | -21.10 | -43.62 | 588 |
| 53 | Bollinger reversion · 1h | reversion | 80.42 | -19.58 | 171 | 34.5 | -30.96 | -6.47 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.34 | -19.66 | 198 | 42.9 | -26.35 | -3.97 | -28.17 | 450 |
| 55 | Agent (ML meta-label) | meta | 80.11 | -19.89 | 849 | 18.8 | -12.18 | -2.13 | -16.24 | 367 |
| 56 | Heikin-Ashi · 1h | trend | 79.22 | -20.78 | 264 | 23.5 | -42.80 | -10.05 | -43.49 | 652 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 239 | 23.8 | -30.90 | -6.21 | -32.05 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 78.08 | -21.92 | 91 | 23.1 | -14.93 | -2.76 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.89 | -22.11 | 252 | 29.0 | -34.53 | -6.53 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.64 | -22.36 | 158 | 12.0 | -29.68 | -6.10 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.26 | -23.74 | 509 | 21.4 | -50.00 | -11.66 | -50.22 | 1207 |
| 62 | Max aggression: 1-day momentum | meta | 67.01 | -32.99 | 18 | 27.8 | -42.80 | -3.01 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.80 | -42.20 | 704 | 22.7 | -74.96 | -27.61 | -75.02 | 1547 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.64 | -26.23 | -60.64 | 759 |
| 65 | Squeeze breakout | breakout | 53.99 | -46.01 | 546 | 14.3 | -65.98 | -28.80 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 53.41 | -46.59 | 563 | 19.2 | -71.39 | -23.84 | -71.55 | 1251 |
| 67 | RSI(14) reversion | reversion | 53.36 | -46.64 | 821 | 26.4 | -76.40 | -19.62 | -76.81 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.06 | -47.95 | 609 | 20.2 | -78.73 | -23.91 | -79.02 | 1406 |
| 69 | VWAP reversion | reversion | 50.65 | -49.35 | 813 | 25.0 | -74.53 | -17.59 | -74.75 | 1542 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.14 | -98.66 | 5000 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -48.04 | -93.75 | 2501 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.31 | -30.29 | -88.50 | 1872 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.04 | -38.44 | -91.13 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -31.56 | -90.34 | 2143 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.60 | -54.56 | -97.62 | 3433 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.93 | -62.50 | -95.95 | 3315 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.55 | -93.75 | 2426 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.53 | -36.49 | -82.59 | 1673 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.85 | -99.31 | 5641 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -42.20 | -92.20 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.28 | 3348 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -85.01 | -99.74 | 6053 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -46.26 | -91.86 | 2300 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -66.40 | -97.49 | 3505 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -59.27 | -98.46 | 4687 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.12 | -60.18 | -94.15 | 2721 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.54 | -40.01 | -83.63 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.94 | -99.53 | 6127 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.45 | -28.59 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.97 | -38.20 | -90.05 | 2214 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.85 | -47.39 | -95.87 | 3728 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -50.71 | -89.36 | 2077 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.00 | -47.95 | -96.06 | 4097 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.99 | -99.90 | 8106 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T17:10 | Donchian 55/20 | sell | TECL | 13.35 | -0.05 | exit signal |
| 2026-10-23T17:05 | EMA 20/50 cross | buy | BTC-USD | 4.74 | — | entry signal |
| 2026-10-23T17:05 | EMA 20/50 cross | sell | DOGE-USD | 5.19 | -0.04 | exit signal |
| 2026-10-23T17:00 | MACD zero-line · 1h | buy | SOL-USD | 20.53 | — | entry signal |
| 2026-10-23T17:00 | ROC + volume | sell | LABU | 14.38 | -0.05 | exit signal |
| 2026-10-23T16:55 | Donchian 55/20 | sell | AMD | 13.30 | -0.14 | exit signal |
| 2026-10-23T16:55 | ROC + volume | buy | SQQQ | 14.43 | — | entry signal |
| 2026-10-23T16:55 | ROC + volume | buy | LABU | 14.43 | — | entry |
| 2026-10-23T16:45 | Agent | buy | MSTR | 17.89 | — | following Keltner breakout |
| 2026-10-23T16:45 | RSI(14) reversion | sell | COIN | 13.40 | 0.12 | exit signal |
| 2026-10-23T16:45 | EMA 20/50 cross | buy | BITX | 4.28 | — | entry signal |
| 2026-10-23T16:40 | RSI(14) reversion | sell | BTC-USD | 13.29 | -0.03 | exit signal |
| 2026-10-23T16:40 | ROC + volume | buy | MSTR | 14.43 | — | entry signal |
| 2026-10-23T16:40 | EMA 20/50 cross | buy | DOGE-USD | 5.23 | — | entry signal |
| 2026-10-23T16:36 | Donchian 55/20 | buy | MSTR | 13.37 | — | entry signal |
| 2026-10-23T16:30 | Agent (rotation) | sell | TQQQ | 31.86 | -0.27 | selected signal exited |
| 2026-10-23T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.52 | -0.88 | target is flat |
| 2026-10-23T16:30 | Agent (ML meta-label) | sell | ETH-USD | 4.42 | -0.04 | selected signal exited |
| 2026-10-23T16:30 | MFI reversion · 1h | buy | LABU | 20.54 | — | entry signal |
| 2026-10-23T16:30 | VWAP momentum · 1h | sell | SPY | 4.49 | -0.01 | exit signal |
| 2026-10-23T16:30 | VWAP momentum · 1h | sell | QQQ | 4.49 | -0.01 | exit signal |
| 2026-10-23T16:30 | VWAP momentum · 1h | sell | ETHU | 4.48 | -0.01 | exit signal |
| 2026-10-23T16:30 | VWAP momentum · 1h | sell | BITX | 4.49 | -0.01 | exit signal |
| 2026-10-23T16:30 | VWAP momentum · 1h | sell | AAPL | 4.48 | -0.02 | exit signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | TQQQ | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | TECL | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | SOXL | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | QQQ | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | MSFT | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Heikin-Ashi · 1h | buy | AMD | 13.27 | — | entry signal |
| 2026-10-23T16:30 | Opening range 30m | buy | SPY | 2.11 | — | entry |
| 2026-10-23T16:30 | Opening range 30m | buy | IWM | 7.20 | — | entry |
| 2026-10-23T16:30 | Opening range 30m | sell | NVDA | 9.31 | -0.08 | stop-loss |
| 2026-10-23T16:30 | EMA 20/50 cross | sell | SPY | 4.76 | -0.01 | exit signal |
| 2026-10-23T16:25 | Donchian 55/20 | buy | TECL | 4.44 | — | rebalance up |
| 2026-10-23T16:25 | Donchian 55/20 | buy | SOXL | 4.52 | — | rebalance up |
| 2026-10-23T16:25 | Donchian 55/20 | buy | AMD | 4.46 | — | rebalance up |
| 2026-10-23T16:25 | Donchian 55/20 | sell | TQQQ | 8.91 | -0.07 | exit signal |
| 2026-10-23T16:25 | Donchian 55/20 | sell | QQQ | 8.96 | -0.03 | exit signal |
| 2026-10-23T16:25 | Donchian 55/20 | sell | NVDA | 8.93 | -0.08 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 17:15:05.000148+00:00 -> 2026-10-23 17:25:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
