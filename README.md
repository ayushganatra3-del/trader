# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T18:00:05.000152+00:00 · 16986 ticks

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

Today: 27126 decisions in 2532 calls, $0.3395 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T18:00 | 2 / 16 / 11 | TNA 14%, NANC 15% |  |
| Breezy | 2026-10-09T18:00 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-09T18:00 | 0 / 27 / 2 | COIN 75% |  |

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
| 1 | VWAP reversion · 1h | reversion | 103.33 | 3.33 | 37 | 43.2 | -8.02 | -2.46 | -13.79 | 118 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.48 | 2.48 | 0 | — | -4.21 | -0.68 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.20 | 2.20 | 0 | — | -3.66 | -1.50 | -7.31 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.44 | 1.44 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.33 | 1.33 | 0 | — | 0.47 | 0.32 | -3.66 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 101.14 | 1.14 | 0 | — | -0.91 | -0.47 | -5.09 | 1 |
| 9 | Copy: Insider buying | copy | 100.59 | 0.59 | 14 | 57.1 | -13.40 | -2.25 | -21.08 | 72 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Max aggression: 1-day momentum | meta | 100.39 | 0.39 | 10 | 30.0 | -15.04 | -0.51 | -37.31 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.80 | -0.20 | 9 | 22.2 | 3.50 | 1.11 | -7.55 | 44 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.64 | -0.36 | 0 | — | -3.97 | -1.85 | -5.36 | 1 |
| 16 | Stochastic reversion · 1h | reversion | 99.54 | -0.46 | 88 | 55.7 | -10.61 | -2.04 | -14.99 | 342 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.27 | -0.73 | 35 | 37.1 | 4.75 | 2.24 | -1.52 | 90 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.64 | -1.74 | -3.04 | 20 |
| 19 | Hold BTC | benchmark | 98.88 | -1.12 | 0 | — | 26.78 | 3.22 | -8.68 | 1 |
| 20 | Donchian 55/20 · 1h | breakout | 98.86 | -1.14 | 27 | 14.8 | 12.76 | 1.60 | -16.96 | 109 |
| 21 | Copy: Cathie Wood (ARKK) | copy | 98.81 | -1.19 | 0 | — | 11.69 | 1.90 | -8.33 | 1 |
| 22 | Daily: SMA 20/50 cross · AAPL | daily | 98.17 | -1.83 | 0 | — | 1.12 | 0.50 | -5.18 | 1 |
| 23 | Daily: Bullish score | daily | 97.74 | -2.26 | 4 | 0.0 | 0.68 | 0.29 | -12.76 | 11 |
| 24 | Z-score reversion · 1h | reversion | 97.51 | -2.48 | 38 | 42.1 | 0.59 | 0.25 | -8.60 | 165 |
| 25 | Three white soldiers · 1h | momentum | 97.49 | -2.51 | 6 | 0.0 | -3.13 | -2.42 | -4.28 | 27 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -22.71 | -6.38 | -25.39 | 169 |
| 27 | EMA 20/50 cross · 1h | trend | 96.83 | -3.17 | 38 | 13.2 | 4.39 | 0.70 | -19.85 | 135 |
| 28 | Agent (rotation) | meta | 96.76 | -3.24 | 79 | 29.1 | 2.37 | 0.67 | -8.65 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.09 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.47 | -3.53 | 56 | 21.4 | -1.99 | -0.15 | -13.84 | 254 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.87 | -0.21 | -20.87 | 293 |
| 32 | MACD cross · 1h | trend | 96.08 | -3.92 | 107 | 22.4 | -17.04 | -2.77 | -18.77 | 475 |
| 33 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.76 | -5.40 | -10.42 | 245 |
| 34 | Supertrend · 1h | trend | 94.98 | -5.02 | 52 | 13.5 | -0.38 | 0.14 | -18.22 | 209 |
| 35 | Squeeze breakout · 1h | breakout | 94.31 | -5.69 | 35 | 25.7 | 24.29 | 3.30 | -8.61 | 105 |
| 36 | MFI reversion · 1h | reversion | 94.13 | -5.87 | 112 | 35.7 | -11.37 | -1.76 | -17.79 | 129 |
| 37 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.55 | -2.07 | -6.59 | 109 |
| 38 | Gap and go | momentum | 93.88 | -6.12 | 56 | 10.7 | 7.67 | 1.97 | -6.64 | 200 |
| 39 | RSI(14) reversion · 1h | reversion | 93.61 | -6.38 | 26 | 26.9 | -3.90 | -0.75 | -9.03 | 158 |
| 40 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 41 | Agent (ML meta-label) | meta | 93.08 | -6.92 | 389 | 18.3 | -4.44 | -0.67 | -13.95 | 430 |
| 42 | Bollinger reversion · 1h | reversion | 93.05 | -6.95 | 73 | 37.0 | -20.69 | -4.92 | -23.75 | 318 |
| 43 | Connors RSI(2) · 1h | reversion | 92.98 | -7.02 | 110 | 43.6 | -18.36 | -6.10 | -20.97 | 253 |
| 44 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 63 | 15.9 | 3.52 | 0.63 | -17.07 | 219 |
| 45 | Volume breakout · 1h | breakout | 92.23 | -7.77 | 51 | 15.7 | 7.51 | 1.18 | -12.60 | 123 |
| 46 | Williams %R · 1h | reversion | 91.75 | -8.25 | 116 | 48.3 | -25.15 | -4.33 | -27.32 | 512 |
| 47 | Bollinger breakout · 1h | breakout | 91.73 | -8.27 | 67 | 29.9 | 5.39 | 0.86 | -12.90 | 288 |
| 48 | Opening range 30m | breakout | 91.09 | -8.91 | 136 | 19.9 | -16.83 | -5.10 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.79 | -9.21 | 69 | 15.9 | -8.77 | -0.88 | -26.38 | 236 |
| 50 | Candlestick reversal · 1h | reversion | 90.63 | -9.37 | 108 | 30.6 | -28.76 | -5.61 | -30.78 | 523 |
| 51 | CCI reversion · 1h | reversion | 90.18 | -9.82 | 94 | 42.6 | -8.98 | -1.16 | -14.35 | 415 |
| 52 | VWAP momentum · 1h | momentum | 89.89 | -10.11 | 272 | 22.1 | -35.70 | -5.41 | -39.33 | 1279 |
| 53 | MACD zero-line · 1h | trend | 89.61 | -10.39 | 59 | 20.3 | -6.43 | -0.68 | -19.40 | 238 |
| 54 | Opening range 15m | breakout | 89.25 | -10.75 | 158 | 18.4 | -18.40 | -5.23 | -19.78 | 700 |
| 55 | Three white soldiers | momentum | 89.12 | -10.88 | 126 | 19.0 | -47.94 | -23.40 | -48.12 | 586 |
| 56 | Donchian 20/10 · 1h | breakout | 88.81 | -11.19 | 57 | 19.3 | -1.00 | 0.09 | -17.72 | 222 |
| 57 | Heikin-Ashi · 1h | trend | 88.65 | -11.35 | 135 | 25.2 | -31.63 | -5.33 | -36.59 | 699 |
| 58 | OBV trend · 1h | momentum | 88.58 | -11.42 | 145 | 18.6 | -12.84 | -1.47 | -28.83 | 319 |
| 59 | EMA 9/21 cross · 1h | trend | 87.71 | -12.29 | 101 | 13.9 | -10.08 | -1.17 | -21.49 | 337 |
| 60 | Keltner breakout · 1h | breakout | 86.75 | -13.25 | 43 | 18.6 | -12.03 | -1.40 | -25.35 | 216 |
| 61 | Max aggression: 5-day momentum | meta | 86.64 | -13.36 | 7 | 28.6 | -15.66 | -1.20 | -34.64 | 28 |
| 62 | ROC + volume · 1h | momentum | 86.57 | -13.43 | 130 | 21.5 | -10.38 | -1.26 | -23.72 | 415 |
| 63 | RSI(14) reversion | reversion | 75.77 | -24.23 | 346 | 28.9 | -73.38 | -18.63 | -73.61 | 1505 |
| 64 | ROC + volume | momentum | 75.09 | -24.91 | 382 | 22.5 | -73.51 | -17.19 | -74.38 | 1672 |
| 65 | Squeeze breakout | breakout | 74.06 | -25.94 | 288 | 15.3 | -61.57 | -18.17 | -61.73 | 1211 |
| 66 | Donchian 55/20 | breakout | 72.77 | -27.23 | 295 | 16.9 | -67.95 | -14.46 | -68.48 | 1291 |
| 67 | EMA 20/50 cross | trend | 72.10 | -27.91 | 296 | 19.3 | -77.54 | -15.51 | -77.72 | 1462 |
| 68 | Volume breakout | breakout | 71.58 | -28.42 | 241 | 13.7 | -63.35 | -18.16 | -63.47 | 904 |
| 69 | VWAP reversion | reversion | 68.70 | -31.30 | 386 | 26.2 | -72.20 | -16.47 | -72.57 | 1458 |
| 70 | Supertrend | trend | 66.42 | -33.58 | 429 | 20.0 | -86.66 | -21.46 | -86.73 | 1927 |
| 71 | Keltner breakout | breakout | 65.57 | -34.43 | 410 | 14.6 | -84.16 | -27.81 | -84.47 | 1854 |
| 72 | Ichimoku | trend | 62.49 | -37.51 | 373 | 9.1 | -81.74 | -23.46 | -81.87 | 1744 |
| 73 | AI bee: Bizzy | ai | 62.47 | -37.53 | 742 | 9.7 | — | — | — | — |
| 74 | AI bee: Boozy | ai | 62.02 | -37.98 | 246 | 5.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 61.83 | -38.17 | 470 | 21.9 | -88.00 | -28.90 | -88.03 | 2124 |
| 76 | Z-score reversion | reversion | 61.82 | -38.17 | 472 | 23.9 | -85.99 | -23.82 | -86.04 | 2100 |
| 77 | Donchian 20/10 | breakout | 59.38 | -40.62 | 575 | 18.6 | -90.84 | -26.25 | -90.96 | 2658 |
| 78 | Trend pullback | trend | 59.31 | -40.69 | 526 | 16.0 | -90.43 | -27.20 | -90.55 | 2299 |
| 79 | ADX DI cross | trend | 58.86 | -41.14 | 512 | 10.2 | -89.90 | -35.65 | -89.91 | 2146 |
| 80 | RSI momentum | momentum | 58.44 | -41.56 | 539 | 17.1 | -90.24 | -25.60 | -90.35 | 2370 |
| 81 | MACD zero-line | trend | 57.95 | -42.05 | 534 | 15.7 | -91.52 | -30.02 | -91.53 | 2358 |
| 82 | Triple EMA stack | trend | 57.17 | -42.83 | 564 | 15.4 | -93.12 | -30.46 | -93.14 | 2606 |
| 83 | Bollinger breakout | breakout | 54.76 | -45.24 | 601 | 15.0 | -93.56 | -33.38 | -93.56 | 2811 |
| 84 | Consensus | meta | 52.90 | -47.10 | 572 | 10.1 | -94.34 | -26.22 | -94.34 | 2685 |
| 85 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -31.08 | -98.74 | 5406 |
| 86 | EMA 9/21 cross | trend | 50.57 | -49.43 | 728 | 15.8 | -97.39 | -33.77 | -97.39 | 3544 |
| 87 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -36.72 | -96.42 | 3582 |
| 88 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.56 | -99.36 | 5700 |
| 89 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.27 | -96.29 | 3595 |
| 90 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.67 | -99.73 | 6179 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.31 | -38.59 | -97.32 | 3662 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.63 | -98.50 | 4718 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -41.26 | -99.53 | 6154 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -34.23 | -95.93 | 3747 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -35.20 | -95.67 | 4089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.53 | -99.90 | 8316 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T18:00 | Consensus | buy | TSLA | 4.42 | — | entry |
| 2026-10-09T18:00 | Consensus | sell | MSTR | 4.42 | -0.02 | target is flat |
| 2026-10-09T18:00 | Candlestick reversal · 1h | buy | QQQ | 2.49 | — | entry |
| 2026-10-09T18:00 | Candlestick reversal · 1h | buy | AMD | 7.56 | — | entry |
| 2026-10-09T18:00 | Candlestick reversal · 1h | sell | ETH-USD | 10.05 | -0.10 | exit signal |
| 2026-10-09T18:00 | OBV trend · 1h | buy | TSLA | 12.62 | — | entry |
| 2026-10-09T18:00 | ADX DI cross · 1h | buy | COIN | 11.94 | — | entry |
| 2026-10-09T18:00 | ADX DI cross · 1h | sell | BTC-USD | 11.94 | -0.15 | exit signal |
| 2026-10-09T18:00 | Volume breakout | buy | TNA | 17.90 | — | entry signal |
| 2026-10-09T18:00 | Volume breakout | buy | IWM | 17.90 | — | entry |
| 2026-10-09T18:00 | Squeeze breakout | buy | IWM | 11.08 | — | entry signal |
| 2026-10-09T18:00 | Squeeze breakout | sell | TNA | 3.72 | -0.00 | rebalance down |
| 2026-10-09T18:00 | Squeeze breakout | sell | TECL | 3.71 | -0.00 | rebalance down |
| 2026-10-09T18:00 | Keltner breakout | buy | TNA | 6.52 | — | entry signal |
| 2026-10-09T18:00 | Keltner breakout | buy | LABU | 10.93 | — | entry |
| 2026-10-09T18:00 | Keltner breakout | sell | UPRO | 5.46 | 0.01 | rebalance down |
| 2026-10-09T18:00 | Keltner breakout | sell | COIN | 5.51 | 0.01 | rebalance down |
| 2026-10-09T18:00 | RSI momentum | buy | DOGE-USD | 3.30 | — | entry signal |
| 2026-10-09T18:00 | MACD zero-line | buy | SOXL | 14.49 | — | entry signal |
| 2026-10-09T17:56 | Consensus | buy | MSTR | 4.44 | — | entry |
| 2026-10-09T17:56 | Consensus | sell | COIN | 4.44 | 0.00 | rebalance down |
| 2026-10-09T17:56 | OBV trend · 1h | sell | TQQQ | 12.62 | 0.01 | target is flat |
| 2026-10-09T17:56 | Volume breakout | sell | IWM | 17.89 | -0.01 | target is flat |
| 2026-10-09T17:56 | Squeeze breakout | buy | XRP-USD | 18.53 | — | entry signal |
| 2026-10-09T17:56 | Squeeze breakout | buy | TNA | 18.53 | — | entry signal |
| 2026-10-09T17:56 | Bollinger breakout | buy | TNA | 7.38 | — | entry signal |
| 2026-10-09T17:56 | Bollinger breakout | buy | IWM | 7.83 | — | entry signal |
| 2026-10-09T17:56 | Bollinger breakout | sell | XRP-USD | 5.82 | -0.03 | rebalance down |
| 2026-10-09T17:56 | Bollinger breakout | sell | UPRO | 3.13 | 0.00 | rebalance down |
| 2026-10-09T17:56 | Bollinger breakout | sell | TECL | 3.13 | -0.00 | rebalance down |
| 2026-10-09T17:56 | Bollinger breakout | sell | PLTR | 3.13 | -0.01 | rebalance down |
| 2026-10-09T17:56 | ROC + volume | sell | LABU | 18.68 | -0.12 | exit signal |
| 2026-10-09T17:56 | Triple EMA stack | buy | AMZN | 5.72 | — | entry signal |
| 2026-10-09T17:56 | EMA 9/21 cross | buy | SOL-USD | 5.17 | — | entry signal |
| 2026-10-09T17:56 | EMA 9/21 cross | buy | MSTR | 6.33 | — | entry signal |
| 2026-10-09T17:56 | EMA 9/21 cross | buy | AMZN | 6.33 | — | entry signal |
| 2026-10-09T17:56 | EMA 9/21 cross | sell | XRP-USD | 3.79 | -0.01 | rebalance down |
| 2026-10-09T17:56 | EMA 9/21 cross | sell | DOGE-USD | 6.29 | -0.03 | rebalance down |
| 2026-10-09T17:56 | EMA 9/21 cross | sell | COIN | 3.91 | 0.08 | rebalance down |
| 2026-10-09T17:56 | EMA 9/21 cross | sell | AAPL | 3.84 | 0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 18:00:05.000152+00:00 -> 2026-10-09 18:10:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
