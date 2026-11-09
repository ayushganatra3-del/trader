# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T15:39:05.000129+00:00 · 53543 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.81 (-12.19%)

Closed trades 156, win rate 35.9%, fees £4.86, max drawdown -12.91%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 35.18 | +0.27 |
| TSLA | 17.55 | +0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 15015 decisions in 2493 calls, $0.2025 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T15:39 | 2 / 21 / 7 | cash |  |
| Breezy | 2026-11-09T15:39 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-09T15:39 | 6 / 22 / 2 | COIN 79% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.86 | 15.86 | 19 | 68.4 | 15.37 | 3.25 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 110.34 | 10.34 | 0 | — | 11.62 | 3.86 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.31 | 10.31 | 30 | 26.7 | 18.11 | 2.86 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.46 | 2.46 | 30 | 43.3 | 0.50 | 0.24 | -9.64 | 31 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.34 | 1.34 | 0 | — | 4.80 | 1.39 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.03 | 1.03 | 122 | 35.2 | 9.37 | 3.83 | -2.27 | 89 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.64 | -0.36 | 7 | 42.9 | -2.40 | 0.02 | -18.69 | 8 |
| 10 | Agent (rotation) | meta | 97.21 | -2.79 | 176 | 27.8 | -4.64 | -2.16 | -10.70 | 179 |
| 11 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 13 | Gap and go | momentum | 97.02 | -2.98 | 174 | 27.6 | 1.79 | 0.64 | -9.06 | 240 |
| 14 | Hold SPY | benchmark | 96.24 | -3.76 | 0 | — | -2.33 | -0.71 | -6.18 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 93.75 | -6.25 | 0 | — | -4.45 | -1.24 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.91 | -7.09 | 108 | 23.1 | -13.39 | -4.98 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.41 | -7.59 | 0 | — | -5.11 | -1.40 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Copy: Insider buying | copy | 89.78 | -10.22 | 40 | 37.5 | -10.79 | -2.43 | -16.06 | 63 |
| 22 | Opening range 30m | breakout | 89.70 | -10.30 | 375 | 32.5 | -14.77 | -4.76 | -15.99 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.08 | -2.81 | -14.15 | 79 |
| 24 | Agent | meta | 87.81 | -12.19 | 156 | 35.9 | -13.14 | -6.83 | -13.75 | 200 |
| 25 | Hold BTC | benchmark | 87.47 | -12.53 | 1 | 0.0 | -4.98 | -0.49 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.55 | -13.45 | 15 | 20.0 | -9.26 | -1.37 | -16.76 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.49 | -14.51 | 167 | 26.9 | -11.51 | -2.09 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.55 | -15.45 | 74 | 31.1 | -16.05 | -4.58 | -18.49 | 92 |
| 29 | Stochastic reversion · 1h | reversion | 84.09 | -15.91 | 278 | 48.2 | -22.02 | -3.10 | -27.15 | 387 |
| 30 | Donchian 55/20 · 1h | breakout | 83.96 | -16.04 | 71 | 14.1 | -15.40 | -3.20 | -21.54 | 103 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 83.42 | -16.58 | 2 | 0.0 | -9.16 | -1.02 | -24.16 | 1 |
| 32 | Opening range 15m | breakout | 83.12 | -16.88 | 465 | 30.5 | -19.34 | -5.59 | -20.97 | 735 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 34 | Connors RSI(2) · 1h | reversion | 80.99 | -19.01 | 205 | 40.0 | -19.10 | -6.38 | -19.64 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -24.39 | -5.22 | -25.33 | 180 |
| 36 | MFI reversion · 1h | reversion | 79.41 | -20.59 | 345 | 33.6 | -16.89 | -2.14 | -21.23 | 162 |
| 37 | Heikin-Ashi · 1h | trend | 79.33 | -20.67 | 394 | 23.1 | -38.74 | -7.41 | -41.75 | 669 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -38.35 | -2.57 | -44.05 | 25 |
| 39 | CCI reversion · 1h | reversion | 78.73 | -21.27 | 307 | 43.6 | -24.68 | -3.80 | -30.29 | 461 |
| 40 | ADX DI cross · 1h | trend | 78.59 | -21.41 | 179 | 18.4 | -24.97 | -4.13 | -28.65 | 269 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.22 | -22.78 | 170 | 22.9 | -21.88 | -4.48 | -27.59 | 242 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.33 | -4.06 | -33.04 | 372 |
| 44 | Williams %R · 1h | reversion | 75.43 | -24.57 | 328 | 46.3 | -32.26 | -4.83 | -36.07 | 542 |
| 45 | MACD cross · 1h | trend | 75.00 | -25.00 | 349 | 22.6 | -32.45 | -5.41 | -39.38 | 488 |
| 46 | Z-score reversion · 1h | reversion | 74.75 | -25.25 | 172 | 34.9 | -21.32 | -3.11 | -27.66 | 227 |
| 47 | EMA 20/50 cross · 1h | trend | 74.53 | -25.47 | 102 | 10.8 | -22.45 | -3.79 | -31.52 | 127 |
| 48 | MACD zero-line · 1h | trend | 74.48 | -25.52 | 157 | 16.6 | -24.84 | -5.12 | -29.17 | 209 |
| 49 | Supertrend · 1h | trend | 72.91 | -27.09 | 167 | 13.2 | -31.27 | -5.81 | -34.46 | 232 |
| 50 | RSI momentum · 1h | momentum | 72.84 | -27.16 | 159 | 12.6 | -25.65 | -4.46 | -33.26 | 213 |
| 51 | Triple EMA stack · 1h | trend | 72.75 | -27.25 | 142 | 14.8 | -26.85 | -4.88 | -34.51 | 202 |
| 52 | OBV trend · 1h | momentum | 71.86 | -28.14 | 274 | 18.2 | -28.76 | -5.90 | -34.16 | 277 |
| 53 | ROC + volume · 1h | momentum | 70.81 | -29.18 | 349 | 25.5 | -37.81 | -7.23 | -39.67 | 380 |
| 54 | Daily: Momentum burst | daily | 70.70 | -29.30 | 26 | 11.5 | -38.33 | -5.38 | -39.17 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.19 | -29.81 | 142 | 19.7 | -31.23 | -5.82 | -35.56 | 209 |
| 56 | Agent (ML meta-label) | meta | 68.24 | -31.76 | 1561 | 23.3 | -12.54 | -1.79 | -22.82 | 334 |
| 57 | RSI(14) reversion · 1h | reversion | 68.03 | -31.97 | 155 | 28.4 | -27.56 | -4.14 | -32.51 | 233 |
| 58 | VWAP momentum · 1h | momentum | 67.56 | -32.44 | 801 | 21.6 | -52.85 | -11.41 | -54.01 | 1244 |
| 59 | EMA 9/21 cross · 1h | trend | 65.79 | -34.21 | 246 | 9.8 | -39.91 | -7.78 | -41.00 | 328 |
| 60 | Candlestick reversal · 1h | reversion | 65.64 | -34.36 | 430 | 28.1 | -38.49 | -6.99 | -39.90 | 594 |
| 61 | Max aggression: 1-day momentum | meta | 65.59 | -34.41 | 27 | 25.9 | -34.29 | -1.89 | -57.50 | 42 |
| 62 | Three white soldiers | momentum | 62.64 | -37.36 | 488 | 15.0 | -48.65 | -22.42 | -48.79 | 646 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.62 | -98.99 | 5291 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.06 | -26.06 | -80.25 | 1430 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.28 | -46.18 | -93.38 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -32.06 | -89.52 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.84 | -39.83 | -90.95 | 2307 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.04 | -31.74 | -90.04 | 2180 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -54.19 | -97.75 | 3478 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -57.12 | -96.33 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.50 | -32.19 | -93.59 | 2399 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.33 | -35.07 | -82.44 | 1673 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.52 | -55.40 | -99.53 | 5985 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -43.54 | -92.63 | 2602 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -37.40 | -95.57 | 3392 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.00 | -99.80 | 6179 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.92 | -43.92 | -91.93 | 2271 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.84 | -24.83 | -76.24 | 1592 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.00 | -97.72 | 3497 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.82 | -61.91 | -98.85 | 4897 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.87 | -27.67 | -69.47 | 1209 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -55.00 | -94.69 | 2741 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.00 | -37.14 | -85.12 | 1769 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.32 | -99.66 | 6388 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.56 | -32.07 | -89.76 | 2299 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.34 | -20.03 | -78.55 | 1757 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.58 | -36.10 | -90.78 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.64 | -96.82 | 3904 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -57.37 | -89.54 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.09 | -29.07 | -66.26 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.73 | -23.44 | -72.24 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.46 | -19.08 | -79.73 | 1695 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.29 | -49.93 | -97.34 | 4329 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -105.45 | -99.93 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T15:30 | Agent (ML meta-label) | buy | LABU | 1.69 | — | following MFI reversion |
| 2026-11-09T15:30 | Agent (ML meta-label) | buy | AAPL | 4.53 | — | entry |
| 2026-11-09T15:30 | Agent (ML meta-label) | sell | AMD | 5.99 | 0.96 | selected signal exited |
| 2026-11-09T15:30 | CCI reversion · 1h | buy | TNA | 1.54 | — | entry |
| 2026-11-09T15:30 | CCI reversion · 1h | buy | LABU | 4.13 | — | entry |
| 2026-11-09T15:30 | CCI reversion · 1h | sell | AMD | 5.67 | 0.55 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | buy | XRP-USD | 9.42 | — | entry |
| 2026-11-09T15:30 | Williams %R · 1h | buy | UPRO | 9.42 | — | entry signal |
| 2026-11-09T15:30 | Williams %R · 1h | buy | SPY | 9.42 | — | entry signal |
| 2026-11-09T15:30 | Williams %R · 1h | buy | SOL-USD | 8.06 | — | rebalance up |
| 2026-11-09T15:30 | Williams %R · 1h | buy | MSFT | 8.31 | — | rebalance up |
| 2026-11-09T15:30 | Williams %R · 1h | buy | ETH-USD | 5.12 | — | rebalance up |
| 2026-11-09T15:30 | Williams %R · 1h | buy | BTC-USD | 5.10 | — | rebalance up |
| 2026-11-09T15:30 | Williams %R · 1h | sell | TSLA | 1.77 | 0.03 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | TQQQ | 7.03 | 0.50 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | TNA | 4.66 | 0.08 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | TECL | 6.94 | 0.41 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | SOXL | 7.57 | 1.04 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | QQQ | 6.68 | 0.15 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | PLTR | 4.40 | 0.10 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | META | 6.73 | 0.20 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | LABU | 7.24 | 0.71 | exit signal |
| 2026-11-09T15:30 | Williams %R · 1h | sell | IWM | 4.60 | 0.07 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | buy | XRP-USD | 18.72 | — | rebalance up |
| 2026-11-09T15:30 | Stochastic reversion · 1h | buy | MSTR | 16.13 | — | rebalance up |
| 2026-11-09T15:30 | Stochastic reversion · 1h | buy | COIN | 16.03 | — | rebalance up |
| 2026-11-09T15:30 | Stochastic reversion · 1h | buy | BITX | 16.19 | — | rebalance up |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | UPRO | 5.05 | 0.19 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | TSLA | 5.35 | 0.39 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | TQQQ | 5.17 | 0.31 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | TNA | 5.47 | 0.47 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | TECL | 5.19 | 0.31 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | SPY | 4.10 | 0.05 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | SOXL | 5.61 | 0.77 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | QQQ | 2.26 | 0.04 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | LABU | 5.47 | 0.35 | exit signal |
| 2026-11-09T15:30 | Stochastic reversion · 1h | sell | IWM | 5.17 | 0.14 | exit signal |
| 2026-11-09T15:30 | Z-score reversion · 1h | sell | IWM | 4.40 | 0.08 | exit signal |
| 2026-11-09T15:30 | Z-score reversion · 1h | sell | AMD | 4.76 | 0.53 | exit signal |
| 2026-11-09T15:30 | Bollinger reversion · 1h | sell | UPRO | 9.40 | 0.29 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 15:39:05.000129+00:00 -> 2026-11-09 15:49:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 15:39:05.000129+00:00 -> 2026-11-09 15:49:05.000129+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 15:39:05.000129+00:00 -> 2026-11-09 15:49:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
