# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-08T13:20:05.000134+00:00 · 52149 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.54 (-12.46%)

Closed trades 156, win rate 35.9%, fees £4.84, max drawdown -12.87%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 10326 decisions in 2070 calls, $0.1443 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-08T13:20 | 4 / 1 / 0 | DOGE-USD 15% |  |
| Breezy | 2026-11-08T13:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-08T13:20 | 5 / 0 / 0 | ETH-USD 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 1.95 | +8.75% | 6 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| VWAP reversion | SQQQ | 1.93 | +6.85% | 4 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| Keltner breakout | COIN | 1.83 | +1.67% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 16.48 | 3.20 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.26 | 12.26 | 0 | — | 13.03 | 4.47 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.83 | 5.83 | 30 | 26.7 | 14.37 | 2.41 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.66 | 1.66 | 30 | 43.3 | 0.06 | 0.13 | -9.63 | 30 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.41 | -0.59 | 0 | — | 2.38 | 0.77 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.65 | -1.35 | 126 | 46.0 | -12.38 | -2.91 | -13.75 | 147 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 121 | 34.7 | 5.46 | 2.83 | -2.45 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 11 | Agent (rotation) | meta | 95.00 | -5.00 | 176 | 27.8 | -6.88 | -3.99 | -10.35 | 162 |
| 12 | Hold SPY | benchmark | 94.81 | -5.19 | 0 | — | -4.16 | -1.54 | -6.18 | 1 |
| 13 | Gap and go | momentum | 94.25 | -5.75 | 172 | 27.9 | -1.54 | -0.42 | -9.14 | 229 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 15 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.15 | -7.85 | 7 | 42.9 | -10.10 | -0.97 | -18.73 | 8 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 92.11 | -7.89 | 0 | — | -7.24 | -2.20 | -9.25 | 1 |
| 18 | Trend pullback · 1h | trend | 92.07 | -7.93 | 108 | 23.1 | -14.27 | -5.43 | -17.86 | 78 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.80 | -9.20 | 0 | — | -7.19 | -2.15 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.24 | -10.76 | 375 | 32.5 | -16.49 | -5.33 | -17.56 | 588 |
| 22 | Hold BTC | benchmark | 88.88 | -11.12 | 1 | 0.0 | -4.09 | -0.44 | -14.09 | 1 |
| 23 | Copy: Insider buying | copy | 88.77 | -11.23 | 40 | 37.5 | -12.86 | -3.08 | -15.96 | 62 |
| 24 | Daily: Bullish score | daily | 88.76 | -11.23 | 15 | 20.0 | -5.00 | -0.66 | -16.58 | 14 |
| 25 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.27 | -3.58 | -14.68 | 85 |
| 26 | Agent | meta | 87.54 | -12.46 | 156 | 35.9 | -14.32 | -7.67 | -14.33 | 197 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -12.88 | -2.83 | -20.50 | 234 |
| 28 | Donchian 55/20 · 1h | breakout | 85.95 | -14.05 | 71 | 14.1 | -12.74 | -2.59 | -20.43 | 103 |
| 29 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 17 | 47.1 | -32.59 | -2.07 | -40.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.01 | -15.99 | 74 | 31.1 | -18.23 | -5.45 | -18.65 | 93 |
| 31 | Opening range 15m | breakout | 82.11 | -17.89 | 465 | 30.5 | -21.43 | -6.33 | -21.54 | 724 |
| 32 | Stochastic reversion · 1h | reversion | 82.01 | -17.99 | 263 | 46.8 | -25.11 | -3.70 | -29.25 | 392 |
| 33 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -16.48 | -3.72 | -21.45 | 99 |
| 34 | Connors RSI(2) · 1h | reversion | 81.05 | -18.95 | 205 | 40.0 | -18.94 | -6.31 | -19.54 | 125 |
| 35 | Keltner breakout · 1h | breakout | 80.97 | -19.03 | 107 | 23.4 | -22.29 | -4.62 | -24.50 | 172 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.47 | -19.53 | 2 | 0.0 | -12.03 | -1.56 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.35 | -20.65 | 175 | 18.3 | -23.98 | -4.00 | -27.07 | 261 |
| 38 | MFI reversion · 1h | reversion | 78.48 | -21.52 | 337 | 34.1 | -18.67 | -2.67 | -20.14 | 156 |
| 39 | Ichimoku · 1h | trend | 77.88 | -22.12 | 94 | 14.9 | -22.74 | -4.65 | -29.43 | 124 |
| 40 | Bollinger breakout · 1h | breakout | 77.20 | -22.80 | 170 | 22.9 | -23.47 | -4.89 | -27.58 | 247 |
| 41 | CCI reversion · 1h | reversion | 76.43 | -23.57 | 296 | 44.9 | -29.65 | -4.87 | -29.95 | 463 |
| 42 | EMA 20/50 cross · 1h | trend | 76.08 | -23.92 | 102 | 10.8 | -21.86 | -3.93 | -30.58 | 127 |
| 43 | Heikin-Ashi · 1h | trend | 75.60 | -24.40 | 393 | 22.9 | -42.90 | -9.05 | -42.90 | 676 |
| 44 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -25.54 | -5.28 | -29.20 | 208 |
| 45 | Triple EMA stack · 1h | trend | 74.46 | -25.54 | 142 | 14.8 | -27.51 | -5.75 | -33.48 | 200 |
| 46 | Supertrend · 1h | trend | 73.63 | -26.37 | 166 | 13.3 | -29.81 | -5.18 | -34.80 | 215 |
| 47 | RSI momentum · 1h | momentum | 73.47 | -26.53 | 158 | 12.7 | -26.42 | -5.01 | -32.60 | 214 |
| 48 | Z-score reversion · 1h | reversion | 72.98 | -27.02 | 164 | 35.4 | -25.15 | -3.73 | -27.66 | 227 |
| 49 | MACD cross · 1h | trend | 72.89 | -27.11 | 342 | 23.1 | -34.22 | -6.02 | -38.98 | 478 |
| 50 | Bollinger reversion · 1h | reversion | 72.72 | -27.29 | 257 | 39.3 | -30.04 | -5.14 | -32.97 | 368 |
| 51 | Williams %R · 1h | reversion | 72.44 | -27.56 | 315 | 44.8 | -36.00 | -5.78 | -37.81 | 534 |
| 52 | Daily: Momentum burst | daily | 72.31 | -27.69 | 26 | 11.5 | -35.92 | -5.05 | -38.31 | 31 |
| 53 | Donchian 20/10 · 1h | breakout | 71.47 | -28.53 | 141 | 19.9 | -29.91 | -5.54 | -34.69 | 212 |
| 54 | OBV trend · 1h | momentum | 70.94 | -29.06 | 273 | 17.9 | -28.47 | -5.85 | -34.11 | 281 |
| 55 | ROC + volume · 1h | momentum | 69.77 | -30.23 | 348 | 25.3 | -38.35 | -7.44 | -39.25 | 382 |
| 56 | EMA 9/21 cross · 1h | trend | 67.15 | -32.85 | 243 | 9.9 | -38.63 | -7.92 | -39.14 | 333 |
| 57 | VWAP momentum · 1h | momentum | 66.60 | -33.40 | 790 | 21.8 | -54.21 | -11.98 | -54.29 | 1236 |
| 58 | Agent (ML meta-label) | meta | 66.32 | -33.68 | 1541 | 23.0 | -6.84 | -1.14 | -17.19 | 336 |
| 59 | RSI(14) reversion · 1h | reversion | 66.25 | -33.76 | 143 | 27.3 | -29.67 | -4.66 | -31.54 | 228 |
| 60 | Candlestick reversal · 1h | reversion | 65.08 | -34.92 | 418 | 28.2 | -38.33 | -7.08 | -38.81 | 587 |
| 61 | Three white soldiers | momentum | 63.47 | -36.53 | 480 | 15.2 | -49.37 | -23.02 | -49.37 | 653 |
| 62 | Max aggression: 1-day momentum | meta | 62.24 | -37.76 | 26 | 26.9 | -42.96 | -2.72 | -56.96 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -46.10 | -98.96 | 5239 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.59 | -26.15 | -80.69 | 1435 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -47.20 | -93.43 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.99 | -32.34 | -89.00 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.79 | -40.08 | -90.80 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.19 | -32.33 | -90.23 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -54.86 | -97.72 | 3482 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -57.00 | -96.31 | 3402 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -34.02 | -93.75 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.30 | -34.69 | -82.32 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -54.41 | -99.53 | 5999 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.63 | -44.08 | -92.63 | 2604 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.74 | -38.63 | -95.74 | 3422 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -74.83 | -99.80 | 6191 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -43.87 | -91.77 | 2277 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.23 | -24.70 | -75.23 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -63.30 | -97.77 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.82 | -63.36 | -98.82 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.60 | -28.86 | -69.60 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -54.68 | -94.65 | 2748 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.75 | -37.31 | -84.75 | 1762 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -74.31 | -99.64 | 6384 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.50 | -31.94 | -89.50 | 2301 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.22 | -19.73 | -78.23 | 1755 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.07 | -37.54 | -91.07 | 2225 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.71 | -52.17 | -96.71 | 3901 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.44 | -55.05 | -89.47 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.73 | -28.75 | -65.73 | 803 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.94 | -24.28 | -72.94 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.77 | -18.49 | -78.79 | 1677 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.26 | -50.12 | -97.26 | 4336 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.19 | -99.93 | 8307 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-08T13:20 | Three white soldiers | buy | SOL-USD | 15.88 | — | entry signal |
| 2026-11-08T13:05 | Three white soldiers | buy | BTC-USD | 15.88 | — | entry signal |
| 2026-11-08T12:40 | Three white soldiers | sell | BTC-USD | 15.81 | -0.10 | exit signal |
| 2026-11-08T12:35 | Three white soldiers | buy | BTC-USD | 15.91 | — | entry signal |
| 2026-11-08T12:10 | Three white soldiers | sell | BTC-USD | 15.83 | -0.10 | exit signal |
| 2026-11-08T12:00 | CCI reversion · 1h | buy | DOGE-USD | 4.02 | — | entry signal |
| 2026-11-08T12:00 | CCI reversion · 1h | sell | XRP-USD | 1.00 | -0.01 | exit signal |
| 2026-11-08T12:00 | CCI reversion · 1h | sell | ETH-USD | 3.81 | -0.01 | exit signal |
| 2026-11-08T12:00 | Bollinger reversion · 1h | sell | SOL-USD | 5.00 | -0.01 | exit signal |
| 2026-11-08T12:00 | ADX DI cross · 1h | buy | SOL-USD | 19.84 | — | entry signal |
| 2026-11-08T12:00 | MACD cross · 1h | buy | DOGE-USD | 4.86 | — | entry signal |
| 2026-11-08T11:20 | Three white soldiers | buy | BTC-USD | 15.93 | — | entry signal |
| 2026-11-08T11:05 | VWAP reversion · 1h | sell | DOGE-USD | 24.54 | -0.16 | target is flat |
| 2026-11-08T11:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.70 | — | entry signal |
| 2026-11-08T11:00 | VWAP momentum · 1h | buy | SOL-USD | 1.55 | — | entry |
| 2026-11-08T11:00 | VWAP momentum · 1h | buy | ETH-USD | 6.05 | — | entry |
| 2026-11-08T11:00 | VWAP momentum · 1h | sell | XRP-USD | 6.60 | -0.06 | exit signal |
| 2026-11-08T10:00 | MACD cross · 1h | sell | DOGE-USD | 4.80 | -0.06 | exit signal |
| 2026-11-08T10:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 16.79 | — | entry signal |
| 2026-11-08T09:20 | CCI reversion · 1h | sell | DOGE-USD | 3.41 | -0.06 | stop-loss |
| 2026-11-08T09:20 | Candlestick reversal · 1h | buy | ETH-USD | 3.99 | — | entry |
| 2026-11-08T09:20 | Candlestick reversal · 1h | sell | DOGE-USD | 3.99 | -0.05 | stop-loss |
| 2026-11-08T09:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.03 | — | entry |
| 2026-11-08T09:00 | Candlestick reversal · 1h | sell | XRP-USD | 4.03 | 0.00 | exit signal |
| 2026-11-08T08:45 | Agent (ML meta-label) | sell | XRP-USD | 3.67 | -0.02 | selected signal exited |
| 2026-11-08T08:30 | Agent (ML meta-label) | buy | XRP-USD | 3.69 | — | entry |
| 2026-11-08T08:00 | CCI reversion · 1h | buy | SOL-USD | 1.71 | — | entry |
| 2026-11-08T08:00 | CCI reversion · 1h | sell | BTC-USD | 1.31 | -0.00 | exit signal |
| 2026-11-08T08:00 | Bollinger reversion · 1h | sell | ETH-USD | 4.84 | -0.01 | exit signal |
| 2026-11-08T08:00 | MACD cross · 1h | buy | SOL-USD | 4.86 | — | entry signal |
| 2026-11-08T08:00 | MACD cross · 1h | buy | DOGE-USD | 4.86 | — | entry signal |
| 2026-11-08T06:00 | Stochastic reversion · 1h | sell | XRP-USD | 2.28 | 0.00 | exit signal |
| 2026-11-08T06:00 | Bollinger reversion · 1h | sell | XRP-USD | 5.59 | -0.02 | exit signal |
| 2026-11-08T06:00 | VWAP momentum · 1h | buy | XRP-USD | 6.66 | — | entry signal |
| 2026-11-08T05:35 | Three white soldiers | sell | SOL-USD | 15.85 | -0.11 | exit signal |
| 2026-11-08T05:15 | Three white soldiers | buy | SOL-USD | 15.96 | — | entry signal |
| 2026-11-08T05:00 | VWAP momentum · 1h | sell | ETH-USD | 6.62 | -0.04 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | SOL-USD | 24.65 | -0.13 | exit signal |
| 2026-11-08T04:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.60 | -0.18 | exit signal |
| 2026-11-08T04:00 | Z-score reversion · 1h | sell | BTC-USD | 5.22 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-10 13:20:05.000134+00:00 -> 2026-11-08 13:30:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-10 13:20:05.000134+00:00 -> 2026-11-08 13:30:05.000134+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-10 13:20:05.000134+00:00 -> 2026-11-08 13:30:05.000134+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
