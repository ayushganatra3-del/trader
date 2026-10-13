# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-13T02:25:05.000174+00:00 · 20831 ticks

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

Today: 1650 decisions in 330 calls, $0.0232 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-13T02:25 | 1 / 3 / 1 | SOL-USD 15%, ETH-USD 14%, PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-13T02:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-13T02:25 | 5 / 0 / 0 | ETH-USD 23% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.92 | 2.92 | 0 | — | 1.61 | 0.83 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.21 | 2.21 | 16 | 50.0 | -12.86 | -2.12 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Hold SPY | benchmark | 101.43 | 1.43 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.10 | -3.27 | 17 |
| 6 | VWAP reversion · 1h | reversion | 101.24 | 1.24 | 42 | 40.5 | -8.80 | -2.61 | -13.79 | 117 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.22 | 1.22 | 0 | — | 1.71 | 0.83 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.65 | 0.65 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.63 | 0.63 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.30 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.43 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 3.58 | 1.40 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.36 | -0.64 | 0 | — | -4.89 | -2.25 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Hold BTC | benchmark | 99.11 | -0.89 | 0 | — | 29.50 | 3.45 | -8.68 | 1 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.78 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.24 | -1.76 | 31 | 12.9 | 12.04 | 1.45 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.14 | -1.86 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.01 | -1.99 | 11 | 36.4 | -16.71 | -0.62 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.88 | -2.12 | 78 | 23.1 | -23.01 | -6.42 | -25.60 | 168 |
| 23 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 24 | Stochastic reversion · 1h | reversion | 97.10 | -2.90 | 100 | 51.0 | -11.52 | -2.16 | -13.91 | 345 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 97.03 | -2.97 | 0 | — | 9.02 | 1.50 | -8.33 | 1 |
| 26 | Z-score reversion · 1h | reversion | 96.72 | -3.28 | 45 | 42.2 | 3.25 | 0.77 | -8.60 | 163 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.48 | -3.52 | 62 | 19.4 | -5.74 | -0.91 | -13.79 | 252 |
| 29 | Agent (rotation) | meta | 96.15 | -3.85 | 86 | 30.2 | -7.56 | -2.71 | -8.94 | 304 |
| 30 | MACD cross · 1h | trend | 95.85 | -4.15 | 125 | 24.0 | -11.45 | -1.79 | -17.79 | 461 |
| 31 | Parabolic SAR · 1h | trend | 95.36 | -4.64 | 86 | 22.1 | 2.00 | 0.44 | -21.52 | 289 |
| 32 | EMA 20/50 cross · 1h | trend | 95.34 | -4.66 | 45 | 15.6 | 4.95 | 0.76 | -23.71 | 136 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.86 | -3.80 | -8.72 | 230 |
| 34 | Supertrend · 1h | trend | 94.56 | -5.44 | 58 | 13.8 | 1.32 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.16 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.50 | -6.50 | 39 | 23.1 | 15.62 | 2.46 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.45 | -6.55 | 151 | 32.5 | -7.88 | -1.18 | -16.91 | 130 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.27 | -2.76 | -6.49 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.62 | -7.38 | 66 | 15.2 | -0.63 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.52 | -7.48 | 115 | 43.5 | -18.87 | -6.23 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.50 | -7.50 | 439 | 17.8 | 1.19 | 0.35 | -12.73 | 392 |
| 42 | Volume breakout · 1h | breakout | 91.72 | -8.28 | 70 | 20.0 | 9.16 | 1.39 | -12.60 | 116 |
| 43 | RSI(14) reversion · 1h | reversion | 91.65 | -8.35 | 34 | 26.5 | 0.52 | 0.23 | -9.40 | 134 |
| 44 | Ichimoku · 1h | trend | 91.02 | -8.98 | 48 | 16.7 | 0.99 | 0.32 | -22.34 | 126 |
| 45 | Bollinger breakout · 1h | breakout | 90.87 | -9.13 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 46 | Triple EMA stack · 1h | trend | 90.72 | -9.28 | 71 | 15.5 | -7.21 | -0.63 | -27.17 | 237 |
| 47 | Bollinger reversion · 1h | reversion | 90.53 | -9.47 | 88 | 35.2 | -23.88 | -5.78 | -24.43 | 320 |
| 48 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.70 | -16.08 | 569 |
| 49 | CCI reversion · 1h | reversion | 89.01 | -10.99 | 113 | 45.1 | -9.81 | -1.29 | -14.35 | 408 |
| 50 | Williams %R · 1h | reversion | 88.72 | -11.28 | 136 | 44.9 | -25.97 | -4.25 | -28.82 | 510 |
| 51 | OBV trend · 1h | momentum | 88.72 | -11.28 | 150 | 18.7 | -12.52 | -1.18 | -34.15 | 318 |
| 52 | VWAP momentum · 1h | momentum | 88.25 | -11.75 | 311 | 23.2 | -32.80 | -4.86 | -40.15 | 1250 |
| 53 | Max aggression: 5-day momentum | meta | 88.10 | -11.90 | 7 | 28.6 | -14.35 | -1.04 | -34.64 | 28 |
| 54 | Candlestick reversal · 1h | reversion | 88.02 | -11.98 | 130 | 30.8 | -27.92 | -5.32 | -28.40 | 494 |
| 55 | Heikin-Ashi · 1h | trend | 87.72 | -12.28 | 153 | 28.1 | -29.97 | -4.94 | -37.65 | 675 |
| 56 | Donchian 20/10 · 1h | breakout | 87.72 | -12.28 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 57 | MACD zero-line · 1h | trend | 87.60 | -12.40 | 67 | 17.9 | -21.01 | -3.89 | -21.53 | 232 |
| 58 | EMA 9/21 cross · 1h | trend | 87.11 | -12.89 | 108 | 13.0 | -8.23 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.29 | -5.03 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.65 | -13.35 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.58 | -13.42 | 153 | 17.0 | -48.14 | -22.95 | -48.26 | 587 |
| 62 | ROC + volume · 1h | momentum | 85.53 | -14.47 | 164 | 20.1 | -9.21 | -1.07 | -25.13 | 397 |
| 63 | ROC + volume | momentum | 72.92 | -27.09 | 421 | 22.3 | -72.68 | -16.17 | -74.72 | 1661 |
| 64 | Squeeze breakout | breakout | 69.52 | -30.48 | 354 | 15.5 | -62.19 | -17.94 | -62.19 | 1221 |
| 65 | Volume breakout | breakout | 69.45 | -30.55 | 279 | 14.7 | -61.51 | -17.37 | -61.51 | 891 |
| 66 | RSI(14) reversion | reversion | 68.73 | -31.27 | 430 | 27.0 | -73.85 | -17.23 | -74.03 | 1486 |
| 67 | EMA 20/50 cross | trend | 67.40 | -32.60 | 357 | 19.9 | -76.36 | -14.99 | -76.38 | 1431 |
| 68 | Donchian 55/20 | breakout | 66.53 | -33.47 | 360 | 17.5 | -68.17 | -14.24 | -69.15 | 1291 |
| 69 | VWAP reversion | reversion | 62.85 | -37.15 | 470 | 25.1 | -73.00 | -15.49 | -73.03 | 1419 |
| 70 | Supertrend | trend | 60.52 | -39.48 | 503 | 19.3 | -85.81 | -20.40 | -86.04 | 1893 |
| 71 | Keltner breakout | breakout | 60.41 | -39.59 | 485 | 14.6 | -83.19 | -26.67 | -83.24 | 1839 |
| 72 | AI bee: Boozy | ai | 60.28 | -39.72 | 262 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.09 | -42.91 | 436 | 9.9 | -82.16 | -22.71 | -82.16 | 1731 |
| 74 | AI bee: Bizzy | ai | 55.35 | -44.65 | 893 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 55.26 | -44.74 | 628 | 20.1 | -88.00 | -27.02 | -88.19 | 2119 |
| 76 | Z-score reversion | reversion | 54.68 | -45.32 | 576 | 22.2 | -86.29 | -22.37 | -86.48 | 2083 |
| 77 | ADX DI cross | trend | 53.65 | -46.35 | 600 | 10.0 | -89.04 | -33.21 | -89.12 | 2106 |
| 78 | Donchian 20/10 | breakout | 52.30 | -47.70 | 684 | 17.5 | -90.74 | -25.25 | -90.84 | 2644 |
| 79 | MACD zero-line | trend | 51.23 | -48.77 | 635 | 14.5 | -91.41 | -29.07 | -91.48 | 2348 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.56 | -29.48 | -98.59 | 5311 |
| 81 | Trend pullback | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.12 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.12 | -29.27 | -93.13 | 2591 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.37 | -24.80 | -90.45 | 2361 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.32 | -31.99 | -97.35 | 3518 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -34.72 | -96.33 | 3575 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -25.33 | -94.35 | 2634 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.88 | -99.38 | 5637 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -30.70 | -96.29 | 3591 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.80 | -99.73 | 6141 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.26 | -36.65 | -97.26 | 3646 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.90 | -98.55 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.33 | -31.90 | -93.36 | 2792 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -38.74 | -99.55 | 6113 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.07 | -32.52 | -96.09 | 3735 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.78 | -33.84 | -95.81 | 4050 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.88 | -43.85 | -99.89 | 8199 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-13T02:25 | Donchian 55/20 | buy | XRP-USD | 16.66 | — | entry signal |
| 2026-10-13T02:25 | Donchian 55/20 | buy | BTC-USD | 16.66 | — | entry signal |
| 2026-10-13T02:22 | Keltner breakout | buy | SOL-USD | 3.01 | — | rebalance up |
| 2026-10-13T02:22 | Keltner breakout | sell | XRP-USD | 3.01 | -0.01 | rebalance down |
| 2026-10-13T02:20 | AI bee: Boozy | buy | ETH-USD | 14.16 | — | Jev: buy (buy p=0.78) |
| 2026-10-13T02:20 | AI bee: Bizzy | buy | SOL-USD | 8.17 | — | Jev: buy (buy p=0.59) |
| 2026-10-13T02:20 | Keltner breakout | buy | SOL-USD | 3.08 | — | entry signal |
| 2026-10-13T02:20 | Keltner breakout | sell | BTC-USD | 3.08 | 0.01 | rebalance down |
| 2026-10-13T02:18 | AI bee: Bizzy | buy | ETH-USD | 7.94 | — | Jev: buy (buy p=0.57) |
| 2026-10-13T02:15 | Keltner breakout | buy | ETH-USD | 15.06 | — | entry signal |
| 2026-10-13T02:15 | Keltner breakout | buy | DOGE-USD | 15.09 | — | entry signal |
| 2026-10-13T02:15 | MACD zero-line | buy | SOL-USD | 2.55 | — | rebalance up |
| 2026-10-13T02:15 | MACD zero-line | sell | ETH-USD | 2.55 | 0.00 | rebalance down |
| 2026-10-13T02:15 | EMA 20/50 cross | buy | XRP-USD | 16.86 | — | entry signal |
| 2026-10-13T02:15 | EMA 20/50 cross | buy | BTC-USD | 16.86 | — | entry signal |
| 2026-10-13T02:10 | ADX DI cross | buy | SOL-USD | 5.38 | — | entry signal |
| 2026-10-13T02:10 | ADX DI cross | sell | XRP-USD | 2.72 | 0.00 | rebalance down |
| 2026-10-13T02:10 | ADX DI cross | sell | BTC-USD | 2.66 | -0.01 | rebalance down |
| 2026-10-13T02:07 | Donchian 20/10 | buy | SOL-USD | 2.59 | — | rebalance up |
| 2026-10-13T02:07 | Donchian 20/10 | sell | BTC-USD | 2.59 | -0.00 | rebalance down |
| 2026-10-13T02:05 | MFI reversion | sell | SOL-USD | 13.88 | 0.21 | exit signal |
| 2026-10-13T02:05 | MFI reversion | sell | DOGE-USD | 13.83 | 0.13 | exit signal |
| 2026-10-13T02:05 | Z-score reversion | sell | SOL-USD | 13.73 | 0.14 | exit signal |
| 2026-10-13T02:05 | Keltner breakout | buy | XRP-USD | 15.08 | — | entry signal |
| 2026-10-13T02:05 | Donchian 20/10 | buy | SOL-USD | 5.24 | — | entry signal |
| 2026-10-13T02:05 | Donchian 20/10 | sell | XRP-USD | 2.61 | 0.00 | rebalance down |
| 2026-10-13T02:05 | Donchian 20/10 | sell | DOGE-USD | 2.60 | -0.00 | rebalance down |
| 2026-10-13T02:05 | MACD zero-line | buy | SOL-USD | 5.12 | — | entry signal |
| 2026-10-13T02:05 | MACD zero-line | sell | XRP-USD | 2.55 | -0.00 | rebalance down |
| 2026-10-13T02:05 | MACD zero-line | sell | BTC-USD | 2.55 | -0.01 | rebalance down |
| 2026-10-13T02:00 | CCI reversion · 1h | buy | BTC-USD | 3.61 | — | entry signal |
| 2026-10-13T02:00 | Williams %R · 1h | buy | SOL-USD | 10.13 | — | entry signal |
| 2026-10-13T02:00 | Williams %R · 1h | buy | ETH-USD | 12.64 | — | entry signal |
| 2026-10-13T02:00 | Williams %R · 1h | buy | DOGE-USD | 12.64 | — | entry signal |
| 2026-10-13T02:00 | Williams %R · 1h | buy | BTC-USD | 12.64 | — | entry signal |
| 2026-10-13T02:00 | Z-score reversion · 1h | buy | ETH-USD | 1.63 | — | entry signal |
| 2026-10-13T02:00 | Z-score reversion · 1h | buy | BTC-USD | 8.79 | — | entry signal |
| 2026-10-13T02:00 | Bollinger reversion · 1h | buy | SOL-USD | 7.09 | — | entry signal |
| 2026-10-13T02:00 | Bollinger reversion · 1h | buy | ETH-USD | 10.04 | — | entry signal |
| 2026-10-13T02:00 | Bollinger reversion · 1h | buy | DOGE-USD | 10.04 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-15 02:25:05.000174+00:00 -> 2026-10-13 02:35:05.000174+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
