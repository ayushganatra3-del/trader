# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T18:56:05.000132+00:00 · 64744 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.83 (-15.17%)

Closed trades 223, win rate 35.9%, fees £6.14, max drawdown -17.33%.

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

Today: 30768 decisions in 2946 calls, $0.3862 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T18:56 | 2 / 17 / 11 | cash |  |
| Breezy | 2026-11-18T18:56 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-18T18:56 | 4 / 23 / 3 | COIN 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.87 | +5.50% | 10 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.00 | 15.00 | 0 | — | 13.06 | 4.43 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.39 | 4.39 | 0 | — | 5.26 | 1.42 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.59 | 0.59 | 150 | 34.7 | -3.17 | -2.68 | -4.83 | 70 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 99.99 | -0.01 | 196 | 32.7 | 7.96 | 2.22 | -9.06 | 214 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 97.07 | -2.93 | 8 | 50.0 | -3.48 | -0.05 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 96.00 | -4.00 | 0 | — | -3.91 | -1.27 | -6.91 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 201 | 29.9 | -4.20 | -1.48 | -8.74 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.34 | -8.39 | -5.93 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.47 | -7.53 | 0 | — | -7.36 | -1.94 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Congress Democrats (NANC) | copy | 91.15 | -8.85 | 0 | — | -7.49 | -2.01 | -12.67 | 1 |
| 18 | Copy: Insider buying | copy | 91.14 | -8.86 | 52 | 40.4 | -9.38 | -1.88 | -14.79 | 64 |
| 19 | Trend pullback · 1h | trend | 90.13 | -9.87 | 113 | 23.9 | -12.71 | -7.01 | -12.99 | 57 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -11.42 | -3.36 | -18.48 | 147 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 86.93 | -13.07 | 17 | 17.6 | -5.44 | -0.87 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.03 | -8.99 | -16.08 | 70 |
| 24 | Opening range 30m | breakout | 85.15 | -14.85 | 443 | 33.4 | -10.36 | -3.28 | -14.63 | 566 |
| 25 | Agent | meta | 84.83 | -15.17 | 223 | 35.9 | -15.16 | -7.36 | -17.06 | 201 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 104 | 33.7 | -15.70 | -4.17 | -19.74 | 97 |
| 27 | Parabolic SAR · 1h | trend | 81.73 | -18.27 | 188 | 28.2 | -24.27 | -6.71 | -27.42 | 200 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.42 | -6.42 | -14.74 | 86 |
| 29 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -15.63 | -5.02 | -21.17 | 77 |
| 30 | Keltner breakout · 1h | breakout | 79.68 | -20.32 | 124 | 25.8 | -25.27 | -6.80 | -27.46 | 155 |
| 31 | Donchian 55/20 · 1h | breakout | 79.09 | -20.91 | 78 | 12.8 | -25.38 | -6.67 | -30.57 | 84 |
| 32 | Max aggression: 5-day momentum | meta | 78.47 | -21.53 | 21 | 42.9 | -48.43 | -3.25 | -55.24 | 21 |
| 33 | Opening range 15m | breakout | 77.88 | -22.12 | 536 | 31.5 | -16.84 | -4.55 | -21.54 | 676 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.59 | -22.41 | 2 | 0.0 | -17.63 | -2.33 | -26.43 | 1 |
| 35 | ADX DI cross · 1h | trend | 75.17 | -24.83 | 209 | 19.1 | -27.22 | -4.46 | -35.44 | 269 |
| 36 | Ichimoku · 1h | trend | 74.10 | -25.90 | 104 | 14.4 | -29.30 | -8.54 | -30.36 | 110 |
| 37 | Hold BTC | benchmark | 74.05 | -25.95 | 2 | 0.0 | -17.79 | -2.49 | -28.91 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 73.40 | -26.60 | 350 | 42.3 | -33.85 | -5.12 | -35.58 | 426 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -31.09 | -8.37 | -34.18 | 218 |
| 40 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -39.02 | -2.37 | -57.50 | 39 |
| 41 | Supertrend · 1h | trend | 71.70 | -28.30 | 191 | 16.2 | -32.28 | -5.45 | -39.50 | 202 |
| 42 | MFI reversion · 1h | reversion | 70.94 | -29.06 | 447 | 33.6 | -26.73 | -3.94 | -30.08 | 172 |
| 43 | Triple EMA stack · 1h | trend | 70.78 | -29.22 | 156 | 14.7 | -30.79 | -6.15 | -36.85 | 177 |
| 44 | RSI momentum · 1h | momentum | 70.17 | -29.82 | 179 | 14.5 | -31.41 | -5.68 | -38.17 | 199 |
| 45 | MACD zero-line · 1h | trend | 69.83 | -30.17 | 184 | 17.9 | -27.83 | -5.56 | -33.94 | 202 |
| 46 | Heikin-Ashi · 1h | trend | 69.66 | -30.34 | 474 | 23.0 | -44.91 | -9.88 | -45.84 | 633 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | EMA 20/50 cross · 1h | trend | 69.32 | -30.68 | 116 | 10.3 | -36.31 | -9.36 | -40.28 | 117 |
| 49 | ROC + volume · 1h | momentum | 68.67 | -31.33 | 413 | 28.1 | -33.86 | -6.19 | -39.37 | 342 |
| 50 | OBV trend · 1h | momentum | 68.17 | -31.83 | 310 | 19.4 | -35.04 | -7.50 | -39.78 | 253 |
| 51 | MACD cross · 1h | trend | 68.13 | -31.87 | 417 | 22.3 | -40.12 | -6.57 | -46.29 | 491 |
| 52 | CCI reversion · 1h | reversion | 67.63 | -32.37 | 386 | 41.5 | -41.88 | -7.01 | -44.29 | 474 |
| 53 | Donchian 20/10 · 1h | breakout | 66.39 | -33.61 | 162 | 17.9 | -36.87 | -7.04 | -41.48 | 199 |
| 54 | Bollinger reversion · 1h | reversion | 64.22 | -35.78 | 348 | 37.9 | -38.44 | -5.83 | -39.58 | 417 |
| 55 | Williams %R · 1h | reversion | 64.05 | -35.95 | 436 | 40.6 | -46.42 | -8.09 | -47.60 | 572 |
| 56 | EMA 9/21 cross · 1h | trend | 62.94 | -37.06 | 284 | 11.3 | -40.30 | -7.88 | -46.26 | 322 |
| 57 | Agent (ML meta-label) | meta | 60.35 | -39.65 | 1928 | 24.6 | -19.17 | -3.35 | -22.33 | 304 |
| 58 | RSI(14) reversion · 1h | reversion | 59.36 | -40.64 | 206 | 32.0 | -41.11 | -6.10 | -43.36 | 254 |
| 59 | Z-score reversion · 1h | reversion | 58.03 | -41.97 | 227 | 35.2 | -36.30 | -4.99 | -39.63 | 257 |
| 60 | VWAP momentum · 1h | momentum | 55.61 | -44.39 | 976 | 21.7 | -55.89 | -11.11 | -59.89 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 55.59 | -44.41 | 552 | 26.4 | -47.17 | -8.63 | -48.93 | 642 |
| 62 | Three white soldiers | momentum | 54.75 | -45.25 | 588 | 14.5 | -49.66 | -21.86 | -50.71 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.96 | -99.03 | 5281 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.35 | -25.55 | -82.56 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -41.98 | -93.97 | 2461 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.86 | -31.49 | -90.31 | 1946 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.96 | -38.06 | -91.46 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -31.00 | -90.12 | 2089 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -47.78 | -97.92 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -52.80 | -96.42 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.51 | -38.91 | -93.54 | 2202 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.41 | -34.36 | -82.79 | 1590 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.98 | -99.61 | 6102 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.84 | -42.88 | -92.15 | 2549 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.81 | -39.12 | -94.83 | 3236 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.92 | -99.81 | 6197 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.35 | -42.58 | -92.64 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.83 | -26.75 | -76.29 | 1650 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -61.45 | -97.72 | 3436 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.06 | -58.47 | -99.07 | 4966 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -28.96 | -70.15 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -56.43 | -94.67 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -37.70 | -85.07 | 1736 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.99 | -99.70 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.86 | -31.34 | -91.03 | 2362 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.18 | -19.05 | -80.59 | 1846 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.43 | -36.86 | -91.57 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.58 | -46.58 | -97.60 | 3916 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -59.11 | -89.29 | 2158 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.30 | -30.77 | -67.06 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.61 | -24.32 | -73.12 | 1218 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.48 | -18.36 | -81.88 | 1767 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -46.35 | -97.60 | 4323 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -114.69 | -99.94 | 8460 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | TSLA | 1.45 | — | following Stochastic reversion |
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | TNA | 6.04 | — | entry |
| 2026-11-18T18:56 | Agent (ML meta-label) | buy | AAPL | 6.04 | — | entry |
| 2026-11-18T18:50 | Agent (ML meta-label) | sell | TNA | 7.54 | 0.02 | selected signal exited |
| 2026-11-18T18:50 | Agent (ML meta-label) | sell | ETHU | 5.98 | -0.01 | selected signal exited |
| 2026-11-18T18:46 | Agent (ML meta-label) | buy | ETHU | 5.99 | — | entry |
| 2026-11-18T18:37 | Copy: Insider buying | buy | STWD | 7.78 | — | rebalance up |
| 2026-11-18T18:37 | Copy: Insider buying | buy | PEPG | 11.38 | — | entry |
| 2026-11-18T18:37 | Copy: Insider buying | sell | PAM | 8.65 | -0.07 | target is flat |
| 2026-11-18T18:37 | Copy: Insider buying | sell | HUBS | 10.51 | -0.83 | target is flat |
| 2026-11-18T18:30 | Agent (ML meta-label) | buy | TNA | 7.52 | — | entry |
| 2026-11-18T18:30 | Keltner breakout · 1h | buy | AMZN | 19.96 | — | entry signal |
| 2026-11-18T18:30 | VWAP momentum · 1h | buy | MSFT | 4.16 | — | entry signal |
| 2026-11-18T18:30 | VWAP momentum · 1h | sell | SOXL | 4.16 | -0.13 | exit signal |
| 2026-11-18T18:30 | Trend pullback · 1h | buy | SQQQ | 22.58 | — | entry signal |
| 2026-11-18T18:27 | Agent (ML meta-label) | sell | TNA | 6.73 | 0.04 | selected signal exited |
| 2026-11-18T18:25 | MFI reversion · 1h | buy | TNA | 5.89 | — | entry |
| 2026-11-18T18:25 | MFI reversion · 1h | sell | ETHU | 5.91 | -0.03 | target is flat |
| 2026-11-18T18:15 | Agent (ML meta-label) | sell | AAPL | 6.01 | -0.01 | selected signal exited |
| 2026-11-18T18:10 | Agent | sell | SPY | 16.91 | -0.07 | selected signal exited |
| 2026-11-18T18:00 | Agent (ML meta-label) | buy | AAPL | 6.02 | — | entry |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | ETH-USD | 4.70 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | DOGE-USD | 5.89 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | buy | BTC-USD | 5.89 | — | entry signal |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | MSTR | 7.08 | -0.01 | target is flat |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | MSFT | 4.25 | -0.00 | rebalance down |
| 2026-11-18T18:00 | MFI reversion · 1h | sell | ETHU | 4.17 | -0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | SOL-USD | 7.11 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | ETH-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | DOGE-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | buy | BTC-USD | 7.12 | — | entry signal |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | UPRO | 5.64 | -0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | TNA | 5.68 | 0.03 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | SPY | 5.71 | -0.00 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | MSFT | 5.74 | -0.01 | rebalance down |
| 2026-11-18T18:00 | Bollinger reversion · 1h | sell | IWM | 5.72 | 0.02 | rebalance down |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | UPRO | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | SPY | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | PLTR | 3.94 | — | entry |
| 2026-11-18T18:00 | RSI(14) reversion · 1h | buy | ETH-USD | 3.94 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 18:56:05.000132+00:00 -> 2026-11-18 19:06:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 18:56:05.000132+00:00 -> 2026-11-18 19:06:05.000132+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
