# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T23:30:05.000218+00:00 · 38401 ticks

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
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-27)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 24.91 · VIX 17.52 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.8, MSFT 7.3, PLTR 6.5, AAPL 6.1, SQQQ 4.5, LABU 3.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 38902 decisions in 3476 calls, $0.4838 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T23:30 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-27T23:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T23:30 | 2 / 3 / 0 | ETH-USD 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.34 | +7.11% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |
| Candlestick reversal | LABU | 1.85 | +4.39% | 10 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.13 | 7.13 | 0 | — | 8.22 | 4.05 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 3.78 | 1.25 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.88 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.78 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.14 | 1.14 | 0 | — | 2.52 | 1.19 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.23 | -3.69 | -14.11 | 148 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.60 | -0.40 | 0 | — | -0.00 | 0.05 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.03 | -0.97 | 86 | 37.2 | 6.76 | 3.25 | -2.11 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.75 | -2.25 | 0 | — | -0.98 | -0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -3.39 | -4.57 | -4.22 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -2.06 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.39 | -3.61 | 123 | 31.7 | -3.52 | -2.08 | -7.67 | 175 |
| 15 | Hold BTC | benchmark | 96.13 | -3.87 | 0 | — | 2.21 | 0.54 | -9.28 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.04 | -3.96 | 0 | — | -5.83 | -2.39 | -7.83 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.22 | 1.02 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.50 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 120 | 30.0 | 5.14 | 1.69 | -8.76 | 203 |
| 20 | Opening range 30m | breakout | 93.84 | -6.16 | 285 | 37.2 | -9.36 | -2.77 | -17.21 | 587 |
| 21 | Donchian 55/20 · 1h | breakout | 93.70 | -6.30 | 49 | 16.3 | -12.89 | -2.87 | -15.40 | 97 |
| 22 | Trend pullback · 1h | trend | 93.46 | -6.54 | 96 | 22.9 | -23.09 | -7.44 | -23.22 | 113 |
| 23 | Parabolic SAR · 1h | trend | 92.61 | -7.39 | 121 | 25.6 | -19.99 | -4.91 | -22.91 | 247 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.60 | -7.40 | 0 | — | -3.09 | -0.35 | -14.57 | 1 |
| 25 | ADX DI cross · 1h | trend | 91.98 | -8.02 | 120 | 18.3 | -14.03 | -3.05 | -15.83 | 271 |
| 26 | Daily: Momentum burst | daily | 91.97 | -8.03 | 13 | 15.4 | -17.98 | -3.50 | -19.23 | 39 |
| 27 | Copy: Insider buying | copy | 91.86 | -8.14 | 29 | 37.9 | -19.85 | -3.93 | -22.94 | 63 |
| 28 | Daily: Bullish score | daily | 91.34 | -8.66 | 11 | 18.2 | -6.76 | -0.82 | -14.40 | 14 |
| 29 | Max aggression: 5-day momentum | meta | 91.26 | -8.74 | 12 | 41.7 | -14.31 | -1.29 | -27.23 | 25 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.41 | -2.22 | -16.91 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 91.09 | -8.91 | 52 | 23.1 | -4.47 | -1.17 | -12.21 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.34 | -9.66 | 112 | 26.8 | -11.77 | -2.43 | -15.94 | 112 |
| 33 | Agent | meta | 89.98 | -10.02 | 116 | 38.8 | -10.01 | -6.43 | -12.20 | 208 |
| 34 | Bollinger breakout · 1h | breakout | 89.01 | -10.99 | 109 | 26.6 | -11.29 | -2.20 | -18.15 | 246 |
| 35 | Agent (aggressive) | meta | 88.06 | -11.94 | 58 | 36.2 | -11.00 | -3.65 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.88 | -12.12 | 205 | 47.3 | -20.80 | -3.87 | -22.35 | 388 |
| 37 | Keltner breakout · 1h | breakout | 87.35 | -12.65 | 74 | 23.0 | -19.82 | -3.84 | -23.13 | 187 |
| 38 | Opening range 15m | breakout | 87.30 | -12.70 | 351 | 33.3 | -14.09 | -4.00 | -17.87 | 709 |
| 39 | Z-score reversion · 1h | reversion | 87.01 | -12.99 | 125 | 36.0 | -12.68 | -2.01 | -21.48 | 207 |
| 40 | Supertrend · 1h | trend | 85.87 | -14.13 | 114 | 14.0 | -23.68 | -4.83 | -26.59 | 230 |
| 41 | RSI momentum · 1h | momentum | 85.18 | -14.82 | 104 | 15.4 | -24.11 | -4.83 | -26.87 | 211 |
| 42 | Connors RSI(2) · 1h | reversion | 85.16 | -14.84 | 176 | 40.9 | -23.72 | -7.49 | -24.36 | 179 |
| 43 | EMA 20/50 cross · 1h | trend | 84.55 | -15.45 | 73 | 11.0 | -22.69 | -4.64 | -24.49 | 136 |
| 44 | MACD cross · 1h | trend | 84.42 | -15.58 | 244 | 22.1 | -27.96 | -5.49 | -29.94 | 477 |
| 45 | Ichimoku · 1h | trend | 84.13 | -15.87 | 68 | 11.8 | -19.81 | -4.05 | -24.73 | 114 |
| 46 | Triple EMA stack · 1h | trend | 83.73 | -16.27 | 101 | 14.9 | -28.02 | -5.35 | -31.19 | 204 |
| 47 | MFI reversion · 1h | reversion | 83.50 | -16.50 | 274 | 32.1 | -16.07 | -2.49 | -20.70 | 153 |
| 48 | CCI reversion · 1h | reversion | 82.61 | -17.39 | 230 | 45.2 | -24.54 | -3.51 | -28.06 | 462 |
| 49 | Donchian 20/10 · 1h | breakout | 82.16 | -17.84 | 99 | 20.2 | -22.93 | -4.36 | -26.02 | 219 |
| 50 | Williams %R · 1h | reversion | 82.16 | -17.84 | 232 | 47.0 | -34.79 | -5.93 | -35.85 | 536 |
| 51 | MACD zero-line · 1h | trend | 81.39 | -18.61 | 111 | 15.3 | -23.76 | -5.11 | -25.67 | 229 |
| 52 | Agent (ML meta-label) | meta | 80.86 | -19.14 | 982 | 20.6 | -9.61 | -1.63 | -18.67 | 337 |
| 53 | Bollinger reversion · 1h | reversion | 80.84 | -19.16 | 182 | 37.4 | -29.08 | -6.00 | -30.19 | 364 |
| 54 | OBV trend · 1h | momentum | 80.70 | -19.30 | 209 | 17.7 | -31.46 | -6.51 | -33.78 | 294 |
| 55 | RSI(14) reversion · 1h | reversion | 80.43 | -19.57 | 107 | 27.1 | -18.17 | -3.37 | -24.48 | 193 |
| 56 | ROC + volume · 1h | momentum | 79.38 | -20.62 | 259 | 25.9 | -30.36 | -5.81 | -32.63 | 380 |
| 57 | Heikin-Ashi · 1h | trend | 78.45 | -21.55 | 300 | 22.7 | -42.97 | -9.52 | -44.66 | 666 |
| 58 | Candlestick reversal · 1h | reversion | 77.43 | -22.57 | 285 | 29.5 | -39.01 | -7.76 | -39.77 | 554 |
| 59 | VWAP momentum · 1h | momentum | 77.16 | -22.84 | 575 | 22.3 | -49.46 | -10.86 | -51.28 | 1237 |
| 60 | Three white soldiers | momentum | 76.92 | -23.08 | 326 | 19.0 | -45.20 | -21.43 | -45.20 | 609 |
| 61 | EMA 9/21 cross · 1h | trend | 76.79 | -23.21 | 176 | 10.8 | -29.61 | -6.30 | -31.61 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 72.60 | -27.40 | 20 | 30.0 | -37.60 | -2.44 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.45 | -46.55 | 814 | 22.2 | -74.79 | -27.18 | -74.96 | 1567 |
| 64 | Volume breakout | breakout | 51.79 | -48.21 | 491 | 12.6 | -63.74 | -26.35 | -64.24 | 809 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -44.88 | -98.86 | 5119 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.00 | -23.62 | -79.67 | 1417 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -46.02 | -93.67 | 2525 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.00 | -30.32 | -89.25 | 1919 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.45 | -38.54 | -91.61 | 2341 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.40 | -32.83 | -90.41 | 2192 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -55.43 | -97.88 | 3510 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -59.74 | -96.16 | 3374 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.04 | -37.41 | -94.05 | 2465 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.22 | -34.47 | -82.42 | 1689 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -56.36 | -99.43 | 5762 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -44.28 | -93.10 | 2634 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -40.16 | -95.42 | 3387 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -81.91 | -99.78 | 6177 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -45.98 | -92.42 | 2318 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -67.43 | -97.81 | 3590 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.82 | -98.65 | 4791 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.85 | -29.94 | -68.94 | 1183 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -58.46 | -94.71 | 2774 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -39.65 | -84.59 | 1809 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -69.90 | -99.61 | 6295 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.26 | -29.46 | -88.27 | 2225 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.37 | -19.00 | -76.79 | 1681 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -38.27 | -90.63 | 2272 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -49.15 | -96.26 | 3811 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -51.04 | -90.05 | 2129 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.89 | -24.93 | -73.43 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.28 | -18.28 | -76.49 | 1577 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -51.11 | -96.55 | 4194 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -116.76 | -99.92 | 8284 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T22:25 | Volume breakout | sell | XRP-USD | 12.96 | -0.11 | exit signal |
| 2026-10-27T22:00 | Triple EMA stack · 1h | buy | BTC-USD | 4.60 | — | entry |
| 2026-10-27T22:00 | Triple EMA stack · 1h | sell | XRP-USD | 4.60 | 0.08 | rebalance down |
| 2026-10-27T22:00 | Volume breakout | sell | SOL-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | Volume breakout | sell | ETH-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | SOL-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T22:00 | ROC + volume | sell | ETH-USD | 13.33 | -0.13 | stop-loss |
| 2026-10-27T21:45 | Volume breakout | sell | BTC-USD | 12.95 | -0.12 | stop-loss |
| 2026-10-27T21:45 | ROC + volume | sell | BTC-USD | 13.34 | -0.12 | stop-loss |
| 2026-10-27T21:35 | Volume breakout | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | SOL-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | ETH-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | Volume breakout | buy | BTC-USD | 13.07 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | SOL-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | ETH-USD | 13.46 | — | entry signal |
| 2026-10-27T21:35 | ROC + volume | buy | BTC-USD | 13.46 | — | entry signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | XRP-USD | 4.32 | -0.03 | exit signal |
| 2026-10-27T21:00 | Heikin-Ashi · 1h | sell | ETH-USD | 1.35 | -0.01 | exit signal |
| 2026-10-27T20:20 | Three white soldiers | sell | SOL-USD | 19.16 | -0.12 | exit signal |
| 2026-10-27T20:15 | Three white soldiers | sell | ETH-USD | 19.20 | -0.15 | exit signal |
| 2026-10-27T20:00 | OBV trend · 1h | buy | BTC-USD | 7.33 | — | entry signal |
| 2026-10-27T20:00 | OBV trend · 1h | sell | XRP-USD | 4.13 | 0.02 | rebalance down |
| 2026-10-27T20:00 | OBV trend · 1h | sell | DOGE-USD | 4.14 | -0.00 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 2.04 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | buy | BTC-USD | 10.56 | — | entry signal |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | XRP-USD | 6.30 | 0.09 | rebalance down |
| 2026-10-27T20:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 6.29 | 0.00 | rebalance down |
| 2026-10-27T20:00 | Three white soldiers | buy | SOL-USD | 19.28 | — | entry |
| 2026-10-27T19:55 | Agent (rotation) | sell | TQQQ | 32.22 | 0.12 | selected signal exited |
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | TSLA | 24.98 | 0.40 | target is flat |
| 2026-10-27T19:55 | Day trade: Stocks in Play ORB | sell | AMD | 24.86 | 0.28 | target is flat |
| 2026-10-27T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.82 | -0.11 | target is flat |
| 2026-10-27T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 106.48 | 0.40 | target is flat |
| 2026-10-27T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 97.54 | -0.24 | target is flat |
| 2026-10-27T19:55 | Agent (ML meta-label) | buy | SOXL | 4.11 | — | rebalance up |
| 2026-10-27T19:55 | Agent (ML meta-label) | buy | META | 20.18 | — | following VWAP reversion |
| 2026-10-27T19:55 | Agent (aggressive) | sell | PLTR | 43.97 | -0.12 | selected signal exited |
| 2026-10-27T19:55 | Agent | sell | PLTR | 17.96 | -0.05 | selected signal exited |
| 2026-10-27T19:55 | Three white soldiers | sell | SPY | 19.33 | -0.02 | end-of-day flatten |
| 2026-10-27T19:55 | Three white soldiers | sell | SOL-USD | 19.17 | -0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 23:30:05.000218+00:00 -> 2026-10-27 23:40:05.000218+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
