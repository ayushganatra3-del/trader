# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T08:30:05.000131+00:00 · 15390 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.68 (-3.32%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.46 | +0.08 |
| ETHU | 19.47 | +0.09 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 6560 decisions in 1312 calls, $0.0920 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T08:30 | 1 / 4 / 0 | PLTR 15% |  |
| Breezy | 2026-10-08T08:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T08:30 | 4 / 1 / 0 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |
| RSI(14) reversion | SOXL | 1.90 | +5.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.79 | 5.79 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.26 | 2.26 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.67 | 1.67 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.37 | 1.36 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.19 | 1.19 | 18 | 5.6 | 11.48 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.73 | 0.73 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.69 | 0.69 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.54 | 0.54 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.94 | -0.07 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.43 | -0.57 | 0 | — | 27.47 | 3.31 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.88 | -1.12 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.56 | -1.44 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.56 | -1.44 | 68 | 23.5 | -20.99 | -6.02 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.47 | -1.53 | 34 | 5.9 | 7.06 | 0.98 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.48 | -2.52 | 62 | 58.1 | -10.85 | -2.16 | -11.26 | 339 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.45 | -2.55 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.13 | -2.87 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.81 | -3.19 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.68 | -3.32 | 42 | 57.1 | -9.68 | -5.52 | -10.27 | 249 |
| 28 | Copy: Insider buying | copy | 96.55 | -3.45 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 30 | Supertrend · 1h | trend | 95.83 | -4.17 | 42 | 9.5 | -3.06 | -0.26 | -17.19 | 209 |
| 31 | Candlestick reversal · 1h | reversion | 95.63 | -4.37 | 85 | 32.9 | -26.52 | -6.03 | -26.73 | 482 |
| 32 | Parabolic SAR · 1h | trend | 95.52 | -4.48 | 80 | 21.2 | -6.70 | -0.77 | -20.87 | 293 |
| 33 | RSI(14) reversion · 1h | reversion | 95.46 | -4.54 | 20 | 35.0 | 1.69 | 0.53 | -6.57 | 117 |
| 34 | Z-score reversion · 1h | reversion | 95.37 | -4.63 | 32 | 40.6 | -0.77 | -0.03 | -8.60 | 159 |
| 35 | ADX DI cross · 1h | trend | 95.23 | -4.77 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.18 | -4.82 | 55 | 41.8 | -17.20 | -4.29 | -18.92 | 311 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.36 | -0.57 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 94.98 | -5.02 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.94 | -5.06 | 290 | 15.5 | 0.51 | 0.23 | -12.53 | 352 |
| 40 | MACD cross · 1h | trend | 94.87 | -5.13 | 101 | 22.8 | -12.31 | -1.73 | -17.27 | 466 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.96 | 2.49 | -8.12 | 102 |
| 42 | RSI momentum · 1h | momentum | 94.23 | -5.77 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.96 | -6.04 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.58 | -6.42 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.56 | -6.44 | 63 | 30.2 | 7.31 | 1.09 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.26 | -6.74 | 61 | 11.5 | -8.88 | -0.90 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.76 | -7.24 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.47 | -7.53 | 96 | 47.9 | -23.22 | -4.22 | -23.35 | 499 |
| 50 | MFI reversion · 1h | reversion | 92.42 | -7.58 | 87 | 27.6 | -12.26 | -2.11 | -16.99 | 122 |
| 51 | Opening range 15m | breakout | 92.28 | -7.72 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.22 | -8.78 | 50 | 20.0 | 2.07 | 0.46 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.21 | -8.79 | 90 | 11.1 | -4.49 | -0.40 | -18.86 | 339 |
| 54 | CCI reversion · 1h | reversion | 90.68 | -9.31 | 82 | 43.9 | -6.36 | -0.81 | -12.41 | 407 |
| 55 | MACD zero-line · 1h | trend | 90.58 | -9.42 | 57 | 19.3 | -5.36 | -0.52 | -19.00 | 239 |
| 56 | VWAP momentum · 1h | momentum | 90.42 | -9.58 | 243 | 22.6 | -36.25 | -5.50 | -37.99 | 1271 |
| 57 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.57 | -24.17 | -48.57 | 583 |
| 58 | OBV trend · 1h | momentum | 89.35 | -10.65 | 126 | 16.7 | -14.07 | -1.56 | -28.48 | 326 |
| 59 | Keltner breakout · 1h | breakout | 88.98 | -11.02 | 39 | 17.9 | -9.52 | -1.07 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.74 | -11.26 | 126 | 24.6 | -31.97 | -5.45 | -35.62 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.06 | -12.94 | 123 | 19.5 | -8.94 | -1.05 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.78 | -19.22 | 272 | 30.9 | -72.26 | -19.00 | -72.36 | 1433 |
| 64 | ROC + volume | momentum | 75.85 | -24.15 | 329 | 20.1 | -73.26 | -17.03 | -73.60 | 1648 |
| 65 | Squeeze breakout | breakout | 75.60 | -24.41 | 265 | 14.7 | -62.12 | -18.34 | -62.14 | 1213 |
| 66 | Donchian 55/20 | breakout | 73.99 | -26.01 | 269 | 16.7 | -68.68 | -14.88 | -68.69 | 1288 |
| 67 | EMA 20/50 cross | trend | 72.82 | -27.18 | 275 | 17.8 | -77.92 | -15.76 | -77.92 | 1465 |
| 68 | VWAP reversion | reversion | 72.82 | -27.18 | 326 | 27.9 | -70.27 | -16.02 | -70.45 | 1396 |
| 69 | Volume breakout | breakout | 72.79 | -27.21 | 216 | 12.0 | -64.34 | -18.85 | -64.34 | 907 |
| 70 | Supertrend | trend | 68.55 | -31.45 | 375 | 19.2 | -86.91 | -21.64 | -86.92 | 1929 |
| 71 | MFI reversion | reversion | 66.15 | -33.85 | 410 | 21.5 | -87.53 | -29.44 | -87.55 | 2111 |
| 72 | Keltner breakout | breakout | 65.84 | -34.16 | 367 | 12.5 | -85.22 | -29.36 | -85.22 | 1872 |
| 73 | Ichimoku | trend | 65.30 | -34.70 | 332 | 9.0 | -81.80 | -23.72 | -81.80 | 1734 |
| 74 | Z-score reversion | reversion | 65.19 | -34.81 | 419 | 24.1 | -85.47 | -24.21 | -85.53 | 2071 |
| 75 | AI bee: Bizzy | ai | 64.49 | -35.51 | 661 | 8.3 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.33 | -37.67 | 430 | 8.6 | -89.77 | -35.70 | -89.79 | 2114 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.42 | -38.58 | 509 | 17.5 | -91.09 | -26.65 | -91.10 | 2663 |
| 79 | MACD zero-line | trend | 61.00 | -39.00 | 484 | 14.7 | -91.49 | -29.88 | -91.49 | 2362 |
| 80 | Trend pullback | trend | 59.86 | -40.14 | 495 | 15.4 | -90.99 | -28.07 | -90.99 | 2322 |
| 81 | RSI momentum | momentum | 59.83 | -40.17 | 478 | 16.1 | -90.49 | -25.84 | -90.50 | 2369 |
| 82 | Triple EMA stack | trend | 58.97 | -41.03 | 518 | 15.1 | -93.35 | -31.32 | -93.35 | 2619 |
| 83 | Bollinger breakout | breakout | 57.24 | -42.76 | 531 | 13.4 | -93.83 | -34.23 | -93.83 | 2826 |
| 84 | Consensus | meta | 55.99 | -44.01 | 507 | 9.9 | -94.35 | -25.52 | -94.35 | 2679 |
| 85 | EMA 9/21 cross | trend | 53.57 | -46.43 | 655 | 15.7 | -97.40 | -33.86 | -97.40 | 3534 |
| 86 | Stochastic reversion | reversion | 53.17 | -46.83 | 769 | 22.1 | -95.62 | -34.75 | -95.62 | 4041 |
| 87 | Connors RSI(2) | reversion | 52.96 | -47.04 | 697 | 19.9 | -96.35 | -32.15 | -96.35 | 3591 |
| 88 | Bollinger reversion | reversion | 52.30 | -47.70 | 718 | 16.7 | -95.79 | -34.18 | -95.80 | 3696 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -31.11 | -98.71 | 5357 |
| 90 | OBV trend | momentum | 50.45 | -49.55 | 755 | 14.4 | -96.40 | -37.44 | -96.40 | 3594 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -37.54 | -99.32 | 5597 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.87 | -99.73 | 6130 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.29 | -97.39 | 3659 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.01 | -98.48 | 4684 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.86 | -99.51 | 6097 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.68 | -99.90 | 8252 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T08:30 | Stochastic reversion | buy | BTC-USD | 13.30 | — | entry signal |
| 2026-10-08T08:30 | MACD zero-line | buy | XRP-USD | 8.72 | — | rebalance up |
| 2026-10-08T08:30 | MACD zero-line | sell | DOGE-USD | 15.20 | -0.10 | exit signal |
| 2026-10-08T08:28 | AI bee: Bizzy | sell | XRP-USD | 9.70 | -0.07 | Jev: sell (sell p=0.67) after 10 min |
| 2026-10-08T08:25 | Ichimoku | sell | ETH-USD | 13.03 | -0.12 | exit signal |
| 2026-10-08T08:23 | AI bee: Bizzy | sell | DOGE-USD | 9.90 | -0.06 | Jev: sell (sell p=0.54) after 15 min |
| 2026-10-08T08:18 | AI bee: Bizzy | buy | XRP-USD | 9.77 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T08:15 | Keltner breakout | sell | BTC-USD | 16.36 | -0.14 | exit signal |
| 2026-10-08T08:15 | Bollinger breakout | buy | XRP-USD | 2.03 | — | entry |
| 2026-10-08T08:15 | Bollinger breakout | buy | DOGE-USD | 12.20 | — | rebalance up |
| 2026-10-08T08:15 | Bollinger breakout | sell | BTC-USD | 14.23 | -0.13 | exit signal |
| 2026-10-08T08:10 | Stochastic reversion | buy | SOL-USD | 13.31 | — | entry signal |
| 2026-10-08T08:08 | AI bee: Bizzy | buy | DOGE-USD | 9.96 | — | Jev: buy (buy p=0.62) |
| 2026-10-08T08:05 | MACD zero-line | buy | XRP-USD | 6.56 | — | entry |
| 2026-10-08T08:05 | MACD zero-line | buy | DOGE-USD | 15.30 | — | entry |
| 2026-10-08T08:05 | MACD zero-line | sell | ETH-USD | 6.63 | -0.06 | exit signal |
| 2026-10-08T08:05 | MACD zero-line | sell | BTC-USD | 15.23 | -0.09 | exit signal |
| 2026-10-08T08:00 | CCI reversion · 1h | buy | BTC-USD | 9.27 | — | entry signal |
| 2026-10-08T08:00 | CCI reversion · 1h | sell | XRP-USD | 4.63 | 0.01 | rebalance down |
| 2026-10-08T08:00 | CCI reversion · 1h | sell | ETH-USD | 4.55 | -0.02 | rebalance down |
| 2026-10-08T08:00 | VWAP momentum · 1h | buy | BTC-USD | 5.65 | — | entry signal |
| 2026-10-08T08:00 | ADX DI cross | sell | DOGE-USD | 15.51 | -0.13 | exit signal |
| 2026-10-08T07:50 | ROC + volume | sell | SOL-USD | 18.82 | -0.19 | exit signal |
| 2026-10-08T07:50 | Ichimoku | buy | XRP-USD | 6.53 | — | rebalance up |
| 2026-10-08T07:50 | Ichimoku | buy | DOGE-USD | 3.28 | — | rebalance up |
| 2026-10-08T07:50 | Ichimoku | sell | SOL-USD | 13.01 | -0.13 | exit signal |
| 2026-10-08T07:50 | ADX DI cross | sell | XRP-USD | 4.90 | -0.03 | exit signal |
| 2026-10-08T07:45 | MFI reversion | sell | DOGE-USD | 16.54 | -0.02 | exit signal |
| 2026-10-08T07:45 | ADX DI cross | buy | XRP-USD | 4.93 | — | entry |
| 2026-10-08T07:45 | ADX DI cross | sell | SOL-USD | 4.93 | -0.04 | exit signal |
| 2026-10-08T07:38 | AI bee: Boozy | sell | ETH-USD | 18.85 | -0.12 | Jev: buy |
| 2026-10-08T07:33 | AI bee: Bizzy | sell | SOL-USD | 10.09 | -0.06 | Jev: sell (sell p=0.61) after 12 min |
| 2026-10-08T07:26 | Ichimoku | sell | BTC-USD | 3.27 | -0.02 | rebalance down |
| 2026-10-08T07:25 | VWAP reversion | sell | XRP-USD | 18.21 | 0.05 | exit signal |
| 2026-10-08T07:25 | VWAP reversion | sell | SOL-USD | 18.20 | 0.03 | exit signal |
| 2026-10-08T07:25 | OBV trend | buy | BTC-USD | 12.13 | — | entry signal |
| 2026-10-08T07:25 | ROC + volume | buy | SOL-USD | 19.02 | — | entry signal |
| 2026-10-08T07:25 | Ichimoku | buy | XRP-USD | 9.89 | — | entry signal |
| 2026-10-08T07:25 | Ichimoku | buy | SOL-USD | 13.15 | — | entry signal |
| 2026-10-08T07:25 | Ichimoku | buy | ETH-USD | 13.15 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 08:30:05.000131+00:00 -> 2026-10-08 08:40:05.000131+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
