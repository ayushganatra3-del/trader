# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T07:10:05.000109+00:00 · 62876 ticks

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
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 5679 decisions in 1137 calls, $0.0794 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T07:10 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-11-17T07:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T07:10 | 3 / 2 / 0 | SOL-USD 62% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.93 | 17.93 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.61 | 3.61 | 0 | — | 5.47 | 1.51 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.53 | -3.46 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.74 | -6.26 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.58 | -8.42 | 47 | 42.6 | -8.37 | -1.64 | -14.79 | 59 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.48 | -8.52 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.30 | -12.70 | 67 | 20.9 | -11.28 | -4.43 | -16.32 | 79 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.61 | -13.39 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.11 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.33 | -16.67 | 180 | 28.3 | -22.78 | -6.14 | -24.73 | 213 |
| 28 | Keltner breakout · 1h | breakout | 80.56 | -19.44 | 121 | 25.6 | -19.01 | -4.25 | -25.84 | 158 |
| 29 | Donchian 55/20 · 1h | breakout | 80.49 | -19.51 | 76 | 13.2 | -25.67 | -6.60 | -28.90 | 86 |
| 30 | Connors RSI(2) · 1h | reversion | 80.27 | -19.73 | 213 | 39.9 | -14.54 | -6.43 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.03 | -21.97 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.23 | -22.77 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.53 | -24.47 | 2 | 0.0 | -14.61 | -2.03 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -31.24 | -8.80 | -31.74 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.85 | -25.15 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.72 | -25.28 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Bollinger breakout · 1h | breakout | 74.12 | -25.88 | 185 | 22.2 | -24.66 | -5.28 | -31.87 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 41 | MFI reversion · 1h | reversion | 72.10 | -27.90 | 420 | 34.3 | -25.52 | -3.62 | -29.02 | 162 |
| 42 | Supertrend · 1h | trend | 71.74 | -28.27 | 187 | 16.0 | -32.10 | -5.43 | -39.67 | 200 |
| 43 | MACD zero-line · 1h | trend | 71.71 | -28.29 | 177 | 18.1 | -25.70 | -5.08 | -32.32 | 198 |
| 44 | Heikin-Ashi · 1h | trend | 71.45 | -28.55 | 461 | 23.2 | -39.32 | -7.52 | -43.26 | 639 |
| 45 | Triple EMA stack · 1h | trend | 71.21 | -28.79 | 154 | 14.9 | -30.21 | -5.81 | -37.77 | 192 |
| 46 | RSI momentum · 1h | momentum | 71.20 | -28.80 | 175 | 14.3 | -31.04 | -5.60 | -38.07 | 203 |
| 47 | EMA 20/50 cross · 1h | trend | 70.90 | -29.10 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | MACD cross · 1h | trend | 70.64 | -29.36 | 407 | 22.4 | -33.64 | -4.82 | -43.43 | 476 |
| 49 | ROC + volume · 1h | momentum | 70.56 | -29.44 | 405 | 28.4 | -28.30 | -4.65 | -37.95 | 355 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.18 | -30.82 | 303 | 19.1 | -31.39 | -6.08 | -39.29 | 259 |
| 52 | CCI reversion · 1h | reversion | 68.04 | -31.96 | 378 | 42.1 | -40.07 | -6.48 | -42.07 | 454 |
| 53 | Donchian 20/10 · 1h | breakout | 67.71 | -32.29 | 157 | 18.5 | -30.27 | -4.96 | -39.25 | 207 |
| 54 | Bollinger reversion · 1h | reversion | 66.56 | -33.45 | 333 | 39.0 | -36.36 | -5.48 | -36.96 | 405 |
| 55 | Williams %R · 1h | reversion | 64.21 | -35.79 | 420 | 41.4 | -44.53 | -7.48 | -45.12 | 543 |
| 56 | EMA 9/21 cross · 1h | trend | 63.94 | -36.06 | 276 | 11.2 | -38.75 | -7.60 | -45.10 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -27.80 | -4.40 | -32.26 | 312 |
| 58 | Z-score reversion · 1h | reversion | 59.54 | -40.46 | 221 | 35.7 | -34.78 | -4.76 | -36.18 | 242 |
| 59 | RSI(14) reversion · 1h | reversion | 59.27 | -40.73 | 204 | 31.9 | -40.69 | -5.98 | -42.13 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.31 | -41.69 | 947 | 21.6 | -53.13 | -9.28 | -57.87 | 1207 |
| 61 | Candlestick reversal · 1h | reversion | 57.23 | -42.77 | 537 | 27.0 | -45.63 | -8.24 | -45.69 | 615 |
| 62 | Three white soldiers | momentum | 56.30 | -43.70 | 572 | 14.7 | -49.27 | -21.88 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -42.99 | -98.98 | 5280 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.34 | -25.62 | -81.60 | 1431 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.01 | -43.49 | -94.01 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.98 | -31.21 | -90.00 | 1935 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -40.33 | -91.46 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.15 | -30.01 | -90.15 | 2156 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.91 | -46.95 | -97.91 | 3461 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -52.72 | -96.48 | 3442 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -37.28 | -93.55 | 2261 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -33.42 | -82.87 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.70 | -99.60 | 6054 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -41.65 | -92.10 | 2582 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.25 | -35.83 | -95.25 | 3356 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.37 | -99.81 | 6150 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.33 | -42.90 | -92.33 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.65 | -26.18 | -76.65 | 1653 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -58.94 | -97.62 | 3471 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -54.32 | -99.00 | 4941 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.85 | -27.51 | -68.85 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -55.56 | -94.74 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.68 | -37.62 | -84.68 | 1745 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.46 | -99.69 | 6376 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.44 | -29.68 | -90.47 | 2335 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.54 | -18.45 | -79.61 | 1818 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.94 | -34.98 | -91.00 | 2172 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.45 | -44.41 | -97.45 | 3903 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -58.34 | -89.28 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.52 | -30.01 | -66.52 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.21 | -23.37 | -72.21 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.19 | -17.44 | -80.48 | 1752 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.11 | -97.57 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.91 | -99.94 | 8398 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | SOL-USD | 4.35 | — | rebalance up |
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | ETH-USD | 4.38 | — | rebalance up |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | XRP-USD | 7.22 | -0.11 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.23 | -0.11 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | sell | BTC-USD | 7.23 | -0.11 | exit signal |
| 2026-11-17T07:00 | Heikin-Ashi · 1h | sell | SOL-USD | 17.82 | -0.12 | exit signal |
| 2026-11-17T07:00 | Heikin-Ashi · 1h | sell | ETH-USD | 17.75 | -0.20 | exit signal |
| 2026-11-17T07:00 | Ichimoku · 1h | sell | ETH-USD | 18.63 | -0.21 | exit signal |
| 2026-11-17T07:00 | MACD zero-line · 1h | sell | BTC-USD | 17.34 | -0.24 | exit signal |
| 2026-11-17T07:00 | MACD cross · 1h | buy | ETH-USD | 3.53 | — | rebalance up |
| 2026-11-17T07:00 | MACD cross · 1h | sell | DOGE-USD | 3.40 | -0.04 | exit signal |
| 2026-11-17T07:00 | MACD cross · 1h | sell | BTC-USD | 14.00 | -0.21 | exit signal |
| 2026-11-17T07:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.31 | — | rebalance up |
| 2026-11-17T07:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 10.56 | -0.16 | exit signal |
| 2026-11-17T06:00 | MFI reversion · 1h | sell | ETH-USD | 7.22 | 0.01 | exit signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | SOL-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Heikin-Ashi · 1h | buy | ETH-USD | 17.95 | — | entry signal |
| 2026-11-17T06:00 | Ichimoku · 1h | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-11-17T05:00 | Williams %R · 1h | sell | XRP-USD | 7.25 | 0.08 | exit signal |
| 2026-11-17T05:00 | Squeeze breakout · 1h | buy | SOL-USD | 21.85 | — | entry signal |
| 2026-11-17T05:00 | Donchian 20/10 · 1h | buy | SOL-USD | 16.96 | — | entry signal |
| 2026-11-17T05:00 | MACD zero-line · 1h | buy | BTC-USD | 17.59 | — | entry signal |
| 2026-11-17T05:00 | MACD cross · 1h | buy | DOGE-USD | 3.44 | — | entry signal |
| 2026-11-17T04:00 | CCI reversion · 1h | sell | XRP-USD | 17.19 | 0.16 | exit signal |
| 2026-11-17T04:00 | Williams %R · 1h | sell | SOL-USD | 7.36 | 0.15 | exit signal |
| 2026-11-17T04:00 | Candlestick reversal · 1h | buy | BTC-USD | 7.16 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | Bollinger breakout · 1h | buy | SOL-USD | 18.59 | — | entry signal |
| 2026-11-17T04:00 | RSI momentum · 1h | buy | SOL-USD | 17.81 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | XRP-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | ETH-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | buy | BTC-USD | 7.34 | — | entry signal |
| 2026-11-17T04:00 | VWAP momentum · 1h | sell | SOL-USD | 7.52 | 0.09 | rebalance down |
| 2026-11-17T04:00 | Parabolic SAR · 1h | buy | SOL-USD | 20.85 | — | entry signal |
| 2026-11-17T04:00 | MACD zero-line · 1h | buy | XRP-USD | 18.03 | — | entry signal |
| 2026-11-17T04:00 | MACD cross · 1h | buy | ETH-USD | 14.21 | — | entry signal |
| 2026-11-17T04:00 | MACD cross · 1h | buy | BTC-USD | 14.21 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.55 | — | entry signal |
| 2026-11-17T04:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 10.72 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 07:10:05.000109+00:00 -> 2026-11-17 07:20:05.000109+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 07:10:05.000109+00:00 -> 2026-11-17 07:20:05.000109+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
