# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T19:05:05.000139+00:00 · 63487 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.69 (-15.31%)

Closed trades 216, win rate 35.6%, fees £6.02, max drawdown -17.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 31221 decisions in 2970 calls, $0.3918 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T19:05 | 8 / 13 / 9 | cash |  |
| Breezy | 2026-11-17T19:05 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-17T19:05 | 4 / 23 / 3 | BITX 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.30 | 17.30 | 0 | — | 13.52 | 4.51 | -4.66 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.26 | 11.26 | 24 | 62.5 | 16.84 | 3.41 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.71 | 2.71 | 0 | — | 5.37 | 1.48 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.48 | -2.96 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.48 | -1.52 | 38 | 39.5 | -2.69 | -0.48 | -9.64 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.56 | -4.44 | 8 | 50.0 | -0.85 | 0.21 | -18.69 | 6 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 95.14 | -4.86 | 0 | — | -4.04 | -1.31 | -6.90 | 1 |
| 13 | Agent (rotation) | meta | 94.02 | -5.98 | 197 | 29.9 | -3.22 | -1.13 | -8.23 | 152 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.43 | -8.63 | -5.59 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.14 | -7.86 | 0 | — | -8.40 | -2.20 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 18 | Copy: Insider buying | copy | 90.42 | -9.58 | 50 | 42.0 | -8.66 | -1.71 | -14.79 | 62 |
| 19 | Copy: Congress Democrats (NANC) | copy | 90.28 | -9.72 | 0 | — | -8.24 | -2.22 | -12.67 | 1 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -16.39 | -7.09 | -18.31 | 68 |
| 21 | Daily: Bullish score | daily | 87.29 | -12.71 | 17 | 17.6 | -4.63 | -0.71 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -11.63 | -4.00 | -16.86 | 75 |
| 24 | Opening range 30m | breakout | 86.36 | -13.64 | 438 | 33.6 | -9.68 | -3.06 | -14.11 | 575 |
| 25 | Agent | meta | 84.69 | -15.31 | 216 | 35.6 | -15.09 | -7.05 | -16.88 | 204 |
| 26 | Agent (aggressive) | meta | 82.10 | -17.90 | 101 | 33.7 | -16.97 | -4.67 | -19.92 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.04 | -7.14 | -27.99 | 202 |
| 28 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 122 | 26.2 | -21.02 | -5.05 | -27.31 | 158 |
| 29 | Max aggression: 5-day momentum | meta | 80.74 | -19.27 | 21 | 42.9 | -47.39 | -3.10 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.65 | -6.48 | -15.05 | 93 |
| 31 | Volume breakout · 1h | breakout | 79.93 | -20.07 | 162 | 28.4 | -15.43 | -4.77 | -22.16 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.51 | -29.47 | 83 |
| 33 | Opening range 15m | breakout | 78.27 | -21.73 | 533 | 31.5 | -16.49 | -4.41 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 77.45 | -22.55 | 30 | 26.7 | -23.39 | -0.86 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 75.96 | -24.04 | 2 | 0.0 | -15.20 | -1.87 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.26 | -24.74 | 208 | 19.2 | -26.20 | -4.13 | -34.71 | 259 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.28 | -8.50 | -29.80 | 111 |
| 38 | Hold BTC | benchmark | 74.32 | -25.68 | 2 | 0.0 | -16.55 | -2.35 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.09 | -5.66 | -33.15 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.55 | -27.45 | 345 | 42.6 | -35.24 | -5.32 | -36.44 | 424 |
| 41 | Supertrend · 1h | trend | 71.23 | -28.77 | 189 | 15.9 | -32.57 | -5.54 | -39.76 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.18 | -28.82 | 155 | 14.8 | -30.65 | -6.15 | -36.52 | 184 |
| 43 | RSI momentum · 1h | momentum | 71.07 | -28.93 | 176 | 14.2 | -31.03 | -5.65 | -37.43 | 198 |
| 44 | MACD zero-line · 1h | trend | 70.78 | -29.22 | 181 | 17.7 | -26.28 | -5.19 | -32.76 | 198 |
| 45 | MFI reversion · 1h | reversion | 70.39 | -29.61 | 430 | 33.7 | -26.67 | -3.84 | -30.74 | 165 |
| 46 | EMA 20/50 cross · 1h | trend | 70.01 | -29.99 | 115 | 10.4 | -36.65 | -9.85 | -39.68 | 115 |
| 47 | Heikin-Ashi · 1h | trend | 69.81 | -30.19 | 466 | 23.0 | -41.37 | -8.29 | -44.71 | 633 |
| 48 | ROC + volume · 1h | momentum | 69.58 | -30.42 | 408 | 28.2 | -30.32 | -4.97 | -39.08 | 353 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 50 | MACD cross · 1h | trend | 69.13 | -30.87 | 413 | 22.3 | -39.49 | -6.42 | -44.70 | 470 |
| 51 | OBV trend · 1h | momentum | 68.51 | -31.49 | 306 | 19.0 | -35.69 | -7.56 | -39.92 | 262 |
| 52 | Donchian 20/10 · 1h | breakout | 67.34 | -32.66 | 159 | 18.2 | -30.88 | -5.22 | -39.10 | 204 |
| 53 | CCI reversion · 1h | reversion | 66.38 | -33.62 | 382 | 41.6 | -41.75 | -6.86 | -44.29 | 467 |
| 54 | Bollinger reversion · 1h | reversion | 63.80 | -36.20 | 344 | 37.8 | -38.81 | -5.84 | -39.56 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.05 | -36.95 | 280 | 11.1 | -37.57 | -7.09 | -44.89 | 319 |
| 56 | Williams %R · 1h | reversion | 62.64 | -37.35 | 430 | 40.7 | -46.15 | -7.86 | -47.03 | 562 |
| 57 | Agent (ML meta-label) | meta | 60.18 | -39.82 | 1890 | 24.5 | -31.00 | -6.15 | -31.40 | 320 |
| 58 | RSI(14) reversion · 1h | reversion | 58.01 | -41.99 | 205 | 31.7 | -41.13 | -6.04 | -42.99 | 249 |
| 59 | Z-score reversion · 1h | reversion | 56.90 | -43.10 | 224 | 35.3 | -37.73 | -5.21 | -39.23 | 254 |
| 60 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -53.55 | -9.58 | -58.20 | 1195 |
| 61 | Three white soldiers | momentum | 55.09 | -44.91 | 584 | 14.6 | -49.76 | -21.46 | -50.31 | 662 |
| 62 | Candlestick reversal · 1h | reversion | 54.81 | -45.19 | 546 | 26.6 | -48.26 | -8.74 | -49.46 | 625 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -42.44 | -99.04 | 5265 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.87 | -25.98 | -82.05 | 1400 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.10 | -41.84 | -94.10 | 2487 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.19 | -31.24 | -90.38 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.55 | -38.96 | -91.56 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -30.56 | -89.89 | 2120 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -46.08 | -97.93 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -52.28 | -96.55 | 3419 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -37.29 | -93.54 | 2218 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.22 | -32.00 | -83.30 | 1609 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.74 | -99.60 | 6068 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -40.63 | -92.13 | 2568 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.99 | -37.88 | -95.02 | 3310 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -64.54 | -99.81 | 6163 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.42 | -42.15 | -92.42 | 2253 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.93 | -25.03 | -76.95 | 1645 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -56.97 | -97.66 | 3436 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -53.78 | -99.02 | 4940 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.56 | -26.76 | -68.60 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -52.27 | -94.60 | 2734 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.48 | -36.34 | -84.49 | 1730 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -64.36 | -99.70 | 6371 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.80 | -30.21 | -90.90 | 2358 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.60 | -18.48 | -79.85 | 1828 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.22 | -35.44 | -91.29 | 2170 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -44.34 | -97.56 | 3898 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -55.01 | -89.41 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -29.74 | -66.33 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.09 | -22.93 | -72.51 | 1227 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.45 | -17.57 | -80.69 | 1717 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.83 | -97.60 | 4338 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.36 | -99.94 | 8437 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T19:05 | Agent (ML meta-label) | buy | SPY | 15.05 | — | entry |
| 2026-11-17T19:05 | Agent (ML meta-label) | sell | SQQQ | 15.04 | -0.00 | selected signal exited |
| 2026-11-17T19:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 98.44 | — | entry |
| 2026-11-17T19:01 | Agent (ML meta-label) | buy | SQQQ | 15.05 | — | entry |
| 2026-11-17T19:01 | Agent | sell | BITX | 16.96 | 0.02 | selected signal exited |
| 2026-11-17T19:01 | MFI reversion · 1h | buy | SPY | 4.08 | — | rebalance up |
| 2026-11-17T19:01 | MFI reversion · 1h | buy | AMZN | 4.03 | — | rebalance up |
| 2026-11-17T19:01 | MFI reversion · 1h | sell | BITX | 8.77 | -0.04 | target is flat |
| 2026-11-17T18:56 | Agent (aggressive) | sell | COIN | 40.05 | -0.03 | selected signal exited |
| 2026-11-17T18:56 | Agent | sell | COIN | 16.71 | -0.01 | selected signal exited |
| 2026-11-17T18:50 | Agent | buy | BITX | 16.93 | — | following MFI reversion |
| 2026-11-17T18:50 | Three white soldiers | sell | META | 13.79 | -0.05 | exit signal |
| 2026-11-17T18:41 | Copy: Insider buying | buy | PAM | 8.71 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | buy | LILA | 11.34 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | buy | HUBS | 11.34 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | sell | MDGL | 11.51 | -0.06 | target is flat |
| 2026-11-17T18:41 | Copy: Insider buying | sell | KOD | 10.51 | -0.94 | target is flat |
| 2026-11-17T18:41 | Copy: Insider buying | sell | KMI | 9.37 | 0.18 | target is flat |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | QQQ | 4.71 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | ETHU | 4.63 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | BTC-USD | 4.70 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | sell | GOOGL | 10.05 | -0.02 | target is flat |
| 2026-11-17T18:41 | Three white soldiers | sell | SOXL | 13.61 | -0.23 | exit signal |
| 2026-11-17T18:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.44 | -1.30 | target is flat |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | META | 7.43 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | LABU | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | GOOGL | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | COIN | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | AMD | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | SOXL | 10.13 | 0.28 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | ETHU | 9.09 | 0.13 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | AMZN | 9.06 | -0.03 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | AAPL | 8.92 | -0.07 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | UPRO | 3.06 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | TQQQ | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | TNA | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | SPY | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | QQQ | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | MSFT | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | META | 3.07 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 19:05:05.000139+00:00 -> 2026-11-17 19:15:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 19:05:05.000139+00:00 -> 2026-11-17 19:15:05.000139+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
