# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T14:30:05.000154+00:00 · 15672 ticks

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

Today: 14338 decisions in 2126 calls, $0.1908 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T14:30 | 2 / 25 / 3 | NANC 16%, TECL 14% |  |
| Breezy | 2026-10-08T14:30 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-08T14:30 | 5 / 24 / 1 | COIN 57% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.29 | 5.29 | 0 | — | -1.89 | -0.26 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.28 | 2.28 | 34 | 41.2 | -8.73 | -2.71 | -13.79 | 117 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.06 | 2.06 | 0 | — | -0.16 | -0.06 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 6 | Hold SPY | benchmark | 101.17 | 1.17 | 0 | — | 0.34 | 0.25 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.14 | 1.14 | 0 | — | 1.94 | 0.95 | -3.62 | 1 |
| 8 | Copy: Warren Buffett (BRK-B) | copy | 100.96 | 0.96 | 0 | — | -2.30 | -0.90 | -7.65 | 1 |
| 9 | Donchian 55/20 · 1h | breakout | 100.87 | 0.87 | 18 | 5.6 | 11.66 | 1.59 | -16.96 | 109 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 99.84 | -0.16 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 99.82 | -0.18 | 30 | 36.7 | 5.36 | 2.52 | -1.52 | 86 |
| 14 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 5 | 40.0 | -4.05 | -1.37 | -9.74 | 23 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Daily: SMA 20/50 cross · AAPL | daily | 99.07 | -0.93 | 0 | — | -0.47 | -0.09 | -5.18 | 1 |
| 18 | Trend pullback · 1h | trend | 99.02 | -0.98 | 70 | 25.7 | -21.52 | -6.23 | -24.25 | 170 |
| 19 | Hold BTC | benchmark | 99.01 | -0.99 | 0 | — | 26.79 | 3.24 | -8.68 | 1 |
| 20 | Daily: Bullish score | daily | 98.23 | -1.77 | 3 | 0.0 | 1.10 | 0.34 | -12.76 | 10 |
| 21 | Three white soldiers · 1h | momentum | 98.09 | -1.91 | 4 | 0.0 | -2.46 | -1.92 | -3.95 | 25 |
| 22 | EMA 20/50 cross · 1h | trend | 97.95 | -2.05 | 35 | 8.6 | 2.47 | 0.50 | -17.82 | 138 |
| 23 | Copy: Insider buying | copy | 97.34 | -2.66 | 11 | 54.5 | -16.66 | -3.03 | -21.08 | 75 |
| 24 | Stochastic reversion · 1h | reversion | 97.01 | -2.99 | 70 | 52.9 | -12.67 | -2.52 | -13.12 | 341 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.99 | -3.01 | 0 | — | 12.06 | 1.97 | -7.38 | 1 |
| 26 | Agent (rotation) | meta | 96.21 | -3.79 | 75 | 26.7 | 0.85 | 0.32 | -8.02 | 265 |
| 27 | ADX DI cross · 1h | trend | 96.17 | -3.83 | 52 | 23.1 | -3.47 | -0.38 | -13.84 | 256 |
| 28 | Connors RSI(2) · 1h | reversion | 96.15 | -3.85 | 92 | 44.6 | -16.16 | -5.89 | -18.23 | 234 |
| 29 | Agent | meta | 96.12 | -3.88 | 45 | 55.6 | -9.29 | -5.11 | -10.37 | 238 |
| 30 | Parabolic SAR · 1h | trend | 95.95 | -4.05 | 80 | 21.2 | -5.52 | -0.60 | -20.87 | 292 |
| 31 | Supertrend · 1h | trend | 95.92 | -4.08 | 42 | 9.5 | -2.85 | -0.22 | -17.19 | 208 |
| 32 | Daily: Momentum burst | daily | 95.88 | -4.12 | 4 | 0.0 | -4.33 | -0.50 | -17.52 | 40 |
| 33 | MACD cross · 1h | trend | 95.32 | -4.68 | 103 | 22.3 | -14.36 | -2.25 | -17.27 | 462 |
| 34 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -1.28 | -0.53 | -6.03 | 109 |
| 35 | Candlestick reversal · 1h | reversion | 94.88 | -5.12 | 89 | 31.5 | -26.94 | -5.91 | -27.32 | 503 |
| 36 | Z-score reversion · 1h | reversion | 94.84 | -5.16 | 34 | 38.2 | -3.09 | -0.48 | -8.60 | 158 |
| 37 | Squeeze breakout · 1h | breakout | 94.72 | -5.28 | 34 | 26.5 | 14.27 | 2.38 | -8.13 | 104 |
| 38 | Agent (ML meta-label) | meta | 94.64 | -5.36 | 297 | 15.8 | -3.57 | -0.49 | -15.83 | 370 |
| 39 | RSI(14) reversion · 1h | reversion | 94.52 | -5.48 | 22 | 31.8 | -5.23 | -1.14 | -8.15 | 134 |
| 40 | RSI momentum · 1h | momentum | 94.20 | -5.80 | 52 | 5.8 | 2.04 | 0.46 | -16.53 | 221 |
| 41 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 42 | Bollinger breakout · 1h | breakout | 93.54 | -6.46 | 63 | 30.2 | 7.03 | 1.05 | -12.06 | 291 |
| 43 | Ichimoku · 1h | trend | 93.41 | -6.59 | 39 | 17.9 | -3.10 | -0.23 | -19.68 | 120 |
| 44 | Bollinger reversion · 1h | reversion | 93.15 | -6.85 | 61 | 37.7 | -20.66 | -5.25 | -21.25 | 307 |
| 45 | Triple EMA stack · 1h | trend | 93.09 | -6.91 | 61 | 11.5 | -8.23 | -0.78 | -24.51 | 240 |
| 46 | Opening range 30m | breakout | 92.89 | -7.11 | 113 | 20.4 | -15.82 | -4.77 | -16.77 | 562 |
| 47 | Volume breakout · 1h | breakout | 92.66 | -7.34 | 45 | 17.8 | 6.34 | 1.03 | -12.60 | 122 |
| 48 | Williams %R · 1h | reversion | 92.24 | -7.76 | 100 | 48.0 | -24.98 | -4.52 | -25.29 | 504 |
| 49 | Max aggression: 1-day momentum | meta | 92.04 | -7.96 | 9 | 33.3 | -23.45 | -1.19 | -37.31 | 43 |
| 50 | MFI reversion · 1h | reversion | 91.65 | -8.35 | 89 | 27.0 | -15.08 | -2.62 | -16.99 | 121 |
| 51 | Opening range 15m | breakout | 90.90 | -9.10 | 132 | 18.9 | -17.55 | -5.07 | -18.28 | 680 |
| 52 | Donchian 20/10 · 1h | breakout | 90.86 | -9.14 | 50 | 20.0 | 1.84 | 0.43 | -16.18 | 221 |
| 53 | EMA 9/21 cross · 1h | trend | 90.72 | -9.28 | 91 | 12.1 | -5.21 | -0.50 | -18.95 | 340 |
| 54 | MACD zero-line · 1h | trend | 90.56 | -9.44 | 57 | 19.3 | -6.14 | -0.65 | -19.10 | 239 |
| 55 | Three white soldiers | momentum | 90.16 | -9.84 | 109 | 18.3 | -48.52 | -24.19 | -48.65 | 585 |
| 56 | OBV trend · 1h | momentum | 89.11 | -10.89 | 129 | 17.8 | -15.09 | -1.77 | -28.16 | 324 |
| 57 | CCI reversion · 1h | reversion | 89.06 | -10.94 | 86 | 41.9 | -8.51 | -1.14 | -12.63 | 407 |
| 58 | VWAP momentum · 1h | momentum | 88.92 | -11.08 | 255 | 21.6 | -37.17 | -5.69 | -39.00 | 1272 |
| 59 | Keltner breakout · 1h | breakout | 88.91 | -11.09 | 39 | 17.9 | -10.06 | -1.13 | -23.68 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 88.59 | -11.41 | 130 | 26.2 | -32.21 | -5.50 | -35.72 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.34 | -12.66 | 125 | 20.0 | -8.29 | -0.95 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 84.29 | -15.71 | 7 | 28.6 | -26.61 | -2.37 | -33.47 | 30 |
| 63 | RSI(14) reversion | reversion | 79.30 | -20.70 | 291 | 30.9 | -72.52 | -19.24 | -72.81 | 1481 |
| 64 | ROC + volume | momentum | 75.62 | -24.38 | 335 | 20.3 | -73.09 | -16.93 | -73.66 | 1648 |
| 65 | Squeeze breakout | breakout | 74.92 | -25.08 | 269 | 14.5 | -62.34 | -18.41 | -62.45 | 1216 |
| 66 | Volume breakout | breakout | 72.74 | -27.26 | 217 | 12.0 | -63.96 | -18.63 | -63.96 | 906 |
| 67 | Donchian 55/20 | breakout | 72.65 | -27.35 | 274 | 16.8 | -68.84 | -14.93 | -68.93 | 1290 |
| 68 | EMA 20/50 cross | trend | 72.27 | -27.73 | 282 | 18.1 | -78.27 | -15.87 | -78.32 | 1469 |
| 69 | VWAP reversion | reversion | 71.53 | -28.47 | 336 | 27.4 | -71.21 | -16.45 | -71.28 | 1414 |
| 70 | Supertrend | trend | 67.92 | -32.08 | 387 | 19.4 | -86.94 | -21.66 | -86.97 | 1942 |
| 71 | Keltner breakout | breakout | 65.87 | -34.13 | 370 | 13.0 | -84.97 | -28.81 | -84.97 | 1863 |
| 72 | AI bee: Bizzy | ai | 64.66 | -35.34 | 667 | 8.4 | — | — | — | — |
| 73 | Ichimoku | trend | 64.58 | -35.42 | 340 | 8.8 | -81.78 | -23.64 | -81.78 | 1738 |
| 74 | MFI reversion | reversion | 64.40 | -35.60 | 422 | 21.1 | -87.75 | -29.69 | -87.81 | 2125 |
| 75 | Z-score reversion | reversion | 63.80 | -36.20 | 431 | 24.1 | -85.59 | -24.08 | -85.73 | 2090 |
| 76 | ADX DI cross | trend | 61.74 | -38.26 | 440 | 8.9 | -89.60 | -35.42 | -89.61 | 2117 |
| 77 | AI bee: Boozy | ai | 61.50 | -38.50 | 234 | 4.7 | — | — | — | — |
| 78 | MACD zero-line | trend | 60.85 | -39.15 | 493 | 15.0 | -91.52 | -29.90 | -91.53 | 2367 |
| 79 | Donchian 20/10 | breakout | 60.74 | -39.26 | 525 | 17.9 | -91.07 | -26.64 | -91.07 | 2656 |
| 80 | Trend pullback | trend | 59.78 | -40.22 | 497 | 15.5 | -90.83 | -27.94 | -90.84 | 2314 |
| 81 | RSI momentum | momentum | 59.45 | -40.55 | 487 | 16.6 | -90.54 | -25.81 | -90.54 | 2368 |
| 82 | Triple EMA stack | trend | 58.86 | -41.14 | 523 | 15.5 | -93.28 | -31.13 | -93.28 | 2605 |
| 83 | Consensus | meta | 56.61 | -43.39 | 510 | 10.4 | -94.16 | -25.09 | -94.16 | 2675 |
| 84 | Bollinger breakout | breakout | 56.52 | -43.48 | 548 | 13.7 | -93.78 | -34.01 | -93.79 | 2821 |
| 85 | EMA 9/21 cross | trend | 53.25 | -46.75 | 666 | 16.1 | -97.39 | -33.78 | -97.40 | 3534 |
| 86 | Connors RSI(2) | reversion | 52.67 | -47.33 | 702 | 20.1 | -96.30 | -32.32 | -96.30 | 3582 |
| 87 | Stochastic reversion | reversion | 52.42 | -47.58 | 786 | 21.8 | -95.66 | -35.10 | -95.71 | 4059 |
| 88 | Bollinger reversion | reversion | 50.96 | -49.04 | 748 | 17.5 | -95.85 | -34.34 | -95.88 | 3722 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -31.02 | -98.70 | 5367 |
| 90 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -36.79 | -96.34 | 3570 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.33 | -37.83 | -99.34 | 5669 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.57 | -99.73 | 6157 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -39.54 | -97.35 | 3654 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.90 | -98.50 | 4709 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.13 | -99.52 | 6119 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.46 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T14:30 | Consensus | buy | AMZN | 14.15 | — | entry |
| 2026-10-08T14:30 | Consensus | sell | UPRO | 14.16 | 0.01 | target is flat |
| 2026-10-08T14:30 | Agent | sell | SOXL | 19.75 | 0.66 | selected signal exited |
| 2026-10-08T14:30 | CCI reversion · 1h | buy | META | 22.27 | — | entry signal |
| 2026-10-08T14:30 | Williams %R · 1h | buy | NVDA | 13.13 | — | entry signal |
| 2026-10-08T14:30 | Williams %R · 1h | buy | COIN | 13.19 | — | entry signal |
| 2026-10-08T14:30 | Williams %R · 1h | sell | XRP-USD | 5.08 | -0.01 | rebalance down |
| 2026-10-08T14:30 | Williams %R · 1h | sell | UPRO | 5.38 | 0.01 | rebalance down |
| 2026-10-08T14:30 | Williams %R · 1h | sell | TSLA | 5.30 | -0.01 | rebalance down |
| 2026-10-08T14:30 | Williams %R · 1h | sell | ETH-USD | 5.24 | -0.01 | rebalance down |
| 2026-10-08T14:30 | Williams %R · 1h | sell | BTC-USD | 5.33 | -0.02 | rebalance down |
| 2026-10-08T14:30 | Connors RSI(2) · 1h | buy | TSLA | 24.05 | — | entry signal |
| 2026-10-08T14:30 | Connors RSI(2) · 1h | buy | MSTR | 24.05 | — | entry signal |
| 2026-10-08T14:30 | Connors RSI(2) · 1h | buy | BITX | 24.05 | — | entry signal |
| 2026-10-08T14:30 | Candlestick reversal · 1h | buy | META | 14.26 | — | entry signal |
| 2026-10-08T14:30 | Candlestick reversal · 1h | buy | ETHU | 18.98 | — | entry signal |
| 2026-10-08T14:30 | Candlestick reversal · 1h | sell | XRP-USD | 4.86 | -0.00 | rebalance down |
| 2026-10-08T14:30 | Candlestick reversal · 1h | sell | DOGE-USD | 4.81 | -0.01 | rebalance down |
| 2026-10-08T14:30 | Volume breakout · 1h | buy | PLTR | 23.17 | — | entry signal |
| 2026-10-08T14:30 | Squeeze breakout · 1h | buy | AAPL | 23.68 | — | entry signal |
| 2026-10-08T14:30 | Keltner breakout · 1h | buy | PLTR | 22.23 | — | entry signal |
| 2026-10-08T14:30 | Bollinger breakout · 1h | buy | PLTR | 23.39 | — | entry signal |
| 2026-10-08T14:30 | OBV trend · 1h | buy | QQQ | 8.86 | — | rebalance up |
| 2026-10-08T14:30 | OBV trend · 1h | sell | TSLA | 9.90 | -0.02 | exit signal |
| 2026-10-08T14:30 | RSI momentum · 1h | sell | TSLA | 4.69 | 0.03 | exit signal |
| 2026-10-08T14:30 | ROC + volume · 1h | buy | GOOGL | 21.84 | — | entry signal |
| 2026-10-08T14:30 | ROC + volume · 1h | buy | AAPL | 21.84 | — | entry signal |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | UPRO | 6.76 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | SPY | 6.76 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | QQQ | 6.75 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | BITX | 6.70 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | AMZN | 6.75 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | AMD | 6.71 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | buy | AAPL | 6.74 | — | rebalance up |
| 2026-10-08T14:30 | VWAP momentum · 1h | sell | TSLA | 5.94 | -0.01 | exit signal |
| 2026-10-08T14:30 | VWAP momentum · 1h | sell | PLTR | 5.85 | -0.10 | exit signal |
| 2026-10-08T14:30 | VWAP momentum · 1h | sell | MSFT | 5.91 | -0.04 | exit signal |
| 2026-10-08T14:30 | VWAP momentum · 1h | sell | GOOGL | 5.90 | -0.05 | exit signal |
| 2026-10-08T14:30 | Trend pullback · 1h | buy | TECL | 11.00 | — | entry signal |
| 2026-10-08T14:30 | Heikin-Ashi · 1h | buy | PLTR | 9.64 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 14:30:05.000154+00:00 -> 2026-10-08 14:40:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
