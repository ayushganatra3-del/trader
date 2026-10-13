# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T22:25:05.000160+00:00 · 21769 ticks

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

Today: 36868 decisions in 3143 calls, $0.4576 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T22:25 | 3 / 1 / 1 | AMD 14% |  |
| Breezy | 2026-10-13T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T22:25 | 3 / 2 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.14 | 3.14 | 0 | — | 2.51 | 1.27 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.70 | -13.79 | 116 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.45 | 1.45 | 18 | 50.0 | -15.67 | -2.50 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.66 | 1.73 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.15 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.44 | 0.44 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.87 | -0.13 | 0 | — | 4.59 | 1.78 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.84 | -0.16 | 0 | — | -2.37 | -1.31 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.56 | -0.44 | 0 | — | 31.22 | 3.61 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.96 | -1.04 | 0 | — | -8.33 | -1.51 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.43 | -1.57 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.81 | -2.19 | 82 | 25.6 | -22.65 | -6.41 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.49 | -2.51 | 32 | 12.5 | 7.03 | 0.99 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.39 | -2.61 | 5 | 0.0 | 0.46 | 0.26 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -6.84 | -2.77 | -8.90 | 307 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.43 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.57 | -3.43 | 63 | 19.0 | -11.14 | -2.06 | -14.81 | 249 |
| 26 | Stochastic reversion · 1h | reversion | 96.27 | -3.73 | 107 | 51.4 | -14.37 | -2.80 | -16.52 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.80 | -4.20 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.56 | -4.44 | 131 | 23.7 | -8.95 | -1.17 | -19.25 | 459 |
| 29 | Z-score reversion · 1h | reversion | 95.40 | -4.60 | 50 | 44.0 | 2.78 | 0.68 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.40 | -4.61 | 45 | 15.6 | 9.66 | 1.24 | -19.71 | 139 |
| 31 | Max aggression: 1-day momentum | meta | 95.38 | -4.62 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.79 | -4.99 | -8.97 | 234 |
| 33 | Supertrend · 1h | trend | 94.00 | -6.00 | 60 | 13.3 | 2.19 | 0.47 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.95 | -6.05 | 40 | 22.5 | 5.69 | 1.23 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.78 | -6.22 | 90 | 22.2 | 1.25 | 0.35 | -22.66 | 290 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.45 | -0.44 | -5.63 | 112 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.56 | 2.18 | -6.74 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.64 | -7.36 | 66 | 15.2 | 0.93 | 0.32 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.55 | -7.45 | 165 | 31.5 | -7.95 | -1.23 | -17.02 | 131 |
| 40 | Connors RSI(2) · 1h | reversion | 92.04 | -7.96 | 127 | 42.5 | -19.96 | -5.90 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.43 | -8.57 | 37 | 32.4 | 5.93 | 1.37 | -9.40 | 126 |
| 42 | Ichimoku · 1h | trend | 91.32 | -8.68 | 48 | 16.7 | 2.06 | 0.45 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 91.08 | -8.91 | 485 | 18.1 | -3.08 | -0.44 | -12.77 | 367 |
| 44 | Triple EMA stack · 1h | trend | 90.74 | -9.26 | 71 | 15.5 | -7.83 | -0.62 | -32.27 | 242 |
| 45 | Volume breakout · 1h | breakout | 90.69 | -9.31 | 75 | 22.7 | 8.82 | 1.35 | -12.60 | 119 |
| 46 | Bollinger breakout · 1h | breakout | 90.68 | -9.31 | 77 | 28.6 | 7.26 | 1.08 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.03 | -9.97 | 97 | 37.1 | -23.81 | -5.76 | -24.98 | 322 |
| 48 | Williams %R · 1h | reversion | 89.44 | -10.56 | 143 | 45.5 | -28.11 | -4.79 | -29.98 | 511 |
| 49 | CCI reversion · 1h | reversion | 88.94 | -11.06 | 117 | 45.3 | -10.01 | -1.32 | -14.42 | 417 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.03 | -4.55 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.13 | -11.87 | 158 | 18.4 | -9.57 | -0.80 | -33.87 | 322 |
| 52 | MACD zero-line · 1h | trend | 87.64 | -12.36 | 69 | 17.4 | -21.93 | -4.28 | -22.68 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.60 | -12.40 | 325 | 23.1 | -34.36 | -5.16 | -40.76 | 1255 |
| 54 | Heikin-Ashi · 1h | trend | 87.02 | -12.98 | 164 | 26.8 | -29.83 | -4.92 | -38.32 | 678 |
| 55 | Donchian 20/10 · 1h | breakout | 87.01 | -12.99 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 56 | Max aggression: 5-day momentum | meta | 86.78 | -13.22 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 49 | 20.4 | -8.31 | -0.90 | -26.76 | 215 |
| 58 | EMA 9/21 cross · 1h | trend | 86.69 | -13.31 | 110 | 12.7 | -10.72 | -1.37 | -24.14 | 330 |
| 59 | Candlestick reversal · 1h | reversion | 86.59 | -13.41 | 140 | 30.7 | -29.25 | -5.71 | -29.91 | 473 |
| 60 | Three white soldiers | momentum | 86.57 | -13.43 | 162 | 18.5 | -47.60 | -22.32 | -47.87 | 585 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -5.03 | -20.82 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.35 | -14.65 | 173 | 20.2 | -8.82 | -1.01 | -24.84 | 399 |
| 63 | ROC + volume | momentum | 71.59 | -28.41 | 452 | 22.6 | -72.99 | -16.45 | -74.90 | 1664 |
| 64 | Volume breakout | breakout | 68.06 | -31.94 | 291 | 14.4 | -61.78 | -17.54 | -61.78 | 886 |
| 65 | Squeeze breakout | breakout | 67.87 | -32.13 | 376 | 15.4 | -62.25 | -17.92 | -62.26 | 1218 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.69 | -17.12 | -74.07 | 1482 |
| 67 | EMA 20/50 cross | trend | 66.66 | -33.34 | 385 | 20.5 | -76.18 | -14.91 | -76.43 | 1435 |
| 68 | Donchian 55/20 | breakout | 65.07 | -34.93 | 381 | 17.3 | -68.57 | -14.38 | -69.93 | 1280 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.91 | -15.10 | -71.97 | 1385 |
| 70 | Supertrend | trend | 60.13 | -39.87 | 536 | 20.1 | -85.49 | -20.20 | -85.58 | 1907 |
| 71 | AI bee: Boozy | ai | 60.10 | -39.90 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.10 | -40.90 | 524 | 14.7 | -83.20 | -26.81 | -83.20 | 1847 |
| 73 | Ichimoku | trend | 55.10 | -44.90 | 472 | 9.7 | -82.21 | -22.86 | -82.27 | 1722 |
| 74 | AI bee: Bizzy | ai | 53.82 | -46.18 | 943 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.18 | -46.82 | 668 | 20.2 | -87.90 | -27.30 | -87.91 | 2118 |
| 76 | Z-score reversion | reversion | 52.56 | -47.44 | 618 | 23.3 | -86.18 | -22.15 | -86.22 | 2087 |
| 77 | ADX DI cross | trend | 51.88 | -48.12 | 645 | 10.5 | -89.25 | -33.59 | -89.25 | 2116 |
| 78 | Donchian 20/10 | breakout | 50.70 | -49.30 | 733 | 17.3 | -90.73 | -25.34 | -90.73 | 2628 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -29.00 | -98.50 | 5309 |
| 80 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.20 | -29.48 | -93.22 | 2603 |
| 81 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.16 | -24.50 | -90.19 | 2364 |
| 82 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.67 | -26.97 | -91.67 | 2357 |
| 83 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.28 | -31.80 | -97.28 | 3523 |
| 84 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.41 | -35.06 | -96.41 | 3585 |
| 85 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -25.31 | -94.41 | 2637 |
| 86 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.75 | -99.36 | 5624 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -31.04 | -96.34 | 3591 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.42 | -99.72 | 6159 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.32 | -29.08 | -91.32 | 2349 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.06 | -97.37 | 3674 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.55 | -98.51 | 4672 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.35 | -32.04 | -93.35 | 2796 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.41 | -99.54 | 6121 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -32.00 | -95.98 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -33.33 | -95.65 | 4039 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.85 | -99.89 | 8213 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-13T19:55 | MFI reversion | sell | SPY | 10.65 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | MFI reversion | sell | QQQ | 13.30 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | MFI reversion | sell | ETHU | 13.33 | -0.03 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 22:25:05.000160+00:00 -> 2026-10-13 22:35:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
