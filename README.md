# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T20:40:05.000140+00:00 · 58608 ticks

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
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 40047 decisions in 3279 calls, $0.4952 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T20:40 | 4 / 11 / 15 | cash |  |
| Breezy | 2026-11-13T20:40 | 0 / 23 / 7 | cash |  |
| Boozy | 2026-11-13T20:40 | 3 / 24 / 3 | COIN 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| MFI reversion | LABU | 1.92 | +6.76% | 3 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.50 | 17.50 | 0 | — | 14.94 | 5.00 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.61 | 15.61 | 34 | 29.4 | 24.00 | 3.44 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.56 | 12.56 | 22 | 68.2 | 15.97 | 3.27 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.13 | 5.13 | 32 | 43.8 | 5.05 | 1.28 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 104.53 | 4.53 | 0 | — | 6.49 | 1.79 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.27 | 1.27 | 141 | 34.8 | 7.84 | 3.08 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.10 | -1.90 | 0 | — | -0.82 | -0.21 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.69 | -3.31 | 1 | 0.0 | -3.45 | -2.23 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.43 | -3.57 | 191 | 30.4 | -2.49 | -0.85 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.24 | -3.77 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 94.19 | -5.81 | 43 | 39.5 | -5.10 | -0.95 | -14.81 | 66 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.40 | -6.60 | 0 | — | -5.10 | -1.36 | -10.64 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.24 | -6.76 | 22 | 18.2 | -9.00 | -7.52 | -9.14 | 22 |
| 20 | Trend pullback · 1h | trend | 91.76 | -8.24 | 110 | 22.7 | -15.18 | -5.61 | -17.77 | 70 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -11.03 | -2.36 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.99 | -14.01 | 433 | 33.3 | -10.11 | -3.19 | -14.11 | 604 |
| 24 | Daily: Bullish score | daily | 85.73 | -14.27 | 16 | 18.8 | -10.22 | -1.62 | -19.56 | 15 |
| 25 | Agent | meta | 85.50 | -14.50 | 195 | 35.9 | -14.97 | -7.48 | -15.94 | 208 |
| 26 | Parabolic SAR · 1h | trend | 85.14 | -14.86 | 176 | 29.0 | -15.74 | -3.40 | -22.50 | 218 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -16.11 | -4.44 | -18.51 | 97 |
| 28 | Donchian 55/20 · 1h | breakout | 81.79 | -18.21 | 73 | 13.7 | -23.26 | -4.85 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.32 | -18.68 | 1 | 0.0 | -11.13 | -1.55 | -22.00 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 81.04 | -18.96 | 2 | 0.0 | -9.68 | -1.11 | -24.16 | 1 |
| 31 | Connors RSI(2) · 1h | reversion | 80.62 | -19.38 | 212 | 40.1 | -18.17 | -6.39 | -18.32 | 115 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Keltner breakout · 1h | breakout | 80.41 | -19.59 | 121 | 25.6 | -17.48 | -3.54 | -25.39 | 171 |
| 34 | Stochastic reversion · 1h | reversion | 79.60 | -20.40 | 303 | 47.5 | -26.63 | -3.93 | -28.07 | 398 |
| 35 | Opening range 15m | breakout | 78.44 | -21.56 | 526 | 31.2 | -17.34 | -4.65 | -21.36 | 720 |
| 36 | MFI reversion · 1h | reversion | 77.68 | -22.32 | 401 | 35.4 | -22.62 | -2.94 | -27.13 | 171 |
| 37 | ADX DI cross · 1h | trend | 76.67 | -23.33 | 198 | 19.7 | -24.04 | -3.63 | -32.23 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -40.72 | -2.63 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | MACD cross · 1h | trend | 74.64 | -25.36 | 385 | 23.6 | -29.28 | -4.35 | -38.65 | 470 |
| 42 | Heikin-Ashi · 1h | trend | 74.55 | -25.45 | 444 | 24.1 | -38.27 | -7.10 | -39.41 | 670 |
| 43 | Max aggression: 1-day momentum | meta | 74.46 | -25.54 | 29 | 27.6 | -20.61 | -0.64 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.44 | -26.57 | 171 | 18.7 | -23.81 | -4.68 | -30.99 | 202 |
| 45 | RSI momentum · 1h | momentum | 72.52 | -27.48 | 171 | 14.0 | -26.69 | -4.08 | -37.92 | 208 |
| 46 | Supertrend · 1h | trend | 72.51 | -27.49 | 180 | 15.0 | -30.66 | -5.24 | -36.51 | 216 |
| 47 | EMA 20/50 cross · 1h | trend | 72.34 | -27.66 | 109 | 10.1 | -28.47 | -4.80 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 71.87 | -28.13 | 303 | 41.6 | -33.25 | -5.20 | -35.72 | 383 |
| 49 | Triple EMA stack · 1h | trend | 71.58 | -28.42 | 151 | 14.6 | -28.33 | -4.68 | -38.65 | 205 |
| 50 | ROC + volume · 1h | momentum | 71.23 | -28.77 | 399 | 28.8 | -31.46 | -5.78 | -38.37 | 377 |
| 51 | CCI reversion · 1h | reversion | 71.05 | -28.95 | 346 | 43.4 | -37.62 | -5.89 | -38.71 | 471 |
| 52 | OBV trend · 1h | momentum | 69.63 | -30.37 | 299 | 19.1 | -30.30 | -5.35 | -38.15 | 276 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.35 | -4.53 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.19 | -30.80 | 153 | 19.0 | -30.35 | -5.43 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.84 | -32.16 | 383 | 43.6 | -42.44 | -6.92 | -44.04 | 543 |
| 56 | Z-score reversion · 1h | reversion | 65.45 | -34.55 | 204 | 37.3 | -30.56 | -4.32 | -31.55 | 237 |
| 57 | Agent (ML meta-label) | meta | 64.88 | -35.12 | 1855 | 24.7 | -21.34 | -3.63 | -25.31 | 348 |
| 58 | EMA 9/21 cross · 1h | trend | 64.71 | -35.29 | 267 | 11.6 | -37.89 | -7.65 | -43.16 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 64.32 | -35.69 | 186 | 32.8 | -37.10 | -5.50 | -38.35 | 239 |
| 60 | VWAP momentum · 1h | momentum | 62.48 | -37.52 | 914 | 22.3 | -52.87 | -10.67 | -53.42 | 1241 |
| 61 | Candlestick reversal · 1h | reversion | 61.97 | -38.03 | 486 | 28.4 | -44.93 | -8.28 | -45.99 | 604 |
| 62 | Three white soldiers | momentum | 58.34 | -41.66 | 542 | 14.6 | -49.50 | -22.28 | -49.51 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.00 | -44.57 | -99.00 | 5307 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.04 | -25.54 | -80.33 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.86 | -46.58 | -93.86 | 2552 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -31.66 | -89.28 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -41.66 | -91.30 | 2354 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.83 | -31.39 | -89.83 | 2199 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -52.35 | -97.89 | 3505 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.23 | -56.43 | -96.23 | 3433 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.72 | -32.79 | -93.72 | 2336 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -34.71 | -83.20 | 1662 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.55 | -99.57 | 6035 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -43.30 | -92.25 | 2636 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.29 | -95.43 | 3480 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.05 | -99.81 | 6177 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.28 | -43.24 | -92.29 | 2284 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.85 | -26.21 | -75.87 | 1644 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -61.38 | -97.63 | 3529 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.88 | -64.05 | -98.88 | 4944 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.70 | -27.10 | -68.70 | 1254 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.77 | -58.04 | -94.77 | 2815 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.22 | -39.85 | -85.24 | 1794 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.76 | -99.66 | 6387 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.05 | -32.62 | -90.19 | 2328 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.51 | -20.17 | -78.89 | 1798 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -36.40 | -90.82 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.01 | -51.91 | -97.02 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -58.31 | -89.44 | 2161 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.55 | -30.83 | -66.55 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.55 | -23.20 | -71.55 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.10 | -19.28 | -80.47 | 1754 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.00 | -97.41 | 4356 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -114.38 | -99.93 | 8469 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T20:35 | Keltner breakout · 1h | sell | AAPL | 20.10 | -0.14 | stop-loss |
| 2026-11-13T20:35 | OBV trend · 1h | buy | TSLA | 17.41 | — | entry |
| 2026-11-13T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 93.19 | — | entry |
| 2026-11-13T20:30 | Connors RSI(2) · 1h | buy | AAPL | 20.16 | — | entry signal |
| 2026-11-13T20:30 | OBV trend · 1h | sell | TSLA | 17.37 | -0.03 | target is flat |
| 2026-11-13T20:30 | ROC + volume · 1h | sell | AAPL | 18.15 | -0.00 | exit signal |
| 2026-11-13T20:30 | VWAP momentum · 1h | buy | AMD | 2.84 | — | entry signal |
| 2026-11-13T20:30 | VWAP momentum · 1h | sell | TSLA | 3.29 | -0.00 | exit signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | UPRO | 9.30 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | TNA | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | TECL | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | SPY | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | buy | MSTR | 9.34 | — | entry signal |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | MSFT | 9.37 | -0.02 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | META | 9.50 | 0.04 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | DOGE-USD | 9.12 | -0.08 | rebalance down |
| 2026-11-13T20:30 | Heikin-Ashi · 1h | sell | AAPL | 18.68 | -0.10 | exit signal |
| 2026-11-13T20:30 | EMA 9/21 cross · 1h | buy | META | 12.95 | — | entry |
| 2026-11-13T20:30 | EMA 9/21 cross · 1h | sell | AMD | 13.09 | 0.52 | exit signal |
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | META | 3.10 | — | entry |
| 2026-11-13T20:06 | Agent (ML meta-label) | buy | AMZN | 4.07 | — | following Supertrend |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | MSTR | 3.54 | — | entry |
| 2026-11-13T20:00 | Bollinger reversion · 1h | buy | ETHU | 6.75 | — | rebalance up |
| 2026-11-13T20:00 | Bollinger reversion · 1h | sell | ETH-USD | 10.30 | -0.04 | exit signal |
| 2026-11-13T20:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 18.60 | — | entry signal |
| 2026-11-13T19:55 | Agent (ML meta-label) | sell | AMZN | 5.89 | -0.01 | selected signal exited |
| 2026-11-13T19:50 | Agent (ML meta-label) | buy | AMZN | 5.90 | — | following Supertrend |
| 2026-11-13T19:45 | Agent (ML meta-label) | sell | MSTR | 5.73 | -0.02 | selected signal exited |
| 2026-11-13T19:45 | Agent (ML meta-label) | sell | AMZN | 1.45 | -0.00 | selected signal exited |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | SOXL | 3.83 | — | entry |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | ETHU | 7.79 | — | entry |
| 2026-11-13T19:45 | MFI reversion · 1h | buy | COIN | 4.55 | — | rebalance up |
| 2026-11-13T19:45 | MFI reversion · 1h | sell | TSLA | 9.67 | 0.03 | target is flat |
| 2026-11-13T19:45 | MFI reversion · 1h | sell | BITX | 6.49 | -0.01 | target is flat |
| 2026-11-13T19:45 | ROC + volume · 1h | buy | META | 17.81 | — | entry |
| 2026-11-13T19:41 | Agent (ML meta-label) | buy | AMZN | 1.45 | — | following Supertrend |
| 2026-11-13T19:41 | Agent (ML meta-label) | sell | PLTR | 1.45 | -0.00 | selected signal exited |
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | PLTR | 1.45 | — | following VWAP reversion |
| 2026-11-13T19:35 | Agent (ML meta-label) | buy | MSTR | 5.75 | — | entry |
| 2026-11-13T19:35 | Agent (ML meta-label) | sell | UPRO | 3.79 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 20:40:05.000140+00:00 -> 2026-11-13 20:50:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
