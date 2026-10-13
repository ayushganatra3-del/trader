# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T11:25:05.000142+00:00 · 21276 ticks

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

Today: 8325 decisions in 1665 calls, $0.1165 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T11:25 | 2 / 2 / 1 | DOGE-USD 15%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T11:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T11:25 | 4 / 1 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MFI reversion | AAPL | 2.02 | +0.67% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.69 | 2.69 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 101.98 | 1.98 | 16 | 50.0 | -15.08 | -2.39 | -21.97 | 73 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.81 | -2.62 | -13.79 | 116 |
| 6 | Hold SPY | benchmark | 101.20 | 1.20 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.99 | 0.99 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.43 | 0.43 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.40 | 0.40 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.90 | -0.10 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.89 | -0.11 | 0 | — | 29.44 | 3.41 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.08 | -1.92 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.92 | -2.08 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.79 | -2.21 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.66 | -2.34 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.20 | -2.80 | 105 | 52.4 | -10.82 | -2.01 | -13.91 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.81 | -3.19 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 26 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 27 | Z-score reversion · 1h | reversion | 96.47 | -3.53 | 47 | 44.7 | 3.34 | 0.79 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.22 | -3.77 | 63 | 19.0 | -5.98 | -0.95 | -13.79 | 254 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -9.75 | -3.70 | -10.90 | 299 |
| 30 | MACD cross · 1h | trend | 95.53 | -4.47 | 125 | 24.0 | -10.20 | -1.57 | -17.79 | 460 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.82 | -3.78 | -8.72 | 231 |
| 32 | Parabolic SAR · 1h | trend | 95.19 | -4.81 | 86 | 22.1 | 2.16 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.13 | -4.87 | 45 | 15.6 | 5.06 | 0.77 | -23.77 | 136 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 58 | 13.8 | 0.55 | 0.27 | -19.12 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.26 | -6.74 | 151 | 32.5 | -7.42 | -1.11 | -16.91 | 131 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.23 | -2.74 | -6.45 | 113 |
| 39 | RSI momentum · 1h | momentum | 92.41 | -7.59 | 66 | 15.2 | -0.64 | 0.13 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.32 | -7.68 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.30 | -7.70 | 439 | 17.8 | 0.75 | 0.27 | -12.49 | 396 |
| 42 | Volume breakout · 1h | breakout | 91.57 | -8.43 | 70 | 20.0 | 9.08 | 1.38 | -12.60 | 117 |
| 43 | RSI(14) reversion · 1h | reversion | 91.42 | -8.58 | 36 | 30.6 | -1.10 | -0.13 | -9.40 | 140 |
| 44 | Ichimoku · 1h | trend | 90.83 | -9.18 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.73 | -9.27 | 93 | 37.6 | -23.66 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.72 | -9.28 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.52 | -9.48 | 71 | 15.5 | -6.58 | -0.55 | -27.18 | 235 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.98 | -11.02 | 141 | 46.1 | -25.35 | -4.12 | -28.82 | 508 |
| 50 | CCI reversion · 1h | reversion | 88.81 | -11.19 | 114 | 45.6 | -9.92 | -1.31 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.52 | -11.48 | 150 | 18.7 | -12.36 | -1.17 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.06 | -11.95 | 311 | 23.2 | -32.72 | -4.85 | -40.31 | 1255 |
| 53 | Max aggression: 5-day momentum | meta | 87.91 | -12.09 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.85 | -12.15 | 130 | 30.8 | -29.56 | -5.60 | -29.66 | 499 |
| 55 | Donchian 20/10 · 1h | breakout | 87.53 | -12.47 | 63 | 17.5 | -0.65 | 0.13 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.34 | -12.65 | 67 | 17.9 | -20.11 | -3.71 | -21.66 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 87.03 | -12.97 | 158 | 27.2 | -30.40 | -5.03 | -38.03 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.84 | -13.16 | 109 | 12.8 | -7.06 | -0.71 | -23.22 | 329 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.46 | -13.54 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.04 | -22.98 | -48.12 | 585 |
| 62 | ROC + volume · 1h | momentum | 85.34 | -14.66 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.73 | 1660 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.07 | -17.94 | -62.07 | 1219 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.24 | -17.29 | -61.24 | 887 |
| 66 | RSI(14) reversion | reversion | 67.47 | -32.53 | 438 | 26.5 | -74.39 | -17.54 | -74.47 | 1496 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 362 | 20.4 | -76.02 | -14.80 | -76.17 | 1427 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.04 | -15.51 | -73.08 | 1416 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.87 | -25.92 | -83.05 | 1831 |
| 71 | Supertrend | trend | 60.37 | -39.63 | 510 | 20.0 | -85.73 | -20.29 | -85.92 | 1893 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.14 | -22.74 | -82.14 | 1729 |
| 74 | MFI reversion | reversion | 54.48 | -45.52 | 632 | 19.9 | -87.98 | -27.62 | -88.01 | 2118 |
| 75 | AI bee: Bizzy | ai | 54.42 | -45.58 | 911 | 8.2 | — | — | — | — |
| 76 | ADX DI cross | trend | 53.43 | -46.57 | 610 | 10.7 | -88.97 | -33.19 | -89.06 | 2110 |
| 77 | Z-score reversion | reversion | 53.38 | -46.62 | 586 | 21.8 | -86.24 | -22.46 | -86.30 | 2081 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.56 | -24.92 | -90.69 | 2636 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.22 | -28.58 | -91.32 | 2338 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -28.98 | -98.53 | 5289 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.35 | -90.34 | 2354 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.32 | -26.46 | -91.32 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.38 | -97.29 | 3506 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -34.57 | -96.29 | 3573 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -25.36 | -94.30 | 2632 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.54 | -99.38 | 5648 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.40 | -31.48 | -96.40 | 3611 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.56 | -99.72 | 6138 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.26 | -36.81 | -97.26 | 3650 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.46 | -98.55 | 4672 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.22 | -31.73 | -93.22 | 2785 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.62 | -99.55 | 6118 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.09 | -33.04 | -96.09 | 3737 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.82 | -34.35 | -95.84 | 4053 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.48 | -99.88 | 8189 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T11:25 | MFI reversion | buy | XRP-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | MFI reversion | buy | SOL-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | MFI reversion | buy | BTC-USD | 13.65 | — | entry signal |
| 2026-10-13T11:25 | Z-score reversion | buy | DOGE-USD | 13.36 | — | entry signal |
| 2026-10-13T11:25 | Z-score reversion | sell | BTC-USD | 13.38 | -0.02 | exit signal |
| 2026-10-13T11:25 | RSI(14) reversion | buy | SOL-USD | 16.91 | — | entry signal |
| 2026-10-13T11:25 | RSI(14) reversion | buy | DOGE-USD | 16.91 | — | entry signal |
| 2026-10-13T11:25 | RSI(14) reversion | sell | ETH-USD | 13.58 | 0.00 | take-profit |
| 2026-10-13T11:25 | RSI(14) reversion | sell | BTC-USD | 16.90 | -0.01 | take-profit |
| 2026-10-13T11:25 | ADX DI cross | buy | XRP-USD | 10.72 | — | entry signal |
| 2026-10-13T11:25 | ADX DI cross | buy | SOL-USD | 10.72 | — | entry signal |
| 2026-10-13T11:25 | ADX DI cross | buy | ETH-USD | 10.72 | — | entry signal |
| 2026-10-13T11:25 | ADX DI cross | buy | DOGE-USD | 10.72 | — | entry signal |
| 2026-10-13T11:25 | ADX DI cross | buy | BTC-USD | 10.72 | — | entry signal |
| 2026-10-13T11:25 | Supertrend | buy | SOL-USD | 15.14 | — | entry signal |
| 2026-10-13T11:25 | Supertrend | buy | ETH-USD | 15.14 | — | entry signal |
| 2026-10-13T11:25 | Supertrend | buy | DOGE-USD | 15.14 | — | entry signal |
| 2026-10-13T11:25 | Supertrend | buy | BTC-USD | 15.14 | — | entry signal |
| 2026-10-13T11:24 | AI bee: Bizzy | buy | DOGE-USD | 8.35 | — | Jev: buy (buy p=0.61) |
| 2026-10-13T11:20 | MFI reversion | sell | SOL-USD | 13.52 | -0.17 | stop-loss |
| 2026-10-13T11:20 | Z-score reversion | sell | SOL-USD | 13.24 | -0.16 | stop-loss |
| 2026-10-13T11:20 | RSI(14) reversion | sell | DOGE-USD | 16.76 | -0.20 | stop-loss |
| 2026-10-13T11:15 | RSI(14) reversion | buy | XRP-USD | 6.70 | — | rebalance up |
| 2026-10-13T11:15 | RSI(14) reversion | buy | DOGE-USD | 3.38 | — | rebalance up |
| 2026-10-13T11:15 | RSI(14) reversion | buy | BTC-USD | 3.38 | — | rebalance up |
| 2026-10-13T11:15 | RSI(14) reversion | sell | SOL-USD | 16.77 | -0.20 | stop-loss |
| 2026-10-13T11:13 | RSI(14) reversion | buy | XRP-USD | 3.37 | — | rebalance up |
| 2026-10-13T11:13 | RSI(14) reversion | sell | DOGE-USD | 3.37 | -0.03 | rebalance down |
| 2026-10-13T11:12 | RSI(14) reversion | buy | XRP-USD | 3.38 | — | rebalance up |
| 2026-10-13T11:12 | RSI(14) reversion | sell | ETH-USD | 3.38 | -0.02 | rebalance down |
| 2026-10-13T11:10 | Z-score reversion | buy | XRP-USD | 13.32 | — | entry signal |
| 2026-10-13T11:10 | RSI(14) reversion | buy | XRP-USD | 3.48 | — | entry signal |
| 2026-10-13T11:10 | RSI(14) reversion | buy | BTC-USD | 13.53 | — | entry signal |
| 2026-10-13T11:05 | Z-score reversion | sell | XRP-USD | 13.31 | -0.20 | stop-loss |
| 2026-10-13T11:00 | Three white soldiers · 1h | sell | ETH-USD | 23.93 | -0.36 | exit signal |
| 2026-10-13T11:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 2.86 | -0.05 | exit signal |
| 2026-10-13T11:00 | RSI(14) reversion | buy | SOL-USD | 16.97 | — | entry signal |
| 2026-10-13T10:55 | MFI reversion | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-13T10:55 | Z-score reversion | buy | ETH-USD | 13.38 | — | entry signal |
| 2026-10-13T10:55 | RSI(14) reversion | buy | ETH-USD | 16.98 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 11:25:05.000142+00:00 -> 2026-10-13 11:35:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
