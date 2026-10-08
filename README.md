# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T16:30:05.000148+00:00 · 15772 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.15 (-3.85%)

Closed trades 46, win rate 56.5%, fees £1.93, max drawdown -4.99%.

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

Today: 23344 decisions in 2426 calls, $0.2965 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T16:30 | 1 / 13 / 16 | TNA 16% |  |
| Breezy | 2026-10-08T16:30 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-08T16:30 | 2 / 27 / 1 | MSTR 64% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.96 | +0.82% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 104.16 | 4.16 | 0 | — | -2.55 | -0.39 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 35 | 40.0 | -8.49 | -2.63 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.72 | 1.72 | 0 | — | -0.38 | -0.18 | -5.09 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.54 | 0.65 | -4.29 | 18 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.31 | 1.31 | 0 | — | 2.07 | 1.01 | -3.62 | 1 |
| 7 | Hold SPY | benchmark | 101.09 | 1.09 | 0 | — | 0.40 | 0.29 | -3.66 | 1 |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 100.79 | 0.79 | 0 | — | -2.52 | -1.00 | -7.65 | 1 |
| 9 | Donchian 55/20 · 1h | breakout | 100.35 | 0.35 | 18 | 5.6 | 12.75 | 1.67 | -16.96 | 109 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 15 | Daily: SMA 20/50 cross · AAPL | daily | 99.40 | -0.60 | 0 | — | 0.58 | 0.30 | -5.18 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.81 | -1.20 | 0 | — | -5.19 | -2.48 | -5.49 | 1 |
| 18 | Trend pullback · 1h | trend | 98.52 | -1.48 | 70 | 25.7 | -22.27 | -6.48 | -24.37 | 172 |
| 19 | Copy: Insider buying | copy | 98.13 | -1.87 | 12 | 50.0 | -15.95 | -2.86 | -21.08 | 75 |
| 20 | Three white soldiers · 1h | momentum | 97.91 | -2.09 | 4 | 0.0 | -2.65 | -2.08 | -3.95 | 25 |
| 21 | EMA 20/50 cross · 1h | trend | 97.59 | -2.41 | 35 | 8.6 | -0.93 | 0.07 | -18.58 | 138 |
| 22 | Hold BTC | benchmark | 97.34 | -2.66 | 0 | — | 25.50 | 3.08 | -8.68 | 1 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 96.67 | -3.33 | 0 | — | 11.65 | 1.91 | -7.75 | 1 |
| 24 | Agent (rotation) | meta | 96.29 | -3.71 | 76 | 26.3 | 1.94 | 0.63 | -7.88 | 261 |
| 25 | ADX DI cross · 1h | trend | 96.15 | -3.85 | 53 | 22.6 | -6.85 | -1.03 | -13.84 | 260 |
| 26 | Agent | meta | 96.15 | -3.85 | 46 | 56.5 | -11.31 | -6.21 | -11.67 | 235 |
| 27 | Daily: Momentum burst | daily | 95.91 | -4.09 | 4 | 0.0 | -3.64 | -0.39 | -17.53 | 40 |
| 28 | Supertrend · 1h | trend | 95.62 | -4.38 | 46 | 13.0 | -3.01 | -0.24 | -17.19 | 210 |
| 29 | Parabolic SAR · 1h | trend | 95.60 | -4.40 | 81 | 22.2 | -5.07 | -0.53 | -20.80 | 292 |
| 30 | Stochastic reversion · 1h | reversion | 95.39 | -4.61 | 74 | 50.0 | -14.10 | -2.74 | -14.77 | 345 |
| 31 | Daily: Bullish score | daily | 95.36 | -4.64 | 3 | 0.0 | -1.92 | -0.05 | -12.76 | 10 |
| 32 | MACD cross · 1h | trend | 95.28 | -4.72 | 103 | 22.3 | -11.27 | -1.59 | -17.27 | 462 |
| 33 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -6.14 | -2.65 | -6.63 | 118 |
| 34 | Connors RSI(2) · 1h | reversion | 95.06 | -4.95 | 93 | 44.1 | -17.14 | -6.10 | -19.64 | 242 |
| 35 | Squeeze breakout · 1h | breakout | 94.80 | -5.20 | 34 | 26.5 | 14.85 | 2.46 | -8.14 | 104 |
| 36 | Z-score reversion · 1h | reversion | 94.27 | -5.73 | 35 | 37.1 | -2.58 | -0.39 | -8.60 | 160 |
| 37 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 38 | RSI momentum · 1h | momentum | 93.81 | -6.19 | 54 | 9.3 | 5.10 | 0.81 | -16.57 | 217 |
| 39 | Agent (ML meta-label) | meta | 93.77 | -6.23 | 311 | 16.7 | -1.70 | -0.17 | -10.94 | 378 |
| 40 | Bollinger breakout · 1h | breakout | 93.41 | -6.59 | 63 | 30.2 | 5.48 | 0.87 | -12.06 | 289 |
| 41 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | -0.71 | 0.12 | -20.61 | 118 |
| 42 | Triple EMA stack · 1h | trend | 92.62 | -7.38 | 62 | 12.9 | -10.63 | -1.19 | -24.52 | 241 |
| 43 | Volume breakout · 1h | breakout | 92.47 | -7.53 | 45 | 17.8 | 6.01 | 0.99 | -12.60 | 122 |
| 44 | RSI(14) reversion · 1h | reversion | 92.13 | -7.87 | 26 | 26.9 | -3.46 | -0.65 | -8.68 | 137 |
| 45 | Candlestick reversal · 1h | reversion | 91.83 | -8.17 | 93 | 30.1 | -29.26 | -5.93 | -29.37 | 505 |
| 46 | Opening range 30m | breakout | 91.57 | -8.43 | 122 | 18.9 | -16.92 | -5.15 | -17.30 | 566 |
| 47 | Max aggression: 1-day momentum | meta | 91.31 | -8.69 | 9 | 33.3 | -24.09 | -1.24 | -37.31 | 43 |
| 48 | Williams %R · 1h | reversion | 90.83 | -9.17 | 103 | 46.6 | -25.57 | -4.53 | -26.55 | 502 |
| 49 | MFI reversion · 1h | reversion | 90.79 | -9.21 | 90 | 26.7 | -15.86 | -2.72 | -16.95 | 124 |
| 50 | MACD zero-line · 1h | trend | 90.61 | -9.39 | 57 | 19.3 | -5.85 | -0.61 | -19.10 | 238 |
| 51 | EMA 9/21 cross · 1h | trend | 90.45 | -9.55 | 93 | 14.0 | -6.57 | -0.69 | -18.95 | 333 |
| 52 | Donchian 20/10 · 1h | breakout | 90.43 | -9.57 | 50 | 20.0 | -1.71 | -0.00 | -16.18 | 222 |
| 53 | Bollinger reversion · 1h | reversion | 90.25 | -9.75 | 68 | 33.8 | -23.27 | -5.35 | -23.63 | 312 |
| 54 | Three white soldiers | momentum | 89.56 | -10.44 | 114 | 19.3 | -48.91 | -24.58 | -48.99 | 586 |
| 55 | Opening range 15m | breakout | 89.00 | -11.00 | 144 | 17.4 | -19.13 | -5.55 | -19.13 | 686 |
| 56 | Keltner breakout · 1h | breakout | 88.70 | -11.30 | 39 | 17.9 | -9.39 | -1.01 | -23.68 | 224 |
| 57 | OBV trend · 1h | momentum | 88.58 | -11.42 | 135 | 17.8 | -15.50 | -1.83 | -28.22 | 322 |
| 58 | Heikin-Ashi · 1h | trend | 88.22 | -11.79 | 132 | 25.8 | -32.75 | -5.62 | -35.84 | 689 |
| 59 | VWAP momentum · 1h | momentum | 88.19 | -11.81 | 261 | 21.5 | -37.03 | -5.67 | -39.16 | 1262 |
| 60 | CCI reversion · 1h | reversion | 87.82 | -12.18 | 90 | 41.1 | -9.89 | -1.33 | -13.90 | 406 |
| 61 | ROC + volume · 1h | momentum | 87.05 | -12.95 | 126 | 20.6 | -9.53 | -1.14 | -23.15 | 409 |
| 62 | Max aggression: 5-day momentum | meta | 83.62 | -16.38 | 7 | 28.6 | -27.22 | -2.43 | -33.98 | 30 |
| 63 | RSI(14) reversion | reversion | 77.84 | -22.16 | 305 | 30.8 | -73.12 | -18.98 | -73.21 | 1468 |
| 64 | ROC + volume | momentum | 75.42 | -24.58 | 337 | 20.2 | -73.38 | -17.11 | -73.91 | 1639 |
| 65 | Squeeze breakout | breakout | 74.46 | -25.54 | 271 | 14.4 | -62.57 | -18.67 | -62.57 | 1217 |
| 66 | Donchian 55/20 | breakout | 72.68 | -27.32 | 274 | 16.8 | -68.78 | -14.95 | -68.81 | 1282 |
| 67 | Volume breakout | breakout | 72.64 | -27.36 | 218 | 11.9 | -64.06 | -18.74 | -64.07 | 911 |
| 68 | EMA 20/50 cross | trend | 72.02 | -27.98 | 283 | 18.0 | -78.08 | -15.75 | -78.11 | 1459 |
| 69 | VWAP reversion | reversion | 70.08 | -29.92 | 346 | 27.5 | -71.69 | -16.24 | -71.80 | 1413 |
| 70 | Supertrend | trend | 66.87 | -33.13 | 398 | 18.8 | -87.01 | -21.45 | -87.13 | 1931 |
| 71 | Keltner breakout | breakout | 65.76 | -34.24 | 371 | 12.9 | -85.03 | -28.91 | -85.04 | 1866 |
| 72 | AI bee: Bizzy | ai | 64.42 | -35.58 | 673 | 8.5 | — | — | — | — |
| 73 | Ichimoku | trend | 64.17 | -35.83 | 343 | 8.7 | -81.89 | -23.62 | -81.89 | 1736 |
| 74 | MFI reversion | reversion | 63.39 | -36.61 | 435 | 21.4 | -87.97 | -29.51 | -88.01 | 2127 |
| 75 | Z-score reversion | reversion | 63.17 | -36.83 | 444 | 24.1 | -85.88 | -24.10 | -85.92 | 2095 |
| 76 | AI bee: Boozy | ai | 61.11 | -38.89 | 235 | 5.1 | — | — | — | — |
| 77 | ADX DI cross | trend | 60.97 | -39.03 | 453 | 8.8 | -89.74 | -35.64 | -89.76 | 2138 |
| 78 | MACD zero-line | trend | 59.95 | -40.05 | 500 | 14.8 | -91.63 | -29.94 | -91.63 | 2359 |
| 79 | Donchian 20/10 | breakout | 59.95 | -40.05 | 529 | 17.8 | -91.11 | -26.61 | -91.12 | 2656 |
| 80 | Trend pullback | trend | 59.47 | -40.53 | 503 | 15.3 | -90.80 | -28.04 | -90.80 | 2305 |
| 81 | RSI momentum | momentum | 58.78 | -41.22 | 495 | 16.4 | -90.62 | -25.82 | -90.62 | 2351 |
| 82 | Triple EMA stack | trend | 58.67 | -41.33 | 526 | 15.4 | -93.30 | -31.08 | -93.30 | 2606 |
| 83 | Consensus | meta | 56.53 | -43.47 | 512 | 10.4 | -94.18 | -25.44 | -94.18 | 2663 |
| 84 | Bollinger breakout | breakout | 56.14 | -43.86 | 550 | 13.6 | -93.80 | -33.98 | -93.81 | 2821 |
| 85 | Connors RSI(2) | reversion | 52.75 | -47.25 | 709 | 20.6 | -96.27 | -32.29 | -96.28 | 3575 |
| 86 | EMA 9/21 cross | trend | 52.46 | -47.54 | 677 | 15.8 | -97.42 | -33.80 | -97.42 | 3540 |
| 87 | Stochastic reversion | reversion | 51.71 | -48.29 | 809 | 22.4 | -95.69 | -34.98 | -95.73 | 4068 |
| 88 | Bollinger reversion | reversion | 50.69 | -49.31 | 759 | 17.8 | -95.84 | -34.11 | -95.87 | 3724 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -30.87 | -98.70 | 5376 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.37 | -37.13 | -96.37 | 3569 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -37.21 | -99.34 | 5658 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.03 | -99.73 | 6136 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -39.64 | -97.39 | 3642 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.63 | -98.51 | 4706 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.97 | -99.52 | 6120 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.93 | -99.90 | 8247 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T16:30 | Agent (ML meta-label) | buy | TNA | 5.52 | — | entry |
| 2026-10-08T16:30 | Agent (ML meta-label) | buy | LABU | 5.52 | — | entry |
| 2026-10-08T16:30 | Agent (ML meta-label) | buy | GOOGL | 5.52 | — | entry |
| 2026-10-08T16:30 | Agent (ML meta-label) | buy | BITX | 5.52 | — | following Bollinger breakout |
| 2026-10-08T16:30 | Consensus | buy | SPY | 14.14 | — | entry |
| 2026-10-08T16:30 | MFI reversion · 1h | buy | TNA | 22.70 | — | entry signal |
| 2026-10-08T16:30 | CCI reversion · 1h | sell | SQQQ | 17.88 | 0.26 | exit signal |
| 2026-10-08T16:30 | Williams %R · 1h | buy | SPY | 9.18 | — | entry signal |
| 2026-10-08T16:30 | Williams %R · 1h | sell | UPRO | 4.56 | 0.01 | rebalance down |
| 2026-10-08T16:30 | Williams %R · 1h | sell | TSLA | 4.62 | 0.00 | rebalance down |
| 2026-10-08T16:30 | Stochastic reversion · 1h | buy | TNA | 13.62 | — | entry signal |
| 2026-10-08T16:30 | Stochastic reversion · 1h | buy | MSTR | 13.63 | — | entry signal |
| 2026-10-08T16:30 | Stochastic reversion · 1h | buy | IWM | 13.63 | — | entry signal |
| 2026-10-08T16:30 | Stochastic reversion · 1h | sell | TSLA | 5.73 | -0.00 | rebalance down |
| 2026-10-08T16:30 | Stochastic reversion · 1h | sell | SQQQ | 5.76 | 0.03 | rebalance down |
| 2026-10-08T16:30 | Stochastic reversion · 1h | sell | META | 5.66 | -0.03 | rebalance down |
| 2026-10-08T16:30 | Stochastic reversion · 1h | sell | LABU | 10.01 | -0.12 | rebalance down |
| 2026-10-08T16:30 | Z-score reversion · 1h | buy | TNA | 23.57 | — | entry signal |
| 2026-10-08T16:30 | Z-score reversion · 1h | buy | IWM | 23.57 | — | entry signal |
| 2026-10-08T16:30 | Bollinger reversion · 1h | buy | TSLA | 22.46 | — | entry signal |
| 2026-10-08T16:30 | Bollinger reversion · 1h | buy | BITX | 22.57 | — | entry signal |
| 2026-10-08T16:30 | Connors RSI(2) · 1h | buy | NVDA | 9.45 | — | entry signal |
| 2026-10-08T16:30 | RSI(14) reversion · 1h | buy | TNA | 23.04 | — | entry signal |
| 2026-10-08T16:30 | RSI(14) reversion · 1h | buy | MSTR | 23.04 | — | entry signal |
| 2026-10-08T16:30 | RSI(14) reversion · 1h | buy | IWM | 23.04 | — | entry signal |
| 2026-10-08T16:30 | Candlestick reversal · 1h | buy | SOXL | 22.74 | — | entry signal |
| 2026-10-08T16:30 | Candlestick reversal · 1h | buy | LABU | 22.97 | — | entry signal |
| 2026-10-08T16:30 | Candlestick reversal · 1h | buy | BITX | 22.97 | — | entry signal |
| 2026-10-08T16:30 | RSI momentum · 1h | buy | AMZN | 5.96 | — | rebalance up |
| 2026-10-08T16:30 | RSI momentum · 1h | sell | NVDA | 8.06 | 0.18 | exit signal |
| 2026-10-08T16:30 | RSI momentum · 1h | sell | AMD | 4.51 | 0.01 | exit signal |
| 2026-10-08T16:30 | ROC + volume · 1h | buy | SQQQ | 21.76 | — | entry signal |
| 2026-10-08T16:30 | VWAP momentum · 1h | buy | MSFT | 22.05 | — | entry signal |
| 2026-10-08T16:30 | Heikin-Ashi · 1h | sell | GOOGL | 21.98 | -0.29 | exit signal |
| 2026-10-08T16:30 | ADX DI cross · 1h | buy | SPY | 24.04 | — | entry signal |
| 2026-10-08T16:30 | Parabolic SAR · 1h | sell | AMZN | 24.04 | 0.44 | exit signal |
| 2026-10-08T16:30 | Supertrend · 1h | buy | GOOGL | 5.27 | — | rebalance up |
| 2026-10-08T16:30 | Supertrend · 1h | buy | AMZN | 4.89 | — | rebalance up |
| 2026-10-08T16:30 | Supertrend · 1h | sell | AMD | 9.51 | -0.09 | exit signal |
| 2026-10-08T16:30 | EMA 9/21 cross · 1h | sell | TSLA | 6.13 | 0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 16:30:05.000148+00:00 -> 2026-10-08 16:40:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
