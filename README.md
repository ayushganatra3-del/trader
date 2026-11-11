# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T15:24:05.000133+00:00 · 55909 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.95 (-13.05%)

Closed trades 173, win rate 35.3%, fees £5.18, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 34.67 | -0.22 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 14460 decisions in 2313 calls, $0.1940 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T15:24 | 3 / 13 / 14 | cash |  |
| Breezy | 2026-11-11T15:24 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-11T15:24 | 3 / 24 / 3 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| MFI reversion | LABU | 1.93 | +6.15% | 4 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.23 | 4.05 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.25 | 14.25 | 0 | — | 14.26 | 4.67 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.93 | 10.93 | 32 | 28.1 | 19.23 | 2.88 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.94 | 1.03 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.24 | 3.24 | 0 | — | 5.77 | 1.61 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.07 | 0.07 | 132 | 34.8 | 10.76 | 3.72 | -2.93 | 85 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.60 | -1.40 | 183 | 30.6 | 5.30 | 1.54 | -9.06 | 239 |
| 11 | Hold SPY | benchmark | 98.00 | -2.00 | 0 | — | -0.31 | -0.03 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 97.79 | -2.21 | 180 | 28.3 | -2.22 | -0.78 | -8.92 | 170 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.72 | -3.28 | 0 | — | -2.50 | -0.59 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 93.98 | -6.02 | 43 | 39.5 | -7.20 | -1.45 | -15.11 | 67 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.83 | -6.17 | 0 | — | -2.91 | -0.72 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.74 | -8.26 | 109 | 22.9 | -16.12 | -5.66 | -18.68 | 80 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.24 | -3.15 | -14.15 | 77 |
| 23 | Opening range 30m | breakout | 88.25 | -11.75 | 404 | 33.2 | -13.79 | -4.22 | -13.97 | 583 |
| 24 | Agent | meta | 86.95 | -13.05 | 173 | 35.3 | -14.26 | -7.38 | -14.49 | 202 |
| 25 | Parabolic SAR · 1h | trend | 86.34 | -13.66 | 168 | 26.8 | -14.11 | -2.97 | -21.98 | 224 |
| 26 | Hold BTC | benchmark | 86.31 | -13.69 | 1 | 0.0 | -4.78 | -0.59 | -16.64 | 1 |
| 27 | Daily: Bullish score | daily | 84.96 | -15.04 | 16 | 18.8 | -7.70 | -1.13 | -18.57 | 15 |
| 28 | Agent (aggressive) | meta | 84.81 | -15.19 | 81 | 33.3 | -16.18 | -4.58 | -18.51 | 95 |
| 29 | Max aggression: 5-day momentum | meta | 84.57 | -15.43 | 19 | 47.4 | -29.89 | -1.69 | -45.81 | 25 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 84.34 | -15.66 | 2 | 0.0 | -5.92 | -0.58 | -24.16 | 1 |
| 31 | Donchian 55/20 · 1h | breakout | 83.03 | -16.97 | 71 | 14.1 | -23.60 | -4.99 | -28.51 | 100 |
| 32 | Keltner breakout · 1h | breakout | 81.60 | -18.40 | 110 | 23.6 | -20.29 | -4.21 | -25.32 | 175 |
| 33 | ADX DI cross · 1h | trend | 81.59 | -18.41 | 185 | 18.9 | -23.31 | -3.80 | -30.55 | 270 |
| 34 | Stochastic reversion · 1h | reversion | 81.37 | -18.63 | 287 | 47.7 | -24.90 | -3.58 | -27.17 | 392 |
| 35 | Opening range 15m | breakout | 80.63 | -19.37 | 500 | 31.4 | -19.26 | -5.21 | -20.82 | 718 |
| 36 | Connors RSI(2) · 1h | reversion | 80.58 | -19.42 | 208 | 39.9 | -19.85 | -6.61 | -19.98 | 125 |
| 37 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -14.13 | -3.28 | -21.11 | 92 |
| 38 | Heikin-Ashi · 1h | trend | 79.78 | -20.22 | 417 | 24.5 | -39.24 | -7.21 | -42.12 | 665 |
| 39 | MFI reversion · 1h | reversion | 79.05 | -20.95 | 370 | 34.9 | -17.00 | -2.15 | -23.02 | 159 |
| 40 | Max aggression: 1-day momentum | meta | 78.39 | -21.61 | 27 | 25.9 | -20.31 | -0.66 | -57.50 | 40 |
| 41 | MACD cross · 1h | trend | 77.34 | -22.66 | 360 | 21.9 | -30.34 | -4.83 | -39.51 | 479 |
| 42 | CCI reversion · 1h | reversion | 77.00 | -23.00 | 327 | 45.0 | -26.57 | -3.99 | -31.08 | 454 |
| 43 | Bollinger breakout · 1h | breakout | 76.69 | -23.31 | 171 | 22.8 | -21.41 | -4.42 | -28.21 | 237 |
| 44 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 45 | MACD zero-line · 1h | trend | 75.12 | -24.88 | 159 | 16.4 | -22.05 | -4.36 | -31.04 | 208 |
| 46 | Supertrend · 1h | trend | 75.00 | -25.00 | 168 | 13.1 | -29.14 | -5.11 | -36.07 | 228 |
| 47 | EMA 20/50 cross · 1h | trend | 74.93 | -25.07 | 102 | 10.8 | -26.01 | -4.44 | -36.22 | 114 |
| 48 | Bollinger reversion · 1h | reversion | 74.66 | -25.34 | 283 | 41.0 | -25.98 | -3.96 | -32.54 | 371 |
| 49 | RSI momentum · 1h | momentum | 74.55 | -25.45 | 159 | 12.6 | -25.58 | -3.97 | -36.77 | 206 |
| 50 | Daily: Momentum burst | daily | 73.66 | -26.34 | 27 | 11.1 | -33.35 | -4.51 | -38.23 | 33 |
| 51 | Triple EMA stack · 1h | trend | 73.44 | -26.55 | 144 | 14.6 | -25.86 | -4.30 | -36.34 | 189 |
| 52 | ROC + volume · 1h | momentum | 72.41 | -27.59 | 373 | 27.6 | -34.05 | -6.24 | -38.55 | 380 |
| 53 | Williams %R · 1h | reversion | 71.84 | -28.16 | 350 | 45.7 | -35.17 | -5.50 | -36.28 | 533 |
| 54 | Donchian 20/10 · 1h | breakout | 71.59 | -28.41 | 142 | 19.7 | -30.18 | -5.56 | -35.64 | 206 |
| 55 | OBV trend · 1h | momentum | 71.44 | -28.57 | 278 | 18.3 | -28.11 | -5.10 | -35.23 | 284 |
| 56 | Z-score reversion · 1h | reversion | 70.82 | -29.18 | 190 | 36.3 | -23.56 | -3.27 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 68.12 | -31.88 | 171 | 31.0 | -26.90 | -3.93 | -32.54 | 236 |
| 58 | VWAP momentum · 1h | momentum | 67.35 | -32.65 | 846 | 21.9 | -52.42 | -10.63 | -54.67 | 1234 |
| 59 | EMA 9/21 cross · 1h | trend | 66.96 | -33.04 | 253 | 9.9 | -35.97 | -6.88 | -41.68 | 337 |
| 60 | Agent (ML meta-label) | meta | 66.55 | -33.45 | 1712 | 24.7 | -11.62 | -1.92 | -18.70 | 331 |
| 61 | Candlestick reversal · 1h | reversion | 64.25 | -35.75 | 457 | 28.4 | -37.70 | -6.84 | -40.44 | 592 |
| 62 | Three white soldiers | momentum | 60.26 | -39.74 | 513 | 14.6 | -49.30 | -22.65 | -49.30 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.05 | -44.83 | -99.05 | 5339 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.29 | -26.08 | -80.29 | 1436 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.70 | -45.91 | -93.70 | 2539 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.42 | -31.80 | -89.45 | 1926 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.07 | -39.22 | -91.17 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.36 | -32.28 | -90.38 | 2216 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -53.83 | -97.86 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.44 | -57.99 | -96.44 | 3462 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.35 | -31.55 | -93.53 | 2343 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.06 | -34.02 | -83.23 | 1680 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.41 | -99.54 | 5969 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.33 | -42.75 | -92.34 | 2620 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -37.25 | -95.59 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.99 | -99.80 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.09 | -43.03 | -92.09 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.26 | -25.17 | -75.43 | 1635 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.25 | -97.75 | 3535 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.15 | -98.84 | 4884 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -26.85 | -69.04 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -53.95 | -94.75 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.00 | -37.39 | -85.22 | 1795 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.56 | -99.63 | 6334 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.40 | -31.44 | -89.45 | 2283 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.36 | -19.39 | -77.76 | 1747 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -35.62 | -90.68 | 2185 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.69 | -50.55 | -96.69 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.08 | -54.22 | -89.08 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.60 | -27.73 | -66.53 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.31 | -22.56 | -71.80 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.31 | -18.32 | -78.58 | 1692 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -47.42 | -97.18 | 4278 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -100.47 | -99.93 | 8341 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T15:21 | Agent (ML meta-label) | buy | COIN | 16.64 | — | following Donchian 20/10 |
| 2026-11-11T15:21 | Agent (ML meta-label) | sell | META | 16.62 | -0.05 | selected signal exited |
| 2026-11-11T15:21 | Agent (ML meta-label) | sell | AMZN | 16.62 | -0.07 | selected signal exited |
| 2026-11-11T15:21 | Connors RSI(2) · 1h | sell | MSFT | 19.85 | -0.41 | stop-loss |
| 2026-11-11T15:16 | Agent (rotation) | buy | TSLA | 16.30 | — | entry |
| 2026-11-11T15:16 | Day trade: Stocks in Play ORB | buy | TSLA | 25.04 | — | entry |
| 2026-11-11T15:16 | Agent (ML meta-label) | buy | META | 6.35 | — | rebalance up |
| 2026-11-11T15:16 | Agent (ML meta-label) | buy | AMZN | 6.36 | — | rebalance up |
| 2026-11-11T15:16 | Agent (ML meta-label) | sell | TECL | 10.10 | -0.10 | selected signal exited |
| 2026-11-11T15:16 | Agent (ML meta-label) | sell | SOXL | 10.74 | -0.13 | selected signal exited |
| 2026-11-11T15:16 | Agent (ML meta-label) | sell | COIN | 11.63 | 0.12 | selected signal exited |
| 2026-11-11T15:16 | Candlestick reversal · 1h | buy | TQQQ | 3.76 | — | rebalance up |
| 2026-11-11T15:16 | Candlestick reversal · 1h | buy | ETHU | 3.51 | — | rebalance up |
| 2026-11-11T15:16 | Candlestick reversal · 1h | buy | BITX | 3.69 | — | rebalance up |
| 2026-11-11T15:16 | Candlestick reversal · 1h | sell | MSFT | 10.63 | -0.16 | stop-loss |
| 2026-11-11T15:16 | Opening range 30m | buy | TSLA | 22.05 | — | entry signal |
| 2026-11-11T15:16 | Opening range 15m | buy | TSLA | 20.17 | — | entry signal |
| 2026-11-11T15:16 | Gap and go | buy | TSLA | 24.64 | — | entry signal |
| 2026-11-11T15:10 | Agent (ML meta-label) | buy | SOXL | 5.90 | — | rebalance up |
| 2026-11-11T15:10 | Agent (ML meta-label) | buy | COIN | 4.47 | — | rebalance up |
| 2026-11-11T15:10 | Agent (ML meta-label) | sell | TSLA | 10.36 | 0.05 | selected signal exited |
| 2026-11-11T15:10 | OBV trend · 1h | buy | META | 3.59 | — | rebalance up |
| 2026-11-11T15:05 | Agent (ML meta-label) | buy | TECL | 10.21 | — | entry |
| 2026-11-11T15:05 | Agent (ML meta-label) | buy | SOXL | 4.97 | — | entry |
| 2026-11-11T15:05 | Agent (ML meta-label) | sell | TSLA | 4.29 | -0.01 | rebalance down |
| 2026-11-11T15:05 | Agent (ML meta-label) | sell | META | 4.56 | -0.01 | rebalance down |
| 2026-11-11T15:05 | Agent (ML meta-label) | sell | AMZN | 6.33 | -0.02 | rebalance down |
| 2026-11-11T15:05 | Agent | sell | COIN | 17.20 | -0.29 | selected signal exited |
| 2026-11-11T15:01 | Agent (ML meta-label) | buy | TSLA | 14.61 | — | entry |
| 2026-11-11T15:01 | Agent (ML meta-label) | buy | META | 14.89 | — | entry |
| 2026-11-11T15:01 | Agent (ML meta-label) | sell | SOXL | 16.60 | 0.16 | selected signal exited |
| 2026-11-11T15:01 | Agent (ML meta-label) | sell | COIN | 9.46 | 0.13 | rebalance down |
| 2026-11-11T15:01 | Candlestick reversal · 1h | buy | MSFT | 3.73 | — | rebalance up |
| 2026-11-11T15:01 | Candlestick reversal · 1h | buy | ETH-USD | 3.63 | — | rebalance up |
| 2026-11-11T15:01 | Candlestick reversal · 1h | buy | BTC-USD | 3.67 | — | rebalance up |
| 2026-11-11T15:01 | Candlestick reversal · 1h | sell | XRP-USD | 9.13 | -0.03 | exit signal |
| 2026-11-11T15:01 | VWAP momentum · 1h | buy | TQQQ | 1.29 | — | entry |
| 2026-11-11T15:01 | VWAP momentum · 1h | buy | SOL-USD | 4.81 | — | entry |
| 2026-11-11T15:01 | VWAP momentum · 1h | sell | DOGE-USD | 2.02 | -0.01 | exit signal |
| 2026-11-11T15:01 | VWAP momentum · 1h | sell | BTC-USD | 4.08 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 15:24:05.000133+00:00 -> 2026-11-11 15:34:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
