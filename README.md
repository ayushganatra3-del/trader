# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T18:35:05.000150+00:00 · 63468 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.77 (-15.23%)

Closed trades 214, win rate 35.5%, fees £6.00, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 16.80 | +0.08 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 29517 decisions in 2913 calls, $0.3718 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T18:35 | 3 / 13 / 14 | TECL 15% |  |
| Breezy | 2026-11-17T18:35 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-17T18:35 | 6 / 22 / 2 | ETHU 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.40 | 17.40 | 0 | — | 13.79 | 4.60 | -4.64 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.07 | 10.07 | 24 | 62.5 | 15.59 | 3.18 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.98 | 2.98 | 0 | — | 5.21 | 1.44 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.79 | 2.16 | -9.06 | 224 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.33 | -2.84 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.44 | -1.56 | 38 | 39.5 | -2.73 | -0.49 | -9.64 | 34 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.49 | -3.50 | 8 | 50.0 | -1.39 | 0.15 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.43 | -4.57 | 0 | — | -2.63 | -0.81 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.43 | -8.63 | -5.59 | 20 |
| 14 | Agent (rotation) | meta | 93.68 | -6.32 | 197 | 29.9 | -2.98 | -1.03 | -8.29 | 157 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 91.80 | -8.20 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 17 | Copy: Insider buying | copy | 91.13 | -8.87 | 47 | 42.6 | -8.95 | -1.77 | -14.79 | 62 |
| 18 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -16.39 | -7.09 | -18.31 | 68 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.11 | -9.89 | 0 | — | -8.43 | -2.27 | -12.67 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 22 | Daily: Bullish score | daily | 87.08 | -12.92 | 17 | 17.6 | -4.11 | -0.61 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -15.78 | -5.15 | -20.74 | 77 |
| 24 | Opening range 30m | breakout | 86.12 | -13.88 | 438 | 33.6 | -9.93 | -3.15 | -14.11 | 575 |
| 25 | Agent | meta | 84.77 | -15.23 | 214 | 35.5 | -14.99 | -7.03 | -16.88 | 204 |
| 26 | Agent (aggressive) | meta | 82.33 | -17.67 | 100 | 34.0 | -16.73 | -4.61 | -19.92 | 98 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -25.63 | -6.97 | -27.58 | 202 |
| 28 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 122 | 26.2 | -23.08 | -5.62 | -28.34 | 156 |
| 29 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.64 | -6.48 | -15.05 | 93 |
| 30 | Max aggression: 5-day momentum | meta | 79.87 | -20.13 | 21 | 42.9 | -47.95 | -3.17 | -55.24 | 22 |
| 31 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.51 | -29.47 | 83 |
| 32 | Volume breakout · 1h | breakout | 79.71 | -20.29 | 162 | 28.4 | -15.58 | -4.85 | -22.08 | 79 |
| 33 | Opening range 15m | breakout | 78.06 | -21.94 | 533 | 31.5 | -16.71 | -4.48 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 76.62 | -23.38 | 30 | 26.7 | -24.21 | -0.92 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.10 | -23.90 | 2 | 0.0 | -14.16 | -1.71 | -26.43 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.28 | -8.50 | -29.80 | 111 |
| 37 | ADX DI cross · 1h | trend | 75.05 | -24.95 | 208 | 19.2 | -26.39 | -4.18 | -34.71 | 259 |
| 38 | Hold BTC | benchmark | 74.45 | -25.55 | 2 | 0.0 | -16.00 | -2.26 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.48 | -5.73 | -33.49 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 73.06 | -26.94 | 345 | 42.6 | -34.21 | -5.16 | -35.87 | 423 |
| 41 | Supertrend · 1h | trend | 71.27 | -28.73 | 189 | 15.9 | -32.76 | -5.51 | -39.97 | 199 |
| 42 | Triple EMA stack · 1h | trend | 70.98 | -29.02 | 155 | 14.8 | -31.00 | -6.24 | -36.52 | 184 |
| 43 | RSI momentum · 1h | momentum | 70.95 | -29.05 | 176 | 14.2 | -30.82 | -5.59 | -37.29 | 197 |
| 44 | MFI reversion · 1h | reversion | 70.65 | -29.35 | 428 | 33.9 | -26.65 | -3.85 | -30.64 | 165 |
| 45 | MACD zero-line · 1h | trend | 70.57 | -29.43 | 181 | 17.7 | -26.48 | -5.22 | -32.76 | 198 |
| 46 | EMA 20/50 cross · 1h | trend | 69.81 | -30.19 | 115 | 10.4 | -36.82 | -9.90 | -39.68 | 115 |
| 47 | Heikin-Ashi · 1h | trend | 69.63 | -30.37 | 466 | 23.0 | -41.57 | -8.32 | -44.74 | 633 |
| 48 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 49 | ROC + volume · 1h | momentum | 69.37 | -30.63 | 408 | 28.2 | -30.13 | -4.81 | -39.26 | 352 |
| 50 | MACD cross · 1h | trend | 69.02 | -30.98 | 413 | 22.3 | -39.70 | -6.46 | -44.78 | 470 |
| 51 | OBV trend · 1h | momentum | 68.31 | -31.69 | 306 | 19.0 | -36.13 | -7.67 | -39.93 | 263 |
| 52 | Donchian 20/10 · 1h | breakout | 67.23 | -32.77 | 159 | 18.2 | -31.17 | -5.27 | -39.19 | 204 |
| 53 | CCI reversion · 1h | reversion | 66.86 | -33.14 | 382 | 41.6 | -41.06 | -6.71 | -44.29 | 465 |
| 54 | Bollinger reversion · 1h | reversion | 64.14 | -35.86 | 344 | 37.8 | -38.47 | -5.80 | -39.50 | 414 |
| 55 | Williams %R · 1h | reversion | 63.08 | -36.92 | 430 | 40.7 | -45.71 | -7.77 | -46.94 | 560 |
| 56 | EMA 9/21 cross · 1h | trend | 63.01 | -36.99 | 280 | 11.1 | -37.59 | -7.08 | -44.92 | 319 |
| 57 | Agent (ML meta-label) | meta | 60.19 | -39.81 | 1889 | 24.5 | -27.54 | -5.35 | -28.00 | 329 |
| 58 | RSI(14) reversion · 1h | reversion | 58.34 | -41.66 | 205 | 31.7 | -40.78 | -5.99 | -42.91 | 248 |
| 59 | Z-score reversion · 1h | reversion | 57.38 | -42.62 | 224 | 35.3 | -37.27 | -5.16 | -39.23 | 253 |
| 60 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -53.40 | -9.55 | -58.06 | 1195 |
| 61 | Three white soldiers | momentum | 55.30 | -44.70 | 582 | 14.6 | -49.37 | -21.62 | -49.93 | 660 |
| 62 | Candlestick reversal · 1h | reversion | 55.18 | -44.82 | 546 | 26.6 | -47.89 | -8.70 | -49.45 | 625 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -42.22 | -99.02 | 5265 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.78 | -25.62 | -82.04 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.09 | -41.63 | -94.10 | 2491 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.13 | -31.19 | -90.38 | 1942 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -38.59 | -91.47 | 2309 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.86 | -30.55 | -89.86 | 2120 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -45.76 | -97.92 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -51.77 | -96.54 | 3419 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -37.45 | -93.58 | 2218 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.04 | -32.07 | -83.12 | 1613 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.83 | -99.60 | 6060 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.99 | -40.64 | -92.05 | 2568 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.02 | -37.85 | -95.04 | 3313 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -64.22 | -99.81 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.34 | -42.07 | -92.34 | 2253 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.28 | -25.60 | -76.28 | 1646 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -56.67 | -97.66 | 3445 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.39 | -99.03 | 4939 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.49 | -26.66 | -68.56 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.50 | -52.07 | -94.52 | 2739 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.22 | -36.29 | -84.22 | 1731 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -64.50 | -99.70 | 6358 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -30.20 | -90.90 | 2358 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.50 | -18.41 | -79.85 | 1821 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.13 | -35.47 | -91.23 | 2148 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.53 | -44.33 | -97.56 | 3898 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -55.02 | -89.39 | 2168 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.13 | -29.68 | -66.13 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.07 | -22.94 | -72.51 | 1228 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.33 | -17.51 | -80.69 | 1717 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.84 | -97.61 | 4333 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.58 | -99.94 | 8440 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T18:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.44 | -1.30 | target is flat |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | META | 7.43 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | LABU | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | GOOGL | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | COIN | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | AMD | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | SOXL | 10.13 | 0.28 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | ETHU | 9.09 | 0.13 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | AMZN | 9.06 | -0.03 | rebalance down |
| 2026-11-17T18:30 | CCI reversion · 1h | sell | AAPL | 8.92 | -0.07 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | UPRO | 3.06 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | TQQQ | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | TNA | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | SPY | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | QQQ | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | MSFT | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | META | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | IWM | 3.07 | — | entry signal |
| 2026-11-17T18:30 | Candlestick reversal · 1h | buy | DOGE-USD | 3.07 | — | entry |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | TSLA | 3.05 | -0.01 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | TECL | 3.09 | 0.03 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | SOXL | 3.05 | 0.04 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | PLTR | 3.09 | 0.02 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | NVDA | 3.05 | -0.02 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | MSTR | 3.02 | -0.02 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | ETHU | 3.16 | 0.04 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | AMD | 3.06 | -0.00 | rebalance down |
| 2026-11-17T18:30 | Candlestick reversal · 1h | sell | AAPL | 3.05 | -0.01 | rebalance down |
| 2026-11-17T18:30 | Three white soldiers | buy | SOXL | 13.84 | — | entry signal |
| 2026-11-17T18:30 | Three white soldiers | buy | META | 13.84 | — | entry signal |
| 2026-11-17T18:15 | Three white soldiers | sell | AMZN | 13.80 | -0.05 | exit signal |
| 2026-11-17T18:11 | Agent | sell | TNA | 16.76 | -0.30 | selected signal exited |
| 2026-11-17T18:11 | Agent | sell | BITX | 16.93 | -0.03 | selected signal exited |
| 2026-11-17T18:11 | MFI reversion · 1h | buy | GOOGL | 10.07 | — | entry |
| 2026-11-17T18:11 | MFI reversion · 1h | sell | LABU | 7.10 | 0.23 | target is flat |
| 2026-11-17T18:05 | Agent (ML meta-label) | sell | SQQQ | 15.03 | -0.02 | selected signal exited |
| 2026-11-17T18:05 | Agent | buy | BITX | 16.96 | — | following MFI reversion |
| 2026-11-17T18:05 | Agent | sell | IWM | 16.96 | -0.02 | selected signal exited |
| 2026-11-17T18:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 99.74 | — | entry |
| 2026-11-17T18:00 | Agent (ML meta-label) | buy | SQQQ | 15.05 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 18:35:05.000150+00:00 -> 2026-11-17 18:45:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 18:35:05.000150+00:00 -> 2026-11-17 18:45:05.000150+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
