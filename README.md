# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T18:52:05.000128+00:00 · 46452 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.54 (-9.46%)

Closed trades 141, win rate 39.0%, fees £3.96, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 28278 decisions in 2748 calls, $0.3545 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T18:52 | 2 / 10 / 18 | cash |  |
| Breezy | 2026-11-03T18:52 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T18:52 | 3 / 26 / 1 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| MACD zero-line | MSFT | 1.87 | +0.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.37 | 9.37 | 0 | — | 10.68 | 4.61 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 1.26 | 0.54 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.01 | 1.01 | 26 | 26.9 | 8.76 | 2.22 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.93 | -3.58 | -13.20 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 97.04 | -2.96 | 0 | — | -1.21 | -0.60 | -3.94 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.63 | -3.37 | 5 | 40.0 | 3.01 | 0.79 | -7.93 | 8 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.45 | -3.55 | 107 | 34.6 | 4.44 | 2.13 | -3.79 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.85 | -4.15 | 0 | — | -0.80 | -0.23 | -6.60 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.24 | -4.76 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.61 | -5.33 | 29 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.47 | -5.53 | 0 | — | -2.86 | -1.07 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -5.15 | -3.05 | -8.68 | 185 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | 1.50 | 0.54 | -9.15 | 226 |
| 19 | Hold BTC | benchmark | 91.51 | -8.49 | 0 | — | 0.27 | 0.22 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.71 | -9.29 | 102 | 21.6 | -16.48 | -6.10 | -17.42 | 79 |
| 22 | Agent | meta | 90.54 | -9.46 | 141 | 39.0 | -10.54 | -6.38 | -12.22 | 209 |
| 23 | Opening range 30m | breakout | 90.21 | -9.79 | 337 | 32.9 | -12.55 | -3.82 | -17.21 | 591 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -8.09 | -2.73 | -13.79 | 88 |
| 25 | Parabolic SAR · 1h | trend | 88.66 | -11.34 | 150 | 26.7 | -13.79 | -3.19 | -17.40 | 241 |
| 26 | Copy: Insider buying | copy | 88.59 | -11.41 | 35 | 37.1 | -22.10 | -4.49 | -23.13 | 61 |
| 27 | Donchian 55/20 · 1h | breakout | 88.38 | -11.62 | 60 | 13.3 | -14.62 | -3.29 | -18.06 | 100 |
| 28 | Daily: Bullish score | daily | 88.28 | -11.72 | 14 | 21.4 | -5.23 | -0.61 | -14.82 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.16 | -12.84 | 1 | 0.0 | -2.76 | -0.25 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Stochastic reversion · 1h | reversion | 84.93 | -15.07 | 241 | 46.9 | -23.72 | -4.74 | -26.18 | 390 |
| 32 | Volume breakout · 1h | breakout | 84.72 | -15.28 | 129 | 28.7 | -15.48 | -3.57 | -18.08 | 96 |
| 33 | Max aggression: 5-day momentum | meta | 84.61 | -15.39 | 15 | 40.0 | -29.69 | -1.97 | -36.71 | 25 |
| 34 | MFI reversion · 1h | reversion | 84.49 | -15.51 | 305 | 33.1 | -14.66 | -2.26 | -18.11 | 150 |
| 35 | Keltner breakout · 1h | breakout | 84.08 | -15.93 | 89 | 23.6 | -23.37 | -4.90 | -23.96 | 174 |
| 36 | Connors RSI(2) · 1h | reversion | 83.92 | -16.08 | 191 | 40.8 | -20.04 | -6.56 | -20.56 | 134 |
| 37 | ADX DI cross · 1h | trend | 83.32 | -16.68 | 148 | 18.2 | -17.88 | -3.47 | -21.39 | 252 |
| 38 | Opening range 15m | breakout | 83.00 | -17.00 | 411 | 30.2 | -17.94 | -5.21 | -20.73 | 724 |
| 39 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -17.67 | -3.58 | -23.31 | 233 |
| 40 | Ichimoku · 1h | trend | 81.10 | -18.90 | 84 | 13.1 | -17.95 | -3.63 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.95 | -20.05 | 90 | 11.1 | -19.36 | -3.60 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 79.40 | -20.59 | 268 | 44.8 | -25.19 | -3.97 | -27.71 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.44 | -21.56 | 225 | 38.7 | -27.40 | -5.33 | -30.14 | 376 |
| 44 | MACD zero-line · 1h | trend | 77.95 | -22.05 | 136 | 15.4 | -24.94 | -5.45 | -27.28 | 214 |
| 45 | Supertrend · 1h | trend | 77.83 | -22.17 | 141 | 12.8 | -27.80 | -5.29 | -29.54 | 222 |
| 46 | Z-score reversion · 1h | reversion | 77.73 | -22.27 | 142 | 34.5 | -14.19 | -2.04 | -23.02 | 218 |
| 47 | MACD cross · 1h | trend | 77.27 | -22.73 | 301 | 23.6 | -34.09 | -6.57 | -36.66 | 484 |
| 48 | Williams %R · 1h | reversion | 77.06 | -22.94 | 278 | 46.4 | -36.26 | -6.44 | -37.62 | 530 |
| 49 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.10 | -3.53 | -33.57 | 33 |
| 50 | RSI momentum · 1h | momentum | 76.46 | -23.54 | 136 | 12.5 | -28.76 | -5.63 | -30.59 | 214 |
| 51 | Triple EMA stack · 1h | trend | 76.24 | -23.75 | 126 | 14.3 | -28.59 | -5.69 | -31.27 | 205 |
| 52 | Heikin-Ashi · 1h | trend | 76.20 | -23.80 | 357 | 22.4 | -41.21 | -8.69 | -44.15 | 667 |
| 53 | OBV trend · 1h | momentum | 75.88 | -24.12 | 240 | 17.5 | -30.42 | -6.39 | -32.63 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.23 | -24.77 | 120 | 20.0 | -28.86 | -5.24 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.15 | -25.85 | 304 | 25.7 | -35.16 | -6.93 | -36.05 | 376 |
| 56 | RSI(14) reversion · 1h | reversion | 73.21 | -26.79 | 130 | 26.2 | -19.82 | -3.40 | -26.28 | 207 |
| 57 | Candlestick reversal · 1h | reversion | 71.20 | -28.80 | 358 | 28.8 | -34.74 | -6.49 | -38.25 | 551 |
| 58 | Agent (ML meta-label) | meta | 70.04 | -29.96 | 1357 | 21.7 | -13.22 | -2.57 | -16.47 | 292 |
| 59 | EMA 9/21 cross · 1h | trend | 69.12 | -30.88 | 219 | 9.6 | -37.12 | -7.49 | -38.85 | 330 |
| 60 | Three white soldiers | momentum | 69.09 | -30.91 | 416 | 16.1 | -46.39 | -21.73 | -46.39 | 619 |
| 61 | VWAP momentum · 1h | momentum | 68.60 | -31.40 | 701 | 21.7 | -53.37 | -10.50 | -56.29 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 68.17 | -31.83 | 23 | 30.4 | -32.88 | -1.87 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.23 | -98.96 | 5162 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.11 | -22.95 | -80.24 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.29 | -43.99 | -93.38 | 2523 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.75 | -30.52 | -89.04 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -36.58 | -91.12 | 2331 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -31.94 | -90.69 | 2223 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.68 | -50.57 | -97.70 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -56.87 | -96.22 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -34.64 | -93.67 | 2407 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.65 | -34.15 | -82.07 | 1666 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.74 | -99.48 | 5848 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -42.90 | -92.95 | 2620 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.35 | -36.76 | -95.37 | 3355 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.70 | -99.80 | 6171 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -43.90 | -91.89 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.52 | -26.05 | -74.93 | 1555 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -60.20 | -97.78 | 3528 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.42 | -98.66 | 4806 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.36 | -28.53 | -70.27 | 1190 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -52.82 | -94.72 | 2780 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.84 | -37.17 | -84.87 | 1810 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.70 | -99.61 | 6283 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.09 | -29.70 | -88.22 | 2225 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.32 | -18.83 | -76.65 | 1687 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.04 | -35.88 | -90.11 | 2217 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -49.27 | -96.42 | 3795 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -52.26 | -89.27 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.24 | -26.93 | -65.75 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.29 | -24.51 | -74.09 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.91 | -18.85 | -77.10 | 1584 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.49 | -96.80 | 4211 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.27 | -99.92 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | TSLA | 4.38 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | SQQQ | 4.40 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | MSTR | 4.41 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | ETHU | 4.42 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | BITX | 4.42 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | sell | UPRO | 2.84 | -0.00 | selected signal exited |
| 2026-11-03T18:50 | Agent (ML meta-label) | sell | TQQQ | 9.59 | -0.01 | selected signal exited |
| 2026-11-03T18:50 | Agent (ML meta-label) | sell | SOXL | 9.59 | -0.02 | selected signal exited |
| 2026-11-03T18:50 | Three white soldiers | sell | IWM | 17.25 | -0.03 | exit signal |
| 2026-11-03T18:45 | Agent (ML meta-label) | buy | UPRO | 2.85 | — | entry |
| 2026-11-03T18:45 | Agent (ML meta-label) | buy | TQQQ | 9.61 | — | entry |
| 2026-11-03T18:45 | Agent (ML meta-label) | buy | SOXL | 9.61 | — | following Connors RSI(2) |
| 2026-11-03T18:45 | Agent (ML meta-label) | sell | TSLA | 4.38 | -0.01 | rebalance down |
| 2026-11-03T18:45 | Agent (ML meta-label) | sell | SQQQ | 4.45 | -0.01 | rebalance down |
| 2026-11-03T18:45 | Agent (ML meta-label) | sell | MSTR | 4.40 | -0.01 | rebalance down |
| 2026-11-03T18:45 | Agent (ML meta-label) | sell | ETHU | 4.41 | -0.00 | rebalance down |
| 2026-11-03T18:45 | Agent (ML meta-label) | sell | BITX | 4.43 | -0.00 | rebalance down |
| 2026-11-03T18:30 | Williams %R · 1h | buy | TSLA | 4.02 | — | entry signal |
| 2026-11-03T18:30 | Z-score reversion · 1h | buy | PLTR | 5.55 | — | entry signal |
| 2026-11-03T18:30 | Bollinger reversion · 1h | buy | PLTR | 1.93 | — | entry |
| 2026-11-03T18:30 | Bollinger reversion · 1h | buy | AAPL | 11.21 | — | entry |
| 2026-11-03T18:30 | Bollinger reversion · 1h | sell | BITX | 13.14 | 0.14 | exit signal |
| 2026-11-03T18:30 | Candlestick reversal · 1h | buy | AMD | 3.91 | — | entry signal |
| 2026-11-03T18:30 | Candlestick reversal · 1h | sell | SOXL | 3.91 | 0.03 | rebalance down |
| 2026-11-03T18:30 | VWAP momentum · 1h | buy | GOOGL | 1.80 | — | entry signal |
| 2026-11-03T18:30 | VWAP momentum · 1h | buy | AMZN | 3.12 | — | entry |
| 2026-11-03T18:30 | VWAP momentum · 1h | sell | COIN | 4.92 | 0.04 | exit signal |
| 2026-11-03T18:30 | Trend pullback · 1h | buy | IWM | 22.68 | — | entry signal |
| 2026-11-03T18:30 | MACD cross · 1h | buy | SPY | 1.10 | — | entry signal |
| 2026-11-03T18:30 | MACD cross · 1h | buy | QQQ | 3.86 | — | entry signal |
| 2026-11-03T18:30 | MACD cross · 1h | sell | SQQQ | 4.56 | 0.09 | exit signal |
| 2026-11-03T18:30 | Triple EMA stack · 1h | buy | TNA | 8.50 | — | entry signal |
| 2026-11-03T18:30 | Triple EMA stack · 1h | sell | XRP-USD | 3.97 | -0.03 | rebalance down |
| 2026-11-03T18:30 | Triple EMA stack · 1h | sell | SQQQ | 4.54 | 0.13 | rebalance down |
| 2026-11-03T18:30 | EMA 9/21 cross · 1h | buy | IWM | 3.76 | — | rebalance up |
| 2026-11-03T18:30 | EMA 9/21 cross · 1h | sell | AMZN | 4.01 | 0.02 | rebalance down |
| 2026-11-03T18:25 | Candlestick reversal · 1h | buy | ETHU | 4.60 | — | entry |
| 2026-11-03T18:23 | Candlestick reversal · 1h | sell | ETHU | 4.60 | -0.01 | target is flat |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | TSLA | 3.96 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | SQQQ | 4.04 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 18:52:05.000128+00:00 -> 2026-11-03 19:02:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 18:52:05.000128+00:00 -> 2026-11-03 19:02:05.000128+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 18:52:05.000128+00:00 -> 2026-11-03 19:02:05.000128+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
