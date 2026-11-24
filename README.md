# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-24T15:10:05.000110+00:00 · 71953 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £78.69 (-21.31%)

Closed trades 241, win rate 35.7%, fees £6.52, max drawdown -21.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-24 | WWB 12%, PEPG 12%, KNOP 12%, BORR 12%, PAM 12%, ANAB 12%, BH 12%, FUN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-23)

**Correction** since 2026-11-13 · level correction · 4 distribution days in 25 sessions · timing exposure 0% · VXN 36.31 · VIX 26.62 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.4, AAPL 4.1, TSLA 3.2, AMZN 1.1, GOOGL 0.8, META 0.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 15063 decisions in 2439 calls, $0.2028 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-24T15:10 | 2 / 14 / 14 | cash |  |
| Breezy | 2026-11-24T15:10 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-24T15:10 | 5 / 21 / 4 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | SQQQ | 2.14 | +6.46% | 11 |
| Z-score reversion | SQQQ | 1.84 | +8.94% | 4 |
| RSI(14) reversion | SQQQ | 1.68 | +6.49% | 3 |
| MFI reversion | SQQQ | 1.62 | +10.95% | 3 |
| CCI reversion | SQQQ | 1.58 | +9.47% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 128.32 | 28.32 | 27 | 66.7 | 28.17 | 4.27 | -5.42 | 28 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.80 | 15.80 | 0 | — | 13.59 | 4.70 | -4.89 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 109.37 | 9.37 | 41 | 43.9 | 7.71 | 1.41 | -9.74 | 34 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.44 | 4.44 | 0 | — | 4.29 | 1.29 | -6.60 | 0 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.91 | 3.91 | 42 | 28.6 | 3.23 | 0.66 | -12.39 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Gap and go | momentum | 98.74 | -1.26 | 218 | 31.7 | 0.23 | 0.16 | -8.58 | 209 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 96.71 | -3.29 | 168 | 33.3 | -3.22 | -3.22 | -4.52 | 61 |
| 10 | Agent (rotation) | meta | 96.35 | -3.65 | 228 | 28.5 | 0.05 | 0.10 | -7.48 | 155 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -4.84 | -2.88 | -7.38 | 1 |
| 12 | Hold SPY | benchmark | 94.49 | -5.50 | 0 | — | -6.53 | -1.63 | -11.71 | 1 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.38 | -8.28 | -5.49 | 19 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 92.07 | -7.93 | 0 | — | -8.61 | -1.76 | -13.87 | 1 |
| 15 | Copy: Insider buying | copy | 91.47 | -8.53 | 58 | 39.7 | -7.35 | -1.37 | -14.79 | 70 |
| 16 | Trend pullback · 1h | trend | 91.39 | -8.61 | 116 | 24.1 | -8.60 | -4.58 | -11.83 | 39 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 90.60 | -9.40 | 28 | 17.9 | -9.83 | -7.53 | -10.08 | 25 |
| 18 | Copy: Congress Democrats (NANC) | copy | 89.82 | -10.18 | 0 | — | -11.20 | -2.41 | -17.03 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -14.61 | -2.99 | -20.94 | 1 |
| 20 | VWAP reversion · 1h | reversion | 86.59 | -13.41 | 163 | 46.0 | -11.01 | -2.02 | -20.49 | 153 |
| 21 | Opening range 30m | breakout | 85.96 | -14.04 | 463 | 33.3 | -13.53 | -4.55 | -14.39 | 546 |
| 22 | Daily: Bullish score | daily | 85.28 | -14.72 | 20 | 20.0 | -13.98 | -3.13 | -19.56 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 83.20 | -16.80 | 77 | 19.5 | -19.03 | -6.99 | -19.04 | 75 |
| 24 | Daily: Connors RSI(2) · 3x ETFs | daily | 83.13 | -16.87 | 10 | 40.0 | -14.04 | -0.88 | -26.65 | 6 |
| 25 | Connors RSI(2) · 1h | reversion | 79.97 | -20.04 | 221 | 40.7 | -14.80 | -6.59 | -14.96 | 66 |
| 26 | Parabolic SAR · 1h | trend | 79.27 | -20.73 | 205 | 28.3 | -31.30 | -8.30 | -31.72 | 183 |
| 27 | Agent | meta | 78.69 | -21.31 | 241 | 35.7 | -25.19 | -5.66 | -25.55 | 196 |
| 28 | Agent (aggressive) | meta | 77.54 | -22.46 | 111 | 32.4 | -14.71 | -4.13 | -17.05 | 85 |
| 29 | Opening range 15m | breakout | 77.21 | -22.79 | 574 | 31.0 | -22.00 | -6.85 | -22.95 | 670 |
| 30 | Volume breakout · 1h | breakout | 76.53 | -23.47 | 169 | 27.8 | -24.01 | -7.40 | -24.18 | 72 |
| 31 | Donchian 55/20 · 1h | breakout | 75.98 | -24.02 | 87 | 13.8 | -30.20 | -8.05 | -30.20 | 84 |
| 32 | Keltner breakout · 1h | breakout | 75.64 | -24.36 | 137 | 24.8 | -27.28 | -7.16 | -27.50 | 149 |
| 33 | Ichimoku · 1h | trend | 73.54 | -26.46 | 113 | 15.9 | -30.34 | -8.00 | -31.21 | 102 |
| 34 | Daily: Momentum burst | daily | 70.00 | -30.00 | 31 | 16.1 | -35.06 | -4.86 | -36.53 | 24 |
| 35 | ADX DI cross · 1h | trend | 69.93 | -30.07 | 253 | 19.0 | -39.93 | -7.44 | -40.38 | 278 |
| 36 | Hold BTC | benchmark | 69.51 | -30.49 | 3 | 0.0 | -29.02 | -5.17 | -36.10 | 1 |
| 37 | Supertrend · 1h | trend | 69.05 | -30.95 | 204 | 18.6 | -34.96 | -6.77 | -35.68 | 212 |
| 38 | Copy: Cathie Wood (ARKK) | copy | 69.04 | -30.96 | 3 | 0.0 | -24.42 | -2.92 | -32.18 | 1 |
| 39 | Triple EMA stack · 1h | trend | 68.44 | -31.56 | 169 | 15.4 | -39.23 | -10.38 | -39.73 | 164 |
| 40 | EMA 20/50 cross · 1h | trend | 67.84 | -32.16 | 123 | 9.8 | -37.43 | -10.16 | -38.51 | 115 |
| 41 | Bollinger breakout · 1h | breakout | 67.60 | -32.40 | 208 | 22.1 | -34.46 | -9.18 | -35.40 | 213 |
| 42 | OBV trend · 1h | momentum | 66.46 | -33.54 | 323 | 19.8 | -39.93 | -10.23 | -40.97 | 232 |
| 43 | Heikin-Ashi · 1h | trend | 64.61 | -35.39 | 528 | 22.2 | -48.05 | -9.85 | -49.06 | 629 |
| 44 | MACD zero-line · 1h | trend | 64.55 | -35.45 | 198 | 16.7 | -33.74 | -9.06 | -33.76 | 205 |
| 45 | RSI momentum · 1h | momentum | 64.18 | -35.82 | 200 | 15.0 | -41.60 | -9.66 | -41.88 | 195 |
| 46 | Stochastic reversion · 1h | reversion | 64.10 | -35.90 | 397 | 40.6 | -35.55 | -3.91 | -43.59 | 433 |
| 47 | Max aggression: 5-day momentum | meta | 61.64 | -38.36 | 26 | 34.6 | -63.45 | -4.22 | -67.33 | 23 |
| 48 | ROC + volume · 1h | momentum | 61.58 | -38.42 | 452 | 27.0 | -43.44 | -8.72 | -43.62 | 341 |
| 49 | Donchian 20/10 · 1h | breakout | 60.97 | -39.03 | 181 | 17.7 | -41.37 | -8.87 | -42.88 | 193 |
| 50 | MFI reversion · 1h | reversion | 60.29 | -39.71 | 494 | 33.0 | -33.47 | -5.04 | -35.63 | 181 |
| 51 | Max aggression: 1-day momentum | meta | 59.59 | -40.41 | 34 | 26.5 | -59.14 | -4.35 | -60.19 | 38 |
| 52 | EMA 9/21 cross · 1h | trend | 59.56 | -40.44 | 307 | 12.4 | -44.67 | -10.67 | -46.09 | 333 |
| 53 | MACD cross · 1h | trend | 58.03 | -41.97 | 474 | 21.1 | -52.10 | -10.42 | -53.02 | 514 |
| 54 | Agent (ML meta-label) | meta | 57.28 | -42.72 | 2050 | 25.0 | -19.84 | -2.39 | -27.32 | 335 |
| 55 | CCI reversion · 1h | reversion | 56.60 | -43.40 | 437 | 39.4 | -50.26 | -8.48 | -51.89 | 506 |
| 56 | Bollinger reversion · 1h | reversion | 56.19 | -43.81 | 391 | 37.6 | -39.53 | -4.79 | -45.42 | 430 |
| 57 | VWAP momentum · 1h | momentum | 53.49 | -46.51 | 1060 | 21.7 | -57.33 | -13.00 | -58.49 | 1188 |
| 58 | Williams %R · 1h | reversion | 51.37 | -48.63 | 506 | 37.9 | -54.73 | -8.96 | -56.03 | 591 |
| 59 | Candlestick reversal · 1h ⛔ | reversion | 50.96 | -49.04 | 604 | 25.7 | -51.69 | -8.48 | -52.63 | 681 |
| 60 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.19 | -50.03 | -99.19 | 5431 |
| 61 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -84.08 | -33.94 | -84.24 | 1441 |
| 62 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.56 | -50.29 | -94.57 | 2440 |
| 63 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.63 | -32.44 | -90.63 | 1916 |
| 64 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.89 | -42.26 | -91.90 | 2256 |
| 65 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.66 | -28.63 | -89.74 | 1966 |
| 66 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -98.20 | -49.46 | -98.20 | 3437 |
| 67 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.03 | -55.34 | -97.03 | 3394 |
| 68 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.37 | -38.10 | -93.38 | 2106 |
| 69 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.51 | -35.30 | -83.54 | 1561 |
| 70 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.67 | -57.62 | -99.67 | 6277 |
| 71 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.26 | -39.11 | -93.28 | 2502 |
| 72 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.39 | -36.51 | -94.42 | 3165 |
| 73 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.60 | -99.82 | 6131 |
| 74 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -93.35 | -44.88 | -93.35 | 2277 |
| 75 | Three white soldiers ⛔ | momentum | 50.14 | -49.86 | 639 | 14.2 | -51.76 | -22.33 | -51.80 | 641 |
| 76 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -78.88 | -23.87 | -78.88 | 1615 |
| 77 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.81 | -59.57 | -97.81 | 3291 |
| 78 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.17 | -62.01 | -99.17 | 5128 |
| 79 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 80 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -71.10 | -27.34 | -71.12 | 1199 |
| 81 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -95.01 | -48.51 | -95.03 | 2675 |
| 82 | Z-score reversion · 1h ⛔ | reversion | 49.92 | -50.08 | 247 | 32.4 | -46.38 | -6.52 | -48.78 | 280 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.58 | -37.37 | -85.58 | 1675 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.76 | -75.38 | -99.76 | 6536 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -91.39 | -31.05 | -91.40 | 2476 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -82.87 | -20.25 | -82.87 | 1955 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.74 | -31.36 | -91.74 | 2173 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -98.11 | -49.72 | -98.11 | 4063 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.41 | -48.61 | -90.42 | 2208 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -68.70 | -29.57 | -68.73 | 798 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -28.38 | -73.57 | 1170 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -83.81 | -19.01 | -83.81 | 1829 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -98.00 | -50.21 | -98.00 | 4412 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -102.83 | -99.94 | 8273 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |
| 96 | RSI(14) reversion · 1h ⛔ | reversion | 49.47 | -50.53 | 256 | 30.1 | -46.90 | -7.01 | -50.99 | 303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-24T15:10 | MFI reversion · 1h | buy | UPRO | 3.29 | — | rebalance up |
| 2026-11-24T15:10 | MFI reversion · 1h | sell | COIN | 3.14 | -0.19 | stop-loss |
| 2026-11-24T15:10 | CCI reversion · 1h | sell | COIN | 2.53 | -0.15 | stop-loss |
| 2026-11-24T15:10 | Williams %R · 1h | sell | COIN | 5.20 | -0.27 | stop-loss |
| 2026-11-24T15:10 | MACD cross · 1h | sell | COIN | 4.42 | -0.26 | stop-loss |
| 2026-11-24T15:05 | Day trade: Stocks in Play ORB | buy | TNA | 24.23 | — | entry |
| 2026-11-24T15:05 | Day trade: Stocks in Play ORB | buy | LABU | 24.23 | — | entry |
| 2026-11-24T15:05 | Agent (ML meta-label) | buy | MSTR | 7.93 | — | rebalance up |
| 2026-11-24T15:05 | Agent (ML meta-label) | sell | SQQQ | 11.45 | 0.57 | selected signal exited |
| 2026-11-24T15:05 | MFI reversion · 1h | sell | TNA | 3.04 | 0.07 | target is flat |
| 2026-11-24T15:05 | MFI reversion · 1h | sell | MSFT | 3.19 | 0.00 | target is flat |
| 2026-11-24T15:05 | Opening range 30m | buy | UPRO | 21.60 | — | entry signal |
| 2026-11-24T15:05 | Opening range 30m | buy | TNA | 21.60 | — | entry signal |
| 2026-11-24T15:05 | Opening range 30m | buy | SPY | 21.60 | — | entry signal |
| 2026-11-24T15:05 | Opening range 30m | buy | IWM | 21.60 | — | entry signal |
| 2026-11-24T15:05 | Opening range 15m | buy | TQQQ | 7.03 | — | entry |
| 2026-11-24T15:05 | Opening range 15m | buy | QQQ | 7.05 | — | entry |
| 2026-11-24T15:05 | Opening range 15m | buy | PLTR | 7.05 | — | entry signal |
| 2026-11-24T15:05 | Opening range 15m | buy | META | 7.05 | — | entry |
| 2026-11-24T15:05 | Opening range 15m | sell | UPRO | 4.06 | 0.03 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | TNA | 4.02 | 0.01 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | SPY | 4.01 | 0.01 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | MSFT | 4.00 | -0.01 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | IWM | 4.00 | 0.00 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | AMZN | 4.04 | 0.01 | rebalance down |
| 2026-11-24T15:05 | Opening range 15m | sell | AAPL | 4.03 | 0.00 | rebalance down |
| 2026-11-24T15:00 | Bollinger reversion · 1h | buy | XRP-USD | 14.19 | — | entry signal |
| 2026-11-24T15:00 | Bollinger reversion · 1h | buy | SOL-USD | 14.19 | — | entry signal |
| 2026-11-24T15:00 | Bollinger reversion · 1h | buy | DOGE-USD | 14.19 | — | entry signal |
| 2026-11-24T15:00 | VWAP momentum · 1h | buy | BTC-USD | 8.87 | — | entry signal |
| 2026-11-24T15:00 | VWAP momentum · 1h | sell | GOOGL | 8.87 | -0.08 | target is flat |
| 2026-11-24T14:55 | Opening range 15m | buy | TNA | 11.03 | — | entry signal |
| 2026-11-24T14:55 | Opening range 15m | buy | IWM | 11.04 | — | entry signal |
| 2026-11-24T14:55 | Opening range 15m | sell | UPRO | 4.46 | 0.01 | rebalance down |
| 2026-11-24T14:55 | Opening range 15m | sell | SPY | 4.43 | 0.00 | rebalance down |
| 2026-11-24T14:55 | Opening range 15m | sell | MSFT | 4.39 | -0.01 | rebalance down |
| 2026-11-24T14:55 | Opening range 15m | sell | AMZN | 4.41 | -0.01 | rebalance down |
| 2026-11-24T14:55 | Opening range 15m | sell | AAPL | 4.39 | -0.01 | rebalance down |
| 2026-11-24T14:50 | Agent (rotation) | sell | LABU | 7.89 | -0.13 | selected signal exited |
| 2026-11-24T14:50 | Day trade: Stocks in Play ORB | sell | TNA | 24.51 | 0.11 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-26 15:10:05.000110+00:00 -> 2026-11-24 15:20:05.000110+00:00); yahoo: cooling down after a rate limit
- PORT-: yfinance: $PORT-: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
