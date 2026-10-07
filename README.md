# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-07T02:55:05.000182+00:00 · 14141 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £97.40 (-2.60%)

Closed trades 39, win rate 59.0%, fees £1.51, max drawdown -3.05%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-06)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.15 · VIX 15.01 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.5, MSTR 7.5, AMD 7.3, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 2310 decisions in 462 calls, $0.0324 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-07T02:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-07T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-07T02:55 | 2 / 3 / 0 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 2.34 | +4.22% | 5 |
| Stochastic reversion · 1h | XRP-USD | 2.19 | +4.46% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| RSI(14) reversion | ETHU | 1.93 | +0.48% | 3 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.15 | 6.15 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.76 | -13.79 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.09 | 2.09 | 0 | — | 0.76 | 0.48 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.76 | 1.76 | 0 | — | 3.28 | 1.56 | -3.62 | 1 |
| 6 | Donchian 55/20 · 1h | breakout | 101.56 | 1.56 | 17 | 0.0 | 12.20 | 1.66 | -16.96 | 110 |
| 7 | Daily: Bullish score | daily | 101.47 | 1.47 | 3 | 0.0 | 5.96 | 0.98 | -12.76 | 10 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 9 | Hold SPY | benchmark | 101.20 | 1.20 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.53 | -7.55 | 43 |
| 11 | Copy: Warren Buffett (BRK-B) | copy | 100.15 | 0.15 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 12 | Stochastic reversion · 1h | reversion | 100.13 | 0.13 | 56 | 64.3 | -8.66 | -1.78 | -10.60 | 328 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.89 | -1.59 | 84 |
| 14 | Hold BTC | benchmark | 100.08 | 0.08 | 0 | — | 29.64 | 3.57 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 100.07 | 0.07 | 0 | — | -3.61 | -1.75 | -5.14 | 1 |
| 16 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 17 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.38 | -9.74 | 23 |
| 19 | EMA 20/50 cross · 1h | trend | 99.80 | -0.20 | 32 | 6.2 | 7.35 | 1.08 | -17.11 | 138 |
| 20 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.16 | 1.19 | -6.57 | 116 |
| 21 | Candlestick reversal · 1h | reversion | 99.42 | -0.58 | 70 | 37.1 | -21.97 | -5.00 | -23.37 | 488 |
| 22 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.45 | -2.90 | 21 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 99.36 | -0.64 | 0 | — | 18.30 | 2.76 | -6.29 | 1 |
| 24 | Connors RSI(2) · 1h | reversion | 98.84 | -1.16 | 75 | 44.0 | -11.46 | -4.12 | -14.77 | 218 |
| 25 | Trend pullback · 1h | trend | 98.61 | -1.39 | 67 | 23.9 | -21.47 | -6.33 | -24.41 | 168 |
| 26 | Daily: Momentum burst | daily | 98.45 | -1.55 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.36 | -3.95 | 25 |
| 28 | Copy: Insider buying | copy | 98.07 | -1.93 | 11 | 54.5 | -15.61 | -2.86 | -21.08 | 73 |
| 29 | Daily: SMA 20/50 cross · AAPL | daily | 97.60 | -2.40 | 0 | — | -0.63 | -0.15 | -5.18 | 1 |
| 30 | Agent | meta | 97.40 | -2.60 | 39 | 59.0 | -8.56 | -5.35 | -9.35 | 224 |
| 31 | Bollinger reversion · 1h | reversion | 97.39 | -2.61 | 50 | 46.0 | -15.18 | -3.75 | -17.03 | 300 |
| 32 | Z-score reversion · 1h | reversion | 97.30 | -2.70 | 25 | 48.0 | 2.64 | 0.67 | -8.60 | 152 |
| 33 | Agent (rotation) | meta | 97.15 | -2.85 | 65 | 27.7 | 1.14 | 0.39 | -9.99 | 270 |
| 34 | ADX DI cross · 1h | trend | 96.89 | -3.11 | 43 | 11.6 | -3.98 | -0.56 | -13.84 | 255 |
| 35 | Agent (ML meta-label) | meta | 96.73 | -3.27 | 265 | 14.7 | 0.09 | 0.16 | -13.58 | 398 |
| 36 | Supertrend · 1h | trend | 96.64 | -3.36 | 36 | 8.3 | 1.07 | 0.33 | -16.43 | 209 |
| 37 | Parabolic SAR · 1h | trend | 96.38 | -3.62 | 66 | 15.2 | -4.39 | -0.40 | -19.45 | 300 |
| 38 | Agent (aggressive) | meta | 96.24 | -3.76 | 18 | 50.0 | -2.48 | -1.16 | -5.66 | 104 |
| 39 | Williams %R · 1h | reversion | 96.07 | -3.93 | 86 | 52.3 | -19.48 | -3.62 | -19.58 | 490 |
| 40 | CCI reversion · 1h | reversion | 95.84 | -4.16 | 73 | 47.9 | -0.14 | 0.14 | -12.41 | 407 |
| 41 | MACD cross · 1h | trend | 95.64 | -4.36 | 91 | 19.8 | -13.40 | -2.15 | -17.27 | 466 |
| 42 | RSI momentum · 1h | momentum | 95.50 | -4.50 | 45 | 2.2 | -0.16 | 0.17 | -16.65 | 229 |
| 43 | MFI reversion · 1h | reversion | 95.12 | -4.88 | 75 | 28.0 | -9.65 | -1.65 | -16.99 | 117 |
| 44 | Squeeze breakout · 1h | breakout | 95.11 | -4.88 | 30 | 20.0 | 15.71 | 2.61 | -8.06 | 106 |
| 45 | Max aggression: 1-day momentum | meta | 95.06 | -4.94 | 7 | 42.9 | -23.54 | -1.21 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.70 | -5.30 | 35 | 14.3 | 2.14 | 0.47 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.62 | -5.38 | 57 | 10.5 | -10.09 | -1.00 | -24.82 | 254 |
| 48 | Bollinger breakout · 1h | breakout | 94.57 | -5.43 | 51 | 23.5 | 7.53 | 1.12 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 7.12 | 1.86 | -6.07 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.39 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.67 | -6.33 | 36 | 11.1 | 6.28 | 1.03 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.69 | -7.31 | 84 | 10.7 | -2.96 | -0.20 | -18.47 | 347 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.58 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.42 | -8.58 | 5 | 40.0 | -19.91 | -1.71 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.26 | -8.74 | 43 | 14.0 | 2.38 | 0.50 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.18 | -8.82 | 51 | 17.6 | -4.05 | -0.35 | -18.32 | 240 |
| 57 | Three white soldiers | momentum | 90.78 | -9.22 | 103 | 19.4 | -49.57 | -24.80 | -49.68 | 592 |
| 58 | VWAP momentum · 1h | momentum | 90.77 | -9.23 | 229 | 22.7 | -37.37 | -5.73 | -37.46 | 1269 |
| 59 | OBV trend · 1h | momentum | 90.46 | -9.54 | 111 | 11.7 | -12.73 | -1.41 | -26.73 | 334 |
| 60 | Heikin-Ashi · 1h | trend | 90.02 | -9.98 | 116 | 25.0 | -31.13 | -5.31 | -34.35 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.76 | -10.24 | 30 | 6.7 | -10.61 | -1.22 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.26 | -12.74 | 113 | 15.9 | -9.46 | -1.13 | -23.04 | 415 |
| 63 | RSI(14) reversion | reversion | 84.44 | -15.55 | 229 | 31.4 | -71.50 | -19.78 | -71.50 | 1419 |
| 64 | Squeeze breakout | breakout | 77.12 | -22.88 | 253 | 15.4 | -62.41 | -18.76 | -62.41 | 1222 |
| 65 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.95 | -17.60 | -73.95 | 1655 |
| 66 | VWAP reversion | reversion | 76.55 | -23.45 | 282 | 28.0 | -68.85 | -15.95 | -69.01 | 1372 |
| 67 | Donchian 55/20 | breakout | 75.88 | -24.12 | 260 | 17.3 | -68.79 | -15.09 | -68.79 | 1302 |
| 68 | EMA 20/50 cross | trend | 73.94 | -26.06 | 269 | 18.2 | -78.46 | -16.05 | -78.46 | 1475 |
| 69 | Volume breakout | breakout | 73.30 | -26.70 | 212 | 12.3 | -65.57 | -19.28 | -65.57 | 924 |
| 70 | Z-score reversion | reversion | 69.27 | -30.73 | 366 | 26.8 | -85.24 | -25.39 | -85.24 | 2048 |
| 71 | Supertrend | trend | 68.86 | -31.14 | 364 | 19.8 | -87.16 | -22.10 | -87.16 | 1922 |
| 72 | MFI reversion | reversion | 68.85 | -31.14 | 362 | 20.7 | -87.14 | -30.33 | -87.15 | 2104 |
| 73 | Keltner breakout | breakout | 67.65 | -32.35 | 352 | 13.1 | -85.61 | -29.95 | -85.61 | 1888 |
| 74 | AI bee: Bizzy | ai | 66.76 | -33.24 | 620 | 8.7 | — | — | — | — |
| 75 | Ichimoku | trend | 66.42 | -33.58 | 323 | 9.0 | -82.30 | -24.53 | -82.30 | 1769 |
| 76 | AI bee: Boozy | ai | 65.97 | -34.03 | 219 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.12 | -35.88 | 405 | 9.1 | -89.62 | -36.06 | -89.62 | 2096 |
| 78 | MACD zero-line | trend | 62.40 | -37.60 | 461 | 15.2 | -91.53 | -30.41 | -91.53 | 2359 |
| 79 | Donchian 20/10 | breakout | 62.00 | -38.00 | 497 | 17.9 | -91.17 | -27.12 | -91.17 | 2667 |
| 80 | RSI momentum | momentum | 61.13 | -38.87 | 462 | 16.7 | -90.71 | -26.43 | -90.71 | 2381 |
| 81 | Trend pullback | trend | 59.91 | -40.09 | 493 | 15.4 | -91.44 | -29.77 | -91.44 | 2347 |
| 82 | Triple EMA stack | trend | 59.51 | -40.49 | 515 | 15.1 | -93.45 | -31.89 | -93.45 | 2636 |
| 83 | Bollinger breakout | breakout | 58.66 | -41.34 | 507 | 13.8 | -94.06 | -34.81 | -94.06 | 2824 |
| 84 | Consensus | meta | 56.84 | -43.16 | 493 | 9.9 | -94.47 | -26.23 | -94.47 | 2694 |
| 85 | Stochastic reversion | reversion | 56.54 | -43.46 | 733 | 22.9 | -95.56 | -36.95 | -95.57 | 4041 |
| 86 | Bollinger reversion | reversion | 55.78 | -44.22 | 678 | 17.6 | -95.69 | -36.17 | -95.70 | 3678 |
| 87 | EMA 9/21 cross | trend | 54.45 | -45.55 | 639 | 16.1 | -97.44 | -34.69 | -97.44 | 3548 |
| 88 | Connors RSI(2) | reversion | 53.60 | -46.40 | 681 | 20.1 | -96.57 | -34.14 | -96.57 | 3637 |
| 89 | OBV trend | momentum | 51.55 | -48.45 | 745 | 14.6 | -96.48 | -38.65 | -96.48 | 3627 |
| 90 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -31.48 | -98.72 | 5367 |
| 91 | CCI reversion | reversion | 50.31 | -49.69 | 712 | 17.0 | -98.46 | -39.62 | -98.46 | 4690 |
| 92 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.29 | -39.45 | -99.29 | 5612 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -45.19 | -99.73 | 6134 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.43 | -41.15 | -97.43 | 3686 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -42.99 | -99.51 | 6096 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -49.92 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-07T02:51 | Z-score reversion | sell | SOL-USD | 3.48 | -0.01 | rebalance down |
| 2026-10-07T02:50 | Z-score reversion | buy | XRP-USD | 10.44 | — | entry signal |
| 2026-10-07T02:50 | Z-score reversion | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-07T02:50 | Z-score reversion | buy | DOGE-USD | 13.90 | — | entry signal |
| 2026-10-07T02:50 | Z-score reversion | buy | BTC-USD | 13.90 | — | entry signal |
| 2026-10-07T02:50 | RSI(14) reversion | buy | XRP-USD | 21.13 | — | entry signal |
| 2026-10-07T02:41 | MFI reversion | buy | ETH-USD | 3.44 | — | rebalance up |
| 2026-10-07T02:41 | MFI reversion | sell | XRP-USD | 3.44 | -0.01 | rebalance down |
| 2026-10-07T02:40 | MFI reversion | buy | ETH-USD | 6.93 | — | entry signal |
| 2026-10-07T02:40 | MFI reversion | buy | BTC-USD | 13.79 | — | entry signal |
| 2026-10-07T02:40 | MFI reversion | sell | SOL-USD | 3.47 | -0.00 | rebalance down |
| 2026-10-07T02:40 | Z-score reversion | buy | SOL-USD | 17.37 | — | entry signal |
| 2026-10-07T02:35 | CCI reversion | buy | XRP-USD | 10.10 | — | entry signal |
| 2026-10-07T02:35 | CCI reversion | buy | SOL-USD | 10.10 | — | entry signal |
| 2026-10-07T02:35 | CCI reversion | buy | ETH-USD | 10.10 | — | entry signal |
| 2026-10-07T02:35 | CCI reversion | buy | DOGE-USD | 10.10 | — | entry signal |
| 2026-10-07T02:35 | CCI reversion | buy | BTC-USD | 10.10 | — | entry signal |
| 2026-10-07T02:35 | RSI(14) reversion | buy | SOL-USD | 21.13 | — | entry signal |
| 2026-10-07T02:30 | AI bee: Bizzy | sell | SOL-USD | 10.14 | -0.08 | Jev: sell (sell p=0.65) after 10 min |
| 2026-10-07T02:20 | AI bee: Bizzy | buy | SOL-USD | 10.22 | — | Jev: buy (buy p=0.61) |
| 2026-10-07T02:20 | Bollinger reversion | buy | XRP-USD | 11.20 | — | entry signal |
| 2026-10-07T02:20 | Bollinger reversion | buy | SOL-USD | 11.20 | — | entry signal |
| 2026-10-07T02:20 | Bollinger reversion | buy | ETH-USD | 11.20 | — | entry signal |
| 2026-10-07T02:20 | Bollinger reversion | buy | DOGE-USD | 11.20 | — | entry signal |
| 2026-10-07T02:20 | Bollinger reversion | buy | BTC-USD | 11.20 | — | entry signal |
| 2026-10-07T02:15 | MFI reversion | buy | XRP-USD | 17.25 | — | entry signal |
| 2026-10-07T02:15 | MFI reversion | buy | SOL-USD | 17.25 | — | entry signal |
| 2026-10-07T02:15 | MFI reversion | buy | DOGE-USD | 17.25 | — | entry signal |
| 2026-10-07T02:10 | VWAP reversion | buy | XRP-USD | 19.18 | — | entry signal |
| 2026-10-07T02:10 | VWAP reversion | buy | SOL-USD | 19.18 | — | entry signal |
| 2026-10-07T02:10 | VWAP reversion | buy | DOGE-USD | 19.18 | — | entry signal |
| 2026-10-07T02:10 | VWAP reversion | buy | BTC-USD | 19.18 | — | entry signal |
| 2026-10-07T02:05 | Stochastic reversion | buy | SOL-USD | 14.14 | — | entry signal |
| 2026-10-07T02:05 | Stochastic reversion | buy | ETH-USD | 14.14 | — | entry signal |
| 2026-10-07T02:05 | Stochastic reversion | buy | BTC-USD | 14.14 | — | entry signal |
| 2026-10-07T02:00 | Agent (aggressive) | sell | XRP-USD | 48.24 | -0.96 | selected signal exited |
| 2026-10-07T02:00 | Agent (aggressive) | sell | DOGE-USD | 47.97 | -1.26 | selected signal exited |
| 2026-10-07T02:00 | Agent | sell | XRP-USD | 19.27 | -0.38 | selected signal exited |
| 2026-10-07T02:00 | Agent | sell | DOGE-USD | 19.16 | -0.50 | selected signal exited |
| 2026-10-07T02:00 | CCI reversion · 1h | sell | DOGE-USD | 18.76 | -0.35 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-09 02:55:05.000182+00:00 -> 2026-10-07 03:05:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
