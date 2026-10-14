# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T15:57:05.000132+00:00 · 22621 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £94.26 (-5.74%)

Closed trades 65, win rate 46.2%, fees £2.41, max drawdown -6.17%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 21.14 · VIX 15.27 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 20452 decisions in 2321 calls, $0.2623 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T15:57 | 1 / 6 / 22 | cash |  |
| Breezy | 2026-10-14T15:57 | 0 / 21 / 8 | cash |  |
| Boozy | 2026-10-14T15:57 | 0 / 26 / 3 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |
| Keltner breakout | LABU | 1.69 | +7.27% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.14 | 4.14 | 0 | — | 2.88 | 1.44 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.58 | 2.58 | 18 | 50.0 | -15.58 | -2.48 | -21.97 | 76 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.79 | 1.79 | 0 | — | 5.45 | 2.07 | -5.18 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.65 | 1.66 | 8 | 62.5 | 4.81 | 2.14 | -3.27 | 19 |
| 6 | VWAP reversion · 1h | reversion | 101.65 | 1.65 | 44 | 40.9 | -8.44 | -2.53 | -13.79 | 114 |
| 7 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 101.32 | 1.32 | 8 | 62.5 | -4.30 | -1.46 | -9.84 | 26 |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.98 | -7.55 | 43 |
| 9 | Hold SPY | benchmark | 100.92 | 0.92 | 0 | — | -0.75 | -0.40 | -3.58 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.69 | -0.31 | 0 | — | -1.06 | -0.42 | -3.21 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.33 | -0.67 | 0 | — | -4.26 | -2.45 | -5.09 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.15 | -0.85 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -3.21 | -3.73 | -3.51 | 20 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.02 | -2.07 | 67 |
| 17 | Hold BTC | benchmark | 98.21 | -1.79 | 0 | — | 29.05 | 3.38 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 97.03 | -2.97 | 86 | 24.4 | -24.46 | -6.93 | -25.21 | 168 |
| 19 | Donchian 55/20 · 1h | breakout | 96.96 | -3.04 | 34 | 14.7 | 5.69 | 0.84 | -22.11 | 114 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.64 | -0.39 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 22 | Max aggression: 1-day momentum | meta | 96.62 | -3.38 | 13 | 38.5 | -8.69 | -0.11 | -37.31 | 42 |
| 23 | Agent (rotation) | meta | 96.52 | -3.48 | 90 | 31.1 | -13.48 | -4.64 | -15.28 | 274 |
| 24 | Timing: Nasdaq FTD · TQQQ | daily | 96.34 | -3.66 | 0 | — | -13.56 | -2.64 | -15.27 | 1 |
| 25 | ADX DI cross · 1h | trend | 96.28 | -3.72 | 68 | 19.1 | -5.96 | -0.92 | -13.66 | 253 |
| 26 | Daily: Bullish score | daily | 96.03 | -3.97 | 5 | 0.0 | -1.95 | -0.06 | -12.76 | 12 |
| 27 | EMA 20/50 cross · 1h | trend | 94.88 | -5.12 | 45 | 15.6 | 4.52 | 0.70 | -23.70 | 136 |
| 28 | Parabolic SAR · 1h | trend | 94.26 | -5.74 | 92 | 22.8 | 0.49 | 0.26 | -23.46 | 287 |
| 29 | Agent | meta | 94.26 | -5.74 | 65 | 46.2 | -6.36 | -2.36 | -8.75 | 228 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 93.99 | -6.01 | 0 | — | 3.96 | 0.76 | -10.34 | 1 |
| 31 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.14 | 0.92 | -9.46 | 103 |
| 32 | Stochastic reversion · 1h | reversion | 93.52 | -6.48 | 112 | 50.0 | -16.21 | -3.11 | -16.39 | 348 |
| 33 | Gap and go | momentum | 93.50 | -6.50 | 62 | 11.3 | 9.07 | 2.30 | -6.78 | 199 |
| 34 | MACD cross · 1h | trend | 93.36 | -6.64 | 148 | 23.0 | -12.51 | -1.67 | -21.65 | 457 |
| 35 | Supertrend · 1h | trend | 92.58 | -7.42 | 69 | 11.6 | 2.25 | 0.47 | -22.11 | 210 |
| 36 | RSI momentum · 1h | momentum | 92.46 | -7.54 | 69 | 14.5 | 1.76 | 0.41 | -24.48 | 225 |
| 37 | Z-score reversion · 1h | reversion | 92.35 | -7.65 | 60 | 38.3 | -4.75 | -0.82 | -11.06 | 158 |
| 38 | Agent (aggressive) | meta | 92.13 | -7.87 | 33 | 36.4 | -2.99 | -0.91 | -6.57 | 118 |
| 39 | Bollinger breakout · 1h | breakout | 91.58 | -8.42 | 78 | 29.5 | 7.14 | 1.08 | -14.21 | 277 |
| 40 | Max aggression: 5-day momentum | meta | 91.08 | -8.92 | 8 | 37.5 | -7.56 | -0.37 | -34.64 | 27 |
| 41 | Connors RSI(2) · 1h | reversion | 90.92 | -9.08 | 131 | 42.0 | -21.03 | -6.16 | -22.79 | 258 |
| 42 | MFI reversion · 1h | reversion | 90.86 | -9.13 | 174 | 30.5 | -15.61 | -2.75 | -17.17 | 130 |
| 43 | Ichimoku · 1h | trend | 90.80 | -9.20 | 50 | 16.0 | -0.27 | 0.18 | -23.18 | 126 |
| 44 | Volume breakout · 1h | breakout | 90.62 | -9.38 | 77 | 22.1 | 8.12 | 1.27 | -12.60 | 118 |
| 45 | Triple EMA stack · 1h | trend | 90.58 | -9.42 | 74 | 14.9 | -8.69 | -0.72 | -32.73 | 239 |
| 46 | Agent (ML meta-label) | meta | 89.55 | -10.45 | 495 | 18.4 | -4.16 | -0.57 | -13.30 | 395 |
| 47 | Opening range 30m | breakout | 88.87 | -11.13 | 167 | 22.8 | -14.05 | -4.23 | -17.60 | 558 |
| 48 | OBV trend · 1h | momentum | 88.28 | -11.72 | 163 | 19.0 | -10.58 | -0.91 | -34.52 | 322 |
| 49 | RSI(14) reversion · 1h | reversion | 87.82 | -12.18 | 48 | 27.1 | -10.88 | -2.03 | -13.14 | 155 |
| 50 | Keltner breakout · 1h | breakout | 87.55 | -12.45 | 50 | 22.0 | -7.31 | -0.77 | -26.75 | 212 |
| 51 | MACD zero-line · 1h | trend | 87.01 | -12.99 | 74 | 16.2 | -22.55 | -4.41 | -22.72 | 228 |
| 52 | Donchian 20/10 · 1h | breakout | 86.74 | -13.26 | 69 | 18.8 | -0.81 | 0.10 | -20.27 | 217 |
| 53 | Bollinger reversion · 1h | reversion | 86.53 | -13.46 | 105 | 34.3 | -27.42 | -6.22 | -27.58 | 321 |
| 54 | Williams %R · 1h | reversion | 86.22 | -13.78 | 153 | 43.8 | -30.83 | -5.21 | -31.19 | 511 |
| 55 | ROC + volume · 1h | momentum | 85.69 | -14.31 | 177 | 21.5 | -11.14 | -1.46 | -25.30 | 396 |
| 56 | VWAP momentum · 1h | momentum | 85.66 | -14.34 | 346 | 22.0 | -36.41 | -5.48 | -42.76 | 1247 |
| 57 | CCI reversion · 1h | reversion | 85.59 | -14.41 | 128 | 43.0 | -14.31 | -1.89 | -18.41 | 416 |
| 58 | Heikin-Ashi · 1h | trend | 85.57 | -14.43 | 168 | 26.2 | -31.49 | -5.24 | -39.49 | 670 |
| 59 | EMA 9/21 cross · 1h | trend | 85.51 | -14.49 | 118 | 12.7 | -11.20 | -1.35 | -26.41 | 328 |
| 60 | Three white soldiers | momentum | 85.09 | -14.90 | 172 | 17.4 | -48.05 | -22.34 | -48.28 | 587 |
| 61 | Opening range 15m | breakout | 84.62 | -15.38 | 213 | 20.2 | -18.95 | -5.19 | -21.41 | 697 |
| 62 | Candlestick reversal · 1h | reversion | 83.25 | -16.75 | 154 | 28.6 | -32.88 | -6.32 | -32.88 | 502 |
| 63 | ROC + volume | momentum | 68.26 | -31.74 | 474 | 21.7 | -73.66 | -16.51 | -75.82 | 1680 |
| 64 | Squeeze breakout | breakout | 66.32 | -33.68 | 386 | 15.0 | -63.09 | -18.41 | -63.16 | 1219 |
| 65 | RSI(14) reversion | reversion | 66.10 | -33.90 | 488 | 26.6 | -73.87 | -17.16 | -73.92 | 1535 |
| 66 | Volume breakout | breakout | 66.07 | -33.92 | 305 | 13.8 | -62.92 | -17.80 | -63.22 | 902 |
| 67 | EMA 20/50 cross | trend | 63.29 | -36.71 | 406 | 19.5 | -77.00 | -15.12 | -77.70 | 1434 |
| 68 | Donchian 55/20 | breakout | 63.09 | -36.91 | 397 | 16.6 | -69.26 | -14.61 | -70.95 | 1278 |
| 69 | VWAP reversion | reversion | 60.50 | -39.50 | 508 | 25.0 | -72.83 | -15.33 | -72.88 | 1412 |
| 70 | AI bee: Boozy | ai | 57.96 | -42.04 | 272 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 56.67 | -43.33 | 562 | 19.2 | -85.97 | -20.46 | -86.00 | 1896 |
| 72 | Keltner breakout | breakout | 56.32 | -43.68 | 548 | 14.1 | -83.39 | -26.89 | -83.53 | 1850 |
| 73 | Ichimoku | trend | 54.17 | -45.83 | 484 | 9.7 | -82.16 | -22.95 | -82.21 | 1716 |
| 74 | AI bee: Bizzy | ai | 52.31 | -47.69 | 975 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 51.71 | -48.29 | 695 | 20.0 | -87.86 | -27.53 | -87.86 | 2113 |
| 76 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.53 | -29.06 | -98.53 | 5332 |
| 77 | Z-score reversion | reversion | 50.50 | -49.50 | 658 | 22.2 | -86.16 | -22.15 | -86.16 | 2115 |
| 78 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -30.18 | -93.59 | 2605 |
| 79 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.57 | -25.07 | -90.57 | 2359 |
| 80 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.71 | -26.83 | -91.71 | 2350 |
| 81 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -32.50 | -97.37 | 3507 |
| 82 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -35.85 | -96.57 | 3580 |
| 83 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.61 | -26.09 | -94.63 | 2640 |
| 84 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -35.96 | -99.39 | 5702 |
| 85 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.97 | -25.68 | -91.05 | 2628 |
| 86 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -31.14 | -96.36 | 3580 |
| 87 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.16 | -99.73 | 6147 |
| 88 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.61 | -29.42 | -91.64 | 2350 |
| 89 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -37.43 | -97.43 | 3657 |
| 90 | ADX DI cross | trend | 50.02 | -49.98 | 664 | 10.2 | -89.24 | -33.99 | -89.28 | 2100 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -36.06 | -98.52 | 4673 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.41 | -32.51 | -93.46 | 2792 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.13 | -99.55 | 6136 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -32.55 | -96.03 | 3752 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.84 | -95.77 | 4062 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.62 | -99.89 | 8197 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T15:55 | RSI(14) reversion | buy | SOXL | 3.15 | — | entry signal |
| 2026-10-14T15:55 | RSI(14) reversion | buy | QQQ | 3.15 | — | entry signal |
| 2026-10-14T15:55 | RSI(14) reversion | buy | NVDA | 3.15 | — | entry signal |
| 2026-10-14T15:55 | ADX DI cross | sell | SOL-USD | 12.46 | -0.10 | exit signal |
| 2026-10-14T15:50 | MFI reversion | buy | TECL | 3.70 | — | entry signal |
| 2026-10-14T15:50 | VWAP reversion | buy | MSTR | 4.03 | — | entry signal |
| 2026-10-14T15:50 | VWAP reversion | buy | AMD | 4.03 | — | entry signal |
| 2026-10-14T15:50 | RSI(14) reversion | buy | AMD | 4.73 | — | entry signal |
| 2026-10-14T15:50 | Ichimoku | sell | AAPL | 13.52 | 0.02 | exit signal |
| 2026-10-14T15:49 | AI bee: Bizzy | sell | SQQQ | 7.47 | -0.01 | Jev: sell (sell p=0.60) after 10 min |
| 2026-10-14T15:45 | Donchian 20/10 · 1h | buy | GOOGL | 4.34 | — | rebalance up |
| 2026-10-14T15:45 | Z-score reversion | sell | TNA | 3.35 | -0.04 | stop-loss |
| 2026-10-14T15:45 | Z-score reversion | sell | IWM | 3.39 | -0.01 | stop-loss |
| 2026-10-14T15:45 | Z-score reversion | sell | AMD | 3.36 | -0.04 | stop-loss |
| 2026-10-14T15:45 | RSI(14) reversion | buy | ETHU | 3.53 | — | rebalance up |
| 2026-10-14T15:45 | RSI(14) reversion | sell | SPY | 2.70 | -0.01 | stop-loss |
| 2026-10-14T15:45 | Three white soldiers | sell | AMZN | 21.22 | -0.07 | exit signal |
| 2026-10-14T15:45 | ADX DI cross | sell | DOGE-USD | 12.46 | -0.10 | exit signal |
| 2026-10-14T15:43 | AI bee: Bizzy | sell | LABU | 7.53 | -0.06 | Jev: sell (sell p=0.90) after 11 min |
| 2026-10-14T15:40 | MFI reversion | buy | SOL-USD | 3.99 | — | entry |
| 2026-10-14T15:40 | MFI reversion | buy | ETHU | 2.86 | — | rebalance up |
| 2026-10-14T15:40 | MFI reversion | sell | SPY | 4.71 | 0.00 | stop-loss |
| 2026-10-14T15:40 | MFI reversion | sell | NVDA | 3.04 | -0.02 | stop-loss |
| 2026-10-14T15:40 | MFI reversion | sell | IWM | 4.71 | -0.02 | stop-loss |
| 2026-10-14T15:40 | VWAP reversion | sell | TECL | 4.28 | -0.06 | stop-loss |
| 2026-10-14T15:40 | VWAP reversion | sell | META | 4.33 | -0.03 | stop-loss |
| 2026-10-14T15:40 | Z-score reversion | buy | XRP-USD | 3.17 | — | entry |
| 2026-10-14T15:40 | Z-score reversion | buy | PLTR | 3.17 | — | entry |
| 2026-10-14T15:40 | Z-score reversion | sell | UPRO | 1.83 | -0.00 | stop-loss |
| 2026-10-14T15:40 | Z-score reversion | sell | NVDA | 2.80 | -0.01 | stop-loss |
| 2026-10-14T15:40 | Z-score reversion | sell | META | 3.37 | -0.03 | stop-loss |
| 2026-10-14T15:40 | RSI(14) reversion | sell | UPRO | 3.47 | -0.01 | stop-loss |
| 2026-10-14T15:40 | RSI(14) reversion | sell | NVDA | 3.46 | -0.02 | stop-loss |
| 2026-10-14T15:40 | RSI(14) reversion | sell | META | 1.64 | -0.01 | stop-loss |
| 2026-10-14T15:39 | AI bee: Bizzy | buy | SQQQ | 7.48 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T15:39 | AI bee: Bizzy | sell | COIN | 7.40 | -0.03 | Jev: sell (sell p=0.85) after 11 min |
| 2026-10-14T15:35 | Agent (ML meta-label) | buy | MSTR | 6.36 | — | entry |
| 2026-10-14T15:35 | Agent (ML meta-label) | buy | AAPL | 8.97 | — | entry |
| 2026-10-14T15:35 | VWAP reversion | buy | NVDA | 4.33 | — | entry signal |
| 2026-10-14T15:35 | VWAP reversion | sell | MSFT | 4.34 | -0.01 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 15:57:05.000132+00:00 -> 2026-10-14 16:07:05.000132+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
