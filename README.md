# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-18T15:30:05.000097+00:00 · 64579 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.66 (-15.34%)

Closed trades 219, win rate 35.6%, fees £6.07, max drawdown -17.33%.

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

Today: 16002 decisions in 2451 calls, $0.2135 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-18T15:30 | 3 / 16 / 11 | cash |  |
| Breezy | 2026-11-18T15:30 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-18T15:30 | 2 / 24 / 4 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | SOXL | 2.08 | +16.03% | 8 |
| CCI reversion | SOXL | 2.02 | +16.49% | 14 |
| OBV trend | SQQQ | 1.88 | +3.85% | 12 |
| Squeeze breakout | SPY | 1.80 | +1.03% | 4 |
| Stochastic reversion | TSLA | 1.77 | +4.11% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 115.46 | 15.46 | 0 | — | 13.36 | 4.70 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.86 | 12.86 | 38 | 31.6 | 20.00 | 3.00 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.39 | 11.39 | 25 | 64.0 | 17.51 | 3.58 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.06 | 4.05 | 0 | — | 5.98 | 1.36 | -6.60 | 0 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.27 | 0.27 | 150 | 34.7 | -3.43 | -2.98 | -4.83 | 70 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 8.02 | 2.24 | -9.06 | 212 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.59 | -1.41 | 39 | 41.0 | -2.66 | -0.48 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.45 | -3.55 | 8 | 50.0 | -4.36 | -0.11 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.73 | -4.27 | 0 | — | -4.01 | -1.33 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 94.03 | -5.97 | 199 | 30.2 | -4.24 | -1.50 | -8.80 | 148 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.74 | -9.14 | -5.90 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.59 | -7.41 | 0 | — | -7.15 | -1.88 | -8.68 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.65 | -8.35 | 25 | 16.0 | -9.71 | -8.17 | -10.18 | 24 |
| 17 | Copy: Insider buying | copy | 90.89 | -9.11 | 50 | 42.0 | -9.43 | -1.89 | -14.79 | 64 |
| 18 | Copy: Congress Democrats (NANC) | copy | 90.87 | -9.13 | 0 | — | -7.97 | -2.16 | -12.67 | 1 |
| 19 | Trend pullback · 1h | trend | 90.27 | -9.73 | 113 | 23.9 | -13.25 | -7.20 | -13.31 | 58 |
| 20 | VWAP reversion · 1h | reversion | 89.83 | -10.17 | 155 | 45.8 | -12.55 | -3.70 | -18.48 | 149 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.05 | -12.95 | 17 | 17.6 | -5.25 | -0.84 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 86.32 | -13.68 | 70 | 20.0 | -16.00 | -8.98 | -16.05 | 70 |
| 24 | Opening range 30m | breakout | 86.18 | -13.81 | 439 | 33.7 | -9.24 | -2.94 | -14.11 | 562 |
| 25 | Agent | meta | 84.66 | -15.34 | 219 | 35.6 | -15.37 | -7.48 | -17.11 | 198 |
| 26 | Agent (aggressive) | meta | 81.77 | -18.23 | 103 | 33.0 | -17.29 | -4.78 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.44 | -18.56 | 188 | 28.2 | -25.36 | -7.04 | -28.11 | 202 |
| 28 | Connors RSI(2) · 1h | reversion | 80.61 | -19.39 | 216 | 40.3 | -14.31 | -6.36 | -14.63 | 87 |
| 29 | Keltner breakout · 1h | breakout | 79.83 | -20.17 | 124 | 25.8 | -24.92 | -6.58 | -28.78 | 162 |
| 30 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 163 | 28.8 | -16.51 | -4.91 | -22.76 | 80 |
| 31 | Donchian 55/20 · 1h | breakout | 79.46 | -20.54 | 77 | 13.0 | -24.99 | -6.55 | -29.99 | 84 |
| 32 | Max aggression: 5-day momentum | meta | 79.07 | -20.93 | 21 | 42.9 | -47.98 | -3.20 | -55.24 | 21 |
| 33 | Opening range 15m | breakout | 78.56 | -21.44 | 534 | 31.6 | -15.96 | -4.28 | -21.37 | 673 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.49 | -22.51 | 2 | 0.0 | -17.71 | -2.34 | -26.43 | 1 |
| 35 | Ichimoku · 1h | trend | 74.74 | -25.26 | 101 | 14.9 | -28.81 | -8.43 | -29.97 | 111 |
| 36 | ADX DI cross · 1h | trend | 74.51 | -25.49 | 209 | 19.1 | -28.52 | -4.67 | -36.07 | 268 |
| 37 | Hold BTC | benchmark | 74.45 | -25.55 | 2 | 0.0 | -17.24 | -2.41 | -28.91 | 1 |
| 38 | Stochastic reversion · 1h | reversion | 73.35 | -26.65 | 348 | 42.5 | -33.99 | -5.15 | -35.59 | 426 |
| 39 | Bollinger breakout · 1h | breakout | 73.01 | -26.99 | 192 | 21.9 | -29.69 | -7.85 | -33.83 | 223 |
| 40 | Supertrend · 1h | trend | 72.01 | -27.99 | 189 | 15.9 | -31.86 | -5.38 | -39.50 | 202 |
| 41 | Max aggression: 1-day momentum ⏸ | meta | 71.77 | -28.23 | 32 | 28.1 | -38.26 | -2.31 | -57.50 | 39 |
| 42 | Triple EMA stack · 1h | trend | 71.24 | -28.77 | 155 | 14.8 | -33.23 | -6.64 | -39.35 | 179 |
| 43 | MFI reversion · 1h | reversion | 70.77 | -29.23 | 441 | 33.8 | -27.73 | -4.13 | -30.08 | 164 |
| 44 | RSI momentum · 1h | momentum | 70.77 | -29.23 | 176 | 14.2 | -30.44 | -5.52 | -37.25 | 198 |
| 45 | MACD zero-line · 1h | trend | 69.99 | -30.01 | 183 | 17.5 | -28.04 | -5.68 | -34.23 | 203 |
| 46 | EMA 20/50 cross · 1h | trend | 69.61 | -30.39 | 115 | 10.4 | -35.93 | -9.20 | -39.91 | 117 |
| 47 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 48 | Heikin-Ashi · 1h | trend | 68.95 | -31.05 | 474 | 23.0 | -44.99 | -9.84 | -45.37 | 638 |
| 49 | OBV trend · 1h | momentum | 68.43 | -31.57 | 308 | 19.2 | -36.12 | -7.71 | -39.99 | 257 |
| 50 | ROC + volume · 1h | momentum | 68.39 | -31.61 | 412 | 28.2 | -33.99 | -6.12 | -39.93 | 360 |
| 51 | MACD cross · 1h | trend | 68.35 | -31.65 | 416 | 22.1 | -40.74 | -6.72 | -45.84 | 481 |
| 52 | CCI reversion · 1h | reversion | 67.49 | -32.51 | 383 | 41.5 | -41.51 | -6.90 | -44.29 | 473 |
| 53 | Donchian 20/10 · 1h | breakout | 67.06 | -32.94 | 159 | 18.2 | -35.52 | -6.56 | -40.92 | 203 |
| 54 | Bollinger reversion · 1h | reversion | 64.17 | -35.83 | 345 | 37.7 | -38.50 | -5.85 | -39.50 | 413 |
| 55 | Williams %R · 1h | reversion | 63.98 | -36.02 | 432 | 41.0 | -46.26 | -8.04 | -47.56 | 564 |
| 56 | EMA 9/21 cross · 1h | trend | 63.37 | -36.63 | 282 | 11.0 | -39.83 | -7.79 | -45.90 | 321 |
| 57 | Agent (ML meta-label) | meta | 60.19 | -39.81 | 1912 | 24.5 | -21.18 | -4.19 | -21.63 | 278 |
| 58 | RSI(14) reversion · 1h | reversion | 59.21 | -40.79 | 206 | 32.0 | -40.27 | -5.88 | -43.22 | 255 |
| 59 | Z-score reversion · 1h | reversion | 57.87 | -42.13 | 225 | 35.1 | -37.47 | -5.23 | -39.38 | 256 |
| 60 | VWAP momentum · 1h | momentum | 56.38 | -43.62 | 971 | 21.7 | -55.41 | -11.26 | -59.10 | 1201 |
| 61 | Candlestick reversal · 1h | reversion | 55.51 | -44.49 | 548 | 26.6 | -47.61 | -8.76 | -49.07 | 635 |
| 62 | Three white soldiers | momentum | 54.89 | -45.11 | 587 | 14.5 | -49.83 | -21.68 | -50.81 | 664 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -43.52 | -99.04 | 5335 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.41 | -26.25 | -82.35 | 1404 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -43.66 | -93.90 | 2448 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.01 | -31.85 | -90.25 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.06 | -39.84 | -91.35 | 2287 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.03 | -31.56 | -90.06 | 2108 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -48.26 | -97.90 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -54.12 | -96.45 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -39.52 | -93.62 | 2215 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.26 | -33.96 | -82.52 | 1582 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.64 | -99.60 | 6085 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.93 | -42.44 | -92.09 | 2546 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.90 | -39.43 | -94.91 | 3278 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.66 | -99.81 | 6177 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.45 | -43.86 | -92.57 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.73 | -25.55 | -76.48 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -61.29 | -97.68 | 3422 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.07 | -58.31 | -99.07 | 4975 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.88 | -28.40 | -69.44 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -56.94 | -94.65 | 2749 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -37.93 | -84.64 | 1724 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.92 | -99.70 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.88 | -31.32 | -90.88 | 2367 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.71 | -18.90 | -79.85 | 1830 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.49 | -36.58 | -91.50 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.56 | -46.10 | -97.56 | 3918 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -57.72 | -89.27 | 2152 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.20 | -30.14 | -67.08 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.16 | -23.00 | -72.89 | 1219 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.11 | -18.22 | -81.17 | 1738 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -46.25 | -97.59 | 4326 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -113.03 | -99.94 | 8451 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | TSLA | 6.68 | — | following Stochastic reversion |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | TNA | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | SOXL | 6.69 | — | following Z-score reversion, CCI reversion |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | LABU | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | IWM | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | AMD | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | buy | AAPL | 6.69 | — | entry |
| 2026-11-18T15:30 | Agent (ML meta-label) | sell | SQQQ | 8.40 | 0.03 | rebalance down |
| 2026-11-18T15:30 | Agent (ML meta-label) | sell | SPY | 8.34 | -0.01 | rebalance down |
| 2026-11-18T15:30 | MFI reversion · 1h | buy | QQQ | 11.79 | — | entry signal |
| 2026-11-18T15:30 | MFI reversion · 1h | buy | LABU | 11.80 | — | entry signal |
| 2026-11-18T15:30 | MFI reversion · 1h | buy | GOOGL | 11.80 | — | entry signal |
| 2026-11-18T15:30 | MFI reversion · 1h | buy | AMD | 11.80 | — | entry signal |
| 2026-11-18T15:30 | MFI reversion · 1h | sell | SPY | 5.83 | -0.01 | rebalance down |
| 2026-11-18T15:30 | MFI reversion · 1h | sell | AMZN | 6.13 | 0.08 | rebalance down |
| 2026-11-18T15:30 | CCI reversion · 1h | buy | NVDA | 2.08 | — | entry |
| 2026-11-18T15:30 | CCI reversion · 1h | buy | MSFT | 4.22 | — | entry |
| 2026-11-18T15:30 | CCI reversion · 1h | buy | IWM | 4.22 | — | entry signal |
| 2026-11-18T15:30 | CCI reversion · 1h | sell | SOXL | 3.50 | 0.22 | rebalance down |
| 2026-11-18T15:30 | CCI reversion · 1h | sell | AMZN | 3.48 | 0.10 | rebalance down |
| 2026-11-18T15:30 | CCI reversion · 1h | sell | AMD | 3.54 | 0.14 | rebalance down |
| 2026-11-18T15:30 | Williams %R · 1h | buy | ETH-USD | 1.79 | — | entry |
| 2026-11-18T15:30 | Williams %R · 1h | buy | DOGE-USD | 3.20 | — | entry |
| 2026-11-18T15:30 | Williams %R · 1h | buy | BTC-USD | 3.20 | — | entry |
| 2026-11-18T15:30 | Williams %R · 1h | sell | AMZN | 4.08 | 0.13 | exit signal |
| 2026-11-18T15:30 | Williams %R · 1h | sell | AMD | 4.12 | 0.16 | exit signal |
| 2026-11-18T15:30 | Stochastic reversion · 1h | buy | MSTR | 4.58 | — | entry signal |
| 2026-11-18T15:30 | Stochastic reversion · 1h | sell | AMZN | 4.45 | 0.15 | exit signal |
| 2026-11-18T15:30 | RSI(14) reversion · 1h | buy | MSFT | 1.62 | — | entry |
| 2026-11-18T15:30 | RSI(14) reversion · 1h | buy | LABU | 5.92 | — | entry |
| 2026-11-18T15:30 | RSI(14) reversion · 1h | sell | AMZN | 7.55 | 0.24 | exit signal |
| 2026-11-18T15:30 | OBV trend · 1h | buy | AAPL | 17.11 | — | entry signal |
| 2026-11-18T15:30 | ROC + volume · 1h | buy | SQQQ | 17.10 | — | entry signal |
| 2026-11-18T15:30 | ROC + volume · 1h | buy | AMZN | 17.10 | — | entry signal |
| 2026-11-18T15:30 | ROC + volume · 1h | buy | AMD | 17.10 | — | entry signal |
| 2026-11-18T15:30 | VWAP momentum · 1h | buy | TNA | 13.93 | — | entry signal |
| 2026-11-18T15:30 | VWAP momentum · 1h | buy | IWM | 14.10 | — | entry signal |
| 2026-11-18T15:30 | VWAP momentum · 1h | sell | MSFT | 14.10 | -0.02 | exit signal |
| 2026-11-18T15:30 | VWAP momentum · 1h | sell | ETHU | 13.92 | -0.35 | exit signal |
| 2026-11-18T15:30 | Trend pullback · 1h | buy | AAPL | 22.57 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-20 15:30:05.000097+00:00 -> 2026-11-18 15:40:05.000097+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-20 15:30:05.000097+00:00 -> 2026-11-18 15:40:05.000097+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
