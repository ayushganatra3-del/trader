# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T14:40:05.000120+00:00 · 57035 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

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

Today: 12396 decisions in 2331 calls, $0.1714 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T14:40 | 3 / 18 / 9 | AMD 19%, AMZN 15% |  |
| Breezy | 2026-11-12T14:40 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-12T14:40 | 5 / 24 / 1 | COIN 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.44 | 16.44 | 0 | — | 16.04 | 5.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.21 | 12.21 | 21 | 66.7 | 17.83 | 3.59 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.32 | 11.32 | 33 | 27.3 | 19.86 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.22 | 4.22 | 0 | — | 6.61 | 1.82 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.35 | 0.35 | 191 | 33.0 | 6.36 | 1.81 | -9.06 | 232 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.66 | -0.34 | 134 | 34.3 | 6.16 | 2.47 | -3.49 | 89 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.29 | 0.06 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.30 | -1.70 | 0 | — | -1.20 | -0.24 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.57 | -2.42 | 188 | 30.3 | -2.15 | -0.76 | -8.93 | 168 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.54 | -2.46 | 1 | 0.0 | -2.20 | -1.52 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.84 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 95.59 | -4.41 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 16 | VWAP reversion · 1h | reversion | 95.53 | -4.47 | 142 | 47.2 | -12.77 | -3.31 | -13.44 | 155 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.50 | -5.50 | 0 | — | -3.37 | -0.85 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 92.67 | -7.33 | 1 | 0.0 | -7.40 | -1.65 | -16.91 | 2 |
| 21 | Trend pullback · 1h | trend | 92.27 | -7.73 | 109 | 22.9 | -14.17 | -4.98 | -18.42 | 76 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -8.27 | -2.89 | -14.89 | 75 |
| 23 | Parabolic SAR · 1h | trend | 86.58 | -13.42 | 168 | 26.8 | -13.33 | -2.82 | -21.98 | 220 |
| 24 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 25 | Opening range 30m | breakout | 85.46 | -14.54 | 417 | 32.9 | -10.88 | -3.50 | -14.11 | 589 |
| 26 | Max aggression: 5-day momentum | meta | 85.32 | -14.68 | 19 | 47.4 | -27.53 | -1.46 | -45.81 | 24 |
| 27 | Daily: Bullish score | daily | 85.08 | -14.92 | 16 | 18.8 | -12.47 | -1.55 | -19.56 | 15 |
| 28 | Hold BTC | benchmark | 84.85 | -15.15 | 1 | 0.0 | -8.56 | -0.88 | -17.75 | 1 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.26 | -15.74 | 2 | 0.0 | -6.49 | -0.62 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 83.53 | -16.47 | 73 | 13.7 | -22.35 | -4.70 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 81.50 | -18.50 | 186 | 18.8 | -22.33 | -3.82 | -30.08 | 280 |
| 33 | Keltner breakout · 1h | breakout | 80.95 | -19.05 | 114 | 23.7 | -19.37 | -4.04 | -25.52 | 173 |
| 34 | Connors RSI(2) · 1h | reversion | 80.91 | -19.09 | 209 | 40.2 | -20.28 | -6.81 | -20.74 | 121 |
| 35 | Volume breakout · 1h | breakout | 80.59 | -19.41 | 154 | 27.3 | -13.97 | -3.26 | -21.82 | 91 |
| 36 | Stochastic reversion · 1h | reversion | 80.05 | -19.95 | 294 | 48.0 | -25.55 | -3.79 | -27.05 | 393 |
| 37 | MFI reversion · 1h | reversion | 79.41 | -20.59 | 376 | 35.6 | -18.42 | -2.35 | -23.02 | 159 |
| 38 | Heikin-Ashi · 1h | trend | 78.63 | -21.37 | 430 | 24.7 | -35.82 | -6.68 | -38.20 | 656 |
| 39 | Opening range 15m | breakout | 78.31 | -21.69 | 511 | 31.3 | -18.14 | -4.93 | -21.11 | 710 |
| 40 | Max aggression: 1-day momentum | meta | 77.79 | -22.21 | 28 | 28.6 | -21.04 | -0.65 | -57.50 | 41 |
| 41 | MACD cross · 1h | trend | 76.98 | -23.02 | 368 | 22.0 | -29.42 | -4.30 | -39.89 | 464 |
| 42 | Bollinger breakout · 1h | breakout | 76.18 | -23.82 | 179 | 22.3 | -23.00 | -4.82 | -29.75 | 241 |
| 43 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 44 | MACD zero-line · 1h | trend | 75.35 | -24.65 | 162 | 16.7 | -20.82 | -3.94 | -30.73 | 209 |
| 45 | Supertrend · 1h | trend | 75.26 | -24.75 | 168 | 13.1 | -27.88 | -4.79 | -36.28 | 220 |
| 46 | RSI momentum · 1h | momentum | 74.67 | -25.33 | 160 | 12.5 | -24.88 | -3.85 | -36.25 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 74.15 | -25.85 | 105 | 10.5 | -27.03 | -4.66 | -37.33 | 118 |
| 48 | Triple EMA stack · 1h | trend | 73.72 | -26.28 | 146 | 14.4 | -25.06 | -4.15 | -36.65 | 185 |
| 49 | Daily: Momentum burst | daily | 73.63 | -26.38 | 27 | 11.1 | -34.67 | -4.75 | -38.23 | 33 |
| 50 | Bollinger reversion · 1h | reversion | 73.44 | -26.56 | 288 | 41.3 | -29.53 | -4.55 | -34.84 | 370 |
| 51 | ROC + volume · 1h | momentum | 72.41 | -27.59 | 378 | 27.5 | -32.74 | -6.00 | -38.34 | 379 |
| 52 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -33.41 | -4.90 | -35.70 | 452 |
| 53 | Donchian 20/10 · 1h | breakout | 71.53 | -28.47 | 145 | 19.3 | -29.37 | -5.43 | -35.87 | 211 |
| 54 | OBV trend · 1h | momentum | 71.49 | -28.51 | 282 | 19.1 | -28.23 | -4.94 | -36.93 | 284 |
| 55 | Williams %R · 1h | reversion | 68.80 | -31.20 | 358 | 45.5 | -39.53 | -6.27 | -39.97 | 528 |
| 56 | Z-score reversion · 1h | reversion | 67.98 | -32.02 | 199 | 38.2 | -26.98 | -3.74 | -28.98 | 233 |
| 57 | EMA 9/21 cross · 1h | trend | 67.10 | -32.90 | 255 | 9.8 | -34.19 | -6.77 | -41.56 | 333 |
| 58 | Agent (ML meta-label) | meta | 66.51 | -33.49 | 1756 | 24.8 | -12.64 | -2.00 | -18.44 | 337 |
| 59 | VWAP momentum · 1h | momentum | 66.43 | -33.56 | 876 | 22.4 | -51.31 | -10.58 | -51.67 | 1219 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -32.77 | -4.57 | -34.13 | 243 |
| 61 | Candlestick reversal · 1h | reversion | 62.95 | -37.05 | 467 | 28.5 | -42.50 | -7.68 | -42.58 | 596 |
| 62 | Three white soldiers | momentum | 59.83 | -40.17 | 523 | 14.9 | -48.60 | -22.48 | -48.63 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -44.29 | -99.01 | 5271 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.73 | -25.42 | -79.73 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -43.79 | -93.45 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.48 | -32.34 | -89.50 | 1924 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.09 | -40.37 | -91.10 | 2326 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.96 | -31.54 | -89.96 | 2179 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -54.09 | -97.87 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -54.54 | -96.29 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -33.09 | -93.57 | 2352 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -34.12 | -83.03 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.72 | -99.57 | 6003 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -42.73 | -92.18 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.35 | -95.45 | 3449 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -79.02 | -99.81 | 6135 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.14 | -44.13 | -92.16 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.99 | -25.03 | -75.20 | 1616 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -58.36 | -97.62 | 3504 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -64.13 | -98.89 | 4911 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.31 | -26.76 | -68.64 | 1231 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.34 | -94.70 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.95 | -38.42 | -84.96 | 1780 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -76.76 | -99.66 | 6348 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.87 | -32.64 | -89.93 | 2302 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.63 | -20.16 | -78.70 | 1771 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.82 | -36.86 | -90.85 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.89 | -53.22 | -96.90 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.13 | -57.29 | -89.14 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.15 | -30.07 | -66.15 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.33 | -22.98 | -71.38 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.52 | -18.82 | -79.75 | 1717 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.32 | -49.56 | -97.33 | 4297 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -113.36 | -99.93 | 8335 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T14:40 | Agent (rotation) | buy | TQQQ | 28.51 | — | rebalance up |
| 2026-11-12T14:40 | Agent (rotation) | buy | AMD | 8.13 | — | following Parabolic SAR |
| 2026-11-12T14:40 | Day trade: Stocks in Play ORB | buy | UPRO | 24.93 | — | entry |
| 2026-11-12T14:40 | Day trade: Stocks in Play ORB | buy | TECL | 24.93 | — | entry |
| 2026-11-12T14:40 | Day trade: Stocks in Play ORB | buy | NVDA | 24.93 | — | entry |
| 2026-11-12T14:40 | Day trade: Stocks in Play ORB | buy | BITX | 24.93 | — | entry |
| 2026-11-12T14:40 | Day trade: Open breakout · TQQQ/SQQQ | buy | TQQQ | 112.26 | — | entry |
| 2026-11-12T14:40 | Three white soldiers | buy | SOL-USD | 14.98 | — | entry signal |
| 2026-11-12T14:40 | Three white soldiers | buy | DOGE-USD | 14.98 | — | entry signal |
| 2026-11-12T14:40 | Gap and go | buy | AMD | 25.09 | — | entry signal |
| 2026-11-12T14:35 | Max aggression: 1-day momentum | buy | AMD | 76.72 | — | entry |
| 2026-11-12T14:35 | Max aggression: 1-day momentum | sell | SOXL | 76.72 | 17.41 | target is flat |
| 2026-11-12T14:35 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 112.26 | -5.30 | target is flat |
| 2026-11-12T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 109.59 | — | entry |
| 2026-11-12T14:35 | Agent (ML meta-label) | buy | XRP-USD | 4.10 | — | rebalance up |
| 2026-11-12T14:35 | Agent (ML meta-label) | buy | TSLA | 3.63 | — | rebalance up |
| 2026-11-12T14:35 | Agent (ML meta-label) | buy | TECL | 4.30 | — | rebalance up |
| 2026-11-12T14:35 | Agent (ML meta-label) | buy | AMZN | 3.56 | — | rebalance up |
| 2026-11-12T14:35 | Agent (ML meta-label) | buy | AMD | 3.54 | — | rebalance up |
| 2026-11-12T14:35 | Agent (ML meta-label) | sell | GOOGL | 9.54 | 0.02 | selected signal exited |
| 2026-11-12T14:35 | Agent (ML meta-label) | sell | AAPL | 9.59 | 0.07 | selected signal exited |
| 2026-11-12T14:35 | Daily: Bullish score | buy | AAPL | 21.32 | — | entry |
| 2026-11-12T14:35 | Timing: Nasdaq FTD · QQQ | buy | QQQ | 97.06 | — | entry |
| 2026-11-12T14:35 | Timing: Nasdaq FTD · TQQQ | buy | TQQQ | 91.23 | — | entry |
| 2026-11-12T14:35 | MFI reversion · 1h | buy | SPY | 19.71 | — | entry |
| 2026-11-12T14:35 | MFI reversion · 1h | buy | AAPL | 19.71 | — | entry |
| 2026-11-12T14:35 | MFI reversion · 1h | sell | SQQQ | 20.71 | 0.78 | target is flat |
| 2026-11-12T14:35 | CCI reversion · 1h | sell | NVDA | 17.19 | -1.59 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T14:35 | CCI reversion · 1h | sell | ETHU | 18.07 | -1.13 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T14:35 | CCI reversion · 1h | sell | BITX | 18.40 | -0.91 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-12T14:35 | Williams %R · 1h | buy | XRP-USD | 13.69 | — | entry |
| 2026-11-12T14:35 | Williams %R · 1h | buy | SOL-USD | 13.69 | — | entry |
| 2026-11-12T14:35 | Williams %R · 1h | buy | ETH-USD | 7.85 | — | rebalance up |
| 2026-11-12T14:35 | Williams %R · 1h | buy | DOGE-USD | 3.52 | — | rebalance up |
| 2026-11-12T14:35 | Williams %R · 1h | sell | MSTR | 13.56 | -0.89 | stop-loss |
| 2026-11-12T14:35 | Williams %R · 1h | sell | META | 11.85 | -0.33 | stop-loss |
| 2026-11-12T14:35 | Williams %R · 1h | sell | BITX | 13.63 | -0.69 | target is flat |
| 2026-11-12T14:35 | Stochastic reversion · 1h | buy | SOL-USD | 1.04 | — | entry |
| 2026-11-12T14:35 | Stochastic reversion · 1h | buy | BTC-USD | 9.98 | — | entry |
| 2026-11-12T14:35 | Stochastic reversion · 1h | sell | BITX | 11.02 | -0.53 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 14:40:05.000120+00:00 -> 2026-11-12 14:50:05.000120+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
