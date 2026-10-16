# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T23:55:05.000118+00:00 · 25333 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 22.89 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 41729 decisions in 3550 calls, $0.5189 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T23:55 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-16T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T23:55 | 0 / 5 / 0 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.43 | -3.32 | -13.79 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.33 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -8.28 | -2.97 | -12.17 | 293 |
| 17 | Hold BTC | benchmark | 96.76 | -3.24 | 0 | — | 28.95 | 3.39 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.00 | -6.25 | -22.15 | 150 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.99 | -1.61 | -13.33 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.90 | -0.33 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.29 | -2.19 | -9.54 | 124 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.80 | -6.05 | -11.80 | 245 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.38 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.25 | 0.36 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.16 | 0.98 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.24 | -0.55 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.09 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | MACD cross · 1h | trend | 89.13 | -10.87 | 171 | 22.8 | -14.49 | -1.92 | -27.78 | 453 |
| 42 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.85 | -1.09 | -27.05 | 208 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.14 | -7.57 | -26.03 | 239 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.95 | -0.73 | -34.02 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.97 | -13.03 | 136 | 43.4 | -20.54 | -3.74 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.49 | -4.42 | -23.33 | 218 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.34 | 0.37 | -21.63 | 217 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.68 | -20.07 | -48.37 | 609 |
| 51 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -21.46 | -3.60 | -22.06 | 139 |
| 52 | Heikin-Ashi · 1h | trend | 83.84 | -16.16 | 189 | 24.3 | -31.17 | -5.14 | -40.33 | 674 |
| 53 | VWAP momentum · 1h | momentum | 83.78 | -16.22 | 387 | 21.2 | -36.04 | -5.49 | -43.85 | 1252 |
| 54 | Z-score reversion · 1h | reversion | 83.46 | -16.54 | 86 | 31.4 | -15.36 | -2.67 | -19.86 | 182 |
| 55 | Agent (ML meta-label) | meta | 83.13 | -16.87 | 610 | 19.2 | -5.32 | -0.62 | -16.35 | 379 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.91 | -1.70 | -27.02 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.69 | -0.59 | -29.70 | 318 |
| 58 | Bollinger reversion · 1h | reversion | 80.20 | -19.80 | 138 | 31.2 | -30.15 | -6.25 | -32.42 | 345 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.35 | -5.60 | -35.92 | 528 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.63 | -2.61 | -21.70 | 164 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.49 | -2.53 | -25.42 | 431 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -34.98 | -6.31 | -35.88 | 531 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.25 | -18.23 | -63.25 | 879 |
| 64 | ROC + volume | momentum | 63.23 | -36.77 | 550 | 22.0 | -75.88 | -17.70 | -77.45 | 1721 |
| 65 | Squeeze breakout | breakout | 62.99 | -37.01 | 430 | 14.7 | -62.92 | -17.95 | -64.05 | 1216 |
| 66 | RSI(14) reversion ⏸ | reversion | 62.42 | -37.58 | 646 | 25.9 | -74.55 | -16.67 | -74.63 | 1631 |
| 67 | Donchian 55/20 | breakout | 61.47 | -38.53 | 435 | 17.9 | -69.09 | -14.58 | -71.81 | 1285 |
| 68 | EMA 20/50 cross | trend | 59.87 | -40.13 | 455 | 19.3 | -77.06 | -15.22 | -79.04 | 1452 |
| 69 | VWAP reversion | reversion | 55.81 | -44.19 | 676 | 23.7 | -73.32 | -15.54 | -73.54 | 1500 |
| 70 | AI bee: Boozy | ai | 55.30 | -44.70 | 303 | 6.6 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.59 | -45.41 | 608 | 16.1 | -83.49 | -27.05 | -83.58 | 1841 |
| 72 | Ichimoku | trend | 52.02 | -47.98 | 553 | 11.8 | -81.91 | -23.05 | -82.05 | 1731 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.53 | -20.51 | -87.07 | 1918 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.68 | -98.61 | 5308 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -30.41 | -93.50 | 2603 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.44 | -24.80 | -90.49 | 2368 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.80 | -27.69 | -91.81 | 2344 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -32.77 | -97.45 | 3533 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -36.61 | -96.70 | 3619 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -26.70 | -94.50 | 2629 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -36.86 | -99.40 | 5830 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -25.98 | -91.38 | 2650 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -32.46 | -96.36 | 3569 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.55 | -99.73 | 6224 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -29.64 | -91.76 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -38.68 | -97.46 | 3658 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.92 | -98.50 | 4772 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -33.29 | -93.69 | 2811 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.86 | -99.54 | 6257 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.62 | -22.36 | -86.64 | 2160 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.98 | -27.32 | -88.01 | 2161 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.99 | -32.99 | -96.02 | 3826 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -34.25 | -89.41 | 2115 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -34.01 | -95.84 | 4157 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.99 | -99.89 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T23:30 | Squeeze breakout | sell | ETH-USD | 15.67 | -0.11 | exit signal |
| 2026-10-16T23:25 | Keltner breakout | sell | DOGE-USD | 13.55 | -0.13 | stop-loss |
| 2026-10-16T23:25 | ROC + volume | sell | DOGE-USD | 15.73 | -0.12 | exit signal |
| 2026-10-16T23:10 | VWAP reversion | buy | DOGE-USD | 13.96 | — | entry |
| 2026-10-16T23:10 | ROC + volume | sell | SOL-USD | 15.85 | 0.01 | exit signal |
| 2026-10-16T23:05 | VWAP reversion | sell | DOGE-USD | 11.20 | 0.06 | exit signal |
| 2026-10-16T23:05 | Keltner breakout | buy | DOGE-USD | 13.68 | — | entry signal |
| 2026-10-16T23:05 | Donchian 55/20 | buy | XRP-USD | 15.39 | — | entry signal |
| 2026-10-16T23:02 | AI bee: Boozy | sell | ETH-USD | 18.24 | -0.11 | Jev: buy |
| 2026-10-16T23:00 | VWAP reversion · 1h | sell | BTC-USD | 9.97 | -0.02 | exit signal |
| 2026-10-16T23:00 | VWAP momentum · 1h | buy | BTC-USD | 20.97 | — | entry signal |
| 2026-10-16T23:00 | Heikin-Ashi · 1h | buy | SOL-USD | 20.98 | — | entry signal |
| 2026-10-16T22:56 | ROC + volume | buy | DOGE-USD | 15.85 | — | entry signal |
| 2026-10-16T22:50 | EMA 20/50 cross | buy | ETH-USD | 3.05 | — | entry |
| 2026-10-16T22:50 | EMA 20/50 cross | sell | DOGE-USD | 2.99 | -0.01 | rebalance down |
| 2026-10-16T22:47 | AI bee: Boozy | buy | ETH-USD | 18.36 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T22:20 | Squeeze breakout | buy | ETH-USD | 15.77 | — | entry signal |
| 2026-10-16T22:19 | AI bee: Boozy | sell | ETH-USD | 18.36 | -0.09 | Jev: buy |
| 2026-10-16T22:10 | Donchian 55/20 | buy | DOGE-USD | 15.38 | — | entry signal |
| 2026-10-16T22:04 | AI bee: Boozy | buy | ETH-USD | 18.45 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T21:57 | Squeeze breakout | sell | DOGE-USD | 15.66 | -0.15 | exit signal |
| 2026-10-16T21:45 | EMA 20/50 cross | buy | XRP-USD | 14.95 | — | entry signal |
| 2026-10-16T21:35 | Squeeze breakout | buy | DOGE-USD | 15.81 | — | entry signal |
| 2026-10-16T21:34 | AI bee: Boozy | sell | ETH-USD | 18.45 | -0.10 | Jev: buy |
| 2026-10-16T21:30 | EMA 20/50 cross | buy | DOGE-USD | 14.97 | — | entry signal |
| 2026-10-16T21:25 | VWAP reversion | buy | XRP-USD | 2.79 | — | rebalance up |
| 2026-10-16T21:25 | VWAP reversion | buy | ETH-USD | 2.81 | — | rebalance up |
| 2026-10-16T21:25 | VWAP reversion | sell | BTC-USD | 11.11 | -0.03 | exit signal |
| 2026-10-16T21:20 | EMA 20/50 cross | buy | SOL-USD | 14.98 | — | entry signal |
| 2026-10-16T21:18 | AI bee: Boozy | buy | ETH-USD | 18.54 | — | Jev: buy (buy p=0.68) |
| 2026-10-16T21:05 | Agent (ML meta-label) | buy | ETH-USD | 6.11 | — | entry |
| 2026-10-16T21:05 | Agent (ML meta-label) | buy | BTC-USD | 9.24 | — | entry |
| 2026-10-16T20:48 | AI bee: Boozy | sell | SOL-USD | 18.54 | -0.12 | Jev: sell |
| 2026-10-16T20:32 | AI bee: Boozy | buy | SOL-USD | 18.67 | — | Jev: buy (buy p=0.67) |
| 2026-10-16T20:26 | Agent (ML meta-label) | sell | BTC-USD | 8.27 | -0.06 | selected signal exited |
| 2026-10-16T20:25 | EMA 20/50 cross | buy | BTC-USD | 14.99 | — | entry signal |
| 2026-10-16T20:15 | Agent (ML meta-label) | sell | ETH-USD | 7.08 | -0.05 | selected signal exited |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | ETH-USD | 7.13 | — | entry |
| 2026-10-16T20:05 | Agent (ML meta-label) | buy | BTC-USD | 8.33 | — | entry |
| 2026-10-16T20:05 | ROC + volume | buy | SOL-USD | 15.83 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 23:55:05.000118+00:00 -> 2026-10-17 00:05:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
