# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T10:30:05.000320+00:00 · 15486 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.71 (-3.29%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.48 | +0.10 |
| ETHU | 19.49 | +0.11 |

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

Today: 8000 decisions in 1600 calls, $0.1122 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T10:30 | 0 / 0 / 5 | PLTR 15% |  |
| Breezy | 2026-10-08T10:30 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T10:30 | 1 / 4 / 0 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.89 | 5.89 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.36 | 2.36 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.76 | 1.76 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.46 | 1.46 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.28 | 1.28 | 18 | 5.6 | 11.91 | 1.62 | -16.96 | 108 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.82 | 0.82 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.79 | 0.79 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.56 | 0.56 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 100.03 | 0.03 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 14 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 15 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 99.26 | -0.73 | 0 | — | 26.94 | 3.26 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.97 | -1.03 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.66 | -1.34 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.65 | -1.35 | 68 | 23.5 | -20.83 | -5.95 | -23.40 | 173 |
| 21 | EMA 20/50 cross · 1h | trend | 98.54 | -1.46 | 34 | 5.9 | 7.05 | 0.98 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 97.52 | -2.48 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 24 | Stochastic reversion · 1h | reversion | 97.49 | -2.51 | 62 | 58.1 | -10.97 | -2.19 | -11.26 | 340 |
| 25 | Connors RSI(2) · 1h | reversion | 97.21 | -2.79 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.85 | -3.15 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.71 | -3.29 | 42 | 57.1 | -9.68 | -5.52 | -10.27 | 249 |
| 28 | Copy: Insider buying | copy | 96.64 | -3.36 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 30 | Supertrend · 1h | trend | 95.89 | -4.11 | 42 | 9.5 | -3.06 | -0.26 | -17.19 | 209 |
| 31 | Parabolic SAR · 1h | trend | 95.57 | -4.43 | 80 | 21.2 | -6.92 | -0.81 | -20.87 | 294 |
| 32 | Candlestick reversal · 1h | reversion | 95.40 | -4.60 | 86 | 32.6 | -26.96 | -6.08 | -27.15 | 483 |
| 33 | RSI(14) reversion · 1h | reversion | 95.38 | -4.62 | 20 | 35.0 | 1.48 | 0.48 | -6.57 | 117 |
| 34 | Z-score reversion · 1h | reversion | 95.34 | -4.66 | 32 | 40.6 | -0.85 | -0.05 | -8.60 | 159 |
| 35 | ADX DI cross · 1h | trend | 95.30 | -4.70 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.23 | -4.77 | 55 | 41.8 | -17.23 | -4.31 | -18.92 | 311 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.36 | -0.57 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 95.07 | -4.93 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 95.02 | -4.99 | 290 | 15.5 | 0.56 | 0.24 | -11.96 | 353 |
| 40 | MACD cross · 1h | trend | 94.98 | -5.03 | 101 | 22.8 | -12.33 | -1.74 | -17.27 | 466 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.79 | 2.46 | -8.12 | 102 |
| 42 | RSI momentum · 1h | momentum | 94.31 | -5.70 | 51 | 3.9 | -3.92 | -0.40 | -18.16 | 222 |
| 43 | Opening range 30m | breakout | 94.05 | -5.95 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 44 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 45 | Ichimoku · 1h | trend | 93.62 | -6.38 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.60 | -6.40 | 63 | 30.2 | 7.34 | 1.09 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.33 | -6.67 | 61 | 11.5 | -8.90 | -0.90 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.78 | -7.22 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.48 | -7.52 | 96 | 47.9 | -23.25 | -4.23 | -23.35 | 499 |
| 50 | MFI reversion · 1h | reversion | 92.38 | -7.62 | 87 | 27.6 | -12.34 | -2.12 | -16.99 | 122 |
| 51 | Opening range 15m | breakout | 92.37 | -7.63 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.30 | -8.70 | 50 | 20.0 | 2.07 | 0.46 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.27 | -8.73 | 90 | 11.1 | -4.49 | -0.40 | -18.86 | 339 |
| 54 | CCI reversion · 1h | reversion | 90.63 | -9.37 | 82 | 43.9 | -6.53 | -0.84 | -12.41 | 408 |
| 55 | MACD zero-line · 1h | trend | 90.63 | -9.37 | 57 | 19.3 | -5.36 | -0.52 | -19.00 | 239 |
| 56 | VWAP momentum · 1h | momentum | 90.39 | -9.61 | 243 | 22.6 | -36.31 | -5.52 | -38.04 | 1272 |
| 57 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.61 | -24.23 | -48.61 | 583 |
| 58 | OBV trend · 1h | momentum | 89.37 | -10.63 | 126 | 16.7 | -14.03 | -1.56 | -28.48 | 327 |
| 59 | Keltner breakout · 1h | breakout | 89.00 | -11.00 | 39 | 17.9 | -9.27 | -1.04 | -23.68 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 88.76 | -11.24 | 126 | 24.6 | -31.84 | -5.42 | -35.61 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.11 | -12.89 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.85 | -19.15 | 272 | 30.9 | -72.27 | -19.01 | -72.36 | 1434 |
| 64 | ROC + volume | momentum | 75.72 | -24.28 | 330 | 20.0 | -73.32 | -17.08 | -73.67 | 1649 |
| 65 | Squeeze breakout | breakout | 75.27 | -24.73 | 267 | 14.6 | -62.17 | -18.33 | -62.27 | 1213 |
| 66 | Donchian 55/20 | breakout | 73.74 | -26.26 | 270 | 16.7 | -68.72 | -14.88 | -68.82 | 1289 |
| 67 | VWAP reversion | reversion | 72.84 | -27.16 | 326 | 27.9 | -70.52 | -16.14 | -70.69 | 1401 |
| 68 | Volume breakout | breakout | 72.81 | -27.19 | 216 | 12.0 | -64.32 | -18.85 | -64.32 | 906 |
| 69 | EMA 20/50 cross | trend | 72.70 | -27.30 | 276 | 17.8 | -78.10 | -15.86 | -78.10 | 1468 |
| 70 | Supertrend | trend | 68.52 | -31.48 | 377 | 19.1 | -86.97 | -21.70 | -86.97 | 1929 |
| 71 | MFI reversion | reversion | 66.13 | -33.87 | 410 | 21.5 | -87.53 | -29.45 | -87.54 | 2110 |
| 72 | Keltner breakout | breakout | 65.87 | -34.13 | 367 | 12.5 | -85.26 | -29.42 | -85.26 | 1872 |
| 73 | Z-score reversion | reversion | 65.19 | -34.81 | 419 | 24.1 | -85.47 | -24.22 | -85.53 | 2071 |
| 74 | Ichimoku | trend | 64.81 | -35.19 | 338 | 8.9 | -81.83 | -23.76 | -81.83 | 1734 |
| 75 | AI bee: Bizzy | ai | 64.32 | -35.68 | 664 | 8.3 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.37 | -37.63 | 430 | 8.6 | -89.74 | -35.65 | -89.74 | 2112 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.40 | -38.60 | 511 | 17.4 | -91.19 | -26.85 | -91.19 | 2666 |
| 79 | MACD zero-line | trend | 60.79 | -39.21 | 487 | 14.6 | -91.54 | -29.98 | -91.54 | 2364 |
| 80 | Trend pullback | trend | 59.88 | -40.12 | 495 | 15.4 | -90.98 | -28.07 | -90.98 | 2321 |
| 81 | RSI momentum | momentum | 59.82 | -40.17 | 479 | 16.1 | -90.45 | -25.74 | -90.45 | 2366 |
| 82 | Triple EMA stack | trend | 59.02 | -40.98 | 518 | 15.1 | -93.30 | -31.26 | -93.30 | 2616 |
| 83 | Bollinger breakout | breakout | 56.97 | -43.03 | 535 | 13.3 | -93.90 | -34.54 | -93.90 | 2829 |
| 84 | Consensus | meta | 56.02 | -43.98 | 507 | 9.9 | -94.38 | -25.56 | -94.38 | 2683 |
| 85 | EMA 9/21 cross | trend | 53.58 | -46.42 | 656 | 15.7 | -97.41 | -33.97 | -97.41 | 3535 |
| 86 | Stochastic reversion | reversion | 53.07 | -46.93 | 773 | 22.0 | -95.62 | -34.78 | -95.62 | 4040 |
| 87 | Connors RSI(2) | reversion | 52.97 | -47.03 | 697 | 19.9 | -96.33 | -32.19 | -96.33 | 3588 |
| 88 | Bollinger reversion | reversion | 52.27 | -47.73 | 719 | 16.7 | -95.78 | -34.11 | -95.79 | 3694 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.95 | -98.69 | 5349 |
| 90 | OBV trend ⛔ | momentum | 50.35 | -49.65 | 757 | 14.4 | -96.39 | -37.46 | -96.39 | 3591 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.32 | -37.71 | -99.32 | 5596 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.84 | -99.73 | 6128 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -40.13 | -97.38 | 3659 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.94 | -98.48 | 4683 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.75 | -99.51 | 6094 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.85 | -99.90 | 8253 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T10:30 | Squeeze breakout | sell | DOGE-USD | 18.73 | -0.16 | stop-loss |
| 2026-10-08T10:30 | Bollinger breakout | sell | DOGE-USD | 14.16 | -0.13 | stop-loss |
| 2026-10-08T10:30 | Donchian 20/10 | sell | DOGE-USD | 11.07 | -0.02 | exit signal |
| 2026-10-08T10:30 | ROC + volume | sell | DOGE-USD | 18.79 | -0.18 | stop-loss |
| 2026-10-08T10:30 | Ichimoku | sell | DOGE-USD | 16.21 | -0.09 | exit signal |
| 2026-10-08T10:30 | Supertrend | buy | DOGE-USD | 6.40 | — | entry |
| 2026-10-08T10:30 | Supertrend | sell | BTC-USD | 6.40 | -0.04 | exit signal |
| 2026-10-08T10:25 | Donchian 55/20 | sell | XRP-USD | 18.24 | -0.18 | stop-loss |
| 2026-10-08T10:20 | Ichimoku | sell | XRP-USD | 16.34 | -0.08 | exit signal |
| 2026-10-08T10:20 | Ichimoku | sell | BTC-USD | 16.20 | -0.12 | exit signal |
| 2026-10-08T10:20 | MACD zero-line | sell | SOL-USD | 6.37 | -0.05 | exit signal |
| 2026-10-08T10:20 | MACD zero-line | sell | ETH-USD | 15.11 | -0.12 | exit signal |
| 2026-10-08T10:10 | Squeeze breakout | sell | XRP-USD | 18.73 | -0.16 | exit signal |
| 2026-10-08T10:10 | Bollinger breakout | buy | DOGE-USD | 12.34 | — | rebalance up |
| 2026-10-08T10:10 | Bollinger breakout | sell | XRP-USD | 14.20 | -0.09 | exit signal |
| 2026-10-08T10:10 | Ichimoku | sell | ETH-USD | 16.07 | -0.14 | exit signal |
| 2026-10-08T10:05 | AI bee: Bizzy | sell | DOGE-USD | 9.55 | -0.04 | Jev: sell (sell p=0.52) after 13 min |
| 2026-10-08T10:05 | Ichimoku | buy | ETH-USD | 16.20 | — | entry signal |
| 2026-10-08T10:00 | VWAP momentum · 1h | buy | XRP-USD | 5.03 | — | entry signal |
| 2026-10-08T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.03 | — | entry signal |
| 2026-10-08T10:00 | MACD zero-line | buy | SOL-USD | 6.42 | — | entry signal |
| 2026-10-08T09:55 | ROC + volume | buy | DOGE-USD | 18.97 | — | entry signal |
| 2026-10-08T09:55 | MACD zero-line | buy | ETH-USD | 15.24 | — | entry signal |
| 2026-10-08T09:52 | AI bee: Bizzy | buy | DOGE-USD | 9.60 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T09:50 | Ichimoku | buy | BTC-USD | 16.31 | — | entry signal |
| 2026-10-08T09:46 | AI bee: Bizzy | sell | SOL-USD | 9.13 | -0.06 | Jev: sell (sell p=0.67) after 12 min |
| 2026-10-08T09:40 | Squeeze breakout | buy | XRP-USD | 18.89 | — | entry signal |
| 2026-10-08T09:35 | Stochastic reversion | sell | ETH-USD | 13.25 | -0.03 | exit signal |
| 2026-10-08T09:35 | Bollinger reversion | sell | ETH-USD | 13.04 | -0.03 | exit signal |
| 2026-10-08T09:35 | Squeeze breakout | buy | DOGE-USD | 18.90 | — | entry signal |
| 2026-10-08T09:35 | Bollinger breakout | buy | DOGE-USD | 1.95 | — | entry signal |
| 2026-10-08T09:35 | Donchian 55/20 | buy | XRP-USD | 18.43 | — | entry signal |
| 2026-10-08T09:35 | Donchian 55/20 | buy | DOGE-USD | 18.50 | — | entry signal |
| 2026-10-08T09:34 | AI bee: Bizzy | buy | SOL-USD | 9.19 | — | Jev: buy (buy p=0.57) |
| 2026-10-08T09:25 | Ichimoku | buy | DOGE-USD | 16.31 | — | entry |
| 2026-10-08T09:20 | Ichimoku | sell | DOGE-USD | 16.30 | -0.13 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | SOL-USD | 13.26 | -0.05 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | DOGE-USD | 13.25 | -0.03 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | BTC-USD | 13.23 | -0.07 | exit signal |
| 2026-10-08T09:05 | Bollinger breakout | buy | XRP-USD | 14.29 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 10:30:05.000320+00:00 -> 2026-10-08 10:40:05.000320+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
