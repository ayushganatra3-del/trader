# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T03:55:05.000193+00:00 · 20911 ticks

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

Today: 2850 decisions in 570 calls, $0.0400 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T03:55 | 0 / 3 / 2 | SOL-USD 14%, PLTR 15%, AMD 15%, DOGE-USD 14% |  |
| Breezy | 2026-10-13T03:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T03:55 | 4 / 0 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.81 | 2.81 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.10 | 2.10 | 16 | 50.0 | -12.87 | -2.12 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.32 | 1.32 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.11 | 1.11 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.55 | 0.55 | 0 | — | -5.03 | -0.82 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.52 | 0.52 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.02 | 0.02 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Hold BTC | benchmark | 99.64 | -0.36 | 0 | — | 30.28 | 3.52 | -8.68 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.26 | -0.74 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.17 | -1.83 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.04 | -1.96 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 97.91 | -2.09 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.78 | -2.23 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.24 | -2.76 | 101 | 51.5 | -11.56 | -2.15 | -13.91 | 347 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.93 | -3.07 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.70 | -3.30 | 45 | 42.2 | 3.49 | 0.82 | -8.60 | 165 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.40 | -3.60 | 62 | 19.4 | -5.60 | -0.88 | -13.79 | 251 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.36 | -2.62 | -9.12 | 297 |
| 30 | MACD cross · 1h | trend | 95.78 | -4.22 | 125 | 24.0 | -11.40 | -1.78 | -17.79 | 461 |
| 31 | Parabolic SAR · 1h | trend | 95.28 | -4.72 | 86 | 22.1 | 2.01 | 0.45 | -21.52 | 289 |
| 32 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.82 | -3.78 | -8.72 | 231 |
| 33 | EMA 20/50 cross · 1h | trend | 95.25 | -4.75 | 45 | 15.6 | 4.88 | 0.75 | -23.71 | 136 |
| 34 | Supertrend · 1h | trend | 94.47 | -5.53 | 58 | 13.8 | 0.74 | 0.29 | -18.92 | 213 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.46 | -6.54 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.37 | -6.63 | 151 | 32.5 | -7.55 | -1.13 | -16.91 | 130 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.23 | -2.74 | -6.45 | 113 |
| 39 | RSI momentum · 1h | momentum | 92.52 | -7.48 | 66 | 15.2 | -0.62 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.43 | -7.57 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.41 | -7.58 | 439 | 17.8 | 0.36 | 0.20 | -12.69 | 393 |
| 42 | RSI(14) reversion · 1h | reversion | 91.67 | -8.33 | 34 | 26.5 | 0.99 | 0.33 | -9.40 | 135 |
| 43 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 70 | 20.0 | 9.08 | 1.38 | -12.60 | 117 |
| 44 | Ichimoku · 1h | trend | 90.93 | -9.07 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.80 | -9.20 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 46 | Bollinger reversion · 1h | reversion | 90.66 | -9.34 | 89 | 34.8 | -23.62 | -5.69 | -24.43 | 320 |
| 47 | Triple EMA stack · 1h | trend | 90.62 | -9.38 | 71 | 15.5 | -7.39 | -0.65 | -27.17 | 238 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 88.95 | -11.05 | 113 | 45.1 | -9.91 | -1.30 | -14.35 | 412 |
| 50 | Williams %R · 1h | reversion | 88.95 | -11.05 | 137 | 44.5 | -25.61 | -4.17 | -28.82 | 510 |
| 51 | OBV trend · 1h | momentum | 88.63 | -11.37 | 150 | 18.7 | -12.46 | -1.18 | -34.14 | 317 |
| 52 | VWAP momentum · 1h | momentum | 88.16 | -11.84 | 311 | 23.2 | -32.70 | -4.84 | -40.20 | 1255 |
| 53 | Max aggression: 5-day momentum | meta | 88.01 | -11.99 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 87.98 | -12.02 | 130 | 30.8 | -28.82 | -5.48 | -29.12 | 496 |
| 55 | Heikin-Ashi · 1h | trend | 87.70 | -12.30 | 153 | 28.1 | -29.98 | -4.94 | -37.65 | 675 |
| 56 | Donchian 20/10 · 1h | breakout | 87.63 | -12.37 | 63 | 17.5 | -0.59 | 0.13 | -19.51 | 214 |
| 57 | MACD zero-line · 1h | trend | 87.53 | -12.47 | 67 | 17.9 | -21.28 | -3.95 | -21.53 | 233 |
| 58 | EMA 9/21 cross · 1h | trend | 87.04 | -12.96 | 108 | 13.0 | -8.22 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.57 | -13.43 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.49 | -13.51 | 154 | 17.5 | -48.09 | -22.95 | -48.17 | 586 |
| 62 | ROC + volume · 1h | momentum | 85.44 | -14.56 | 164 | 20.1 | -9.19 | -1.06 | -25.13 | 397 |
| 63 | ROC + volume | momentum | 73.34 | -26.66 | 421 | 22.3 | -72.52 | -16.00 | -74.73 | 1663 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.12 | -17.91 | -62.12 | 1220 |
| 65 | Volume breakout | breakout | 69.27 | -30.73 | 279 | 14.7 | -61.56 | -17.41 | -61.61 | 893 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.87 | -17.24 | -74.05 | 1487 |
| 67 | EMA 20/50 cross | trend | 67.79 | -32.21 | 357 | 19.9 | -76.20 | -14.88 | -76.40 | 1434 |
| 68 | Donchian 55/20 | breakout | 66.51 | -33.48 | 360 | 17.5 | -68.18 | -14.24 | -69.18 | 1294 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -72.84 | -15.46 | -72.87 | 1415 |
| 70 | Supertrend | trend | 60.92 | -39.08 | 503 | 19.3 | -85.71 | -20.18 | -86.05 | 1894 |
| 71 | Keltner breakout | breakout | 60.80 | -39.20 | 485 | 14.6 | -83.03 | -26.23 | -83.21 | 1838 |
| 72 | AI bee: Boozy | ai | 60.13 | -39.87 | 264 | 4.9 | — | — | — | — |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.13 | -22.67 | -82.13 | 1729 |
| 74 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -87.90 | -27.05 | -88.10 | 2116 |
| 75 | AI bee: Bizzy | ai | 55.14 | -44.86 | 897 | 8.4 | — | — | — | — |
| 76 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.23 | -22.36 | -86.43 | 2079 |
| 77 | ADX DI cross | trend | 53.99 | -46.01 | 600 | 10.0 | -88.98 | -32.69 | -89.14 | 2107 |
| 78 | Donchian 20/10 | breakout | 52.65 | -47.35 | 684 | 17.5 | -90.63 | -24.90 | -90.79 | 2641 |
| 79 | MACD zero-line | trend | 51.40 | -48.60 | 637 | 14.8 | -91.32 | -28.76 | -91.43 | 2345 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.51 | -29.09 | -98.55 | 5301 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.07 | -29.04 | -93.13 | 2593 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.25 | -24.45 | -90.42 | 2359 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.27 | -31.50 | -97.32 | 3512 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -34.50 | -96.34 | 3578 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -25.49 | -94.38 | 2641 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.85 | -99.38 | 5646 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.30 | 3592 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.64 | -99.72 | 6138 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.25 | -36.56 | -97.25 | 3649 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -35.87 | -98.54 | 4666 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.27 | -31.73 | -93.30 | 2791 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.74 | -99.55 | 6111 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -32.52 | -96.09 | 3735 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.87 | -95.80 | 4050 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -44.50 | -99.88 | 8199 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T03:55 | ADX DI cross | sell | ETH-USD | 2.69 | 0.03 | rebalance down |
| 2026-10-13T03:55 | EMA 20/50 cross | sell | ETH-USD | 3.38 | 0.01 | rebalance down |
| 2026-10-13T03:50 | AI bee: Bizzy | buy | SOL-USD | 7.75 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T03:50 | ROC + volume | buy | SOL-USD | 7.44 | — | entry signal |
| 2026-10-13T03:50 | ROC + volume | sell | ETH-USD | 3.71 | 0.06 | rebalance down |
| 2026-10-13T03:50 | ROC + volume | sell | DOGE-USD | 3.73 | 0.06 | rebalance down |
| 2026-10-13T03:44 | AI bee: Bizzy | sell | ETH-USD | 7.69 | -0.06 | Jev: sell (sell p=0.55) after 11 min |
| 2026-10-13T03:35 | Volume breakout | buy | ETH-USD | 17.36 | — | entry signal |
| 2026-10-13T03:35 | Volume breakout | buy | DOGE-USD | 17.36 | — | entry signal |
| 2026-10-13T03:35 | Volume breakout | buy | BTC-USD | 17.36 | — | entry signal |
| 2026-10-13T03:35 | Donchian 55/20 | buy | SOL-USD | 13.33 | — | entry signal |
| 2026-10-13T03:35 | Donchian 55/20 | buy | ETH-USD | 13.35 | — | entry signal |
| 2026-10-13T03:35 | Donchian 55/20 | buy | DOGE-USD | 13.35 | — | entry signal |
| 2026-10-13T03:35 | Donchian 55/20 | sell | XRP-USD | 3.36 | 0.00 | rebalance down |
| 2026-10-13T03:35 | Donchian 55/20 | sell | BTC-USD | 3.35 | 0.00 | rebalance down |
| 2026-10-13T03:33 | AI bee: Bizzy | buy | ETH-USD | 7.76 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T03:25 | AI bee: Bizzy | buy | DOGE-USD | 7.74 | — | Jev: buy (buy p=0.56) |
| 2026-10-13T03:23 | AI bee: Boozy | sell | ETH-USD | 14.01 | -0.08 | Jev: buy |
| 2026-10-13T03:20 | Three white soldiers | sell | BTC-USD | 21.65 | 0.03 | exit signal |
| 2026-10-13T03:20 | MACD zero-line | buy | SOL-USD | 5.09 | — | rebalance up |
| 2026-10-13T03:20 | MACD zero-line | sell | XRP-USD | 10.19 | 0.03 | exit signal |
| 2026-10-13T03:20 | MACD zero-line | sell | BTC-USD | 10.18 | 0.01 | exit signal |
| 2026-10-13T03:10 | Keltner breakout | buy | SOL-USD | 3.02 | — | rebalance up |
| 2026-10-13T03:10 | Keltner breakout | sell | DOGE-USD | 3.02 | 0.00 | rebalance down |
| 2026-10-13T03:10 | ADX DI cross | buy | SOL-USD | 2.68 | — | rebalance up |
| 2026-10-13T03:10 | ADX DI cross | sell | DOGE-USD | 2.68 | 0.01 | rebalance down |
| 2026-10-13T03:08 | AI bee: Boozy | buy | ETH-USD | 14.09 | — | Jev: buy (buy p=0.77) |
| 2026-10-13T03:06 | AI bee: Bizzy | sell | XRP-USD | 7.90 | -0.05 | Jev: sell (sell p=0.68) after 11 min |
| 2026-10-13T03:00 | Williams %R · 1h | buy | XRP-USD | 8.07 | — | entry |
| 2026-10-13T03:00 | Williams %R · 1h | buy | SOL-USD | 4.56 | — | rebalance up |
| 2026-10-13T03:00 | Williams %R · 1h | sell | BTC-USD | 12.63 | -0.01 | exit signal |
| 2026-10-13T03:00 | Stochastic reversion · 1h | buy | SOL-USD | 10.84 | — | entry |
| 2026-10-13T03:00 | Stochastic reversion · 1h | sell | BTC-USD | 10.84 | 0.12 | exit signal |
| 2026-10-13T03:00 | Bollinger reversion · 1h | buy | XRP-USD | 10.03 | — | entry |
| 2026-10-13T03:00 | Bollinger reversion · 1h | sell | BTC-USD | 10.03 | -0.01 | exit signal |
| 2026-10-13T03:00 | MACD zero-line | sell | DOGE-USD | 2.56 | 0.01 | rebalance down |
| 2026-10-13T02:55 | AI bee: Bizzy | buy | XRP-USD | 7.95 | — | Jev: buy (buy p=0.58) |
| 2026-10-13T02:51 | EMA 20/50 cross | buy | SOL-USD | 3.36 | — | rebalance up |
| 2026-10-13T02:51 | EMA 20/50 cross | sell | BTC-USD | 3.36 | -0.02 | rebalance down |
| 2026-10-13T02:50 | EMA 20/50 cross | buy | SOL-USD | 6.78 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 03:55:05.000193+00:00 -> 2026-10-13 04:05:05.000193+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
