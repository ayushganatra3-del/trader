# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T00:30:05.000155+00:00 · 14982 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.66 (-3.33%)

Closed trades 41, win rate 56.1%, fees £1.82, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.07 |
| DOGE-USD | 19.43 | +0.03 |
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
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 450 decisions in 90 calls, $0.0063 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T00:30 | 0 / 0 / 5 | PLTR 14% |  |
| Breezy | 2026-10-08T00:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T00:30 | 0 / 4 / 1 | DOGE-USD 31% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.95 | +0.75% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.70 | 5.70 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.66 | 2.66 | 30 | 46.7 | -9.20 | -2.87 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.17 | 2.17 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.58 | 1.58 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.27 | 1.27 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.10 | 1.10 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.64 | 0.64 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.60 | 0.60 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.51 | 0.51 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.84 | -0.16 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.66 | -0.34 | 0 | — | 28.83 | 3.45 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.79 | -1.21 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.47 | -1.52 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.47 | -1.53 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.41 | -1.59 | 34 | 5.9 | 7.46 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.52 | -2.48 | 61 | 59.0 | -10.45 | -2.07 | -11.21 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.36 | -2.64 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.17 | -2.83 | 16 | 43.8 | 3.40 | 0.97 | -6.57 | 114 |
| 26 | Connors RSI(2) · 1h | reversion | 97.04 | -2.96 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 27 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Agent | meta | 96.66 | -3.33 | 41 | 56.1 | -10.34 | -5.50 | -10.70 | 254 |
| 29 | Z-score reversion · 1h | reversion | 96.57 | -3.43 | 28 | 46.4 | 0.53 | 0.23 | -8.60 | 159 |
| 30 | Agent (rotation) | meta | 96.54 | -3.46 | 70 | 28.6 | 1.54 | 0.52 | -10.39 | 277 |
| 31 | Copy: Insider buying | copy | 96.46 | -3.54 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 32 | Candlestick reversal · 1h | reversion | 96.41 | -3.59 | 81 | 34.6 | -25.90 | -5.86 | -26.51 | 479 |
| 33 | Supertrend · 1h | trend | 95.76 | -4.24 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.48 | -4.52 | 80 | 21.2 | -6.67 | -0.77 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.17 | -4.83 | 47 | 14.9 | -6.46 | -0.90 | -13.84 | 251 |
| 36 | Bollinger reversion · 1h | reversion | 95.13 | -4.87 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.13 | -4.87 | 19 | 47.4 | -4.27 | -1.57 | -6.03 | 114 |
| 38 | Agent (ML meta-label) | meta | 94.96 | -5.04 | 286 | 15.7 | 1.80 | 0.47 | -12.82 | 368 |
| 39 | MACD cross · 1h | trend | 94.94 | -5.06 | 100 | 23.0 | -11.90 | -1.67 | -17.27 | 466 |
| 40 | Max aggression: 1-day momentum | meta | 94.89 | -5.11 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.11 | 2.51 | -8.12 | 102 |
| 42 | RSI momentum · 1h | momentum | 94.16 | -5.84 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.88 | -6.12 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.54 | -6.46 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.52 | -6.48 | 63 | 30.2 | 7.56 | 1.12 | -12.06 | 290 |
| 47 | MFI reversion · 1h | reversion | 93.52 | -6.48 | 84 | 28.6 | -11.28 | -1.92 | -16.99 | 123 |
| 48 | Triple EMA stack · 1h | trend | 93.19 | -6.80 | 61 | 11.5 | -8.93 | -0.90 | -24.26 | 243 |
| 49 | Williams %R · 1h | reversion | 93.17 | -6.83 | 91 | 49.5 | -22.43 | -4.05 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.77 | 1.09 | -12.60 | 122 |
| 51 | Opening range 15m | breakout | 92.20 | -7.80 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.15 | -8.85 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.15 | -8.85 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 91.14 | -8.86 | 80 | 45.0 | -5.35 | -0.66 | -12.41 | 406 |
| 55 | VWAP momentum · 1h | momentum | 90.70 | -9.30 | 236 | 23.3 | -36.48 | -5.55 | -37.98 | 1268 |
| 56 | MACD zero-line · 1h | trend | 90.54 | -9.46 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 57 | Three white soldiers | momentum | 90.43 | -9.57 | 106 | 18.9 | -48.46 | -23.93 | -48.51 | 582 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.14 | -1.57 | -28.48 | 328 |
| 59 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -9.49 | -1.07 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.96 | -11.04 | 124 | 25.0 | -31.95 | -5.44 | -35.56 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.00 | -13.00 | 123 | 19.5 | -8.98 | -1.06 | -23.15 | 409 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.73 | -19.27 | 270 | 31.1 | -72.00 | -18.76 | -72.03 | 1427 |
| 64 | ROC + volume | momentum | 76.17 | -23.83 | 327 | 20.2 | -73.38 | -17.08 | -73.58 | 1651 |
| 65 | Squeeze breakout | breakout | 76.10 | -23.90 | 262 | 14.9 | -62.09 | -18.32 | -62.09 | 1215 |
| 66 | Donchian 55/20 | breakout | 74.44 | -25.56 | 265 | 17.0 | -68.48 | -14.76 | -68.65 | 1290 |
| 67 | VWAP reversion | reversion | 73.18 | -26.82 | 321 | 27.4 | -70.02 | -15.85 | -70.18 | 1391 |
| 68 | Volume breakout | breakout | 73.04 | -26.96 | 214 | 12.1 | -64.72 | -18.85 | -64.72 | 916 |
| 69 | EMA 20/50 cross | trend | 72.94 | -27.06 | 274 | 17.9 | -77.77 | -15.63 | -77.87 | 1466 |
| 70 | Supertrend | trend | 68.76 | -31.24 | 371 | 19.4 | -86.62 | -21.21 | -86.78 | 1926 |
| 71 | MFI reversion | reversion | 66.67 | -33.33 | 403 | 21.8 | -87.54 | -29.17 | -87.55 | 2118 |
| 72 | Keltner breakout | breakout | 66.48 | -33.52 | 360 | 12.8 | -85.19 | -29.00 | -85.19 | 1875 |
| 73 | Z-score reversion | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.24 | -23.80 | -85.24 | 2064 |
| 74 | Ichimoku | trend | 66.16 | -33.84 | 326 | 8.9 | -81.65 | -23.41 | -81.69 | 1734 |
| 75 | AI bee: Bizzy | ai | 65.38 | -34.62 | 648 | 8.5 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.23 | -36.77 | 222 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.01 | -36.99 | 422 | 8.8 | -89.63 | -34.75 | -89.63 | 2109 |
| 78 | MACD zero-line | trend | 61.91 | -38.09 | 475 | 14.9 | -91.40 | -29.49 | -91.40 | 2359 |
| 79 | Donchian 20/10 | breakout | 61.66 | -38.34 | 506 | 17.6 | -90.95 | -26.23 | -90.98 | 2662 |
| 80 | RSI momentum | momentum | 60.34 | -39.66 | 472 | 16.3 | -90.33 | -25.42 | -90.39 | 2368 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.13 | -28.58 | -91.13 | 2331 |
| 82 | Triple EMA stack | trend | 58.92 | -41.09 | 518 | 15.1 | -93.18 | -30.57 | -93.19 | 2614 |
| 83 | Bollinger breakout | breakout | 57.68 | -42.32 | 524 | 13.5 | -93.83 | -33.71 | -93.83 | 2830 |
| 84 | Consensus | meta | 56.34 | -43.66 | 503 | 9.9 | -94.40 | -25.73 | -94.40 | 2686 |
| 85 | EMA 9/21 cross | trend | 54.05 | -45.95 | 649 | 15.9 | -97.35 | -33.16 | -97.35 | 3533 |
| 86 | Stochastic reversion | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.62 | -34.47 | -95.62 | 4037 |
| 87 | Bollinger reversion | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.76 | -33.69 | -95.76 | 3693 |
| 88 | Connors RSI(2) | reversion | 53.37 | -46.62 | 692 | 20.1 | -96.41 | -32.71 | -96.41 | 3602 |
| 89 | OBV trend | momentum | 50.72 | -49.28 | 752 | 14.5 | -96.38 | -36.77 | -96.38 | 3593 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.35 | -98.65 | 5333 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -36.75 | -99.30 | 5584 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.78 | -99.73 | 6129 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -39.29 | -97.36 | 3662 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.36 | -98.47 | 4682 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.28 | -99.51 | 6089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.01 | -99.90 | 8251 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T00:30 | Consensus | sell | SOL-USD | 13.67 | -0.11 | target is flat |
| 2026-10-08T00:30 | MACD zero-line | sell | BTC-USD | 7.19 | -0.06 | exit signal |
| 2026-10-08T00:28 | AI bee: Bizzy | sell | XRP-USD | 9.05 | -0.07 | Jev: sell (sell p=0.76) after 10 min |
| 2026-10-08T00:28 | AI bee: Bizzy | sell | DOGE-USD | 13.53 | -0.06 | Jev: sell (sell p=0.57) after 11 min |
| 2026-10-08T00:20 | Consensus | buy | SOL-USD | 13.79 | — | entry |
| 2026-10-08T00:20 | RSI(14) reversion · 1h | buy | XRP-USD | 5.00 | — | entry |
| 2026-10-08T00:20 | RSI(14) reversion · 1h | sell | DOGE-USD | 4.87 | -0.00 | rebalance down |
| 2026-10-08T00:20 | VWAP reversion | sell | ETH-USD | 18.30 | -0.05 | exit signal |
| 2026-10-08T00:20 | VWAP reversion | sell | BTC-USD | 18.30 | -0.10 | exit signal |
| 2026-10-08T00:20 | Keltner breakout | buy | SOL-USD | 16.65 | — | entry signal |
| 2026-10-08T00:20 | Donchian 55/20 | buy | SOL-USD | 18.64 | — | entry signal |
| 2026-10-08T00:20 | MACD zero-line | buy | BTC-USD | 7.24 | — | entry signal |
| 2026-10-08T00:19 | AI bee: Boozy | buy | DOGE-USD | 19.91 | — | Jev: buy (buy p=0.70) |
| 2026-10-08T00:18 | AI bee: Bizzy | buy | XRP-USD | 9.12 | — | Jev: buy (buy p=0.56) |
| 2026-10-08T00:17 | AI bee: Bizzy | buy | DOGE-USD | 13.59 | — | Jev: buy (buy p=0.83) |
| 2026-10-08T00:15 | Consensus | buy | DOGE-USD | 14.12 | — | entry |
| 2026-10-08T00:15 | VWAP reversion · 1h | sell | DOGE-USD | 5.12 | -0.02 | rebalance down |
| 2026-10-08T00:15 | VWAP reversion | sell | SOL-USD | 10.28 | -0.04 | exit signal |
| 2026-10-08T00:10 | Consensus | sell | DOGE-USD | 13.83 | -0.09 | target is flat |
| 2026-10-08T00:10 | VWAP reversion | buy | SOL-USD | 6.66 | — | rebalance up |
| 2026-10-08T00:10 | VWAP reversion | buy | ETH-USD | 5.07 | — | rebalance up |
| 2026-10-08T00:10 | VWAP reversion | buy | BTC-USD | 3.68 | — | rebalance up |
| 2026-10-08T00:10 | VWAP reversion | sell | DOGE-USD | 15.41 | -0.04 | target is flat |
| 2026-10-08T00:10 | MACD zero-line | buy | XRP-USD | 15.52 | — | entry |
| 2026-10-08T00:10 | MACD zero-line | sell | SOL-USD | 7.28 | -0.04 | exit signal |
| 2026-10-08T00:10 | MACD zero-line | sell | ETH-USD | 15.48 | -0.08 | exit signal |
| 2026-10-08T00:05 | Consensus | sell | ETH-USD | 14.07 | -0.09 | target is flat |
| 2026-10-08T00:05 | Squeeze breakout | sell | ETH-USD | 18.94 | -0.12 | stop-loss |
| 2026-10-08T00:05 | Keltner breakout | sell | ETH-USD | 16.55 | -0.12 | stop-loss |
| 2026-10-08T00:05 | Bollinger breakout | buy | XRP-USD | 2.37 | — | entry |
| 2026-10-08T00:05 | Bollinger breakout | buy | DOGE-USD | 11.98 | — | rebalance up |
| 2026-10-08T00:05 | Bollinger breakout | sell | ETH-USD | 14.36 | -0.09 | stop-loss |
| 2026-10-08T00:00 | Williams %R · 1h | buy | XRP-USD | 1.48 | — | entry signal |
| 2026-10-07T23:57 | AI bee: Bizzy | sell | DOGE-USD | 9.15 | -0.05 | Jev: sell (sell p=0.74) after 10 min |
| 2026-10-07T23:55 | Three white soldiers | sell | ETH-USD | 22.51 | -0.14 | exit signal |
| 2026-10-07T23:55 | Bollinger breakout | buy | DOGE-USD | 2.45 | — | entry |
| 2026-10-07T23:55 | Bollinger breakout | sell | BTC-USD | 2.45 | -0.02 | exit signal |
| 2026-10-07T23:50 | MFI reversion | sell | DOGE-USD | 16.67 | 0.00 | exit signal |
| 2026-10-07T23:50 | Keltner breakout | buy | DOGE-USD | 16.66 | — | entry signal |
| 2026-10-07T23:47 | AI bee: Bizzy | buy | DOGE-USD | 9.20 | — | Jev: buy (buy p=0.56) |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 00:30:05.000155+00:00 -> 2026-10-08 00:40:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
