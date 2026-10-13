# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T10:25:05.000153+00:00 · 21225 ticks

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

Today: 7560 decisions in 1512 calls, $0.1058 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T10:25 | 0 / 2 / 3 | XRP-USD 14%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T10:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T10:25 | 1 / 3 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.70 | 2.70 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 101.99 | 1.99 | 16 | 50.0 | -15.07 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.14 | -2.72 | -13.79 | 119 |
| 6 | Hold SPY | benchmark | 101.21 | 1.21 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.00 | 1.00 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.44 | 0.44 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.41 | 0.41 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.91 | -0.09 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.74 | -0.26 | 0 | — | 29.68 | 3.45 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.15 | -0.85 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.08 | -1.92 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.93 | -2.07 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.80 | -2.20 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.67 | -2.33 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.20 | -2.80 | 105 | 52.4 | -10.83 | -2.01 | -13.91 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.82 | -3.18 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Three white soldiers · 1h | momentum | 96.80 | -3.20 | 9 | 0.0 | -3.69 | -2.83 | -4.84 | 29 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Z-score reversion · 1h | reversion | 96.46 | -3.54 | 47 | 44.7 | 3.30 | 0.78 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.21 | -3.79 | 63 | 19.0 | -6.31 | -1.01 | -13.79 | 255 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.70 | -3.09 | -8.87 | 319 |
| 30 | MACD cross · 1h | trend | 95.52 | -4.48 | 125 | 24.0 | -10.06 | -1.55 | -17.79 | 459 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 32 | Parabolic SAR · 1h | trend | 95.19 | -4.81 | 86 | 22.1 | 2.15 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.14 | -4.86 | 45 | 15.6 | 5.04 | 0.76 | -23.73 | 136 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 58 | 13.8 | 0.50 | 0.26 | -18.92 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.41 | -6.59 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.25 | -6.75 | 151 | 32.5 | -7.39 | -1.10 | -16.91 | 131 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.42 | -7.58 | 66 | 15.2 | -0.70 | 0.12 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.33 | -7.67 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.31 | -7.69 | 439 | 17.8 | 0.00 | 0.14 | -13.16 | 400 |
| 42 | Volume breakout · 1h | breakout | 91.58 | -8.42 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.40 | -8.60 | 36 | 30.6 | 1.61 | 0.47 | -9.40 | 132 |
| 44 | Ichimoku · 1h | trend | 90.83 | -9.17 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.73 | -9.27 | 93 | 37.6 | -23.66 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.72 | -9.28 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.53 | -9.47 | 71 | 15.5 | -6.85 | -0.58 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.98 | -11.02 | 141 | 46.1 | -25.36 | -4.12 | -28.82 | 508 |
| 50 | CCI reversion · 1h | reversion | 88.80 | -11.20 | 114 | 45.6 | -9.97 | -1.31 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.53 | -11.47 | 150 | 18.7 | -12.46 | -1.18 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.06 | -11.94 | 311 | 23.2 | -32.75 | -4.85 | -40.18 | 1254 |
| 53 | Max aggression: 5-day momentum | meta | 87.92 | -12.09 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.87 | -12.13 | 130 | 30.8 | -27.97 | -5.33 | -28.06 | 492 |
| 55 | Donchian 20/10 · 1h | breakout | 87.53 | -12.47 | 63 | 17.5 | -0.67 | 0.12 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.32 | -12.68 | 67 | 17.9 | -20.18 | -3.72 | -21.59 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 87.03 | -12.97 | 158 | 27.2 | -30.39 | -5.03 | -38.02 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.85 | -13.15 | 108 | 13.0 | -7.56 | -0.77 | -23.12 | 331 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.47 | -13.53 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.13 | -23.09 | -48.13 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.35 | -14.65 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.72 | 1659 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.22 | -18.02 | -62.22 | 1221 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.63 | -17.54 | -61.63 | 892 |
| 66 | RSI(14) reversion | reversion | 68.14 | -31.86 | 432 | 26.9 | -74.24 | -17.45 | -74.25 | 1492 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 362 | 20.4 | -76.02 | -14.80 | -76.17 | 1427 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.07 | -15.51 | -73.10 | 1417 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.97 | -26.13 | -83.16 | 1834 |
| 71 | Supertrend | trend | 60.55 | -39.45 | 510 | 20.0 | -85.67 | -20.21 | -85.91 | 1888 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.11 | -22.69 | -82.11 | 1728 |
| 74 | MFI reversion | reversion | 54.78 | -45.22 | 631 | 20.0 | -87.95 | -27.37 | -88.04 | 2114 |
| 75 | AI bee: Bizzy | ai | 54.50 | -45.50 | 910 | 8.2 | — | — | — | — |
| 76 | Z-score reversion | reversion | 53.90 | -46.10 | 580 | 22.1 | -86.20 | -22.47 | -86.20 | 2080 |
| 77 | ADX DI cross | trend | 53.59 | -46.41 | 610 | 10.7 | -88.96 | -33.05 | -89.06 | 2106 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.65 | -25.09 | -90.76 | 2640 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.22 | -28.58 | -91.32 | 2338 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.96 | -98.53 | 5285 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.35 | -90.34 | 2354 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.32 | -26.46 | -91.32 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.38 | -97.29 | 3506 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -34.54 | -96.30 | 3574 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.27 | -25.22 | -94.27 | 2628 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.20 | -99.37 | 5638 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -31.41 | -96.39 | 3610 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.71 | -40.16 | -99.71 | 6132 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.25 | -36.71 | -97.25 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -36.18 | -98.53 | 4667 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.28 | -31.95 | -93.28 | 2789 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -39.29 | -99.54 | 6112 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.08 | -32.82 | -96.08 | 3734 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.76 | -33.98 | -95.76 | 4047 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.75 | -99.88 | 8199 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T10:23 | AI bee: Bizzy | buy | XRP-USD | 7.57 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T10:20 | Z-score reversion | buy | XRP-USD | 2.71 | — | rebalance up |
| 2026-10-13T10:20 | Z-score reversion | buy | DOGE-USD | 2.70 | — | rebalance up |
| 2026-10-13T10:20 | Z-score reversion | sell | SOL-USD | 10.74 | -0.13 | stop-loss |
| 2026-10-13T10:15 | EMA 20/50 cross | sell | BTC-USD | 16.87 | -0.00 | exit signal |
| 2026-10-13T10:07 | Z-score reversion | buy | XRP-USD | 2.69 | — | rebalance up |
| 2026-10-13T10:07 | Z-score reversion | sell | SOL-USD | 2.69 | -0.03 | rebalance down |
| 2026-10-13T10:05 | Z-score reversion | buy | XRP-USD | 8.11 | — | entry signal |
| 2026-10-13T10:05 | Z-score reversion | buy | DOGE-USD | 10.81 | — | entry signal |
| 2026-10-13T10:05 | Z-score reversion | sell | ETH-USD | 2.72 | -0.02 | rebalance down |
| 2026-10-13T10:05 | Z-score reversion | sell | BTC-USD | 2.81 | -0.02 | rebalance down |
| 2026-10-13T10:00 | Heikin-Ashi · 1h | sell | XRP-USD | 21.57 | -0.32 | exit signal |
| 2026-10-13T10:00 | Heikin-Ashi · 1h | sell | BTC-USD | 17.48 | -0.06 | exit signal |
| 2026-10-13T09:55 | Z-score reversion | sell | XRP-USD | 13.39 | -0.14 | stop-loss |
| 2026-10-13T09:50 | AI bee: Bizzy | sell | SOL-USD | 7.82 | -0.09 | Jev: sell (sell p=0.89) after 10 min |
| 2026-10-13T09:50 | MFI reversion | sell | SOL-USD | 13.63 | -0.18 | stop-loss |
| 2026-10-13T09:50 | RSI(14) reversion | sell | SOL-USD | 16.96 | -0.22 | stop-loss |
| 2026-10-13T09:40 | AI bee: Bizzy | buy | SOL-USD | 7.91 | — | Jev: buy (buy p=0.58) |
| 2026-10-13T09:40 | Z-score reversion | buy | XRP-USD | 13.54 | — | entry signal |
| 2026-10-13T09:40 | Z-score reversion | buy | SOL-USD | 13.59 | — | entry signal |
| 2026-10-13T09:40 | Z-score reversion | buy | ETH-USD | 13.59 | — | entry signal |
| 2026-10-13T09:40 | RSI(14) reversion | buy | DOGE-USD | 17.10 | — | entry signal |
| 2026-10-13T09:30 | MFI reversion | sell | XRP-USD | 13.66 | -0.16 | stop-loss |
| 2026-10-13T09:30 | Z-score reversion | sell | XRP-USD | 13.52 | -0.15 | stop-loss |
| 2026-10-13T09:30 | EMA 20/50 cross | sell | XRP-USD | 16.83 | -0.08 | exit signal |
| 2026-10-13T09:30 | EMA 20/50 cross | sell | ETH-USD | 13.50 | 0.04 | exit signal |
| 2026-10-13T09:25 | MFI reversion | sell | DOGE-USD | 13.67 | -0.15 | stop-loss |
| 2026-10-13T09:25 | Z-score reversion | sell | DOGE-USD | 13.53 | -0.14 | stop-loss |
| 2026-10-13T09:25 | RSI(14) reversion | sell | DOGE-USD | 17.00 | -0.18 | stop-loss |
| 2026-10-13T09:20 | EMA 20/50 cross | buy | XRP-USD | 3.42 | — | rebalance up |
| 2026-10-13T09:20 | EMA 20/50 cross | buy | BTC-USD | 3.39 | — | rebalance up |
| 2026-10-13T09:20 | EMA 20/50 cross | sell | SOL-USD | 10.15 | 0.02 | exit signal |
| 2026-10-13T09:20 | EMA 20/50 cross | sell | DOGE-USD | 13.50 | 0.04 | exit signal |
| 2026-10-13T09:10 | MFI reversion | buy | XRP-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | MFI reversion | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | MFI reversion | buy | DOGE-USD | 13.81 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | XRP-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | DOGE-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | Z-score reversion | buy | BTC-USD | 13.67 | — | entry signal |
| 2026-10-13T09:10 | RSI(14) reversion | buy | SOL-USD | 17.18 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 10:25:05.000153+00:00 -> 2026-10-13 10:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
