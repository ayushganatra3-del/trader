# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T03:01:05.000129+00:00 · 15102 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.63 (-3.37%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.06 |
| ETHU | 19.45 | +0.06 |

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

Today: 2250 decisions in 450 calls, $0.0315 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T03:01 | 2 / 3 / 0 | PLTR 15% |  |
| Breezy | 2026-10-08T03:01 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T03:01 | 4 / 1 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.66 | 5.66 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.14 | 2.14 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.54 | 1.54 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.24 | 1.24 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.06 | 1.06 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.60 | 0.60 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.57 | 0.57 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.51 | 0.51 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.81 | -0.19 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.52 | -0.48 | 0 | — | 29.00 | 3.47 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.76 | -1.24 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.44 | -1.56 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.44 | -1.56 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.38 | -1.61 | 34 | 5.9 | 7.47 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.49 | -2.51 | 62 | 58.1 | -10.54 | -2.09 | -11.21 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.31 | -2.69 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.18 | -2.82 | 16 | 43.8 | 3.75 | 1.06 | -6.57 | 115 |
| 26 | Connors RSI(2) · 1h | reversion | 97.01 | -2.99 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 27 | Daily: Momentum burst | daily | 96.75 | -3.25 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Agent | meta | 96.63 | -3.37 | 42 | 57.1 | -11.14 | -6.08 | -11.47 | 256 |
| 29 | Z-score reversion · 1h | reversion | 96.58 | -3.42 | 28 | 46.4 | 0.61 | 0.25 | -8.60 | 159 |
| 30 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 0.35 | 0.19 | -10.39 | 279 |
| 31 | Copy: Insider buying | copy | 96.43 | -3.57 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 32 | Candlestick reversal · 1h | reversion | 96.39 | -3.61 | 81 | 34.6 | -26.15 | -5.88 | -26.78 | 481 |
| 33 | Supertrend · 1h | trend | 95.74 | -4.26 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.46 | -4.54 | 80 | 21.2 | -6.67 | -0.77 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.14 | -4.86 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.11 | -4.89 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -4.71 | -1.76 | -6.03 | 114 |
| 38 | Agent (ML meta-label) | meta | 94.92 | -5.08 | 287 | 15.7 | 0.03 | 0.14 | -12.57 | 366 |
| 39 | MACD cross · 1h | trend | 94.90 | -5.10 | 100 | 23.0 | -11.76 | -1.65 | -17.27 | 466 |
| 40 | Max aggression: 1-day momentum | meta | 94.86 | -5.14 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.13 | -5.87 | 51 | 3.9 | -3.51 | -0.34 | -18.16 | 221 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.85 | -6.16 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.53 | -6.47 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | MFI reversion · 1h | reversion | 93.52 | -6.48 | 84 | 28.6 | -11.17 | -1.90 | -16.99 | 122 |
| 47 | Bollinger breakout · 1h | breakout | 93.51 | -6.49 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 48 | Triple EMA stack · 1h | trend | 93.17 | -6.83 | 61 | 11.5 | -8.68 | -0.87 | -24.26 | 242 |
| 49 | Williams %R · 1h | reversion | 93.10 | -6.90 | 93 | 49.5 | -22.45 | -4.06 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.73 | -7.27 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 51 | Opening range 15m | breakout | 92.17 | -7.83 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.13 | -8.87 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.13 | -8.87 | 90 | 11.1 | -4.65 | -0.42 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 91.11 | -8.89 | 80 | 45.0 | -5.28 | -0.64 | -12.41 | 406 |
| 55 | MACD zero-line · 1h | trend | 90.53 | -9.47 | 57 | 19.3 | -4.96 | -0.47 | -19.00 | 237 |
| 56 | VWAP momentum · 1h | momentum | 90.49 | -9.51 | 240 | 22.9 | -36.96 | -5.65 | -37.98 | 1275 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.59 | -24.14 | -48.59 | 583 |
| 58 | OBV trend · 1h | momentum | 89.32 | -10.68 | 126 | 16.7 | -14.58 | -1.63 | -28.48 | 330 |
| 59 | Keltner breakout · 1h | breakout | 88.95 | -11.05 | 39 | 17.9 | -8.92 | -0.99 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.90 | -11.10 | 124 | 25.0 | -31.80 | -5.41 | -35.54 | 691 |
| 61 | ROC + volume · 1h | momentum | 86.98 | -13.02 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.71 | -19.29 | 270 | 31.1 | -72.25 | -18.93 | -72.28 | 1434 |
| 64 | ROC + volume | momentum | 76.16 | -23.84 | 327 | 20.2 | -73.40 | -17.09 | -73.60 | 1652 |
| 65 | Squeeze breakout | breakout | 75.78 | -24.22 | 264 | 14.8 | -62.27 | -18.48 | -62.27 | 1217 |
| 66 | Donchian 55/20 | breakout | 73.95 | -26.05 | 269 | 16.7 | -68.79 | -14.95 | -68.93 | 1293 |
| 67 | VWAP reversion | reversion | 73.17 | -26.83 | 321 | 27.4 | -70.08 | -15.83 | -70.23 | 1392 |
| 68 | EMA 20/50 cross | trend | 72.97 | -27.03 | 274 | 17.9 | -77.70 | -15.61 | -77.73 | 1462 |
| 69 | Volume breakout | breakout | 72.77 | -27.23 | 216 | 12.0 | -64.75 | -18.90 | -64.75 | 914 |
| 70 | Supertrend | trend | 68.68 | -31.32 | 372 | 19.4 | -86.63 | -21.24 | -86.81 | 1926 |
| 71 | MFI reversion | reversion | 66.38 | -33.62 | 405 | 21.7 | -87.51 | -29.29 | -87.51 | 2111 |
| 72 | Z-score reversion | reversion | 66.38 | -33.62 | 408 | 24.8 | -85.18 | -23.72 | -85.19 | 2061 |
| 73 | Ichimoku | trend | 66.08 | -33.92 | 327 | 9.2 | -81.61 | -23.40 | -81.64 | 1731 |
| 74 | Keltner breakout | breakout | 65.95 | -34.05 | 366 | 12.6 | -85.33 | -29.43 | -85.33 | 1879 |
| 75 | AI bee: Bizzy | ai | 65.13 | -34.87 | 652 | 8.4 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.87 | -37.13 | 423 | 8.7 | -89.68 | -34.90 | -89.69 | 2113 |
| 77 | AI bee: Boozy | ai | 62.77 | -37.23 | 226 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.67 | -38.33 | 506 | 17.6 | -90.97 | -26.31 | -91.01 | 2662 |
| 79 | MACD zero-line | trend | 61.59 | -38.41 | 478 | 14.9 | -91.41 | -29.60 | -91.41 | 2359 |
| 80 | RSI momentum | momentum | 60.16 | -39.84 | 475 | 16.2 | -90.43 | -25.67 | -90.44 | 2372 |
| 81 | Trend pullback | trend | 59.85 | -40.16 | 495 | 15.4 | -91.13 | -28.58 | -91.13 | 2331 |
| 82 | Triple EMA stack | trend | 58.90 | -41.10 | 518 | 15.1 | -93.25 | -30.99 | -93.28 | 2619 |
| 83 | Bollinger breakout | breakout | 57.51 | -42.49 | 528 | 13.4 | -93.84 | -34.04 | -93.84 | 2830 |
| 84 | Consensus | meta | 55.96 | -44.04 | 507 | 9.9 | -94.50 | -26.03 | -94.50 | 2695 |
| 85 | EMA 9/21 cross | trend | 53.95 | -46.05 | 650 | 15.8 | -97.34 | -33.25 | -97.35 | 3529 |
| 86 | Stochastic reversion | reversion | 53.77 | -46.23 | 760 | 22.2 | -95.58 | -34.33 | -95.58 | 4034 |
| 87 | Bollinger reversion | reversion | 53.36 | -46.65 | 707 | 16.8 | -95.72 | -33.58 | -95.72 | 3690 |
| 88 | Connors RSI(2) | reversion | 53.22 | -46.78 | 694 | 20.0 | -96.39 | -32.53 | -96.39 | 3599 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.50 | -98.65 | 5336 |
| 90 | OBV trend | momentum | 50.60 | -49.40 | 753 | 14.5 | -96.38 | -37.15 | -96.39 | 3596 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -36.75 | -99.30 | 5580 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.25 | -99.73 | 6129 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -39.96 | -97.38 | 3667 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -37.27 | -98.45 | 4677 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -40.33 | -99.50 | 6088 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.58 | -99.90 | 8252 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T03:00 | AI bee: Boozy | sell | ETH-USD | 19.37 | -0.14 | Jev: sell |
| 2026-10-08T03:00 | Candlestick reversal · 1h | buy | XRP-USD | 16.07 | — | entry signal |
| 2026-10-08T03:00 | VWAP momentum · 1h | buy | XRP-USD | 5.03 | — | entry signal |
| 2026-10-08T03:00 | VWAP momentum · 1h | buy | SOL-USD | 5.03 | — | entry signal |
| 2026-10-08T03:00 | VWAP momentum · 1h | buy | ETH-USD | 5.03 | — | entry signal |
| 2026-10-08T03:00 | Ichimoku | buy | SOL-USD | 16.53 | — | entry signal |
| 2026-10-08T02:55 | MACD zero-line | sell | DOGE-USD | 15.30 | -0.12 | exit signal |
| 2026-10-08T02:50 | MFI reversion | buy | BTC-USD | 14.39 | — | rebalance up |
| 2026-10-08T02:50 | MFI reversion | sell | SOL-USD | 16.56 | -0.06 | exit signal |
| 2026-10-08T02:50 | MACD zero-line | buy | DOGE-USD | 15.43 | — | entry signal |
| 2026-10-08T02:44 | AI bee: Boozy | buy | ETH-USD | 19.51 | — | Jev: buy (buy p=0.70) |
| 2026-10-08T02:41 | Bollinger reversion | sell | BTC-USD | 13.29 | -0.06 | exit signal |
| 2026-10-08T02:35 | AI bee: Bizzy | sell | SOL-USD | 9.14 | -0.05 | Jev: sell (sell p=0.61) after 10 min |
| 2026-10-08T02:30 | MFI reversion | buy | BTC-USD | 2.24 | — | entry signal |
| 2026-10-08T02:25 | AI bee: Bizzy | buy | SOL-USD | 9.20 | — | Jev: buy (buy p=0.56) |
| 2026-10-08T02:25 | MFI reversion | buy | SOL-USD | 16.63 | — | entry signal |
| 2026-10-08T02:20 | Connors RSI(2) | sell | DOGE-USD | 13.23 | -0.10 | target is flat |
| 2026-10-08T02:20 | Donchian 55/20 | sell | XRP-USD | 18.42 | -0.14 | stop-loss |
| 2026-10-08T02:20 | Donchian 55/20 | sell | ETH-USD | 18.44 | -0.18 | stop-loss |
| 2026-10-08T02:20 | ADX DI cross | buy | DOGE-USD | 15.72 | — | entry signal |
| 2026-10-08T02:15 | ADX DI cross | sell | DOGE-USD | 15.64 | -0.11 | exit signal |
| 2026-10-08T02:05 | Stochastic reversion | buy | DOGE-USD | 13.45 | — | entry signal |
| 2026-10-08T02:05 | Z-score reversion | buy | BTC-USD | 16.61 | — | entry signal |
| 2026-10-08T02:05 | Bollinger reversion | buy | BTC-USD | 13.35 | — | entry signal |
| 2026-10-08T02:05 | ADX DI cross | buy | DOGE-USD | 15.75 | — | entry signal |
| 2026-10-08T02:00 | VWAP momentum · 1h | sell | XRP-USD | 4.75 | -0.03 | exit signal |
| 2026-10-08T02:00 | VWAP momentum · 1h | sell | SOL-USD | 4.73 | -0.04 | exit signal |
| 2026-10-08T02:00 | VWAP momentum · 1h | sell | ETH-USD | 4.75 | -0.02 | exit signal |
| 2026-10-08T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 4.73 | -0.05 | exit signal |
| 2026-10-08T02:00 | Heikin-Ashi · 1h | buy | XRP-USD | 9.88 | — | entry signal |
| 2026-10-08T02:00 | MFI reversion | sell | SOL-USD | 16.52 | -0.15 | stop-loss |
| 2026-10-08T02:00 | Connors RSI(2) | buy | DOGE-USD | 13.33 | — | entry signal |
| 2026-10-08T02:00 | Squeeze breakout | sell | XRP-USD | 18.87 | -0.15 | exit signal |
| 2026-10-08T02:00 | Keltner breakout | sell | XRP-USD | 16.48 | -0.10 | exit signal |
| 2026-10-08T02:00 | Keltner breakout | sell | ETH-USD | 16.41 | -0.14 | exit signal |
| 2026-10-08T02:00 | Bollinger breakout | sell | XRP-USD | 14.33 | -0.09 | exit signal |
| 2026-10-08T02:00 | Donchian 55/20 | buy | XRP-USD | 18.56 | — | entry |
| 2026-10-08T02:00 | Donchian 55/20 | sell | DOGE-USD | 18.53 | -0.10 | exit signal |
| 2026-10-08T02:00 | EMA 9/21 cross | buy | ETH-USD | 10.55 | — | entry |
| 2026-10-08T02:00 | EMA 9/21 cross | sell | DOGE-USD | 10.55 | -0.05 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 03:01:05.000129+00:00 -> 2026-10-08 03:11:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
