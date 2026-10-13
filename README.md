# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T10:55:05.000133+00:00 · 21254 ticks

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

Today: 7995 decisions in 1599 calls, $0.1119 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T10:55 | 1 / 1 / 3 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T10:55 | 1 / 4 / 0 | COIN 77% |  |

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
| 5 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -9.14 | -2.72 | -13.79 | 119 |
| 6 | Hold SPY | benchmark | 101.20 | 1.20 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.99 | 0.99 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 9 | Timing: Nasdaq FTD · TQQQ | daily | 100.43 | 0.43 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 100.40 | 0.40 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.90 | -0.10 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 15 | Hold BTC | benchmark | 99.48 | -0.52 | 0 | — | 29.28 | 3.41 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.14 | -0.86 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.08 | -1.92 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 97.92 | -2.08 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.79 | -2.21 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.66 | -2.34 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.20 | -2.80 | 105 | 52.4 | -10.83 | -2.01 | -13.91 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 96.81 | -3.19 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 25 | Three white soldiers · 1h | momentum | 96.68 | -3.32 | 9 | 0.0 | -3.81 | -2.91 | -4.96 | 29 |
| 26 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 27 | Z-score reversion · 1h | reversion | 96.41 | -3.59 | 47 | 44.7 | 3.18 | 0.76 | -8.60 | 165 |
| 28 | ADX DI cross · 1h | trend | 96.17 | -3.83 | 63 | 19.0 | -6.64 | -1.07 | -13.79 | 256 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.70 | -3.09 | -8.87 | 319 |
| 30 | MACD cross · 1h | trend | 95.39 | -4.61 | 125 | 24.0 | -10.18 | -1.57 | -17.79 | 459 |
| 31 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.82 | -3.78 | -8.72 | 231 |
| 32 | Parabolic SAR · 1h | trend | 95.19 | -4.81 | 86 | 22.1 | 2.16 | 0.46 | -21.52 | 288 |
| 33 | EMA 20/50 cross · 1h | trend | 95.13 | -4.87 | 45 | 15.6 | 5.01 | 0.76 | -23.76 | 136 |
| 34 | Supertrend · 1h | trend | 94.36 | -5.64 | 58 | 13.8 | 0.38 | 0.24 | -19.03 | 218 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.40 | -6.60 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.26 | -6.74 | 151 | 32.5 | -7.72 | -1.16 | -16.91 | 130 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.23 | -2.74 | -6.45 | 113 |
| 39 | RSI momentum · 1h | momentum | 92.41 | -7.59 | 66 | 15.2 | -0.72 | 0.12 | -23.02 | 230 |
| 40 | Connors RSI(2) · 1h | reversion | 92.32 | -7.68 | 115 | 43.5 | -18.94 | -6.26 | -21.22 | 255 |
| 41 | Agent (ML meta-label) | meta | 92.30 | -7.70 | 439 | 17.8 | 2.50 | 0.59 | -11.75 | 392 |
| 42 | Volume breakout · 1h | breakout | 91.57 | -8.43 | 70 | 20.0 | 9.08 | 1.38 | -12.60 | 117 |
| 43 | RSI(14) reversion · 1h | reversion | 91.33 | -8.67 | 36 | 30.6 | 1.44 | 0.43 | -9.40 | 132 |
| 44 | Ichimoku · 1h | trend | 90.83 | -9.18 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger reversion · 1h | reversion | 90.73 | -9.27 | 93 | 37.6 | -23.66 | -5.71 | -24.41 | 319 |
| 46 | Bollinger breakout · 1h | breakout | 90.72 | -9.28 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.52 | -9.48 | 71 | 15.5 | -6.89 | -0.58 | -27.17 | 236 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | Williams %R · 1h | reversion | 88.98 | -11.02 | 141 | 46.1 | -25.37 | -4.12 | -28.82 | 508 |
| 50 | CCI reversion · 1h | reversion | 88.79 | -11.21 | 114 | 45.6 | -10.16 | -1.35 | -14.35 | 410 |
| 51 | OBV trend · 1h | momentum | 88.52 | -11.48 | 150 | 18.7 | -12.39 | -1.17 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.06 | -11.95 | 311 | 23.2 | -32.93 | -4.89 | -40.20 | 1255 |
| 53 | Max aggression: 5-day momentum | meta | 87.91 | -12.09 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.79 | -12.21 | 130 | 30.8 | -27.97 | -5.33 | -28.00 | 491 |
| 55 | Donchian 20/10 · 1h | breakout | 87.53 | -12.47 | 63 | 17.5 | -0.70 | 0.12 | -19.51 | 215 |
| 56 | MACD zero-line · 1h | trend | 87.26 | -12.74 | 67 | 17.9 | -20.23 | -3.73 | -21.63 | 229 |
| 57 | Heikin-Ashi · 1h | trend | 87.03 | -12.97 | 158 | 27.2 | -30.40 | -5.03 | -38.03 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 86.79 | -13.21 | 108 | 13.0 | -7.65 | -0.78 | -23.19 | 331 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.46 | -13.54 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.19 | -13.81 | 156 | 17.3 | -48.04 | -22.98 | -48.12 | 585 |
| 62 | ROC + volume · 1h | momentum | 85.34 | -14.66 | 164 | 20.1 | -8.89 | -1.02 | -25.13 | 396 |
| 63 | ROC + volume | momentum | 73.36 | -26.64 | 426 | 23.0 | -72.38 | -15.90 | -74.73 | 1660 |
| 64 | Squeeze breakout | breakout | 69.22 | -30.78 | 356 | 15.4 | -62.06 | -17.94 | -62.06 | 1219 |
| 65 | Volume breakout | breakout | 68.85 | -31.15 | 285 | 14.7 | -61.24 | -17.29 | -61.24 | 887 |
| 66 | RSI(14) reversion | reversion | 67.85 | -32.15 | 434 | 26.7 | -74.32 | -17.50 | -74.32 | 1492 |
| 67 | EMA 20/50 cross | trend | 67.43 | -32.57 | 362 | 20.4 | -76.02 | -14.80 | -76.17 | 1427 |
| 68 | Donchian 55/20 | breakout | 66.43 | -33.57 | 365 | 17.5 | -68.07 | -14.19 | -69.19 | 1290 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.07 | -15.51 | -73.10 | 1417 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 492 | 15.4 | -82.87 | -25.92 | -83.05 | 1831 |
| 71 | Supertrend | trend | 60.55 | -39.45 | 510 | 20.0 | -85.68 | -20.21 | -85.92 | 1889 |
| 72 | AI bee: Boozy | ai | 59.91 | -40.09 | 267 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 56.54 | -43.46 | 440 | 9.8 | -82.11 | -22.69 | -82.11 | 1728 |
| 74 | MFI reversion | reversion | 54.74 | -45.26 | 631 | 20.0 | -87.92 | -27.44 | -88.01 | 2115 |
| 75 | AI bee: Bizzy | ai | 54.45 | -45.55 | 911 | 8.2 | — | — | — | — |
| 76 | ADX DI cross | trend | 53.59 | -46.41 | 610 | 10.7 | -88.93 | -32.99 | -89.06 | 2105 |
| 77 | Z-score reversion | reversion | 53.49 | -46.51 | 583 | 22.0 | -86.24 | -22.49 | -86.24 | 2080 |
| 78 | Donchian 20/10 | breakout | 52.22 | -47.78 | 693 | 18.0 | -90.56 | -24.92 | -90.69 | 2636 |
| 79 | MACD zero-line | trend | 51.34 | -48.66 | 640 | 15.2 | -91.22 | -28.58 | -91.32 | 2338 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.49 | -29.10 | -98.53 | 5289 |
| 81 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.02 | -28.85 | -93.06 | 2588 |
| 82 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.20 | -24.35 | -90.34 | 2354 |
| 83 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.32 | -26.46 | -91.32 | 2329 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.25 | -31.38 | -97.29 | 3506 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -34.57 | -96.29 | 3573 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -25.22 | -94.26 | 2627 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -36.37 | -99.37 | 5647 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.39 | -31.47 | -96.39 | 3609 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.36 | -99.72 | 6132 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.25 | -36.71 | -97.25 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -36.33 | -98.54 | 4667 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.24 | -31.77 | -93.24 | 2786 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.49 | -99.55 | 6113 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.11 | -32.95 | -96.11 | 3739 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.26 | -95.80 | 4051 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -45.64 | -99.88 | 8194 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T10:55 | MFI reversion | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-13T10:55 | Z-score reversion | buy | ETH-USD | 13.38 | — | entry signal |
| 2026-10-13T10:55 | RSI(14) reversion | buy | ETH-USD | 16.98 | — | entry signal |
| 2026-10-13T10:50 | Z-score reversion | buy | SOL-USD | 13.40 | — | entry signal |
| 2026-10-13T10:50 | Z-score reversion | buy | BTC-USD | 13.40 | — | entry signal |
| 2026-10-13T10:50 | RSI(14) reversion | buy | DOGE-USD | 16.99 | — | entry signal |
| 2026-10-13T10:45 | Z-score reversion | sell | BTC-USD | 10.74 | -0.11 | stop-loss |
| 2026-10-13T10:40 | Z-score reversion | sell | DOGE-USD | 13.39 | -0.13 | stop-loss |
| 2026-10-13T10:35 | RSI(14) reversion | sell | DOGE-USD | 16.91 | -0.18 | stop-loss |
| 2026-10-13T10:33 | AI bee: Bizzy | sell | XRP-USD | 7.50 | -0.07 | Jev: sell (sell p=0.89) after 10 min |
| 2026-10-13T10:30 | Z-score reversion | sell | ETH-USD | 10.74 | -0.11 | stop-loss |
| 2026-10-13T10:30 | RSI(14) reversion | sell | ETH-USD | 16.99 | -0.19 | stop-loss |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 10:55:05.000133+00:00 -> 2026-10-13 11:05:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
