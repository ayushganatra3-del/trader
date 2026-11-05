# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T10:25:05.000122+00:00 · 48324 ticks

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

Today: 8355 decisions in 1674 calls, $0.1168 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T10:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-05T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T10:25 | 3 / 2 / 0 | ETH-USD 68% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.89 | 12.89 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.56 | 0.56 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.95 | -0.05 | 105 | 46.7 | -10.71 | -2.78 | -12.83 | 138 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.04 | -0.96 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 9 | Hold SPY | benchmark | 97.93 | -2.07 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.25 | -4.75 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.81 | -5.19 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Hold BTC | benchmark | 94.40 | -5.60 | 0 | — | -1.42 | -0.07 | -13.22 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.34 | -5.66 | 18 | 11.1 | -3.28 | -3.07 | -5.59 | 27 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 91.18 | -8.82 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 22 | Trend pullback · 1h | trend | 90.93 | -9.06 | 103 | 22.3 | -16.20 | -5.98 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.84 | -10.16 | 157 | 28.0 | -14.48 | -3.20 | -19.35 | 244 |
| 24 | Copy: Insider buying | copy | 89.49 | -10.51 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.47 | -14.15 | 88 |
| 28 | Daily: Bullish score | daily | 86.99 | -13.01 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.92 | -13.08 | 62 | 12.9 | -12.78 | -2.71 | -19.91 | 105 |
| 30 | Stochastic reversion · 1h | reversion | 86.76 | -13.24 | 249 | 47.8 | -20.39 | -3.85 | -24.97 | 380 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.05 | -13.95 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.10 | -14.90 | 155 | 18.1 | -18.65 | -3.35 | -22.68 | 277 |
| 34 | MFI reversion · 1h | reversion | 84.36 | -15.64 | 324 | 34.3 | -13.54 | -2.03 | -18.47 | 152 |
| 35 | Volume breakout · 1h | breakout | 84.32 | -15.68 | 135 | 29.6 | -14.26 | -3.27 | -18.09 | 103 |
| 36 | Keltner breakout · 1h | breakout | 83.61 | -16.39 | 94 | 24.5 | -20.12 | -4.12 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.09 | -16.91 | 197 | 41.1 | -19.38 | -6.40 | -20.21 | 128 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.09 | -17.91 | 85 | 12.9 | -20.25 | -4.28 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.32 | -18.68 | 149 | 25.5 | -18.09 | -3.67 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.88 | -19.12 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.58 | -20.42 | 92 | 10.9 | -18.68 | -3.28 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 78.75 | -21.25 | 375 | 22.7 | -40.47 | -8.45 | -43.89 | 677 |
| 44 | MACD zero-line · 1h | trend | 78.26 | -21.74 | 144 | 17.4 | -25.82 | -5.38 | -29.11 | 219 |
| 45 | Z-score reversion · 1h | reversion | 77.94 | -22.06 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 46 | MACD cross · 1h | trend | 77.92 | -22.08 | 315 | 24.1 | -30.73 | -6.00 | -33.62 | 477 |
| 47 | Supertrend · 1h | trend | 77.83 | -22.17 | 147 | 12.9 | -28.54 | -5.20 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.85 | -23.15 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.59 | -23.41 | 290 | 47.6 | -33.08 | -5.94 | -34.59 | 523 |
| 51 | RSI momentum · 1h | momentum | 76.53 | -23.47 | 142 | 12.0 | -27.89 | -5.33 | -30.33 | 225 |
| 52 | Triple EMA stack · 1h | trend | 76.00 | -24.00 | 131 | 13.7 | -26.69 | -5.22 | -31.75 | 210 |
| 53 | OBV trend · 1h | momentum | 75.31 | -24.69 | 249 | 17.3 | -30.39 | -6.68 | -30.87 | 296 |
| 54 | Donchian 20/10 · 1h | breakout | 74.40 | -25.60 | 124 | 19.4 | -27.63 | -5.02 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.07 | -25.93 | 324 | 26.2 | -33.23 | -6.42 | -36.17 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.14 | -27.86 | 136 | 28.7 | -20.64 | -3.43 | -26.28 | 216 |
| 57 | EMA 9/21 cross · 1h | trend | 69.62 | -30.38 | 225 | 9.8 | -36.61 | -7.35 | -40.09 | 341 |
| 58 | Candlestick reversal · 1h | reversion | 69.18 | -30.82 | 376 | 30.1 | -35.17 | -6.55 | -37.63 | 553 |
| 59 | Agent (ML meta-label) | meta | 69.09 | -30.91 | 1449 | 22.2 | -7.09 | -1.23 | -17.58 | 312 |
| 60 | VWAP momentum · 1h | momentum | 68.99 | -31.01 | 741 | 22.4 | -54.09 | -11.33 | -55.84 | 1233 |
| 61 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.21 | -21.89 | -47.21 | 635 |
| 62 | Max aggression: 1-day momentum | meta | 66.55 | -33.45 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.40 | -98.94 | 5158 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.78 | -25.31 | -80.02 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.27 | -46.55 | -93.28 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.71 | -31.00 | -88.73 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.57 | -38.99 | -90.59 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.65 | -32.68 | -90.68 | 2239 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -53.86 | -97.63 | 3453 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -59.05 | -96.16 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -34.16 | -93.87 | 2480 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.95 | -37.16 | -81.97 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.63 | -99.48 | 5868 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.78 | -44.70 | -92.78 | 2596 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.81 | -37.87 | -95.81 | 3443 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -74.16 | -99.79 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -43.94 | -91.61 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.65 | -26.54 | -74.70 | 1553 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -61.31 | -97.69 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.53 | -98.70 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.43 | -28.64 | -69.91 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -56.31 | -94.64 | 2754 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.66 | -36.67 | -84.66 | 1783 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.15 | -99.62 | 6306 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.10 | -29.70 | -88.25 | 2238 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.50 | -18.95 | -76.95 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.78 | -90.62 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -49.64 | -96.42 | 3827 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -51.95 | -89.21 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.48 | -27.77 | -65.56 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.42 | -24.97 | -73.61 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.36 | -18.16 | -77.15 | 1602 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.94 | -51.01 | -96.94 | 4251 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.50 | -99.93 | 8233 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T10:05 | Three white soldiers | sell | BTC-USD | 16.74 | -0.12 | exit signal |
| 2026-11-05T10:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.78 | 0.16 | exit signal |
| 2026-11-05T10:00 | Three white soldiers | buy | BTC-USD | 16.86 | — | entry signal |
| 2026-11-05T09:46 | Three white soldiers | sell | XRP-USD | 16.77 | -0.12 | exit signal |
| 2026-11-05T09:40 | Three white soldiers | buy | XRP-USD | 16.89 | — | entry signal |
| 2026-11-05T09:05 | Three white soldiers | sell | XRP-USD | 16.77 | -0.16 | stop-loss |
| 2026-11-05T09:00 | Williams %R · 1h | buy | DOGE-USD | 1.12 | — | entry signal |
| 2026-11-05T09:00 | VWAP reversion · 1h | sell | DOGE-USD | 25.01 | 0.03 | exit signal |
| 2026-11-05T09:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.84 | 0.07 | exit signal |
| 2026-11-05T09:00 | Three white soldiers · 1h | buy | XRP-USD | 23.63 | — | entry signal |
| 2026-11-05T09:00 | OBV trend · 1h | buy | DOGE-USD | 6.28 | — | entry signal |
| 2026-11-05T09:00 | VWAP momentum · 1h | buy | SOL-USD | 6.15 | — | entry signal |
| 2026-11-05T09:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.28 | — | entry signal |
| 2026-11-05T09:00 | Parabolic SAR · 1h | buy | SOL-USD | 9.99 | — | entry signal |
| 2026-11-05T09:00 | MACD cross · 1h | buy | XRP-USD | 3.90 | — | entry signal |
| 2026-11-05T09:00 | MACD cross · 1h | buy | SOL-USD | 3.90 | — | entry signal |
| 2026-11-05T08:30 | Three white soldiers | buy | XRP-USD | 16.93 | — | entry signal |
| 2026-11-05T08:00 | OBV trend · 1h | sell | DOGE-USD | 6.77 | -0.07 | exit signal |
| 2026-11-05T08:00 | VWAP momentum · 1h | sell | ETH-USD | 6.21 | -0.08 | exit signal |
| 2026-11-05T08:00 | VWAP momentum · 1h | sell | BTC-USD | 6.22 | -0.06 | exit signal |
| 2026-11-05T08:00 | MACD zero-line · 1h | sell | SOL-USD | 8.64 | 0.11 | exit signal |
| 2026-11-05T08:00 | MACD cross · 1h | sell | SOL-USD | 4.11 | 0.09 | exit signal |
| 2026-11-05T07:05 | VWAP reversion · 1h | buy | DOGE-USD | 24.98 | — | entry |
| 2026-11-05T07:00 | Connors RSI(2) · 1h | sell | ETH-USD | 20.75 | -0.03 | exit signal |
| 2026-11-05T07:00 | Connors RSI(2) · 1h | sell | BTC-USD | 20.72 | -0.06 | exit signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | XRP-USD | 5.98 | — | entry signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | ETH-USD | 6.28 | — | entry signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | BTC-USD | 6.28 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | ETH-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | BTC-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Volume breakout · 1h | sell | ETH-USD | 7.04 | 0.07 | exit signal |
| 2026-11-05T06:00 | Volume breakout · 1h | sell | BTC-USD | 7.67 | -0.02 | exit signal |
| 2026-11-05T06:00 | VWAP momentum · 1h | sell | XRP-USD | 5.26 | -0.03 | exit signal |
| 2026-11-05T05:45 | Three white soldiers | sell | XRP-USD | 16.82 | -0.14 | exit signal |
| 2026-11-05T05:40 | Three white soldiers | buy | XRP-USD | 16.97 | — | entry signal |
| 2026-11-05T05:00 | Agent (ML meta-label) | buy | XRP-USD | 5.10 | — | entry |
| 2026-11-05T05:00 | Agent (ML meta-label) | sell | SOL-USD | 5.10 | -0.05 | selected signal exited |
| 2026-11-05T05:00 | ROC + volume · 1h | sell | BTC-USD | 3.92 | 0.03 | exit signal |
| 2026-11-05T05:00 | VWAP momentum · 1h | sell | SOL-USD | 6.87 | -0.06 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 10:25:05.000122+00:00 -> 2026-11-05 10:35:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 10:25:05.000122+00:00 -> 2026-11-05 10:35:05.000122+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 10:25:05.000122+00:00 -> 2026-11-05 10:35:05.000122+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
