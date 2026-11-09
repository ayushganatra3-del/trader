# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T17:06:05.000135+00:00 · 53611 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 158, win rate 36.1%, fees £4.90, max drawdown -12.91%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.53 | -0.08 |

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

Today: 21180 decisions in 2697 calls, $0.2744 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T17:06 | 9 / 16 / 6 | NVDA 15% |  |
| Breezy | 2026-11-09T17:06 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-11-09T17:06 | 8 / 20 / 3 | COIN 74% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.83 | 16.83 | 19 | 68.4 | 16.27 | 3.38 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.34 | 11.34 | 0 | — | 12.48 | 4.24 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.23 | 11.23 | 30 | 26.7 | 19.04 | 2.95 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.32 | 3.32 | 30 | 43.3 | 2.91 | 0.81 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.23 | 1.23 | 0 | — | 4.63 | 1.35 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.21 | 1.21 | 123 | 35.0 | 9.46 | 3.83 | -2.27 | 89 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.47 | 0.47 | 7 | 42.9 | -1.63 | 0.11 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent (rotation) | meta | 97.72 | -2.28 | 176 | 27.8 | -3.55 | -1.52 | -10.11 | 161 |
| 11 | Gap and go | momentum | 97.60 | -2.40 | 179 | 29.1 | 2.35 | 0.79 | -9.06 | 241 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.54 | -3.46 | 0 | — | -2.18 | -0.61 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.25 | -5.75 | 0 | — | -4.00 | -1.08 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.73 | -7.27 | 108 | 23.1 | -13.57 | -5.08 | -17.86 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.55 | -7.45 | 0 | — | -4.72 | -1.29 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.11 | -9.89 | 376 | 32.4 | -14.65 | -4.69 | -16.08 | 598 |
| 22 | Copy: Insider buying | copy | 89.72 | -10.28 | 40 | 37.5 | -10.99 | -2.49 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.96 | -2.76 | -14.15 | 78 |
| 24 | Agent | meta | 87.54 | -12.46 | 158 | 36.1 | -13.11 | -6.80 | -13.58 | 199 |
| 25 | Hold BTC | benchmark | 87.18 | -12.82 | 1 | 0.0 | -5.10 | -0.56 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.35 | -13.65 | 15 | 20.0 | -9.96 | -1.40 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.66 | -14.34 | 167 | 26.9 | -11.38 | -2.06 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.88 | -4.52 | -18.49 | 92 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.02 | -15.98 | 2 | 0.0 | -8.66 | -0.92 | -24.16 | 1 |
| 30 | Donchian 55/20 · 1h | breakout | 83.77 | -16.23 | 71 | 14.1 | -15.67 | -3.27 | -21.87 | 103 |
| 31 | Stochastic reversion · 1h | reversion | 83.64 | -16.36 | 279 | 48.4 | -22.43 | -3.19 | -27.12 | 387 |
| 32 | Opening range 15m | breakout | 83.44 | -16.56 | 465 | 30.5 | -19.11 | -5.49 | -20.97 | 735 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 34 | Keltner breakout · 1h | breakout | 81.45 | -18.55 | 107 | 23.4 | -22.32 | -4.69 | -25.10 | 179 |
| 35 | Connors RSI(2) · 1h | reversion | 80.81 | -19.19 | 205 | 40.0 | -19.29 | -6.46 | -19.64 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.68 | -20.32 | 394 | 23.1 | -38.66 | -7.30 | -41.79 | 682 |
| 37 | MFI reversion · 1h | reversion | 79.50 | -20.50 | 346 | 33.8 | -16.69 | -2.11 | -21.23 | 164 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -38.94 | -2.61 | -44.97 | 25 |
| 39 | ADX DI cross · 1h | trend | 79.11 | -20.89 | 179 | 18.4 | -24.29 | -4.17 | -28.65 | 271 |
| 40 | CCI reversion · 1h | reversion | 78.93 | -21.07 | 308 | 43.8 | -24.56 | -3.77 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 77.03 | -22.97 | 170 | 22.9 | -22.42 | -4.63 | -27.77 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.83 | -4.14 | -33.49 | 373 |
| 44 | Williams %R · 1h | reversion | 75.26 | -24.74 | 334 | 46.7 | -32.18 | -4.84 | -35.90 | 541 |
| 45 | MACD cross · 1h | trend | 75.23 | -24.77 | 349 | 22.6 | -33.12 | -5.45 | -39.51 | 486 |
| 46 | Z-score reversion · 1h | reversion | 75.07 | -24.93 | 176 | 36.4 | -20.42 | -2.94 | -27.66 | 226 |
| 47 | MACD zero-line · 1h | trend | 74.41 | -25.59 | 157 | 16.6 | -24.96 | -5.15 | -29.22 | 208 |
| 48 | EMA 20/50 cross · 1h | trend | 74.37 | -25.63 | 102 | 10.8 | -21.80 | -3.64 | -31.13 | 129 |
| 49 | Supertrend · 1h | trend | 73.25 | -26.75 | 167 | 13.2 | -31.07 | -5.77 | -34.46 | 233 |
| 50 | RSI momentum · 1h | momentum | 72.93 | -27.07 | 159 | 12.6 | -23.92 | -3.81 | -33.29 | 215 |
| 51 | Triple EMA stack · 1h | trend | 72.62 | -27.38 | 142 | 14.8 | -26.41 | -4.72 | -34.73 | 202 |
| 52 | OBV trend · 1h | momentum | 71.78 | -28.22 | 274 | 18.2 | -28.59 | -5.85 | -34.27 | 277 |
| 53 | ROC + volume · 1h | momentum | 71.36 | -28.64 | 349 | 25.5 | -37.44 | -7.16 | -39.87 | 387 |
| 54 | Daily: Momentum burst | daily | 70.55 | -29.45 | 26 | 11.5 | -38.59 | -5.41 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.27 | -29.73 | 142 | 19.7 | -32.11 | -5.98 | -35.64 | 210 |
| 56 | RSI(14) reversion · 1h | reversion | 68.23 | -31.77 | 158 | 29.7 | -29.01 | -4.27 | -32.51 | 243 |
| 57 | Agent (ML meta-label) | meta | 68.07 | -31.93 | 1576 | 23.6 | -6.16 | -0.78 | -19.47 | 342 |
| 58 | VWAP momentum · 1h | momentum | 67.68 | -32.32 | 804 | 21.8 | -52.28 | -11.24 | -53.70 | 1238 |
| 59 | Max aggression: 1-day momentum | meta | 67.34 | -32.66 | 27 | 25.9 | -32.57 | -1.72 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.59 | -34.41 | 246 | 9.8 | -40.11 | -7.74 | -41.58 | 330 |
| 61 | Candlestick reversal · 1h | reversion | 65.47 | -34.53 | 432 | 28.2 | -37.97 | -7.00 | -39.08 | 592 |
| 62 | Three white soldiers | momentum | 62.39 | -37.61 | 492 | 15.0 | -48.78 | -22.61 | -48.79 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -45.68 | -99.00 | 5287 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.96 | -26.29 | -80.09 | 1424 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.28 | -46.53 | -93.36 | 2509 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.43 | -32.38 | -89.47 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.75 | -40.12 | -90.81 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.97 | -31.50 | -89.98 | 2183 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -54.84 | -97.72 | 3457 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.79 | -96.30 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -32.48 | -93.61 | 2406 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -34.84 | -82.35 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.72 | -99.54 | 5992 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -43.26 | -92.55 | 2597 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.56 | -37.58 | -95.58 | 3408 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.97 | -99.80 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -44.01 | -91.89 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.44 | -24.81 | -75.91 | 1590 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -62.14 | -97.68 | 3491 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.29 | -98.84 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.82 | -27.63 | -69.44 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -55.14 | -94.60 | 2733 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.91 | -37.41 | -84.95 | 1767 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -74.56 | -99.66 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.65 | -32.65 | -89.68 | 2280 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.85 | -20.13 | -78.89 | 1783 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.31 | -90.76 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.63 | -96.82 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -57.95 | -89.43 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.07 | -29.04 | -66.26 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.46 | -23.30 | -72.06 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.65 | -19.11 | -79.73 | 1695 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.74 | -97.33 | 4327 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -107.27 | -99.93 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T17:06 | Agent (ML meta-label) | buy | SOXL | 5.24 | — | entry |
| 2026-11-09T17:06 | Agent (ML meta-label) | buy | LABU | 5.24 | — | following MFI reversion |
| 2026-11-09T17:06 | Agent (ML meta-label) | sell | GOOGL | 3.98 | -0.04 | selected signal exited |
| 2026-11-09T17:06 | Agent (ML meta-label) | sell | AAPL | 4.52 | -0.01 | selected signal exited |
| 2026-11-09T17:00 | Agent (ML meta-label) | buy | TECL | 5.24 | — | entry |
| 2026-11-09T17:00 | Agent (ML meta-label) | sell | BITX | 5.24 | 0.00 | selected signal exited |
| 2026-11-09T17:00 | Candlestick reversal · 1h | sell | SOL-USD | 6.41 | -0.05 | exit signal |
| 2026-11-09T16:55 | Agent (ML meta-label) | buy | SPY | 5.24 | — | entry |
| 2026-11-09T16:55 | Agent (ML meta-label) | buy | BITX | 5.24 | — | entry |
| 2026-11-09T16:51 | Agent (ML meta-label) | sell | TECL | 2.16 | 0.02 | selected signal exited |
| 2026-11-09T16:51 | Agent (ML meta-label) | sell | SPY | 4.86 | -0.00 | selected signal exited |
| 2026-11-09T16:51 | Agent (ML meta-label) | sell | BITX | 4.08 | -0.01 | selected signal exited |
| 2026-11-09T16:51 | Gap and go | buy | IWM | 4.90 | — | rebalance up |
| 2026-11-09T16:45 | Agent (ML meta-label) | buy | SPY | 4.86 | — | entry |
| 2026-11-09T16:45 | Agent (ML meta-label) | sell | SOXL | 4.56 | 0.04 | selected signal exited |
| 2026-11-09T16:45 | Agent (ML meta-label) | sell | LABU | 4.52 | 0.00 | selected signal exited |
| 2026-11-09T16:40 | Agent (ML meta-label) | buy | TECL | 2.14 | — | entry |
| 2026-11-09T16:40 | Agent (ML meta-label) | buy | SOXL | 4.52 | — | entry |
| 2026-11-09T16:40 | Agent (ML meta-label) | buy | LABU | 4.52 | — | following MFI reversion |
| 2026-11-09T16:37 | Agent (ML meta-label) | sell | TECL | 4.95 | 0.03 | selected signal exited |
| 2026-11-09T16:37 | Agent (ML meta-label) | sell | SPY | 4.95 | -0.00 | selected signal exited |
| 2026-11-09T16:35 | Day trade: Stocks in Play ORB | sell | NVDA | 24.12 | -0.21 | target is flat |
| 2026-11-09T16:35 | Agent (ML meta-label) | buy | TECL | 4.25 | — | rebalance up |
| 2026-11-09T16:35 | Agent (ML meta-label) | buy | SPY | 4.95 | — | entry |
| 2026-11-09T16:35 | Agent (ML meta-label) | sell | SOXL | 4.78 | -0.09 | selected signal exited |
| 2026-11-09T16:35 | Gap and go | buy | LABU | 4.88 | — | rebalance up |
| 2026-11-09T16:35 | Gap and go | buy | AMD | 4.91 | — | rebalance up |
| 2026-11-09T16:35 | Gap and go | sell | SOXL | 19.40 | 1.00 | stop-loss |
| 2026-11-09T16:30 | Agent (ML meta-label) | sell | TECL | 3.65 | 0.15 | rebalance down |
| 2026-11-09T16:30 | Agent (aggressive) | sell | COIN | 42.32 | 0.31 | selected signal exited |
| 2026-11-09T16:30 | Agent | sell | COIN | 34.99 | 0.08 | selected signal exited |
| 2026-11-09T16:30 | MFI reversion · 1h | buy | NVDA | 3.46 | — | entry signal |
| 2026-11-09T16:30 | MFI reversion · 1h | buy | ETHU | 7.19 | — | entry signal |
| 2026-11-09T16:30 | MFI reversion · 1h | sell | SOXL | 10.66 | 1.35 | exit signal |
| 2026-11-09T16:30 | Williams %R · 1h | sell | UPRO | 18.67 | -0.07 | exit signal |
| 2026-11-09T16:30 | Williams %R · 1h | sell | SPY | 18.89 | -0.03 | exit signal |
| 2026-11-09T16:30 | Z-score reversion · 1h | buy | TQQQ | 4.18 | — | rebalance up |
| 2026-11-09T16:30 | Z-score reversion · 1h | buy | TECL | 3.90 | — | rebalance up |
| 2026-11-09T16:30 | Z-score reversion · 1h | sell | TNA | 4.66 | 0.35 | exit signal |
| 2026-11-09T16:30 | Z-score reversion · 1h | sell | LABU | 4.70 | 0.39 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 17:06:05.000135+00:00 -> 2026-11-09 17:16:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 17:06:05.000135+00:00 -> 2026-11-09 17:16:05.000135+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 17:06:05.000135+00:00 -> 2026-11-09 17:16:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
