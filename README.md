# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T12:10:05.000149+00:00 · 63138 ticks

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

Today: 9576 decisions in 1923 calls, $0.1340 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T12:10 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-17T12:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-17T12:10 | 1 / 3 / 1 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 118.04 | 18.04 | 0 | — | 13.96 | 4.66 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.84 | 12.84 | 36 | 30.6 | 18.59 | 2.79 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.74 | 3.74 | 0 | — | 5.51 | 1.52 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.32 | 0.32 | 146 | 34.9 | -1.77 | -1.51 | -3.69 | 74 |
| 7 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.43 | 2.07 | -9.06 | 224 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.08 | 0.30 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 96.62 | -3.38 | 0 | — | -2.59 | -0.80 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.54 | -3.38 | -5.99 | 21 |
| 14 | Agent (rotation) | meta | 93.85 | -6.15 | 196 | 29.6 | -1.94 | -0.62 | -8.15 | 157 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.83 | -6.17 | 0 | — | -6.65 | -1.72 | -8.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.67 | -8.33 | 47 | 42.6 | -8.37 | -1.64 | -14.79 | 59 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.57 | -8.43 | 0 | — | -7.13 | -1.91 | -10.92 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.34 | -6.93 | -17.28 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.42 | -12.58 | 67 | 20.9 | -11.09 | -4.37 | -16.34 | 78 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 86.67 | -13.33 | 16 | 18.8 | -4.53 | -0.69 | -19.56 | 15 |
| 24 | Agent | meta | 86.11 | -13.89 | 203 | 36.5 | -14.10 | -6.97 | -15.83 | 196 |
| 25 | Opening range 30m | breakout | 86.10 | -13.90 | 437 | 33.6 | -10.77 | -3.43 | -14.11 | 583 |
| 26 | Agent (aggressive) | meta | 83.34 | -16.66 | 97 | 34.0 | -15.13 | -4.18 | -16.78 | 96 |
| 27 | Parabolic SAR · 1h | trend | 83.03 | -16.97 | 181 | 28.2 | -23.09 | -6.24 | -24.87 | 214 |
| 28 | Keltner breakout · 1h | breakout | 80.58 | -19.42 | 121 | 25.6 | -19.20 | -4.40 | -25.84 | 157 |
| 29 | Donchian 55/20 · 1h | breakout | 80.37 | -19.63 | 76 | 13.2 | -26.54 | -6.88 | -29.01 | 87 |
| 30 | Connors RSI(2) · 1h | reversion | 80.31 | -19.69 | 213 | 39.9 | -14.53 | -6.42 | -14.88 | 95 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.38 | -5.18 | -21.95 | 85 |
| 32 | Opening range 15m | breakout | 78.14 | -21.86 | 531 | 31.6 | -17.36 | -4.67 | -21.37 | 692 |
| 33 | Max aggression: 5-day momentum | meta | 78.10 | -21.90 | 21 | 42.9 | -48.60 | -3.25 | -55.24 | 23 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.31 | -22.69 | 2 | 0.0 | -14.56 | -1.78 | -24.50 | 1 |
| 35 | Hold BTC | benchmark | 75.82 | -24.18 | 2 | 0.0 | -14.68 | -2.05 | -28.91 | 1 |
| 36 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -31.24 | -8.80 | -31.74 | 116 |
| 37 | Max aggression: 1-day momentum | meta | 74.92 | -25.08 | 30 | 26.7 | -23.41 | -0.84 | -57.50 | 40 |
| 38 | ADX DI cross · 1h | trend | 74.74 | -25.26 | 207 | 19.3 | -26.70 | -4.34 | -34.65 | 256 |
| 39 | Stochastic reversion · 1h | reversion | 74.07 | -25.93 | 333 | 44.1 | -32.01 | -4.72 | -32.87 | 415 |
| 40 | Bollinger breakout · 1h | breakout | 73.97 | -26.03 | 186 | 22.0 | -24.73 | -5.29 | -31.89 | 235 |
| 41 | MFI reversion · 1h | reversion | 72.13 | -27.87 | 420 | 34.3 | -25.81 | -3.66 | -29.33 | 163 |
| 42 | Supertrend · 1h | trend | 71.85 | -28.15 | 187 | 16.0 | -32.04 | -5.41 | -39.67 | 200 |
| 43 | MACD zero-line · 1h | trend | 71.67 | -28.33 | 178 | 18.0 | -25.79 | -5.10 | -32.35 | 198 |
| 44 | Heikin-Ashi · 1h | trend | 71.47 | -28.53 | 461 | 23.2 | -38.61 | -7.34 | -43.26 | 636 |
| 45 | RSI momentum · 1h | momentum | 71.31 | -28.69 | 175 | 14.3 | -30.96 | -5.58 | -38.07 | 203 |
| 46 | Triple EMA stack · 1h | trend | 71.22 | -28.78 | 154 | 14.9 | -31.42 | -6.18 | -37.77 | 192 |
| 47 | EMA 20/50 cross · 1h | trend | 70.93 | -29.07 | 112 | 9.8 | -35.46 | -9.65 | -38.88 | 113 |
| 48 | ROC + volume · 1h | momentum | 70.58 | -29.42 | 405 | 28.4 | -28.12 | -4.58 | -37.95 | 354 |
| 49 | MACD cross · 1h | trend | 70.24 | -29.76 | 409 | 22.2 | -34.27 | -4.99 | -43.66 | 477 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 69.21 | -30.79 | 303 | 19.1 | -33.39 | -6.85 | -39.75 | 261 |
| 52 | CCI reversion · 1h | reversion | 67.88 | -32.12 | 378 | 42.1 | -40.22 | -6.52 | -42.07 | 456 |
| 53 | Donchian 20/10 · 1h | breakout | 67.36 | -32.65 | 158 | 18.4 | -31.12 | -5.19 | -39.27 | 208 |
| 54 | Bollinger reversion · 1h | reversion | 66.48 | -33.52 | 333 | 39.0 | -36.43 | -5.50 | -36.96 | 408 |
| 55 | Williams %R · 1h | reversion | 64.22 | -35.78 | 420 | 41.4 | -44.56 | -7.49 | -45.13 | 544 |
| 56 | EMA 9/21 cross · 1h | trend | 63.66 | -36.34 | 278 | 11.2 | -40.14 | -8.08 | -45.47 | 319 |
| 57 | Agent (ML meta-label) | meta | 60.84 | -39.16 | 1876 | 24.5 | -26.43 | -4.47 | -29.79 | 331 |
| 58 | Z-score reversion · 1h | reversion | 59.60 | -40.40 | 221 | 35.7 | -34.90 | -4.79 | -36.18 | 244 |
| 59 | RSI(14) reversion · 1h | reversion | 59.29 | -40.71 | 204 | 31.9 | -40.74 | -5.99 | -42.17 | 240 |
| 60 | VWAP momentum · 1h | momentum | 57.82 | -42.18 | 949 | 21.7 | -53.13 | -9.38 | -57.93 | 1209 |
| 61 | Candlestick reversal · 1h | reversion | 57.12 | -42.88 | 538 | 27.0 | -45.55 | -8.23 | -45.70 | 620 |
| 62 | Three white soldiers | momentum | 56.13 | -43.87 | 575 | 14.6 | -49.19 | -21.93 | -49.37 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.13 | -98.99 | 5286 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.45 | -25.78 | -81.68 | 1436 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.01 | -43.76 | -94.01 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.09 | -31.54 | -90.16 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -39.98 | -91.38 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.05 | -30.50 | -90.05 | 2147 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.93 | -47.84 | -97.94 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.43 | -52.15 | -96.43 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -37.32 | -93.64 | 2267 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.86 | -33.52 | -82.86 | 1639 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -53.10 | -99.60 | 6055 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -41.14 | -92.02 | 2581 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.14 | -37.11 | -95.14 | 3344 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -66.73 | -99.80 | 6146 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -43.50 | -92.43 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.49 | -26.38 | -76.49 | 1652 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.61 | -58.43 | -97.62 | 3470 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -55.05 | -99.00 | 4944 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.51 | -27.06 | -68.56 | 1229 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -55.15 | -94.68 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.48 | -37.41 | -84.52 | 1744 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -65.80 | -99.69 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.45 | -29.69 | -90.56 | 2337 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.92 | -18.79 | -79.97 | 1822 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.04 | -35.59 | -91.09 | 2168 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.49 | -44.99 | -97.49 | 3913 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.44 | -60.22 | -89.47 | 2164 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.28 | -30.02 | -66.33 | 828 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.97 | -23.28 | -72.23 | 1249 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.40 | -17.58 | -80.61 | 1760 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.18 | -97.57 | 4355 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -95.34 | -99.94 | 8394 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T12:10 | Three white soldiers | sell | XRP-USD | 13.97 | -0.05 | exit signal |
| 2026-11-17T12:00 | CCI reversion · 1h | buy | DOGE-USD | 17.01 | — | entry signal |
| 2026-11-17T12:00 | CCI reversion · 1h | buy | BTC-USD | 17.01 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Bollinger reversion · 1h | buy | BTC-USD | 4.16 | — | entry signal |
| 2026-11-17T12:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.72 | — | entry signal |
| 2026-11-17T12:00 | Bollinger breakout · 1h | buy | XRP-USD | 18.54 | — | entry signal |
| 2026-11-17T12:00 | Donchian 55/20 · 1h | buy | SOL-USD | 20.12 | — | entry signal |
| 2026-11-17T12:00 | Donchian 20/10 · 1h | buy | XRP-USD | 16.88 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | XRP-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | SOL-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | VWAP momentum · 1h | buy | BTC-USD | 8.29 | — | entry signal |
| 2026-11-17T12:00 | Parabolic SAR · 1h | buy | XRP-USD | 20.81 | — | entry signal |
| 2026-11-17T12:00 | MACD cross · 1h | buy | XRP-USD | 17.60 | — | entry signal |
| 2026-11-17T11:20 | Three white soldiers | buy | XRP-USD | 14.02 | — | entry signal |
| 2026-11-17T11:15 | Three white soldiers | buy | BTC-USD | 14.03 | — | entry signal |
| 2026-11-17T11:00 | VWAP momentum · 1h | sell | SOL-USD | 14.42 | -0.08 | exit signal |
| 2026-11-17T11:00 | MACD zero-line · 1h | sell | XRP-USD | 17.71 | -0.32 | exit signal |
| 2026-11-17T11:00 | MACD cross · 1h | sell | XRP-USD | 14.12 | -0.13 | exit signal |
| 2026-11-17T11:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 15.58 | -0.37 | exit signal |
| 2026-11-17T10:10 | Donchian 20/10 · 1h | sell | ETH-USD | 16.43 | -0.53 | stop-loss |
| 2026-11-17T10:10 | Three white soldiers | sell | SOL-USD | 13.99 | -0.09 | exit signal |
| 2026-11-17T10:00 | Williams %R · 1h | buy | DOGE-USD | 6.41 | — | entry signal |
| 2026-11-17T10:00 | Parabolic SAR · 1h | sell | ETH-USD | 20.06 | -0.49 | exit signal |
| 2026-11-17T10:00 | MACD cross · 1h | sell | ETH-USD | 17.45 | -0.29 | exit signal |
| 2026-11-17T09:45 | Three white soldiers | sell | ETH-USD | 13.97 | -0.10 | exit signal |
| 2026-11-17T09:40 | Three white soldiers | buy | ETH-USD | 14.07 | — | entry signal |
| 2026-11-17T09:35 | Three white soldiers | buy | SOL-USD | 14.08 | — | entry signal |
| 2026-11-17T09:05 | Candlestick reversal · 1h | sell | BTC-USD | 7.02 | -0.14 | stop-loss |
| 2026-11-17T09:00 | Bollinger breakout · 1h | sell | XRP-USD | 18.28 | -0.30 | exit signal |
| 2026-11-17T09:00 | VWAP momentum · 1h | buy | SOL-USD | 2.92 | — | rebalance up |
| 2026-11-17T09:00 | VWAP momentum · 1h | sell | ETH-USD | 11.59 | -0.13 | exit signal |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 3.19 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 5.27 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 5.29 | — | rebalance up |
| 2026-11-17T09:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 10.55 | -0.17 | exit signal |
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | SOL-USD | 4.35 | — | rebalance up |
| 2026-11-17T07:00 | VWAP momentum · 1h | buy | ETH-USD | 4.38 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 12:10:05.000149+00:00 -> 2026-11-17 12:20:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 12:10:05.000149+00:00 -> 2026-11-17 12:20:05.000149+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
