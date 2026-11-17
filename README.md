# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T01:11:05.000159+00:00 · 62557 ticks

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
| Copy: Insider buying | 2026-11-16 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 900 decisions in 180 calls, $0.0126 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T01:11 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-17T01:11 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T01:11 | 2 / 3 / 0 | ETH-USD 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.06 | 18.06 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.76 | 3.76 | 0 | — | 5.51 | 1.52 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.64 | -3.36 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.84 | -6.16 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.68 | -8.32 | 47 | 42.6 | -10.04 | -2.01 | -14.95 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.58 | -8.42 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.40 | -12.60 | 67 | 20.9 | -8.83 | -2.62 | -16.01 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.68 | -13.32 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.10 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.24 | -16.76 | 180 | 28.3 | -19.89 | -4.89 | -24.65 | 215 |
| 28 | Keltner breakout · 1h | breakout | 80.59 | -19.41 | 121 | 25.6 | -19.20 | -4.40 | -25.84 | 157 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -22.94 | -5.30 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 213 | 39.9 | -14.21 | -6.23 | -14.88 | 98 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.38 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.12 | -21.88 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.32 | -22.68 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.65 | -24.36 | 2 | 0.0 | -14.74 | -2.06 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.12 | -8.29 | -31.62 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.93 | -25.07 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.35 | -25.65 | 185 | 22.2 | -23.89 | -5.00 | -31.78 | 234 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | MACD zero-line · 1h | trend | 72.10 | -27.90 | 174 | 18.4 | -25.35 | -5.00 | -31.74 | 195 |
| 42 | MFI reversion · 1h | reversion | 72.07 | -27.93 | 419 | 34.1 | -25.79 | -3.66 | -29.26 | 165 |
| 43 | Heikin-Ashi · 1h | trend | 71.79 | -28.21 | 459 | 23.3 | -39.07 | -7.45 | -43.26 | 637 |
| 44 | Supertrend · 1h | trend | 71.43 | -28.57 | 187 | 16.0 | -32.51 | -5.53 | -39.67 | 200 |
| 45 | RSI momentum · 1h | momentum | 71.26 | -28.74 | 175 | 14.3 | -31.25 | -5.65 | -38.07 | 202 |
| 46 | Triple EMA stack · 1h | trend | 71.23 | -28.77 | 154 | 14.9 | -28.26 | -5.08 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.94 | -29.06 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.77 | -29.23 | 403 | 22.6 | -33.97 | -4.92 | -43.17 | 476 |
| 49 | ROC + volume · 1h | momentum | 70.65 | -29.35 | 404 | 28.5 | -27.88 | -4.56 | -37.95 | 356 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.22 | -30.78 | 303 | 19.1 | -30.32 | -5.44 | -39.75 | 261 |
| 52 | CCI reversion · 1h | reversion | 67.91 | -32.09 | 377 | 41.9 | -40.21 | -6.52 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.70 | -32.30 | 157 | 18.5 | -30.07 | -4.91 | -39.25 | 206 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | EMA 9/21 cross · 1h | trend | 64.06 | -35.95 | 273 | 11.4 | -38.66 | -7.57 | -44.83 | 317 |
| 56 | Williams %R · 1h | reversion | 64.05 | -35.95 | 418 | 41.1 | -44.33 | -7.42 | -45.12 | 546 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -22.93 | -3.51 | -27.67 | 339 |
| 58 | Z-score reversion · 1h | reversion | 59.60 | -40.40 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.30 | -40.70 | 204 | 31.9 | -40.74 | -5.99 | -42.17 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.45 | -41.55 | 944 | 21.7 | -53.12 | -9.37 | -57.50 | 1209 |
| 61 | Candlestick reversal · 1h | reversion | 57.30 | -42.70 | 537 | 27.0 | -45.12 | -8.10 | -45.56 | 615 |
| 62 | Three white soldiers | momentum | 56.57 | -43.43 | 570 | 14.7 | -48.98 | -21.57 | -48.98 | 655 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -41.77 | -99.02 | 5299 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.42 | -25.35 | -81.43 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.99 | -42.40 | -93.99 | 2508 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.95 | -30.95 | -89.96 | 1931 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -39.31 | -91.39 | 2320 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.11 | -30.04 | -90.12 | 2152 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -45.81 | -97.91 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -51.23 | -96.47 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.57 | -37.02 | -93.57 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.78 | -32.94 | -82.78 | 1635 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -51.44 | -99.59 | 6044 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -40.78 | -92.10 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.24 | -35.84 | -95.24 | 3359 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -66.28 | -99.81 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.36 | -41.79 | -92.36 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.43 | -25.59 | -76.43 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -56.78 | -97.60 | 3466 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -53.09 | -98.99 | 4939 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.48 | -26.80 | -68.48 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -52.65 | -94.69 | 2751 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -36.84 | -84.65 | 1743 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -63.09 | -99.69 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.47 | -29.78 | -90.50 | 2339 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.56 | -18.47 | -79.59 | 1815 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.00 | -35.18 | -91.01 | 2181 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -43.77 | -97.45 | 3902 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.14 | -56.05 | -89.14 | 2146 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -29.24 | -66.40 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.01 | -23.07 | -72.02 | 1246 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.30 | -17.50 | -80.53 | 1752 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.57 | -44.60 | -97.58 | 4360 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -90.82 | -99.94 | 8393 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T01:00 | Bollinger breakout · 1h | sell | ETH-USD | 18.24 | -0.41 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.88 | — | rebalance up |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | ETH-USD | 9.69 | -0.09 | exit signal |
| 2026-11-17T01:00 | VWAP momentum · 1h | sell | BTC-USD | 9.68 | -0.09 | exit signal |
| 2026-11-17T01:00 | MACD zero-line · 1h | sell | DOGE-USD | 17.82 | -0.31 | exit signal |
| 2026-11-17T01:00 | MACD cross · 1h | buy | XRP-USD | 4.13 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | SOL-USD | 4.00 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | ETH-USD | 4.06 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | buy | BTC-USD | 4.03 | — | rebalance up |
| 2026-11-17T01:00 | MACD cross · 1h | sell | DOGE-USD | 9.99 | -0.13 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 01:11:05.000159+00:00 -> 2026-11-17 01:21:05.000159+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 01:11:05.000159+00:00 -> 2026-11-17 01:21:05.000159+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
