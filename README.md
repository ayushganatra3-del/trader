# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T16:55:05.000146+00:00 · 23824 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.04 (-6.96%)

Closed trades 74, win rate 40.5%, fees £2.60, max drawdown -7.41%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 24930 decisions in 2502 calls, $0.3149 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T16:55 | 1 / 20 / 8 | COIN 15% |  |
| Breezy | 2026-10-15T16:55 | 0 / 28 / 1 | cash |  |
| Boozy | 2026-10-15T16:55 | 1 / 26 / 2 | MSTR 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.73 | 4.73 | 0 | — | 4.43 | 2.11 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.61 | 3.61 | 1 | 100.0 | 4.21 | 1.15 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.46 | 1.99 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -3.22 | -0.99 | -9.61 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.63 | 0.63 | 0 | — | 4.35 | 1.70 | -5.18 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Copy: Insider buying | copy | 99.99 | -0.01 | 20 | 45.0 | -16.13 | -2.56 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 99.95 | -0.05 | 0 | — | -0.88 | -0.47 | -3.31 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 11 | VWAP reversion · 1h | reversion | 99.91 | -0.09 | 58 | 39.7 | -11.77 | -3.24 | -14.08 | 115 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.43 | -1.57 | 0 | — | -1.17 | -0.45 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 97.92 | -2.08 | 0 | — | 29.87 | 3.44 | -8.68 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.60 | -2.40 | 0 | — | -5.27 | -2.89 | -6.38 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 97.58 | -2.42 | 36 | 16.7 | 7.04 | 0.98 | -22.11 | 112 |
| 18 | Trend pullback · 1h | trend | 96.91 | -3.09 | 86 | 24.4 | -23.31 | -6.77 | -23.89 | 160 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.72 | -3.28 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 21 | Daily: Momentum burst | daily | 96.14 | -3.86 | 5 | 20.0 | -4.53 | -0.54 | -17.67 | 39 |
| 22 | ADX DI cross · 1h | trend | 96.11 | -3.89 | 70 | 21.4 | -10.47 | -1.91 | -15.50 | 255 |
| 23 | Agent (rotation) | meta | 95.87 | -4.13 | 105 | 31.4 | -13.37 | -4.58 | -14.56 | 271 |
| 24 | Max aggression: 5-day momentum | meta | 94.12 | -5.88 | 8 | 37.5 | -5.57 | -0.20 | -34.64 | 26 |
| 25 | Parabolic SAR · 1h | trend | 93.83 | -6.17 | 93 | 22.6 | 3.48 | 0.62 | -21.79 | 282 |
| 26 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.17 | 1.12 | -9.46 | 101 |
| 27 | EMA 20/50 cross · 1h | trend | 93.55 | -6.45 | 51 | 15.7 | 4.52 | 0.70 | -24.71 | 132 |
| 28 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 8.94 | 2.25 | -6.78 | 202 |
| 29 | Daily: Bullish score | daily | 93.34 | -6.66 | 7 | 0.0 | -4.13 | -0.34 | -12.76 | 13 |
| 30 | Agent | meta | 93.04 | -6.96 | 74 | 40.5 | -8.31 | -3.77 | -8.72 | 229 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 92.69 | -7.31 | 0 | — | 3.97 | 0.75 | -13.89 | 1 |
| 32 | MACD cross · 1h | trend | 92.50 | -7.50 | 154 | 22.1 | -13.23 | -1.79 | -23.19 | 462 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 92.38 | -7.62 | 0 | — | -16.25 | -3.06 | -19.22 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 92.06 | -7.94 | 79 | 30.4 | 5.99 | 0.95 | -14.21 | 274 |
| 35 | RSI momentum · 1h | momentum | 92.01 | -7.99 | 73 | 17.8 | 1.00 | 0.33 | -26.04 | 222 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.60 | -8.40 | 74 | 13.5 | 1.54 | 0.39 | -22.72 | 212 |
| 38 | Triple EMA stack · 1h | trend | 90.78 | -9.22 | 77 | 16.9 | -6.84 | -0.50 | -32.16 | 234 |
| 39 | Ichimoku · 1h | trend | 90.46 | -9.54 | 51 | 15.7 | 0.95 | 0.32 | -22.64 | 123 |
| 40 | Opening range 30m | breakout | 90.45 | -9.55 | 170 | 22.9 | -12.89 | -3.74 | -17.60 | 570 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -14.75 | -4.70 | -15.15 | 117 |
| 42 | Stochastic reversion · 1h | reversion | 90.19 | -9.81 | 128 | 44.5 | -19.17 | -3.50 | -20.99 | 352 |
| 43 | Connors RSI(2) · 1h | reversion | 89.57 | -10.43 | 142 | 40.1 | -23.33 | -6.98 | -24.89 | 248 |
| 44 | MFI reversion · 1h | reversion | 89.47 | -10.53 | 187 | 29.4 | -17.66 | -3.06 | -20.09 | 143 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -17.02 | -0.63 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.50 | -11.49 | 164 | 18.9 | -11.16 | -0.96 | -35.11 | 319 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -15.43 | -2.24 | -29.11 | 213 |
| 48 | MACD zero-line · 1h | trend | 87.81 | -12.19 | 74 | 16.2 | -21.16 | -4.07 | -22.24 | 224 |
| 49 | Z-score reversion · 1h | reversion | 87.39 | -12.61 | 71 | 33.8 | -11.56 | -2.04 | -17.27 | 179 |
| 50 | Agent (ML meta-label) | meta | 86.82 | -13.19 | 568 | 18.5 | -11.77 | -1.82 | -19.84 | 429 |
| 51 | ROC + volume · 1h | momentum | 86.32 | -13.68 | 180 | 21.7 | -8.54 | -1.03 | -25.31 | 400 |
| 52 | Opening range 15m | breakout | 86.27 | -13.73 | 216 | 20.4 | -18.14 | -4.88 | -21.40 | 709 |
| 53 | Donchian 20/10 · 1h | breakout | 86.16 | -13.84 | 72 | 19.4 | -0.92 | 0.09 | -20.56 | 219 |
| 54 | Heikin-Ashi · 1h | trend | 86.00 | -14.00 | 170 | 26.5 | -30.30 | -4.91 | -39.15 | 662 |
| 55 | VWAP momentum · 1h | momentum | 85.86 | -14.14 | 354 | 21.8 | -35.46 | -5.23 | -43.06 | 1247 |
| 56 | Three white soldiers | momentum | 85.85 | -14.15 | 195 | 18.5 | -47.42 | -19.06 | -48.84 | 602 |
| 57 | EMA 9/21 cross · 1h | trend | 85.10 | -14.90 | 120 | 12.5 | -8.40 | -0.86 | -28.14 | 320 |
| 58 | Bollinger reversion · 1h | reversion | 83.61 | -16.39 | 132 | 31.8 | -28.28 | -6.10 | -31.47 | 340 |
| 59 | Williams %R · 1h | reversion | 83.11 | -16.89 | 166 | 42.2 | -32.22 | -5.30 | -34.85 | 525 |
| 60 | CCI reversion · 1h | reversion | 82.69 | -17.31 | 141 | 41.8 | -17.11 | -2.23 | -23.38 | 423 |
| 61 | RSI(14) reversion · 1h | reversion | 82.67 | -17.33 | 61 | 23.0 | -13.81 | -2.46 | -18.95 | 176 |
| 62 | Candlestick reversal · 1h | reversion | 79.83 | -20.17 | 182 | 25.3 | -33.22 | -6.18 | -34.19 | 528 |
| 63 | ROC + volume | momentum | 67.04 | -32.97 | 506 | 22.5 | -74.33 | -16.55 | -76.56 | 1685 |
| 64 | RSI(14) reversion | reversion | 66.68 | -33.32 | 570 | 28.8 | -73.37 | -16.28 | -74.28 | 1568 |
| 65 | Volume breakout | breakout | 65.01 | -34.99 | 313 | 13.4 | -63.44 | -17.81 | -63.51 | 888 |
| 66 | Squeeze breakout | breakout | 64.68 | -35.32 | 405 | 14.8 | -62.71 | -17.33 | -63.39 | 1207 |
| 67 | Donchian 55/20 | breakout | 63.32 | -36.68 | 402 | 17.2 | -69.04 | -14.24 | -71.15 | 1279 |
| 68 | EMA 20/50 cross | trend | 61.68 | -38.33 | 423 | 18.7 | -77.31 | -14.95 | -78.49 | 1440 |
| 69 | VWAP reversion | reversion | 58.34 | -41.66 | 581 | 24.6 | -72.59 | -15.08 | -72.83 | 1433 |
| 70 | AI bee: Boozy | ai | 57.74 | -42.26 | 277 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.38 | -43.62 | 570 | 14.9 | -83.35 | -25.86 | -83.62 | 1843 |
| 72 | Supertrend | trend | 54.62 | -45.38 | 582 | 18.7 | -86.41 | -20.00 | -86.62 | 1908 |
| 73 | Ichimoku | trend | 53.74 | -46.26 | 493 | 9.7 | -81.99 | -22.17 | -82.21 | 1700 |
| 74 | AI bee: Bizzy | ai | 51.01 | -48.99 | 1018 | 8.3 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.81 | -98.63 | 5338 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.37 | -28.54 | -93.47 | 2574 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -23.93 | -90.72 | 2348 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.52 | -26.03 | -91.53 | 2318 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -31.46 | -97.49 | 3503 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -33.88 | -96.59 | 3565 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -24.16 | -94.36 | 2605 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.15 | -99.41 | 5745 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.10 | -24.89 | -91.20 | 2622 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -29.98 | -96.18 | 3541 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.14 | -99.73 | 6151 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -28.69 | -91.94 | 2360 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.22 | -97.47 | 3635 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.53 | -98.55 | 4698 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.45 | -31.16 | -93.54 | 2774 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -37.85 | -99.55 | 6172 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.25 | -21.88 | -86.48 | 2113 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.63 | -26.44 | -87.95 | 2109 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -31.60 | -96.09 | 3778 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -33.01 | -89.50 | 2116 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -32.76 | -95.89 | 4073 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.44 | -99.89 | 8197 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T16:55 | Keltner breakout | buy | SOL-USD | 4.73 | — | rebalance up |
| 2026-10-15T16:55 | Keltner breakout | buy | MSTR | 4.68 | — | rebalance up |
| 2026-10-15T16:55 | Keltner breakout | buy | MSFT | 4.71 | — | rebalance up |
| 2026-10-15T16:55 | Keltner breakout | buy | COIN | 4.65 | — | rebalance up |
| 2026-10-15T16:55 | Keltner breakout | sell | ETHU | 9.42 | 0.03 | target is flat |
| 2026-10-15T16:46 | AI bee: Bizzy | buy | COIN | 7.44 | — | Jev: buy (buy p=0.58) |
| 2026-10-15T16:40 | Keltner breakout | sell | ETH-USD | 9.35 | 0.03 | stop-loss |
| 2026-10-15T16:40 | ROC + volume | sell | COIN | 16.84 | 0.11 | exit signal |
| 2026-10-15T16:35 | ROC + volume | sell | ETHU | 16.71 | -0.15 | exit signal |
| 2026-10-15T16:35 | ROC + volume | sell | ETH-USD | 16.70 | 0.00 | exit signal |
| 2026-10-15T16:30 | MFI reversion · 1h | sell | PLTR | 9.01 | 0.04 | target is flat |
| 2026-10-15T16:30 | Z-score reversion · 1h | buy | NVDA | 7.27 | — | entry signal |
| 2026-10-15T16:30 | Bollinger reversion · 1h | buy | NVDA | 9.28 | — | entry signal |
| 2026-10-15T16:30 | Bollinger reversion · 1h | buy | AMD | 9.28 | — | entry signal |
| 2026-10-15T16:30 | Connors RSI(2) · 1h | sell | PLTR | 22.71 | 0.44 | exit signal |
| 2026-10-15T16:30 | OBV trend · 1h | buy | MSFT | 22.14 | — | entry signal |
| 2026-10-15T16:30 | VWAP momentum · 1h | buy | DOGE-USD | 6.12 | — | entry |
| 2026-10-15T16:30 | VWAP momentum · 1h | sell | GOOGL | 6.12 | -0.05 | exit signal |
| 2026-10-15T16:30 | Trend pullback · 1h | buy | MSFT | 24.23 | — | entry signal |
| 2026-10-15T16:30 | Heikin-Ashi · 1h | buy | TNA | 21.46 | — | entry signal |
| 2026-10-15T16:30 | Heikin-Ashi · 1h | buy | IWM | 21.46 | — | entry signal |
| 2026-10-15T16:30 | Heikin-Ashi · 1h | sell | SQQQ | 22.19 | 0.80 | exit signal |
| 2026-10-15T16:30 | Parabolic SAR · 1h | buy | MSFT | 23.46 | — | entry signal |
| 2026-10-15T16:30 | Keltner breakout | buy | SOL-USD | 5.35 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | buy | MSTR | 5.31 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | buy | MSFT | 5.04 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | buy | ETHU | 5.35 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | buy | ETH-USD | 5.36 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | buy | COIN | 3.06 | — | rebalance up |
| 2026-10-15T16:30 | Keltner breakout | sell | XRP-USD | 4.02 | 0.02 | exit signal |
| 2026-10-15T16:30 | Keltner breakout | sell | DOGE-USD | 4.02 | -0.01 | stop-loss |
| 2026-10-15T16:30 | Keltner breakout | sell | BTC-USD | 4.02 | 0.01 | exit signal |
| 2026-10-15T16:30 | Keltner breakout | sell | BITX | 4.03 | -0.01 | exit signal |
| 2026-10-15T16:30 | Opening range 15m | buy | UPRO | 4.10 | — | entry |
| 2026-10-15T16:30 | Opening range 15m | sell | GOOGL | 4.32 | -0.03 | rebalance down |
| 2026-10-15T16:30 | Donchian 55/20 | buy | UPRO | 1.52 | — | entry |
| 2026-10-15T16:30 | Donchian 55/20 | buy | SPY | 5.75 | — | entry |
| 2026-10-15T16:30 | Donchian 55/20 | sell | LABU | 6.30 | 0.00 | exit signal |
| 2026-10-15T16:30 | EMA 20/50 cross | buy | ETHU | 3.86 | — | entry |
| 2026-10-15T16:30 | EMA 20/50 cross | sell | AMZN | 3.86 | -0.02 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 16:55:05.000146+00:00 -> 2026-10-15 17:05:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
