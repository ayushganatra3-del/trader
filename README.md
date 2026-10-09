# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T18:29:05.000164+00:00 · 17005 ticks

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

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 28809 decisions in 2589 calls, $0.3592 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T18:29 | 1 / 14 / 14 | TECL 15%, NANC 15% |  |
| Breezy | 2026-10-09T18:29 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-09T18:29 | 0 / 27 / 2 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| MFI reversion | IWM | 1.99 | +0.92% | 5 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -7.73 | -2.36 | -13.79 | 119 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.69 | 2.69 | 0 | — | -3.97 | -0.63 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.18 | 2.18 | 0 | — | -3.63 | -1.49 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.46 | 1.46 | 0 | — | 1.95 | 0.94 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.51 | 0.35 | -3.66 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 101.17 | 1.17 | 0 | — | -0.82 | -0.42 | -5.09 | 1 |
| 9 | Copy: Insider buying | copy | 101.05 | 1.04 | 14 | 57.1 | -12.97 | -2.14 | -21.08 | 72 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Max aggression: 1-day momentum | meta | 100.16 | 0.16 | 10 | 30.0 | -15.19 | -0.52 | -37.31 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.41 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 99.57 | -0.43 | 88 | 55.7 | -10.49 | -2.01 | -14.99 | 342 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.51 | -0.49 | 9 | 22.2 | 3.25 | 1.04 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.28 | -0.72 | 35 | 37.1 | 4.77 | 2.25 | -1.52 | 90 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 98.86 | -1.14 | 0 | — | 11.81 | 1.91 | -8.33 | 1 |
| 20 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 27 | 14.8 | 12.76 | 1.60 | -16.96 | 109 |
| 21 | Hold BTC | benchmark | 98.63 | -1.37 | 0 | — | 26.57 | 3.20 | -8.68 | 1 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 98.45 | -1.55 | 0 | — | 1.46 | 0.63 | -5.18 | 1 |
| 23 | Daily: Bullish score | daily | 97.71 | -2.29 | 4 | 0.0 | 0.71 | 0.29 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.47 | -2.53 | 6 | 0.0 | -3.14 | -2.43 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.32 | -2.68 | 38 | 42.1 | 0.41 | 0.21 | -8.60 | 165 |
| 26 | Trend pullback · 1h | trend | 97.06 | -2.94 | 78 | 23.1 | -22.71 | -6.38 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.84 | -3.16 | 38 | 13.2 | 4.53 | 0.72 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 79 | 29.1 | 2.39 | 0.68 | -8.65 | 254 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.15 | -3.85 | 56 | 21.4 | -2.19 | -0.18 | -13.84 | 254 |
| 31 | Parabolic SAR · 1h | trend | 96.08 | -3.92 | 82 | 22.0 | -3.01 | -0.23 | -20.87 | 293 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 33 | MACD cross · 1h | trend | 95.76 | -4.24 | 107 | 22.4 | -16.82 | -2.74 | -18.37 | 473 |
| 34 | Supertrend · 1h | trend | 94.81 | -5.19 | 52 | 13.5 | -0.49 | 0.13 | -18.22 | 209 |
| 35 | Squeeze breakout · 1h | breakout | 94.25 | -5.75 | 35 | 25.7 | 24.22 | 3.29 | -8.61 | 105 |
| 36 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 37 | Gap and go | momentum | 93.89 | -6.11 | 56 | 10.7 | 7.70 | 1.98 | -6.64 | 200 |
| 38 | MFI reversion · 1h | reversion | 93.62 | -6.38 | 113 | 35.4 | -11.60 | -1.83 | -17.79 | 129 |
| 39 | RSI(14) reversion · 1h | reversion | 93.39 | -6.61 | 26 | 26.9 | -2.25 | -0.38 | -9.03 | 151 |
| 40 | Connors RSI(2) · 1h | reversion | 93.29 | -6.71 | 110 | 43.6 | -18.05 | -5.97 | -20.97 | 253 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 42 | Bollinger reversion · 1h | reversion | 93.07 | -6.93 | 73 | 37.0 | -20.63 | -4.90 | -23.75 | 318 |
| 43 | Agent (ML meta-label) | meta | 92.90 | -7.10 | 390 | 18.2 | -2.65 | -0.34 | -12.54 | 424 |
| 44 | RSI momentum · 1h | momentum | 92.53 | -7.47 | 63 | 15.9 | 3.55 | 0.63 | -17.07 | 219 |
| 45 | Volume breakout · 1h | breakout | 92.23 | -7.77 | 51 | 15.7 | 7.57 | 1.19 | -12.60 | 123 |
| 46 | Williams %R · 1h | reversion | 91.78 | -8.21 | 116 | 48.3 | -25.07 | -4.31 | -27.32 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.66 | -8.34 | 67 | 29.9 | 5.63 | 0.89 | -12.90 | 287 |
| 48 | Opening range 30m | breakout | 90.89 | -9.11 | 136 | 19.9 | -16.95 | -5.15 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.74 | -9.26 | 69 | 15.9 | -8.61 | -0.85 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.42 | -9.58 | 108 | 30.6 | -28.47 | -5.57 | -30.43 | 521 |
| 51 | CCI reversion · 1h | reversion | 89.86 | -10.14 | 94 | 42.6 | -9.16 | -1.19 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.73 | -10.28 | 272 | 22.1 | -35.48 | -5.38 | -39.46 | 1275 |
| 53 | MACD zero-line · 1h | trend | 89.49 | -10.51 | 59 | 20.3 | -6.53 | -0.70 | -19.40 | 238 |
| 54 | Three white soldiers | momentum | 89.09 | -10.91 | 126 | 19.0 | -47.89 | -23.32 | -48.05 | 586 |
| 55 | Opening range 15m | breakout | 89.03 | -10.97 | 159 | 18.2 | -18.53 | -5.28 | -19.78 | 700 |
| 56 | Donchian 20/10 · 1h | breakout | 88.70 | -11.30 | 57 | 19.3 | -1.06 | 0.08 | -17.72 | 222 |
| 57 | Heikin-Ashi · 1h | trend | 88.57 | -11.43 | 135 | 25.2 | -31.76 | -5.37 | -36.59 | 699 |
| 58 | OBV trend · 1h | momentum | 88.54 | -11.46 | 145 | 18.6 | -12.78 | -1.46 | -28.83 | 319 |
| 59 | EMA 9/21 cross · 1h | trend | 87.70 | -12.30 | 101 | 13.9 | -10.13 | -1.17 | -21.49 | 337 |
| 60 | Max aggression: 5-day momentum | meta | 86.67 | -13.33 | 7 | 28.6 | -15.58 | -1.19 | -34.64 | 28 |
| 61 | Keltner breakout · 1h | breakout | 86.67 | -13.33 | 43 | 18.6 | -11.88 | -1.38 | -25.35 | 215 |
| 62 | ROC + volume · 1h | momentum | 86.35 | -13.65 | 130 | 21.5 | -10.75 | -1.31 | -23.72 | 415 |
| 63 | RSI(14) reversion | reversion | 75.64 | -24.36 | 346 | 28.9 | -73.28 | -18.57 | -73.48 | 1502 |
| 64 | ROC + volume | momentum | 75.13 | -24.87 | 383 | 22.7 | -73.45 | -17.16 | -74.32 | 1668 |
| 65 | Squeeze breakout | breakout | 74.02 | -25.98 | 288 | 15.3 | -61.70 | -18.26 | -61.87 | 1215 |
| 66 | Donchian 55/20 | breakout | 72.60 | -27.40 | 298 | 17.1 | -68.02 | -14.51 | -68.48 | 1295 |
| 67 | EMA 20/50 cross | trend | 72.07 | -27.93 | 296 | 19.3 | -77.51 | -15.50 | -77.69 | 1461 |
| 68 | Volume breakout | breakout | 71.54 | -28.46 | 242 | 13.6 | -63.40 | -18.21 | -63.52 | 904 |
| 69 | VWAP reversion | reversion | 68.85 | -31.15 | 386 | 26.2 | -72.01 | -16.35 | -72.45 | 1454 |
| 70 | Supertrend | trend | 66.27 | -33.73 | 429 | 20.0 | -86.66 | -21.44 | -86.70 | 1929 |
| 71 | Keltner breakout | breakout | 65.45 | -34.55 | 412 | 14.6 | -84.16 | -27.78 | -84.45 | 1854 |
| 72 | Ichimoku | trend | 62.45 | -37.55 | 374 | 9.4 | -81.75 | -23.47 | -81.87 | 1746 |
| 73 | AI bee: Bizzy | ai | 62.45 | -37.55 | 743 | 9.7 | — | — | — | — |
| 74 | Z-score reversion | reversion | 61.84 | -38.16 | 472 | 23.9 | -85.96 | -23.77 | -86.02 | 2099 |
| 75 | MFI reversion | reversion | 61.74 | -38.26 | 471 | 21.9 | -87.98 | -28.79 | -88.01 | 2131 |
| 76 | AI bee: Boozy | ai | 61.60 | -38.40 | 246 | 5.3 | — | — | — | — |
| 77 | Donchian 20/10 | breakout | 59.38 | -40.62 | 576 | 18.8 | -90.84 | -26.24 | -90.96 | 2661 |
| 78 | Trend pullback | trend | 59.17 | -40.83 | 527 | 15.9 | -90.44 | -27.25 | -90.55 | 2300 |
| 79 | ADX DI cross | trend | 58.86 | -41.14 | 512 | 10.2 | -89.82 | -35.23 | -89.83 | 2142 |
| 80 | RSI momentum | momentum | 58.37 | -41.63 | 541 | 17.4 | -90.24 | -25.61 | -90.35 | 2373 |
| 81 | MACD zero-line | trend | 57.93 | -42.07 | 534 | 15.7 | -91.51 | -29.95 | -91.52 | 2360 |
| 82 | Triple EMA stack | trend | 57.09 | -42.91 | 566 | 15.7 | -93.12 | -30.47 | -93.14 | 2608 |
| 83 | Bollinger breakout | breakout | 54.75 | -45.25 | 602 | 15.0 | -93.54 | -33.30 | -93.55 | 2815 |
| 84 | Consensus | meta | 52.83 | -47.17 | 575 | 10.1 | -94.28 | -26.00 | -94.29 | 2680 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -30.92 | -98.73 | 5398 |
| 86 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -33.36 | -97.36 | 3539 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -36.74 | -96.42 | 3582 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.45 | -99.36 | 5698 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.25 | -96.29 | 3599 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.76 | -99.73 | 6185 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -38.61 | -97.32 | 3665 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.60 | -98.50 | 4718 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.30 | -99.53 | 6157 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -34.29 | -95.93 | 3747 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -35.19 | -95.67 | 4089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.50 | -99.90 | 8323 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T18:25 | AI bee: Bizzy | buy | TECL | 9.42 | — | Jev: buy (buy p=0.60) |
| 2026-10-09T18:25 | Agent (ML meta-label) | buy | META | 3.32 | — | following Connors RSI(2) · 1h |
| 2026-10-09T18:25 | Agent (ML meta-label) | buy | LABU | 4.89 | — | entry |
| 2026-10-09T18:25 | Agent (ML meta-label) | sell | SQQQ | 8.21 | -0.08 | selected signal exited |
| 2026-10-09T18:25 | Consensus | buy | TSLA | 7.17 | — | rebalance up |
| 2026-10-09T18:25 | Consensus | sell | SPY | 8.80 | -0.01 | target is flat |
| 2026-10-09T18:25 | MFI reversion · 1h | sell | MSTR | 23.14 | -0.27 | target is flat |
| 2026-10-09T18:25 | Stochastic reversion · 1h | buy | SOXL | 5.00 | — | rebalance up |
| 2026-10-09T18:25 | Stochastic reversion · 1h | sell | AMD | 5.00 | -0.05 | rebalance down |
| 2026-10-09T18:25 | MFI reversion | buy | LABU | 8.82 | — | entry signal |
| 2026-10-09T18:25 | MFI reversion | sell | SPY | 8.82 | -0.01 | exit signal |
| 2026-10-09T18:25 | VWAP reversion | buy | TSLA | 3.47 | — | rebalance up |
| 2026-10-09T18:25 | VWAP reversion | sell | SOXL | 3.47 | 0.02 | rebalance down |
| 2026-10-09T18:25 | Three white soldiers | buy | AMD | 22.28 | — | entry signal |
| 2026-10-09T18:25 | Squeeze breakout | buy | AMD | 10.06 | — | entry signal |
| 2026-10-09T18:25 | Squeeze breakout | buy | AAPL | 10.58 | — | entry signal |
| 2026-10-09T18:25 | Squeeze breakout | sell | XRP-USD | 7.83 | -0.06 | rebalance down |
| 2026-10-09T18:25 | Squeeze breakout | sell | UPRO | 4.31 | 0.03 | rebalance down |
| 2026-10-09T18:25 | Squeeze breakout | sell | TNA | 4.21 | -0.01 | rebalance down |
| 2026-10-09T18:25 | Squeeze breakout | sell | TECL | 4.28 | 0.01 | rebalance down |
| 2026-10-09T18:25 | Keltner breakout | buy | TECL | 13.00 | — | entry signal |
| 2026-10-09T18:25 | Keltner breakout | sell | UPRO | 3.29 | 0.01 | rebalance down |
| 2026-10-09T18:25 | Keltner breakout | sell | TNA | 3.27 | -0.00 | rebalance down |
| 2026-10-09T18:25 | Bollinger breakout | buy | QQQ | 3.19 | — | entry signal |
| 2026-10-09T18:25 | Bollinger breakout | buy | AMD | 4.56 | — | entry signal |
| 2026-10-09T18:25 | Bollinger breakout | sell | TNA | 2.81 | -0.00 | rebalance down |
| 2026-10-09T18:25 | Donchian 55/20 | buy | TECL | 7.26 | — | entry signal |
| 2026-10-09T18:25 | Donchian 55/20 | buy | QQQ | 7.26 | — | entry signal |
| 2026-10-09T18:25 | Donchian 55/20 | sell | COIN | 7.27 | 0.17 | exit signal |
| 2026-10-09T18:25 | Donchian 20/10 | buy | QQQ | 2.13 | — | entry signal |
| 2026-10-09T18:25 | Donchian 20/10 | buy | AMD | 4.95 | — | entry signal |
| 2026-10-09T18:25 | RSI momentum | buy | AMD | 3.89 | — | entry signal |
| 2026-10-09T18:25 | RSI momentum | sell | COIN | 4.48 | 0.10 | exit signal |
| 2026-10-09T18:25 | ROC + volume | buy | SOXL | 18.79 | — | entry signal |
| 2026-10-09T18:25 | ROC + volume | sell | TECL | 18.82 | 0.04 | target is flat |
| 2026-10-09T18:25 | Trend pullback | buy | LABU | 3.94 | — | entry |
| 2026-10-09T18:25 | Supertrend | buy | AMD | 6.86 | — | entry signal |
| 2026-10-09T18:25 | Supertrend | sell | TECL | 3.36 | 0.01 | rebalance down |
| 2026-10-09T18:25 | Supertrend | sell | COIN | 3.51 | 0.07 | rebalance down |
| 2026-10-09T18:25 | MACD zero-line | buy | AMD | 4.69 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 18:29:05.000164+00:00 -> 2026-10-09 18:39:05.000164+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
