# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T00:00:05.000113+00:00 · 14953 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.62 (-3.38%)

Closed trades 41, win rate 56.1%, fees £1.82, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.06 |
| DOGE-USD | 19.40 | -0.01 |
| ETHU | 19.45 | +0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 15 decisions in 3 calls, $0.0002 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T00:00 | 0 / 3 / 2 | PLTR 14% |  |
| Breezy | 2026-10-08T00:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T00:00 | 3 / 1 / 1 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.34 | +4.22% | 5 |
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| Stochastic reversion · 1h | XRP-USD | 2.19 | +4.46% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| RSI(14) reversion | ETHU | 1.93 | +0.48% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.68 | 5.68 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.64 | 2.64 | 30 | 46.7 | -9.21 | -2.89 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.15 | 2.15 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.56 | 1.56 | 0 | — | 2.17 | 1.07 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.25 | 1.25 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.08 | 1.08 | 18 | 5.6 | 11.49 | 1.58 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.62 | 0.62 | 4 | 50.0 | -4.52 | -1.56 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.58 | 0.58 | 0 | — | -2.78 | -1.12 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.51 | 0.51 | 28 | 39.3 | 5.12 | 2.44 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.77 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.83 | -0.17 | 0 | — | -4.16 | -2.03 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.72 | -0.28 | 0 | — | 29.01 | 3.50 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.34 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.77 | -1.23 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.46 | -1.54 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.46 | -1.54 | 68 | 23.5 | -20.89 | -6.03 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.40 | -1.60 | 34 | 5.9 | 7.47 | 1.03 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.03 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.50 | -2.50 | 61 | 59.0 | -10.53 | -2.10 | -11.21 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.34 | -2.66 | 0 | — | 12.75 | 2.08 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.18 | -2.82 | 16 | 43.8 | 3.40 | 0.98 | -6.57 | 114 |
| 26 | Connors RSI(2) · 1h | reversion | 97.03 | -2.97 | 77 | 44.2 | -15.42 | -5.66 | -17.97 | 231 |
| 27 | Daily: Momentum burst | daily | 96.76 | -3.24 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Agent | meta | 96.62 | -3.38 | 41 | 56.1 | -11.09 | -6.13 | -11.41 | 256 |
| 29 | Z-score reversion · 1h | reversion | 96.55 | -3.45 | 28 | 46.4 | 0.53 | 0.23 | -8.60 | 159 |
| 30 | Agent (rotation) | meta | 96.53 | -3.47 | 70 | 28.6 | 1.53 | 0.52 | -10.39 | 277 |
| 31 | Copy: Insider buying | copy | 96.45 | -3.55 | 11 | 54.5 | -17.32 | -3.20 | -21.08 | 74 |
| 32 | Candlestick reversal · 1h | reversion | 96.42 | -3.58 | 81 | 34.6 | -25.88 | -5.90 | -26.51 | 479 |
| 33 | Supertrend · 1h | trend | 95.75 | -4.25 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.47 | -4.53 | 80 | 21.2 | -6.67 | -0.78 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.15 | -4.84 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.12 | -4.88 | 55 | 41.8 | -17.17 | -4.32 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.04 | -4.96 | 19 | 47.4 | -4.73 | -1.78 | -6.03 | 114 |
| 38 | Agent (ML meta-label) | meta | 94.94 | -5.06 | 286 | 15.7 | 0.72 | 0.27 | -12.66 | 364 |
| 39 | MACD cross · 1h | trend | 94.93 | -5.07 | 100 | 23.0 | -11.90 | -1.68 | -17.27 | 466 |
| 40 | Max aggression: 1-day momentum | meta | 94.87 | -5.13 | 8 | 37.5 | -21.09 | -1.02 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.54 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.14 | -5.86 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.95 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.86 | -6.14 | 104 | 21.2 | -17.38 | -5.32 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.53 | -6.47 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.52 | -6.48 | 63 | 30.2 | 7.62 | 1.13 | -12.06 | 290 |
| 47 | MFI reversion · 1h | reversion | 93.50 | -6.50 | 84 | 28.6 | -11.28 | -1.94 | -16.99 | 123 |
| 48 | Triple EMA stack · 1h | trend | 93.18 | -6.82 | 61 | 11.5 | -8.81 | -0.90 | -24.26 | 243 |
| 49 | Williams %R · 1h | reversion | 93.15 | -6.85 | 91 | 49.5 | -22.43 | -4.08 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.73 | -7.27 | 44 | 15.9 | 6.79 | 1.10 | -12.60 | 122 |
| 51 | Opening range 15m | breakout | 92.18 | -7.82 | 121 | 19.8 | -19.15 | -5.59 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.14 | -8.86 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.14 | -8.86 | 90 | 11.1 | -4.65 | -0.43 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 91.12 | -8.88 | 80 | 45.0 | -5.13 | -0.62 | -12.41 | 407 |
| 55 | VWAP momentum · 1h | momentum | 90.68 | -9.32 | 236 | 23.3 | -36.32 | -5.56 | -37.98 | 1267 |
| 56 | MACD zero-line · 1h | trend | 90.53 | -9.47 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 57 | Three white soldiers | momentum | 90.43 | -9.57 | 106 | 18.9 | -48.46 | -24.38 | -48.51 | 582 |
| 58 | OBV trend · 1h | momentum | 89.32 | -10.68 | 126 | 16.7 | -14.15 | -1.59 | -28.48 | 328 |
| 59 | Heikin-Ashi · 1h | trend | 88.96 | -11.04 | 124 | 25.0 | -31.95 | -5.49 | -35.56 | 690 |
| 60 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -9.08 | -1.02 | -23.68 | 226 |
| 61 | ROC + volume · 1h | momentum | 86.99 | -13.01 | 123 | 19.5 | -9.20 | -1.10 | -23.15 | 410 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.11 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.72 | -19.28 | 270 | 31.1 | -72.07 | -19.09 | -72.09 | 1428 |
| 64 | Squeeze breakout | breakout | 76.17 | -23.83 | 261 | 14.9 | -62.06 | -18.54 | -62.06 | 1215 |
| 65 | ROC + volume | momentum | 76.16 | -23.84 | 327 | 20.2 | -73.38 | -17.30 | -73.58 | 1651 |
| 66 | Donchian 55/20 | breakout | 74.49 | -25.51 | 265 | 17.0 | -68.45 | -14.92 | -68.65 | 1289 |
| 67 | VWAP reversion | reversion | 73.38 | -26.62 | 317 | 27.8 | -69.91 | -15.96 | -70.18 | 1391 |
| 68 | Volume breakout | breakout | 73.04 | -26.96 | 214 | 12.1 | -64.72 | -19.12 | -64.72 | 916 |
| 69 | EMA 20/50 cross | trend | 72.94 | -27.06 | 274 | 17.9 | -77.82 | -15.84 | -77.87 | 1467 |
| 70 | Supertrend | trend | 68.73 | -31.27 | 371 | 19.4 | -86.62 | -21.56 | -86.77 | 1926 |
| 71 | MFI reversion | reversion | 66.66 | -33.34 | 403 | 21.8 | -87.54 | -29.89 | -87.55 | 2118 |
| 72 | Keltner breakout | breakout | 66.59 | -33.41 | 359 | 12.8 | -85.17 | -29.62 | -85.17 | 1874 |
| 73 | Z-score reversion | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.31 | -24.36 | -85.31 | 2066 |
| 74 | Ichimoku | trend | 66.13 | -33.87 | 326 | 8.9 | -81.66 | -23.86 | -81.69 | 1734 |
| 75 | AI bee: Bizzy | ai | 65.50 | -34.50 | 646 | 8.5 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.31 | -36.69 | 222 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.00 | -36.99 | 422 | 8.8 | -89.65 | -35.90 | -89.65 | 2110 |
| 78 | MACD zero-line | trend | 62.07 | -37.93 | 472 | 15.0 | -91.35 | -30.00 | -91.35 | 2357 |
| 79 | Donchian 20/10 | breakout | 61.66 | -38.34 | 506 | 17.6 | -90.95 | -26.79 | -90.97 | 2662 |
| 80 | RSI momentum | momentum | 60.32 | -39.68 | 472 | 16.3 | -90.35 | -25.97 | -90.37 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.15 | -29.33 | -91.15 | 2332 |
| 82 | Triple EMA stack | trend | 58.90 | -41.09 | 518 | 15.1 | -93.17 | -31.37 | -93.19 | 2613 |
| 83 | Bollinger breakout | breakout | 57.72 | -42.27 | 523 | 13.6 | -93.80 | -34.61 | -93.80 | 2828 |
| 84 | Consensus | meta | 56.58 | -43.42 | 500 | 10.0 | -94.38 | -26.18 | -94.38 | 2685 |
| 85 | EMA 9/21 cross | trend | 54.02 | -45.98 | 649 | 15.9 | -97.35 | -34.03 | -97.35 | 3532 |
| 86 | Stochastic reversion | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.62 | -35.58 | -95.62 | 4037 |
| 87 | Bollinger reversion | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.76 | -34.73 | -95.76 | 3693 |
| 88 | Connors RSI(2) | reversion | 53.37 | -46.63 | 692 | 20.1 | -96.43 | -33.76 | -96.43 | 3603 |
| 89 | OBV trend | momentum | 50.72 | -49.28 | 752 | 14.5 | -96.38 | -38.10 | -96.38 | 3593 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -31.00 | -98.66 | 5335 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -38.06 | -99.30 | 5584 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -44.58 | -99.73 | 6131 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -40.65 | -97.35 | 3659 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -38.72 | -98.47 | 4682 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -41.96 | -99.51 | 6089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.31 | -99.90 | 8251 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T00:00 | Williams %R · 1h | buy | XRP-USD | 1.48 | — | entry signal |
| 2026-10-07T23:57 | AI bee: Bizzy | sell | DOGE-USD | 9.15 | -0.05 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-07T23:55 | Three white soldiers | sell | ETH-USD | 22.51 | -0.14 | exit signal |
| 2026-10-07T23:55 | Bollinger breakout | buy | DOGE-USD | 2.45 | — | entry |
| 2026-10-07T23:55 | Bollinger breakout | sell | BTC-USD | 2.45 | -0.02 | exit signal |
| 2026-10-07T23:50 | MFI reversion | sell | DOGE-USD | 16.67 | 0.00 | exit signal |
| 2026-10-07T23:50 | Keltner breakout | buy | DOGE-USD | 16.66 | — | entry signal |
| 2026-10-07T23:47 | AI bee: Bizzy | buy | DOGE-USD | 9.20 | — | Jev: buy (buy p=0.56) |
| 2026-10-07T23:45 | AI bee: Bizzy | sell | ETH-USD | 9.42 | -0.07 | Jev: sell (sell p=0.81) after 11 min |
| 2026-10-07T23:45 | Consensus | buy | DOGE-USD | 13.92 | — | entry |
| 2026-10-07T23:45 | Donchian 55/20 | buy | DOGE-USD | 18.63 | — | entry signal |
| 2026-10-07T23:36 | AI bee: Boozy | sell | ETH-USD | 19.91 | -0.09 | Jev: add (buy p=0.55) |
| 2026-10-07T23:34 | AI bee: Bizzy | buy | ETH-USD | 9.49 | — | Jev: buy (buy p=0.58) |
| 2026-10-07T23:30 | RSI(14) reversion | sell | BTC-USD | 2.74 | -0.01 | take-profit |
| 2026-10-07T23:30 | Keltner breakout | buy | ETH-USD | 16.67 | — | entry signal |
| 2026-10-07T23:30 | Bollinger breakout | buy | BTC-USD | 2.47 | — | entry signal |
| 2026-10-07T23:25 | Consensus | buy | ETH-USD | 14.16 | — | entry |
| 2026-10-07T23:25 | Three white soldiers | buy | ETH-USD | 22.64 | — | entry signal |
| 2026-10-07T23:23 | AI bee: Bizzy | sell | SOL-USD | 9.11 | -0.04 | Jev: sell (sell p=0.53) after 20 min |
| 2026-10-07T23:21 | AI bee: Boozy | buy | ETH-USD | 20.00 | — | Jev: buy (buy p=0.70) |
| 2026-10-07T23:20 | Squeeze breakout | buy | ETH-USD | 19.05 | — | entry signal |
| 2026-10-07T23:20 | Bollinger breakout | buy | ETH-USD | 14.45 | — | entry signal |
| 2026-10-07T23:20 | Donchian 20/10 | buy | ETH-USD | 11.46 | — | entry signal |
| 2026-10-07T23:20 | RSI momentum | buy | SOL-USD | 15.09 | — | entry signal |
| 2026-10-07T23:15 | MACD zero-line | buy | SOL-USD | 7.32 | — | entry |
| 2026-10-07T23:15 | MACD zero-line | buy | ETH-USD | 8.13 | — | rebalance up |
| 2026-10-07T23:15 | MACD zero-line | sell | DOGE-USD | 15.45 | -0.10 | exit signal |
| 2026-10-07T23:05 | MFI reversion | sell | SOL-USD | 2.34 | -0.00 | exit signal |
| 2026-10-07T23:05 | MACD zero-line | buy | ETH-USD | 7.42 | — | entry signal |
| 2026-10-07T23:03 | AI bee: Bizzy | buy | SOL-USD | 9.15 | — | Jev: buy (buy p=0.56) |
| 2026-10-07T23:01 | VWAP reversion · 1h | sell | ETH-USD | 5.11 | -0.03 | rebalance down |
| 2026-10-07T23:00 | Agent (rotation) | buy | XRP-USD | 6.43 | — | following Stochastic reversion · 1h |
| 2026-10-07T23:00 | Agent (rotation) | buy | SOL-USD | 6.43 | — | entry |
| 2026-10-07T23:00 | VWAP reversion · 1h | buy | XRP-USD | 20.51 | — | entry signal |
| 2026-10-07T23:00 | VWAP reversion · 1h | buy | SOL-USD | 20.51 | — | entry signal |
| 2026-10-07T22:45 | ADX DI cross | sell | SOL-USD | 15.68 | -0.09 | exit signal |
| 2026-10-07T22:41 | AI bee: Bizzy | sell | DOGE-USD | 9.75 | -0.08 | Jev: sell (sell p=0.72) after 12 min |
| 2026-10-07T22:41 | MFI reversion · 1h | buy | SOL-USD | 5.35 | — | rebalance up |
| 2026-10-07T22:41 | MFI reversion · 1h | buy | ETH-USD | 5.35 | — | rebalance up |
| 2026-10-07T22:41 | MFI reversion · 1h | buy | DOGE-USD | 5.30 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 00:00:05.000113+00:00 -> 2026-10-08 00:10:05.000113+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
