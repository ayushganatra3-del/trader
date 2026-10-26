# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T14:11:05.000157+00:00 · 36720 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.29 (-10.71%)

Closed trades 102, win rate 38.2%, fees £3.24, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 35.92 | +0.13 |
| PLTR | 17.85 | -0.01 |

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

Today: 11751 decisions in 2085 calls, $0.1605 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T14:11 | 8 / 16 / 6 | cash |  |
| Breezy | 2026-10-26T14:11 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-26T14:11 | 7 / 22 / 1 | COIN 74% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.15 | 7.15 | 0 | — | 8.22 | 4.18 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.14 | 1.05 | -6.79 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.01 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.38 | 3.38 | 20 | 30.0 | 8.30 | 2.24 | -5.17 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.77 | -0.23 | 0 | — | 2.45 | 1.24 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.46 | -1.54 | 0 | — | -0.18 | -0.12 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.17 | -1.83 | 77 | 33.8 | 7.81 | 3.26 | -2.25 | 102 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.12 | -2.01 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.27 | -3.73 | 0 | — | -0.33 | -0.19 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 95.79 | -4.21 | 120 | 30.8 | -2.39 | -1.33 | -6.28 | 191 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.60 | 1.07 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.19 | -2.66 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.69 | -5.31 | 0 | — | -7.06 | -3.00 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.58 | -5.42 | 0 | — | 0.58 | 0.44 | -9.28 | 1 |
| 19 | Copy: Insider buying | copy | 94.18 | -5.82 | 25 | 40.0 | -15.83 | -3.01 | -21.73 | 60 |
| 20 | Trend pullback · 1h | trend | 93.51 | -6.49 | 95 | 23.2 | -21.75 | -7.04 | -22.05 | 115 |
| 21 | Gap and go | momentum | 93.02 | -6.98 | 99 | 21.2 | 3.43 | 1.16 | -8.76 | 194 |
| 22 | Max aggression: 5-day momentum | meta | 92.96 | -7.04 | 11 | 45.5 | -13.79 | -1.22 | -27.80 | 25 |
| 23 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -15.26 | -3.44 | -16.02 | 96 |
| 24 | Opening range 30m | breakout | 92.91 | -7.09 | 253 | 34.4 | -10.52 | -3.22 | -17.21 | 557 |
| 25 | Daily: Momentum burst | daily | 91.47 | -8.53 | 10 | 10.0 | -18.54 | -3.77 | -20.97 | 40 |
| 26 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.02 | -0.70 | -11.55 | 91 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.15 | -2.18 | -16.91 | 1 |
| 28 | Parabolic SAR · 1h | trend | 91.02 | -8.98 | 120 | 25.0 | -23.63 | -5.78 | -24.08 | 256 |
| 29 | ADX DI cross · 1h | trend | 90.11 | -9.89 | 112 | 17.9 | -12.60 | -2.53 | -15.52 | 258 |
| 30 | Daily: Bullish score | daily | 90.09 | -9.90 | 11 | 18.2 | -7.27 | -0.90 | -14.40 | 13 |
| 31 | Volume breakout · 1h | breakout | 89.40 | -10.60 | 102 | 23.5 | -12.89 | -2.71 | -15.60 | 112 |
| 32 | Agent | meta | 89.29 | -10.71 | 102 | 38.2 | -11.65 | -7.72 | -12.54 | 208 |
| 33 | Bollinger breakout · 1h | breakout | 88.52 | -11.48 | 106 | 27.4 | -12.31 | -2.40 | -16.71 | 241 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.21 | -11.79 | 0 | — | -6.42 | -0.95 | -14.62 | 1 |
| 35 | Agent (aggressive) | meta | 87.63 | -12.37 | 48 | 35.4 | -10.88 | -3.67 | -14.77 | 90 |
| 36 | Stochastic reversion · 1h | reversion | 87.19 | -12.81 | 189 | 44.4 | -20.93 | -3.94 | -22.42 | 392 |
| 37 | Opening range 15m | breakout | 86.17 | -13.83 | 318 | 30.5 | -15.41 | -4.42 | -17.87 | 699 |
| 38 | Keltner breakout · 1h | breakout | 86.10 | -13.90 | 73 | 23.3 | -21.72 | -4.43 | -23.16 | 189 |
| 39 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 40 | EMA 20/50 cross · 1h | trend | 84.86 | -15.14 | 72 | 11.1 | -23.58 | -4.82 | -23.90 | 135 |
| 41 | RSI momentum · 1h | momentum | 84.71 | -15.29 | 103 | 15.5 | -22.66 | -4.91 | -23.11 | 213 |
| 42 | Supertrend · 1h | trend | 84.02 | -15.98 | 113 | 14.2 | -27.34 | -6.10 | -27.94 | 217 |
| 43 | Ichimoku · 1h | trend | 83.71 | -16.29 | 65 | 12.3 | -24.28 | -5.10 | -24.44 | 109 |
| 44 | Z-score reversion · 1h | reversion | 83.60 | -16.40 | 114 | 33.3 | -15.63 | -2.63 | -21.48 | 206 |
| 45 | MFI reversion · 1h | reversion | 82.75 | -17.25 | 263 | 31.6 | -15.87 | -2.46 | -20.70 | 150 |
| 46 | MACD cross · 1h | trend | 82.49 | -17.51 | 234 | 22.2 | -27.36 | -5.76 | -27.80 | 464 |
| 47 | Triple EMA stack · 1h | trend | 82.45 | -17.55 | 99 | 15.2 | -28.64 | -5.83 | -29.43 | 211 |
| 48 | Williams %R · 1h | reversion | 81.01 | -18.99 | 217 | 43.3 | -35.71 | -6.28 | -36.35 | 536 |
| 49 | MACD zero-line · 1h | trend | 80.99 | -19.01 | 106 | 15.1 | -23.89 | -5.21 | -25.47 | 217 |
| 50 | Bollinger reversion · 1h | reversion | 80.87 | -19.13 | 171 | 34.5 | -29.70 | -6.03 | -31.41 | 375 |
| 51 | Donchian 20/10 · 1h | breakout | 80.67 | -19.33 | 98 | 19.4 | -24.48 | -4.71 | -27.51 | 217 |
| 52 | CCI reversion · 1h | reversion | 79.98 | -20.02 | 208 | 41.3 | -26.46 | -3.91 | -28.08 | 469 |
| 53 | OBV trend · 1h | momentum | 79.85 | -20.15 | 204 | 17.2 | -32.76 | -7.23 | -33.51 | 303 |
| 54 | Three white soldiers | momentum | 79.30 | -20.70 | 289 | 19.0 | -44.14 | -20.35 | -44.14 | 594 |
| 55 | Agent (ML meta-label) | meta | 78.42 | -21.58 | 896 | 18.9 | -18.99 | -4.01 | -19.53 | 361 |
| 56 | ROC + volume · 1h | momentum | 77.51 | -22.49 | 242 | 23.6 | -30.35 | -6.02 | -32.09 | 380 |
| 57 | Heikin-Ashi · 1h | trend | 77.07 | -22.93 | 284 | 22.5 | -44.75 | -10.30 | -45.15 | 663 |
| 58 | RSI(14) reversion · 1h | reversion | 76.98 | -23.02 | 99 | 23.2 | -14.80 | -2.70 | -24.48 | 189 |
| 59 | Candlestick reversal · 1h | reversion | 75.81 | -24.19 | 269 | 27.9 | -34.81 | -6.60 | -34.91 | 555 |
| 60 | EMA 9/21 cross · 1h | trend | 75.72 | -24.28 | 170 | 11.2 | -32.06 | -6.55 | -35.38 | 329 |
| 61 | VWAP momentum · 1h | momentum | 75.02 | -24.98 | 537 | 20.7 | -50.48 | -11.55 | -50.66 | 1235 |
| 62 | Max aggression: 1-day momentum | meta | 67.35 | -32.65 | 19 | 26.3 | -41.83 | -2.86 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.24 | -44.76 | 736 | 21.9 | -74.75 | -27.18 | -74.80 | 1566 |
| 64 | Volume breakout | breakout | 54.22 | -45.78 | 448 | 12.3 | -62.57 | -26.38 | -62.73 | 798 |
| 65 | Squeeze breakout | breakout | 51.12 | -48.88 | 582 | 13.6 | -67.88 | -28.89 | -68.01 | 1184 |
| 66 | Donchian 55/20 | breakout | 50.93 | -49.07 | 593 | 18.5 | -72.23 | -24.11 | -72.35 | 1273 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.56 | -98.91 | 5200 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.47 | -23.71 | -79.49 | 1432 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.08 | -47.13 | -94.08 | 2551 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.30 | -30.99 | -89.32 | 1914 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.57 | -38.99 | -91.59 | 2347 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.79 | -31.57 | -90.80 | 2179 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -55.43 | -97.96 | 3534 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -61.19 | -96.25 | 3388 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.18 | -35.86 | -94.25 | 2466 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.08 | -36.35 | -83.08 | 1702 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -56.35 | -99.44 | 5800 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.75 | -43.11 | -92.76 | 2625 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -38.77 | -95.58 | 3388 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -82.00 | -99.78 | 6189 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -45.91 | -92.49 | 2351 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -65.96 | -97.71 | 3565 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -61.85 | -98.68 | 4816 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -57.61 | -94.68 | 2786 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.42 | -39.68 | -84.46 | 1800 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.05 | -99.61 | 6300 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.56 | -29.72 | -88.58 | 2258 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.78 | -19.97 | -77.82 | 1705 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.75 | -38.13 | -90.77 | 2278 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.38 | -49.87 | -96.40 | 3838 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.93 | -51.03 | -89.94 | 2115 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.33 | -18.04 | -76.54 | 1589 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -49.94 | -96.57 | 4205 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -107.62 | -99.92 | 8256 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T14:11 | Agent (ML meta-label) | buy | IWM | 4.76 | — | entry |
| 2026-10-26T14:11 | Agent | buy | PLTR | 17.86 | — | following VWAP momentum |
| 2026-10-26T14:11 | EMA 9/21 cross · 1h | buy | SQQQ | 3.79 | — | rebalance up |
| 2026-10-26T14:11 | Squeeze breakout | buy | AMZN | 8.52 | — | entry signal |
| 2026-10-26T14:11 | Squeeze breakout | sell | NVDA | 6.35 | -0.05 | stop-loss |
| 2026-10-26T14:11 | Opening range 30m | buy | TNA | 23.23 | — | entry signal |
| 2026-10-26T14:11 | Opening range 30m | buy | IWM | 23.23 | — | entry signal |
| 2026-10-26T14:11 | Donchian 55/20 | sell | NVDA | 7.24 | -0.05 | stop-loss |
| 2026-10-26T14:11 | Gap and go | sell | NVDA | 23.22 | -0.15 | stop-loss |
| 2026-10-26T14:11 | ROC + volume | buy | TECL | 11.05 | — | entry signal |
| 2026-10-26T14:11 | ROC + volume | sell | NVDA | 9.16 | -0.06 | stop-loss |
| 2026-10-26T14:05 | Agent (ML meta-label) | sell | SPY | 3.30 | 0.00 | selected signal exited |
| 2026-10-26T14:05 | Agent (ML meta-label) | sell | IWM | 6.03 | 0.00 | selected signal exited |
| 2026-10-26T14:05 | Volume breakout | buy | TNA | 13.55 | — | entry |
| 2026-10-26T14:05 | Gap and go | sell | LABU | 18.59 | 0.01 | exit signal |
| 2026-10-26T14:00 | Day trade: Stocks in Play ORB | sell | SOXL | 24.06 | -0.67 | target is flat |
| 2026-10-26T14:00 | Day trade: Stocks in Play ORB | sell | QQQ | 24.62 | -0.11 | target is flat |
| 2026-10-26T14:00 | Agent (ML meta-label) | buy | SPY | 3.30 | — | entry |
| 2026-10-26T14:00 | Agent (ML meta-label) | buy | NVDA | 6.03 | — | entry |
| 2026-10-26T14:00 | Agent (ML meta-label) | buy | IWM | 6.03 | — | entry |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | TNA | 3.76 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | SQQQ | 3.86 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | PLTR | 3.95 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | MSFT | 3.91 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | LABU | 3.83 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | IWM | 3.87 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.90 | — | rebalance up |
| 2026-10-26T14:00 | VWAP momentum · 1h | sell | XRP-USD | 6.77 | -0.05 | exit signal |
| 2026-10-26T14:00 | VWAP momentum · 1h | sell | SOL-USD | 6.78 | -0.04 | exit signal |
| 2026-10-26T14:00 | VWAP momentum · 1h | sell | ETH-USD | 6.76 | -0.05 | exit signal |
| 2026-10-26T14:00 | VWAP momentum · 1h | sell | BTC-USD | 6.76 | -0.08 | exit signal |
| 2026-10-26T14:00 | Heikin-Ashi · 1h | sell | XRP-USD | 15.44 | -0.16 | exit signal |
| 2026-10-26T14:00 | Heikin-Ashi · 1h | sell | SOL-USD | 15.43 | -0.17 | exit signal |
| 2026-10-26T14:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 15.44 | -0.16 | exit signal |
| 2026-10-26T14:00 | EMA 9/21 cross · 1h | buy | AAPL | 3.87 | — | rebalance up |
| 2026-10-26T14:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 10.75 | -0.15 | exit signal |
| 2026-10-26T14:00 | Volume breakout | sell | TNA | 13.55 | -0.02 | target is flat |
| 2026-10-26T14:00 | Donchian 55/20 | buy | UPRO | 2.63 | — | rebalance up |
| 2026-10-26T14:00 | Donchian 55/20 | buy | TSLA | 2.60 | — | rebalance up |
| 2026-10-26T14:00 | Donchian 55/20 | buy | TNA | 2.61 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 14:11:05.000157+00:00 -> 2026-10-26 14:21:05.000157+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
