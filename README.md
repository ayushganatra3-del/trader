# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T00:10:05.000145+00:00 · 62506 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.11 (-13.89%)

Closed trades 203, win rate 36.5%, fees £5.77, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-16 | MDGL 12%, KOD 12%, FUN 12%, STWD 12%, KMI 12%, LRN 12%, PSEC 12%, BH 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 135 decisions in 27 calls, $0.0019 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T00:10 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-11-17T00:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T00:10 | 4 / 1 / 0 | ETH-USD 50% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.04 | 18.04 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.71 | 3.71 | 0 | — | 5.47 | 1.51 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.62 | -3.38 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -2.82 | -0.97 | -8.15 | 158 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.83 | -6.17 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.67 | -8.33 | 47 | 42.6 | -10.04 | -2.01 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.57 | -8.43 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -10.76 | -3.99 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.67 | -13.33 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.27 | -16.73 | 180 | 28.3 | -17.87 | -3.89 | -24.65 | 216 |
| 28 | Keltner breakout · 1h | breakout | 80.58 | -19.42 | 121 | 25.6 | -18.48 | -3.98 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -22.85 | -5.25 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.30 | -19.70 | 213 | 39.9 | -14.21 | -6.24 | -14.88 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.10 | -21.90 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.30 | -22.70 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.74 | -24.26 | 2 | 0.0 | -14.77 | -2.06 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.03 | -8.26 | -31.55 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.92 | -25.08 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.45 | -25.55 | 184 | 22.3 | -24.42 | -5.21 | -31.78 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | MACD zero-line · 1h | trend | 72.24 | -27.75 | 173 | 18.5 | -25.20 | -4.96 | -31.65 | 195 |
| 42 | MFI reversion · 1h | reversion | 72.09 | -27.91 | 419 | 34.1 | -25.64 | -3.63 | -29.09 | 163 |
| 43 | Heikin-Ashi · 1h | trend | 71.79 | -28.21 | 459 | 23.3 | -39.07 | -7.45 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.47 | -28.53 | 187 | 16.0 | -32.45 | -5.51 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.26 | -28.74 | 175 | 14.3 | -28.10 | -4.59 | -38.07 | 204 |
| 46 | Triple EMA stack · 1h | trend | 71.22 | -28.78 | 154 | 14.9 | -28.05 | -5.00 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.93 | -29.07 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.88 | -29.12 | 402 | 22.6 | -33.84 | -4.86 | -43.17 | 476 |
| 49 | ROC + volume · 1h | momentum | 70.66 | -29.34 | 404 | 28.5 | -28.18 | -4.62 | -37.95 | 357 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.21 | -30.79 | 303 | 19.1 | -29.59 | -5.23 | -39.29 | 259 |
| 52 | CCI reversion · 1h | reversion | 67.91 | -32.09 | 377 | 41.9 | -40.20 | -6.52 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.71 | -32.29 | 157 | 18.5 | -30.05 | -4.91 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | EMA 9/21 cross · 1h | trend | 64.09 | -35.91 | 273 | 11.4 | -37.71 | -7.13 | -44.79 | 318 |
| 56 | Williams %R · 1h | reversion | 64.06 | -35.94 | 418 | 41.1 | -44.31 | -7.41 | -45.12 | 546 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -28.10 | -4.81 | -32.49 | 327 |
| 58 | Z-score reversion · 1h | reversion | 59.59 | -40.41 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.29 | -40.71 | 204 | 31.9 | -39.75 | -5.77 | -42.13 | 245 |
| 60 | VWAP momentum · 1h | momentum | 58.56 | -41.44 | 942 | 21.8 | -53.24 | -9.31 | -57.64 | 1208 |
| 61 | Candlestick reversal · 1h | reversion | 57.30 | -42.70 | 537 | 27.0 | -45.66 | -8.24 | -45.84 | 617 |
| 62 | Three white soldiers | momentum | 56.57 | -43.43 | 570 | 14.7 | -49.15 | -21.60 | -49.15 | 657 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -41.17 | -99.02 | 5300 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.44 | -25.36 | -81.45 | 1432 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.05 | -42.36 | -94.05 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.05 | -31.15 | -90.07 | 1936 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.44 | -39.31 | -91.44 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -30.04 | -90.12 | 2152 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -45.75 | -97.93 | 3464 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -51.70 | -96.53 | 3446 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -36.65 | -93.56 | 2266 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.87 | -33.03 | -82.87 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.01 | -99.59 | 6048 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.14 | -40.78 | -92.14 | 2582 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.24 | -35.75 | -95.24 | 3359 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -65.60 | -99.81 | 6149 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.36 | -41.79 | -92.36 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.44 | -25.60 | -76.44 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.89 | -97.62 | 3469 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -52.69 | -98.99 | 4943 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.48 | -26.80 | -68.48 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -52.63 | -94.69 | 2752 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.76 | -36.68 | -84.76 | 1747 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -62.48 | -99.69 | 6380 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.47 | -29.75 | -90.49 | 2339 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.60 | -18.49 | -79.63 | 1818 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.00 | -35.07 | -91.02 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.44 | -43.43 | -97.44 | 3907 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.20 | -55.79 | -89.22 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.24 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.01 | -23.07 | -72.02 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.26 | -17.46 | -80.58 | 1754 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.23 | -97.57 | 4361 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.38 | -99.94 | 8396 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T00:00 | MFI reversion · 1h | buy | ETH-USD | 7.21 | — | entry |
| 2026-11-17T00:00 | MFI reversion · 1h | buy | BTC-USD | 7.21 | — | entry |
| 2026-11-17T00:00 | Volume breakout · 1h | sell | ETH-USD | 19.61 | -0.38 | exit signal |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | SOL-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | ETH-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | VWAP momentum · 1h | buy | BTC-USD | 9.77 | — | entry |
| 2026-11-17T00:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.53 | -0.08 | exit signal |
| 2026-11-16T23:00 | CCI reversion · 1h | sell | SOL-USD | 13.71 | 0.09 | exit signal |
| 2026-11-16T22:00 | CCI reversion · 1h | sell | BTC-USD | 17.12 | 0.08 | exit signal |
| 2026-11-16T22:00 | RSI(14) reversion · 1h | sell | BTC-USD | 12.34 | -0.01 | exit signal |
| 2026-11-16T22:00 | MACD zero-line · 1h | buy | BTC-USD | 18.17 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.61 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 10.76 | — | entry signal |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 5.38 | -0.00 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.22 | -0.05 | rebalance down |
| 2026-11-16T22:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.39 | -0.01 | rebalance down |
| 2026-11-16T21:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 3.26 | — | rebalance up |
| 2026-11-16T21:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 5.64 | -0.06 | exit signal |
| 2026-11-16T20:55 | Agent (rotation) | sell | SQQQ | 31.20 | -0.12 | selected signal exited |
| 2026-11-16T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.39 | 0.42 | target is flat |
| 2026-11-16T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 110.78 | -0.43 | target is flat |
| 2026-11-16T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 91.88 | -0.24 | target is flat |
| 2026-11-16T20:55 | Opening range 30m | sell | SQQQ | 21.74 | 0.28 | end-of-day flatten |
| 2026-11-16T20:55 | Opening range 15m | sell | SQQQ | 19.76 | 0.26 | end-of-day flatten |
| 2026-11-16T20:45 | RSI(14) reversion · 1h | sell | LABU | 13.70 | -1.22 | stop-loss |
| 2026-11-16T20:40 | Agent (aggressive) | sell | COIN | 41.62 | -0.09 | selected signal exited |
| 2026-11-16T20:40 | Agent | sell | COIN | 17.12 | -0.04 | selected signal exited |
| 2026-11-16T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 92.12 | — | entry |
| 2026-11-16T20:30 | Williams %R · 1h | buy | COIN | 5.83 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | MSTR | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | LABU | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | BITX | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | buy | AMZN | 11.99 | — | entry signal |
| 2026-11-16T20:30 | Z-score reversion · 1h | sell | ETHU | 3.05 | 0.01 | rebalance down |
| 2026-11-16T20:30 | RSI(14) reversion · 1h | buy | COIN | 14.89 | — | entry signal |
| 2026-11-16T20:30 | EMA 20/50 cross · 1h | sell | META | 17.70 | -0.19 | exit signal |
| 2026-11-16T20:25 | Three white soldiers | sell | XRP-USD | 14.05 | -0.13 | exit signal |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | TNA | 5.73 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | SOXL | 5.61 | -0.16 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-16T20:15 | Candlestick reversal · 1h | sell | NVDA | 5.74 | -0.15 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 00:10:05.000145+00:00 -> 2026-11-17 00:20:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 00:10:05.000145+00:00 -> 2026-11-17 00:20:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
