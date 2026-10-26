# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T14:42:05.000144+00:00 · 36741 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.71 (-10.29%)

Closed trades 102, win rate 38.2%, fees £3.24, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 36.05 | +0.27 |
| PLTR | 18.14 | +0.28 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | PAM 12%, PEP 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 13638 decisions in 2148 calls, $0.1823 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T14:42 | 6 / 18 / 6 | META 15%, TECL 14% |  |
| Breezy | 2026-10-26T14:42 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-26T14:42 | 8 / 20 / 2 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Bollinger reversion | BITX | 2.12 | +2.39% | 13 |
| VWAP momentum | PLTR | 1.73 | +4.99% | 6 |
| Stochastic reversion | BITX | 1.67 | +3.43% | 12 |
| RSI(14) reversion | TSLA | 1.52 | +3.64% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.08 | 7.08 | 0 | — | 8.00 | 4.06 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.84 | 5.84 | 13 | 69.2 | 3.08 | 1.03 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.33 | 5.33 | 20 | 30.0 | 10.15 | 2.67 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.01 | 4.01 | 18 | 44.4 | 5.74 | 1.89 | -4.92 | 27 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.62 | 0.62 | 0 | — | 3.12 | 1.56 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.90 | -1.10 | 0 | — | 0.00 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.41 | -1.59 | 77 | 33.8 | 8.02 | 3.36 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.12 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.65 | -3.35 | 0 | — | -0.36 | -0.09 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.20 | -3.80 | 120 | 30.8 | -0.89 | -0.42 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.60 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.87 | -5.13 | 0 | — | -7.06 | -3.00 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.78 | -5.22 | 0 | — | 0.23 | 0.45 | -9.28 | 1 |
| 19 | Trend pullback · 1h | trend | 93.71 | -6.29 | 95 | 23.2 | -21.42 | -6.91 | -21.85 | 114 |
| 20 | Gap and go | momentum | 93.52 | -6.48 | 100 | 21.0 | 3.74 | 1.26 | -8.76 | 199 |
| 21 | Copy: Insider buying | copy | 93.29 | -6.71 | 27 | 37.0 | -16.46 | -3.15 | -21.73 | 60 |
| 22 | Opening range 30m | breakout | 92.91 | -7.09 | 255 | 34.1 | -10.59 | -3.24 | -17.21 | 569 |
| 23 | Donchian 55/20 · 1h | breakout | 92.41 | -7.59 | 48 | 16.7 | -15.76 | -3.56 | -16.33 | 99 |
| 24 | Daily: Momentum burst | daily | 91.63 | -8.37 | 10 | 10.0 | -19.33 | -3.76 | -20.97 | 40 |
| 25 | Max aggression: 5-day momentum | meta | 91.51 | -8.49 | 11 | 45.5 | -15.29 | -1.40 | -27.80 | 25 |
| 26 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.08 | -0.72 | -11.55 | 91 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.16 | -2.18 | -16.91 | 1 |
| 28 | Daily: Bullish score | daily | 90.69 | -9.31 | 11 | 18.2 | -7.24 | -0.82 | -14.40 | 13 |
| 29 | Parabolic SAR · 1h | trend | 90.23 | -9.77 | 121 | 25.6 | -24.58 | -6.08 | -25.01 | 249 |
| 30 | Agent | meta | 89.71 | -10.29 | 102 | 38.2 | -10.77 | -7.01 | -12.54 | 201 |
| 31 | ADX DI cross · 1h | trend | 89.66 | -10.34 | 112 | 17.9 | -14.25 | -2.94 | -16.62 | 264 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 89.23 | -10.77 | 0 | — | -5.78 | -0.79 | -14.57 | 1 |
| 33 | Volume breakout · 1h | breakout | 89.06 | -10.94 | 103 | 23.3 | -13.27 | -2.80 | -15.73 | 113 |
| 34 | Bollinger breakout · 1h | breakout | 88.08 | -11.92 | 107 | 27.1 | -12.86 | -2.52 | -17.07 | 244 |
| 35 | Stochastic reversion · 1h | reversion | 87.90 | -12.10 | 195 | 46.2 | -20.31 | -3.80 | -22.40 | 393 |
| 36 | Agent (aggressive) | meta | 87.80 | -12.20 | 48 | 35.4 | -10.79 | -3.64 | -14.77 | 90 |
| 37 | Opening range 15m | breakout | 86.51 | -13.49 | 320 | 30.6 | -15.17 | -4.34 | -17.87 | 709 |
| 38 | Keltner breakout · 1h | breakout | 85.72 | -14.28 | 74 | 23.0 | -23.75 | -5.08 | -25.23 | 192 |
| 39 | Connors RSI(2) · 1h | reversion | 85.28 | -14.72 | 173 | 40.5 | -26.30 | -7.96 | -26.96 | 197 |
| 40 | EMA 20/50 cross · 1h | trend | 84.58 | -15.42 | 72 | 11.1 | -23.13 | -4.62 | -23.44 | 137 |
| 41 | Z-score reversion · 1h | reversion | 84.44 | -15.56 | 114 | 33.3 | -14.85 | -2.47 | -21.48 | 206 |
| 42 | RSI momentum · 1h | momentum | 84.25 | -15.76 | 103 | 15.5 | -20.40 | -4.17 | -20.75 | 207 |
| 43 | Supertrend · 1h | trend | 83.79 | -16.21 | 113 | 14.2 | -27.79 | -6.19 | -28.62 | 219 |
| 44 | Ichimoku · 1h | trend | 83.38 | -16.62 | 65 | 12.3 | -23.67 | -4.97 | -23.67 | 107 |
| 45 | MFI reversion · 1h | reversion | 82.89 | -17.11 | 263 | 31.6 | -15.90 | -2.46 | -20.70 | 151 |
| 46 | MACD cross · 1h | trend | 82.88 | -17.12 | 236 | 22.9 | -28.32 | -6.00 | -28.94 | 469 |
| 47 | Triple EMA stack · 1h | trend | 82.36 | -17.64 | 99 | 15.2 | -33.01 | -6.39 | -33.57 | 198 |
| 48 | Bollinger reversion · 1h | reversion | 81.66 | -18.34 | 173 | 35.3 | -29.11 | -5.84 | -31.36 | 375 |
| 49 | Williams %R · 1h | reversion | 81.44 | -18.56 | 226 | 45.6 | -35.33 | -6.19 | -36.29 | 541 |
| 50 | MACD zero-line · 1h | trend | 81.02 | -18.98 | 107 | 15.9 | -23.88 | -5.18 | -25.47 | 217 |
| 51 | CCI reversion · 1h | reversion | 80.73 | -19.27 | 210 | 41.9 | -25.89 | -3.80 | -28.08 | 469 |
| 52 | Donchian 20/10 · 1h | breakout | 80.31 | -19.69 | 99 | 20.2 | -24.81 | -4.78 | -27.76 | 220 |
| 53 | OBV trend · 1h | momentum | 79.62 | -20.38 | 205 | 17.6 | -32.57 | -7.08 | -33.11 | 305 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 291 | 19.2 | -44.20 | -20.43 | -44.20 | 595 |
| 55 | Agent (ML meta-label) | meta | 79.04 | -20.96 | 897 | 19.0 | -20.21 | -3.87 | -21.18 | 363 |
| 56 | RSI(14) reversion · 1h | reversion | 77.74 | -22.26 | 99 | 23.2 | -21.83 | -4.41 | -24.48 | 189 |
| 57 | ROC + volume · 1h | momentum | 77.22 | -22.78 | 243 | 23.9 | -30.60 | -6.08 | -32.25 | 381 |
| 58 | Heikin-Ashi · 1h | trend | 77.07 | -22.93 | 284 | 22.5 | -44.75 | -10.30 | -45.15 | 663 |
| 59 | Candlestick reversal · 1h | reversion | 76.40 | -23.60 | 270 | 28.1 | -35.03 | -6.60 | -35.53 | 563 |
| 60 | EMA 9/21 cross · 1h | trend | 75.80 | -24.20 | 171 | 11.1 | -32.08 | -6.57 | -35.39 | 329 |
| 61 | VWAP momentum · 1h | momentum | 75.32 | -24.68 | 538 | 20.6 | -50.34 | -11.50 | -50.63 | 1243 |
| 62 | Max aggression: 1-day momentum | meta | 67.49 | -32.51 | 19 | 26.3 | -41.82 | -2.86 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.62 | -44.38 | 737 | 21.8 | -74.45 | -26.90 | -74.74 | 1566 |
| 64 | Volume breakout | breakout | 54.31 | -45.69 | 449 | 12.2 | -62.58 | -26.39 | -62.73 | 799 |
| 65 | Squeeze breakout | breakout | 51.33 | -48.67 | 583 | 13.7 | -67.51 | -28.62 | -67.82 | 1182 |
| 66 | Donchian 55/20 | breakout | 51.04 | -48.96 | 593 | 18.5 | -72.06 | -24.04 | -72.35 | 1277 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.56 | -98.92 | 5201 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.29 | -23.65 | -79.42 | 1435 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.05 | -46.85 | -94.09 | 2552 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -31.03 | -89.35 | 1924 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.51 | -38.78 | -91.58 | 2341 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.74 | -31.72 | -90.74 | 2175 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.96 | -55.46 | -97.97 | 3543 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -60.92 | -96.24 | 3383 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -36.69 | -94.20 | 2451 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.85 | -35.57 | -83.06 | 1706 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -56.23 | -99.44 | 5808 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.69 | -42.95 | -92.73 | 2627 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -38.68 | -95.60 | 3377 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.07 | -99.78 | 6197 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.45 | -45.69 | -92.49 | 2351 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -66.37 | -97.72 | 3567 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -61.74 | -98.68 | 4816 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -56.69 | -94.62 | 2779 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.44 | -39.23 | -84.56 | 1809 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.98 | -99.61 | 6299 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.55 | -29.69 | -88.58 | 2259 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.67 | -19.93 | -77.76 | 1721 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.80 | -38.29 | -90.84 | 2281 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.37 | -49.80 | -96.40 | 3839 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.02 | -51.73 | -90.03 | 2116 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.43 | -18.03 | -76.58 | 1592 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -49.79 | -96.57 | 4204 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -107.26 | -99.92 | 8265 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T14:40 | Agent (rotation) | buy | TQQQ | 31.13 | — | rebalance up |
| 2026-10-26T14:40 | Day trade: Open breakout · TQQQ/SQQQ | buy | TQQQ | 105.90 | — | entry |
| 2026-10-26T14:40 | Volume breakout | buy | QQQ | 13.34 | — | entry signal |
| 2026-10-26T14:40 | Opening range 30m | buy | TECL | 7.74 | — | entry signal |
| 2026-10-26T14:40 | Opening range 15m | buy | TECL | 7.21 | — | entry signal |
| 2026-10-26T14:40 | Donchian 55/20 | buy | TQQQ | 4.12 | — | entry |
| 2026-10-26T14:40 | Donchian 55/20 | buy | TECL | 4.64 | — | entry signal |
| 2026-10-26T14:40 | Donchian 55/20 | buy | QQQ | 4.64 | — | entry |
| 2026-10-26T14:40 | Donchian 55/20 | sell | UPRO | 2.71 | 0.02 | rebalance down |
| 2026-10-26T14:40 | Donchian 55/20 | sell | TSLA | 2.65 | 0.02 | rebalance down |
| 2026-10-26T14:40 | Donchian 55/20 | sell | TNA | 2.72 | 0.04 | rebalance down |
| 2026-10-26T14:40 | Donchian 55/20 | sell | SPY | 2.66 | 0.01 | rebalance down |
| 2026-10-26T14:40 | Donchian 55/20 | sell | IWM | 2.66 | 0.01 | rebalance down |
| 2026-10-26T14:40 | Gap and go | buy | SOXL | 4.87 | — | entry signal |
| 2026-10-26T14:40 | Gap and go | sell | TECL | 4.77 | 0.04 | rebalance down |
| 2026-10-26T14:37 | Three white soldiers | sell | IWM | 19.76 | -0.09 | stop-loss |
| 2026-10-26T14:37 | Volume breakout | sell | LABU | 13.34 | -0.25 | stop-loss |
| 2026-10-26T14:37 | Squeeze breakout | sell | IWM | 6.42 | 0.03 | stop-loss |
| 2026-10-26T14:37 | Opening range 30m | sell | LABU | 7.00 | -0.19 | stop-loss |
| 2026-10-26T14:37 | Opening range 30m | sell | BITX | 7.10 | -0.09 | exit signal |
| 2026-10-26T14:37 | Opening range 15m | sell | LABU | 6.52 | -0.10 | stop-loss |
| 2026-10-26T14:37 | Opening range 15m | sell | BITX | 6.61 | -0.08 | exit signal |
| 2026-10-26T14:37 | Gap and go | buy | TSLA | 4.68 | — | rebalance up |
| 2026-10-26T14:37 | ROC + volume | buy | TQQQ | 6.74 | — | rebalance up |
| 2026-10-26T14:37 | ROC + volume | sell | LABU | 9.13 | -0.06 | stop-loss |
| 2026-10-26T14:30 | Agent (rotation) | buy | TQQQ | 32.01 | — | entry |
| 2026-10-26T14:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 103.52 | — | entry |
| 2026-10-26T14:30 | Agent (ML meta-label) | sell | IWM | 4.77 | 0.01 | selected signal exited |
| 2026-10-26T14:30 | MFI reversion · 1h | buy | NVDA | 9.57 | — | entry signal |
| 2026-10-26T14:30 | MFI reversion · 1h | sell | TSLA | 5.05 | 0.26 | rebalance down |
| 2026-10-26T14:30 | MFI reversion · 1h | sell | LABU | 4.53 | 0.13 | rebalance down |
| 2026-10-26T14:30 | CCI reversion · 1h | buy | XRP-USD | 4.48 | — | entry |
| 2026-10-26T14:30 | CCI reversion · 1h | sell | TSLA | 5.00 | 0.25 | exit signal |
| 2026-10-26T14:30 | CCI reversion · 1h | sell | IWM | 3.67 | 0.03 | exit signal |
| 2026-10-26T14:30 | Williams %R · 1h | buy | UPRO | 5.04 | — | rebalance up |
| 2026-10-26T14:30 | Williams %R · 1h | buy | META | 10.19 | — | entry signal |
| 2026-10-26T14:30 | Williams %R · 1h | buy | LABU | 4.89 | — | rebalance up |
| 2026-10-26T14:30 | Williams %R · 1h | buy | GOOGL | 10.19 | — | entry signal |
| 2026-10-26T14:30 | Williams %R · 1h | buy | ETH-USD | 4.39 | — | rebalance up |
| 2026-10-26T14:30 | Williams %R · 1h | buy | COIN | 10.19 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 14:42:05.000144+00:00 -> 2026-10-26 14:52:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
