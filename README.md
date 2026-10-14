# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T05:25:05.000124+00:00 · 22120 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.12 (-4.88%)

Closed trades 64, win rate 46.9%, fees £2.37, max drawdown -5.38%.

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

Today: 4090 decisions in 818 calls, $0.0572 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T05:25 | 3 / 2 / 0 | DOGE-USD 14%, AMD 14% |  |
| Breezy | 2026-10-14T05:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T05:25 | 5 / 0 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Three white soldiers | NVDA | 1.77 | +1.00% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.02 | 3.02 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.12 | -2.70 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.72 | 1.72 | 18 | 50.0 | -15.67 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.96 | 0.96 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.32 | 0.33 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.75 | -0.24 | 0 | — | 4.59 | 1.77 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.75 | -0.25 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.53 | -0.47 | 0 | — | 30.50 | 3.52 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.87 | -1.12 | 0 | — | -8.33 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.32 | -1.68 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.70 | -2.30 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.39 | -2.61 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.28 | -2.72 | 5 | 0.0 | 0.46 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.87 | -8.69 | 309 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.32 | -3.68 | 64 | 18.8 | -11.17 | -2.06 | -14.81 | 253 |
| 26 | Stochastic reversion · 1h | reversion | 96.17 | -3.83 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.69 | -4.31 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.49 | -4.51 | 132 | 23.5 | -9.18 | -1.19 | -19.25 | 461 |
| 29 | Z-score reversion · 1h | reversion | 95.40 | -4.60 | 52 | 44.2 | 2.86 | 0.69 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.29 | -4.71 | 45 | 15.6 | 10.36 | 1.31 | -20.35 | 136 |
| 31 | Max aggression: 1-day momentum | meta | 95.27 | -4.73 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.68 | -4.97 | -8.86 | 234 |
| 33 | Supertrend · 1h | trend | 93.94 | -6.06 | 60 | 13.3 | 2.26 | 0.48 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.92 | -6.08 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.59 | -6.41 | 90 | 22.2 | 1.76 | 0.41 | -22.77 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.45 | -0.43 | -5.63 | 112 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.56 | 2.17 | -6.74 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.54 | -7.46 | 66 | 15.2 | 1.21 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.45 | -7.55 | 165 | 31.5 | -7.87 | -1.21 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.94 | -8.06 | 127 | 42.5 | -19.96 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.44 | -8.56 | 38 | 34.2 | 6.02 | 1.38 | -9.40 | 126 |
| 42 | Ichimoku · 1h | trend | 91.22 | -8.78 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 90.98 | -9.02 | 485 | 18.1 | -5.49 | -0.91 | -14.20 | 372 |
| 44 | Triple EMA stack · 1h | trend | 90.65 | -9.35 | 71 | 15.5 | -7.23 | -0.55 | -32.27 | 239 |
| 45 | Volume breakout · 1h | breakout | 90.64 | -9.36 | 75 | 22.7 | 8.82 | 1.34 | -12.60 | 119 |
| 46 | Bollinger breakout · 1h | breakout | 90.63 | -9.37 | 77 | 28.6 | 7.25 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 89.94 | -10.06 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.34 | -10.65 | 143 | 45.5 | -28.07 | -4.76 | -29.60 | 509 |
| 49 | CCI reversion · 1h | reversion | 88.92 | -11.08 | 119 | 45.4 | -9.64 | -1.25 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.03 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.04 | -11.96 | 158 | 18.4 | -9.14 | -0.75 | -33.87 | 318 |
| 52 | MACD zero-line · 1h | trend | 87.45 | -12.55 | 69 | 17.4 | -22.12 | -4.30 | -22.65 | 230 |
| 53 | VWAP momentum · 1h | momentum | 87.41 | -12.59 | 328 | 22.9 | -33.72 | -5.01 | -40.74 | 1257 |
| 54 | Donchian 20/10 · 1h | breakout | 86.92 | -13.08 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.68 | -13.32 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.64 | -13.36 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.62 | -13.38 | 110 | 12.7 | -10.13 | -1.28 | -24.14 | 329 |
| 58 | Heikin-Ashi · 1h | trend | 86.62 | -13.38 | 165 | 26.7 | -29.59 | -4.85 | -38.32 | 678 |
| 59 | Candlestick reversal · 1h | reversion | 86.47 | -13.53 | 141 | 31.2 | -29.62 | -5.72 | -30.19 | 475 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.82 | 698 |
| 61 | Three white soldiers | momentum | 85.93 | -14.07 | 167 | 18.0 | -47.79 | -22.18 | -47.79 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.25 | -14.75 | 173 | 20.2 | -8.84 | -1.01 | -24.84 | 399 |
| 63 | ROC + volume | momentum | 70.74 | -29.27 | 458 | 22.3 | -73.12 | -16.35 | -75.20 | 1669 |
| 64 | Volume breakout | breakout | 67.41 | -32.59 | 296 | 14.2 | -61.82 | -17.28 | -62.10 | 887 |
| 65 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.75 | -16.92 | -74.13 | 1483 |
| 66 | Squeeze breakout | breakout | 67.30 | -32.70 | 381 | 15.2 | -62.37 | -17.83 | -62.58 | 1219 |
| 67 | EMA 20/50 cross | trend | 65.52 | -34.48 | 393 | 20.1 | -76.54 | -14.96 | -76.88 | 1440 |
| 68 | Donchian 55/20 | breakout | 63.83 | -36.17 | 390 | 16.9 | -69.03 | -14.44 | -70.45 | 1283 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -72.57 | -15.22 | -72.57 | 1402 |
| 70 | AI bee: Boozy | ai | 59.84 | -40.16 | 270 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 58.54 | -41.46 | 551 | 19.6 | -85.78 | -20.33 | -85.78 | 1911 |
| 72 | Keltner breakout | breakout | 58.02 | -41.98 | 535 | 14.4 | -83.14 | -26.70 | -83.14 | 1844 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.33 | -22.78 | -82.33 | 1722 |
| 74 | AI bee: Bizzy | ai | 53.25 | -46.75 | 955 | 8.5 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.92 | -47.08 | 672 | 20.2 | -87.92 | -26.88 | -87.93 | 2111 |
| 76 | Z-score reversion | reversion | 52.35 | -47.65 | 622 | 23.2 | -86.17 | -21.78 | -86.18 | 2088 |
| 77 | ADX DI cross | trend | 51.33 | -48.67 | 651 | 10.4 | -89.23 | -33.15 | -89.23 | 2113 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.46 | -28.70 | -98.46 | 5294 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -29.48 | -93.39 | 2612 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.37 | -24.54 | -90.37 | 2370 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.73 | -26.54 | -91.73 | 2360 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.35 | -31.79 | -97.35 | 3533 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -34.85 | -96.50 | 3606 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.54 | -25.34 | -94.54 | 2644 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -34.94 | -99.36 | 5637 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.89 | -25.40 | -90.89 | 2631 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -30.64 | -96.39 | 3601 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.74 | -99.72 | 6163 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.50 | -29.05 | -91.50 | 2359 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -36.36 | -97.41 | 3676 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -34.73 | -98.51 | 4676 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.36 | -31.61 | -93.36 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.62 | -99.54 | 6132 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -31.30 | -96.01 | 3746 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -32.73 | -95.69 | 4051 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.57 | -99.89 | 8215 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T05:25 | AI bee: Bizzy | buy | DOGE-USD | 7.58 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T05:10 | MFI reversion | sell | BTC-USD | 13.15 | -0.12 | stop-loss |
| 2026-10-14T05:10 | Keltner breakout | sell | DOGE-USD | 14.39 | -0.16 | target is flat |
| 2026-10-14T05:10 | Donchian 55/20 | sell | DOGE-USD | 15.83 | -0.18 | stop-loss |
| 2026-10-14T05:10 | Ichimoku | sell | SOL-USD | 13.44 | -0.13 | exit signal |
| 2026-10-14T05:10 | Ichimoku | sell | DOGE-USD | 13.46 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | XRP-USD | 11.72 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | SOL-USD | 11.71 | -0.16 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | ETH-USD | 11.73 | -0.12 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | DOGE-USD | 11.62 | -0.09 | exit signal |
| 2026-10-14T05:10 | Supertrend | sell | BTC-USD | 11.76 | -0.10 | exit signal |
| 2026-10-14T05:10 | EMA 20/50 cross | sell | ETH-USD | 16.28 | -0.16 | stop-loss |
| 2026-10-14T05:05 | Ichimoku | buy | SOL-USD | 13.57 | — | entry signal |
| 2026-10-14T05:05 | Ichimoku | buy | DOGE-USD | 13.57 | — | entry signal |
| 2026-10-14T05:05 | Ichimoku | sell | BTC-USD | 13.58 | -0.09 | exit signal |
| 2026-10-14T05:00 | Z-score reversion · 1h | sell | XRP-USD | 10.55 | 0.01 | exit signal |
| 2026-10-14T05:00 | Z-score reversion · 1h | sell | DOGE-USD | 8.06 | -0.00 | exit signal |
| 2026-10-14T05:00 | RSI(14) reversion · 1h | sell | DOGE-USD | 11.42 | 0.06 | exit signal |
| 2026-10-14T05:00 | Heikin-Ashi · 1h | buy | BTC-USD | 21.68 | — | entry signal |
| 2026-10-14T05:00 | MACD zero-line · 1h | buy | ETH-USD | 6.45 | — | entry signal |
| 2026-10-14T05:00 | MACD zero-line · 1h | sell | DOGE-USD | 6.45 | -0.02 | rebalance down |
| 2026-10-14T05:00 | MFI reversion | buy | BTC-USD | 13.27 | — | entry signal |
| 2026-10-14T05:00 | Three white soldiers | sell | SOL-USD | 21.37 | -0.14 | exit signal |
| 2026-10-14T04:58 | AI bee: Bizzy | sell | XRP-USD | 7.58 | -0.05 | Jev: sell (sell p=0.82) after 11 min |
| 2026-10-14T04:47 | AI bee: Bizzy | buy | XRP-USD | 7.64 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T04:42 | AI bee: Bizzy | sell | SOL-USD | 7.97 | -0.03 | Jev: sell (sell p=0.60) after 10 min |
| 2026-10-14T04:40 | Keltner breakout | buy | DOGE-USD | 14.55 | — | entry signal |
| 2026-10-14T04:40 | Donchian 55/20 | buy | DOGE-USD | 16.00 | — | entry signal |
| 2026-10-14T04:35 | Three white soldiers | buy | SOL-USD | 21.52 | — | entry signal |
| 2026-10-14T04:32 | AI bee: Bizzy | buy | SOL-USD | 8.00 | — | Jev: buy (buy p=0.60) |
| 2026-10-14T04:30 | MFI reversion | buy | DOGE-USD | 13.28 | — | entry signal |
| 2026-10-14T04:25 | Supertrend | buy | DOGE-USD | 11.70 | — | entry |
| 2026-10-14T04:25 | Supertrend | sell | XRP-USD | 2.95 | -0.02 | rebalance down |
| 2026-10-14T04:25 | Supertrend | sell | SOL-USD | 2.95 | -0.03 | rebalance down |
| 2026-10-14T04:20 | ADX DI cross | sell | SOL-USD | 12.76 | -0.09 | exit signal |
| 2026-10-14T04:20 | Supertrend | buy | XRP-USD | 5.89 | — | rebalance up |
| 2026-10-14T04:20 | Supertrend | buy | SOL-USD | 2.98 | — | rebalance up |
| 2026-10-14T04:20 | Supertrend | sell | DOGE-USD | 14.68 | -0.14 | exit signal |
| 2026-10-14T04:16 | ADX DI cross | buy | SOL-USD | 12.85 | — | entry signal |
| 2026-10-14T04:05 | Squeeze breakout | sell | SOL-USD | 16.81 | -0.14 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 05:25:05.000124+00:00 -> 2026-10-14 05:35:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
