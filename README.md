# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T14:25:05.000106+00:00 · 48541 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 11604 decisions in 2325 calls, $0.1623 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T14:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-05T14:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T14:25 | 1 / 4 / 0 | ETH-USD 52% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.00 | 13.00 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.66 | 0.67 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.80 | -0.20 | 105 | 46.7 | -10.85 | -2.82 | -12.83 | 139 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.14 | -0.86 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.03 | -1.97 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.35 | -4.65 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.91 | -5.09 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 18 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 19 | Hold BTC | benchmark | 93.20 | -6.79 | 0 | — | -0.41 | 0.10 | -13.22 | 1 |
| 20 | Max aggression: 5-day momentum | meta | 91.28 | -8.72 | 16 | 43.8 | -23.01 | -1.32 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.69 | -9.31 | 103 | 22.3 | -16.47 | -6.10 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.74 | -10.26 | 157 | 28.0 | -15.29 | -3.37 | -19.35 | 246 |
| 24 | Copy: Insider buying | copy | 89.58 | -10.42 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.90 | -3.04 | -14.15 | 90 |
| 28 | Daily: Bullish score | daily | 87.03 | -12.97 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.85 | -13.15 | 249 | 47.8 | -20.39 | -3.85 | -24.97 | 380 |
| 30 | Donchian 55/20 · 1h | breakout | 86.38 | -13.62 | 65 | 15.4 | -13.49 | -2.87 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.14 | -13.86 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 84.98 | -15.02 | 157 | 19.1 | -18.58 | -3.34 | -22.68 | 272 |
| 34 | MFI reversion · 1h | reversion | 84.42 | -15.58 | 324 | 34.3 | -13.66 | -2.05 | -18.44 | 150 |
| 35 | Volume breakout · 1h | breakout | 84.39 | -15.61 | 135 | 29.6 | -14.39 | -3.30 | -18.09 | 103 |
| 36 | Keltner breakout · 1h | breakout | 83.54 | -16.46 | 96 | 26.0 | -20.42 | -4.20 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 82.63 | -17.37 | 197 | 41.1 | -19.63 | -6.49 | -20.07 | 130 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.77 | -18.23 | 86 | 14.0 | -20.67 | -4.38 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.37 | -18.63 | 150 | 26.0 | -18.64 | -3.82 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.96 | -19.04 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.19 | -20.81 | 92 | 10.9 | -19.76 | -3.48 | -27.87 | 133 |
| 43 | Heikin-Ashi · 1h | trend | 78.83 | -21.17 | 375 | 22.7 | -40.55 | -8.47 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.32 | -21.68 | 144 | 17.4 | -25.34 | -5.27 | -28.44 | 216 |
| 45 | Z-score reversion · 1h | reversion | 78.02 | -21.98 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 46 | MACD cross · 1h | trend | 77.95 | -22.05 | 317 | 24.0 | -30.53 | -5.95 | -33.62 | 477 |
| 47 | Supertrend · 1h | trend | 77.55 | -22.45 | 147 | 12.9 | -28.81 | -5.26 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.93 | -23.07 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.65 | -23.36 | 291 | 47.4 | -33.13 | -5.95 | -34.59 | 521 |
| 51 | RSI momentum · 1h | momentum | 76.20 | -23.80 | 143 | 11.9 | -28.40 | -5.43 | -30.33 | 226 |
| 52 | Triple EMA stack · 1h | trend | 75.48 | -24.52 | 132 | 13.6 | -27.92 | -5.48 | -31.75 | 213 |
| 53 | OBV trend · 1h | momentum | 74.91 | -25.09 | 254 | 18.1 | -31.38 | -6.85 | -31.44 | 299 |
| 54 | Donchian 20/10 · 1h | breakout | 74.14 | -25.86 | 128 | 21.1 | -28.24 | -5.17 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.13 | -25.87 | 324 | 26.2 | -33.35 | -6.45 | -36.29 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.21 | -27.79 | 136 | 28.7 | -20.71 | -3.44 | -26.28 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 69.31 | -30.69 | 225 | 9.8 | -37.38 | -7.65 | -39.08 | 336 |
| 58 | Candlestick reversal · 1h | reversion | 69.22 | -30.78 | 376 | 30.1 | -34.78 | -6.44 | -37.31 | 545 |
| 59 | Agent (ML meta-label) | meta | 69.10 | -30.90 | 1449 | 22.2 | -10.15 | -1.83 | -18.46 | 330 |
| 60 | VWAP momentum · 1h | momentum | 68.84 | -31.16 | 744 | 22.3 | -54.10 | -11.30 | -55.84 | 1231 |
| 61 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.21 | -21.89 | -47.21 | 635 |
| 62 | Max aggression: 1-day momentum | meta | 66.61 | -33.38 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.76 | -98.93 | 5166 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.97 | -25.47 | -80.10 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -47.90 | -93.40 | 2522 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.69 | -30.85 | -88.72 | 1900 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -38.85 | -90.57 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -32.93 | -90.98 | 2257 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.65 | -54.28 | -97.66 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.21 | -59.96 | -96.21 | 3401 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.89 | -34.16 | -93.95 | 2479 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -37.39 | -82.03 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.26 | -99.48 | 5868 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -44.39 | -92.73 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.82 | -38.00 | -95.82 | 3444 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -73.01 | -99.79 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.59 | -43.77 | -91.59 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.62 | -26.49 | -74.70 | 1552 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.23 | -97.73 | 3532 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.50 | -98.69 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.43 | -28.64 | -69.91 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.68 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -36.11 | -84.53 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.79 | -99.62 | 6308 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.32 | -30.38 | -88.35 | 2246 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.23 | -18.68 | -76.57 | 1695 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -36.87 | -90.61 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -49.60 | -96.41 | 3827 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.14 | -51.15 | -89.16 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.48 | -27.77 | -65.56 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -25.12 | -73.64 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.14 | -17.99 | -76.64 | 1600 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.99 | -51.32 | -97.00 | 4258 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.10 | -99.93 | 8225 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T14:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.99 | — | entry signal |
| 2026-11-05T14:00 | OBV trend · 1h | sell | ETH-USD | 6.74 | 0.23 | exit signal |
| 2026-11-05T14:00 | Triple EMA stack · 1h | buy | SOL-USD | 6.30 | — | entry |
| 2026-11-05T14:00 | Triple EMA stack · 1h | sell | DOGE-USD | 9.26 | -0.24 | exit signal |
| 2026-11-05T13:00 | Connors RSI(2) · 1h | buy | XRP-USD | 20.77 | — | entry signal |
| 2026-11-05T13:00 | Connors RSI(2) · 1h | buy | ETH-USD | 20.77 | — | entry signal |
| 2026-11-05T13:00 | Connors RSI(2) · 1h | buy | BTC-USD | 20.77 | — | entry signal |
| 2026-11-05T13:00 | Donchian 55/20 · 1h | sell | ETH-USD | 8.54 | 0.22 | exit signal |
| 2026-11-05T13:00 | Donchian 55/20 · 1h | sell | DOGE-USD | 8.54 | -0.11 | exit signal |
| 2026-11-05T13:00 | Donchian 55/20 · 1h | sell | BTC-USD | 8.61 | 0.01 | exit signal |
| 2026-11-05T13:00 | Donchian 20/10 · 1h | sell | SOL-USD | 4.62 | -0.01 | exit signal |
| 2026-11-05T13:00 | Donchian 20/10 · 1h | sell | ETH-USD | 4.59 | 0.12 | exit signal |
| 2026-11-05T13:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 4.59 | -0.06 | exit signal |
| 2026-11-05T13:00 | Donchian 20/10 · 1h | sell | BTC-USD | 4.63 | 0.05 | exit signal |
| 2026-11-05T13:00 | OBV trend · 1h | sell | XRP-USD | 6.83 | 0.11 | exit signal |
| 2026-11-05T13:00 | OBV trend · 1h | sell | SOL-USD | 3.43 | -0.00 | exit signal |
| 2026-11-05T13:00 | OBV trend · 1h | sell | BTC-USD | 6.79 | 0.01 | exit signal |
| 2026-11-05T13:00 | RSI momentum · 1h | sell | DOGE-USD | 5.39 | -0.07 | exit signal |
| 2026-11-05T13:00 | VWAP momentum · 1h | sell | XRP-USD | 5.93 | -0.05 | exit signal |
| 2026-11-05T13:00 | VWAP momentum · 1h | sell | SOL-USD | 6.02 | -0.12 | exit signal |
| 2026-11-05T13:00 | Ichimoku · 1h | sell | XRP-USD | 9.09 | 0.16 | exit signal |
| 2026-11-05T13:00 | ADX DI cross · 1h | sell | ETH-USD | 5.20 | 0.19 | exit signal |
| 2026-11-05T13:00 | ADX DI cross · 1h | sell | BTC-USD | 5.24 | 0.10 | exit signal |
| 2026-11-05T12:40 | Williams %R · 1h | sell | DOGE-USD | 1.10 | -0.02 | stop-loss |
| 2026-11-05T12:40 | Keltner breakout · 1h | sell | ETH-USD | 5.92 | 0.15 | stop-loss |
| 2026-11-05T12:40 | Keltner breakout · 1h | sell | BTC-USD | 5.97 | 0.01 | stop-loss |
| 2026-11-05T12:40 | OBV trend · 1h | sell | DOGE-USD | 6.15 | -0.13 | stop-loss |
| 2026-11-05T12:35 | Three white soldiers · 1h | sell | XRP-USD | 23.22 | -0.41 | stop-loss |
| 2026-11-05T12:00 | MACD cross · 1h | sell | XRP-USD | 3.86 | -0.04 | exit signal |
| 2026-11-05T12:00 | MACD cross · 1h | sell | SOL-USD | 3.87 | -0.03 | exit signal |
| 2026-11-05T11:00 | Bollinger breakout · 1h | sell | BTC-USD | 4.80 | 0.04 | exit signal |
| 2026-11-05T11:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.23 | -0.05 | exit signal |
| 2026-11-05T10:05 | Three white soldiers | sell | BTC-USD | 16.74 | -0.12 | exit signal |
| 2026-11-05T10:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.78 | 0.16 | exit signal |
| 2026-11-05T10:00 | Three white soldiers | buy | BTC-USD | 16.86 | — | entry signal |
| 2026-11-05T09:46 | Three white soldiers | sell | XRP-USD | 16.77 | -0.12 | exit signal |
| 2026-11-05T09:40 | Three white soldiers | buy | XRP-USD | 16.89 | — | entry signal |
| 2026-11-05T09:05 | Three white soldiers | sell | XRP-USD | 16.77 | -0.16 | stop-loss |
| 2026-11-05T09:00 | Williams %R · 1h | buy | DOGE-USD | 1.12 | — | entry signal |
| 2026-11-05T09:00 | VWAP reversion · 1h | sell | DOGE-USD | 25.01 | 0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 14:25:05.000106+00:00 -> 2026-11-05 14:35:05.000106+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 14:25:05.000106+00:00 -> 2026-11-05 14:35:05.000106+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 14:25:05.000106+00:00 -> 2026-11-05 14:35:05.000106+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
