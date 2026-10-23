# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T16:45:05.000151+00:00 · 33263 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.45 (-10.54%)

Closed trades 100, win rate 39.0%, fees £3.18, max drawdown -10.96%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSTR | 17.88 | -0.01 |

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

Today: 24456 decisions in 2556 calls, $0.3093 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T16:45 | 10 / 17 / 2 | MSTR 16% |  |
| Breezy | 2026-10-23T16:45 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-23T16:45 | 7 / 21 / 1 | MSTR 80% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.88 | 6.88 | 0 | — | 8.37 | 4.47 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.54 | -3.21 | -13.74 | 152 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.60 | 0.60 | 0 | — | 3.22 | 1.52 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.40 | -0.60 | 72 | 33.3 | 5.56 | 2.72 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.16 | -1.84 | 0 | — | -0.38 | -0.18 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.62 | -3.38 | 0 | — | 1.63 | 0.45 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.06 | -3.94 | 120 | 30.8 | -2.39 | -1.40 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.96 | -4.04 | 0 | — | -0.59 | -0.19 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.48 | -5.52 | 0 | — | -6.56 | -2.78 | -7.76 | 1 |
| 19 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 20 | Copy: Insider buying | copy | 93.93 | -6.07 | 25 | 40.0 | -15.03 | -2.88 | -20.68 | 71 |
| 21 | Opening range 30m | breakout | 93.76 | -6.24 | 239 | 35.1 | -10.35 | -3.21 | -17.21 | 561 |
| 22 | Trend pullback · 1h | trend | 93.70 | -6.30 | 95 | 23.2 | -21.59 | -7.10 | -21.85 | 115 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -13.79 | -1.26 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 92.83 | -7.17 | 48 | 16.7 | -16.37 | -3.72 | -17.44 | 98 |
| 25 | Daily: Momentum burst | daily | 92.25 | -7.75 | 10 | 10.0 | -16.94 | -3.28 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.77 | -8.22 | 117 | 25.6 | -21.18 | -5.03 | -24.17 | 254 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.90 | -9.10 | 108 | 18.5 | -11.92 | -2.45 | -14.53 | 255 |
| 30 | Daily: Bullish score | daily | 89.46 | -10.54 | 9 | 0.0 | -8.12 | -1.06 | -14.40 | 14 |
| 31 | Agent | meta | 89.45 | -10.54 | 100 | 39.0 | -10.81 | -7.54 | -11.53 | 205 |
| 32 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 88.92 | -11.08 | 0 | — | -5.55 | -0.82 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.72 | -11.28 | 105 | 27.6 | -12.52 | -2.49 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.98 | -12.02 | 186 | 45.2 | -19.56 | -3.68 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | Opening range 15m | breakout | 86.69 | -13.31 | 305 | 30.2 | -15.30 | -4.44 | -17.87 | 702 |
| 38 | EMA 20/50 cross · 1h | trend | 86.64 | -13.37 | 71 | 11.3 | -22.40 | -4.48 | -25.11 | 138 |
| 39 | Keltner breakout · 1h | breakout | 86.01 | -13.98 | 73 | 23.3 | -22.95 | -4.89 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 85.94 | -14.06 | 108 | 14.8 | -23.84 | -5.04 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.28 | -14.72 | 101 | 15.8 | -21.77 | -4.67 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.19 | -14.81 | 172 | 40.1 | -26.48 | -8.13 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 85.09 | -14.91 | 216 | 23.1 | -22.63 | -4.53 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 84.30 | -15.70 | 106 | 34.0 | -14.40 | -2.42 | -21.48 | 197 |
| 45 | Triple EMA stack · 1h | trend | 83.82 | -16.18 | 98 | 15.3 | -25.93 | -5.20 | -28.44 | 210 |
| 46 | Ichimoku · 1h | trend | 83.63 | -16.37 | 65 | 12.3 | -23.97 | -5.02 | -25.68 | 110 |
| 47 | MFI reversion · 1h | reversion | 82.44 | -17.56 | 257 | 31.9 | -17.19 | -2.80 | -20.54 | 143 |
| 48 | MACD zero-line · 1h | trend | 82.18 | -17.82 | 103 | 15.5 | -21.15 | -4.43 | -24.81 | 217 |
| 49 | Williams %R · 1h | reversion | 81.67 | -18.33 | 213 | 44.1 | -34.90 | -6.26 | -36.69 | 522 |
| 50 | OBV trend · 1h | momentum | 81.54 | -18.46 | 201 | 17.4 | -31.75 | -7.02 | -33.61 | 304 |
| 51 | Three white soldiers | momentum | 81.33 | -18.67 | 274 | 20.1 | -43.50 | -21.10 | -43.62 | 588 |
| 52 | Donchian 20/10 · 1h | breakout | 81.27 | -18.73 | 96 | 19.8 | -24.47 | -4.77 | -27.45 | 217 |
| 53 | Bollinger reversion · 1h | reversion | 80.80 | -19.20 | 171 | 34.5 | -30.62 | -6.36 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.62 | -19.38 | 198 | 42.9 | -26.08 | -3.92 | -28.17 | 450 |
| 55 | Agent (ML meta-label) | meta | 80.36 | -19.64 | 849 | 18.8 | -11.88 | -2.07 | -16.21 | 367 |
| 56 | Heikin-Ashi · 1h | trend | 79.70 | -20.30 | 264 | 23.5 | -42.45 | -9.93 | -43.38 | 652 |
| 57 | RSI(14) reversion · 1h | reversion | 78.36 | -21.64 | 91 | 23.1 | -14.62 | -2.69 | -23.51 | 186 |
| 58 | ROC + volume · 1h | momentum | 78.12 | -21.88 | 239 | 23.8 | -30.99 | -6.23 | -32.05 | 380 |
| 59 | Candlestick reversal · 1h | reversion | 78.11 | -21.89 | 252 | 29.0 | -34.35 | -6.48 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.68 | -22.32 | 158 | 12.0 | -29.66 | -6.10 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.46 | -23.54 | 509 | 21.4 | -49.82 | -11.62 | -50.22 | 1207 |
| 62 | Max aggression: 1-day momentum | meta | 66.49 | -33.51 | 18 | 27.8 | -43.24 | -3.06 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.78 | -42.22 | 703 | 22.8 | -74.86 | -27.51 | -74.89 | 1544 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.55 | -26.14 | -60.55 | 758 |
| 65 | Squeeze breakout | breakout | 53.99 | -46.01 | 546 | 14.3 | -65.98 | -28.80 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 53.71 | -46.29 | 561 | 19.3 | -71.23 | -23.94 | -71.48 | 1251 |
| 67 | RSI(14) reversion | reversion | 53.37 | -46.63 | 821 | 26.4 | -76.40 | -19.62 | -76.81 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.31 | -47.69 | 608 | 20.2 | -78.64 | -23.90 | -78.97 | 1405 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -45.17 | -98.66 | 5000 |
| 70 | VWAP reversion | reversion | 50.55 | -49.45 | 813 | 25.0 | -74.62 | -17.60 | -74.79 | 1541 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -48.22 | -93.73 | 2499 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.26 | -30.16 | -88.50 | 1872 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -38.30 | -91.13 | 2300 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -31.56 | -90.34 | 2142 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.59 | -54.38 | -97.62 | 3429 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.91 | -62.37 | -95.94 | 3313 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.56 | -93.75 | 2425 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.47 | -36.48 | -82.55 | 1666 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.58 | -99.31 | 5635 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.09 | -42.09 | -92.20 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.27 | -40.60 | -95.28 | 3346 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -85.01 | -99.74 | 6052 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.82 | -46.20 | -91.85 | 2298 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -66.44 | -97.49 | 3502 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.93 | -98.45 | 4687 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.12 | -60.18 | -94.15 | 2720 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.54 | -39.99 | -83.62 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.52 | -99.52 | 6126 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.47 | -28.66 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.98 | -37.83 | -90.09 | 2219 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -47.15 | -95.87 | 3723 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -50.66 | -89.36 | 2077 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.98 | -47.63 | -96.06 | 4086 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -112.09 | -99.90 | 8103 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-23T16:20 | Agent (ML meta-label) | buy | IWM | 4.46 | — | entry |
| 2026-10-23T16:20 | Agent (ML meta-label) | buy | ETH-USD | 4.46 | — | entry |
| 2026-10-23T16:20 | EMA 20/50 cross | sell | PLTR | 4.75 | -0.02 | exit signal |
| 2026-10-23T16:16 | Agent (ML meta-label) | sell | IWM | 4.71 | 0.00 | selected signal exited |
| 2026-10-23T16:16 | Agent (ML meta-label) | sell | ETH-USD | 4.44 | -0.03 | selected signal exited |
| 2026-10-23T16:15 | MFI reversion · 1h | sell | LABU | 20.78 | 0.22 | target is flat |
| 2026-10-23T16:15 | Squeeze breakout | sell | TECL | 13.64 | 0.14 | exit signal |
| 2026-10-23T16:10 | Agent (ML meta-label) | buy | ETH-USD | 4.47 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 16:45:05.000151+00:00 -> 2026-10-23 16:55:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
