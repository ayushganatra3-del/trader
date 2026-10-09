# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T20:55:05.000160+00:00 · 17124 ticks

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

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.54 · VIX 14.79 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 36303 decisions in 2946 calls, $0.4484 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T20:55 | 1 / 3 / 1 | XRP-USD 14%, NANC 16%, COIN 14% |  |
| Breezy | 2026-10-09T20:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T20:55 | 4 / 1 / 0 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |
| VWAP reversion · 1h | DOGE-USD | 1.78 | +2.31% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.26 | 3.27 | 37 | 43.2 | -7.16 | -2.15 | -13.79 | 120 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.53 | 2.53 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.20 | 2.20 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.01 | 2.01 | 14 | 57.1 | -12.05 | -1.91 | -21.08 | 72 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.43 | 1.43 | 0 | — | 1.98 | 0.95 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.24 | 1.25 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.09 | 1.09 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.75 | -0.25 | 10 | 30.0 | -15.50 | -0.55 | -37.31 | 43 |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 5.16 | 2.42 | -1.52 | 90 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 99.53 | -0.47 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 99.28 | -0.72 | 27 | 14.8 | 13.30 | 1.66 | -16.96 | 109 |
| 18 | Stochastic reversion · 1h | reversion | 99.13 | -0.87 | 88 | 55.7 | -10.86 | -2.11 | -14.99 | 342 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 20 | Daily: SMA 20/50 cross · AAPL | daily | 98.59 | -1.41 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 21 | Copy: Cathie Wood (ARKK) | copy | 98.56 | -1.44 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 22 | Hold BTC | benchmark | 98.50 | -1.50 | 0 | — | 26.46 | 3.19 | -8.68 | 1 |
| 23 | Daily: Bullish score | daily | 97.80 | -2.21 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.60 | -2.40 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Trend pullback · 1h | trend | 97.04 | -2.96 | 78 | 23.1 | -22.69 | -6.37 | -25.39 | 170 |
| 26 | Z-score reversion · 1h | reversion | 97.03 | -2.97 | 38 | 42.1 | 0.15 | 0.16 | -8.60 | 165 |
| 27 | EMA 20/50 cross · 1h | trend | 96.81 | -3.19 | 38 | 13.2 | 4.50 | 0.71 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | 2.65 | 0.73 | -8.65 | 255 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.30 | -3.70 | 58 | 20.7 | -1.97 | -0.14 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.26 | -3.74 | 82 | 22.0 | -2.84 | -0.21 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.61 | -4.39 | 108 | 23.1 | -17.12 | -2.80 | -18.57 | 474 |
| 34 | Supertrend · 1h | trend | 94.83 | -5.17 | 52 | 13.5 | -0.43 | 0.14 | -18.22 | 210 |
| 35 | Squeeze breakout · 1h | breakout | 94.25 | -5.75 | 35 | 25.7 | 24.23 | 3.30 | -8.62 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 7.72 | 1.98 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.48 | -6.51 | 119 | 34.5 | -13.05 | -2.19 | -17.79 | 130 |
| 39 | RSI(14) reversion · 1h | reversion | 93.08 | -6.92 | 26 | 26.9 | -3.09 | -0.57 | -9.03 | 153 |
| 40 | Connors RSI(2) · 1h | reversion | 93.01 | -6.99 | 113 | 43.4 | -18.28 | -6.06 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 92.99 | -7.01 | 41 | 19.5 | -0.38 | 0.16 | -19.98 | 120 |
| 42 | Agent (ML meta-label) | meta | 92.81 | -7.19 | 392 | 18.4 | -5.68 | -0.91 | -13.02 | 428 |
| 43 | Bollinger reversion · 1h | reversion | 92.75 | -7.25 | 73 | 37.0 | -20.91 | -5.00 | -23.75 | 318 |
| 44 | RSI momentum · 1h | momentum | 92.65 | -7.35 | 64 | 15.6 | 3.76 | 0.66 | -17.07 | 221 |
| 45 | Volume breakout · 1h | breakout | 92.55 | -7.45 | 56 | 19.6 | 8.31 | 1.28 | -12.60 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 91.94 | -8.06 | 67 | 29.9 | 6.65 | 1.02 | -12.90 | 284 |
| 47 | Williams %R · 1h | reversion | 91.60 | -8.40 | 116 | 48.3 | -25.19 | -4.34 | -27.32 | 512 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.67 | -9.33 | 69 | 15.9 | -8.63 | -0.86 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.08 | -9.93 | 114 | 30.7 | -28.73 | -5.66 | -30.41 | 522 |
| 51 | VWAP momentum · 1h | momentum | 89.59 | -10.41 | 277 | 22.0 | -35.57 | -5.40 | -39.46 | 1276 |
| 52 | CCI reversion · 1h | reversion | 89.57 | -10.43 | 96 | 43.8 | -9.41 | -1.24 | -14.35 | 418 |
| 53 | MACD zero-line · 1h | trend | 89.40 | -10.60 | 60 | 20.0 | -6.60 | -0.71 | -19.41 | 239 |
| 54 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.22 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.12 | -10.88 | 128 | 19.5 | -47.86 | -23.27 | -48.05 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.78 | -11.22 | 58 | 19.0 | 0.02 | 0.21 | -17.72 | 219 |
| 57 | OBV trend · 1h | momentum | 88.72 | -11.28 | 149 | 18.8 | -12.38 | -1.40 | -28.83 | 320 |
| 58 | Heikin-Ashi · 1h | trend | 88.61 | -11.39 | 138 | 25.4 | -31.76 | -5.37 | -36.59 | 703 |
| 59 | Max aggression: 5-day momentum | meta | 87.92 | -12.08 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 60 | EMA 9/21 cross · 1h | trend | 87.74 | -12.26 | 101 | 13.9 | -10.08 | -1.17 | -21.49 | 337 |
| 61 | Keltner breakout · 1h | breakout | 87.05 | -12.95 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.22 | -13.78 | 132 | 21.2 | -9.89 | -1.19 | -23.20 | 412 |
| 63 | RSI(14) reversion | reversion | 75.54 | -24.46 | 350 | 29.1 | -73.20 | -18.52 | -73.38 | 1504 |
| 64 | ROC + volume | momentum | 74.91 | -25.09 | 388 | 22.7 | -73.41 | -17.08 | -74.27 | 1668 |
| 65 | Squeeze breakout | breakout | 73.91 | -26.09 | 299 | 15.7 | -61.58 | -18.17 | -61.67 | 1216 |
| 66 | Donchian 55/20 | breakout | 72.55 | -27.45 | 310 | 18.4 | -68.04 | -14.52 | -68.48 | 1297 |
| 67 | EMA 20/50 cross | trend | 71.97 | -28.03 | 307 | 20.5 | -77.57 | -15.53 | -77.72 | 1464 |
| 68 | Volume breakout | breakout | 71.54 | -28.46 | 248 | 13.7 | -63.40 | -18.27 | -63.65 | 901 |
| 69 | VWAP reversion | reversion | 68.32 | -31.68 | 393 | 26.2 | -72.13 | -16.45 | -72.42 | 1454 |
| 70 | Supertrend | trend | 66.07 | -33.94 | 434 | 20.5 | -86.70 | -21.49 | -86.71 | 1931 |
| 71 | Keltner breakout | breakout | 65.43 | -34.57 | 420 | 15.0 | -84.15 | -27.76 | -84.45 | 1858 |
| 72 | Ichimoku | trend | 62.41 | -37.59 | 383 | 10.2 | -81.75 | -23.47 | -81.87 | 1749 |
| 73 | AI bee: Bizzy | ai | 61.92 | -38.08 | 756 | 9.7 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.49 | -38.51 | 480 | 23.8 | -85.89 | -23.70 | -85.90 | 2103 |
| 75 | MFI reversion | reversion | 61.33 | -38.67 | 486 | 22.0 | -88.03 | -28.97 | -88.03 | 2118 |
| 76 | AI bee: Boozy | ai | 61.26 | -38.74 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.24 | -40.76 | 591 | 19.0 | -90.81 | -26.11 | -90.91 | 2661 |
| 78 | Trend pullback | trend | 59.09 | -40.91 | 537 | 16.0 | -90.42 | -27.21 | -90.52 | 2298 |
| 79 | ADX DI cross | trend | 58.65 | -41.35 | 518 | 10.4 | -89.82 | -35.00 | -89.82 | 2143 |
| 80 | RSI momentum | momentum | 58.16 | -41.84 | 558 | 17.9 | -90.28 | -25.69 | -90.35 | 2376 |
| 81 | MACD zero-line | trend | 57.63 | -42.38 | 541 | 15.7 | -91.54 | -29.91 | -91.54 | 2362 |
| 82 | Triple EMA stack | trend | 56.97 | -43.03 | 578 | 16.3 | -93.13 | -30.50 | -93.14 | 2611 |
| 83 | Bollinger breakout | breakout | 54.68 | -45.32 | 617 | 15.1 | -93.53 | -33.16 | -93.54 | 2816 |
| 84 | Consensus | meta | 52.91 | -47.09 | 586 | 10.4 | -94.22 | -25.78 | -94.24 | 2681 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -30.64 | -98.71 | 5392 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.21 | -97.36 | 3541 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -36.60 | -96.40 | 3584 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.35 | -99.36 | 5708 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.28 | -32.20 | -96.28 | 3604 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.56 | -99.73 | 6203 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.33 | -38.71 | -97.33 | 3676 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.53 | -98.50 | 4727 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.96 | -99.53 | 6160 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -34.15 | -95.93 | 3753 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -35.20 | -95.69 | 4097 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.08 | -99.90 | 8336 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T20:54 | AI bee: Bizzy | buy | XRP-USD | 8.86 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T20:35 | MACD zero-line | buy | DOGE-USD | 14.41 | — | entry signal |
| 2026-10-09T20:32 | AI bee: Bizzy | sell | DOGE-USD | 8.82 | -0.08 | Jev: sell (sell p=0.84) after 10 min |
| 2026-10-09T20:30 | ADX DI cross | sell | BTC-USD | 14.59 | -0.09 | exit signal |
| 2026-10-09T20:29 | AI bee: Bizzy | sell | SOL-USD | 8.73 | -0.06 | Jev: sell (sell p=0.81) after 10 min |
| 2026-10-09T20:25 | ADX DI cross | buy | BTC-USD | 14.68 | — | entry signal |
| 2026-10-09T20:22 | AI bee: Bizzy | buy | DOGE-USD | 8.90 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T20:20 | VWAP reversion | sell | XRP-USD | 17.13 | -0.05 | exit signal |
| 2026-10-09T20:20 | Z-score reversion | sell | DOGE-USD | 15.36 | -0.03 | exit signal |
| 2026-10-09T20:20 | RSI momentum | buy | XRP-USD | 14.55 | — | entry signal |
| 2026-10-09T20:20 | Supertrend | buy | DOGE-USD | 16.53 | — | entry signal |
| 2026-10-09T20:20 | MACD zero-line | buy | XRP-USD | 14.43 | — | entry signal |
| 2026-10-09T20:20 | Triple EMA stack | buy | XRP-USD | 14.26 | — | entry signal |
| 2026-10-09T20:20 | EMA 20/50 cross | buy | XRP-USD | 18.01 | — | entry signal |
| 2026-10-09T20:19 | AI bee: Bizzy | buy | SOL-USD | 8.79 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T20:10 | Z-score reversion | buy | SOL-USD | 15.37 | — | entry signal |
| 2026-10-09T20:00 | MACD zero-line · 1h | sell | BTC-USD | 22.38 | -0.20 | exit signal |
| 2026-10-09T20:00 | MACD cross · 1h | sell | BTC-USD | 6.77 | 0.00 | exit signal |
| 2026-10-09T19:56 | AI bee: Bizzy | sell | AMZN | 9.55 | -0.01 | Jev: sell (sell p=0.60) after 18 min |
| 2026-10-09T19:55 | Agent (rotation) | sell | SQQQ | 32.26 | 0.03 | selected signal exited |
| 2026-10-09T19:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.76 | -0.08 | target is flat |
| 2026-10-09T19:55 | Day trade: Stocks in Play ORB | sell | PLTR | 25.28 | 0.53 | target is flat |
| 2026-10-09T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 99.05 | -0.21 | target is flat |
| 2026-10-09T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 99.58 | 0.11 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | PLTR | 13.30 | 0.23 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | MSFT | 13.20 | -0.02 | target is flat |
| 2026-10-09T19:55 | Consensus | sell | AMZN | 13.22 | 0.04 | target is flat |
| 2026-10-09T19:55 | MFI reversion · 1h | buy | TSLA | 18.73 | — | entry |
| 2026-10-09T19:55 | MFI reversion · 1h | sell | COIN | 19.02 | 0.57 | target is flat |
| 2026-10-09T19:55 | Candlestick reversal · 1h | buy | QQQ | 10.00 | — | entry |
| 2026-10-09T19:55 | VWAP momentum · 1h | buy | TSLA | 6.41 | — | entry |
| 2026-10-09T19:55 | MFI reversion | sell | META | 12.29 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | MFI reversion | sell | LABU | 12.27 | -0.08 | end-of-day flatten |
| 2026-10-09T19:55 | MFI reversion | sell | GOOGL | 12.27 | -0.02 | end-of-day flatten |
| 2026-10-09T19:55 | VWAP reversion | sell | NVDA | 17.08 | -0.04 | end-of-day flatten |
| 2026-10-09T19:55 | Z-score reversion | buy | ETH-USD | 3.08 | — | rebalance up |
| 2026-10-09T19:55 | Z-score reversion | buy | DOGE-USD | 15.39 | — | entry signal |
| 2026-10-09T19:55 | Z-score reversion | buy | BTC-USD | 3.08 | — | rebalance up |
| 2026-10-09T19:55 | Z-score reversion | sell | MSTR | 12.32 | -0.01 | end-of-day flatten |
| 2026-10-09T19:55 | Z-score reversion | sell | META | 12.29 | -0.02 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 20:55:05.000160+00:00 -> 2026-10-09 21:05:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
