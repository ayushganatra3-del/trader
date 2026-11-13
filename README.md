# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T16:10:05.000127+00:00 · 58391 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.30 (-14.70%)

Closed trades 193, win rate 35.2%, fees £5.61, max drawdown -15.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 17.18 | +0.17 |
| TQQQ | 17.03 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 20538 decisions in 2628 calls, $0.2673 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T16:10 | 15 / 11 / 4 | cash |  |
| Breezy | 2026-11-13T16:10 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-13T16:10 | 8 / 20 / 2 | BITX 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.59 | +2.90% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.57 | 17.57 | 0 | — | 15.32 | 5.11 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 117.19 | 17.19 | 34 | 29.4 | 26.04 | 3.60 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.09 | 14.09 | 22 | 68.2 | 17.87 | 3.60 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.57 | 6.57 | 32 | 43.8 | 6.78 | 1.63 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.77 | 4.77 | 0 | — | 7.03 | 1.91 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.62 | 1.62 | 141 | 34.8 | 8.28 | 3.23 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.57 | -2.43 | 0 | — | -1.09 | -0.30 | -6.18 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.97 | -4.03 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 95.86 | -4.14 | 1 | 0.0 | -4.01 | -2.44 | -6.65 | 2 |
| 14 | Agent (rotation) | meta | 95.51 | -4.49 | 191 | 30.4 | -3.26 | -1.09 | -8.69 | 161 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.34 | -5.66 | 43 | 39.5 | -4.82 | -0.89 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.87 | -7.13 | 0 | — | -5.37 | -1.44 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.77 | -8.23 | 110 | 22.7 | -14.59 | -5.33 | -17.58 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.60 | -2.56 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 86.12 | -13.88 | 433 | 33.3 | -9.85 | -3.10 | -14.11 | 603 |
| 24 | Daily: Bullish score | daily | 86.02 | -13.98 | 16 | 18.8 | -9.75 | -1.53 | -19.56 | 15 |
| 25 | Agent | meta | 85.30 | -14.70 | 193 | 35.2 | -15.92 | -7.87 | -16.40 | 214 |
| 26 | Parabolic SAR · 1h | trend | 85.10 | -14.90 | 175 | 28.6 | -15.61 | -3.37 | -22.40 | 217 |
| 27 | Agent (aggressive) | meta | 83.70 | -16.30 | 94 | 34.0 | -19.24 | -5.30 | -20.17 | 102 |
| 28 | Donchian 55/20 · 1h | breakout | 81.65 | -18.35 | 73 | 13.7 | -23.23 | -4.84 | -30.61 | 90 |
| 29 | Hold BTC | benchmark | 81.01 | -18.99 | 1 | 0.0 | -11.35 | -1.57 | -22.00 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.62 | -19.38 | 211 | 40.3 | -18.11 | -6.37 | -18.30 | 114 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 32 | Keltner breakout · 1h | breakout | 80.46 | -19.54 | 120 | 25.8 | -16.48 | -3.30 | -25.32 | 169 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 79.91 | -20.09 | 2 | 0.0 | -10.68 | -1.24 | -24.16 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 78.73 | -21.27 | 302 | 47.4 | -26.91 | -3.98 | -28.24 | 392 |
| 35 | Opening range 15m | breakout | 78.53 | -21.47 | 526 | 31.2 | -17.14 | -4.58 | -21.36 | 719 |
| 36 | MFI reversion · 1h | reversion | 76.98 | -23.02 | 395 | 35.2 | -22.94 | -2.98 | -26.70 | 162 |
| 37 | ADX DI cross · 1h | trend | 76.89 | -23.11 | 198 | 19.7 | -23.73 | -3.59 | -32.07 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -44.57 | -2.84 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 41 | Heikin-Ashi · 1h | trend | 75.12 | -24.88 | 442 | 24.2 | -37.79 | -7.05 | -39.26 | 660 |
| 42 | MACD cross · 1h | trend | 74.65 | -25.35 | 384 | 23.4 | -29.28 | -4.36 | -38.65 | 472 |
| 43 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.16 | -4.53 | -30.99 | 203 |
| 44 | Max aggression: 1-day momentum | meta | 73.23 | -26.77 | 29 | 27.6 | -21.70 | -0.71 | -57.50 | 41 |
| 45 | RSI momentum · 1h | momentum | 72.58 | -27.42 | 169 | 13.0 | -27.23 | -4.21 | -37.83 | 209 |
| 46 | Supertrend · 1h | trend | 72.51 | -27.49 | 180 | 15.0 | -30.47 | -5.22 | -36.51 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 71.95 | -28.05 | 109 | 10.1 | -29.46 | -4.99 | -40.33 | 121 |
| 48 | ROC + volume · 1h | momentum | 71.47 | -28.53 | 396 | 28.8 | -31.10 | -5.73 | -38.37 | 376 |
| 49 | Bollinger reversion · 1h | reversion | 71.28 | -28.72 | 300 | 41.3 | -33.79 | -5.29 | -35.72 | 376 |
| 50 | Triple EMA stack · 1h | trend | 71.28 | -28.72 | 150 | 14.0 | -29.08 | -4.83 | -38.47 | 205 |
| 51 | CCI reversion · 1h | reversion | 70.65 | -29.35 | 346 | 43.4 | -38.77 | -6.13 | -39.55 | 462 |
| 52 | OBV trend · 1h | momentum | 69.54 | -30.46 | 297 | 19.2 | -30.26 | -5.34 | -38.08 | 275 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -34.44 | -4.64 | -37.70 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.13 | -30.87 | 153 | 19.0 | -30.27 | -5.42 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.63 | -32.37 | 381 | 43.6 | -42.91 | -7.04 | -44.04 | 531 |
| 56 | Z-score reversion · 1h | reversion | 65.16 | -34.84 | 204 | 37.3 | -30.68 | -4.33 | -31.55 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 64.52 | -35.48 | 260 | 10.0 | -38.13 | -7.71 | -43.15 | 329 |
| 58 | Agent (ML meta-label) | meta | 63.92 | -36.08 | 1837 | 24.7 | -16.36 | -2.41 | -22.52 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 63.57 | -36.43 | 186 | 32.8 | -38.16 | -5.68 | -38.93 | 240 |
| 60 | VWAP momentum · 1h | momentum | 62.79 | -37.21 | 909 | 22.2 | -53.01 | -10.66 | -53.94 | 1217 |
| 61 | Candlestick reversal · 1h | reversion | 61.29 | -38.71 | 486 | 28.4 | -45.01 | -8.24 | -45.92 | 593 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.52 | -99.00 | 5260 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.09 | -25.67 | -80.18 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -46.38 | -93.83 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.62 | -89.31 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -41.29 | -91.31 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.77 | -31.15 | -89.77 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.45 | -97.90 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.47 | -96.27 | 3434 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.57 | -93.76 | 2343 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -34.87 | -83.21 | 1660 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -55.65 | -99.59 | 6040 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.20 | -42.80 | -92.24 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.11 | -95.40 | 3468 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.04 | -99.81 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -42.83 | -92.30 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.90 | -25.93 | -76.07 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -60.42 | -97.64 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -64.05 | -98.91 | 4948 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.61 | -26.86 | -68.79 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -56.86 | -94.74 | 2784 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.04 | -39.05 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.87 | -99.67 | 6385 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.17 | -32.71 | -90.22 | 2329 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.93 | -20.15 | -79.03 | 1802 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.01 | -36.98 | -91.06 | 2194 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.04 | -52.17 | -97.06 | 3895 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -58.30 | -89.42 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.82 | -31.07 | -66.82 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.36 | -22.98 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.58 | -19.24 | -80.72 | 1756 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.42 | -51.01 | -97.44 | 4354 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -110.25 | -99.93 | 8386 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T16:10 | Agent (aggressive) | sell | TSLA | 41.78 | 0.24 | selected signal exited |
| 2026-11-13T16:10 | Agent | sell | TSLA | 17.11 | 0.10 | selected signal exited |
| 2026-11-13T16:05 | Agent (ML meta-label) | sell | GOOGL | 6.28 | -0.02 | selected signal exited |
| 2026-11-13T16:00 | Agent (ML meta-label) | buy | GOOGL | 6.30 | — | entry |
| 2026-11-13T16:00 | OBV trend · 1h | sell | AMD | 17.34 | -0.09 | target is flat |
| 2026-11-13T16:00 | Heikin-Ashi · 1h | sell | SOL-USD | 18.54 | -0.29 | exit signal |
| 2026-11-13T16:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 19.12 | -0.11 | exit signal |
| 2026-11-13T15:55 | Agent (ML meta-label) | buy | TECL | 12.80 | — | entry |
| 2026-11-13T15:55 | Agent (ML meta-label) | sell | GOOGL | 12.74 | -0.07 | selected signal exited |
| 2026-11-13T15:55 | MFI reversion · 1h | buy | TECL | 18.67 | — | entry |
| 2026-11-13T15:50 | Agent | buy | TQQQ | 17.05 | — | following Z-score reversion |
| 2026-11-13T15:50 | Opening range 30m | buy | MSFT | 21.54 | — | entry signal |
| 2026-11-13T15:40 | Candlestick reversal · 1h | buy | ETH-USD | 5.27 | — | rebalance up |
| 2026-11-13T15:40 | Candlestick reversal · 1h | buy | BTC-USD | 5.17 | — | rebalance up |
| 2026-11-13T15:40 | Candlestick reversal · 1h | sell | XRP-USD | 9.99 | -0.30 | stop-loss |
| 2026-11-13T15:40 | Candlestick reversal · 1h | sell | SQQQ | 10.81 | 0.74 | take-profit |
| 2026-11-13T15:40 | ADX DI cross · 1h | sell | DOGE-USD | 19.01 | -0.55 | stop-loss |
| 2026-11-13T15:40 | MACD cross · 1h | buy | SOL-USD | 4.19 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | buy | DOGE-USD | 4.97 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | buy | BTC-USD | 4.88 | — | rebalance up |
| 2026-11-13T15:40 | MACD cross · 1h | sell | ETH-USD | 10.54 | -0.25 | stop-loss |
| 2026-11-13T15:35 | VWAP momentum · 1h | buy | XRP-USD | 3.10 | — | rebalance up |
| 2026-11-13T15:35 | MACD cross · 1h | buy | ETH-USD | 3.72 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | buy | GOOGL | 11.25 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | buy | AAPL | 3.68 | — | rebalance up |
| 2026-11-13T15:30 | Agent (ML meta-label) | sell | TECL | 10.61 | -0.51 | selected signal exited |
| 2026-11-13T15:30 | Agent (ML meta-label) | sell | AMD | 10.67 | -0.31 | selected signal exited |
| 2026-11-13T15:30 | CCI reversion · 1h | buy | META | 8.81 | — | entry signal |
| 2026-11-13T15:30 | Williams %R · 1h | buy | META | 3.88 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | ETH-USD | 4.03 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | BTC-USD | 3.93 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | buy | AMZN | 3.91 | — | rebalance up |
| 2026-11-13T15:30 | Williams %R · 1h | sell | SQQQ | 10.11 | 0.44 | exit signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | buy | TNA | 5.60 | — | entry signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | buy | IWM | 13.09 | — | entry signal |
| 2026-11-13T15:30 | Stochastic reversion · 1h | sell | SQQQ | 12.69 | 0.94 | exit signal |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | NVDA | 3.53 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | ETH-USD | 3.36 | — | rebalance up |
| 2026-11-13T15:30 | RSI(14) reversion · 1h | buy | BTC-USD | 3.23 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 16:10:05.000127+00:00 -> 2026-11-13 16:20:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
