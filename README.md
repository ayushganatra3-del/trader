# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T18:10:05.000115+00:00 · 57213 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.87 (-14.13%)

Closed trades 185, win rate 35.7%, fees £5.47, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.04 | -0.17 |

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

Today: 28415 decisions in 2861 calls, $0.3584 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T18:10 | 3 / 16 / 12 | NANC 17%, NVDA 14% |  |
| Breezy | 2026-11-12T18:10 | 0 / 27 / 4 | cash |  |
| Boozy | 2026-11-12T18:10 | 4 / 22 / 5 | COIN 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.13 | +7.31% | 5 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.16 | 17.16 | 0 | — | 15.92 | 5.23 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.85 | 13.85 | 21 | 66.7 | 20.34 | 3.98 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 33 | 27.3 | 21.37 | 3.14 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.14 | 4.14 | 0 | — | 6.32 | 1.74 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.31 | 1.31 | 137 | 33.6 | 7.84 | 3.02 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.44 | 1.83 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Hold SPY | benchmark | 98.90 | -1.10 | 0 | — | -0.64 | -0.09 | -6.18 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.86 | 0.06 | -18.69 | 5 |
| 12 | Agent (rotation) | meta | 98.55 | -1.45 | 190 | 30.5 | -2.02 | -0.68 | -9.59 | 172 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.14 | -1.86 | 1 | 0.0 | -1.80 | -1.19 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.32 | -3.68 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.57 | -4.43 | 142 | 47.2 | -12.67 | -3.28 | -13.44 | 156 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.80 | -5.20 | 0 | — | -2.85 | -0.71 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.78 | -5.22 | 43 | 39.5 | -6.70 | -1.31 | -15.11 | 67 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 94.02 | -5.98 | 1 | 0.0 | -6.23 | -1.32 | -16.91 | 2 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 91.99 | -8.01 | 109 | 22.9 | -13.72 | -4.79 | -18.42 | 75 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -7.23 | -2.29 | -14.89 | 74 |
| 23 | Parabolic SAR · 1h | trend | 86.52 | -13.48 | 171 | 27.5 | -13.31 | -2.81 | -21.98 | 222 |
| 24 | Opening range 30m | breakout | 86.49 | -13.51 | 418 | 32.8 | -9.91 | -3.12 | -14.11 | 604 |
| 25 | Agent | meta | 85.87 | -14.13 | 185 | 35.7 | -15.07 | -7.55 | -15.74 | 213 |
| 26 | Hold BTC | benchmark | 84.72 | -15.29 | 1 | 0.0 | -7.18 | -0.93 | -18.34 | 1 |
| 27 | Daily: Bullish score | daily | 84.68 | -15.32 | 16 | 18.8 | -10.34 | -1.66 | -19.56 | 15 |
| 28 | Agent (aggressive) | meta | 84.50 | -15.50 | 90 | 34.4 | -16.03 | -4.43 | -18.51 | 100 |
| 29 | Donchian 55/20 · 1h | breakout | 83.93 | -16.07 | 73 | 13.7 | -22.41 | -4.69 | -29.68 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.90 | -17.10 | 2 | 0.0 | -7.92 | -0.86 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.72 | -18.28 | 114 | 23.7 | -18.08 | -3.73 | -25.87 | 177 |
| 32 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -26.30 | -1.36 | -45.81 | 24 |
| 33 | Connors RSI(2) · 1h | reversion | 81.13 | -18.87 | 210 | 40.5 | -19.73 | -6.64 | -20.32 | 120 |
| 34 | ADX DI cross · 1h | trend | 81.11 | -18.89 | 191 | 19.4 | -21.31 | -3.38 | -29.90 | 270 |
| 35 | Volume breakout · 1h | breakout | 80.35 | -19.65 | 157 | 28.0 | -13.72 | -3.20 | -21.15 | 92 |
| 36 | MFI reversion · 1h | reversion | 80.18 | -19.82 | 379 | 36.1 | -17.92 | -2.27 | -23.02 | 166 |
| 37 | Stochastic reversion · 1h | reversion | 79.82 | -20.18 | 297 | 47.5 | -26.51 | -3.92 | -27.37 | 390 |
| 38 | Opening range 15m | breakout | 78.88 | -21.12 | 512 | 31.2 | -17.46 | -4.69 | -21.36 | 726 |
| 39 | Heikin-Ashi · 1h | trend | 77.95 | -22.05 | 431 | 24.6 | -36.10 | -6.78 | -38.20 | 658 |
| 40 | MACD cross · 1h | trend | 77.41 | -22.59 | 370 | 21.9 | -27.34 | -4.03 | -38.92 | 463 |
| 41 | Bollinger breakout · 1h | breakout | 76.32 | -23.68 | 179 | 22.3 | -22.25 | -4.62 | -29.88 | 242 |
| 42 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -20.04 | -0.59 | -57.50 | 41 |
| 43 | MACD zero-line · 1h | trend | 75.82 | -24.18 | 164 | 17.1 | -22.52 | -4.64 | -31.10 | 205 |
| 44 | Supertrend · 1h | trend | 75.70 | -24.30 | 172 | 14.0 | -29.15 | -5.22 | -36.13 | 223 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 46 | RSI momentum · 1h | momentum | 75.17 | -24.83 | 162 | 13.6 | -24.06 | -3.71 | -36.52 | 213 |
| 47 | EMA 20/50 cross · 1h | trend | 74.80 | -25.20 | 105 | 10.5 | -26.59 | -4.47 | -37.91 | 120 |
| 48 | Daily: Momentum burst | daily | 74.42 | -25.58 | 27 | 11.1 | -34.39 | -4.65 | -38.14 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.30 | -26.70 | 147 | 14.3 | -25.41 | -4.20 | -36.72 | 206 |
| 50 | ROC + volume · 1h | momentum | 73.26 | -26.74 | 385 | 27.8 | -30.72 | -5.73 | -38.31 | 376 |
| 51 | Bollinger reversion · 1h | reversion | 72.70 | -27.30 | 290 | 41.0 | -31.25 | -4.85 | -35.67 | 378 |
| 52 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -35.92 | -5.59 | -36.22 | 455 |
| 53 | Donchian 20/10 · 1h | breakout | 72.26 | -27.74 | 145 | 19.3 | -27.77 | -5.04 | -35.87 | 211 |
| 54 | OBV trend · 1h | momentum | 71.81 | -28.20 | 288 | 19.4 | -26.95 | -4.60 | -36.86 | 287 |
| 55 | Williams %R · 1h | reversion | 68.35 | -31.65 | 358 | 45.5 | -41.37 | -6.84 | -41.62 | 531 |
| 56 | Z-score reversion · 1h | reversion | 67.95 | -32.05 | 199 | 38.2 | -27.28 | -3.79 | -29.17 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 67.37 | -32.63 | 257 | 9.7 | -33.11 | -6.11 | -41.74 | 333 |
| 58 | VWAP momentum · 1h | momentum | 66.70 | -33.30 | 885 | 22.4 | -51.07 | -10.54 | -52.00 | 1218 |
| 59 | Agent (ML meta-label) | meta | 66.58 | -33.42 | 1793 | 24.9 | -14.94 | -1.84 | -21.62 | 329 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -34.28 | -4.93 | -35.23 | 238 |
| 61 | Candlestick reversal · 1h | reversion | 63.17 | -36.83 | 467 | 28.5 | -40.70 | -7.17 | -41.33 | 589 |
| 62 | Three white soldiers | momentum | 58.67 | -41.33 | 536 | 14.6 | -49.58 | -22.58 | -49.58 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.17 | -99.01 | 5275 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.08 | -26.13 | -80.08 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -46.14 | -93.68 | 2522 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.33 | -32.21 | -89.58 | 1933 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.11 | -40.88 | -91.12 | 2335 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.23 | -32.03 | -90.32 | 2210 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -54.28 | -97.88 | 3474 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.32 | -55.29 | -96.33 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.54 | -32.54 | -93.54 | 2328 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.90 | -34.01 | -82.97 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.73 | -99.57 | 5987 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -43.68 | -92.27 | 2605 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -37.16 | -95.44 | 3467 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -78.72 | -99.82 | 6146 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -43.85 | -92.25 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.11 | -25.28 | -75.19 | 1625 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -59.08 | -97.64 | 3515 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -64.08 | -98.89 | 4903 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.62 | -27.06 | -68.64 | 1238 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -58.62 | -94.79 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.11 | -39.35 | -85.15 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.87 | -99.66 | 6331 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.89 | -32.78 | -90.05 | 2298 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.90 | -20.08 | -78.42 | 1764 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -36.84 | -90.85 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.87 | -53.30 | -96.90 | 3849 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.14 | -57.98 | -89.14 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.33 | -30.43 | -66.34 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.48 | -23.15 | -71.59 | 1261 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.17 | -18.88 | -79.48 | 1713 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -49.70 | -97.31 | 4290 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -116.03 | -99.93 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-12T18:00 | MFI reversion · 1h | sell | ETH-USD | 5.31 | -0.01 | rebalance down |
| 2026-11-12T18:00 | MFI reversion · 1h | sell | DOGE-USD | 5.35 | 0.01 | rebalance down |
| 2026-11-12T18:00 | MFI reversion · 1h | sell | AMZN | 5.29 | -0.03 | rebalance down |
| 2026-11-12T18:00 | Z-score reversion · 1h | buy | XRP-USD | 10.28 | — | entry signal |
| 2026-11-12T18:00 | Z-score reversion · 1h | buy | ETH-USD | 13.60 | — | entry signal |
| 2026-11-12T18:00 | Z-score reversion · 1h | buy | DOGE-USD | 13.60 | — | entry signal |
| 2026-11-12T18:00 | Z-score reversion · 1h | sell | ETHU | 3.65 | -0.11 | rebalance down |
| 2026-11-12T18:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.69 | — | entry signal |
| 2026-11-12T17:55 | Agent (ML meta-label) | sell | UPRO | 4.17 | -0.00 | selected signal exited |
| 2026-11-12T17:55 | Agent (ML meta-label) | sell | PLTR | 4.16 | -0.01 | selected signal exited |
| 2026-11-12T17:55 | Agent | buy | AMD | 17.21 | — | following Parabolic SAR |
| 2026-11-12T17:55 | OBV trend · 1h | sell | TNA | 8.99 | -0.03 | target is flat |
| 2026-11-12T17:50 | Opening range 30m | buy | ETHU | 6.12 | — | entry signal |
| 2026-11-12T17:45 | Agent (ML meta-label) | buy | PLTR | 4.17 | — | entry |
| 2026-11-12T17:45 | Agent (ML meta-label) | sell | SPY | 3.72 | -0.01 | selected signal exited |
| 2026-11-12T17:45 | MFI reversion · 1h | buy | MSFT | 2.58 | — | entry |
| 2026-11-12T17:45 | MFI reversion · 1h | buy | META | 8.92 | — | entry |
| 2026-11-12T17:45 | MFI reversion · 1h | sell | SPY | 11.50 | 0.10 | target is flat |
| 2026-11-12T17:45 | Volume breakout · 1h | buy | AAPL | 20.08 | — | entry |
| 2026-11-12T17:45 | OBV trend · 1h | buy | SPY | 8.99 | — | entry |
| 2026-11-12T17:45 | OBV trend · 1h | sell | IWM | 6.52 | -0.02 | target is flat |
| 2026-11-12T17:45 | VWAP momentum · 1h | buy | QQQ | 7.43 | — | entry |
| 2026-11-12T17:41 | Agent (ML meta-label) | buy | UPRO | 4.17 | — | following Gap and go |
| 2026-11-12T17:40 | Agent (ML meta-label) | sell | QQQ | 4.17 | 0.00 | selected signal exited |
| 2026-11-12T17:40 | Three white soldiers | sell | BTC-USD | 14.59 | -0.14 | exit signal |
| 2026-11-12T17:40 | Three white soldiers | sell | BITX | 14.62 | -0.11 | exit signal |
| 2026-11-12T17:31 | Agent (ML meta-label) | buy | QQQ | 4.16 | — | entry |
| 2026-11-12T17:31 | Agent (ML meta-label) | sell | TNA | 3.91 | -0.00 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 18:10:05.000115+00:00 -> 2026-11-12 18:20:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
