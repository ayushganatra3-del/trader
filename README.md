# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T18:40:05.000152+00:00 · 57241 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.96 (-14.04%)

Closed trades 185, win rate 35.7%, fees £5.47, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.13 | -0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 30926 decisions in 2945 calls, $0.3878 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T18:40 | 4 / 16 / 10 | cash |  |
| Breezy | 2026-11-12T18:40 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-12T18:40 | 5 / 23 / 2 | ETHU 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| MFI reversion | LABU | 1.71 | +6.40% | 5 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.19 | 17.18 | 0 | — | 15.79 | 5.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.32 | 14.32 | 21 | 66.7 | 20.73 | 4.04 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 113.42 | 13.42 | 33 | 27.3 | 21.77 | 3.18 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.42 | 4.42 | 0 | — | 6.51 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.59 | 1.59 | 137 | 33.6 | 8.06 | 3.07 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.83 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold SPY | benchmark | 99.00 | -1.00 | 0 | — | -0.64 | -0.09 | -6.18 | 1 |
| 11 | Agent (rotation) | meta | 98.83 | -1.17 | 190 | 30.5 | -1.09 | -0.33 | -8.93 | 169 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.72 | 0.06 | -18.69 | 5 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.33 | -1.67 | 1 | 0.0 | -1.69 | -1.11 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.41 | -3.59 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.68 | -4.32 | 142 | 47.2 | -12.61 | -3.26 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.00 | -5.00 | 43 | 39.5 | -6.57 | -1.28 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.70 | -5.30 | 0 | — | -3.04 | -0.77 | -10.64 | 1 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 94.42 | -5.58 | 1 | 0.0 | -5.93 | -1.23 | -16.91 | 2 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.13 | -7.87 | 109 | 22.9 | -13.09 | -4.55 | -17.88 | 74 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.23 | -2.29 | -14.89 | 74 |
| 23 | Opening range 30m | breakout | 86.78 | -13.22 | 418 | 32.8 | -9.69 | -3.02 | -14.11 | 604 |
| 24 | Parabolic SAR · 1h | trend | 86.65 | -13.35 | 171 | 27.5 | -13.24 | -2.79 | -21.98 | 222 |
| 25 | Agent | meta | 85.96 | -14.04 | 185 | 35.7 | -14.63 | -7.24 | -15.72 | 212 |
| 26 | Hold BTC | benchmark | 84.82 | -15.18 | 1 | 0.0 | -7.26 | -0.93 | -18.34 | 1 |
| 27 | Daily: Bullish score | daily | 84.75 | -15.25 | 16 | 18.8 | -10.78 | -1.65 | -19.56 | 15 |
| 28 | Agent (aggressive) | meta | 84.50 | -15.50 | 90 | 34.4 | -16.50 | -4.54 | -18.79 | 102 |
| 29 | Donchian 55/20 · 1h | breakout | 84.14 | -15.86 | 73 | 13.7 | -22.28 | -4.65 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.08 | -16.92 | 2 | 0.0 | -7.87 | -0.84 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.90 | -18.10 | 114 | 23.7 | -17.73 | -3.66 | -25.87 | 176 |
| 32 | ADX DI cross · 1h | trend | 81.59 | -18.41 | 191 | 19.4 | -20.61 | -3.34 | -29.55 | 268 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -25.26 | -1.28 | -45.81 | 24 |
| 34 | Connors RSI(2) · 1h | reversion | 81.14 | -18.86 | 210 | 40.5 | -19.33 | -6.49 | -19.92 | 120 |
| 35 | MFI reversion · 1h | reversion | 80.53 | -19.48 | 379 | 36.1 | -17.72 | -2.24 | -23.02 | 165 |
| 36 | Volume breakout · 1h | breakout | 80.43 | -19.57 | 157 | 28.0 | -13.67 | -3.19 | -21.15 | 92 |
| 37 | Stochastic reversion · 1h | reversion | 79.92 | -20.08 | 297 | 47.5 | -26.09 | -3.83 | -27.07 | 390 |
| 38 | Opening range 15m | breakout | 79.16 | -20.84 | 512 | 31.2 | -17.26 | -4.61 | -21.36 | 726 |
| 39 | Heikin-Ashi · 1h | trend | 77.98 | -22.02 | 432 | 24.8 | -35.78 | -6.70 | -38.20 | 658 |
| 40 | MACD cross · 1h | trend | 77.63 | -22.36 | 370 | 21.9 | -27.67 | -4.18 | -38.74 | 464 |
| 41 | Bollinger breakout · 1h | breakout | 76.55 | -23.45 | 179 | 22.3 | -22.09 | -4.59 | -29.88 | 242 |
| 42 | MACD zero-line · 1h | trend | 76.09 | -23.91 | 164 | 17.1 | -21.16 | -4.11 | -30.95 | 204 |
| 43 | Supertrend · 1h | trend | 76.00 | -24.00 | 172 | 14.0 | -27.62 | -4.84 | -35.51 | 218 |
| 44 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -19.66 | -0.57 | -57.50 | 41 |
| 45 | RSI momentum · 1h | momentum | 75.41 | -24.59 | 162 | 13.6 | -23.83 | -3.66 | -36.52 | 213 |
| 46 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 47 | EMA 20/50 cross · 1h | trend | 74.99 | -25.01 | 105 | 10.5 | -26.59 | -4.47 | -37.99 | 122 |
| 48 | Daily: Momentum burst | daily | 74.79 | -25.21 | 27 | 11.1 | -34.13 | -4.60 | -38.12 | 33 |
| 49 | ROC + volume · 1h | momentum | 73.56 | -26.44 | 385 | 27.8 | -30.31 | -5.56 | -38.31 | 377 |
| 50 | Triple EMA stack · 1h | trend | 73.51 | -26.49 | 147 | 14.3 | -25.07 | -4.14 | -36.53 | 205 |
| 51 | Bollinger reversion · 1h | reversion | 72.86 | -27.14 | 290 | 41.0 | -31.21 | -4.85 | -35.71 | 378 |
| 52 | Donchian 20/10 · 1h | breakout | 72.56 | -27.44 | 145 | 19.3 | -27.58 | -4.99 | -35.89 | 211 |
| 53 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -35.86 | -5.59 | -36.20 | 456 |
| 54 | OBV trend · 1h | momentum | 71.97 | -28.02 | 288 | 19.4 | -26.10 | -4.45 | -36.23 | 289 |
| 55 | Williams %R · 1h | reversion | 68.48 | -31.52 | 358 | 45.5 | -41.78 | -6.87 | -42.13 | 530 |
| 56 | Z-score reversion · 1h | reversion | 68.15 | -31.85 | 199 | 38.2 | -27.13 | -3.77 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.56 | -32.44 | 257 | 9.7 | -32.94 | -6.07 | -41.74 | 333 |
| 58 | VWAP momentum · 1h | momentum | 66.93 | -33.07 | 885 | 22.4 | -50.99 | -10.51 | -51.92 | 1218 |
| 59 | Agent (ML meta-label) | meta | 66.77 | -33.23 | 1799 | 25.0 | -12.44 | -1.61 | -20.82 | 339 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -33.35 | -4.71 | -35.23 | 239 |
| 61 | Candlestick reversal · 1h | reversion | 63.25 | -36.75 | 467 | 28.5 | -40.41 | -7.14 | -41.07 | 589 |
| 62 | Three white soldiers | momentum | 58.67 | -41.33 | 536 | 14.6 | -49.58 | -22.58 | -49.58 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.09 | -99.02 | 5271 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.11 | -26.15 | -80.14 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -46.29 | -93.71 | 2529 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -32.27 | -89.60 | 1934 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.10 | -40.83 | -91.12 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.17 | -31.89 | -90.27 | 2215 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -54.26 | -97.88 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -55.62 | -96.33 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -32.33 | -93.48 | 2321 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.93 | -34.10 | -82.98 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.71 | -99.57 | 5993 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.71 | -92.22 | 2606 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.01 | -95.43 | 3462 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -79.16 | -99.82 | 6142 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -44.25 | -92.30 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.22 | -25.28 | -75.22 | 1626 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -58.70 | -97.64 | 3511 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -64.02 | -98.89 | 4909 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.33 | -26.97 | -68.40 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -58.45 | -94.75 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.09 | -39.32 | -85.12 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.84 | -99.65 | 6331 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.84 | -32.78 | -90.01 | 2296 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.10 | -20.05 | -78.65 | 1768 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.70 | -36.79 | -90.89 | 2193 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -53.24 | -96.90 | 3848 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -58.07 | -89.16 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.25 | -30.36 | -66.25 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.55 | -23.20 | -71.67 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.04 | -18.89 | -79.36 | 1707 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.67 | -97.31 | 4292 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -116.68 | -99.93 | 8363 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T18:40 | Agent (ML meta-label) | sell | TSLA | 1.90 | -0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | buy | IWM | 4.18 | — | entry |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | UPRO | 3.60 | 0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | PLTR | 3.71 | 0.00 | selected signal exited |
| 2026-11-12T18:35 | Agent (ML meta-label) | sell | AAPL | 3.70 | -0.02 | selected signal exited |
| 2026-11-12T18:30 | Agent (ML meta-label) | buy | UPRO | 3.60 | — | following Gap and go |
| 2026-11-12T18:30 | Agent (ML meta-label) | buy | PLTR | 3.71 | — | entry |
| 2026-11-12T18:30 | Candlestick reversal · 1h | buy | NVDA | 4.95 | — | entry signal |
| 2026-11-12T18:30 | Candlestick reversal · 1h | buy | META | 5.75 | — | entry |
| 2026-11-12T18:30 | Candlestick reversal · 1h | buy | LABU | 5.75 | — | entry signal |
| 2026-11-12T18:30 | Candlestick reversal · 1h | sell | SQQQ | 3.30 | 0.04 | rebalance down |
| 2026-11-12T18:30 | Candlestick reversal · 1h | sell | SOL-USD | 3.24 | 0.01 | rebalance down |
| 2026-11-12T18:30 | Candlestick reversal · 1h | sell | ETHU | 3.37 | 0.00 | rebalance down |
| 2026-11-12T18:30 | Candlestick reversal · 1h | sell | ETH-USD | 3.30 | 0.02 | rebalance down |
| 2026-11-12T18:30 | Candlestick reversal · 1h | sell | BTC-USD | 3.25 | -0.00 | rebalance down |
| 2026-11-12T18:30 | OBV trend · 1h | buy | TQQQ | 8.99 | — | entry signal |
| 2026-11-12T18:30 | Heikin-Ashi · 1h | buy | AMD | 19.49 | — | entry signal |
| 2026-11-12T18:30 | Heikin-Ashi · 1h | sell | AAPL | 19.63 | 0.02 | exit signal |
| 2026-11-12T18:30 | EMA 20/50 cross · 1h | buy | UPRO | 2.85 | — | rebalance up |
| 2026-11-12T18:30 | EMA 20/50 cross · 1h | buy | TQQQ | 10.71 | — | entry signal |
| 2026-11-12T18:30 | EMA 20/50 cross · 1h | sell | TSLA | 4.31 | 0.00 | rebalance down |
| 2026-11-12T18:30 | EMA 20/50 cross · 1h | sell | SPY | 4.23 | 0.01 | rebalance down |
| 2026-11-12T18:30 | EMA 20/50 cross · 1h | sell | AMD | 5.03 | 0.66 | rebalance down |
| 2026-11-12T18:20 | Agent (ML meta-label) | sell | UPRO | 3.60 | -0.00 | selected signal exited |
| 2026-11-12T18:20 | Agent (ML meta-label) | sell | PLTR | 3.70 | 0.00 | selected signal exited |
| 2026-11-12T18:15 | Agent (ML meta-label) | buy | UPRO | 3.60 | — | following Gap and go |
| 2026-11-12T18:15 | Agent (ML meta-label) | buy | QQQ | 3.70 | — | entry |
| 2026-11-12T18:15 | Agent (ML meta-label) | buy | PLTR | 3.70 | — | entry |
| 2026-11-12T18:05 | Agent (ML meta-label) | sell | PLTR | 3.91 | -0.01 | selected signal exited |
| 2026-11-12T18:05 | Agent (ML meta-label) | sell | IWM | 3.92 | -0.01 | selected signal exited |
| 2026-11-12T18:00 | Agent (ML meta-label) | buy | PLTR | 3.92 | — | entry |
| 2026-11-12T18:00 | Agent (ML meta-label) | buy | IWM | 3.92 | — | entry |
| 2026-11-12T18:00 | Agent (ML meta-label) | buy | ETHU | 3.92 | — | entry |
| 2026-11-12T18:00 | MFI reversion · 1h | buy | XRP-USD | 1.72 | — | rebalance up |
| 2026-11-12T18:00 | MFI reversion · 1h | buy | SOXL | 6.18 | — | entry |
| 2026-11-12T18:00 | MFI reversion · 1h | buy | LABU | 6.18 | — | entry |
| 2026-11-12T18:00 | MFI reversion · 1h | buy | ETHU | 6.18 | — | entry |
| 2026-11-12T18:00 | MFI reversion · 1h | buy | BTC-USD | 6.18 | — | entry signal |
| 2026-11-12T18:00 | MFI reversion · 1h | sell | TECL | 5.24 | 0.24 | rebalance down |
| 2026-11-12T18:00 | MFI reversion · 1h | sell | SOL-USD | 5.24 | -0.03 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 18:40:05.000152+00:00 -> 2026-11-12 18:50:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
