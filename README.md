# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-28T13:00:05.000163+00:00 · 39048 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.98 (-10.02%)

Closed trades 116, win rate 38.8%, fees £3.50, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-28 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 9366 decisions in 1878 calls, $0.1309 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-28T13:00 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-28T13:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-28T13:00 | 0 / 5 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.31 | +6.31% | 11 |
| MACD zero-line | MSFT | 2.19 | +0.66% | 5 |
| VWAP momentum · 1h | LABU | 2.05 | +21.96% | 3 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.30 | 7.30 | 0 | — | 8.22 | 4.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.24 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.30 | 1.30 | 0 | — | 2.52 | 1.18 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.71 | -3.76 | -14.59 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.75 | -0.25 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 7.46 | 3.49 | -2.42 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.90 | -2.10 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.53 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.44 | -3.56 | 123 | 31.7 | -4.47 | -2.47 | -7.67 | 186 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.18 | -3.81 | 0 | — | -5.83 | -2.37 | -7.83 | 1 |
| 16 | Hold BTC | benchmark | 96.02 | -3.98 | 0 | — | 0.84 | 0.31 | -9.28 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.01 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.18 | 1.69 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.75 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.70 | -6.30 | 51 | 15.7 | -13.63 | -3.04 | -15.40 | 101 |
| 22 | Trend pullback · 1h | trend | 93.22 | -6.78 | 96 | 22.9 | -20.99 | -6.96 | -21.20 | 110 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.75 | -7.25 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 24 | Parabolic SAR · 1h | trend | 92.72 | -7.28 | 125 | 28.0 | -20.12 | -4.91 | -22.91 | 247 |
| 25 | ADX DI cross · 1h | trend | 92.13 | -7.87 | 120 | 18.3 | -14.23 | -3.06 | -16.04 | 271 |
| 26 | Daily: Momentum burst | daily | 92.08 | -7.92 | 13 | 15.4 | -17.98 | -3.47 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 92.00 | -8.00 | 29 | 37.9 | -19.85 | -3.90 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.48 | -8.52 | 11 | 18.2 | -6.76 | -0.81 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.40 | -8.60 | 12 | 41.7 | -14.31 | -1.28 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.20 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.05 | -8.95 | 55 | 23.6 | -5.07 | -1.33 | -12.22 | 96 |
| 32 | Volume breakout · 1h | breakout | 90.33 | -9.67 | 113 | 26.5 | -12.82 | -2.67 | -16.02 | 105 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.02 | -6.38 | -12.20 | 209 |
| 34 | Bollinger breakout · 1h | breakout | 88.93 | -11.07 | 114 | 27.2 | -11.44 | -2.21 | -18.15 | 247 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.62 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.98 | -12.02 | 205 | 47.3 | -20.58 | -3.81 | -22.35 | 389 |
| 37 | Keltner breakout · 1h | breakout | 87.48 | -12.52 | 74 | 23.0 | -18.89 | -3.62 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -3.96 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.11 | -12.89 | 125 | 36.0 | -12.68 | -2.00 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 86.01 | -13.99 | 114 | 14.0 | -23.76 | -4.81 | -26.59 | 232 |
| 41 | RSI momentum · 1h | momentum | 85.18 | -14.82 | 106 | 15.1 | -24.33 | -4.83 | -26.87 | 213 |
| 42 | Connors RSI(2) · 1h | reversion | 84.91 | -15.09 | 176 | 40.9 | -23.52 | -7.35 | -23.76 | 178 |
| 43 | EMA 20/50 cross · 1h | trend | 84.60 | -15.40 | 73 | 11.0 | -22.95 | -4.66 | -24.49 | 138 |
| 44 | MACD cross · 1h | trend | 84.42 | -15.58 | 248 | 23.0 | -27.49 | -5.32 | -29.94 | 475 |
| 45 | Ichimoku · 1h | trend | 84.26 | -15.74 | 68 | 11.8 | -19.90 | -4.04 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.79 | -16.21 | 101 | 14.9 | -28.31 | -5.37 | -31.19 | 205 |
| 47 | MFI reversion · 1h | reversion | 83.57 | -16.43 | 274 | 32.1 | -16.01 | -2.46 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.73 | -17.27 | 230 | 45.2 | -23.41 | -3.35 | -28.06 | 461 |
| 49 | Williams %R · 1h | reversion | 82.28 | -17.72 | 232 | 47.0 | -34.45 | -5.83 | -35.53 | 536 |
| 50 | Donchian 20/10 · 1h | breakout | 82.21 | -17.79 | 100 | 21.0 | -23.14 | -4.37 | -26.02 | 220 |
| 51 | MACD zero-line · 1h | trend | 81.43 | -18.57 | 112 | 15.2 | -23.95 | -5.11 | -25.67 | 229 |
| 52 | Agent (ML meta-label) | meta | 80.98 | -19.02 | 982 | 20.6 | -8.87 | -1.62 | -17.82 | 365 |
| 53 | Bollinger reversion · 1h | reversion | 80.94 | -19.06 | 182 | 37.4 | -28.99 | -5.92 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.77 | -19.23 | 209 | 17.7 | -31.38 | -6.45 | -33.78 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 80.54 | -19.46 | 107 | 27.1 | -15.78 | -2.94 | -24.48 | 185 |
| 56 | ROC + volume · 1h | momentum | 79.50 | -20.50 | 259 | 25.9 | -29.21 | -5.51 | -31.48 | 377 |
| 57 | Heikin-Ashi · 1h | trend | 78.44 | -21.56 | 305 | 22.6 | -42.73 | -9.34 | -43.95 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.55 | -22.45 | 285 | 29.5 | -36.01 | -7.31 | -36.80 | 540 |
| 59 | VWAP momentum · 1h | momentum | 76.96 | -23.04 | 585 | 22.7 | -49.48 | -10.82 | -50.46 | 1234 |
| 60 | EMA 9/21 cross · 1h | trend | 76.89 | -23.11 | 176 | 10.8 | -29.59 | -6.23 | -31.61 | 337 |
| 61 | Three white soldiers | momentum | 76.19 | -23.81 | 334 | 18.6 | -45.37 | -21.42 | -45.42 | 613 |
| 62 | Max aggression: 1-day momentum | meta | 72.71 | -27.29 | 20 | 30.0 | -37.60 | -2.42 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 52.08 | -47.92 | 826 | 21.9 | -75.51 | -27.46 | -75.52 | 1570 |
| 64 | Volume breakout | breakout | 51.00 | -49.00 | 502 | 12.4 | -64.51 | -26.49 | -64.53 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -43.53 | -98.86 | 5110 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.08 | -23.38 | -79.18 | 1409 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.72 | -45.94 | -93.72 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -30.29 | -89.21 | 1918 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.61 | -38.11 | -91.61 | 2339 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.50 | -31.65 | -90.50 | 2201 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -52.32 | -97.86 | 3499 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -59.58 | -96.25 | 3390 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -36.85 | -94.12 | 2470 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.53 | -34.41 | -82.53 | 1694 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -52.85 | -99.42 | 5753 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.16 | -44.05 | -93.16 | 2640 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.71 | -95.43 | 3398 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -75.95 | -99.78 | 6176 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.40 | -44.90 | -92.41 | 2310 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.82 | -65.42 | -97.82 | 3589 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.72 | -98.66 | 4788 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.31 | -30.10 | -69.34 | 1189 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -57.19 | -94.83 | 2776 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.95 | -39.85 | -84.96 | 1817 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.95 | -99.61 | 6298 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.25 | -28.67 | -88.28 | 2222 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.66 | -18.97 | -76.87 | 1685 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -36.85 | -90.61 | 2261 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.30 | -47.53 | -96.30 | 3814 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.06 | -48.90 | -90.06 | 2129 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.10 | -24.59 | -73.14 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.34 | -18.05 | -76.49 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.63 | -49.65 | -96.64 | 4204 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -105.07 | -99.92 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-28T13:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 21.24 | — | entry signal |
| 2026-10-28T13:00 | Donchian 55/20 · 1h | buy | DOGE-USD | 3.89 | — | rebalance up |
| 2026-10-28T13:00 | Donchian 55/20 · 1h | sell | XRP-USD | 3.89 | -0.06 | exit signal |
| 2026-10-28T13:00 | Donchian 20/10 · 1h | buy | SOL-USD | 5.48 | — | entry |
| 2026-10-28T13:00 | Donchian 20/10 · 1h | sell | XRP-USD | 8.28 | 0.02 | exit signal |
| 2026-10-28T13:00 | RSI momentum · 1h | buy | DOGE-USD | 5.07 | — | entry |
| 2026-10-28T13:00 | RSI momentum · 1h | buy | BTC-USD | 5.33 | — | entry |
| 2026-10-28T13:00 | RSI momentum · 1h | sell | XRP-USD | 5.64 | -0.02 | exit signal |
| 2026-10-28T13:00 | RSI momentum · 1h | sell | ETH-USD | 4.25 | -0.02 | exit signal |
| 2026-10-28T13:00 | VWAP momentum · 1h | sell | SOL-USD | 3.20 | 0.00 | exit signal |
| 2026-10-28T13:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.44 | 0.08 | exit signal |
| 2026-10-28T13:00 | Heikin-Ashi · 1h | sell | SOL-USD | 4.83 | -0.08 | exit signal |
| 2026-10-28T13:00 | Parabolic SAR · 1h | sell | DOGE-USD | 11.51 | 0.23 | exit signal |
| 2026-10-28T13:00 | Parabolic SAR · 1h | sell | BTC-USD | 11.34 | 0.06 | exit signal |
| 2026-10-28T13:00 | MACD zero-line · 1h | buy | SOL-USD | 6.79 | — | entry |
| 2026-10-28T13:00 | MACD zero-line · 1h | sell | ETH-USD | 8.95 | -0.05 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | ETH-USD | 5.22 | 0.04 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | DOGE-USD | 3.64 | -0.04 | exit signal |
| 2026-10-28T13:00 | MACD cross · 1h | sell | BTC-USD | 4.91 | 0.03 | exit signal |
| 2026-10-28T12:35 | Bollinger breakout · 1h | sell | SOL-USD | 5.49 | -0.08 | stop-loss |
| 2026-10-28T12:35 | Donchian 55/20 · 1h | buy | DOGE-USD | 5.44 | — | rebalance up |
| 2026-10-28T12:35 | Donchian 55/20 · 1h | sell | BTC-USD | 5.44 | -0.08 | stop-loss |
| 2026-10-28T12:35 | VWAP momentum · 1h | sell | ETH-USD | 4.47 | -0.08 | stop-loss |
| 2026-10-28T12:35 | VWAP momentum · 1h | sell | BTC-USD | 4.23 | -0.07 | stop-loss |
| 2026-10-28T12:15 | Squeeze breakout · 1h | sell | BTC-USD | 18.20 | -0.01 | stop-loss |
| 2026-10-28T12:15 | Bollinger breakout · 1h | sell | DOGE-USD | 5.18 | -0.07 | stop-loss |
| 2026-10-28T12:15 | Bollinger breakout · 1h | sell | BTC-USD | 6.36 | 0.02 | stop-loss |
| 2026-10-28T12:10 | Squeeze breakout · 1h | sell | ETH-USD | 18.25 | -0.03 | stop-loss |
| 2026-10-28T12:10 | Bollinger breakout · 1h | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-10-28T12:10 | Bollinger breakout · 1h | sell | ETH-USD | 6.35 | 0.05 | stop-loss |
| 2026-10-28T12:00 | Connors RSI(2) · 1h | buy | XRP-USD | 21.30 | — | entry signal |
| 2026-10-28T12:00 | Squeeze breakout · 1h | sell | XRP-USD | 18.24 | 0.05 | exit signal |
| 2026-10-28T12:00 | Bollinger breakout · 1h | buy | SOL-USD | 1.08 | — | entry |
| 2026-10-28T12:00 | Bollinger breakout · 1h | buy | DOGE-USD | 5.25 | — | entry |
| 2026-10-28T12:00 | Bollinger breakout · 1h | sell | XRP-USD | 6.33 | 0.05 | exit signal |
| 2026-10-28T12:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 4.00 | 0.09 | exit signal |
| 2026-10-28T12:00 | Heikin-Ashi · 1h | sell | BTC-USD | 4.33 | -0.03 | exit signal |
| 2026-10-28T12:00 | Parabolic SAR · 1h | sell | ETH-USD | 11.43 | 0.14 | exit signal |
| 2026-10-28T10:00 | Heikin-Ashi · 1h | buy | BTC-USD | 4.36 | — | entry signal |
| 2026-10-28T09:30 | Three white soldiers | sell | BTC-USD | 19.03 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-30 13:00:05.000163+00:00 -> 2026-10-28 13:10:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
