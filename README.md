# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T19:25:05.000126+00:00 · 54914 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.50 (-12.50%)

Closed trades 169, win rate 35.5%, fees £5.11, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.50 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 31547 decisions in 2890 calls, $0.3942 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T19:25 | 3 / 16 / 11 | cash |  |
| Breezy | 2026-11-10T19:25 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-10T19:25 | 5 / 20 / 5 | BITX 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.94 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.18 | 15.18 | 0 | — | 14.73 | 4.86 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.89 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.33 | 1.33 | 0 | — | 4.19 | 1.23 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.07 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.48 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.34 | -1.77 | -9.88 | 149 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.65 | -3.35 | 0 | — | -1.16 | -0.33 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.80 | -4.20 | 138 | 46.4 | -12.86 | -3.33 | -13.48 | 154 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.43 | -5.57 | 0 | — | -4.95 | -1.31 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.87 | -7.13 | 108 | 23.1 | -13.29 | -4.97 | -17.51 | 78 |
| 19 | Copy: Insider buying | copy | 92.67 | -7.33 | 43 | 39.5 | -8.23 | -1.71 | -15.11 | 67 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.25 | -7.75 | 0 | — | -4.63 | -1.23 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.30 | -2.90 | -14.15 | 78 |
| 23 | Opening range 30m | breakout | 88.45 | -11.55 | 403 | 33.3 | -15.11 | -4.66 | -15.17 | 605 |
| 24 | Agent | meta | 87.50 | -12.50 | 169 | 35.5 | -13.42 | -6.88 | -14.37 | 198 |
| 25 | Daily: Bullish score | daily | 86.77 | -13.23 | 15 | 20.0 | -7.77 | -1.01 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 85.81 | -14.19 | 1 | 0.0 | -6.41 | -0.84 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.36 | -14.64 | 168 | 26.8 | -13.82 | -2.83 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -15.80 | -4.46 | -18.49 | 92 |
| 29 | Donchian 55/20 · 1h | breakout | 84.30 | -15.70 | 71 | 14.1 | -16.62 | -3.47 | -22.24 | 101 |
| 30 | Keltner breakout · 1h | breakout | 81.63 | -18.37 | 110 | 23.6 | -22.39 | -4.69 | -25.32 | 176 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 81.57 | -18.43 | 2 | 0.0 | -8.71 | -0.98 | -24.16 | 1 |
| 32 | Connors RSI(2) · 1h | reversion | 81.00 | -19.00 | 206 | 39.8 | -19.35 | -6.47 | -19.97 | 126 |
| 33 | Opening range 15m | breakout | 80.94 | -19.06 | 499 | 31.5 | -19.84 | -5.45 | -20.55 | 738 |
| 34 | Stochastic reversion · 1h | reversion | 80.79 | -19.21 | 284 | 47.5 | -25.33 | -3.73 | -26.97 | 395 |
| 35 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.42 | -3.62 | -22.08 | 93 |
| 36 | Max aggression: 5-day momentum | meta | 79.99 | -20.01 | 18 | 44.4 | -36.56 | -2.34 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.10 | -7.53 | -42.42 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.85 | -21.15 | 185 | 18.9 | -24.89 | -4.31 | -29.95 | 269 |
| 39 | CCI reversion · 1h | reversion | 76.98 | -23.02 | 326 | 45.1 | -25.62 | -3.89 | -30.69 | 454 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.35 | -4.44 | -27.99 | 236 |
| 41 | MFI reversion · 1h | reversion | 76.82 | -23.18 | 360 | 33.9 | -19.08 | -2.42 | -22.46 | 160 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.26 | -8.88 | -31.64 | 119 |
| 43 | EMA 20/50 cross · 1h | trend | 75.05 | -24.95 | 102 | 10.8 | -26.99 | -4.82 | -36.41 | 121 |
| 44 | MACD cross · 1h | trend | 74.46 | -25.54 | 360 | 21.9 | -32.26 | -5.28 | -39.64 | 468 |
| 45 | Bollinger reversion · 1h | reversion | 73.77 | -26.23 | 278 | 40.3 | -26.94 | -4.16 | -32.54 | 370 |
| 46 | MACD zero-line · 1h | trend | 73.71 | -26.29 | 159 | 16.4 | -25.44 | -5.24 | -30.85 | 215 |
| 47 | Supertrend · 1h | trend | 73.29 | -26.71 | 168 | 13.1 | -32.58 | -5.99 | -36.07 | 231 |
| 48 | RSI momentum · 1h | momentum | 73.26 | -26.74 | 159 | 12.6 | -24.94 | -4.11 | -34.10 | 212 |
| 49 | Triple EMA stack · 1h | trend | 72.15 | -27.85 | 144 | 14.6 | -26.78 | -4.71 | -35.23 | 203 |
| 50 | OBV trend · 1h | momentum | 71.77 | -28.23 | 275 | 18.2 | -27.50 | -4.85 | -35.86 | 279 |
| 51 | Williams %R · 1h | reversion | 71.68 | -28.32 | 346 | 45.7 | -35.71 | -5.58 | -36.06 | 534 |
| 52 | ROC + volume · 1h | momentum | 70.96 | -29.04 | 362 | 26.5 | -35.83 | -6.87 | -38.42 | 378 |
| 53 | Donchian 20/10 · 1h | breakout | 70.80 | -29.20 | 142 | 19.7 | -29.98 | -5.59 | -35.64 | 205 |
| 54 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -26.46 | -3.83 | -28.98 | 232 |
| 55 | Daily: Momentum burst | daily | 70.54 | -29.46 | 27 | 11.1 | -38.63 | -5.47 | -39.29 | 34 |
| 56 | Max aggression: 1-day momentum | meta | 66.86 | -33.14 | 27 | 25.9 | -31.09 | -1.56 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.37 | -33.63 | 170 | 30.6 | -27.06 | -3.75 | -32.54 | 241 |
| 58 | VWAP momentum · 1h | momentum | 66.11 | -33.88 | 838 | 22.0 | -53.91 | -11.60 | -54.98 | 1216 |
| 59 | Agent (ML meta-label) | meta | 65.37 | -34.63 | 1692 | 24.4 | -11.96 | -2.03 | -16.96 | 326 |
| 60 | EMA 9/21 cross · 1h | trend | 65.27 | -34.73 | 252 | 9.9 | -37.36 | -7.44 | -41.69 | 333 |
| 61 | Candlestick reversal · 1h | reversion | 63.52 | -36.48 | 445 | 27.9 | -39.02 | -7.20 | -40.10 | 590 |
| 62 | Three white soldiers | momentum | 60.63 | -39.37 | 510 | 14.7 | -49.17 | -23.00 | -49.17 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -46.09 | -98.97 | 5255 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.91 | -26.50 | -79.96 | 1418 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -47.09 | -93.22 | 2503 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -32.37 | -89.34 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.71 | -39.98 | -90.71 | 2324 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -32.54 | -90.32 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -55.10 | -97.78 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.65 | -96.20 | 3396 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.47 | -33.63 | -93.58 | 2361 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.44 | -35.13 | -82.49 | 1669 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -55.67 | -99.56 | 6018 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.20 | -43.79 | -92.21 | 2606 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.88 | -95.55 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -77.05 | -99.81 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -44.04 | -92.00 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.47 | -24.73 | -75.56 | 1597 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -63.97 | -97.73 | 3515 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -63.73 | -98.87 | 4894 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.51 | -27.40 | -69.01 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -55.94 | -94.60 | 2773 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.40 | -37.35 | -84.53 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.02 | -99.65 | 6345 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.70 | -32.63 | -89.83 | 2292 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.67 | -20.08 | -78.95 | 1770 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.81 | -37.24 | -90.95 | 2204 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.82 | -52.60 | -96.84 | 3856 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.41 | -58.81 | -89.47 | 2167 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.44 | -27.86 | -66.13 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.10 | -23.03 | -71.12 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.98 | -19.35 | -80.16 | 1694 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.19 | -49.61 | -97.22 | 4287 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -118.09 | -99.93 | 8311 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | COIN | 4.89 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | AMZN | 4.88 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | buy | AMD | 4.85 | — | rebalance up |
| 2026-11-10T19:25 | Agent (ML meta-label) | sell | AAPL | 10.89 | -0.00 | selected signal exited |
| 2026-11-10T19:15 | Three white soldiers | sell | SOL-USD | 15.13 | -0.17 | exit signal |
| 2026-11-10T19:15 | Three white soldiers | sell | ETH-USD | 15.17 | -0.12 | exit signal |
| 2026-11-10T19:15 | Three white soldiers | sell | DOGE-USD | 15.16 | -0.09 | exit signal |
| 2026-11-10T19:05 | Agent (ML meta-label) | buy | AAPL | 10.89 | — | entry |
| 2026-11-10T19:05 | Agent (ML meta-label) | sell | SOXL | 10.88 | -0.01 | selected signal exited |
| 2026-11-10T19:05 | Three white soldiers | sell | BTC-USD | 12.16 | -0.05 | exit signal |
| 2026-11-10T19:00 | Agent (ML meta-label) | buy | SOXL | 10.90 | — | entry |
| 2026-11-10T19:00 | Agent (ML meta-label) | sell | AAPL | 10.88 | 0.00 | selected signal exited |
| 2026-11-10T19:00 | MFI reversion · 1h | buy | XRP-USD | 12.82 | — | entry signal |
| 2026-11-10T19:00 | MFI reversion · 1h | buy | DOGE-USD | 12.84 | — | entry signal |
| 2026-11-10T19:00 | MFI reversion · 1h | sell | TECL | 6.00 | 0.02 | rebalance down |
| 2026-11-10T19:00 | MFI reversion · 1h | sell | SPY | 6.36 | 0.01 | rebalance down |
| 2026-11-10T19:00 | MFI reversion · 1h | sell | ETHU | 6.46 | 0.07 | rebalance down |
| 2026-11-10T19:00 | MFI reversion · 1h | sell | AAPL | 6.35 | -0.02 | rebalance down |
| 2026-11-10T19:00 | CCI reversion · 1h | buy | XRP-USD | 18.88 | — | entry signal |
| 2026-11-10T19:00 | Williams %R · 1h | buy | SOL-USD | 11.96 | — | entry signal |
| 2026-11-10T19:00 | Williams %R · 1h | buy | ETH-USD | 12.00 | — | entry signal |
| 2026-11-10T19:00 | Williams %R · 1h | buy | DOGE-USD | 12.00 | — | entry signal |
| 2026-11-10T19:00 | Williams %R · 1h | sell | XRP-USD | 6.20 | 0.06 | rebalance down |
| 2026-11-10T19:00 | Williams %R · 1h | sell | SQQQ | 6.06 | 0.05 | rebalance down |
| 2026-11-10T19:00 | Williams %R · 1h | sell | BTC-USD | 5.93 | -0.03 | rebalance down |
| 2026-11-10T19:00 | VWAP reversion · 1h | sell | XRP-USD | 24.33 | 0.46 | exit signal |
| 2026-11-10T19:00 | Bollinger reversion · 1h | buy | DOGE-USD | 8.17 | — | entry signal |
| 2026-11-10T19:00 | Bollinger reversion · 1h | buy | COIN | 8.22 | — | entry |
| 2026-11-10T19:00 | Bollinger reversion · 1h | buy | BITX | 8.22 | — | entry |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | XRP-USD | 4.19 | 0.04 | rebalance down |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | SOL-USD | 4.07 | 0.00 | rebalance down |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | NVDA | 4.04 | 0.00 | rebalance down |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | ETHU | 4.25 | 0.09 | rebalance down |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | ETH-USD | 4.07 | 0.00 | rebalance down |
| 2026-11-10T19:00 | Bollinger reversion · 1h | sell | BTC-USD | 4.01 | -0.02 | rebalance down |
| 2026-11-10T19:00 | RSI(14) reversion · 1h | buy | SOL-USD | 11.08 | — | entry signal |
| 2026-11-10T19:00 | RSI(14) reversion · 1h | buy | ETH-USD | 11.10 | — | entry signal |
| 2026-11-10T19:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 11.10 | — | entry signal |
| 2026-11-10T19:00 | RSI(14) reversion · 1h | sell | XRP-USD | 5.64 | 0.06 | rebalance down |
| 2026-11-10T19:00 | RSI(14) reversion · 1h | sell | TECL | 5.25 | -0.05 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 19:25:05.000126+00:00 -> 2026-11-10 19:35:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
