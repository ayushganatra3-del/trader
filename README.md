# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T06:00:05.000152+00:00 · 15258 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.65 (-3.35%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.45 | +0.07 |
| ETHU | 19.46 | +0.08 |

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

Today: 4580 decisions in 916 calls, $0.0642 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T06:00 | 0 / 2 / 3 | PLTR 15% |  |
| Breezy | 2026-10-08T06:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T06:00 | 0 / 5 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.72 | 5.72 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.20 | 2.20 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.60 | 1.60 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.30 | 1.30 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.12 | 1.12 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.66 | 0.66 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.63 | 0.63 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.87 | -0.13 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 98.99 | -1.01 | 0 | — | 28.22 | 3.39 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.81 | -1.19 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.50 | -1.50 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.50 | -1.50 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.43 | -1.57 | 34 | 5.9 | 7.37 | 1.01 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.40 | -2.60 | 62 | 58.1 | -10.96 | -2.18 | -11.26 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.38 | -2.62 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.07 | -2.93 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.78 | -3.22 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.65 | -3.35 | 42 | 57.1 | -9.18 | -5.02 | -10.29 | 249 |
| 28 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 29 | Copy: Insider buying | copy | 96.49 | -3.51 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 30 | Supertrend · 1h | trend | 95.78 | -4.22 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 31 | Candlestick reversal · 1h | reversion | 95.72 | -4.28 | 85 | 32.9 | -26.46 | -6.02 | -26.59 | 481 |
| 32 | Parabolic SAR · 1h | trend | 95.49 | -4.51 | 80 | 21.2 | -6.88 | -0.80 | -20.87 | 295 |
| 33 | RSI(14) reversion · 1h | reversion | 95.45 | -4.55 | 20 | 35.0 | 1.66 | 0.52 | -6.57 | 114 |
| 34 | Z-score reversion · 1h | reversion | 95.30 | -4.70 | 32 | 40.6 | -0.81 | -0.04 | -8.60 | 159 |
| 35 | ADX DI cross · 1h | trend | 95.19 | -4.81 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.12 | -4.88 | 55 | 41.8 | -17.20 | -4.30 | -18.92 | 309 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -0.97 | -0.38 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 94.92 | -5.08 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.89 | -5.11 | 290 | 15.5 | -2.47 | -0.35 | -11.98 | 366 |
| 40 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.79 | 2.46 | -8.12 | 102 |
| 41 | MACD cross · 1h | trend | 94.73 | -5.27 | 101 | 22.8 | -12.56 | -1.77 | -17.27 | 466 |
| 42 | RSI momentum · 1h | momentum | 94.18 | -5.82 | 51 | 3.9 | -3.88 | -0.39 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.90 | -6.10 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.55 | -6.45 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.53 | -6.47 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.21 | -6.79 | 61 | 11.5 | -8.71 | -0.88 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.50 | 1.05 | -12.60 | 121 |
| 49 | MFI reversion · 1h | reversion | 92.38 | -7.62 | 87 | 27.6 | -12.30 | -2.12 | -16.99 | 122 |
| 50 | Williams %R · 1h | reversion | 92.36 | -7.64 | 96 | 47.9 | -23.13 | -4.20 | -23.36 | 500 |
| 51 | Opening range 15m | breakout | 92.22 | -7.78 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.17 | -8.83 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.16 | -8.84 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 54 | MACD zero-line · 1h | trend | 90.55 | -9.45 | 57 | 19.3 | -4.96 | -0.47 | -19.00 | 237 |
| 55 | CCI reversion · 1h | reversion | 90.46 | -9.54 | 82 | 43.9 | -6.48 | -0.83 | -12.41 | 406 |
| 56 | VWAP momentum · 1h | momentum | 90.39 | -9.61 | 243 | 22.6 | -36.85 | -5.63 | -37.98 | 1275 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.48 | -24.03 | -48.48 | 582 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.55 | -1.63 | -28.48 | 328 |
| 59 | Keltner breakout · 1h | breakout | 88.97 | -11.04 | 39 | 17.9 | -8.91 | -0.98 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.72 | -11.28 | 126 | 24.6 | -31.97 | -5.45 | -35.62 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.02 | -12.98 | 123 | 19.5 | -8.94 | -1.05 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.71 | -19.29 | 271 | 31.0 | -72.32 | -19.04 | -72.35 | 1433 |
| 64 | ROC + volume | momentum | 76.18 | -23.82 | 327 | 20.2 | -73.30 | -17.04 | -73.60 | 1650 |
| 65 | Squeeze breakout | breakout | 75.60 | -24.41 | 265 | 14.7 | -62.16 | -18.38 | -62.21 | 1215 |
| 66 | Donchian 55/20 | breakout | 73.97 | -26.03 | 269 | 16.7 | -68.93 | -15.02 | -68.93 | 1292 |
| 67 | EMA 20/50 cross | trend | 72.89 | -27.11 | 275 | 17.8 | -77.83 | -15.70 | -77.83 | 1462 |
| 68 | Volume breakout | breakout | 72.78 | -27.22 | 216 | 12.0 | -64.57 | -18.90 | -64.58 | 912 |
| 69 | VWAP reversion | reversion | 72.64 | -27.36 | 324 | 27.5 | -70.17 | -15.92 | -70.42 | 1392 |
| 70 | Supertrend | trend | 68.58 | -31.42 | 374 | 19.3 | -86.81 | -21.51 | -86.81 | 1924 |
| 71 | MFI reversion | reversion | 66.15 | -33.85 | 407 | 21.6 | -87.54 | -29.46 | -87.54 | 2112 |
| 72 | Keltner breakout | breakout | 65.97 | -34.03 | 366 | 12.6 | -85.23 | -29.34 | -85.25 | 1875 |
| 73 | Ichimoku | trend | 65.78 | -34.22 | 330 | 9.1 | -81.69 | -23.55 | -81.70 | 1731 |
| 74 | AI bee: Bizzy | ai | 64.97 | -35.03 | 654 | 8.4 | — | — | — | — |
| 75 | Z-score reversion | reversion | 64.94 | -35.06 | 416 | 24.3 | -85.52 | -24.27 | -85.52 | 2071 |
| 76 | ADX DI cross | trend | 62.70 | -37.30 | 425 | 8.7 | -89.62 | -35.01 | -89.63 | 2107 |
| 77 | AI bee: Boozy | ai | 62.68 | -37.32 | 227 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.48 | -38.52 | 508 | 17.5 | -91.04 | -26.53 | -91.06 | 2663 |
| 79 | MACD zero-line | trend | 61.37 | -38.63 | 479 | 14.8 | -91.38 | -29.58 | -91.38 | 2356 |
| 80 | RSI momentum | momentum | 59.88 | -40.12 | 478 | 16.1 | -90.48 | -25.79 | -90.48 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.00 | -28.14 | -91.01 | 2323 |
| 82 | Triple EMA stack | trend | 58.93 | -41.07 | 518 | 15.1 | -93.32 | -31.23 | -93.32 | 2619 |
| 83 | Bollinger breakout | breakout | 57.38 | -42.62 | 530 | 13.4 | -93.83 | -34.17 | -93.85 | 2828 |
| 84 | Consensus | meta | 55.97 | -44.03 | 507 | 9.9 | -94.42 | -25.89 | -94.42 | 2687 |
| 85 | EMA 9/21 cross | trend | 53.69 | -46.31 | 653 | 15.8 | -97.36 | -33.55 | -97.37 | 3527 |
| 86 | Stochastic reversion | reversion | 53.29 | -46.72 | 764 | 22.1 | -95.61 | -34.69 | -95.61 | 4035 |
| 87 | Connors RSI(2) | reversion | 52.95 | -47.05 | 697 | 19.9 | -96.36 | -32.31 | -96.36 | 3593 |
| 88 | Bollinger reversion | reversion | 52.33 | -47.67 | 717 | 16.7 | -95.79 | -34.16 | -95.80 | 3695 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.67 | -98.65 | 5335 |
| 90 | OBV trend | momentum | 50.49 | -49.51 | 755 | 14.4 | -96.44 | -37.56 | -96.44 | 3599 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.31 | -37.41 | -99.31 | 5593 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.62 | -99.73 | 6124 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.18 | -97.39 | 3661 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -38.05 | -98.48 | 4683 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.69 | -99.51 | 6091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.07 | -99.90 | 8252 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T06:00 | Bollinger reversion · 1h | buy | BTC-USD | 9.52 | — | entry signal |
| 2026-10-08T06:00 | Squeeze breakout | sell | BTC-USD | 18.76 | -0.18 | stop-loss |
| 2026-10-08T06:00 | Bollinger breakout | sell | BTC-USD | 14.25 | -0.14 | stop-loss |
| 2026-10-08T06:00 | MACD zero-line | buy | BTC-USD | 8.44 | — | rebalance up |
| 2026-10-08T06:00 | MACD zero-line | sell | ETH-USD | 15.23 | -0.18 | stop-loss |
| 2026-10-08T06:00 | EMA 9/21 cross | buy | BTC-USD | 10.26 | — | entry |
| 2026-10-08T06:00 | EMA 9/21 cross | sell | ETH-USD | 10.26 | -0.12 | stop-loss |
| 2026-10-08T05:55 | MFI reversion | buy | SOL-USD | 1.98 | — | entry |
| 2026-10-08T05:55 | MFI reversion | buy | BTC-USD | 11.21 | — | rebalance up |
| 2026-10-08T05:55 | MFI reversion | sell | ETH-USD | 13.18 | -0.08 | exit signal |
| 2026-10-08T05:55 | Bollinger breakout | sell | ETH-USD | 2.25 | -0.02 | exit signal |
| 2026-10-08T05:45 | ADX DI cross | sell | BTC-USD | 15.59 | -0.12 | exit signal |
| 2026-10-08T05:40 | MACD zero-line | buy | BTC-USD | 6.97 | — | entry signal |
| 2026-10-08T05:35 | AI bee: Bizzy | sell | SOL-USD | 9.02 | -0.05 | Jev: sell (sell p=0.58) after 10 min |
| 2026-10-08T05:35 | ADX DI cross | buy | BTC-USD | 15.71 | — | entry signal |
| 2026-10-08T05:35 | MACD zero-line | buy | ETH-USD | 15.40 | — | entry signal |
| 2026-10-08T05:33 | AI bee: Boozy | sell | ETH-USD | 19.28 | -0.09 | Jev: buy |
| 2026-10-08T05:25 | AI bee: Bizzy | buy | SOL-USD | 9.07 | — | Jev: buy (buy p=0.56) |
| 2026-10-08T05:25 | MFI reversion | buy | BTC-USD | 3.31 | — | rebalance up |
| 2026-10-08T05:25 | MFI reversion | sell | ETH-USD | 3.31 | -0.01 | rebalance down |
| 2026-10-08T05:25 | VWAP reversion | sell | SOL-USD | 18.19 | 0.00 | exit signal |
| 2026-10-08T05:25 | Z-score reversion | buy | XRP-USD | 3.29 | — | rebalance up |
| 2026-10-08T05:25 | Z-score reversion | buy | DOGE-USD | 3.28 | — | rebalance up |
| 2026-10-08T05:25 | Z-score reversion | sell | ETH-USD | 13.07 | -0.03 | exit signal |
| 2026-10-08T05:25 | Z-score reversion | sell | BTC-USD | 13.05 | -0.04 | exit signal |
| 2026-10-08T05:25 | Bollinger reversion | sell | XRP-USD | 13.08 | 0.02 | exit signal |
| 2026-10-08T05:25 | Bollinger reversion | sell | DOGE-USD | 13.09 | -0.06 | exit signal |
| 2026-10-08T05:25 | RSI(14) reversion | buy | DOGE-USD | 2.73 | — | entry |
| 2026-10-08T05:25 | RSI(14) reversion | sell | BTC-USD | 2.73 | -0.01 | exit signal |
| 2026-10-08T05:25 | Squeeze breakout | buy | BTC-USD | 18.94 | — | entry signal |
| 2026-10-08T05:25 | Bollinger breakout | buy | ETH-USD | 2.27 | — | entry signal |
| 2026-10-08T05:25 | Bollinger breakout | buy | BTC-USD | 14.38 | — | entry signal |
| 2026-10-08T05:25 | Donchian 20/10 | buy | BTC-USD | 11.30 | — | entry signal |
| 2026-10-08T05:25 | Supertrend | buy | BTC-USD | 6.59 | — | entry signal |
| 2026-10-08T05:25 | EMA 9/21 cross | buy | ETH-USD | 10.38 | — | entry signal |
| 2026-10-08T05:17 | AI bee: Boozy | buy | ETH-USD | 19.37 | — | Jev: buy (buy p=0.70) |
| 2026-10-08T05:15 | Bollinger reversion | sell | SOL-USD | 13.12 | -0.04 | exit signal |
| 2026-10-08T05:07 | Z-score reversion | buy | XRP-USD | 3.25 | — | rebalance up |
| 2026-10-08T05:07 | Z-score reversion | sell | SOL-USD | 3.25 | -0.02 | rebalance down |
| 2026-10-08T05:05 | Z-score reversion | buy | XRP-USD | 9.78 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 06:00:05.000152+00:00 -> 2026-10-08 06:10:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
