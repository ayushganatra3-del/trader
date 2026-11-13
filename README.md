# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T17:40:05.000148+00:00 · 58460 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.39 (-14.61%)

Closed trades 194, win rate 35.6%, fees £5.62, max drawdown -15.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 17.21 | +0.16 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 26754 decisions in 2835 calls, $0.3399 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T17:40 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-11-13T17:40 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-13T17:40 | 5 / 20 / 5 | BITX 81% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| MFI reversion | TSLA | 1.68 | +2.04% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.96 | 17.96 | 0 | — | 15.39 | 5.13 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 116.68 | 16.68 | 34 | 29.4 | 25.15 | 3.54 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.60 | 13.60 | 22 | 68.2 | 17.04 | 3.46 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.11 | 6.11 | 32 | 43.8 | 6.03 | 1.48 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 105.04 | 5.04 | 0 | — | 7.02 | 1.91 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.51 | 1.51 | 141 | 34.8 | 8.09 | 3.17 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.93 | -2.07 | 0 | — | -0.99 | -0.27 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.37 | -3.63 | 1 | 0.0 | -3.77 | -2.36 | -6.65 | 2 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.23 | -3.77 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 14 | Agent (rotation) | meta | 96.00 | -4.00 | 191 | 30.4 | -2.93 | -0.99 | -8.69 | 161 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 17 | Copy: Insider buying | copy | 93.71 | -6.29 | 43 | 39.5 | -5.67 | -1.07 | -14.81 | 66 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 93.02 | -6.98 | 0 | — | -5.47 | -1.47 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.74 | -8.26 | 110 | 22.7 | -14.75 | -5.40 | -17.77 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -11.93 | -2.49 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 86.07 | -13.93 | 433 | 33.3 | -10.02 | -3.16 | -14.11 | 603 |
| 24 | Daily: Bullish score | daily | 86.00 | -14.01 | 16 | 18.8 | -9.95 | -1.57 | -19.56 | 15 |
| 25 | Agent | meta | 85.39 | -14.61 | 194 | 35.6 | -15.59 | -7.81 | -16.04 | 209 |
| 26 | Parabolic SAR · 1h | trend | 85.23 | -14.77 | 176 | 29.0 | -15.66 | -3.38 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -17.85 | -5.03 | -18.77 | 100 |
| 28 | Donchian 55/20 · 1h | breakout | 81.59 | -18.41 | 73 | 13.7 | -23.45 | -4.88 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.30 | -18.70 | 1 | 0.0 | -11.08 | -1.56 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 80.64 | -19.36 | 2 | 0.0 | -10.11 | -1.17 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 211 | 40.3 | -18.15 | -6.38 | -18.32 | 114 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.51 | -19.49 | 120 | 25.8 | -17.08 | -3.45 | -25.32 | 170 |
| 34 | Stochastic reversion · 1h | reversion | 79.27 | -20.73 | 302 | 47.4 | -26.66 | -3.94 | -28.24 | 401 |
| 35 | Opening range 15m | breakout | 78.49 | -21.52 | 526 | 31.2 | -17.29 | -4.64 | -21.36 | 719 |
| 36 | MFI reversion · 1h | reversion | 77.37 | -22.63 | 395 | 35.2 | -23.19 | -3.00 | -27.13 | 166 |
| 37 | ADX DI cross · 1h | trend | 76.79 | -23.21 | 198 | 19.7 | -23.77 | -3.59 | -32.07 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -42.36 | -2.73 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Heikin-Ashi · 1h | trend | 75.14 | -24.86 | 442 | 24.2 | -37.78 | -7.05 | -39.26 | 662 |
| 41 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 42 | MACD cross · 1h | trend | 74.84 | -25.16 | 385 | 23.6 | -29.24 | -4.35 | -38.65 | 469 |
| 43 | Max aggression: 1-day momentum | meta | 73.87 | -26.13 | 29 | 27.6 | -21.23 | -0.68 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.16 | -4.53 | -30.99 | 203 |
| 45 | Supertrend · 1h | trend | 72.60 | -27.40 | 180 | 15.0 | -30.50 | -5.22 | -36.51 | 215 |
| 46 | RSI momentum · 1h | momentum | 72.55 | -27.45 | 171 | 14.0 | -27.11 | -4.17 | -37.92 | 208 |
| 47 | EMA 20/50 cross · 1h | trend | 71.83 | -28.17 | 109 | 10.1 | -29.38 | -4.95 | -40.51 | 121 |
| 48 | Bollinger reversion · 1h | reversion | 71.67 | -28.33 | 301 | 41.5 | -33.58 | -5.26 | -35.72 | 383 |
| 49 | ROC + volume · 1h | momentum | 71.53 | -28.47 | 397 | 28.7 | -31.22 | -5.75 | -38.37 | 376 |
| 50 | Triple EMA stack · 1h | trend | 71.16 | -28.84 | 150 | 14.0 | -28.94 | -4.78 | -38.65 | 204 |
| 51 | CCI reversion · 1h | reversion | 70.96 | -29.04 | 346 | 43.4 | -38.69 | -6.11 | -39.53 | 464 |
| 52 | OBV trend · 1h | momentum | 69.49 | -30.51 | 298 | 19.1 | -30.81 | -5.43 | -38.11 | 277 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.90 | -4.59 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.20 | -30.80 | 153 | 19.0 | -30.35 | -5.43 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.61 | -32.39 | 382 | 43.5 | -43.15 | -7.08 | -44.04 | 542 |
| 56 | Z-score reversion · 1h | reversion | 65.41 | -34.59 | 204 | 37.3 | -30.55 | -4.32 | -31.55 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 64.64 | -35.36 | 266 | 11.3 | -38.12 | -7.71 | -43.16 | 330 |
| 58 | Agent (ML meta-label) | meta | 64.44 | -35.56 | 1841 | 24.8 | -21.25 | -3.10 | -25.88 | 348 |
| 59 | RSI(14) reversion · 1h | reversion | 64.05 | -35.95 | 186 | 32.8 | -37.97 | -5.65 | -38.98 | 241 |
| 60 | VWAP momentum · 1h | momentum | 62.58 | -37.42 | 911 | 22.2 | -53.15 | -10.64 | -53.72 | 1220 |
| 61 | Candlestick reversal · 1h | reversion | 61.55 | -38.45 | 486 | 28.4 | -44.95 | -8.23 | -45.99 | 604 |
| 62 | Three white soldiers | momentum | 58.38 | -41.62 | 541 | 14.6 | -49.46 | -22.23 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.61 | -99.02 | 5294 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.05 | -25.64 | -80.19 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -46.45 | -93.85 | 2535 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.69 | -89.29 | 1923 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.33 | -41.53 | -91.33 | 2338 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.78 | -31.20 | -89.79 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.60 | -97.91 | 3499 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -57.75 | -96.30 | 3437 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -33.66 | -93.75 | 2344 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -34.91 | -83.28 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.64 | -99.57 | 6038 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -43.35 | -92.26 | 2628 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.39 | -37.07 | -95.40 | 3471 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.56 | -99.81 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.31 | -43.09 | -92.31 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.77 | -25.97 | -75.94 | 1644 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -60.65 | -97.63 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -64.05 | -98.90 | 4947 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.81 | -27.06 | -68.85 | 1247 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -57.44 | -94.77 | 2801 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.09 | -39.31 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.86 | -99.67 | 6381 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.11 | -32.67 | -90.22 | 2329 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.67 | -20.17 | -78.89 | 1798 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.79 | -36.85 | -90.90 | 2187 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.03 | -52.02 | -97.04 | 3892 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.57 | -58.11 | -89.59 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.47 | -30.68 | -66.47 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.45 | -23.07 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.17 | -19.27 | -80.42 | 1748 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.42 | -51.01 | -97.43 | 4354 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.88 | -99.93 | 8424 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T17:40 | Agent (ML meta-label) | buy | PLTR | 1.83 | — | following VWAP reversion |
| 2026-11-13T17:40 | Agent (ML meta-label) | buy | MSTR | 5.37 | — | entry |
| 2026-11-13T17:40 | Agent (ML meta-label) | buy | ETHU | 5.37 | — | entry |
| 2026-11-13T17:40 | Agent (ML meta-label) | sell | GOOGL | 6.44 | 0.00 | selected signal exited |
| 2026-11-13T17:40 | Agent (ML meta-label) | sell | AMZN | 5.84 | -0.07 | selected signal exited |
| 2026-11-13T17:40 | Three white soldiers | buy | BTC-USD | 14.61 | — | entry signal |
| 2026-11-13T17:30 | Agent (ML meta-label) | buy | AMD | 5.34 | — | entry |
| 2026-11-13T17:30 | MFI reversion · 1h | buy | TSLA | 9.65 | — | entry signal |
| 2026-11-13T17:30 | MFI reversion · 1h | buy | TQQQ | 9.70 | — | entry signal |
| 2026-11-13T17:30 | MFI reversion · 1h | buy | QQQ | 9.70 | — | entry signal |
| 2026-11-13T17:30 | MFI reversion · 1h | buy | NVDA | 9.70 | — | entry signal |
| 2026-11-13T17:30 | MFI reversion · 1h | sell | TECL | 9.37 | 0.19 | rebalance down |
| 2026-11-13T17:30 | MFI reversion · 1h | sell | META | 9.98 | 0.08 | rebalance down |
| 2026-11-13T17:30 | MFI reversion · 1h | sell | BTC-USD | 9.70 | -0.10 | rebalance down |
| 2026-11-13T17:30 | MFI reversion · 1h | sell | AMZN | 9.70 | -0.10 | rebalance down |
| 2026-11-13T17:30 | CCI reversion · 1h | buy | PLTR | 5.26 | — | entry signal |
| 2026-11-13T17:30 | Williams %R · 1h | buy | QQQ | 2.51 | — | entry signal |
| 2026-11-13T17:30 | Williams %R · 1h | buy | LABU | 4.23 | — | entry signal |
| 2026-11-13T17:30 | Stochastic reversion · 1h | buy | ETHU | 3.08 | — | entry signal |
| 2026-11-13T17:30 | OBV trend · 1h | buy | META | 17.39 | — | entry signal |
| 2026-11-13T17:30 | VWAP momentum · 1h | buy | MSFT | 9.52 | — | entry signal |
| 2026-11-13T17:30 | VWAP momentum · 1h | sell | TSLA | 3.17 | 0.01 | rebalance down |
| 2026-11-13T17:30 | VWAP momentum · 1h | sell | META | 3.20 | 0.01 | rebalance down |
| 2026-11-13T17:30 | VWAP momentum · 1h | sell | DOGE-USD | 3.15 | -0.02 | rebalance down |
| 2026-11-13T17:30 | Heikin-Ashi · 1h | buy | SQQQ | 18.77 | — | entry signal |
| 2026-11-13T17:30 | Parabolic SAR · 1h | sell | GOOGL | 21.01 | 0.10 | exit signal |
| 2026-11-13T17:30 | EMA 20/50 cross · 1h | buy | META | 17.89 | — | entry signal |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | buy | TSLA | 3.70 | — | rebalance up |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | buy | SQQQ | 12.96 | — | entry signal |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | buy | GOOGL | 3.68 | — | rebalance up |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | buy | AMD | 3.72 | — | rebalance up |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | buy | AAPL | 3.72 | — | rebalance up |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | sell | SPY | 9.25 | 0.08 | exit signal |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | sell | QQQ | 9.27 | 0.07 | exit signal |
| 2026-11-13T17:30 | EMA 9/21 cross · 1h | sell | PLTR | 9.26 | 0.08 | exit signal |
| 2026-11-13T17:20 | Agent (ML meta-label) | buy | GOOGL | 6.44 | — | entry |
| 2026-11-13T17:10 | VWAP momentum · 1h | buy | SQQQ | 3.03 | — | rebalance up |
| 2026-11-13T17:00 | Agent (ML meta-label) | sell | GOOGL | 6.27 | -0.01 | selected signal exited |
| 2026-11-13T17:00 | Agent (ML meta-label) | sell | AAPL | 5.81 | 0.01 | selected signal exited |
| 2026-11-13T17:00 | VWAP momentum · 1h | buy | TSLA | 10.52 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 17:40:05.000148+00:00 -> 2026-11-13 17:50:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
