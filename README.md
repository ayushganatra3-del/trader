# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T20:05:05.000117+00:00 · 53752 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.16 (-12.84%)

Closed trades 160, win rate 35.6%, fees £4.96, max drawdown -13.29%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 34.78 | -0.14 |
| SQQQ | 17.47 | +0.04 |
| TSLA | 17.57 | +0.08 |

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

Today: 33933 decisions in 3120 calls, $0.4232 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T20:05 | 3 / 17 / 10 | TNA 14% |  |
| Breezy | 2026-11-09T20:05 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-09T20:05 | 6 / 21 / 3 | COIN 68% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.66 | 17.66 | 19 | 68.4 | 18.83 | 3.81 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.71 | 12.71 | 0 | — | 14.17 | 4.81 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.03 | 12.03 | 30 | 26.7 | 20.08 | 3.03 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.06 | 4.06 | 30 | 43.3 | 3.81 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.77 | 1.77 | 123 | 35.0 | 10.19 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 101.55 | 1.55 | 0 | — | 5.12 | 1.46 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.19 | 1.19 | 7 | 42.9 | -0.77 | 0.21 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.79 | -1.21 | 181 | 29.8 | 3.85 | 1.14 | -9.06 | 240 |
| 11 | Agent (rotation) | meta | 98.29 | -1.71 | 176 | 27.8 | -3.36 | -1.32 | -10.59 | 169 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.65 | -3.28 | -12.65 | 151 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.71 | -3.29 | 0 | — | -1.32 | -0.39 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.69 | -5.31 | 0 | — | -3.79 | -0.98 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.30 | -6.25 | -7.78 | 21 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 92.83 | -7.17 | 0 | — | -3.95 | -1.04 | -10.64 | 1 |
| 19 | Trend pullback · 1h | trend | 92.78 | -7.22 | 108 | 23.1 | -13.56 | -5.07 | -17.96 | 79 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.66 | -9.34 | 378 | 32.3 | -13.16 | -4.16 | -15.24 | 595 |
| 22 | Copy: Insider buying | copy | 89.33 | -10.67 | 40 | 37.5 | -11.16 | -2.55 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.25 | -3.34 | -14.68 | 81 |
| 24 | Agent | meta | 87.16 | -12.84 | 160 | 35.6 | -13.44 | -6.99 | -13.96 | 205 |
| 25 | Hold BTC | benchmark | 87.00 | -13.01 | 1 | 0.0 | -5.01 | -0.56 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.07 | -13.93 | 15 | 20.0 | -10.35 | -1.58 | -17.30 | 14 |
| 27 | Parabolic SAR · 1h | trend | 86.00 | -14.00 | 167 | 26.9 | -10.95 | -1.98 | -21.29 | 227 |
| 28 | Agent (aggressive) | meta | 84.16 | -15.84 | 75 | 32.0 | -16.30 | -4.67 | -18.49 | 94 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.08 | -15.92 | 2 | 0.0 | -7.53 | -0.82 | -24.16 | 1 |
| 30 | Opening range 15m | breakout | 83.79 | -16.21 | 466 | 30.5 | -18.17 | -5.14 | -19.91 | 728 |
| 31 | Stochastic reversion · 1h | reversion | 83.63 | -16.37 | 279 | 48.4 | -23.70 | -3.49 | -28.11 | 387 |
| 32 | Donchian 55/20 · 1h | breakout | 83.53 | -16.47 | 71 | 14.1 | -18.05 | -3.98 | -22.33 | 103 |
| 33 | Keltner breakout · 1h | breakout | 82.35 | -17.65 | 107 | 23.4 | -21.83 | -4.40 | -25.12 | 173 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.82 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.56 | -19.44 | 205 | 40.0 | -19.71 | -6.62 | -19.87 | 124 |
| 36 | Heikin-Ashi · 1h | trend | 80.02 | -19.98 | 400 | 22.8 | -39.60 | -7.34 | -43.08 | 674 |
| 37 | ADX DI cross · 1h | trend | 79.66 | -20.34 | 179 | 18.4 | -22.12 | -3.81 | -28.34 | 273 |
| 38 | MFI reversion · 1h | reversion | 79.37 | -20.63 | 349 | 34.1 | -16.20 | -2.07 | -21.23 | 167 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.59 | -2.66 | -45.48 | 25 |
| 40 | CCI reversion · 1h | reversion | 79.11 | -20.89 | 314 | 44.9 | -24.14 | -3.69 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -29.07 | -8.38 | -29.30 | 116 |
| 42 | Bollinger breakout · 1h | breakout | 76.88 | -23.12 | 170 | 22.9 | -22.57 | -4.74 | -27.87 | 240 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.17 | -4.00 | -32.89 | 373 |
| 44 | MACD cross · 1h | trend | 75.40 | -24.60 | 349 | 22.6 | -32.87 | -5.38 | -39.46 | 485 |
| 45 | Z-score reversion · 1h | reversion | 75.22 | -24.78 | 176 | 36.4 | -20.18 | -2.88 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 75.16 | -24.84 | 336 | 46.7 | -36.04 | -5.89 | -39.29 | 541 |
| 47 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 157 | 16.6 | -24.48 | -5.02 | -29.19 | 213 |
| 48 | EMA 20/50 cross · 1h | trend | 74.20 | -25.80 | 102 | 10.8 | -24.40 | -4.40 | -32.57 | 127 |
| 49 | Supertrend · 1h | trend | 73.61 | -26.39 | 167 | 13.2 | -29.01 | -5.01 | -34.92 | 225 |
| 50 | RSI momentum · 1h | momentum | 73.33 | -26.67 | 159 | 12.6 | -23.27 | -3.72 | -33.01 | 217 |
| 51 | Triple EMA stack · 1h | trend | 72.71 | -27.29 | 143 | 14.7 | -25.94 | -4.53 | -34.87 | 202 |
| 52 | ROC + volume · 1h | momentum | 71.99 | -28.01 | 349 | 25.5 | -35.94 | -6.74 | -38.89 | 385 |
| 53 | OBV trend · 1h | momentum | 71.93 | -28.07 | 274 | 18.2 | -26.75 | -4.95 | -34.09 | 275 |
| 54 | Donchian 20/10 · 1h | breakout | 70.60 | -29.41 | 142 | 19.7 | -29.70 | -5.50 | -35.64 | 206 |
| 55 | Daily: Momentum burst | daily | 70.35 | -29.65 | 26 | 11.5 | -39.34 | -5.69 | -39.56 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.29 | -31.71 | 160 | 30.6 | -30.94 | -4.62 | -34.37 | 246 |
| 57 | Agent (ML meta-label) | meta | 68.01 | -31.99 | 1626 | 24.1 | -7.72 | -1.07 | -18.75 | 338 |
| 58 | Max aggression: 1-day momentum | meta | 67.85 | -32.15 | 27 | 25.9 | -31.96 | -1.65 | -57.50 | 42 |
| 59 | VWAP momentum · 1h | momentum | 67.84 | -32.16 | 810 | 21.6 | -51.96 | -11.21 | -53.55 | 1231 |
| 60 | EMA 9/21 cross · 1h | trend | 65.84 | -34.16 | 247 | 9.7 | -38.10 | -7.56 | -40.15 | 333 |
| 61 | Candlestick reversal · 1h | reversion | 65.15 | -34.85 | 434 | 28.6 | -37.74 | -6.84 | -38.58 | 592 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.59 | -22.77 | -48.59 | 645 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -45.87 | -98.98 | 5257 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.68 | -26.39 | -79.78 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.17 | -46.17 | -93.29 | 2518 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.00 | -32.15 | -89.09 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.59 | -39.90 | -90.69 | 2319 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.05 | -31.66 | -90.11 | 2191 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -54.46 | -97.66 | 3459 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.92 | -96.30 | 3420 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.65 | -32.38 | -93.71 | 2427 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.93 | -34.04 | -82.22 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -56.07 | -99.53 | 5959 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -43.08 | -92.44 | 2610 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.48 | -37.49 | -95.50 | 3403 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.18 | -99.79 | 6151 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -43.99 | -91.67 | 2256 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.40 | -24.81 | -75.70 | 1597 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -61.85 | -97.66 | 3519 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.60 | -98.84 | 4881 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.47 | -26.79 | -69.32 | 1219 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.48 | -55.12 | -94.51 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -37.74 | -84.63 | 1780 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.02 | -99.65 | 6365 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.57 | -32.55 | -89.67 | 2271 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.36 | -20.16 | -78.37 | 1743 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.49 | -36.86 | -90.59 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.59 | -96.81 | 3879 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -58.90 | -89.31 | 2141 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.24 | -29.23 | -66.41 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.12 | -22.82 | -71.93 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.65 | -19.16 | -79.65 | 1680 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.92 | -97.32 | 4309 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.89 | -99.93 | 8301 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T20:05 | Agent (ML meta-label) | buy | BITX | 2.31 | — | entry |
| 2026-11-09T20:05 | Agent (ML meta-label) | buy | AAPL | 5.23 | — | entry |
| 2026-11-09T20:05 | Agent (ML meta-label) | sell | META | 2.25 | -0.00 | selected signal exited |
| 2026-11-09T20:05 | Agent (ML meta-label) | sell | AMZN | 5.29 | 0.18 | selected signal exited |
| 2026-11-09T20:00 | Agent (ML meta-label) | buy | SOXL | 5.23 | — | entry |
| 2026-11-09T20:00 | Agent (ML meta-label) | sell | BITX | 5.23 | 0.00 | selected signal exited |
| 2026-11-09T19:55 | Agent (ML meta-label) | buy | META | 2.25 | — | entry |
| 2026-11-09T19:55 | Agent (ML meta-label) | buy | LABU | 5.23 | — | following MFI reversion |
| 2026-11-09T19:55 | Agent (ML meta-label) | buy | BITX | 5.23 | — | entry |
| 2026-11-09T19:55 | Stochastic reversion · 1h | buy | SQQQ | 4.19 | — | rebalance up |
| 2026-11-09T19:55 | Stochastic reversion · 1h | sell | MSTR | 4.19 | 0.00 | rebalance down |
| 2026-11-09T19:50 | Agent (ML meta-label) | buy | SOL-USD | 3.89 | — | rebalance up |
| 2026-11-09T19:50 | Agent (ML meta-label) | buy | ETH-USD | 3.69 | — | rebalance up |
| 2026-11-09T19:50 | Agent (ML meta-label) | buy | DOGE-USD | 3.84 | — | rebalance up |
| 2026-11-09T19:50 | Agent (ML meta-label) | sell | SOXL | 6.23 | 0.07 | selected signal exited |
| 2026-11-09T19:50 | Agent (ML meta-label) | sell | META | 4.93 | -0.00 | selected signal exited |
| 2026-11-09T19:50 | Agent (ML meta-label) | sell | LABU | 4.91 | -0.02 | selected signal exited |
| 2026-11-09T19:50 | Agent (ML meta-label) | sell | BITX | 4.11 | -0.02 | selected signal exited |
| 2026-11-09T19:45 | Agent (ML meta-label) | sell | TSLA | 3.96 | -0.01 | selected signal exited |
| 2026-11-09T19:45 | Agent | buy | SQQQ | 17.43 | — | following RSI(14) reversion |
| 2026-11-09T19:40 | Agent (ML meta-label) | buy | TSLA | 3.97 | — | following VWAP momentum |
| 2026-11-09T19:40 | Agent (ML meta-label) | buy | META | 4.94 | — | entry |
| 2026-11-09T19:40 | Agent (ML meta-label) | buy | LABU | 4.94 | — | following MFI reversion |
| 2026-11-09T19:40 | Agent (ML meta-label) | buy | BITX | 4.13 | — | entry |
| 2026-11-09T19:40 | Agent (ML meta-label) | sell | AAPL | 6.17 | 0.00 | selected signal exited |
| 2026-11-09T19:40 | Agent (aggressive) | buy | COIN | 42.16 | — | following Donchian 20/10, Keltner breakout |
| 2026-11-09T19:40 | Agent | buy | COIN | 34.92 | — | following Donchian 20/10, Keltner breakout |
| 2026-11-09T19:40 | Agent | sell | SQQQ | 17.21 | -0.40 | selected signal exited |
| 2026-11-09T19:40 | Stochastic reversion · 1h | buy | SQQQ | 4.27 | — | rebalance up |
| 2026-11-09T19:40 | Stochastic reversion · 1h | sell | ETHU | 4.27 | 0.04 | rebalance down |
| 2026-11-09T19:35 | Agent (ML meta-label) | buy | SOXL | 4.41 | — | rebalance up |
| 2026-11-09T19:35 | Agent (ML meta-label) | buy | AAPL | 6.16 | — | entry |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | TQQQ | 4.84 | 0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | QQQ | 4.52 | -0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | LABU | 4.77 | 0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent (ML meta-label) | sell | BITX | 2.61 | -0.01 | selected signal exited |
| 2026-11-09T19:35 | Agent | buy | TSLA | 17.49 | — | following VWAP momentum |
| 2026-11-09T19:30 | Agent (ML meta-label) | buy | TQQQ | 4.84 | — | entry |
| 2026-11-09T19:30 | Agent (ML meta-label) | sell | UPRO | 5.24 | 0.10 | selected signal exited |
| 2026-11-09T19:30 | Agent (ML meta-label) | sell | META | 4.24 | 0.00 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 20:05:05.000117+00:00 -> 2026-11-09 20:15:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 20:05:05.000117+00:00 -> 2026-11-09 20:15:05.000117+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 20:05:05.000117+00:00 -> 2026-11-09 20:15:05.000117+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
