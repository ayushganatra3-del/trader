# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T22:55:05.000138+00:00 · 21798 ticks

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
| Copy: Insider buying | 2026-10-13 | BBD 12%, GGR 12%, COE 12%, BORR 12%, BPRE 12%, PSUS 12%, AXIA 12%, ACCV 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.32 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 37288 decisions in 3227 calls, $0.4635 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T22:55 | 1 / 4 / 0 | AMD 14% |  |
| Breezy | 2026-10-13T22:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T22:55 | 2 / 3 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.17 | 3.17 | 0 | — | 2.51 | 1.27 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.70 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.48 | 1.48 | 18 | 50.0 | -15.68 | -2.50 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.74 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.10 | 1.10 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.15 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.47 | 0.47 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.89 | -0.11 | 0 | — | 4.58 | 1.78 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.86 | -0.14 | 0 | — | -2.37 | -1.31 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.68 | -0.32 | 0 | — | 31.22 | 3.61 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.98 | -1.02 | 0 | — | -8.34 | -1.51 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.46 | -1.54 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.84 | -2.16 | 82 | 25.6 | -22.65 | -6.41 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.52 | -2.48 | 32 | 12.5 | 7.03 | 0.99 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.42 | -2.58 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -6.73 | -2.73 | -8.77 | 305 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.43 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.61 | -3.39 | 63 | 19.0 | -11.14 | -2.05 | -14.81 | 249 |
| 26 | Stochastic reversion · 1h | reversion | 96.31 | -3.69 | 107 | 51.4 | -14.34 | -2.79 | -16.50 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.83 | -4.17 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.62 | -4.38 | 131 | 23.7 | -8.92 | -1.16 | -19.25 | 459 |
| 29 | Z-score reversion · 1h | reversion | 95.47 | -4.53 | 50 | 44.0 | 2.81 | 0.69 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.43 | -4.57 | 45 | 15.6 | 9.68 | 1.24 | -19.71 | 139 |
| 31 | Max aggression: 1-day momentum | meta | 95.41 | -4.59 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.98 | -5.11 | -8.99 | 233 |
| 33 | Supertrend · 1h | trend | 94.05 | -5.95 | 60 | 13.3 | 1.71 | 0.41 | -20.32 | 214 |
| 34 | Squeeze breakout · 1h | breakout | 93.96 | -6.04 | 40 | 22.5 | 5.69 | 1.23 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.80 | -6.20 | 90 | 22.2 | 1.24 | 0.35 | -22.66 | 290 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.20 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.67 | -7.33 | 66 | 15.2 | 0.94 | 0.32 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.59 | -7.41 | 165 | 31.5 | -8.90 | -1.41 | -17.02 | 131 |
| 40 | Connors RSI(2) · 1h | reversion | 92.07 | -7.93 | 127 | 42.5 | -19.97 | -5.91 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.49 | -8.51 | 37 | 32.4 | 5.96 | 1.37 | -9.40 | 126 |
| 42 | Ichimoku · 1h | trend | 91.35 | -8.65 | 48 | 16.7 | 2.06 | 0.45 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 91.11 | -8.88 | 485 | 18.1 | 2.22 | 0.53 | -12.77 | 359 |
| 44 | Triple EMA stack · 1h | trend | 90.78 | -9.22 | 71 | 15.5 | -7.82 | -0.62 | -32.27 | 242 |
| 45 | Volume breakout · 1h | breakout | 90.70 | -9.30 | 75 | 22.7 | 8.60 | 1.32 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.70 | -9.30 | 77 | 28.6 | 7.26 | 1.08 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.06 | -9.95 | 97 | 37.1 | -23.81 | -5.76 | -24.98 | 322 |
| 48 | Williams %R · 1h | reversion | 89.48 | -10.52 | 143 | 45.5 | -28.07 | -4.78 | -29.95 | 511 |
| 49 | CCI reversion · 1h | reversion | 89.01 | -10.99 | 117 | 45.3 | -9.88 | -1.30 | -14.42 | 417 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.55 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.16 | -11.84 | 158 | 18.4 | -9.77 | -0.82 | -33.87 | 323 |
| 52 | MACD zero-line · 1h | trend | 87.66 | -12.34 | 69 | 17.4 | -21.93 | -4.28 | -22.68 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.66 | -12.34 | 325 | 23.1 | -34.33 | -5.16 | -40.76 | 1256 |
| 54 | Donchian 20/10 · 1h | breakout | 87.03 | -12.97 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Heikin-Ashi · 1h | trend | 87.03 | -12.97 | 164 | 26.8 | -30.20 | -5.00 | -38.65 | 678 |
| 56 | Max aggression: 5-day momentum | meta | 86.81 | -13.19 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | EMA 9/21 cross · 1h | trend | 86.74 | -13.27 | 110 | 12.7 | -10.69 | -1.37 | -24.13 | 330 |
| 58 | Keltner breakout · 1h | breakout | 86.71 | -13.29 | 49 | 20.4 | -8.31 | -0.90 | -26.76 | 215 |
| 59 | Candlestick reversal · 1h | reversion | 86.64 | -13.36 | 140 | 30.7 | -29.24 | -5.71 | -29.92 | 472 |
| 60 | Three white soldiers | momentum | 86.57 | -13.43 | 162 | 18.5 | -47.57 | -22.31 | -47.80 | 582 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -5.03 | -20.83 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.37 | -14.63 | 173 | 20.2 | -8.82 | -1.01 | -24.84 | 399 |
| 63 | ROC + volume | momentum | 71.59 | -28.41 | 452 | 22.6 | -72.93 | -16.41 | -74.84 | 1665 |
| 64 | Volume breakout | breakout | 68.06 | -31.94 | 291 | 14.4 | -61.76 | -17.52 | -61.76 | 886 |
| 65 | Squeeze breakout | breakout | 67.87 | -32.13 | 376 | 15.4 | -62.25 | -17.92 | -62.27 | 1218 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.67 | -17.10 | -74.04 | 1481 |
| 67 | EMA 20/50 cross | trend | 66.70 | -33.30 | 385 | 20.5 | -76.12 | -14.88 | -76.43 | 1433 |
| 68 | Donchian 55/20 | breakout | 65.09 | -34.91 | 381 | 17.3 | -68.63 | -14.40 | -69.93 | 1280 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.92 | -15.11 | -71.99 | 1386 |
| 70 | Supertrend | trend | 60.21 | -39.79 | 536 | 20.1 | -85.48 | -20.18 | -85.59 | 1908 |
| 71 | AI bee: Boozy | ai | 60.10 | -39.90 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.10 | -40.90 | 524 | 14.7 | -83.11 | -26.82 | -83.11 | 1844 |
| 73 | Ichimoku | trend | 55.10 | -44.90 | 472 | 9.7 | -82.24 | -22.87 | -82.28 | 1722 |
| 74 | AI bee: Bizzy | ai | 53.77 | -46.23 | 944 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.20 | -46.80 | 668 | 20.2 | -87.88 | -27.35 | -87.89 | 2116 |
| 76 | Z-score reversion | reversion | 52.56 | -47.44 | 618 | 23.3 | -86.17 | -22.15 | -86.21 | 2086 |
| 77 | ADX DI cross | trend | 51.88 | -48.12 | 645 | 10.5 | -89.24 | -33.59 | -89.24 | 2116 |
| 78 | Donchian 20/10 | breakout | 50.68 | -49.32 | 733 | 17.3 | -90.69 | -25.32 | -90.70 | 2626 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.93 | -98.49 | 5317 |
| 80 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -29.50 | -93.21 | 2604 |
| 81 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.17 | -24.52 | -90.20 | 2364 |
| 82 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -26.88 | -91.65 | 2357 |
| 83 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.80 | -97.28 | 3524 |
| 84 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -34.99 | -96.38 | 3578 |
| 85 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -25.31 | -94.40 | 2634 |
| 86 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.71 | -99.36 | 5628 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -31.01 | -96.34 | 3591 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.48 | -99.72 | 6164 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.35 | -29.15 | -91.35 | 2352 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -37.01 | -97.37 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.55 | -98.51 | 4673 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.32 | -31.99 | -93.32 | 2793 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.41 | -99.54 | 6121 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -31.99 | -95.99 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -33.33 | -95.65 | 4039 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.72 | -99.89 | 8214 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T22:44 | AI bee: Bizzy | sell | DOGE-USD | 7.91 | -0.05 | Jev: sell (sell p=0.78) after 11 min |
| 2026-10-13T22:40 | Donchian 20/10 | buy | XRP-USD | 12.68 | — | entry signal |
| 2026-10-13T22:33 | AI bee: Bizzy | buy | DOGE-USD | 7.97 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T22:20 | Squeeze breakout | sell | BTC-USD | 16.89 | -0.10 | exit signal |
| 2026-10-13T22:05 | Three white soldiers | sell | DOGE-USD | 21.50 | -0.19 | target is flat |
| 2026-10-13T22:05 | Donchian 20/10 | sell | DOGE-USD | 12.59 | -0.12 | stop-loss |
| 2026-10-13T22:05 | ADX DI cross | sell | DOGE-USD | 12.91 | -0.08 | exit signal |
| 2026-10-13T22:00 | MACD cross · 1h | buy | BTC-USD | 3.66 | — | entry signal |
| 2026-10-13T22:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.11 | — | entry signal |
| 2026-10-13T22:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.11 | -0.05 | rebalance down |
| 2026-10-13T21:50 | Donchian 20/10 | buy | DOGE-USD | 12.71 | — | entry signal |
| 2026-10-13T21:43 | AI bee: Bizzy | sell | DOGE-USD | 8.23 | -0.05 | Jev: sell (sell p=0.59) after 10 min |
| 2026-10-13T21:40 | Three white soldiers | buy | DOGE-USD | 21.69 | — | entry signal |
| 2026-10-13T21:40 | Donchian 20/10 | buy | ETH-USD | 12.72 | — | entry signal |
| 2026-10-13T21:35 | MFI reversion | buy | XRP-USD | 13.31 | — | entry signal |
| 2026-10-13T21:35 | Donchian 55/20 | buy | BTC-USD | 16.28 | — | entry signal |
| 2026-10-13T21:33 | AI bee: Bizzy | buy | DOGE-USD | 8.29 | — | Jev: buy (buy p=0.62) |
| 2026-10-13T21:30 | EMA 20/50 cross | sell | XRP-USD | 16.65 | -0.13 | exit signal |
| 2026-10-13T21:25 | Volume breakout | sell | BTC-USD | 16.93 | -0.12 | exit signal |
| 2026-10-13T21:25 | Ichimoku | sell | DOGE-USD | 13.70 | -0.10 | exit signal |
| 2026-10-13T21:20 | Ichimoku | buy | DOGE-USD | 13.80 | — | entry signal |
| 2026-10-13T21:03 | AI bee: Bizzy | sell | BTC-USD | 7.73 | -0.05 | Jev: sell (sell p=0.53) after 16 min |
| 2026-10-13T20:55 | EMA 20/50 cross | buy | ETH-USD | 16.71 | — | entry signal |
| 2026-10-13T20:55 | EMA 20/50 cross | buy | BTC-USD | 16.71 | — | entry signal |
| 2026-10-13T20:50 | Volume breakout | buy | BTC-USD | 17.04 | — | entry signal |
| 2026-10-13T20:50 | Squeeze breakout | buy | BTC-USD | 16.99 | — | entry signal |
| 2026-10-13T20:47 | AI bee: Bizzy | buy | BTC-USD | 7.78 | — | Jev: buy (buy p=0.58) |
| 2026-10-13T20:45 | Ichimoku | sell | XRP-USD | 13.76 | -0.09 | exit signal |
| 2026-10-13T20:45 | Supertrend | buy | BTC-USD | 14.99 | — | entry signal |
| 2026-10-13T20:40 | Donchian 20/10 | buy | BTC-USD | 12.72 | — | entry signal |
| 2026-10-13T20:30 | EMA 20/50 cross | sell | SOL-USD | 16.64 | -0.13 | exit signal |
| 2026-10-13T20:20 | Supertrend | sell | SOL-USD | 14.99 | -0.12 | exit signal |
| 2026-10-13T20:00 | OBV trend · 1h | buy | BTC-USD | 4.12 | — | entry signal |
| 2026-10-13T19:55 | Agent (rotation) | sell | TQQQ | 32.40 | 0.35 | selected signal exited |
| 2026-10-13T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 100.53 | 0.01 | target is flat |
| 2026-10-13T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | TQQQ | 101.41 | 1.10 | target is flat |
| 2026-10-13T19:55 | Agent | sell | IWM | 19.00 | -0.04 | selected signal exited |
| 2026-10-13T19:55 | MFI reversion · 1h | buy | TECL | 10.73 | — | entry |
| 2026-10-13T19:55 | MFI reversion · 1h | sell | TNA | 10.73 | -0.03 | target is flat |
| 2026-10-13T19:55 | MFI reversion | sell | UPRO | 10.67 | 0.01 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 22:55:05.000138+00:00 -> 2026-10-13 23:05:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
