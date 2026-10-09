# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T18:59:05.000151+00:00 · 17025 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-09 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 30570 decisions in 2649 calls, $0.3798 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T18:59 | 2 / 21 / 7 | LABU 14%, PLTR 15% |  |
| Breezy | 2026-10-09T18:59 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-09T18:59 | 0 / 28 / 2 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -7.16 | -2.15 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.62 | 2.62 | 0 | — | -4.03 | -0.64 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.29 | 2.29 | 0 | — | -3.52 | -1.43 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 101.81 | 1.81 | 14 | 57.1 | -12.26 | -1.96 | -21.08 | 72 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.33 | 1.33 | 0 | — | 1.83 | 0.89 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.33 | 1.33 | 0 | — | 0.53 | 0.36 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Max aggression: 1-day momentum | meta | 101.00 | 1.00 | 10 | 30.0 | -14.48 | -0.46 | -37.31 | 43 |
| 11 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.41 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 9 | 22.2 | 3.33 | 1.06 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.48 | -0.52 | 35 | 37.1 | 4.99 | 2.35 | -1.52 | 90 |
| 17 | Stochastic reversion · 1h | reversion | 99.42 | -0.58 | 88 | 55.7 | -10.65 | -2.05 | -14.99 | 342 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 19 | Donchian 55/20 · 1h | breakout | 99.13 | -0.87 | 27 | 14.8 | 13.10 | 1.64 | -16.96 | 109 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 98.95 | -1.05 | 0 | — | 1.98 | 0.83 | -5.18 | 1 |
| 21 | Copy: Cathie Wood (ARKK) | copy | 98.90 | -1.10 | 0 | — | 11.86 | 1.92 | -8.33 | 1 |
| 22 | Hold BTC | benchmark | 98.60 | -1.40 | 0 | — | 26.42 | 3.18 | -8.68 | 1 |
| 23 | Daily: Bullish score | daily | 97.96 | -2.04 | 4 | 0.0 | 0.93 | 0.32 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.51 | -2.50 | 6 | 0.0 | -3.11 | -2.40 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.33 | -2.67 | 38 | 42.1 | 0.43 | 0.21 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.25 | -2.75 | 78 | 23.1 | -22.56 | -6.32 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.89 | -3.11 | 38 | 13.2 | 4.59 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.69 | -3.31 | 79 | 29.1 | 2.63 | 0.73 | -8.65 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.49 | -3.51 | 57 | 21.1 | -1.81 | -0.12 | -13.84 | 255 |
| 31 | Parabolic SAR · 1h | trend | 96.41 | -3.59 | 82 | 22.0 | -2.74 | -0.19 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.93 | -4.07 | 107 | 22.4 | -16.68 | -2.71 | -18.37 | 473 |
| 34 | Supertrend · 1h | trend | 95.02 | -4.98 | 52 | 13.5 | -0.29 | 0.15 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.24 | -5.76 | 35 | 25.7 | 24.21 | 3.29 | -8.62 | 105 |
| 36 | Gap and go | momentum | 93.97 | -6.03 | 56 | 10.7 | 7.79 | 2.00 | -6.64 | 200 |
| 37 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 38 | MFI reversion · 1h | reversion | 93.65 | -6.35 | 114 | 35.1 | -13.00 | -2.18 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.41 | -6.59 | 26 | 26.9 | -2.23 | -0.38 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.14 | -6.86 | 112 | 43.8 | -18.18 | -6.02 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 42 | Agent (ML meta-label) | meta | 93.02 | -6.98 | 392 | 18.4 | -2.06 | -0.22 | -14.15 | 426 |
| 43 | Bollinger reversion · 1h | reversion | 92.97 | -7.03 | 73 | 37.0 | -20.73 | -4.93 | -23.75 | 318 |
| 44 | RSI momentum · 1h | momentum | 92.72 | -7.28 | 63 | 15.9 | 3.75 | 0.66 | -17.07 | 220 |
| 45 | Volume breakout · 1h | breakout | 92.56 | -7.44 | 51 | 15.7 | 7.94 | 1.24 | -12.60 | 123 |
| 46 | Bollinger breakout · 1h | breakout | 91.89 | -8.11 | 67 | 29.9 | 5.84 | 0.92 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.73 | -8.27 | 116 | 48.3 | -25.12 | -4.32 | -27.32 | 512 |
| 48 | Opening range 30m | breakout | 91.15 | -8.85 | 136 | 19.9 | -16.68 | -5.04 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.87 | -9.13 | 69 | 15.9 | -8.49 | -0.84 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.38 | -9.62 | 109 | 31.2 | -28.53 | -5.59 | -30.43 | 522 |
| 51 | VWAP momentum · 1h | momentum | 89.90 | -10.10 | 274 | 22.3 | -35.36 | -5.35 | -39.46 | 1275 |
| 52 | CCI reversion · 1h | reversion | 89.86 | -10.14 | 94 | 42.6 | -9.14 | -1.19 | -14.35 | 418 |
| 53 | MACD zero-line · 1h | trend | 89.50 | -10.50 | 59 | 20.3 | -6.52 | -0.70 | -19.40 | 238 |
| 54 | Opening range 15m | breakout | 89.29 | -10.71 | 159 | 18.2 | -18.27 | -5.17 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.04 | -10.96 | 127 | 18.9 | -47.92 | -23.37 | -48.05 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.99 | -11.01 | 57 | 19.3 | -0.72 | 0.12 | -17.72 | 222 |
| 57 | Heikin-Ashi · 1h | trend | 88.80 | -11.20 | 137 | 24.8 | -31.62 | -5.33 | -36.59 | 702 |
| 58 | OBV trend · 1h | momentum | 88.75 | -11.25 | 145 | 18.6 | -12.56 | -1.43 | -28.83 | 320 |
| 59 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 101 | 13.9 | -9.87 | -1.14 | -21.49 | 337 |
| 60 | Max aggression: 5-day momentum | meta | 87.38 | -12.62 | 7 | 28.6 | -14.89 | -1.11 | -34.64 | 28 |
| 61 | Keltner breakout · 1h | breakout | 86.92 | -13.08 | 43 | 18.6 | -11.84 | -1.37 | -25.35 | 216 |
| 62 | ROC + volume · 1h | momentum | 86.64 | -13.36 | 130 | 21.5 | -9.86 | -1.19 | -23.20 | 414 |
| 63 | RSI(14) reversion | reversion | 75.68 | -24.32 | 346 | 28.9 | -73.21 | -18.49 | -73.42 | 1504 |
| 64 | ROC + volume | momentum | 75.00 | -25.00 | 384 | 22.7 | -73.53 | -17.20 | -74.36 | 1670 |
| 65 | Squeeze breakout | breakout | 74.06 | -25.94 | 289 | 15.2 | -61.50 | -18.11 | -61.67 | 1216 |
| 66 | Donchian 55/20 | breakout | 72.81 | -27.19 | 298 | 17.1 | -67.94 | -14.45 | -68.48 | 1296 |
| 67 | EMA 20/50 cross | trend | 72.11 | -27.89 | 297 | 19.2 | -77.50 | -15.49 | -77.69 | 1462 |
| 68 | Volume breakout | breakout | 71.57 | -28.43 | 242 | 13.6 | -63.57 | -18.38 | -63.70 | 908 |
| 69 | VWAP reversion | reversion | 68.73 | -31.27 | 386 | 26.2 | -72.05 | -16.38 | -72.45 | 1454 |
| 70 | Supertrend | trend | 66.29 | -33.71 | 430 | 20.2 | -86.67 | -21.45 | -86.70 | 1930 |
| 71 | Keltner breakout | breakout | 65.58 | -34.42 | 412 | 14.6 | -84.16 | -27.79 | -84.47 | 1858 |
| 72 | Ichimoku | trend | 62.48 | -37.52 | 375 | 9.3 | -81.74 | -23.46 | -81.87 | 1749 |
| 73 | AI bee: Bizzy | ai | 62.35 | -37.65 | 748 | 9.8 | — | — | — | — |
| 74 | MFI reversion | reversion | 61.83 | -38.17 | 474 | 22.4 | -87.91 | -28.76 | -87.96 | 2131 |
| 75 | Z-score reversion | reversion | 61.79 | -38.21 | 472 | 23.9 | -85.95 | -23.74 | -85.99 | 2106 |
| 76 | AI bee: Boozy | ai | 61.70 | -38.30 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.43 | -40.57 | 577 | 18.7 | -90.84 | -26.23 | -90.96 | 2664 |
| 78 | Trend pullback | trend | 59.26 | -40.74 | 528 | 15.9 | -90.43 | -27.20 | -90.55 | 2301 |
| 79 | ADX DI cross | trend | 58.85 | -41.15 | 512 | 10.2 | -89.78 | -35.14 | -89.79 | 2142 |
| 80 | RSI momentum | momentum | 58.45 | -41.55 | 542 | 17.3 | -90.24 | -25.59 | -90.35 | 2375 |
| 81 | MACD zero-line | trend | 57.86 | -42.14 | 536 | 15.7 | -91.51 | -29.89 | -91.52 | 2359 |
| 82 | Triple EMA stack | trend | 57.11 | -42.89 | 567 | 15.7 | -93.12 | -30.46 | -93.14 | 2609 |
| 83 | Bollinger breakout | breakout | 54.77 | -45.23 | 603 | 14.9 | -93.54 | -33.31 | -93.55 | 2817 |
| 84 | Consensus | meta | 52.99 | -47.01 | 576 | 10.1 | -94.29 | -26.01 | -94.30 | 2683 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.84 | -98.73 | 5395 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.36 | -97.36 | 3540 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -36.59 | -96.40 | 3584 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.41 | -99.36 | 5699 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.25 | -96.29 | 3600 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.71 | -99.73 | 6192 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.62 | -97.32 | 3673 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.58 | -98.50 | 4724 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.12 | -99.53 | 6160 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -34.33 | -95.94 | 3754 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -35.18 | -95.68 | 4095 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.30 | -99.90 | 8325 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T18:58 | AI bee: Bizzy | sell | MSFT | 8.75 | -0.01 | Jev: sell (sell p=0.51) after 14 min |
| 2026-10-09T18:58 | AI bee: Bizzy | sell | COIN | 9.50 | -0.03 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-09T18:55 | AI bee: Bizzy | buy | LABU | 8.74 | — | Jev: buy (buy p=0.56) |
| 2026-10-09T18:55 | Consensus | buy | TECL | 1.63 | — | entry |
| 2026-10-09T18:55 | Volume breakout | buy | PLTR | 17.89 | — | entry signal |
| 2026-10-09T18:55 | ROC + volume | buy | PLTR | 18.75 | — | entry signal |
| 2026-10-09T18:55 | ADX DI cross | buy | ETH-USD | 14.69 | — | entry signal |
| 2026-10-09T18:52 | AI bee: Bizzy | sell | AAPL | 9.53 | 0.01 | Jev: sell (sell p=0.54) after 12 min |
| 2026-10-09T18:50 | MFI reversion | buy | NVDA | 10.28 | — | entry signal |
| 2026-10-09T18:50 | MFI reversion | buy | META | 10.30 | — | entry signal |
| 2026-10-09T18:50 | MFI reversion | sell | SOL-USD | 5.13 | -0.04 | rebalance down |
| 2026-10-09T18:50 | MFI reversion | sell | QQQ | 5.15 | -0.00 | rebalance down |
| 2026-10-09T18:50 | MFI reversion | sell | LABU | 5.14 | 0.00 | rebalance down |
| 2026-10-09T18:50 | MFI reversion | sell | GOOGL | 5.16 | -0.01 | rebalance down |
| 2026-10-09T18:50 | Trend pullback | buy | COIN | 4.93 | — | entry signal |
| 2026-10-09T18:50 | Ichimoku | buy | TSLA | 5.47 | — | rebalance up |
| 2026-10-09T18:50 | Ichimoku | buy | MSFT | 8.93 | — | entry signal |
| 2026-10-09T18:50 | Ichimoku | sell | TQQQ | 3.59 | 0.01 | rebalance down |
| 2026-10-09T18:50 | Ichimoku | sell | TECL | 3.64 | 0.02 | rebalance down |
| 2026-10-09T18:50 | Ichimoku | sell | QQQ | 3.56 | -0.00 | rebalance down |
| 2026-10-09T18:50 | Ichimoku | sell | PLTR | 3.60 | 0.05 | rebalance down |
| 2026-10-09T18:50 | ADX DI cross | buy | COIN | 14.73 | — | entry signal |
| 2026-10-09T18:50 | Supertrend | buy | AMZN | 6.82 | — | entry signal |
| 2026-10-09T18:50 | Supertrend | sell | TECL | 3.32 | 0.01 | rebalance down |
| 2026-10-09T18:50 | Supertrend | sell | AMD | 3.33 | 0.00 | rebalance down |
| 2026-10-09T18:49 | AI bee: Bizzy | buy | PLTR | 9.48 | — | Jev: buy (buy p=0.61) |
| 2026-10-09T18:49 | AI bee: Bizzy | sell | NANC | 9.53 | -0.02 | Jev: sell (sell p=0.89) after 81 min |
| 2026-10-09T18:48 | AI bee: Bizzy | buy | COIN | 9.52 | — | Jev: buy (buy p=0.61) |
| 2026-10-09T18:46 | MFI reversion · 1h | buy | MSTR | 23.39 | — | entry |
| 2026-10-09T18:46 | Triple EMA stack · 1h | buy | UPRO | 4.54 | — | rebalance up |
| 2026-10-09T18:46 | Triple EMA stack · 1h | sell | MSFT | 4.54 | 0.01 | rebalance down |
| 2026-10-09T18:46 | MFI reversion | buy | SOL-USD | 6.64 | — | rebalance up |
| 2026-10-09T18:46 | MFI reversion | buy | QQQ | 6.64 | — | rebalance up |
| 2026-10-09T18:46 | MFI reversion | buy | LABU | 6.61 | — | rebalance up |
| 2026-10-09T18:46 | MFI reversion | buy | GOOGL | 6.64 | — | rebalance up |
| 2026-10-09T18:46 | MFI reversion | sell | PLTR | 8.85 | 0.04 | exit signal |
| 2026-10-09T18:46 | MFI reversion | sell | MSFT | 8.85 | 0.02 | exit signal |
| 2026-10-09T18:46 | Z-score reversion | buy | SOL-USD | 7.72 | — | entry signal |
| 2026-10-09T18:46 | Z-score reversion | buy | ETHU | 7.73 | — | entry signal |
| 2026-10-09T18:46 | Z-score reversion | buy | ETH-USD | 7.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 18:59:05.000151+00:00 -> 2026-10-09 19:09:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
