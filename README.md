# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T15:00:05.000159+00:00 · 15692 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.12 (-3.88%)

Closed trades 45, win rate 55.6%, fees £1.91, max drawdown -4.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 16147 decisions in 2186 calls, $0.2120 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T15:00 | 0 / 20 / 10 | cash |  |
| Breezy | 2026-10-08T15:00 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-08T15:00 | 2 / 24 / 4 | MSTR 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.96 | +0.80% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 104.41 | 4.41 | 0 | — | -2.31 | -0.34 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.49 | 2.49 | 34 | 41.2 | -8.54 | -2.65 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.77 | 1.77 | 0 | — | -0.31 | -0.14 | -5.09 | 1 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.46 | 1.46 | 0 | — | 2.28 | 1.11 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.03 | 1.03 | 0 | — | 0.23 | 0.18 | -3.66 | 1 |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 100.48 | 0.48 | 0 | — | -2.60 | -1.03 | -7.65 | 1 |
| 9 | Donchian 55/20 · 1h | breakout | 100.40 | 0.40 | 18 | 5.6 | 11.65 | 1.57 | -16.96 | 109 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.84 | -0.16 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 13 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 14 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.43 | -0.57 | 30 | 36.7 | 4.95 | 2.34 | -1.52 | 86 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Daily: SMA 20/50 cross · AAPL | daily | 99.12 | -0.88 | 0 | — | -0.49 | -0.10 | -5.18 | 1 |
| 18 | Hold BTC | benchmark | 98.97 | -1.03 | 0 | — | 26.91 | 3.25 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 98.60 | -1.40 | 70 | 25.7 | -21.97 | -6.36 | -24.37 | 171 |
| 20 | Daily: Bullish score | daily | 98.06 | -1.95 | 3 | 0.0 | 1.06 | 0.33 | -12.76 | 10 |
| 21 | Three white soldiers · 1h | momentum | 98.04 | -1.96 | 4 | 0.0 | -2.50 | -1.96 | -3.95 | 25 |
| 22 | Copy: Insider buying | copy | 97.68 | -2.32 | 11 | 54.5 | -16.28 | -2.94 | -21.08 | 75 |
| 23 | EMA 20/50 cross · 1h | trend | 97.61 | -2.39 | 35 | 8.6 | 1.76 | 0.42 | -18.48 | 136 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.24 | -2.76 | 0 | — | 11.83 | 1.94 | -7.38 | 1 |
| 25 | Stochastic reversion · 1h | reversion | 96.88 | -3.12 | 70 | 52.9 | -12.81 | -2.55 | -13.20 | 341 |
| 26 | Connors RSI(2) · 1h | reversion | 96.39 | -3.61 | 92 | 44.6 | -15.96 | -5.83 | -18.25 | 234 |
| 27 | Agent (rotation) | meta | 96.27 | -3.73 | 75 | 26.7 | 1.63 | 0.51 | -8.02 | 273 |
| 28 | ADX DI cross · 1h | trend | 96.22 | -3.78 | 52 | 23.1 | -6.75 | -0.95 | -13.84 | 254 |
| 29 | Agent | meta | 96.12 | -3.88 | 45 | 55.6 | -9.89 | -5.45 | -10.30 | 238 |
| 30 | Daily: Momentum burst | daily | 95.90 | -4.10 | 4 | 0.0 | -4.12 | -0.47 | -17.52 | 40 |
| 31 | Parabolic SAR · 1h | trend | 95.73 | -4.27 | 80 | 21.2 | -4.98 | -0.51 | -20.87 | 291 |
| 32 | Supertrend · 1h | trend | 95.69 | -4.31 | 42 | 9.5 | -2.38 | -0.14 | -17.03 | 206 |
| 33 | MACD cross · 1h | trend | 95.29 | -4.71 | 103 | 22.3 | -11.06 | -1.56 | -17.27 | 467 |
| 34 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -3.27 | -1.45 | -6.03 | 114 |
| 35 | Z-score reversion · 1h | reversion | 94.98 | -5.02 | 34 | 38.2 | -2.96 | -0.46 | -8.60 | 159 |
| 36 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 13.87 | 2.33 | -8.14 | 106 |
| 37 | Candlestick reversal · 1h | reversion | 94.69 | -5.31 | 89 | 31.5 | -25.61 | -5.52 | -25.86 | 509 |
| 38 | Agent (ML meta-label) | meta | 94.40 | -5.60 | 298 | 15.8 | 1.16 | 0.35 | -10.94 | 366 |
| 39 | RSI(14) reversion · 1h | reversion | 94.29 | -5.71 | 22 | 31.8 | 1.25 | 0.39 | -6.79 | 145 |
| 40 | RSI momentum · 1h | momentum | 93.88 | -6.12 | 52 | 5.8 | 5.25 | 0.82 | -16.47 | 220 |
| 41 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 42 | Bollinger breakout · 1h | breakout | 93.38 | -6.62 | 63 | 30.2 | 7.41 | 1.10 | -12.06 | 291 |
| 43 | Ichimoku · 1h | trend | 93.15 | -6.85 | 39 | 17.9 | -3.37 | -0.27 | -19.68 | 120 |
| 44 | Bollinger reversion · 1h | reversion | 92.83 | -7.17 | 61 | 37.7 | -21.05 | -5.30 | -21.27 | 309 |
| 45 | Triple EMA stack · 1h | trend | 92.72 | -7.28 | 61 | 11.5 | -12.20 | -1.37 | -26.86 | 236 |
| 46 | Volume breakout · 1h | breakout | 92.55 | -7.45 | 45 | 17.8 | 6.25 | 1.02 | -12.60 | 122 |
| 47 | Opening range 30m | breakout | 92.31 | -7.70 | 116 | 19.8 | -16.14 | -4.89 | -16.77 | 563 |
| 48 | Williams %R · 1h | reversion | 92.24 | -7.76 | 100 | 48.0 | -24.55 | -4.47 | -25.23 | 501 |
| 49 | Max aggression: 1-day momentum | meta | 91.61 | -8.39 | 9 | 33.3 | -23.81 | -1.21 | -37.31 | 43 |
| 50 | MFI reversion · 1h | reversion | 91.58 | -8.41 | 89 | 27.0 | -15.14 | -2.63 | -16.99 | 122 |
| 51 | MACD zero-line · 1h | trend | 90.50 | -9.50 | 57 | 19.3 | -5.95 | -0.63 | -19.00 | 239 |
| 52 | Donchian 20/10 · 1h | breakout | 90.46 | -9.54 | 50 | 20.0 | 1.62 | 0.40 | -16.18 | 221 |
| 53 | EMA 9/21 cross · 1h | trend | 90.43 | -9.57 | 91 | 12.1 | -5.52 | -0.54 | -18.95 | 340 |
| 54 | Opening range 15m | breakout | 90.28 | -9.71 | 133 | 18.8 | -17.87 | -5.19 | -18.28 | 681 |
| 55 | Three white soldiers | momentum | 89.47 | -10.53 | 113 | 18.6 | -48.61 | -24.26 | -48.64 | 586 |
| 56 | CCI reversion · 1h | reversion | 89.02 | -10.98 | 86 | 41.9 | -8.55 | -1.14 | -12.68 | 409 |
| 57 | OBV trend · 1h | momentum | 88.80 | -11.20 | 130 | 18.5 | -15.25 | -1.79 | -28.12 | 322 |
| 58 | Keltner breakout · 1h | breakout | 88.73 | -11.27 | 39 | 17.9 | -10.24 | -1.17 | -23.68 | 218 |
| 59 | VWAP momentum · 1h | momentum | 88.65 | -11.35 | 255 | 21.6 | -37.30 | -5.71 | -38.94 | 1271 |
| 60 | Heikin-Ashi · 1h | trend | 88.38 | -11.62 | 130 | 26.2 | -32.37 | -5.54 | -35.72 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.15 | -12.85 | 125 | 20.0 | -8.16 | -0.94 | -23.15 | 407 |
| 62 | Max aggression: 5-day momentum | meta | 83.90 | -16.10 | 7 | 28.6 | -26.95 | -2.40 | -33.52 | 30 |
| 63 | RSI(14) reversion | reversion | 79.17 | -20.82 | 295 | 31.2 | -72.81 | -19.28 | -72.97 | 1482 |
| 64 | ROC + volume | momentum | 75.51 | -24.49 | 336 | 20.2 | -73.12 | -16.94 | -73.70 | 1652 |
| 65 | Squeeze breakout | breakout | 74.68 | -25.32 | 270 | 14.4 | -62.47 | -18.64 | -62.49 | 1213 |
| 66 | Volume breakout | breakout | 72.72 | -27.27 | 217 | 12.0 | -64.11 | -18.77 | -64.12 | 916 |
| 67 | Donchian 55/20 | breakout | 72.63 | -27.37 | 274 | 16.8 | -68.93 | -14.99 | -68.94 | 1288 |
| 68 | EMA 20/50 cross | trend | 72.19 | -27.81 | 282 | 18.1 | -78.05 | -15.82 | -78.06 | 1465 |
| 69 | VWAP reversion | reversion | 71.23 | -28.77 | 337 | 27.3 | -71.09 | -16.37 | -71.09 | 1411 |
| 70 | Supertrend | trend | 67.68 | -32.32 | 387 | 19.4 | -86.97 | -21.67 | -86.99 | 1940 |
| 71 | Keltner breakout | breakout | 65.80 | -34.20 | 371 | 12.9 | -84.99 | -28.74 | -85.00 | 1867 |
| 72 | AI bee: Bizzy | ai | 64.57 | -35.43 | 669 | 8.5 | — | — | — | — |
| 73 | Ichimoku | trend | 64.49 | -35.51 | 340 | 8.8 | -81.77 | -23.59 | -81.77 | 1737 |
| 74 | MFI reversion | reversion | 64.02 | -35.98 | 426 | 21.4 | -87.87 | -29.58 | -87.88 | 2114 |
| 75 | Z-score reversion | reversion | 63.63 | -36.37 | 435 | 24.4 | -85.67 | -24.13 | -85.73 | 2089 |
| 76 | AI bee: Boozy | ai | 61.82 | -38.18 | 235 | 5.1 | — | — | — | — |
| 77 | ADX DI cross | trend | 61.48 | -38.52 | 448 | 8.7 | -89.72 | -35.60 | -89.74 | 2124 |
| 78 | MACD zero-line | trend | 60.69 | -39.31 | 495 | 14.9 | -91.53 | -29.95 | -91.54 | 2369 |
| 79 | Donchian 20/10 | breakout | 60.60 | -39.40 | 525 | 17.9 | -91.04 | -26.54 | -91.06 | 2658 |
| 80 | Trend pullback | trend | 59.72 | -40.28 | 498 | 15.5 | -90.82 | -27.98 | -90.82 | 2312 |
| 81 | RSI momentum | momentum | 59.36 | -40.64 | 487 | 16.6 | -90.55 | -25.86 | -90.56 | 2369 |
| 82 | Triple EMA stack | trend | 58.76 | -41.24 | 525 | 15.4 | -93.29 | -31.18 | -93.29 | 2609 |
| 83 | Consensus | meta | 56.53 | -43.47 | 511 | 10.4 | -94.28 | -25.66 | -94.28 | 2683 |
| 84 | Bollinger breakout | breakout | 56.34 | -43.66 | 549 | 13.7 | -93.79 | -33.95 | -93.79 | 2821 |
| 85 | EMA 9/21 cross | trend | 53.07 | -46.93 | 670 | 16.0 | -97.40 | -33.81 | -97.40 | 3543 |
| 86 | Connors RSI(2) | reversion | 52.72 | -47.28 | 703 | 20.2 | -96.29 | -32.30 | -96.30 | 3579 |
| 87 | Stochastic reversion | reversion | 52.09 | -47.91 | 794 | 22.2 | -95.69 | -35.21 | -95.71 | 4055 |
| 88 | Bollinger reversion | reversion | 50.86 | -49.14 | 751 | 17.4 | -95.85 | -34.35 | -95.87 | 3723 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -30.99 | -98.69 | 5372 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -37.11 | -96.39 | 3577 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.83 | -99.34 | 5658 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.53 | -99.73 | 6146 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.38 | -39.72 | -97.39 | 3657 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.86 | -98.49 | 4705 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.16 | -99.52 | 6120 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.29 | -99.90 | 8248 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T15:00 | Agent (ML meta-label) | sell | META | 2.32 | -0.01 | selected signal exited |
| 2026-10-08T15:00 | MFI reversion · 1h | buy | SOL-USD | 22.91 | — | entry signal |
| 2026-10-08T15:00 | CCI reversion · 1h | buy | XRP-USD | 13.44 | — | entry signal |
| 2026-10-08T15:00 | CCI reversion · 1h | buy | BTC-USD | 17.83 | — | entry signal |
| 2026-10-08T15:00 | CCI reversion · 1h | sell | SQQQ | 5.27 | 0.06 | rebalance down |
| 2026-10-08T15:00 | CCI reversion · 1h | sell | DOGE-USD | 4.51 | -0.02 | rebalance down |
| 2026-10-08T15:00 | Z-score reversion · 1h | buy | SOL-USD | 23.76 | — | entry signal |
| 2026-10-08T15:00 | Bollinger reversion · 1h | buy | ETH-USD | 10.97 | — | entry signal |
| 2026-10-08T15:00 | RSI(14) reversion · 1h | buy | ETH-USD | 23.42 | — | entry signal |
| 2026-10-08T15:00 | RSI(14) reversion · 1h | buy | BTC-USD | 23.61 | — | entry signal |
| 2026-10-08T15:00 | Stochastic reversion | buy | LABU | 2.95 | — | rebalance up |
| 2026-10-08T15:00 | Stochastic reversion | sell | IWM | 5.79 | -0.02 | stop-loss |
| 2026-10-08T15:00 | Z-score reversion | sell | IWM | 4.54 | -0.02 | stop-loss |
| 2026-10-08T15:00 | Bollinger reversion | sell | ETHU | 12.70 | -0.01 | exit signal |
| 2026-10-08T15:00 | Donchian 20/10 | buy | COIN | 3.08 | — | entry signal |
| 2026-10-08T15:00 | Donchian 20/10 | sell | AAPL | 3.05 | -0.00 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | buy | PLTR | 6.57 | — | entry |
| 2026-10-08T15:00 | RSI momentum | buy | MSTR | 6.60 | — | entry signal |
| 2026-10-08T15:00 | RSI momentum | buy | COIN | 6.60 | — | entry signal |
| 2026-10-08T15:00 | RSI momentum | sell | XRP-USD | 3.25 | -0.02 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | sell | MSFT | 3.33 | -0.02 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | sell | GOOGL | 3.30 | -0.01 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | sell | DOGE-USD | 3.28 | -0.03 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | sell | BTC-USD | 3.28 | -0.02 | rebalance down |
| 2026-10-08T15:00 | RSI momentum | sell | AAPL | 3.32 | -0.00 | rebalance down |
| 2026-10-08T15:00 | MACD zero-line | buy | MSTR | 12.15 | — | entry signal |
| 2026-10-08T15:00 | MACD zero-line | sell | DOGE-USD | 15.09 | -0.14 | exit signal |
| 2026-10-08T15:00 | Triple EMA stack | sell | MSFT | 14.68 | -0.04 | exit signal |
| 2026-10-08T15:00 | EMA 9/21 cross | sell | MSFT | 5.89 | -0.01 | exit signal |
| 2026-10-08T14:57 | MACD zero-line | buy | NVDA | 3.03 | — | rebalance up |
| 2026-10-08T14:57 | MACD zero-line | sell | BTC-USD | 3.03 | -0.02 | rebalance down |
| 2026-10-08T14:55 | Consensus | sell | AMZN | 14.09 | -0.07 | target is flat |
| 2026-10-08T14:55 | MFI reversion | sell | TNA | 15.95 | -0.16 | stop-loss |
| 2026-10-08T14:55 | Stochastic reversion | buy | TSLA | 3.20 | — | rebalance up |
| 2026-10-08T14:55 | Stochastic reversion | buy | TQQQ | 3.11 | — | rebalance up |
| 2026-10-08T14:55 | Stochastic reversion | buy | SOXL | 3.01 | — | rebalance up |
| 2026-10-08T14:55 | Stochastic reversion | buy | QQQ | 3.12 | — | rebalance up |
| 2026-10-08T14:55 | Stochastic reversion | buy | AMD | 3.11 | — | rebalance up |
| 2026-10-08T14:55 | Stochastic reversion | sell | TNA | 4.27 | -0.05 | stop-loss |
| 2026-10-08T14:55 | Z-score reversion | buy | TSLA | 1.45 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 15:00:05.000159+00:00 -> 2026-10-08 15:10:05.000159+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
