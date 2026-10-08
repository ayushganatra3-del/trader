# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T05:00:05.000163+00:00 · 15207 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.65 (-3.35%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.45 | +0.07 |
| ETHU | 19.46 | +0.07 |

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

Today: 3825 decisions in 765 calls, $0.0537 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T05:00 | 1 / 3 / 1 | PLTR 15% |  |
| Breezy | 2026-10-08T05:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T05:00 | 0 / 5 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.71 | 5.71 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.18 | 2.19 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.59 | 1.59 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.29 | 1.29 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.11 | 1.11 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.65 | 0.65 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.62 | 0.62 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.86 | -0.14 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 98.94 | -1.06 | 0 | — | 28.13 | 3.38 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.80 | -1.20 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.49 | -1.51 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.49 | -1.51 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.42 | -1.58 | 34 | 5.9 | 7.47 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.40 | -2.60 | 62 | 58.1 | -10.95 | -2.18 | -11.26 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.37 | -2.63 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.06 | -2.94 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.65 | -3.35 | 42 | 57.1 | -9.80 | -5.52 | -10.39 | 248 |
| 28 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 29 | Copy: Insider buying | copy | 96.48 | -3.52 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 30 | Supertrend · 1h | trend | 95.77 | -4.23 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 31 | Candlestick reversal · 1h | reversion | 95.71 | -4.29 | 85 | 32.9 | -26.47 | -6.02 | -26.58 | 481 |
| 32 | Parabolic SAR · 1h | trend | 95.49 | -4.51 | 80 | 21.2 | -6.76 | -0.78 | -20.87 | 295 |
| 33 | RSI(14) reversion · 1h | reversion | 95.46 | -4.54 | 20 | 35.0 | 1.66 | 0.52 | -6.57 | 114 |
| 34 | Z-score reversion · 1h | reversion | 95.31 | -4.69 | 32 | 40.6 | -0.80 | -0.04 | -8.60 | 159 |
| 35 | ADX DI cross · 1h | trend | 95.18 | -4.82 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.14 | -4.86 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -2.91 | -1.26 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 94.91 | -5.09 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.88 | -5.12 | 290 | 15.5 | -2.14 | -0.25 | -13.41 | 371 |
| 40 | MACD cross · 1h | trend | 94.75 | -5.25 | 101 | 22.8 | -12.68 | -1.79 | -17.27 | 467 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.17 | -5.83 | 51 | 3.9 | -3.92 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.89 | -6.11 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.55 | -6.45 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.53 | -6.47 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.21 | -6.79 | 61 | 11.5 | -8.70 | -0.88 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 49 | MFI reversion · 1h | reversion | 92.39 | -7.61 | 87 | 27.6 | -12.29 | -2.12 | -16.99 | 122 |
| 50 | Williams %R · 1h | reversion | 92.35 | -7.65 | 96 | 47.9 | -23.14 | -4.20 | -23.35 | 500 |
| 51 | Opening range 15m | breakout | 92.21 | -7.79 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.16 | -8.84 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.16 | -8.84 | 90 | 11.1 | -4.61 | -0.42 | -18.86 | 340 |
| 54 | MACD zero-line · 1h | trend | 90.55 | -9.45 | 57 | 19.3 | -4.96 | -0.47 | -19.00 | 237 |
| 55 | CCI reversion · 1h | reversion | 90.49 | -9.51 | 82 | 43.9 | -6.44 | -0.83 | -12.41 | 406 |
| 56 | VWAP momentum · 1h | momentum | 90.39 | -9.62 | 243 | 22.6 | -36.85 | -5.63 | -37.98 | 1275 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.55 | -24.08 | -48.55 | 583 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.45 | -1.61 | -28.48 | 328 |
| 59 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -8.91 | -0.98 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.72 | -11.28 | 126 | 24.6 | -31.97 | -5.45 | -35.62 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.01 | -12.99 | 123 | 19.5 | -8.94 | -1.05 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.73 | -19.27 | 270 | 31.1 | -72.30 | -19.03 | -72.33 | 1433 |
| 64 | ROC + volume | momentum | 76.18 | -23.82 | 327 | 20.2 | -73.34 | -17.06 | -73.60 | 1651 |
| 65 | Squeeze breakout | breakout | 75.78 | -24.22 | 264 | 14.8 | -62.09 | -18.33 | -62.12 | 1214 |
| 66 | Donchian 55/20 | breakout | 73.96 | -26.04 | 269 | 16.7 | -69.04 | -15.08 | -69.04 | 1294 |
| 67 | EMA 20/50 cross | trend | 72.88 | -27.12 | 275 | 17.8 | -77.83 | -15.70 | -77.83 | 1462 |
| 68 | Volume breakout | breakout | 72.78 | -27.22 | 216 | 12.0 | -64.57 | -18.90 | -64.58 | 912 |
| 69 | VWAP reversion | reversion | 72.59 | -27.41 | 323 | 27.2 | -70.19 | -15.92 | -70.42 | 1392 |
| 70 | Supertrend | trend | 68.62 | -31.38 | 374 | 19.3 | -86.75 | -21.42 | -86.75 | 1922 |
| 71 | MFI reversion | reversion | 66.23 | -33.77 | 406 | 21.7 | -87.46 | -29.23 | -87.46 | 2109 |
| 72 | Keltner breakout | breakout | 65.97 | -34.03 | 366 | 12.6 | -85.23 | -29.35 | -85.25 | 1875 |
| 73 | Ichimoku | trend | 65.78 | -34.22 | 330 | 9.1 | -81.69 | -23.55 | -81.70 | 1731 |
| 74 | Z-score reversion | reversion | 65.19 | -34.81 | 414 | 24.4 | -85.45 | -24.19 | -85.45 | 2069 |
| 75 | AI bee: Bizzy | ai | 65.02 | -34.98 | 653 | 8.4 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.82 | -37.18 | 424 | 8.7 | -89.59 | -34.88 | -89.68 | 2110 |
| 77 | AI bee: Boozy | ai | 62.77 | -37.23 | 226 | 3.5 | — | — | — | — |
| 78 | MACD zero-line | trend | 61.61 | -38.39 | 478 | 14.9 | -91.35 | -29.43 | -91.35 | 2354 |
| 79 | Donchian 20/10 | breakout | 61.54 | -38.46 | 508 | 17.5 | -91.00 | -26.41 | -91.02 | 2661 |
| 80 | RSI momentum | momentum | 59.88 | -40.12 | 478 | 16.1 | -90.48 | -25.79 | -90.48 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.05 | -28.31 | -91.05 | 2326 |
| 82 | Triple EMA stack | trend | 58.92 | -41.08 | 518 | 15.1 | -93.30 | -31.19 | -93.31 | 2618 |
| 83 | Bollinger breakout | breakout | 57.53 | -42.47 | 528 | 13.4 | -93.79 | -33.94 | -93.80 | 2825 |
| 84 | Consensus | meta | 55.97 | -44.03 | 507 | 9.9 | -94.46 | -25.91 | -94.46 | 2691 |
| 85 | EMA 9/21 cross | trend | 53.83 | -46.17 | 652 | 15.8 | -97.34 | -33.35 | -97.34 | 3522 |
| 86 | Stochastic reversion | reversion | 53.29 | -46.72 | 764 | 22.1 | -95.61 | -34.69 | -95.61 | 4035 |
| 87 | Connors RSI(2) | reversion | 52.95 | -47.05 | 697 | 19.9 | -96.38 | -32.47 | -96.38 | 3596 |
| 88 | Bollinger reversion | reversion | 52.20 | -47.80 | 714 | 16.7 | -95.79 | -34.24 | -95.80 | 3695 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -30.47 | -98.65 | 5328 |
| 90 | OBV trend | momentum | 50.49 | -49.51 | 755 | 14.4 | -96.43 | -37.52 | -96.43 | 3599 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -37.27 | -99.31 | 5589 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.49 | -99.73 | 6127 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.22 | -97.39 | 3662 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.98 | -98.48 | 4683 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.79 | -99.51 | 6092 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.78 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T05:00 | Williams %R · 1h | buy | BTC-USD | 18.48 | — | entry signal |
| 2026-10-08T05:00 | Candlestick reversal · 1h | buy | BTC-USD | 23.95 | — | entry signal |
| 2026-10-08T04:55 | Z-score reversion | buy | SOL-USD | 16.31 | — | entry signal |
| 2026-10-08T04:50 | MFI reversion | buy | BTC-USD | 2.06 | — | entry signal |
| 2026-10-08T04:50 | VWAP reversion | buy | XRP-USD | 18.15 | — | entry signal |
| 2026-10-08T04:50 | Bollinger reversion | buy | XRP-USD | 13.06 | — | entry signal |
| 2026-10-08T04:45 | CCI reversion · 1h | buy | XRP-USD | 7.31 | — | rebalance up |
| 2026-10-08T04:45 | CCI reversion · 1h | buy | ETH-USD | 7.52 | — | rebalance up |
| 2026-10-08T04:45 | CCI reversion · 1h | sell | BTC-USD | 14.93 | -0.28 | stop-loss |
| 2026-10-08T04:45 | Williams %R · 1h | sell | XRP-USD | 18.32 | -0.40 | stop-loss |
| 2026-10-08T04:45 | Z-score reversion · 1h | sell | XRP-USD | 23.77 | -0.37 | stop-loss |
| 2026-10-08T04:45 | RSI(14) reversion · 1h | sell | XRP-USD | 23.75 | -0.45 | stop-loss |
| 2026-10-08T04:40 | MFI reversion · 1h | sell | DOGE-USD | 22.86 | -0.54 | stop-loss |
| 2026-10-08T04:40 | CCI reversion · 1h | buy | XRP-USD | 15.36 | — | entry |
| 2026-10-08T04:40 | CCI reversion · 1h | sell | DOGE-USD | 14.86 | -0.38 | stop-loss |
| 2026-10-08T04:40 | Z-score reversion · 1h | buy | XRP-USD | 4.87 | — | rebalance up |
| 2026-10-08T04:40 | Z-score reversion · 1h | buy | ETH-USD | 7.89 | — | rebalance up |
| 2026-10-08T04:40 | Z-score reversion · 1h | sell | DOGE-USD | 15.76 | -0.40 | stop-loss |
| 2026-10-08T04:40 | RSI(14) reversion · 1h | sell | DOGE-USD | 23.71 | -0.59 | stop-loss |
| 2026-10-08T04:40 | Z-score reversion | sell | SOL-USD | 16.19 | -0.20 | stop-loss |
| 2026-10-08T04:40 | Bollinger reversion | sell | XRP-USD | 12.97 | -0.18 | stop-loss |
| 2026-10-08T04:30 | Stochastic reversion | sell | BTC-USD | 13.37 | -0.05 | exit signal |
| 2026-10-08T04:30 | Z-score reversion | buy | SOL-USD | 16.39 | — | entry signal |
| 2026-10-08T04:30 | Bollinger reversion | buy | XRP-USD | 13.15 | — | entry signal |
| 2026-10-08T04:30 | Bollinger reversion | buy | DOGE-USD | 13.15 | — | entry signal |
| 2026-10-08T04:25 | Stochastic reversion | sell | XRP-USD | 13.22 | -0.19 | stop-loss |
| 2026-10-08T04:25 | VWAP reversion | buy | SOL-USD | 18.19 | — | entry signal |
| 2026-10-08T04:25 | VWAP reversion | sell | XRP-USD | 18.04 | -0.26 | stop-loss |
| 2026-10-08T04:25 | Bollinger reversion | buy | SOL-USD | 13.15 | — | entry signal |
| 2026-10-08T04:25 | Bollinger reversion | sell | XRP-USD | 13.03 | -0.19 | stop-loss |
| 2026-10-08T04:20 | MFI reversion · 1h | buy | DOGE-USD | 4.67 | — | rebalance up |
| 2026-10-08T04:20 | MFI reversion · 1h | sell | SOL-USD | 18.44 | -0.33 | stop-loss |
| 2026-10-08T04:20 | MFI reversion · 1h | sell | BTC-USD | 18.46 | -0.28 | stop-loss |
| 2026-10-08T04:20 | Williams %R · 1h | buy | XRP-USD | 5.39 | — | rebalance up |
| 2026-10-08T04:20 | Williams %R · 1h | sell | SOL-USD | 13.12 | -0.29 | stop-loss |
| 2026-10-08T04:20 | Williams %R · 1h | sell | BTC-USD | 13.20 | -0.21 | stop-loss |
| 2026-10-08T04:20 | Z-score reversion · 1h | buy | XRP-USD | 11.97 | — | rebalance up |
| 2026-10-08T04:20 | Z-score reversion · 1h | sell | SOL-USD | 15.83 | -0.30 | stop-loss |
| 2026-10-08T04:20 | Z-score reversion · 1h | sell | BTC-USD | 15.90 | -0.25 | stop-loss |
| 2026-10-08T04:20 | RSI(14) reversion · 1h | buy | XRP-USD | 14.34 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 05:00:05.000163+00:00 -> 2026-10-08 05:10:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
