# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T19:05:05.000127+00:00 · 53704 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.41 (-12.59%)

Closed trades 159, win rate 35.8%, fees £4.91, max drawdown -13.04%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.44 | -0.17 |

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

Today: 29589 decisions in 2976 calls, $0.3726 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T19:05 | 2 / 20 / 9 | cash |  |
| Breezy | 2026-11-09T19:05 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-11-09T19:05 | 4 / 25 / 2 | COIN 70% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.06 | 17.06 | 19 | 68.4 | 17.13 | 3.53 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.40 | 4.60 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.45 | 11.45 | 30 | 26.7 | 19.42 | 2.98 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 30 | 43.3 | 3.25 | 0.88 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.47 | 1.48 | 0 | — | 5.02 | 1.44 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.36 | 1.36 | 123 | 35.0 | 9.74 | 3.83 | -2.27 | 89 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.67 | 0.67 | 7 | 42.9 | -1.32 | 0.15 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.78 | -1.22 | 179 | 29.1 | 3.77 | 1.12 | -9.06 | 240 |
| 11 | Agent (rotation) | meta | 97.93 | -2.08 | 176 | 27.8 | -2.65 | -1.10 | -9.58 | 161 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.60 | -3.40 | 0 | — | -1.48 | -0.45 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.66 | -5.34 | 0 | — | -3.76 | -0.98 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.75 | -7.25 | 108 | 23.1 | -13.39 | -5.00 | -17.75 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.64 | -7.36 | 0 | — | -4.07 | -1.09 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.29 | -9.71 | 378 | 32.3 | -14.33 | -4.56 | -15.99 | 598 |
| 22 | Copy: Insider buying | copy | 89.84 | -10.16 | 40 | 37.5 | -10.77 | -2.42 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -7.96 | -2.79 | -14.15 | 77 |
| 24 | Agent | meta | 87.41 | -12.59 | 159 | 35.8 | -13.20 | -6.86 | -13.71 | 202 |
| 25 | Hold BTC | benchmark | 86.78 | -13.22 | 1 | 0.0 | -5.24 | -0.61 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.23 | -13.77 | 15 | 20.0 | -9.70 | -1.42 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.77 | -14.23 | 167 | 26.9 | -11.16 | -2.02 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.74 | -4.46 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 83.67 | -16.33 | 71 | 14.1 | -16.48 | -3.49 | -21.90 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.63 | -16.37 | 2 | 0.0 | -8.57 | -0.97 | -24.16 | 1 |
| 31 | Opening range 15m | breakout | 83.41 | -16.59 | 466 | 30.5 | -18.98 | -5.42 | -20.97 | 736 |
| 32 | Stochastic reversion · 1h | reversion | 83.19 | -16.81 | 279 | 48.4 | -23.83 | -3.51 | -28.12 | 387 |
| 33 | Keltner breakout · 1h | breakout | 81.95 | -18.05 | 107 | 23.4 | -21.87 | -4.55 | -25.10 | 178 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.70 | -19.30 | 205 | 40.0 | -19.13 | -6.37 | -19.40 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.78 | -20.22 | 398 | 22.9 | -38.22 | -7.15 | -41.81 | 681 |
| 37 | ADX DI cross · 1h | trend | 79.32 | -20.68 | 179 | 18.4 | -22.57 | -3.85 | -28.65 | 269 |
| 38 | MFI reversion · 1h | reversion | 79.28 | -20.73 | 348 | 33.9 | -17.48 | -2.24 | -21.38 | 163 |
| 39 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -39.18 | -2.63 | -44.97 | 25 |
| 40 | CCI reversion · 1h | reversion | 78.91 | -21.09 | 310 | 44.2 | -24.44 | -3.74 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 76.96 | -23.04 | 170 | 22.9 | -22.19 | -4.61 | -27.85 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.80 | -4.12 | -33.46 | 373 |
| 44 | MACD cross · 1h | trend | 75.21 | -24.79 | 349 | 22.6 | -33.51 | -5.47 | -39.64 | 487 |
| 45 | Z-score reversion · 1h | reversion | 75.03 | -24.98 | 176 | 36.4 | -20.42 | -2.94 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 74.97 | -25.03 | 336 | 46.7 | -34.27 | -5.41 | -37.55 | 543 |
| 47 | MACD zero-line · 1h | trend | 74.48 | -25.52 | 157 | 16.6 | -24.81 | -5.11 | -29.19 | 211 |
| 48 | EMA 20/50 cross · 1h | trend | 74.27 | -25.73 | 102 | 10.8 | -21.86 | -3.65 | -31.13 | 128 |
| 49 | Supertrend · 1h | trend | 73.37 | -26.63 | 167 | 13.2 | -31.23 | -5.63 | -34.87 | 229 |
| 50 | RSI momentum · 1h | momentum | 73.15 | -26.85 | 159 | 12.6 | -23.65 | -3.77 | -33.28 | 214 |
| 51 | Triple EMA stack · 1h | trend | 72.60 | -27.40 | 143 | 14.7 | -26.22 | -4.63 | -34.74 | 202 |
| 52 | OBV trend · 1h | momentum | 71.78 | -28.22 | 274 | 18.2 | -28.36 | -5.66 | -34.25 | 276 |
| 53 | ROC + volume · 1h | momentum | 71.70 | -28.30 | 349 | 25.5 | -36.77 | -6.95 | -39.42 | 386 |
| 54 | Donchian 20/10 · 1h | breakout | 70.50 | -29.50 | 142 | 19.7 | -31.85 | -5.92 | -35.64 | 210 |
| 55 | Daily: Momentum burst | daily | 70.47 | -29.53 | 26 | 11.5 | -38.08 | -5.42 | -39.42 | 31 |
| 56 | RSI(14) reversion · 1h | reversion | 68.10 | -31.90 | 160 | 30.6 | -31.31 | -4.77 | -34.60 | 245 |
| 57 | Agent (ML meta-label) | meta | 67.95 | -32.05 | 1608 | 23.8 | -5.39 | -0.67 | -18.50 | 349 |
| 58 | VWAP momentum · 1h | momentum | 67.65 | -32.35 | 810 | 21.6 | -51.81 | -11.07 | -53.77 | 1234 |
| 59 | Max aggression: 1-day momentum | meta | 67.31 | -32.69 | 27 | 25.9 | -32.52 | -1.71 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.66 | -34.34 | 247 | 9.7 | -39.03 | -7.45 | -40.80 | 332 |
| 61 | Candlestick reversal · 1h | reversion | 65.14 | -34.86 | 434 | 28.6 | -38.81 | -7.16 | -39.66 | 594 |
| 62 | Three white soldiers | momentum | 62.31 | -37.69 | 494 | 15.2 | -48.78 | -22.78 | -48.78 | 649 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.74 | -98.98 | 5268 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.86 | -26.41 | -79.95 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.15 | -46.15 | -93.27 | 2506 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.19 | -32.39 | -89.28 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.68 | -40.08 | -90.75 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.71 | -90.05 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -54.67 | -97.69 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -57.49 | -96.29 | 3407 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.44 | -93.60 | 2417 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.09 | -34.48 | -82.28 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -55.98 | -99.53 | 5973 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.27 | -43.01 | -92.48 | 2592 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.49 | -95.50 | 3399 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.01 | -99.79 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -44.06 | -91.73 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.21 | -24.76 | -75.76 | 1584 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -62.14 | -97.67 | 3509 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -63.54 | -98.84 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.48 | -26.70 | -69.38 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -55.06 | -94.53 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -37.50 | -84.83 | 1769 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.51 | -99.65 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.62 | -32.67 | -89.67 | 2270 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.49 | -20.17 | -78.52 | 1748 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.75 | -90.69 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.57 | -96.82 | 3881 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -57.55 | -89.42 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.95 | -28.97 | -66.28 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.31 | -23.11 | -72.00 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.59 | -19.13 | -79.73 | 1686 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -50.13 | -97.31 | 4323 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.11 | -99.93 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T19:05 | Agent (ML meta-label) | buy | AAPL | 5.23 | — | entry |
| 2026-11-09T19:05 | Agent (ML meta-label) | sell | TQQQ | 4.46 | -0.01 | selected signal exited |
| 2026-11-09T19:05 | Agent (ML meta-label) | sell | QQQ | 4.84 | -0.01 | selected signal exited |
| 2026-11-09T19:00 | VWAP momentum · 1h | sell | BTC-USD | 5.94 | -0.06 | exit signal |
| 2026-11-09T19:00 | Three white soldiers | sell | XRP-USD | 15.47 | -0.15 | exit signal |
| 2026-11-09T18:56 | Agent (ML meta-label) | buy | TQQQ | 4.47 | — | entry |
| 2026-11-09T18:56 | Agent (ML meta-label) | buy | TECL | 4.84 | — | entry |
| 2026-11-09T18:56 | Agent (ML meta-label) | buy | QQQ | 4.84 | — | entry |
| 2026-11-09T18:56 | Agent (ML meta-label) | sell | GOOGL | 4.75 | -0.00 | selected signal exited |
| 2026-11-09T18:56 | Agent (ML meta-label) | sell | AAPL | 4.77 | 0.01 | selected signal exited |
| 2026-11-09T18:50 | Agent (ML meta-label) | sell | TECL | 1.99 | 0.02 | selected signal exited |
| 2026-11-09T18:41 | Agent (ML meta-label) | buy | SOXL | 3.63 | — | rebalance up |
| 2026-11-09T18:41 | Agent (ML meta-label) | sell | QQQ | 4.75 | -0.01 | selected signal exited |
| 2026-11-09T18:41 | Agent (ML meta-label) | sell | IWM | 1.52 | -0.00 | selected signal exited |
| 2026-11-09T18:41 | MFI reversion · 1h | sell | ETHU | 7.19 | -0.01 | target is flat |
| 2026-11-09T18:41 | Williams %R · 1h | sell | NVDA | 18.63 | -0.19 | target is flat |
| 2026-11-09T18:41 | Three white soldiers | buy | XRP-USD | 15.61 | — | entry signal |
| 2026-11-09T18:36 | Agent (ML meta-label) | buy | IWM | 1.52 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | QQQ | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | LABU | 4.76 | — | following MFI reversion |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | GOOGL | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | AAPL | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | SOXL | 4.28 | 0.01 | rebalance down |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | META | 5.47 | -0.01 | selected signal exited |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | BITX | 4.81 | -0.04 | selected signal exited |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | TECL | 1.98 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | SOXL | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | META | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | AMD | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | sell | PLTR | 5.49 | 0.38 | selected signal exited |
| 2026-11-09T18:30 | CCI reversion · 1h | sell | IWM | 1.82 | 0.03 | exit signal |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | SQQQ | 5.14 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | ETH-USD | 5.84 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | DOGE-USD | 3.76 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | COIN | 3.75 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | BTC-USD | 6.59 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | sell | TSLA | 9.33 | 0.20 | exit signal |
| 2026-11-09T18:30 | Candlestick reversal · 1h | sell | PLTR | 9.33 | 0.30 | exit signal |
| 2026-11-09T18:30 | VWAP momentum · 1h | sell | TSLA | 3.04 | -0.02 | exit signal |
| 2026-11-09T18:30 | VWAP momentum · 1h | sell | AAPL | 3.05 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 19:05:05.000127+00:00 -> 2026-11-09 19:15:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 19:05:05.000127+00:00 -> 2026-11-09 19:15:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 19:05:05.000127+00:00 -> 2026-11-09 19:15:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
