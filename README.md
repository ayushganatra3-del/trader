# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T08:25:05.000177+00:00 · 21120 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 5985 decisions in 1197 calls, $0.0838 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T08:25 | 0 / 4 / 1 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T08:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T08:25 | 3 / 2 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | AAPL | 1.77 | +1.13% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.79 | 2.79 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.08 | 2.08 | 16 | 50.0 | -15.07 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | Hold SPY | benchmark | 101.30 | 1.30 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.09 | 1.09 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.53 | 0.53 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.50 | 0.50 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Hold BTC | benchmark | 100.35 | 0.35 | 0 | — | 30.80 | 3.55 | -8.68 | 1 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 100.00 | 0.00 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 14 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 15 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.24 | -0.76 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.15 | -1.85 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.02 | -1.98 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.89 | -2.11 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.76 | -2.24 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.32 | -2.68 | 8 | 0.0 | -3.22 | -2.46 | -4.64 | 29 |
| 24 | Stochastic reversion · 1h | reversion | 97.26 | -2.74 | 105 | 52.4 | -10.83 | -2.01 | -13.91 | 341 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.91 | -3.09 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.68 | -3.32 | 47 | 44.7 | 3.71 | 0.86 | -8.60 | 165 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.43 | -3.57 | 62 | 19.4 | -5.92 | -0.94 | -13.79 | 254 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -8.05 | -3.38 | -9.43 | 322 |
| 30 | MACD cross · 1h | trend | 95.86 | -4.14 | 125 | 24.0 | -10.65 | -1.65 | -17.79 | 463 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 32 | Parabolic SAR · 1h | trend | 95.26 | -4.74 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 33 | EMA 20/50 cross · 1h | trend | 95.23 | -4.77 | 45 | 15.6 | 4.90 | 0.75 | -23.71 | 136 |
| 34 | Supertrend · 1h | trend | 94.44 | -5.56 | 58 | 13.8 | 0.79 | 0.30 | -18.92 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.45 | -6.55 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.34 | -6.66 | 151 | 32.5 | -6.89 | -1.01 | -16.91 | 131 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.50 | -7.50 | 66 | 15.2 | -0.65 | 0.13 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.41 | -7.59 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.39 | -7.61 | 439 | 17.8 | 1.09 | 0.33 | -13.18 | 400 |
| 42 | RSI(14) reversion · 1h | reversion | 91.68 | -8.32 | 36 | 30.6 | 2.18 | 0.60 | -9.40 | 130 |
| 43 | Volume breakout · 1h | breakout | 91.64 | -8.36 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 44 | Ichimoku · 1h | trend | 90.91 | -9.09 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.78 | -9.21 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 46 | Bollinger reversion · 1h | reversion | 90.78 | -9.22 | 93 | 37.6 | -23.67 | -5.71 | -24.41 | 319 |
| 47 | Triple EMA stack · 1h | trend | 90.61 | -9.39 | 71 | 15.5 | -6.99 | -0.60 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 89.02 | -10.98 | 141 | 46.1 | -25.27 | -4.10 | -28.82 | 509 |
| 50 | CCI reversion · 1h | reversion | 88.92 | -11.08 | 114 | 45.6 | -9.58 | -1.25 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.61 | -11.39 | 150 | 18.7 | -12.55 | -1.19 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.14 | -11.86 | 311 | 23.2 | -32.35 | -4.77 | -40.18 | 1254 |
| 53 | Heikin-Ashi · 1h | trend | 88.09 | -11.91 | 153 | 28.1 | -29.64 | -4.87 | -37.81 | 680 |
| 54 | Candlestick reversal · 1h | reversion | 88.07 | -11.93 | 130 | 30.8 | -26.86 | -5.10 | -27.05 | 485 |
| 55 | Max aggression: 5-day momentum | meta | 87.99 | -12.01 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 56 | Donchian 20/10 · 1h | breakout | 87.61 | -12.39 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 215 |
| 57 | MACD zero-line · 1h | trend | 87.51 | -12.49 | 67 | 17.9 | -20.29 | -3.74 | -21.54 | 230 |
| 58 | EMA 9/21 cross · 1h | trend | 87.01 | -12.98 | 108 | 13.0 | -8.51 | -0.89 | -23.06 | 335 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.55 | -13.46 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.13 | -23.09 | -48.13 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.42 | -14.57 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.52 | -16.00 | -74.72 | 1662 |
| 64 | Squeeze breakout | breakout | 69.29 | -30.71 | 355 | 15.5 | -62.19 | -17.99 | -62.20 | 1221 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.63 | -17.54 | -61.63 | 892 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.80 | -17.21 | -73.98 | 1484 |
| 67 | EMA 20/50 cross | trend | 68.32 | -31.68 | 357 | 19.9 | -75.74 | -14.57 | -76.17 | 1428 |
| 68 | Donchian 55/20 | breakout | 67.07 | -32.93 | 360 | 17.5 | -67.75 | -13.98 | -69.18 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.95 | -15.49 | -72.98 | 1414 |
| 70 | Supertrend | trend | 61.14 | -38.86 | 505 | 19.6 | -85.58 | -19.96 | -85.95 | 1889 |
| 71 | Keltner breakout | breakout | 60.69 | -39.31 | 491 | 15.5 | -82.97 | -26.11 | -83.17 | 1835 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.78 | -43.22 | 437 | 9.8 | -82.04 | -22.59 | -82.05 | 1728 |
| 74 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -87.84 | -26.97 | -88.04 | 2111 |
| 75 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.23 | -22.36 | -86.42 | 2078 |
| 76 | AI bee: Bizzy | ai | 54.61 | -45.39 | 909 | 8.3 | — | — | — | — |
| 77 | ADX DI cross | trend | 53.97 | -46.03 | 605 | 10.4 | -88.91 | -32.62 | -89.06 | 2107 |
| 78 | Donchian 20/10 | breakout | 52.59 | -47.41 | 688 | 18.0 | -90.57 | -24.81 | -90.76 | 2640 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.23 | -28.63 | -91.34 | 2339 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.73 | -98.54 | 5292 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -92.97 | -28.57 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.23 | -90.41 | 2357 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.26 | -26.25 | -91.26 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.23 | -31.10 | -97.30 | 3507 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -34.41 | -96.33 | 3579 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.28 | -25.27 | -94.28 | 2631 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.85 | -99.37 | 5631 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -30.91 | -96.32 | 3599 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.25 | -99.72 | 6135 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.24 | -36.55 | -97.24 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.93 | -98.52 | 4663 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.26 | -31.84 | -93.26 | 2789 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.78 | -99.54 | 6105 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -32.56 | -96.04 | 3728 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.84 | -95.77 | 4044 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.78 | -99.89 | 8202 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T08:25 | Volume breakout | sell | BTC-USD | 17.10 | -0.15 | exit signal |
| 2026-10-13T08:23 | AI bee: Bizzy | sell | BTC-USD | 7.68 | -0.05 | Jev: sell (sell p=0.64) after 10 min |
| 2026-10-13T08:20 | Three white soldiers | sell | BTC-USD | 21.42 | -0.17 | stop-loss |
| 2026-10-13T08:16 | Three white soldiers | buy | BTC-USD | 21.59 | — | entry signal |
| 2026-10-13T08:16 | Volume breakout | buy | BTC-USD | 17.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | SOL-USD | 14.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | ETH-USD | 14.25 | — | entry signal |
| 2026-10-13T08:16 | Ichimoku | buy | DOGE-USD | 14.25 | — | entry signal |
| 2026-10-13T08:13 | AI bee: Bizzy | buy | BTC-USD | 7.74 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T08:01 | ADX DI cross · 1h | buy | ETH-USD | 7.98 | — | entry signal |
| 2026-10-13T08:01 | EMA 9/21 cross · 1h | buy | ETH-USD | 2.92 | — | entry signal |
| 2026-10-13T08:01 | Volume breakout | sell | BTC-USD | 17.15 | -0.14 | exit signal |
| 2026-10-13T07:52 | AI bee: Bizzy | sell | SOL-USD | 8.81 | -0.03 | Jev: sell (sell p=0.58) after 17 min |
| 2026-10-13T07:42 | Donchian 20/10 | buy | XRP-USD | 2.64 | — | rebalance up |
| 2026-10-13T07:42 | Donchian 20/10 | sell | DOGE-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-13T07:40 | Volume breakout | buy | BTC-USD | 17.28 | — | entry signal |
| 2026-10-13T07:40 | Squeeze breakout | buy | BTC-USD | 17.34 | — | entry signal |
| 2026-10-13T07:40 | Keltner breakout | buy | BTC-USD | 15.19 | — | entry signal |
| 2026-10-13T07:40 | Donchian 20/10 | buy | XRP-USD | 7.92 | — | entry signal |
| 2026-10-13T07:40 | Donchian 20/10 | buy | SOL-USD | 10.56 | — | entry signal |
| 2026-10-13T07:40 | Donchian 20/10 | buy | ETH-USD | 10.56 | — | entry signal |
| 2026-10-13T07:40 | Donchian 20/10 | sell | BTC-USD | 2.71 | 0.03 | rebalance down |
| 2026-10-13T07:40 | Supertrend | buy | SOL-USD | 9.11 | — | entry signal |
| 2026-10-13T07:40 | Supertrend | sell | XRP-USD | 3.10 | 0.04 | rebalance down |
| 2026-10-13T07:40 | Supertrend | sell | BTC-USD | 3.10 | 0.04 | rebalance down |
| 2026-10-13T07:35 | AI bee: Bizzy | buy | SOL-USD | 8.84 | — | Jev: buy (buy p=0.65) |
| 2026-10-13T07:35 | Donchian 20/10 | buy | DOGE-USD | 13.19 | — | entry |
| 2026-10-13T07:35 | ADX DI cross | buy | XRP-USD | 10.65 | — | entry signal |
| 2026-10-13T07:35 | ADX DI cross | buy | SOL-USD | 10.80 | — | entry signal |
| 2026-10-13T07:35 | ADX DI cross | sell | DOGE-USD | 2.72 | -0.01 | rebalance down |
| 2026-10-13T07:35 | Supertrend | buy | DOGE-USD | 15.30 | — | entry |
| 2026-10-13T07:30 | Donchian 20/10 | sell | DOGE-USD | 10.57 | 0.20 | exit signal |
| 2026-10-13T07:30 | ADX DI cross | sell | XRP-USD | 13.43 | -0.10 | exit signal |
| 2026-10-13T07:30 | Supertrend | sell | DOGE-USD | 12.22 | 0.23 | exit signal |
| 2026-10-13T07:25 | Donchian 20/10 | sell | ETH-USD | 10.57 | 0.21 | exit signal |
| 2026-10-13T07:25 | ADX DI cross | buy | DOGE-USD | 2.71 | — | rebalance up |
| 2026-10-13T07:25 | ADX DI cross | sell | SOL-USD | 8.01 | -0.06 | exit signal |
| 2026-10-13T07:20 | ADX DI cross | buy | SOL-USD | 8.07 | — | entry signal |
| 2026-10-13T07:20 | ADX DI cross | buy | DOGE-USD | 10.82 | — | entry signal |
| 2026-10-13T07:20 | ADX DI cross | sell | BTC-USD | 2.74 | 0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 08:25:05.000177+00:00 -> 2026-10-13 08:35:05.000177+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
