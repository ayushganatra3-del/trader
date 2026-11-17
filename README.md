# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T14:40:05.000135+00:00 · 63276 ticks

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

Today: 12177 decisions in 2337 calls, $0.1688 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T14:40 | 5 / 17 / 8 | cash |  |
| Breezy | 2026-11-17T14:40 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-17T14:40 | 5 / 24 / 1 | COIN 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.05 | 18.05 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.54 | 12.54 | 36 | 30.6 | 18.57 | 2.78 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.80 | 3.80 | 0 | — | 5.72 | 1.57 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.28 | 0.28 | 146 | 34.9 | -2.20 | -1.87 | -3.81 | 70 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.67 | 2.13 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.86 | -1.14 | 8 | 50.0 | 0.04 | 0.30 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 96.38 | -3.62 | 0 | — | -3.00 | -0.94 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 93.84 | -6.16 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 15 | Agent (rotation) | meta | 93.77 | -6.23 | 196 | 29.6 | -1.96 | -0.63 | -8.15 | 158 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.68 | -8.32 | 47 | 42.6 | -8.48 | -1.67 | -14.79 | 62 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.58 | -8.43 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.36 | -6.94 | -17.30 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.67 | -12.33 | 67 | 20.9 | -9.33 | -3.50 | -15.82 | 73 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.77 | -13.23 | 17 | 17.6 | -4.05 | -0.60 | -19.56 | 14 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.18 | -6.91 | -16.00 | 197 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.04 | -3.19 | -14.11 | 573 |
| 26 | Parabolic SAR · 1h | trend | 83.46 | -16.54 | 181 | 28.2 | -24.42 | -6.67 | -26.54 | 204 |
| 27 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.87 | -4.36 | -17.06 | 94 |
| 28 | Keltner breakout · 1h | breakout | 80.64 | -19.36 | 121 | 25.6 | -17.60 | -3.81 | -25.52 | 159 |
| 29 | Donchian 55/20 · 1h | breakout | 80.60 | -19.40 | 76 | 13.2 | -24.69 | -6.40 | -29.04 | 84 |
| 30 | Connors RSI(2) · 1h | reversion | 80.32 | -19.68 | 214 | 40.2 | -14.46 | -6.38 | -14.84 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Max aggression: 5-day momentum | meta | 78.34 | -21.66 | 21 | 42.9 | -49.10 | -3.31 | -55.24 | 22 |
| 33 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -16.73 | -4.49 | -21.37 | 683 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.31 | -22.69 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 76.26 | -23.74 | 2 | 0.0 | -14.12 | -1.95 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.30 | -8.51 | -29.91 | 112 |
| 37 | Max aggression: 1-day momentum | meta | 75.15 | -24.85 | 30 | 26.7 | -25.88 | -1.04 | -57.50 | 39 |
| 38 | ADX DI cross · 1h | trend | 74.80 | -25.20 | 207 | 19.3 | -28.73 | -4.63 | -35.87 | 260 |
| 39 | Bollinger breakout · 1h | breakout | 74.41 | -25.59 | 186 | 22.0 | -24.16 | -5.14 | -31.78 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 74.29 | -25.71 | 333 | 44.1 | -32.10 | -4.74 | -32.97 | 415 |
| 41 | MFI reversion · 1h | reversion | 72.40 | -27.60 | 420 | 34.3 | -24.16 | -3.44 | -27.83 | 163 |
| 42 | Supertrend · 1h | trend | 72.29 | -27.71 | 187 | 16.0 | -31.57 | -5.29 | -39.67 | 200 |
| 43 | MACD zero-line · 1h | trend | 71.90 | -28.09 | 178 | 18.0 | -25.70 | -5.08 | -32.48 | 198 |
| 44 | RSI momentum · 1h | momentum | 71.50 | -28.50 | 175 | 14.3 | -30.67 | -5.57 | -37.44 | 202 |
| 45 | Heikin-Ashi · 1h | trend | 71.47 | -28.53 | 461 | 23.2 | -38.75 | -7.37 | -43.32 | 639 |
| 46 | Triple EMA stack · 1h | trend | 71.28 | -28.72 | 154 | 14.9 | -31.43 | -6.32 | -37.17 | 180 |
| 47 | EMA 20/50 cross · 1h | trend | 71.15 | -28.85 | 112 | 9.8 | -35.15 | -9.57 | -38.77 | 113 |
| 48 | ROC + volume · 1h | momentum | 70.56 | -29.44 | 405 | 28.4 | -27.86 | -4.58 | -37.57 | 354 |
| 49 | MACD cross · 1h | trend | 70.56 | -29.44 | 409 | 22.2 | -34.03 | -4.97 | -43.61 | 477 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.20 | -30.80 | 303 | 19.1 | -33.82 | -7.08 | -39.35 | 261 |
| 52 | CCI reversion · 1h | reversion | 68.17 | -31.83 | 378 | 42.1 | -40.19 | -6.51 | -42.07 | 458 |
| 53 | Donchian 20/10 · 1h | breakout | 67.75 | -32.25 | 158 | 18.4 | -30.96 | -5.22 | -39.25 | 208 |
| 54 | Bollinger reversion · 1h | reversion | 66.73 | -33.27 | 336 | 38.7 | -36.30 | -5.47 | -36.96 | 408 |
| 55 | Williams %R · 1h | reversion | 64.23 | -35.77 | 422 | 41.5 | -44.74 | -7.53 | -45.29 | 545 |
| 56 | EMA 9/21 cross · 1h | trend | 63.98 | -36.02 | 278 | 11.2 | -39.83 | -7.91 | -45.67 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.88 | -39.12 | 1876 | 24.5 | -24.93 | -4.26 | -27.88 | 313 |
| 58 | Z-score reversion · 1h | reversion | 60.00 | -40.00 | 221 | 35.7 | -34.46 | -4.70 | -36.18 | 244 |
| 59 | RSI(14) reversion · 1h | reversion | 59.24 | -40.76 | 204 | 31.9 | -40.68 | -5.98 | -41.85 | 240 |
| 60 | VWAP momentum · 1h | momentum | 58.18 | -41.82 | 949 | 21.7 | -52.36 | -9.25 | -57.42 | 1204 |
| 61 | Candlestick reversal · 1h | reversion | 57.41 | -42.59 | 538 | 27.0 | -45.46 | -8.19 | -45.86 | 615 |
| 62 | Three white soldiers | momentum | 55.98 | -44.02 | 577 | 14.7 | -49.43 | -22.06 | -49.45 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -43.49 | -99.01 | 5313 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.88 | -24.89 | -81.70 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.92 | -43.03 | -93.97 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.02 | -31.34 | -90.16 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -39.07 | -91.36 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.93 | -30.53 | -89.98 | 2138 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.89 | -47.04 | -97.92 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.47 | -52.58 | -96.47 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.66 | -37.40 | -93.69 | 2265 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.68 | -32.99 | -82.76 | 1635 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -51.55 | -99.59 | 6030 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.90 | -40.33 | -91.97 | 2575 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.16 | -37.57 | -95.16 | 3340 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -66.69 | -99.80 | 6145 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.32 | -43.04 | -92.33 | 2262 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.42 | -26.38 | -76.42 | 1659 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -59.01 | -97.64 | 3460 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.99 | -54.35 | -98.99 | 4944 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.69 | -27.34 | -68.74 | 1228 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -55.00 | -94.65 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.50 | -37.49 | -84.54 | 1748 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.14 | -99.69 | 6374 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.42 | -29.55 | -90.48 | 2317 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.66 | -18.58 | -79.77 | 1805 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.93 | -34.90 | -90.99 | 2157 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.49 | -45.01 | -97.49 | 3915 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -60.31 | -89.33 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.53 | -30.47 | -66.53 | 830 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.61 | -22.89 | -72.26 | 1240 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.10 | -17.37 | -80.45 | 1756 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -44.65 | -97.55 | 4348 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -99.06 | -99.94 | 8396 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 25.08 | — | entry |
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | MSTR | 25.08 | — | entry |
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | COIN | 25.08 | — | entry |
| 2026-11-17T14:40 | Agent (ML meta-label) | buy | META | 15.22 | — | entry |
| 2026-11-17T14:35 | Agent (rotation) | buy | SQQQ | 31.28 | — | entry |
| 2026-11-17T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 112.84 | — | entry |
| 2026-11-17T14:35 | Agent (ML meta-label) | buy | NVDA | 15.21 | — | entry |
| 2026-11-17T14:35 | Agent (ML meta-label) | buy | AMD | 15.21 | — | entry |
| 2026-11-17T14:35 | Daily: Bullish score | sell | AMZN | 20.25 | -1.07 | target is flat |
| 2026-11-17T14:35 | Daily: Connors RSI(2) · 3x ETFs | buy | UPRO | 98.81 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | TNA | 10.30 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | SPY | 10.30 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | MSTR | 10.30 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | ETHU | 10.30 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | COIN | 10.30 | — | entry |
| 2026-11-17T14:35 | MFI reversion · 1h | buy | AMZN | 10.30 | — | entry |
| 2026-11-17T14:35 | Williams %R · 1h | buy | TQQQ | 4.14 | — | rebalance up |
| 2026-11-17T14:35 | Williams %R · 1h | buy | QQQ | 3.72 | — | rebalance up |
| 2026-11-17T14:35 | Williams %R · 1h | buy | PLTR | 4.16 | — | rebalance up |
| 2026-11-17T14:35 | Williams %R · 1h | buy | META | 3.47 | — | rebalance up |
| 2026-11-17T14:35 | Williams %R · 1h | buy | AMZN | 3.78 | — | rebalance up |
| 2026-11-17T14:35 | Williams %R · 1h | buy | AAPL | 3.74 | — | rebalance up |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | UPRO | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | TSLA | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | TQQQ | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | TNA | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | TECL | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | SPY | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | SOXL | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | QQQ | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | NVDA | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | MSTR | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | MSFT | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | IWM | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | ETHU | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | COIN | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | BITX | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | AMZN | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | AMD | 4.12 | — | entry |
| 2026-11-17T14:35 | Stochastic reversion · 1h | buy | AAPL | 4.12 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 14:40:05.000135+00:00 -> 2026-11-17 14:50:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 14:40:05.000135+00:00 -> 2026-11-17 14:50:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
