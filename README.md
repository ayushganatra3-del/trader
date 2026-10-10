# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-10T00:25:05.000126+00:00 · 17289 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-09 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GGR 12%, COE 12%, GME 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 375 decisions in 75 calls, $0.0053 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-10T00:25 | 0 / 3 / 2 | DOGE-USD 19%, NANC 16%, COIN 14% |  |
| Breezy | 2026-10-10T00:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-10T00:25 | 2 / 3 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| Z-score reversion | TNA | 1.94 | +3.40% | 7 |
| Keltner breakout | LABU | 1.94 | +8.17% | 7 |
| Bollinger reversion | TECL | 1.82 | +2.00% | 8 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.73 | -2.36 | -13.79 | 119 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -12.05 | -1.91 | -21.08 | 72 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.42 | -1.52 | 90 |
| 17 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.30 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.18 | -0.82 | 88 | 55.7 | -10.91 | -2.12 | -14.99 | 345 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Hold BTC | benchmark | 98.70 | -1.30 | 0 | — | 26.95 | 3.24 | -8.68 | 1 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.65 | -1.35 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.85 | -2.15 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.24 | -2.76 | 39 | 43.6 | 1.52 | 0.43 | -8.60 | 162 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 27 | EMA 20/50 cross · 1h | trend | 96.85 | -3.15 | 38 | 13.2 | 4.57 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 1.18 | 0.39 | -8.88 | 252 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.49 | -0.07 | -13.84 | 255 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.78 | -4.22 | 108 | 23.1 | -16.12 | -2.61 | -17.97 | 471 |
| 34 | Supertrend · 1h | trend | 95.05 | -4.95 | 52 | 13.5 | -0.30 | 0.15 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.26 | -5.74 | 35 | 25.7 | 24.23 | 3.30 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -5.06 | -2.32 | -6.77 | 108 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.72 | 1.98 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -12.45 | -1.97 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -3.68 | -0.70 | -9.03 | 154 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.00 | -7.00 | 41 | 19.5 | -0.57 | 0.13 | -19.98 | 121 |
| 42 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -5.21 | -0.78 | -13.67 | 410 |
| 43 | Bollinger reversion · 1h | reversion | 92.79 | -7.21 | 73 | 37.0 | -20.93 | -5.01 | -23.75 | 319 |
| 44 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 3.62 | 0.64 | -17.07 | 221 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.31 | 1.28 | -12.60 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 91.98 | -8.02 | 67 | 29.9 | 6.65 | 1.02 | -12.90 | 284 |
| 47 | Williams %R · 1h | reversion | 91.76 | -8.24 | 116 | 48.3 | -25.14 | -4.33 | -27.32 | 514 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.27 | -0.94 | -26.38 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.20 | -9.80 | 114 | 30.7 | -28.82 | -5.69 | -30.55 | 525 |
| 51 | CCI reversion · 1h | reversion | 89.72 | -10.28 | 97 | 44.3 | -9.31 | -1.22 | -14.35 | 418 |
| 52 | VWAP momentum · 1h | momentum | 89.70 | -10.30 | 277 | 22.0 | -35.56 | -5.39 | -39.28 | 1281 |
| 53 | MACD zero-line · 1h | trend | 89.43 | -10.57 | 60 | 20.0 | -6.29 | -0.66 | -19.41 | 238 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 55 | Three white soldiers | momentum | 88.98 | -11.02 | 128 | 19.5 | -47.79 | -23.28 | -47.90 | 587 |
| 56 | Donchian 20/10 · 1h | breakout | 88.83 | -11.17 | 58 | 19.0 | 0.02 | 0.21 | -17.72 | 219 |
| 57 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.38 | -1.41 | -28.47 | 318 |
| 58 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -31.86 | -5.39 | -36.60 | 704 |
| 59 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.80 | -12.20 | 101 | 13.9 | -9.54 | -1.09 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.55 | -1.33 | -25.35 | 215 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -10.44 | -1.27 | -23.88 | 413 |
| 63 | RSI(14) reversion | reversion | 75.51 | -24.49 | 352 | 29.0 | -73.17 | -18.44 | -73.33 | 1503 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.11 | -16.77 | -73.99 | 1669 |
| 65 | Squeeze breakout | breakout | 73.73 | -26.27 | 300 | 15.7 | -61.63 | -18.22 | -61.66 | 1218 |
| 66 | Donchian 55/20 | breakout | 72.64 | -27.36 | 310 | 18.4 | -68.01 | -14.50 | -68.48 | 1300 |
| 67 | EMA 20/50 cross | trend | 72.03 | -27.97 | 308 | 20.5 | -77.48 | -15.51 | -77.60 | 1466 |
| 68 | Volume breakout | breakout | 71.52 | -28.48 | 248 | 13.7 | -63.44 | -18.27 | -63.59 | 904 |
| 69 | VWAP reversion | reversion | 68.30 | -31.70 | 394 | 26.1 | -71.72 | -16.13 | -71.97 | 1439 |
| 70 | Supertrend | trend | 66.26 | -33.74 | 434 | 20.5 | -86.56 | -21.35 | -86.60 | 1930 |
| 71 | Keltner breakout | breakout | 65.18 | -34.81 | 422 | 14.9 | -84.24 | -27.88 | -84.47 | 1863 |
| 72 | Ichimoku | trend | 62.27 | -37.73 | 384 | 10.2 | -81.81 | -23.53 | -81.88 | 1751 |
| 73 | AI bee: Bizzy | ai | 61.47 | -38.53 | 765 | 9.5 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.41 | -38.59 | 483 | 23.6 | -85.75 | -23.56 | -85.75 | 2096 |
| 75 | MFI reversion | reversion | 61.33 | -38.66 | 486 | 22.0 | -87.83 | -28.81 | -87.84 | 2136 |
| 76 | AI bee: Boozy | ai | 61.16 | -38.84 | 247 | 5.3 | — | — | — | — |
| 77 | Trend pullback | trend | 59.11 | -40.89 | 537 | 16.0 | -90.40 | -27.15 | -90.50 | 2299 |
| 78 | Donchian 20/10 | breakout | 58.86 | -41.14 | 595 | 18.8 | -90.84 | -26.21 | -90.87 | 2666 |
| 79 | ADX DI cross | trend | 58.69 | -41.31 | 518 | 10.4 | -89.71 | -34.83 | -89.72 | 2139 |
| 80 | RSI momentum | momentum | 57.94 | -42.06 | 561 | 17.8 | -90.30 | -25.72 | -90.32 | 2380 |
| 81 | MACD zero-line | trend | 57.26 | -42.74 | 547 | 15.7 | -91.59 | -29.88 | -91.59 | 2365 |
| 82 | Triple EMA stack | trend | 57.01 | -42.99 | 579 | 16.2 | -93.14 | -30.50 | -93.16 | 2616 |
| 83 | Bollinger breakout | breakout | 54.42 | -45.58 | 620 | 15.0 | -93.54 | -33.27 | -93.54 | 2819 |
| 84 | Consensus | meta | 52.87 | -47.13 | 586 | 10.4 | -94.18 | -25.74 | -94.19 | 2682 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.60 | -98.68 | 5390 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.24 | -97.36 | 3545 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.45 | -36.85 | -96.45 | 3605 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -37.02 | -99.35 | 5696 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -32.11 | -96.25 | 3597 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.58 | -99.73 | 6207 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -38.82 | -97.34 | 3681 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.54 | -98.50 | 4726 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.61 | -99.52 | 6159 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -33.68 | -95.86 | 3743 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.60 | -34.46 | -95.60 | 4085 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.92 | -99.90 | 8344 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-10T00:25 | AI bee: Bizzy | sell | XRP-USD | 8.96 | -0.04 | Jev: sell (sell p=0.55) after 10 min |
| 2026-10-10T00:25 | Donchian 20/10 | buy | BTC-USD | 2.95 | — | rebalance up |
| 2026-10-10T00:24 | AI bee: Bizzy | buy | DOGE-USD | 11.56 | — | Jev: buy (buy p=0.75) |
| 2026-10-10T00:20 | Three white soldiers | buy | SOL-USD | 22.28 | — | entry signal |
| 2026-10-10T00:20 | Three white soldiers | buy | ETH-USD | 22.28 | — | entry signal |
| 2026-10-10T00:20 | EMA 20/50 cross | buy | SOL-USD | 7.21 | — | entry signal |
| 2026-10-10T00:15 | AI bee: Bizzy | buy | XRP-USD | 9.00 | — | Jev: buy (buy p=0.58) |
| 2026-10-10T00:15 | Consensus | buy | XRP-USD | 13.23 | — | entry |
| 2026-10-10T00:15 | Consensus | buy | DOGE-USD | 13.23 | — | entry |
| 2026-10-10T00:15 | Volume breakout | buy | DOGE-USD | 17.89 | — | entry signal |
| 2026-10-10T00:15 | Squeeze breakout | buy | XRP-USD | 18.45 | — | entry signal |
| 2026-10-10T00:15 | Squeeze breakout | buy | DOGE-USD | 18.45 | — | entry signal |
| 2026-10-10T00:15 | Keltner breakout | buy | XRP-USD | 16.31 | — | entry signal |
| 2026-10-10T00:15 | Keltner breakout | buy | DOGE-USD | 16.31 | — | entry signal |
| 2026-10-10T00:15 | Bollinger breakout | buy | DOGE-USD | 13.60 | — | entry signal |
| 2026-10-10T00:15 | Trend pullback | buy | BTC-USD | 14.78 | — | entry signal |
| 2026-10-10T00:11 | MFI reversion | buy | DOGE-USD | 15.33 | — | entry signal |
| 2026-10-10T00:11 | VWAP reversion | sell | SOL-USD | 17.04 | -0.05 | exit signal |
| 2026-10-10T00:11 | Bollinger breakout | buy | XRP-USD | 13.61 | — | entry signal |
| 2026-10-10T00:05 | Donchian 20/10 | sell | SOL-USD | 11.70 | -0.11 | exit signal |
| 2026-10-10T00:05 | Donchian 20/10 | sell | ETH-USD | 11.72 | -0.09 | exit signal |
| 2026-10-10T00:05 | RSI momentum | buy | BTC-USD | 2.89 | — | rebalance up |
| 2026-10-10T00:05 | RSI momentum | sell | SOL-USD | 8.75 | -0.08 | stop-loss |
| 2026-10-10T00:05 | Ichimoku | sell | SOL-USD | 15.47 | -0.14 | exit signal |
| 2026-10-10T00:05 | Triple EMA stack | buy | DOGE-USD | 2.85 | — | rebalance up |
| 2026-10-10T00:05 | Triple EMA stack | sell | SOL-USD | 5.71 | -0.05 | stop-loss |
| 2026-10-10T00:05 | EMA 20/50 cross | sell | SOL-USD | 7.21 | -0.06 | exit signal |
| 2026-10-10T00:03 | AI bee: Bizzy | sell | DOGE-USD | 8.47 | -0.06 | Jev: sell (sell p=0.89) after 11 min |
| 2026-10-10T00:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.75 | — | entry signal |
| 2026-10-10T00:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 5.75 | -0.05 | rebalance down |
| 2026-10-10T00:00 | Keltner breakout | sell | ETH-USD | 16.22 | -0.11 | exit signal |
| 2026-10-10T00:00 | MACD zero-line | sell | SOL-USD | 14.23 | -0.11 | exit signal |
| 2026-10-09T23:55 | Squeeze breakout | sell | ETH-USD | 18.36 | -0.12 | exit signal |
| 2026-10-09T23:55 | Bollinger breakout | sell | ETH-USD | 13.56 | -0.07 | exit signal |
| 2026-10-09T23:54 | AI bee: Bizzy | sell | XRP-USD | 9.53 | -0.05 | Jev: sell (sell p=0.55) after 10 min |
| 2026-10-09T23:52 | AI bee: Bizzy | buy | DOGE-USD | 8.52 | — | Jev: buy (buy p=0.55) |
| 2026-10-09T23:50 | Triple EMA stack | buy | SOL-USD | 5.76 | — | entry signal |
| 2026-10-09T23:50 | Triple EMA stack | sell | XRP-USD | 2.88 | -0.00 | rebalance down |
| 2026-10-09T23:50 | Triple EMA stack | sell | DOGE-USD | 2.88 | -0.00 | rebalance down |
| 2026-10-09T23:44 | AI bee: Bizzy | buy | XRP-USD | 9.58 | — | Jev: buy (buy p=0.62) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-12 00:25:05.000126+00:00 -> 2026-10-10 00:35:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
