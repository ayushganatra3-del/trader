# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-16T00:40:05.000207+00:00 · 61272 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.50 (-14.50%)

Closed trades 195, win rate 35.9%, fees £5.63, max drawdown -15.42%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-14 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-13)

**Correction** since 2026-11-13 · level correction · 1 distribution days in 25 sessions · timing exposure 0% · VXN 29.38 · VIX 19.30 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.9, AMZN 5.6, TSLA 5.2, META 3.4, AMD 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 570 decisions in 114 calls, $0.0080 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-16T00:40 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-11-16T00:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-16T00:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.82 | +5.11% | 10 |
| RSI momentum | TNA | 2.47 | +2.95% | 5 |
| CCI reversion | SOXL | 2.19 | +16.29% | 10 |
| Bollinger reversion | TSLA | 2.18 | +2.18% | 6 |
| RSI momentum | IWM | 2.10 | +0.63% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.89 | 17.89 | 0 | — | 15.31 | 5.02 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.23 | 14.23 | 35 | 31.4 | 22.52 | 2.90 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.21 | 11.21 | 23 | 65.2 | 14.58 | 2.96 | -4.91 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.63 | 4.63 | 0 | — | 6.58 | 1.79 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.88 | 3.88 | 33 | 42.4 | 3.80 | 0.99 | -9.64 | 30 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.96 | 0.96 | 142 | 35.2 | 3.07 | 1.93 | -3.47 | 82 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.59 | 1.84 | -9.06 | 230 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.47 | 0.22 | -18.69 | 7 |
| 11 | Hold SPY | benchmark | 98.33 | -1.67 | 0 | — | -0.61 | -0.22 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.89 | -3.12 | 1 | 0.0 | -3.27 | -2.13 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.69 | -3.31 | 191 | 30.4 | -3.11 | -1.07 | -8.52 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.35 | -3.65 | 0 | — | -4.09 | -1.04 | -9.25 | 1 |
| 15 | Copy: Insider buying | copy | 94.25 | -5.75 | 43 | 39.5 | -6.35 | -1.21 | -15.78 | 58 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.70 | -6.30 | 0 | — | -4.81 | -1.26 | -10.64 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 92.12 | -7.88 | 23 | 17.4 | -10.09 | -8.00 | -10.13 | 22 |
| 19 | Trend pullback · 1h | trend | 91.84 | -8.15 | 110 | 22.7 | -13.63 | -5.99 | -14.95 | 65 |
| 20 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -15.00 | -4.11 | -18.48 | 156 |
| 21 | Squeeze breakout · 1h | breakout | 87.66 | -12.34 | 66 | 21.2 | -3.40 | -0.70 | -15.78 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -10.49 | -2.26 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.82 | -14.19 | 436 | 33.5 | -10.29 | -3.61 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.69 | -14.31 | 16 | 18.8 | -10.26 | -1.97 | -19.56 | 19 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.17 | -7.05 | -15.01 | 193 |
| 26 | Parabolic SAR · 1h | trend | 84.89 | -15.12 | 176 | 29.0 | -15.43 | -3.30 | -22.65 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -14.83 | -4.08 | -16.59 | 92 |
| 28 | Donchian 55/20 · 1h | breakout | 81.99 | -18.01 | 73 | 13.7 | -23.08 | -4.78 | -30.83 | 90 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 80.85 | -19.15 | 2 | 0.0 | -9.89 | -1.38 | -24.16 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 212 | 40.1 | -17.94 | -6.24 | -18.02 | 111 |
| 31 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -16.96 | -3.38 | -25.39 | 165 |
| 32 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 160 | 28.8 | -13.80 | -3.14 | -22.33 | 90 |
| 33 | Stochastic reversion · 1h | reversion | 78.85 | -21.14 | 314 | 46.5 | -25.15 | -3.71 | -28.40 | 407 |
| 34 | Opening range 15m | breakout | 78.27 | -21.73 | 529 | 31.6 | -17.51 | -4.88 | -21.36 | 720 |
| 35 | MFI reversion · 1h | reversion | 77.02 | -22.98 | 407 | 35.1 | -19.89 | -2.57 | -26.60 | 169 |
| 36 | Max aggression: 5-day momentum | meta | 76.15 | -23.85 | 21 | 42.9 | -40.05 | -2.57 | -50.62 | 22 |
| 37 | Hold BTC | benchmark | 75.72 | -24.28 | 2 | 0.0 | -17.14 | -2.41 | -28.91 | 1 |
| 38 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -28.67 | -7.43 | -31.44 | 116 |
| 39 | Max aggression: 1-day momentum | meta | 74.90 | -25.11 | 29 | 27.6 | -21.85 | -0.73 | -57.50 | 40 |
| 40 | Bollinger breakout · 1h | breakout | 74.82 | -25.18 | 183 | 22.4 | -22.94 | -4.74 | -31.00 | 235 |
| 41 | ADX DI cross · 1h | trend | 74.81 | -25.19 | 203 | 19.7 | -25.11 | -3.75 | -34.18 | 272 |
| 42 | Heikin-Ashi · 1h | trend | 74.19 | -25.81 | 450 | 23.8 | -37.95 | -6.95 | -40.63 | 669 |
| 43 | MACD zero-line · 1h | trend | 73.14 | -26.86 | 171 | 18.7 | -23.66 | -4.61 | -31.06 | 200 |
| 44 | RSI momentum · 1h | momentum | 72.60 | -27.40 | 171 | 14.0 | -26.62 | -4.04 | -37.92 | 208 |
| 45 | EMA 20/50 cross · 1h | trend | 72.54 | -27.46 | 109 | 10.1 | -28.21 | -4.71 | -40.51 | 120 |
| 46 | MACD cross · 1h | trend | 71.97 | -28.03 | 393 | 23.2 | -31.61 | -4.65 | -41.23 | 473 |
| 47 | Supertrend · 1h | trend | 71.66 | -28.34 | 182 | 14.8 | -29.73 | -5.01 | -37.37 | 211 |
| 48 | Triple EMA stack · 1h | trend | 71.63 | -28.37 | 151 | 14.6 | -27.31 | -4.46 | -38.65 | 201 |
| 49 | Bollinger reversion · 1h | reversion | 70.85 | -29.15 | 313 | 40.9 | -32.41 | -5.07 | -33.79 | 393 |
| 50 | ROC + volume · 1h | momentum | 70.57 | -29.43 | 399 | 28.8 | -30.28 | -5.41 | -37.90 | 363 |
| 51 | CCI reversion · 1h | reversion | 70.13 | -29.87 | 359 | 42.6 | -35.22 | -5.55 | -39.14 | 470 |
| 52 | OBV trend · 1h | momentum | 69.68 | -30.32 | 299 | 19.1 | -28.52 | -4.90 | -38.36 | 271 |
| 53 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -33.10 | -4.60 | -37.81 | 35 |
| 54 | Donchian 20/10 · 1h | breakout | 68.95 | -31.05 | 153 | 19.0 | -30.22 | -5.37 | -37.68 | 205 |
| 55 | Williams %R · 1h | reversion | 66.14 | -33.85 | 404 | 42.3 | -43.44 | -7.32 | -44.30 | 549 |
| 56 | Agent (ML meta-label) | meta | 65.07 | -34.93 | 1855 | 24.7 | -23.58 | -4.62 | -27.65 | 340 |
| 57 | EMA 9/21 cross · 1h | trend | 64.70 | -35.30 | 267 | 11.6 | -37.53 | -7.52 | -43.33 | 328 |
| 58 | VWAP momentum · 1h | momentum | 62.52 | -37.48 | 917 | 22.2 | -52.04 | -10.17 | -53.34 | 1237 |
| 59 | RSI(14) reversion · 1h | reversion | 61.56 | -38.44 | 199 | 32.2 | -39.01 | -5.70 | -40.40 | 250 |
| 60 | Candlestick reversal · 1h | reversion | 60.91 | -39.09 | 508 | 27.6 | -43.36 | -8.11 | -43.69 | 613 |
| 61 | Z-score reversion · 1h | reversion | 60.67 | -39.33 | 216 | 35.6 | -33.79 | -4.64 | -35.69 | 238 |
| 62 | Three white soldiers | momentum | 57.72 | -42.28 | 557 | 14.9 | -49.39 | -21.61 | -49.39 | 667 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -40.55 | -98.98 | 5303 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.03 | -26.52 | -81.10 | 1429 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.76 | -43.72 | -93.76 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.98 | -32.19 | -89.99 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -41.17 | -91.53 | 2357 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.58 | -29.96 | -89.61 | 2176 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.85 | -48.72 | -97.87 | 3495 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -54.08 | -96.34 | 3465 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -31.35 | -93.61 | 2317 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.04 | -33.34 | -83.05 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.29 | -99.59 | 6061 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.11 | -41.44 | -92.17 | 2625 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.20 | -35.34 | -95.20 | 3449 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -66.83 | -99.82 | 6178 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -41.71 | -92.40 | 2291 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.20 | -25.86 | -76.39 | 1675 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -55.88 | -97.59 | 3499 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.98 | -53.15 | -98.99 | 4964 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.06 | -26.86 | -69.22 | 1245 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -53.51 | -94.70 | 2800 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -36.84 | -84.82 | 1776 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.02 | -99.69 | 6398 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.90 | -29.86 | -90.91 | 2352 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -80.23 | -18.59 | -80.92 | 1829 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.14 | -34.87 | -91.17 | 2196 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.43 | -43.50 | -97.43 | 3922 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -54.94 | -89.28 | 2169 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.46 | -29.32 | -66.58 | 832 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.29 | -23.18 | -72.31 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -81.33 | -17.59 | -81.88 | 1763 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.23 | -97.59 | 4361 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -89.09 | -99.93 | 8458 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-16T00:00 | CCI reversion · 1h | sell | XRP-USD | 4.32 | 0.20 | exit signal |
| 2026-11-16T00:00 | Williams %R · 1h | sell | XRP-USD | 4.20 | 0.07 | exit signal |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | buy | ETH-USD | 4.64 | — | rebalance up |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | buy | BTC-USD | 4.67 | — | rebalance up |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | sell | SOL-USD | 8.90 | 0.11 | exit signal |
| 2026-11-16T00:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 7.79 | 0.12 | exit signal |
| 2026-11-16T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 3.82 | — | entry |
| 2026-11-16T00:00 | Candlestick reversal · 1h | sell | DOGE-USD | 3.88 | 0.08 | exit signal |
| 2026-11-16T00:00 | Volume breakout · 1h | buy | DOGE-USD | 20.13 | — | entry signal |
| 2026-11-16T00:00 | Squeeze breakout · 1h | buy | DOGE-USD | 22.00 | — | entry signal |
| 2026-11-16T00:00 | Bollinger breakout · 1h | buy | DOGE-USD | 18.78 | — | entry signal |
| 2026-11-16T00:00 | Donchian 20/10 · 1h | buy | DOGE-USD | 17.26 | — | entry signal |
| 2026-11-16T00:00 | ROC + volume · 1h | buy | SOL-USD | 17.80 | — | entry signal |
| 2026-11-16T00:00 | ROC + volume · 1h | buy | DOGE-USD | 17.80 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | SOL-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | DOGE-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | ADX DI cross · 1h | buy | BTC-USD | 15.10 | — | entry signal |
| 2026-11-16T00:00 | Parabolic SAR · 1h | buy | XRP-USD | 21.08 | — | entry signal |
| 2026-11-16T00:00 | Supertrend · 1h | buy | DOGE-USD | 3.77 | — | entry signal |
| 2026-11-16T00:00 | Supertrend · 1h | sell | XRP-USD | 3.77 | 0.00 | rebalance down |
| 2026-11-16T00:00 | MACD zero-line · 1h | buy | XRP-USD | 18.37 | — | entry signal |
| 2026-11-15T23:15 | Three white soldiers | sell | XRP-USD | 14.30 | -0.18 | stop-loss |
| 2026-11-15T23:05 | Three white soldiers | buy | XRP-USD | 14.48 | — | entry signal |
| 2026-11-15T23:00 | CCI reversion · 1h | sell | DOGE-USD | 3.36 | 0.02 | exit signal |
| 2026-11-15T23:00 | Z-score reversion · 1h | sell | XRP-USD | 10.21 | 0.12 | exit signal |
| 2026-11-15T23:00 | Heikin-Ashi · 1h | buy | SOL-USD | 8.26 | — | entry signal |
| 2026-11-15T20:05 | Three white soldiers | sell | XRP-USD | 14.45 | -0.05 | exit signal |
| 2026-11-15T20:00 | Three white soldiers | sell | SOL-USD | 14.45 | -0.05 | exit signal |
| 2026-11-15T19:10 | Three white soldiers | buy | XRP-USD | 14.50 | — | entry signal |
| 2026-11-15T19:10 | Three white soldiers | buy | SOL-USD | 14.50 | — | entry signal |
| 2026-11-15T19:00 | Williams %R · 1h | buy | XRP-USD | 4.13 | — | entry signal |
| 2026-11-15T18:30 | Three white soldiers | sell | ETH-USD | 14.48 | -0.13 | exit signal |
| 2026-11-15T18:15 | Three white soldiers | sell | SOL-USD | 14.45 | -0.16 | exit signal |
| 2026-11-15T18:15 | Three white soldiers | sell | DOGE-USD | 14.46 | -0.15 | exit signal |
| 2026-11-15T18:05 | Three white soldiers | buy | SOL-USD | 14.61 | — | entry signal |
| 2026-11-15T18:05 | Three white soldiers | buy | ETH-USD | 14.61 | — | entry signal |
| 2026-11-15T18:05 | Three white soldiers | buy | DOGE-USD | 14.61 | — | entry signal |
| 2026-11-15T15:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 2.77 | -0.05 | exit signal |
| 2026-11-15T15:00 | Heikin-Ashi · 1h | sell | BTC-USD | 6.09 | -0.11 | exit signal |
| 2026-11-15T15:00 | ADX DI cross · 1h | sell | XRP-USD | 18.69 | -0.35 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-18 00:40:05.000207+00:00 -> 2026-11-16 00:50:05.000207+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
