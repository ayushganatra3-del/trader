# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T15:25:05.000110+00:00 · 47321 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.87 (-10.13%)

Closed trades 143, win rate 38.5%, fees £4.00, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.72 | -0.31 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 12354 decisions in 1929 calls, $0.1651 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T15:25 | 0 / 13 / 17 | cash |  |
| Breezy | 2026-11-04T15:25 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-04T15:25 | 5 / 23 / 2 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 110.37 | 10.37 | 0 | — | 11.64 | 4.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 108.19 | 8.19 | 17 | 70.6 | 7.75 | 2.35 | -4.91 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.26 | 2.26 | 26 | 46.2 | 0.75 | 0.35 | -5.52 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 101.41 | 1.41 | 0 | — | 5.47 | 1.53 | -6.60 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.10 | 0.10 | 5 | 40.0 | 5.29 | 1.21 | -7.93 | 8 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 9 | Hold SPY | benchmark | 97.85 | -2.15 | 0 | — | -0.83 | -0.38 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.64 | -3.36 | 110 | 35.5 | 6.41 | 2.95 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.64 | -4.36 | 0 | — | -1.66 | -0.56 | -7.64 | 1 |
| 15 | Agent (rotation) | meta | 94.72 | -5.28 | 157 | 28.7 | -5.87 | -4.56 | -8.13 | 175 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Hold BTC | benchmark | 94.51 | -5.49 | 0 | — | -0.58 | 0.07 | -13.22 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.21 | -5.79 | 0 | — | -4.91 | -1.85 | -6.35 | 1 |
| 19 | Gap and go | momentum | 94.08 | -5.92 | 151 | 26.5 | -0.03 | 0.07 | -8.76 | 223 |
| 20 | Max aggression: 5-day momentum | meta | 92.49 | -7.51 | 16 | 43.8 | -22.68 | -1.26 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Parabolic SAR · 1h | trend | 91.07 | -8.93 | 153 | 26.8 | -12.68 | -2.66 | -18.39 | 237 |
| 23 | Trend pullback · 1h | trend | 90.94 | -9.06 | 103 | 22.3 | -16.46 | -6.10 | -17.40 | 78 |
| 24 | Opening range 30m | breakout | 90.03 | -9.97 | 350 | 33.4 | -14.88 | -4.90 | -17.21 | 587 |
| 25 | Agent | meta | 89.87 | -10.13 | 143 | 38.5 | -11.43 | -6.89 | -12.62 | 205 |
| 26 | Copy: Insider buying | copy | 88.80 | -11.20 | 37 | 37.8 | -22.00 | -4.47 | -23.13 | 63 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.78 | -2.56 | -14.15 | 89 |
| 28 | Donchian 55/20 · 1h | breakout | 87.24 | -12.76 | 62 | 12.9 | -14.73 | -3.32 | -19.86 | 104 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.68 | -13.32 | 1 | 0.0 | -6.77 | -0.98 | -16.59 | 1 |
| 30 | Daily: Bullish score | daily | 86.58 | -13.42 | 14 | 21.4 | -11.76 | -1.83 | -16.58 | 14 |
| 31 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -11.94 | -3.93 | -14.77 | 95 |
| 32 | Volume breakout · 1h | breakout | 85.62 | -14.38 | 130 | 28.5 | -13.70 | -3.08 | -18.08 | 95 |
| 33 | Stochastic reversion · 1h | reversion | 85.31 | -14.69 | 243 | 46.9 | -22.28 | -4.40 | -25.60 | 388 |
| 34 | ADX DI cross · 1h | trend | 85.02 | -14.98 | 154 | 17.5 | -17.72 | -3.22 | -22.29 | 263 |
| 35 | Keltner breakout · 1h | breakout | 84.65 | -15.35 | 91 | 23.1 | -20.28 | -4.21 | -23.05 | 175 |
| 36 | MFI reversion · 1h | reversion | 83.40 | -16.60 | 315 | 34.0 | -14.45 | -2.25 | -18.14 | 151 |
| 37 | Opening range 15m | breakout | 83.29 | -16.71 | 427 | 30.7 | -19.60 | -5.96 | -21.19 | 722 |
| 38 | Connors RSI(2) · 1h | reversion | 82.65 | -17.35 | 192 | 40.6 | -19.63 | -6.52 | -20.11 | 130 |
| 39 | Ichimoku · 1h | trend | 82.34 | -17.66 | 84 | 13.1 | -16.99 | -3.39 | -25.73 | 121 |
| 40 | Bollinger breakout · 1h | breakout | 82.13 | -17.87 | 145 | 24.1 | -16.68 | -3.31 | -23.94 | 237 |
| 41 | CCI reversion · 1h | reversion | 80.87 | -19.13 | 270 | 45.2 | -22.51 | -3.29 | -27.71 | 456 |
| 42 | Z-score reversion · 1h | reversion | 80.03 | -19.98 | 144 | 34.7 | -10.93 | -1.44 | -23.02 | 221 |
| 43 | Bollinger reversion · 1h | reversion | 79.46 | -20.54 | 229 | 39.7 | -25.61 | -4.81 | -30.37 | 380 |
| 44 | Heikin-Ashi · 1h | trend | 79.09 | -20.91 | 372 | 22.6 | -39.60 | -8.07 | -43.55 | 666 |
| 45 | MACD cross · 1h | trend | 78.92 | -21.08 | 307 | 23.1 | -31.18 | -5.88 | -33.86 | 481 |
| 46 | MACD zero-line · 1h | trend | 78.83 | -21.17 | 141 | 15.6 | -25.07 | -5.19 | -30.17 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 78.55 | -21.45 | 92 | 10.9 | -20.65 | -3.91 | -27.62 | 130 |
| 48 | Supertrend · 1h | trend | 78.16 | -21.84 | 145 | 12.4 | -26.61 | -4.96 | -30.19 | 228 |
| 49 | Williams %R · 1h | reversion | 77.61 | -22.39 | 283 | 46.6 | -35.70 | -6.21 | -38.02 | 535 |
| 50 | RSI momentum · 1h | momentum | 77.08 | -22.92 | 141 | 12.1 | -28.32 | -5.46 | -31.09 | 217 |
| 51 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.24 | -4.45 | -33.57 | 33 |
| 52 | Triple EMA stack · 1h | trend | 76.15 | -23.85 | 130 | 13.8 | -26.65 | -4.80 | -32.22 | 199 |
| 53 | OBV trend · 1h | momentum | 75.67 | -24.33 | 246 | 17.5 | -30.36 | -6.62 | -31.25 | 288 |
| 54 | Donchian 20/10 · 1h | breakout | 75.03 | -24.97 | 123 | 19.5 | -26.72 | -4.83 | -31.68 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.82 | -25.18 | 314 | 25.5 | -33.99 | -6.60 | -37.24 | 375 |
| 56 | RSI(14) reversion · 1h | reversion | 74.39 | -25.61 | 135 | 28.9 | -18.94 | -3.03 | -26.28 | 224 |
| 57 | Candlestick reversal · 1h | reversion | 72.53 | -27.48 | 373 | 30.3 | -33.10 | -5.87 | -38.74 | 568 |
| 58 | Agent (ML meta-label) | meta | 70.57 | -29.43 | 1388 | 22.0 | -2.98 | -0.46 | -15.96 | 258 |
| 59 | VWAP momentum · 1h | momentum | 70.44 | -29.56 | 720 | 22.1 | -54.64 | -10.99 | -56.52 | 1228 |
| 60 | EMA 9/21 cross · 1h | trend | 69.76 | -30.24 | 225 | 9.8 | -36.87 | -7.37 | -40.44 | 334 |
| 61 | Three white soldiers | momentum | 68.24 | -31.76 | 427 | 15.7 | -46.59 | -21.15 | -47.11 | 629 |
| 62 | Max aggression: 1-day momentum | meta | 65.31 | -34.69 | 24 | 29.2 | -37.10 | -2.24 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.18 | -98.99 | 5174 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -23.69 | -80.25 | 1420 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -43.36 | -93.52 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.73 | -29.31 | -89.12 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -35.52 | -91.21 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.39 | -31.74 | -90.41 | 2185 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.67 | -47.99 | -97.75 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -52.67 | -96.28 | 3359 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -32.48 | -93.67 | 2450 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.05 | -35.03 | -82.06 | 1643 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.95 | -99.49 | 5884 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.95 | -41.54 | -93.10 | 2622 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -36.80 | -95.43 | 3356 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.86 | -99.80 | 6167 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.62 | -39.69 | -91.88 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.78 | -26.54 | -75.04 | 1563 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -54.67 | -97.76 | 3490 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.25 | -98.71 | 4828 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.25 | -26.51 | -70.55 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -50.55 | -94.88 | 2780 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.51 | -34.72 | -84.97 | 1789 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.76 | -99.63 | 6316 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.19 | -30.05 | -88.43 | 2256 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.80 | -19.18 | -77.02 | 1711 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -37.14 | -90.61 | 2229 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.48 | -50.32 | -96.54 | 3834 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.98 | -46.36 | -89.35 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.84 | -25.77 | -65.78 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.55 | -24.25 | -74.12 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.18 | -19.04 | -77.40 | 1619 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.98 | -52.27 | -96.99 | 4246 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.00 | -99.92 | 8197 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T15:25 | Agent (ML meta-label) | sell | GOOGL | 17.59 | -0.03 | selected signal exited |
| 2026-11-04T15:25 | Agent (ML meta-label) | sell | ETH-USD | 17.52 | -0.10 | selected signal exited |
| 2026-11-04T15:25 | EMA 20/50 cross · 1h | buy | DOGE-USD | 4.02 | — | rebalance up |
| 2026-11-04T15:25 | EMA 20/50 cross · 1h | sell | SQQQ | 4.02 | -0.01 | rebalance down |
| 2026-11-04T15:25 | Three white soldiers | buy | BITX | 10.55 | — | entry |
| 2026-11-04T15:25 | Three white soldiers | sell | SOL-USD | 3.54 | 0.03 | rebalance down |
| 2026-11-04T15:25 | Three white soldiers | sell | BTC-USD | 3.56 | 0.03 | rebalance down |
| 2026-11-04T15:25 | Three white soldiers | sell | AAPL | 3.46 | 0.02 | rebalance down |
| 2026-11-04T15:20 | Agent (ML meta-label) | buy | SQQQ | 17.62 | — | entry |
| 2026-11-04T15:20 | Agent (ML meta-label) | buy | GOOGL | 17.62 | — | entry |
| 2026-11-04T15:20 | Agent (ML meta-label) | buy | ETHU | 17.62 | — | entry |
| 2026-11-04T15:20 | Agent (ML meta-label) | buy | ETH-USD | 17.62 | — | entry |
| 2026-11-04T15:20 | Candlestick reversal · 1h | buy | SOXL | 3.73 | — | rebalance up |
| 2026-11-04T15:15 | Agent (rotation) | buy | SPY | 2.27 | — | entry |
| 2026-11-04T15:15 | Agent (ML meta-label) | sell | ETHU | 18.28 | 1.12 | selected signal exited |
| 2026-11-04T15:15 | Three white soldiers | buy | MSTR | 16.93 | — | entry signal |
| 2026-11-04T15:10 | Agent (rotation) | buy | QQQ | 2.44 | — | entry |
| 2026-11-04T15:10 | Agent (rotation) | buy | COIN | 2.44 | — | entry |
| 2026-11-04T15:10 | Agent (ML meta-label) | sell | SQQQ | 17.00 | -0.30 | selected signal exited |
| 2026-11-04T15:10 | Agent (ML meta-label) | sell | GOOGL | 5.10 | -0.02 | selected signal exited |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | TQQQ | 5.62 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | TECL | 5.66 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | SOXL | 6.21 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | QQQ | 5.86 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | PLTR | 6.47 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | buy | AMD | 5.84 | — | rebalance up |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | sell | MSTR | 7.02 | 0.51 | take-profit |
| 2026-11-04T15:10 | RSI(14) reversion · 1h | sell | BITX | 7.15 | 0.49 | take-profit |
| 2026-11-04T15:10 | Candlestick reversal · 1h | buy | TECL | 3.79 | — | rebalance up |
| 2026-11-04T15:10 | Candlestick reversal · 1h | sell | TQQQ | 14.59 | 0.22 | take-profit |
| 2026-11-04T15:10 | Candlestick reversal · 1h | sell | MSTR | 14.77 | 0.74 | take-profit |
| 2026-11-04T15:10 | Candlestick reversal · 1h | sell | COIN | 14.78 | 0.69 | take-profit |
| 2026-11-04T15:10 | Opening range 15m | buy | TECL | 1.72 | — | entry signal |
| 2026-11-04T15:05 | Agent (rotation) | buy | UPRO | 3.16 | — | entry |
| 2026-11-04T15:05 | Agent (rotation) | buy | TSLA | 3.16 | — | entry |
| 2026-11-04T15:05 | Agent (rotation) | buy | PLTR | 3.16 | — | entry |
| 2026-11-04T15:05 | Agent (rotation) | buy | MSTR | 3.16 | — | entry |
| 2026-11-04T15:05 | Agent (rotation) | buy | MSFT | 3.16 | — | following MACD zero-line, Bollinger reversion · 1h |
| 2026-11-04T15:05 | Agent (rotation) | buy | GOOGL | 3.16 | — | entry |
| 2026-11-04T15:05 | Agent (rotation) | buy | ETHU | 3.16 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 15:25:05.000110+00:00 -> 2026-11-04 15:35:05.000110+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 15:25:05.000110+00:00 -> 2026-11-04 15:35:05.000110+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 15:25:05.000110+00:00 -> 2026-11-04 15:35:05.000110+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
