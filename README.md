# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T01:00:05.000124+00:00 · 15007 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.64 (-3.36%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.07 |
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

Today: 825 decisions in 165 calls, $0.0116 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T01:00 | 1 / 4 / 0 | PLTR 14% |  |
| Breezy | 2026-10-08T01:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T01:00 | 2 / 3 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.70 | 5.70 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.90 | -13.84 | 118 |
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
| 16 | Hold BTC | benchmark | 99.80 | -0.20 | 0 | — | 29.09 | 3.48 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.79 | -1.21 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.47 | -1.52 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.47 | -1.53 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.41 | -1.59 | 34 | 5.9 | 7.46 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.53 | -2.47 | 62 | 58.1 | -10.52 | -2.08 | -11.21 | 341 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.34 | -2.66 | 0 | — | 12.72 | 2.06 | -7.19 | 1 |
| 25 | RSI(14) reversion · 1h | reversion | 97.30 | -2.70 | 16 | 43.8 | 3.55 | 1.01 | -6.57 | 114 |
| 26 | Connors RSI(2) · 1h | reversion | 97.04 | -2.96 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 27 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 28 | Z-score reversion · 1h | reversion | 96.67 | -3.33 | 28 | 46.4 | 0.64 | 0.25 | -8.60 | 159 |
| 29 | Agent | meta | 96.64 | -3.36 | 42 | 57.1 | -10.36 | -5.52 | -10.70 | 254 |
| 30 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 31 | Candlestick reversal · 1h | reversion | 96.47 | -3.53 | 81 | 34.6 | -26.10 | -5.86 | -26.75 | 479 |
| 32 | Copy: Insider buying | copy | 96.46 | -3.54 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 33 | Supertrend · 1h | trend | 95.76 | -4.24 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.48 | -4.52 | 80 | 21.2 | -6.67 | -0.77 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.17 | -4.83 | 47 | 14.9 | -6.46 | -0.90 | -13.84 | 251 |
| 36 | Bollinger reversion · 1h | reversion | 95.13 | -4.87 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -4.33 | -1.59 | -6.03 | 114 |
| 38 | Agent (ML meta-label) | meta | 94.96 | -5.04 | 286 | 15.7 | 1.65 | 0.44 | -13.13 | 364 |
| 39 | MACD cross · 1h | trend | 94.95 | -5.05 | 100 | 23.0 | -11.89 | -1.67 | -17.27 | 467 |
| 40 | Max aggression: 1-day momentum | meta | 94.89 | -5.11 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.16 | -5.84 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.88 | -6.12 | 104 | 21.2 | -17.38 | -5.28 | -17.84 | 562 |
| 45 | MFI reversion · 1h | reversion | 93.62 | -6.38 | 84 | 28.6 | -11.10 | -1.89 | -16.99 | 122 |
| 46 | Ichimoku · 1h | trend | 93.54 | -6.46 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 47 | Bollinger breakout · 1h | breakout | 93.52 | -6.48 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 48 | Triple EMA stack · 1h | trend | 93.19 | -6.80 | 61 | 11.5 | -8.93 | -0.90 | -24.26 | 243 |
| 49 | Williams %R · 1h | reversion | 93.13 | -6.87 | 93 | 49.5 | -22.45 | -4.05 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 51 | Opening range 15m | breakout | 92.20 | -7.80 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | CCI reversion · 1h | reversion | 91.21 | -8.79 | 80 | 45.0 | -5.25 | -0.64 | -12.41 | 406 |
| 53 | Donchian 20/10 · 1h | breakout | 91.15 | -8.85 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 54 | EMA 9/21 cross · 1h | trend | 91.15 | -8.85 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 55 | VWAP momentum · 1h | momentum | 90.64 | -9.36 | 236 | 23.3 | -36.55 | -5.57 | -37.98 | 1270 |
| 56 | MACD zero-line · 1h | trend | 90.54 | -9.46 | 57 | 19.3 | -5.21 | -0.50 | -19.00 | 238 |
| 57 | Three white soldiers | momentum | 90.35 | -9.65 | 106 | 18.9 | -48.56 | -24.08 | -48.56 | 583 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.33 | -1.60 | -28.48 | 329 |
| 59 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -9.08 | -1.01 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.93 | -11.07 | 124 | 25.0 | -31.96 | -5.45 | -35.54 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.00 | -13.00 | 123 | 19.5 | -9.12 | -1.08 | -23.22 | 406 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.73 | -19.27 | 270 | 31.1 | -72.00 | -18.76 | -72.03 | 1427 |
| 64 | ROC + volume | momentum | 76.17 | -23.83 | 327 | 20.2 | -73.42 | -17.10 | -73.62 | 1651 |
| 65 | Squeeze breakout | breakout | 76.10 | -23.90 | 262 | 14.9 | -62.09 | -18.32 | -62.09 | 1215 |
| 66 | Donchian 55/20 | breakout | 74.41 | -25.59 | 266 | 16.9 | -68.49 | -14.77 | -68.68 | 1290 |
| 67 | VWAP reversion | reversion | 73.18 | -26.82 | 321 | 27.4 | -70.19 | -15.91 | -70.24 | 1393 |
| 68 | EMA 20/50 cross | trend | 72.96 | -27.04 | 274 | 17.9 | -77.78 | -15.64 | -77.90 | 1467 |
| 69 | Volume breakout | breakout | 72.92 | -27.08 | 215 | 12.1 | -64.68 | -18.83 | -64.68 | 913 |
| 70 | Supertrend | trend | 68.77 | -31.23 | 371 | 19.4 | -86.60 | -21.18 | -86.78 | 1926 |
| 71 | MFI reversion | reversion | 66.62 | -33.38 | 403 | 21.8 | -87.51 | -29.20 | -87.51 | 2110 |
| 72 | Keltner breakout | breakout | 66.45 | -33.55 | 361 | 12.7 | -85.20 | -29.02 | -85.21 | 1875 |
| 73 | Z-score reversion | reversion | 66.43 | -33.57 | 408 | 24.8 | -85.22 | -23.78 | -85.22 | 2063 |
| 74 | Ichimoku | trend | 66.19 | -33.81 | 326 | 8.9 | -81.64 | -23.40 | -81.69 | 1734 |
| 75 | AI bee: Bizzy | ai | 65.32 | -34.68 | 649 | 8.5 | — | — | — | — |
| 76 | AI bee: Boozy | ai | 63.18 | -36.82 | 223 | 3.6 | — | — | — | — |
| 77 | ADX DI cross | trend | 63.01 | -36.99 | 422 | 8.8 | -89.57 | -34.70 | -89.59 | 2106 |
| 78 | MACD zero-line | trend | 61.80 | -38.20 | 476 | 14.9 | -91.42 | -29.55 | -91.42 | 2360 |
| 79 | Donchian 20/10 | breakout | 61.67 | -38.33 | 506 | 17.6 | -90.94 | -26.18 | -90.98 | 2662 |
| 80 | RSI momentum | momentum | 60.35 | -39.65 | 472 | 16.3 | -90.33 | -25.41 | -90.39 | 2369 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.13 | -28.58 | -91.13 | 2331 |
| 82 | Triple EMA stack | trend | 58.92 | -41.09 | 518 | 15.1 | -93.16 | -30.49 | -93.19 | 2613 |
| 83 | Bollinger breakout | breakout | 57.69 | -42.30 | 525 | 13.5 | -93.80 | -33.72 | -93.81 | 2828 |
| 84 | Consensus | meta | 56.20 | -43.80 | 505 | 9.9 | -94.43 | -25.83 | -94.43 | 2688 |
| 85 | EMA 9/21 cross | trend | 54.07 | -45.93 | 649 | 15.9 | -97.35 | -33.14 | -97.35 | 3533 |
| 86 | Stochastic reversion | reversion | 53.82 | -46.18 | 760 | 22.2 | -95.62 | -34.47 | -95.62 | 4037 |
| 87 | Bollinger reversion | reversion | 53.42 | -46.58 | 706 | 16.9 | -95.76 | -33.67 | -95.76 | 3692 |
| 88 | Connors RSI(2) | reversion | 53.37 | -46.62 | 692 | 20.1 | -96.40 | -32.57 | -96.40 | 3600 |
| 89 | OBV trend | momentum | 50.66 | -49.34 | 753 | 14.5 | -96.37 | -36.79 | -96.37 | 3594 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.40 | -98.65 | 5340 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -36.74 | -99.30 | 5581 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.98 | -99.73 | 6132 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -39.51 | -97.36 | 3662 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.33 | -98.47 | 4681 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.38 | -99.51 | 6091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.19 | -99.90 | 8255 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T01:00 | Agent (rotation) | sell | XRP-USD | 6.42 | -0.01 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | SOL-USD | 6.42 | -0.02 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | ETH-USD | 8.02 | -0.03 | selected signal exited |
| 2026-10-08T01:00 | Agent (rotation) | sell | DOGE-USD | 8.04 | -0.01 | selected signal exited |
| 2026-10-08T01:00 | Consensus | sell | DOGE-USD | 13.99 | -0.09 | target is flat |
| 2026-10-08T01:00 | Agent (aggressive) | sell | DOGE-USD | 47.54 | 0.01 | selected signal exited |
| 2026-10-08T01:00 | Agent | sell | DOGE-USD | 19.41 | 0.01 | selected signal exited |
| 2026-10-08T01:00 | Williams %R · 1h | buy | XRP-USD | 11.84 | — | rebalance up |
| 2026-10-08T01:00 | Williams %R · 1h | sell | ETH-USD | 11.59 | -0.03 | exit signal |
| 2026-10-08T01:00 | Williams %R · 1h | sell | DOGE-USD | 13.41 | 0.00 | exit signal |
| 2026-10-08T01:00 | Stochastic reversion · 1h | sell | DOGE-USD | 6.51 | -0.01 | exit signal |
| 2026-10-08T01:00 | VWAP reversion · 1h | sell | XRP-USD | 20.48 | -0.03 | exit signal |
| 2026-10-08T01:00 | VWAP reversion · 1h | sell | SOL-USD | 20.46 | -0.05 | exit signal |
| 2026-10-08T01:00 | VWAP reversion · 1h | sell | ETH-USD | 20.47 | -0.08 | exit signal |
| 2026-10-08T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 20.53 | -0.02 | exit signal |
| 2026-10-08T01:00 | VWAP momentum · 1h | buy | XRP-USD | 4.77 | — | entry signal |
| 2026-10-08T01:00 | VWAP momentum · 1h | buy | SOL-USD | 4.77 | — | entry signal |
| 2026-10-08T01:00 | VWAP momentum · 1h | buy | ETH-USD | 4.77 | — | entry signal |
| 2026-10-08T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 4.77 | — | entry signal |
| 2026-10-08T01:00 | Heikin-Ashi · 1h | buy | SOL-USD | 11.12 | — | entry signal |
| 2026-10-08T01:00 | Volume breakout | sell | DOGE-USD | 18.14 | -0.12 | target is flat |
| 2026-10-08T00:59 | AI bee: Bizzy | sell | SOL-USD | 9.86 | -0.05 | Jev: sell (sell p=0.51) after 10 min |
| 2026-10-08T00:55 | MFI reversion | buy | SOL-USD | 16.67 | — | entry signal |
| 2026-10-08T00:55 | Three white soldiers | buy | BTC-USD | 22.61 | — | entry signal |
| 2026-10-08T00:55 | Volume breakout | buy | DOGE-USD | 18.26 | — | entry signal |
| 2026-10-08T00:50 | Consensus | buy | DOGE-USD | 14.07 | — | entry |
| 2026-10-08T00:50 | MACD zero-line | buy | BTC-USD | 15.46 | — | entry signal |
| 2026-10-08T00:49 | AI bee: Bizzy | buy | SOL-USD | 9.91 | — | Jev: buy (buy p=0.61) |
| 2026-10-08T00:45 | Consensus | sell | DOGE-USD | 14.04 | -0.08 | target is flat |
| 2026-10-08T00:40 | Keltner breakout | sell | SOL-USD | 16.51 | -0.14 | stop-loss |
| 2026-10-08T00:40 | Bollinger breakout | sell | XRP-USD | 2.36 | -0.01 | stop-loss |
| 2026-10-08T00:40 | Donchian 55/20 | sell | SOL-USD | 18.48 | -0.16 | stop-loss |
| 2026-10-08T00:40 | MACD zero-line | sell | XRP-USD | 15.43 | -0.09 | exit signal |
| 2026-10-08T00:35 | OBV trend | buy | DOGE-USD | 12.33 | — | entry |
| 2026-10-08T00:35 | OBV trend | sell | ETH-USD | 12.33 | -0.06 | exit signal |
| 2026-10-08T00:34 | AI bee: Boozy | sell | DOGE-USD | 19.78 | -0.13 | Jev: sell (sell p=0.55) after 15 min |
| 2026-10-08T00:30 | Consensus | sell | SOL-USD | 13.67 | -0.11 | target is flat |
| 2026-10-08T00:30 | MACD zero-line | sell | BTC-USD | 7.19 | -0.06 | exit signal |
| 2026-10-08T00:28 | AI bee: Bizzy | sell | XRP-USD | 9.05 | -0.07 | Jev: sell (sell p=0.76) after 10 min |
| 2026-10-08T00:28 | AI bee: Bizzy | sell | DOGE-USD | 13.53 | -0.06 | Jev: sell (sell p=0.57) after 11 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 01:00:05.000124+00:00 -> 2026-10-08 01:10:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
