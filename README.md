# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-26T15:43:05.000158+00:00 · 36798 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.93 (-10.06%)

Closed trades 103, win rate 38.8%, fees £3.26, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.15 | +0.29 |

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

Today: 18750 decisions in 2319 calls, $0.2418 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-26T15:43 | 3 / 15 / 12 | cash |  |
| Breezy | 2026-10-26T15:43 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-26T15:43 | 5 / 24 / 1 | COIN 63% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.35 | 7.36 | 13 | 69.2 | 4.69 | 1.49 | -6.79 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.97 | 6.97 | 0 | — | 7.89 | 4.07 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.84 | 6.84 | 20 | 30.0 | 11.86 | 2.97 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.50 | 5.50 | 18 | 44.4 | 7.77 | 2.43 | -4.92 | 27 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.22 | -3.07 | -14.02 | 153 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.39 | 0.39 | 0 | — | 3.31 | 1.51 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.95 | -1.05 | 0 | — | 0.13 | 0.13 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.51 | -1.49 | 77 | 33.8 | 8.17 | 3.43 | -2.25 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -2.01 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 97.03 | -2.97 | 120 | 30.8 | -0.14 | -0.02 | -6.28 | 186 |
| 14 | Copy: Congress Democrats (NANC) | copy | 96.94 | -3.06 | 0 | — | -0.02 | 0.09 | -5.99 | 1 |
| 15 | Gap and go | momentum | 95.73 | -4.27 | 101 | 21.8 | 6.56 | 2.07 | -8.76 | 200 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.07 | -7.93 | 8 |
| 17 | Hold BTC | benchmark | 95.58 | -4.42 | 0 | — | 1.42 | 0.61 | -9.28 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.75 | -5.25 | 0 | — | -7.06 | -3.00 | -7.83 | 1 |
| 20 | Opening range 30m | breakout | 93.78 | -6.22 | 255 | 34.1 | -9.71 | -2.92 | -17.21 | 577 |
| 21 | Trend pullback · 1h | trend | 93.66 | -6.34 | 95 | 23.2 | -21.48 | -6.93 | -21.89 | 114 |
| 22 | Copy: Insider buying | copy | 92.95 | -7.05 | 27 | 37.0 | -16.62 | -3.18 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 92.17 | -7.83 | 49 | 16.3 | -15.44 | -3.52 | -16.06 | 98 |
| 24 | Daily: Momentum burst | daily | 91.77 | -8.23 | 10 | 10.0 | -19.25 | -3.69 | -20.97 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 91.32 | -8.68 | 51 | 23.5 | -3.07 | -0.72 | -11.58 | 92 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.18 | -16.91 | 1 |
| 27 | Daily: Bullish score | daily | 90.65 | -9.35 | 11 | 18.2 | -7.23 | -0.81 | -14.40 | 13 |
| 28 | Parabolic SAR · 1h | trend | 90.48 | -9.52 | 121 | 25.6 | -23.66 | -5.95 | -24.32 | 247 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 90.20 | -9.80 | 0 | — | -4.42 | -0.59 | -14.57 | 1 |
| 30 | Agent | meta | 89.93 | -10.06 | 103 | 38.8 | -11.09 | -7.13 | -12.54 | 208 |
| 31 | Max aggression: 5-day momentum | meta | 89.90 | -10.10 | 11 | 45.5 | -16.68 | -1.56 | -27.80 | 25 |
| 32 | ADX DI cross · 1h | trend | 89.31 | -10.69 | 113 | 17.7 | -14.14 | -2.89 | -16.85 | 269 |
| 33 | Volume breakout · 1h | breakout | 89.12 | -10.88 | 103 | 23.3 | -13.17 | -2.77 | -15.73 | 113 |
| 34 | Stochastic reversion · 1h | reversion | 88.53 | -11.47 | 198 | 47.0 | -19.07 | -3.48 | -22.37 | 393 |
| 35 | Agent (aggressive) | meta | 88.18 | -11.82 | 49 | 36.7 | -10.41 | -3.47 | -14.77 | 90 |
| 36 | Bollinger breakout · 1h | breakout | 88.13 | -11.87 | 107 | 27.1 | -12.89 | -2.52 | -17.07 | 244 |
| 37 | Opening range 15m | breakout | 87.32 | -12.69 | 320 | 30.6 | -14.35 | -4.02 | -17.87 | 718 |
| 38 | Keltner breakout · 1h | breakout | 85.77 | -14.23 | 74 | 23.0 | -23.07 | -4.73 | -24.45 | 192 |
| 39 | Z-score reversion · 1h | reversion | 85.44 | -14.56 | 114 | 33.3 | -13.67 | -2.21 | -21.48 | 209 |
| 40 | Connors RSI(2) · 1h | reversion | 84.91 | -15.10 | 173 | 40.5 | -26.61 | -8.08 | -26.96 | 197 |
| 41 | EMA 20/50 cross · 1h | trend | 84.26 | -15.74 | 72 | 11.1 | -23.38 | -4.65 | -23.69 | 131 |
| 42 | RSI momentum · 1h | momentum | 83.99 | -16.01 | 104 | 15.4 | -20.49 | -4.14 | -20.84 | 207 |
| 43 | MACD cross · 1h | trend | 83.59 | -16.41 | 236 | 22.9 | -27.92 | -5.88 | -29.14 | 473 |
| 44 | Supertrend · 1h | trend | 83.41 | -16.59 | 114 | 14.0 | -28.05 | -6.24 | -28.96 | 223 |
| 45 | MFI reversion · 1h | reversion | 83.22 | -16.78 | 263 | 31.6 | -15.43 | -2.36 | -20.70 | 154 |
| 46 | Ichimoku · 1h | trend | 83.14 | -16.86 | 66 | 12.1 | -23.88 | -5.01 | -23.92 | 108 |
| 47 | Bollinger reversion · 1h | reversion | 82.32 | -17.68 | 179 | 37.4 | -28.25 | -5.52 | -31.32 | 376 |
| 48 | Triple EMA stack · 1h | trend | 82.04 | -17.96 | 99 | 15.2 | -30.93 | -6.24 | -31.46 | 211 |
| 49 | Williams %R · 1h | reversion | 82.02 | -17.98 | 228 | 46.1 | -35.06 | -6.06 | -36.64 | 541 |
| 50 | CCI reversion · 1h | reversion | 81.53 | -18.47 | 211 | 42.2 | -23.93 | -3.38 | -28.08 | 468 |
| 51 | MACD zero-line · 1h | trend | 81.03 | -18.97 | 107 | 15.9 | -23.72 | -5.19 | -25.31 | 220 |
| 52 | Donchian 20/10 · 1h | breakout | 80.36 | -19.64 | 99 | 20.2 | -24.70 | -4.74 | -27.78 | 221 |
| 53 | Agent (ML meta-label) | meta | 79.56 | -20.44 | 904 | 19.2 | -14.56 | -2.77 | -17.33 | 349 |
| 54 | OBV trend · 1h | momentum | 79.36 | -20.64 | 206 | 17.5 | -32.73 | -7.06 | -32.90 | 304 |
| 55 | Three white soldiers | momentum | 79.34 | -20.66 | 292 | 19.2 | -43.90 | -20.13 | -44.18 | 596 |
| 56 | RSI(14) reversion · 1h | reversion | 78.96 | -21.04 | 100 | 24.0 | -18.26 | -3.33 | -24.48 | 207 |
| 57 | ROC + volume · 1h | momentum | 77.16 | -22.84 | 243 | 23.9 | -31.05 | -6.15 | -32.73 | 383 |
| 58 | Heikin-Ashi · 1h | trend | 77.05 | -22.95 | 284 | 22.5 | -44.49 | -10.22 | -45.17 | 671 |
| 59 | Candlestick reversal · 1h | reversion | 77.00 | -23.00 | 270 | 28.1 | -34.11 | -6.35 | -35.93 | 577 |
| 60 | VWAP momentum · 1h | momentum | 75.71 | -24.29 | 538 | 20.6 | -49.98 | -11.33 | -50.53 | 1243 |
| 61 | EMA 9/21 cross · 1h | trend | 75.68 | -24.32 | 171 | 11.1 | -31.78 | -6.49 | -35.15 | 330 |
| 62 | Max aggression: 1-day momentum | meta | 67.66 | -32.34 | 19 | 26.3 | -41.60 | -2.84 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.94 | -44.06 | 740 | 21.9 | -74.31 | -26.59 | -74.73 | 1577 |
| 64 | Volume breakout | breakout | 54.27 | -45.73 | 454 | 12.8 | -62.60 | -26.45 | -62.68 | 800 |
| 65 | Squeeze breakout | breakout | 51.33 | -48.67 | 585 | 14.0 | -67.45 | -28.54 | -67.82 | 1182 |
| 66 | Donchian 55/20 | breakout | 51.24 | -48.76 | 594 | 18.5 | -71.94 | -23.95 | -72.35 | 1285 |
| 67 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -45.53 | -98.92 | 5184 |
| 68 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.16 | -23.58 | -79.37 | 1436 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -46.86 | -93.98 | 2555 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.28 | -30.79 | -89.39 | 1930 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.38 | -38.39 | -91.50 | 2346 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.62 | -31.10 | -90.63 | 2158 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -55.33 | -97.95 | 3537 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.13 | -60.45 | -96.19 | 3370 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.28 | -37.09 | -94.31 | 2471 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.59 | -34.49 | -83.02 | 1702 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -55.82 | -99.44 | 5796 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -42.53 | -92.70 | 2635 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -38.50 | -95.59 | 3363 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -81.08 | -99.78 | 6187 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -45.67 | -92.45 | 2353 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -65.87 | -97.72 | 3567 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.43 | -98.67 | 4810 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.54 | -55.73 | -94.62 | 2783 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -38.43 | -84.53 | 1814 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.82 | -99.61 | 6297 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.40 | -29.36 | -88.59 | 2259 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.44 | -19.55 | -77.83 | 1712 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.69 | -37.99 | -90.78 | 2279 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.37 | -49.76 | -96.40 | 3838 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.94 | -51.42 | -90.01 | 2120 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.41 | -18.05 | -76.55 | 1597 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -49.86 | -96.57 | 4203 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -105.33 | -99.92 | 8263 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-26T15:40 | Agent (ML meta-label) | buy | UPRO | 7.23 | — | entry |
| 2026-10-26T15:40 | Agent (ML meta-label) | buy | SOXL | 5.38 | — | rebalance up |
| 2026-10-26T15:40 | Agent (ML meta-label) | sell | MSTR | 5.28 | -0.02 | selected signal exited |
| 2026-10-26T15:40 | Agent (ML meta-label) | sell | IWM | 5.30 | -0.00 | selected signal exited |
| 2026-10-26T15:40 | Agent (ML meta-label) | sell | ETHU | 5.30 | 0.00 | selected signal exited |
| 2026-10-26T15:40 | Agent (ML meta-label) | sell | BITX | 5.31 | 0.01 | selected signal exited |
| 2026-10-26T15:40 | ROC + volume | buy | AMD | 4.30 | — | entry signal |
| 2026-10-26T15:40 | ROC + volume | sell | AAPL | 4.30 | -0.01 | exit signal |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | SOXL | 1.84 | — | entry |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | PLTR | 5.30 | — | following VWAP momentum |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | MSTR | 5.30 | — | entry |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | IWM | 5.30 | — | entry |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | ETHU | 5.30 | — | entry |
| 2026-10-26T15:35 | Agent (ML meta-label) | buy | BITX | 5.30 | — | following Bollinger reversion, Stochastic reversion |
| 2026-10-26T15:35 | Agent (ML meta-label) | sell | TQQQ | 4.64 | 0.09 | rebalance down |
| 2026-10-26T15:35 | Agent (ML meta-label) | sell | TNA | 4.62 | 0.04 | rebalance down |
| 2026-10-26T15:35 | Agent (ML meta-label) | sell | TECL | 4.63 | 0.14 | rebalance down |
| 2026-10-26T15:35 | Agent (ML meta-label) | sell | AMD | 4.64 | 0.11 | rebalance down |
| 2026-10-26T15:35 | Three white soldiers | sell | LABU | 19.64 | -0.24 | target is flat |
| 2026-10-26T15:35 | Volume breakout | sell | UPRO | 10.89 | 0.12 | exit signal |
| 2026-10-26T15:35 | Volume breakout | sell | TNA | 10.89 | 0.11 | exit signal |
| 2026-10-26T15:35 | Volume breakout | sell | NVDA | 13.53 | -0.10 | exit signal |
| 2026-10-26T15:30 | Agent (ML meta-label) | buy | TQQQ | 5.31 | — | rebalance up |
| 2026-10-26T15:30 | Agent (ML meta-label) | buy | TNA | 5.87 | — | rebalance up |
| 2026-10-26T15:30 | Agent (ML meta-label) | buy | TECL | 5.18 | — | rebalance up |
| 2026-10-26T15:30 | Agent (ML meta-label) | buy | AMD | 4.35 | — | rebalance up |
| 2026-10-26T15:30 | Agent (ML meta-label) | sell | UPRO | 7.99 | 0.17 | selected signal exited |
| 2026-10-26T15:30 | Agent (ML meta-label) | sell | SOXL | 5.57 | 0.56 | selected signal exited |
| 2026-10-26T15:30 | MFI reversion · 1h | buy | META | 10.42 | — | entry signal |
| 2026-10-26T15:30 | MFI reversion · 1h | buy | GOOGL | 10.42 | — | entry signal |
| 2026-10-26T15:30 | MFI reversion · 1h | buy | COIN | 10.42 | — | entry signal |
| 2026-10-26T15:30 | MFI reversion · 1h | sell | XRP-USD | 9.78 | 0.06 | rebalance down |
| 2026-10-26T15:30 | MFI reversion · 1h | sell | TSLA | 6.18 | 0.30 | rebalance down |
| 2026-10-26T15:30 | MFI reversion · 1h | sell | LABU | 6.15 | 0.16 | rebalance down |
| 2026-10-26T15:30 | MFI reversion · 1h | sell | BTC-USD | 9.86 | -0.01 | rebalance down |
| 2026-10-26T15:30 | CCI reversion · 1h | buy | GOOGL | 1.82 | — | entry signal |
| 2026-10-26T15:30 | CCI reversion · 1h | buy | BITX | 4.29 | — | entry signal |
| 2026-10-26T15:30 | Williams %R · 1h | buy | ETHU | 10.25 | — | entry signal |
| 2026-10-26T15:30 | Williams %R · 1h | buy | BITX | 10.25 | — | entry signal |
| 2026-10-26T15:30 | Williams %R · 1h | sell | UPRO | 10.23 | 0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-28 15:43:05.000158+00:00 -> 2026-10-26 15:53:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
