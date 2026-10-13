# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T21:55:05.000159+00:00 · 21747 ticks

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

Today: 36538 decisions in 3077 calls, $0.4530 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T21:55 | 1 / 2 / 2 | AMD 14% |  |
| Breezy | 2026-10-13T21:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T21:55 | 1 / 3 / 1 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.22 | +2.54% | 5 |
| RSI momentum | AMZN | 2.13 | +2.75% | 6 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| RSI momentum | IWM | 1.94 | +0.75% | 3 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.14 | 3.14 | 0 | — | 2.51 | 1.27 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -10.90 | -3.16 | -13.79 | 119 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.45 | 1.45 | 18 | 50.0 | -15.67 | -2.50 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.74 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.07 | 1.07 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.15 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.44 | 0.44 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.85 | -0.15 | 0 | — | 4.58 | 1.78 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.84 | -0.16 | 0 | — | -2.37 | -1.31 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.62 | -0.38 | 0 | — | 31.29 | 3.61 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.96 | -1.04 | 0 | — | -8.34 | -1.51 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.43 | -1.57 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.71 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.81 | -2.19 | 82 | 25.6 | -22.65 | -6.41 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.49 | -2.51 | 32 | 12.5 | 7.03 | 0.99 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.39 | -2.61 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.50 | -3.06 | -9.38 | 311 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.43 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.58 | -3.42 | 63 | 19.0 | -10.86 | -2.00 | -14.81 | 248 |
| 26 | Stochastic reversion · 1h | reversion | 96.28 | -3.73 | 107 | 51.4 | -14.37 | -2.80 | -16.52 | 345 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.80 | -4.20 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.61 | -4.39 | 131 | 23.7 | -8.89 | -1.16 | -19.25 | 458 |
| 29 | Z-score reversion · 1h | reversion | 95.44 | -4.56 | 50 | 44.0 | 2.78 | 0.68 | -8.60 | 159 |
| 30 | EMA 20/50 cross · 1h | trend | 95.39 | -4.61 | 45 | 15.6 | 9.48 | 1.22 | -19.71 | 140 |
| 31 | Max aggression: 1-day momentum | meta | 95.38 | -4.62 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -9.06 | -5.15 | -9.07 | 234 |
| 33 | Supertrend · 1h | trend | 94.03 | -5.97 | 60 | 13.3 | 2.23 | 0.48 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.95 | -6.05 | 40 | 22.5 | 5.69 | 1.23 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.78 | -6.22 | 90 | 22.2 | 1.24 | 0.35 | -22.66 | 290 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.62 | -0.50 | -5.61 | 112 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.34 | 2.13 | -6.93 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.64 | -7.36 | 66 | 15.2 | 0.86 | 0.31 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.56 | -7.44 | 165 | 31.5 | -7.17 | -1.09 | -17.02 | 134 |
| 40 | Connors RSI(2) · 1h | reversion | 92.04 | -7.96 | 127 | 42.5 | -19.97 | -5.90 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.47 | -8.53 | 37 | 32.4 | 6.02 | 1.39 | -9.40 | 127 |
| 42 | Ichimoku · 1h | trend | 91.32 | -8.68 | 48 | 16.7 | 1.88 | 0.43 | -22.34 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.08 | -8.92 | 485 | 18.1 | 0.56 | 0.24 | -13.04 | 372 |
| 44 | Triple EMA stack · 1h | trend | 90.75 | -9.25 | 71 | 15.5 | -7.99 | -0.63 | -32.27 | 243 |
| 45 | Volume breakout · 1h | breakout | 90.69 | -9.31 | 75 | 22.7 | 7.73 | 1.20 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.68 | -9.31 | 77 | 28.6 | 7.24 | 1.08 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.03 | -9.97 | 97 | 37.1 | -23.81 | -5.76 | -24.98 | 322 |
| 48 | Williams %R · 1h | reversion | 89.44 | -10.55 | 143 | 45.5 | -28.10 | -4.79 | -29.98 | 511 |
| 49 | CCI reversion · 1h | reversion | 88.98 | -11.02 | 117 | 45.3 | -9.94 | -1.31 | -14.42 | 417 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.55 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.13 | -11.87 | 158 | 18.4 | -10.04 | -0.85 | -33.92 | 323 |
| 52 | MACD zero-line · 1h | trend | 87.64 | -12.36 | 69 | 17.4 | -21.93 | -4.28 | -22.68 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.63 | -12.37 | 325 | 23.1 | -33.87 | -5.06 | -40.35 | 1254 |
| 54 | Heikin-Ashi · 1h | trend | 87.01 | -12.98 | 164 | 26.8 | -29.83 | -4.92 | -38.32 | 678 |
| 55 | Donchian 20/10 · 1h | breakout | 87.01 | -12.99 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 56 | Max aggression: 5-day momentum | meta | 86.78 | -13.22 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | EMA 9/21 cross · 1h | trend | 86.73 | -13.27 | 110 | 12.7 | -10.50 | -1.34 | -24.14 | 327 |
| 58 | Three white soldiers | momentum | 86.70 | -13.30 | 161 | 18.6 | -47.59 | -22.31 | -47.87 | 583 |
| 59 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 49 | 20.4 | -8.10 | -0.87 | -26.76 | 214 |
| 60 | Candlestick reversal · 1h | reversion | 86.61 | -13.39 | 140 | 30.7 | -29.81 | -5.79 | -30.55 | 476 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -5.03 | -20.83 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.34 | -14.66 | 173 | 20.2 | -10.00 | -1.18 | -25.73 | 394 |
| 63 | ROC + volume | momentum | 71.59 | -28.41 | 452 | 22.6 | -72.64 | -16.32 | -74.57 | 1661 |
| 64 | Volume breakout | breakout | 68.06 | -31.94 | 291 | 14.4 | -61.72 | -17.50 | -61.72 | 892 |
| 65 | Squeeze breakout | breakout | 67.94 | -32.05 | 375 | 15.5 | -62.29 | -17.95 | -62.31 | 1219 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.82 | -17.18 | -74.19 | 1486 |
| 67 | EMA 20/50 cross | trend | 66.68 | -33.32 | 385 | 20.5 | -76.17 | -14.90 | -76.43 | 1435 |
| 68 | Donchian 55/20 | breakout | 65.08 | -34.92 | 381 | 17.3 | -68.55 | -14.37 | -69.93 | 1280 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.74 | -15.24 | -71.77 | 1386 |
| 70 | Supertrend | trend | 60.18 | -39.82 | 536 | 20.1 | -85.50 | -20.21 | -85.58 | 1908 |
| 71 | AI bee: Boozy | ai | 60.10 | -39.90 | 267 | 4.9 | — | — | — | — |
| 72 | Keltner breakout | breakout | 59.10 | -40.90 | 524 | 14.7 | -83.20 | -26.81 | -83.20 | 1847 |
| 73 | Ichimoku | trend | 55.10 | -44.90 | 472 | 9.7 | -82.26 | -22.88 | -82.28 | 1724 |
| 74 | AI bee: Bizzy | ai | 53.82 | -46.18 | 943 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.19 | -46.81 | 668 | 20.2 | -87.79 | -27.57 | -87.79 | 2108 |
| 76 | Z-score reversion | reversion | 52.56 | -47.44 | 618 | 23.3 | -86.18 | -22.15 | -86.22 | 2087 |
| 77 | ADX DI cross | trend | 51.96 | -48.04 | 644 | 10.6 | -89.24 | -33.55 | -89.25 | 2117 |
| 78 | Donchian 20/10 | breakout | 50.79 | -49.21 | 732 | 17.3 | -90.71 | -25.33 | -90.71 | 2628 |
| 79 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.47 | -29.06 | -98.48 | 5294 |
| 80 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -29.39 | -93.20 | 2602 |
| 81 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.15 | -24.48 | -90.19 | 2364 |
| 82 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.61 | -26.94 | -91.61 | 2354 |
| 83 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.30 | -31.84 | -97.30 | 3527 |
| 84 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -34.94 | -96.34 | 3570 |
| 85 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -25.26 | -94.36 | 2631 |
| 86 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -35.82 | -99.36 | 5632 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -31.03 | -96.33 | 3591 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -40.33 | -99.72 | 6159 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.32 | -29.09 | -91.33 | 2350 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -37.08 | -97.36 | 3674 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.60 | -98.51 | 4671 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.34 | -32.05 | -93.35 | 2796 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.57 | -99.54 | 6122 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.97 | -32.00 | -95.97 | 3735 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -33.34 | -95.64 | 4039 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.91 | -99.89 | 8214 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-13T19:55 | VWAP reversion | sell | MSTR | 15.74 | 0.03 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | MSFT | 15.65 | -0.07 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | LABU | 12.47 | -0.13 | end-of-day flatten |
| 2026-10-13T19:55 | VWAP reversion | sell | AMZN | 15.65 | -0.01 | end-of-day flatten |
| 2026-10-13T19:55 | Z-score reversion | sell | LABU | 13.03 | -0.14 | end-of-day flatten |
| 2026-10-13T19:55 | Z-score reversion | sell | AMZN | 13.18 | -0.03 | end-of-day flatten |
| 2026-10-13T19:55 | Squeeze breakout | sell | IWM | 13.67 | -0.03 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 21:55:05.000159+00:00 -> 2026-10-13 22:05:05.000159+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
