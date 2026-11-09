# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T17:36:05.000110+00:00 · 53640 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.39 (-12.61%)

Closed trades 159, win rate 35.8%, fees £4.91, max drawdown -13.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.41 | -0.19 |

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

Today: 23799 decisions in 2784 calls, $0.3050 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T17:36 | 5 / 17 / 8 | cash |  |
| Breezy | 2026-11-09T17:36 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-09T17:36 | 9 / 19 / 2 | COIN 64% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.20 | 17.20 | 19 | 68.4 | 16.78 | 3.44 | -4.91 | 27 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.58 | 11.58 | 30 | 26.7 | 19.56 | 2.99 | -8.66 | 44 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 111.50 | 11.50 | 0 | — | 12.72 | 4.35 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.65 | 3.65 | 30 | 43.3 | 3.37 | 0.91 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.23 | 1.23 | 123 | 35.0 | 9.57 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.03 | 1.03 | 0 | — | 4.55 | 1.33 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.79 | 0.79 | 7 | 42.9 | -1.20 | 0.16 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent (rotation) | meta | 97.87 | -2.13 | 176 | 27.8 | -2.72 | -1.14 | -9.58 | 161 |
| 11 | Gap and go | momentum | 97.78 | -2.22 | 179 | 29.1 | 2.67 | 0.87 | -9.06 | 241 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.28 | -3.14 | -12.28 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.59 | -3.41 | 0 | — | -1.93 | -0.54 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.21 | -5.79 | 0 | — | -3.92 | -1.05 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.74 | -7.26 | 108 | 23.1 | -13.52 | -5.05 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.64 | -7.36 | 0 | — | -4.45 | -1.20 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.23 | -9.77 | 376 | 32.4 | -14.43 | -4.61 | -15.99 | 598 |
| 22 | Copy: Insider buying | copy | 89.28 | -10.72 | 40 | 37.5 | -11.46 | -2.65 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.70 | -2.68 | -14.15 | 77 |
| 24 | Agent | meta | 87.39 | -12.61 | 159 | 35.8 | -13.23 | -6.88 | -13.69 | 200 |
| 25 | Hold BTC | benchmark | 86.94 | -13.06 | 1 | 0.0 | -5.15 | -0.58 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.20 | -13.80 | 15 | 20.0 | -10.01 | -1.42 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.74 | -14.26 | 167 | 26.9 | -11.20 | -2.03 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.88 | -4.52 | -18.49 | 92 |
| 29 | Donchian 55/20 · 1h | breakout | 83.64 | -16.36 | 71 | 14.1 | -16.42 | -3.45 | -21.91 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.62 | -16.38 | 2 | 0.0 | -8.80 | -0.98 | -24.16 | 1 |
| 31 | Opening range 15m | breakout | 83.47 | -16.53 | 465 | 30.5 | -19.00 | -5.43 | -20.97 | 735 |
| 32 | Stochastic reversion · 1h | reversion | 83.28 | -16.72 | 279 | 48.4 | -23.63 | -3.48 | -28.00 | 386 |
| 33 | Keltner breakout · 1h | breakout | 81.56 | -18.44 | 107 | 23.4 | -23.63 | -4.98 | -25.20 | 182 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.68 | -19.32 | 205 | 40.0 | -19.40 | -6.50 | -19.64 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.73 | -20.27 | 394 | 23.1 | -38.46 | -7.22 | -41.79 | 682 |
| 37 | MFI reversion · 1h | reversion | 79.39 | -20.61 | 347 | 34.0 | -17.52 | -2.24 | -21.48 | 164 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.26 | -2.64 | -44.97 | 25 |
| 39 | ADX DI cross · 1h | trend | 79.17 | -20.83 | 179 | 18.4 | -25.50 | -4.31 | -28.65 | 272 |
| 40 | CCI reversion · 1h | reversion | 78.90 | -21.10 | 309 | 44.0 | -24.53 | -3.76 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.06 | -22.94 | 170 | 22.9 | -22.36 | -4.61 | -27.77 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.54 | -4.09 | -33.23 | 373 |
| 44 | Williams %R · 1h | reversion | 75.25 | -24.75 | 335 | 46.9 | -34.06 | -5.38 | -37.43 | 543 |
| 45 | MACD cross · 1h | trend | 75.18 | -24.82 | 349 | 22.6 | -32.18 | -5.14 | -39.64 | 486 |
| 46 | Z-score reversion · 1h | reversion | 75.12 | -24.88 | 176 | 36.4 | -20.32 | -2.92 | -27.66 | 228 |
| 47 | MACD zero-line · 1h | trend | 74.45 | -25.55 | 157 | 16.6 | -24.85 | -5.12 | -29.19 | 210 |
| 48 | EMA 20/50 cross · 1h | trend | 74.25 | -25.75 | 102 | 10.8 | -23.08 | -4.11 | -31.15 | 128 |
| 49 | Supertrend · 1h | trend | 73.26 | -26.74 | 167 | 13.2 | -31.02 | -5.75 | -34.46 | 236 |
| 50 | RSI momentum · 1h | momentum | 73.00 | -27.00 | 159 | 12.6 | -24.65 | -4.12 | -33.29 | 215 |
| 51 | Triple EMA stack · 1h | trend | 72.53 | -27.47 | 143 | 14.7 | -26.15 | -4.59 | -34.73 | 202 |
| 52 | OBV trend · 1h | momentum | 71.86 | -28.14 | 274 | 18.2 | -28.91 | -5.98 | -34.27 | 278 |
| 53 | ROC + volume · 1h | momentum | 71.56 | -28.44 | 349 | 25.5 | -36.75 | -6.96 | -39.35 | 386 |
| 54 | Daily: Momentum burst | daily | 70.44 | -29.56 | 26 | 11.5 | -38.55 | -5.42 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.37 | -29.62 | 142 | 19.7 | -31.63 | -5.91 | -35.64 | 209 |
| 56 | RSI(14) reversion · 1h | reversion | 68.25 | -31.75 | 160 | 30.6 | -30.11 | -4.50 | -33.56 | 245 |
| 57 | Agent (ML meta-label) | meta | 67.95 | -32.05 | 1587 | 23.8 | -5.68 | -0.89 | -17.99 | 344 |
| 58 | Max aggression: 1-day momentum | meta | 67.69 | -32.31 | 27 | 25.9 | -32.14 | -1.67 | -57.50 | 42 |
| 59 | VWAP momentum · 1h | momentum | 67.64 | -32.36 | 804 | 21.8 | -52.04 | -11.17 | -53.64 | 1237 |
| 60 | EMA 9/21 cross · 1h | trend | 65.60 | -34.40 | 247 | 9.7 | -40.17 | -7.81 | -41.71 | 331 |
| 61 | Candlestick reversal · 1h | reversion | 65.27 | -34.73 | 432 | 28.2 | -39.38 | -7.26 | -40.34 | 596 |
| 62 | Three white soldiers | momentum | 62.39 | -37.61 | 492 | 15.0 | -48.64 | -22.61 | -48.65 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.67 | -98.99 | 5273 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.96 | -26.33 | -80.06 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -46.44 | -93.30 | 2505 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.43 | -32.37 | -89.47 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.69 | -40.09 | -90.76 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.97 | -31.50 | -89.98 | 2184 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -54.83 | -97.70 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.50 | -96.30 | 3404 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -32.69 | -93.62 | 2408 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -34.58 | -82.30 | 1671 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.79 | -99.53 | 5985 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.34 | -43.03 | -92.53 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.52 | -37.27 | -95.52 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.36 | -99.80 | 6170 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -44.11 | -91.86 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.39 | -24.80 | -75.87 | 1590 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.87 | -97.68 | 3502 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.43 | -98.84 | 4885 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.75 | -27.49 | -69.44 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.14 | -94.59 | 2733 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -37.04 | -85.02 | 1772 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.78 | -99.66 | 6383 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.67 | -32.71 | -89.69 | 2280 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.50 | -20.16 | -78.50 | 1764 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.59 | -36.37 | -90.74 | 2223 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.76 | -52.66 | -96.80 | 3880 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -57.98 | -89.40 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.01 | -29.05 | -66.26 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.35 | -23.19 | -72.00 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.72 | -19.11 | -79.77 | 1695 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -49.97 | -97.33 | 4325 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -106.90 | -99.93 | 8277 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T17:35 | Agent (ML meta-label) | buy | SPY | 3.50 | — | rebalance up |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | LABU | 5.81 | 0.03 | selected signal exited |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | AMD | 5.23 | 0.01 | selected signal exited |
| 2026-11-09T17:35 | Agent (ML meta-label) | sell | AAPL | 5.21 | -0.01 | selected signal exited |
| 2026-11-09T17:30 | Agent (ML meta-label) | buy | SPY | 2.68 | — | entry |
| 2026-11-09T17:30 | Agent (ML meta-label) | buy | BITX | 4.85 | — | entry |
| 2026-11-09T17:30 | MFI reversion · 1h | buy | UPRO | 3.56 | — | rebalance up |
| 2026-11-09T17:30 | MFI reversion · 1h | buy | NVDA | 4.43 | — | rebalance up |
| 2026-11-09T17:30 | MFI reversion · 1h | sell | PLTR | 7.99 | 0.26 | exit signal |
| 2026-11-09T17:30 | CCI reversion · 1h | sell | PLTR | 5.38 | 0.26 | exit signal |
| 2026-11-09T17:30 | Williams %R · 1h | buy | NVDA | 18.82 | — | entry signal |
| 2026-11-09T17:30 | Williams %R · 1h | buy | BITX | 18.82 | — | entry signal |
| 2026-11-09T17:30 | Williams %R · 1h | sell | MSFT | 18.98 | 0.07 | exit signal |
| 2026-11-09T17:30 | Stochastic reversion · 1h | buy | ETHU | 20.84 | — | entry signal |
| 2026-11-09T17:30 | Z-score reversion · 1h | buy | NVDA | 6.26 | — | entry signal |
| 2026-11-09T17:30 | Z-score reversion · 1h | buy | ETHU | 6.26 | — | entry signal |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | buy | UPRO | 4.01 | — | rebalance up |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | buy | TQQQ | 3.72 | — | rebalance up |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | buy | TECL | 4.17 | — | rebalance up |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | buy | SOXL | 3.52 | — | rebalance up |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | buy | NVDA | 8.52 | — | entry signal |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | sell | SPY | 4.49 | 0.06 | exit signal |
| 2026-11-09T17:30 | RSI(14) reversion · 1h | sell | QQQ | 4.54 | 0.11 | exit signal |
| 2026-11-09T17:30 | Keltner breakout · 1h | buy | TNA | 20.17 | — | entry signal |
| 2026-11-09T17:30 | VWAP momentum · 1h | buy | QQQ | 2.36 | — | entry signal |
| 2026-11-09T17:30 | VWAP momentum · 1h | buy | MSFT | 3.22 | — | entry signal |
| 2026-11-09T17:30 | MACD zero-line · 1h | buy | AMD | 18.60 | — | entry signal |
| 2026-11-09T17:30 | Triple EMA stack · 1h | sell | SQQQ | 17.05 | -0.64 | exit signal |
| 2026-11-09T17:30 | EMA 9/21 cross · 1h | buy | IWM | 6.56 | — | entry signal |
| 2026-11-09T17:30 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.56 | — | entry |
| 2026-11-09T17:30 | EMA 9/21 cross · 1h | sell | SQQQ | 9.22 | -0.40 | exit signal |
| 2026-11-09T17:30 | EMA 9/21 cross · 1h | sell | META | 4.10 | 0.02 | rebalance down |
| 2026-11-09T17:25 | Agent (ML meta-label) | sell | SPY | 5.23 | -0.00 | selected signal exited |
| 2026-11-09T17:20 | Agent (ML meta-label) | buy | AMD | 5.22 | — | entry |
| 2026-11-09T17:20 | Agent (ML meta-label) | buy | AAPL | 5.22 | — | entry |
| 2026-11-09T17:20 | Agent (ML meta-label) | sell | TECL | 3.95 | 0.00 | selected signal exited |
| 2026-11-09T17:15 | Agent (ML meta-label) | buy | LABU | 5.78 | — | following MFI reversion |
| 2026-11-09T17:15 | Agent (ML meta-label) | sell | BITX | 1.10 | -0.00 | selected signal exited |
| 2026-11-09T17:15 | Agent (ML meta-label) | sell | AMD | 5.72 | 0.00 | selected signal exited |
| 2026-11-09T17:15 | Agent | sell | TSLA | 17.45 | -0.04 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 17:36:05.000110+00:00 -> 2026-11-09 17:46:05.000110+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 17:36:05.000110+00:00 -> 2026-11-09 17:46:05.000110+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 17:36:05.000110+00:00 -> 2026-11-09 17:46:05.000110+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
