# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T17:28:05.000134+00:00 · 64667 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.89 (-15.11%)

Closed trades 222, win rate 36.0%, fees £6.13, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SPY | 16.98 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-18 | PEPG 12%, FUN 12%, STWD 12%, LRN 12%, PSEC 12%, TEAM 12%, BH 12%, LILA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-17)

**Correction** since 2026-11-13 · level correction · 3 distribution days in 25 sessions · timing exposure 0% · VXN 34.44 · VIX 25.46 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.2, AAPL 6.1, AMZN 4.3, TSLA 2.4, META 1.9, AMD 1.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 23892 decisions in 2715 calls, $0.3059 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T17:28 | 3 / 25 / 2 | AMD 19%, SOXL 15% |  |
| Breezy | 2026-11-18T17:28 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-18T17:28 | 10 / 19 / 1 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.90 | +5.25% | 11 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 114.84 | 14.84 | 0 | — | 12.42 | 4.35 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.25 | 4.25 | 0 | — | 5.35 | 1.38 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.65 | 0.65 | 150 | 34.7 | -3.12 | -2.63 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 7.96 | 2.22 | -9.06 | 214 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.75 | -3.25 | 8 | 50.0 | -4.02 | -0.09 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.93 | -4.07 | 0 | — | -4.00 | -1.30 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.20 | -1.48 | -8.74 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.62 | -8.71 | -6.20 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.49 | -7.51 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 92.02 | -7.98 | 50 | 42.0 | -9.06 | -1.80 | -14.79 | 64 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.98 | -9.02 | 0 | — | -8.02 | -2.17 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.31 | -9.69 | 113 | 23.9 | -12.54 | -6.90 | -12.89 | 56 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.03 | -12.97 | 17 | 17.6 | -5.89 | -0.85 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Opening range 30m | breakout | 85.10 | -14.90 | 443 | 33.4 | -10.42 | -3.30 | -14.43 | 565 |
| 25 | Agent | meta | 84.89 | -15.11 | 222 | 36.0 | -15.10 | -7.32 | -17.06 | 201 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 104 | 33.7 | -15.70 | -4.17 | -19.74 | 97 |
| 27 | Parabolic SAR · 1h | trend | 81.63 | -18.37 | 188 | 28.2 | -23.90 | -6.78 | -26.97 | 202 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Keltner breakout · 1h | breakout | 79.77 | -20.23 | 124 | 25.8 | -24.00 | -6.23 | -28.41 | 158 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -14.35 | -4.42 | -21.17 | 77 |
| 31 | Donchian 55/20 · 1h | breakout | 79.17 | -20.83 | 78 | 12.8 | -25.31 | -6.65 | -30.57 | 84 |
| 32 | Max aggression: 5-day momentum | meta | 78.87 | -21.13 | 21 | 42.9 | -48.18 | -3.23 | -55.24 | 21 |
| 33 | Opening range 15m | breakout | 78.01 | -21.99 | 536 | 31.5 | -16.67 | -4.50 | -21.44 | 674 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.23 | -22.77 | 2 | 0.0 | -18.14 | -2.40 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 74.88 | -25.12 | 209 | 19.1 | -27.82 | -4.58 | -35.70 | 269 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.44 | -8.60 | -30.50 | 111 |
| 37 | Hold BTC | benchmark | 74.09 | -25.91 | 2 | 0.0 | -17.92 | -2.48 | -28.91 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 73.21 | -26.79 | 350 | 42.3 | -34.08 | -5.17 | -35.59 | 426 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -30.02 | -7.92 | -34.15 | 221 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.78 | -2.35 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.70 | -28.30 | 191 | 16.2 | -32.29 | -5.45 | -39.50 | 202 |
| 42 | Triple EMA stack · 1h | trend | 70.95 | -29.05 | 156 | 14.7 | -31.38 | -6.31 | -37.28 | 177 |
| 43 | MFI reversion · 1h | reversion | 70.91 | -29.09 | 444 | 33.6 | -26.82 | -3.96 | -30.08 | 163 |
| 44 | RSI momentum · 1h | momentum | 70.21 | -29.79 | 179 | 14.5 | -31.88 | -5.79 | -38.08 | 199 |
| 45 | MACD zero-line · 1h | trend | 69.94 | -30.06 | 183 | 17.5 | -27.67 | -5.53 | -33.83 | 202 |
| 46 | EMA 20/50 cross · 1h | trend | 69.49 | -30.51 | 116 | 10.3 | -36.18 | -9.32 | -40.13 | 117 |
| 47 | Heikin-Ashi · 1h | trend | 69.41 | -30.59 | 474 | 23.0 | -45.16 | -9.99 | -45.80 | 635 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 49 | ROC + volume · 1h | momentum | 68.47 | -31.53 | 413 | 28.1 | -33.16 | -5.95 | -39.35 | 341 |
| 50 | OBV trend · 1h | momentum | 68.23 | -31.77 | 310 | 19.4 | -35.86 | -7.69 | -39.97 | 255 |
| 51 | MACD cross · 1h | trend | 68.18 | -31.82 | 416 | 22.1 | -40.19 | -6.59 | -46.30 | 484 |
| 52 | CCI reversion · 1h | reversion | 67.53 | -32.47 | 385 | 41.3 | -41.53 | -6.90 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 66.47 | -33.53 | 162 | 17.9 | -35.57 | -6.65 | -41.29 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 64.23 | -35.77 | 346 | 37.6 | -38.46 | -5.84 | -39.58 | 413 |
| 55 | Williams %R · 1h | reversion | 63.93 | -36.07 | 436 | 40.6 | -46.45 | -8.09 | -47.61 | 564 |
| 56 | EMA 9/21 cross · 1h | trend | 63.02 | -36.98 | 284 | 11.3 | -40.59 | -7.98 | -46.52 | 322 |
| 57 | Agent (ML meta-label) | meta | 60.33 | -39.67 | 1919 | 24.5 | -23.99 | -4.83 | -26.32 | 284 |
| 58 | RSI(14) reversion · 1h | reversion | 59.32 | -40.67 | 206 | 32.0 | -40.81 | -6.03 | -43.32 | 250 |
| 59 | Z-score reversion · 1h | reversion | 58.00 | -42.00 | 226 | 35.0 | -36.63 | -5.06 | -39.63 | 253 |
| 60 | VWAP momentum · 1h | momentum | 55.76 | -44.24 | 975 | 21.7 | -55.84 | -11.19 | -59.52 | 1191 |
| 61 | Candlestick reversal · 1h | reversion | 55.49 | -44.51 | 552 | 26.4 | -46.82 | -8.56 | -48.22 | 638 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.68 | -21.86 | -50.71 | 660 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.82 | -99.04 | 5285 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.39 | -25.86 | -82.55 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.64 | -41.59 | -93.95 | 2452 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.92 | -31.83 | -90.26 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.03 | -39.25 | -91.48 | 2296 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.40 | -90.06 | 2090 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -48.49 | -97.92 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -52.91 | -96.42 | 3384 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -39.58 | -93.65 | 2214 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.38 | -34.39 | -82.70 | 1583 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.61 | -55.13 | -99.61 | 6116 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.87 | -42.49 | -92.15 | 2548 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.90 | -39.32 | -94.92 | 3261 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.60 | -99.81 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.43 | -44.01 | -92.65 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.63 | -26.01 | -76.35 | 1652 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -61.10 | -97.71 | 3430 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.37 | -99.08 | 4980 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.24 | -28.75 | -69.59 | 1237 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -57.08 | -94.65 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.50 | -38.25 | -84.85 | 1725 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -70.29 | -99.71 | 6393 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.92 | -31.32 | -91.06 | 2371 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.13 | -19.05 | -80.52 | 1851 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -36.75 | -91.62 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.58 | -46.34 | -97.60 | 3919 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -57.57 | -89.32 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.32 | -29.85 | -67.20 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.57 | -24.08 | -73.04 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.68 | -18.39 | -82.02 | 1778 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -46.40 | -97.61 | 4332 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.25 | -99.94 | 8450 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T17:25 | Agent (aggressive) | sell | SOXL | 42.45 | 1.57 | selected signal exited |
| 2026-11-18T17:25 | Agent | buy | SPY | 16.98 | — | following Squeeze breakout |
| 2026-11-18T17:25 | Agent | sell | SQQQ | 16.48 | -0.45 | selected signal exited |
| 2026-11-18T17:25 | Agent | sell | SOXL | 17.58 | 0.65 | selected signal exited |
| 2026-11-18T17:25 | Opening range 15m | sell | SQQQ | 18.42 | -0.48 | stop-loss |
| 2026-11-18T17:20 | Agent (ML meta-label) | sell | TSLA | 6.67 | 0.02 | selected signal exited |
| 2026-11-18T17:20 | Agent (ML meta-label) | sell | AAPL | 6.65 | -0.00 | selected signal exited |
| 2026-11-18T17:20 | Opening range 30m | sell | SQQQ | 20.80 | -0.48 | stop-loss |
| 2026-11-18T17:15 | MFI reversion · 1h | sell | ETHU | 11.71 | -0.01 | target is flat |
| 2026-11-18T17:11 | Agent (ML meta-label) | buy | TSLA | 6.65 | — | following Stochastic reversion |
| 2026-11-18T17:11 | Agent (ML meta-label) | buy | AAPL | 6.65 | — | entry |
| 2026-11-18T17:05 | Opening range 30m | buy | TNA | 21.00 | — | entry signal |
| 2026-11-18T17:05 | Opening range 30m | buy | IWM | 21.22 | — | entry signal |
| 2026-11-18T17:01 | Agent | sell | TSLA | 16.98 | 0.04 | selected signal exited |
| 2026-11-18T17:01 | Williams %R · 1h | buy | DOGE-USD | 3.95 | — | entry signal |
| 2026-11-18T17:01 | Donchian 20/10 · 1h | sell | SOL-USD | 16.87 | -0.09 | exit signal |
| 2026-11-18T17:01 | RSI momentum · 1h | sell | XRP-USD | 16.78 | -0.25 | exit signal |
| 2026-11-18T17:01 | Supertrend · 1h | buy | SOL-USD | 3.73 | — | rebalance up |
| 2026-11-18T17:01 | Supertrend · 1h | buy | AMZN | 6.52 | — | rebalance up |
| 2026-11-18T17:01 | Supertrend · 1h | sell | XRP-USD | 14.21 | 0.15 | exit signal |
| 2026-11-18T17:01 | Supertrend · 1h | sell | DOGE-USD | 14.19 | -0.13 | exit signal |
| 2026-11-18T17:01 | Triple EMA stack · 1h | sell | SOL-USD | 17.82 | -0.01 | exit signal |
| 2026-11-18T17:01 | EMA 9/21 cross · 1h | sell | SOL-USD | 15.60 | 0.03 | exit signal |
| 2026-11-18T16:55 | Opening range 30m | buy | SQQQ | 21.28 | — | entry signal |
| 2026-11-18T16:50 | Agent (aggressive) | buy | SOXL | 40.89 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T16:50 | Agent | buy | SQQQ | 16.93 | — | following OBV trend |
| 2026-11-18T16:50 | Agent | buy | SOXL | 16.93 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T16:40 | Agent (ML meta-label) | sell | TSLA | 6.65 | -0.03 | selected signal exited |
| 2026-11-18T16:40 | Agent (ML meta-label) | sell | AAPL | 6.68 | -0.01 | selected signal exited |
| 2026-11-18T16:40 | CCI reversion · 1h | buy | TNA | 2.58 | — | entry |
| 2026-11-18T16:40 | CCI reversion · 1h | sell | ETH-USD | 2.33 | -0.05 | stop-loss |
| 2026-11-18T16:40 | Williams %R · 1h | sell | ETHU | 3.44 | -0.07 | stop-loss |
| 2026-11-18T16:40 | Williams %R · 1h | sell | ETH-USD | 1.75 | -0.04 | stop-loss |
| 2026-11-18T16:40 | Candlestick reversal · 1h | sell | ETHU | 2.86 | -0.17 | stop-loss |
| 2026-11-18T16:35 | Agent (ML meta-label) | buy | TECL | 6.64 | — | entry |
| 2026-11-18T16:35 | Agent (ML meta-label) | sell | IWM | 6.67 | -0.02 | selected signal exited |
| 2026-11-18T16:35 | MFI reversion · 1h | buy | ETHU | 11.72 | — | entry |
| 2026-11-18T16:30 | VWAP momentum · 1h | sell | TNA | 13.75 | -0.18 | exit signal |
| 2026-11-18T16:30 | VWAP momentum · 1h | sell | IWM | 14.04 | -0.06 | exit signal |
| 2026-11-18T16:30 | Heikin-Ashi · 1h | buy | AMZN | 17.24 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 17:28:05.000134+00:00 -> 2026-11-18 17:38:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 17:28:05.000134+00:00 -> 2026-11-18 17:38:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
