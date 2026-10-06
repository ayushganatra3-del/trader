# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T15:31:05.000166+00:00 · 13607 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.29 (-1.71%)

Closed trades 37, win rate 62.2%, fees £1.28, max drawdown -2.16%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-05)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.70 · VIX 15.52 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.8, AMD 7.6, TECL 7.6, MSTR 7.5, BITX 7.5, ETHU 7.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 17776 decisions in 2213 calls, $0.2302 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T15:31 | 1 / 23 / 6 | NANC 19% |  |
| Breezy | 2026-10-06T15:31 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-06T15:31 | 0 / 28 / 2 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| Volume breakout | LABU | 1.95 | +2.51% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 107.09 | 7.09 | 0 | — | -0.24 | 0.09 | -15.27 | 1 |
| 2 | Hold BTC | benchmark | 102.83 | 2.83 | 0 | — | 33.06 | 3.98 | -8.68 | 1 |
| 3 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.17 | -2.90 | -13.93 | 113 |
| 4 | Daily: Bullish score | daily | 102.50 | 2.50 | 3 | 0.0 | 6.42 | 1.04 | -12.76 | 10 |
| 5 | Donchian 55/20 · 1h | breakout | 102.36 | 2.36 | 17 | 0.0 | 9.99 | 1.40 | -16.96 | 111 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 102.28 | 2.28 | 0 | — | 0.43 | 0.29 | -5.09 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 102.00 | 2.00 | 0 | — | 3.38 | 1.59 | -3.62 | 1 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.32 | 1.32 | 0 | — | 1.20 | 0.76 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.76 | 0.76 | 66 | 39.4 | -22.25 | -5.22 | -24.74 | 480 |
| 13 | EMA 20/50 cross · 1h | trend | 100.74 | 0.74 | 28 | 7.1 | 15.05 | 1.84 | -15.31 | 141 |
| 14 | Copy: Cathie Wood (ARKK) | copy | 100.63 | 0.63 | 0 | — | 19.02 | 2.90 | -6.29 | 1 |
| 15 | Stochastic reversion · 1h | reversion | 100.55 | 0.55 | 56 | 64.3 | -7.26 | -1.48 | -10.70 | 326 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.42 | 0.42 | 0 | — | -1.45 | -0.52 | -7.65 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 100.13 | 0.13 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.90 | 1.88 | -1.59 | 84 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 20 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 21 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 22 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.71 | -1.65 | -9.74 | 23 |
| 23 | Z-score reversion · 1h | reversion | 99.94 | -0.06 | 22 | 54.5 | 6.45 | 1.47 | -8.60 | 150 |
| 24 | Bollinger reversion · 1h | reversion | 99.93 | -0.07 | 48 | 47.9 | -14.06 | -3.64 | -16.98 | 303 |
| 25 | Trend pullback · 1h | trend | 99.88 | -0.12 | 62 | 25.8 | -20.13 | -5.85 | -24.20 | 169 |
| 26 | Connors RSI(2) · 1h | reversion | 99.63 | -0.37 | 72 | 44.4 | -13.16 | -4.50 | -17.01 | 220 |
| 27 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 5.33 | 1.54 | -6.57 | 113 |
| 28 | Williams %R · 1h | reversion | 99.02 | -0.98 | 84 | 53.6 | -18.00 | -3.35 | -20.60 | 492 |
| 29 | Daily: Momentum burst | daily | 98.68 | -1.32 | 3 | 0.0 | 0.85 | 0.31 | -16.91 | 41 |
| 30 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -2.09 | -1.11 | -4.94 | 104 |
| 31 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 32 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.83 | -5.68 | -10.25 | 229 |
| 33 | Agent (rotation) | meta | 98.01 | -1.99 | 62 | 29.0 | 2.13 | 0.66 | -8.79 | 256 |
| 34 | ADX DI cross · 1h | trend | 97.92 | -2.08 | 41 | 12.2 | -1.80 | -0.16 | -13.84 | 252 |
| 35 | Copy: Insider buying | copy | 97.90 | -2.10 | 9 | 55.6 | -15.55 | -2.87 | -21.08 | 73 |
| 36 | Agent (ML meta-label) | meta | 97.68 | -2.32 | 253 | 15.0 | 3.59 | 0.80 | -13.15 | 371 |
| 37 | Supertrend · 1h | trend | 97.63 | -2.37 | 32 | 9.4 | 3.90 | 0.71 | -16.43 | 212 |
| 38 | CCI reversion · 1h | reversion | 97.38 | -2.62 | 71 | 49.3 | 0.42 | 0.23 | -12.41 | 409 |
| 39 | Daily: SMA 20/50 cross · AAPL | daily | 97.34 | -2.66 | 0 | — | 0.02 | 0.09 | -5.18 | 1 |
| 40 | Parabolic SAR · 1h | trend | 97.21 | -2.79 | 62 | 16.1 | -2.23 | -0.10 | -19.45 | 301 |
| 41 | MACD cross · 1h | trend | 96.64 | -3.36 | 82 | 19.5 | -6.91 | -0.92 | -17.27 | 479 |
| 42 | RSI momentum · 1h | momentum | 96.30 | -3.69 | 45 | 2.2 | 2.15 | 0.48 | -16.65 | 227 |
| 43 | Squeeze breakout · 1h | breakout | 96.08 | -3.92 | 27 | 22.2 | 16.50 | 2.75 | -8.06 | 106 |
| 44 | Ichimoku · 1h | trend | 95.98 | -4.02 | 31 | 16.1 | 9.77 | 1.32 | -15.84 | 124 |
| 45 | Triple EMA stack · 1h | trend | 95.56 | -4.44 | 56 | 10.7 | -6.92 | -0.66 | -24.34 | 244 |
| 46 | Bollinger breakout · 1h | breakout | 95.26 | -4.74 | 46 | 26.1 | 6.81 | 1.04 | -12.06 | 299 |
| 47 | MFI reversion · 1h | reversion | 95.20 | -4.80 | 73 | 27.4 | -9.91 | -1.71 | -16.99 | 118 |
| 48 | Max aggression: 1-day momentum | meta | 94.94 | -5.06 | 7 | 42.9 | -23.51 | -1.21 | -37.31 | 42 |
| 49 | Gap and go | momentum | 94.56 | -5.44 | 43 | 7.0 | 7.09 | 1.85 | -6.40 | 201 |
| 50 | Opening range 30m | breakout | 94.36 | -5.64 | 93 | 22.6 | -17.11 | -5.34 | -17.32 | 572 |
| 51 | Volume breakout · 1h | breakout | 94.24 | -5.76 | 35 | 11.4 | 6.58 | 1.07 | -12.60 | 133 |
| 52 | EMA 9/21 cross · 1h | trend | 93.56 | -6.44 | 78 | 11.5 | -1.49 | -0.00 | -18.47 | 347 |
| 53 | Max aggression: 5-day momentum | meta | 93.20 | -6.80 | 5 | 40.0 | -18.22 | -1.52 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.85 | -7.15 | 105 | 21.0 | -18.05 | -5.35 | -18.88 | 691 |
| 55 | MACD zero-line · 1h | trend | 92.09 | -7.91 | 43 | 18.6 | -1.07 | 0.05 | -18.32 | 249 |
| 56 | Donchian 20/10 · 1h | breakout | 92.02 | -7.98 | 36 | 16.7 | 2.46 | 0.51 | -16.18 | 229 |
| 57 | VWAP momentum · 1h | momentum | 91.67 | -8.33 | 210 | 24.3 | -37.39 | -5.74 | -37.88 | 1291 |
| 58 | Three white soldiers | momentum | 91.46 | -8.54 | 96 | 19.8 | -49.07 | -24.28 | -49.55 | 588 |
| 59 | OBV trend · 1h | momentum | 91.28 | -8.72 | 103 | 11.7 | -11.19 | -1.21 | -26.71 | 338 |
| 60 | Heikin-Ashi · 1h | trend | 90.69 | -9.31 | 108 | 24.1 | -31.04 | -5.34 | -34.14 | 701 |
| 61 | Keltner breakout · 1h | breakout | 90.26 | -9.74 | 30 | 6.7 | -11.00 | -1.27 | -23.31 | 230 |
| 62 | ROC + volume · 1h | momentum | 88.19 | -11.81 | 101 | 15.8 | -9.41 | -1.12 | -23.04 | 425 |
| 63 | RSI(14) reversion | reversion | 85.70 | -14.30 | 217 | 31.8 | -70.76 | -19.64 | -71.09 | 1414 |
| 64 | VWAP reversion | reversion | 78.11 | -21.89 | 259 | 29.0 | -68.48 | -15.87 | -69.03 | 1363 |
| 65 | Squeeze breakout | breakout | 77.88 | -22.11 | 244 | 15.6 | -62.50 | -19.15 | -62.59 | 1227 |
| 66 | ROC + volume | momentum | 77.10 | -22.90 | 313 | 20.1 | -73.84 | -17.82 | -73.99 | 1667 |
| 67 | Donchian 55/20 | breakout | 76.60 | -23.40 | 244 | 18.0 | -69.03 | -15.43 | -69.04 | 1309 |
| 68 | EMA 20/50 cross | trend | 75.43 | -24.57 | 257 | 19.1 | -78.17 | -16.06 | -78.30 | 1486 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.46 | -19.85 | -65.55 | 936 |
| 70 | Z-score reversion | reversion | 72.98 | -27.02 | 344 | 28.2 | -84.86 | -25.33 | -85.06 | 2063 |
| 71 | MFI reversion | reversion | 71.17 | -28.83 | 330 | 20.9 | -86.80 | -30.14 | -86.96 | 2106 |
| 72 | Supertrend | trend | 71.05 | -28.95 | 338 | 21.0 | -86.92 | -22.50 | -87.00 | 1932 |
| 73 | Keltner breakout | breakout | 68.41 | -31.59 | 339 | 13.3 | -85.58 | -30.92 | -85.60 | 1900 |
| 74 | AI bee: Bizzy | ai | 67.86 | -32.14 | 593 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 67.43 | -32.57 | 302 | 8.9 | -82.48 | -24.95 | -82.52 | 1776 |
| 76 | AI bee: Boozy | ai | 66.88 | -33.12 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.59 | -34.41 | 377 | 9.0 | -89.68 | -38.24 | -89.76 | 2107 |
| 78 | MACD zero-line | trend | 64.09 | -35.91 | 434 | 15.7 | -91.53 | -31.23 | -91.54 | 2363 |
| 79 | Donchian 20/10 | breakout | 63.44 | -36.56 | 464 | 18.5 | -91.27 | -28.28 | -91.28 | 2681 |
| 80 | RSI momentum | momentum | 62.69 | -37.31 | 435 | 16.6 | -90.64 | -27.34 | -90.66 | 2386 |
| 81 | Trend pullback | trend | 61.19 | -38.81 | 454 | 15.9 | -91.37 | -31.06 | -91.39 | 2348 |
| 82 | Triple EMA stack | trend | 60.98 | -39.02 | 484 | 15.7 | -93.37 | -32.99 | -93.38 | 2635 |
| 83 | Bollinger breakout | breakout | 60.02 | -39.98 | 484 | 14.3 | -94.09 | -36.54 | -94.09 | 2838 |
| 84 | Stochastic reversion | reversion | 58.87 | -41.13 | 672 | 22.9 | -95.49 | -37.76 | -95.58 | 4014 |
| 85 | Bollinger reversion | reversion | 58.61 | -41.39 | 626 | 17.7 | -95.57 | -36.68 | -95.65 | 3666 |
| 86 | Consensus | meta | 58.08 | -41.92 | 446 | 10.1 | -94.60 | -27.05 | -94.60 | 2693 |
| 87 | EMA 9/21 cross | trend | 56.48 | -43.52 | 593 | 16.7 | -97.42 | -35.78 | -97.42 | 3552 |
| 88 | Connors RSI(2) | reversion | 54.79 | -45.21 | 610 | 19.5 | -96.55 | -35.37 | -96.55 | 3607 |
| 89 | CCI reversion | reversion | 53.31 | -46.69 | 648 | 16.5 | -98.41 | -40.50 | -98.45 | 4680 |
| 90 | OBV trend | momentum | 52.88 | -47.12 | 698 | 15.2 | -96.46 | -40.98 | -96.46 | 3617 |
| 91 | Candlestick reversal | reversion | 51.68 | -48.32 | 743 | 14.7 | -99.28 | -40.73 | -99.28 | 5588 |
| 92 | VWAP momentum | momentum | 51.39 | -48.61 | 674 | 8.6 | -98.72 | -32.60 | -98.72 | 5400 |
| 93 | Parabolic SAR | trend | 50.90 | -49.10 | 638 | 14.9 | -97.41 | -43.14 | -97.41 | 3677 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.26 | -99.73 | 6137 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.49 | -44.75 | -99.50 | 6077 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.78 | -99.90 | 8250 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T15:30 | Agent (rotation) | buy | LABU | 8.17 | — | following Volume breakout, EMA 20/50 cross |
| 2026-10-06T15:30 | Consensus | buy | TQQQ | 4.47 | — | entry |
| 2026-10-06T15:30 | Consensus | sell | ETHU | 3.85 | -0.03 | target is flat |
| 2026-10-06T15:30 | Consensus | sell | DOGE-USD | 3.84 | -0.04 | target is flat |
| 2026-10-06T15:30 | Williams %R · 1h | buy | LABU | 24.76 | — | entry signal |
| 2026-10-06T15:30 | Williams %R · 1h | sell | BITX | 24.80 | 0.40 | exit signal |
| 2026-10-06T15:30 | Stochastic reversion · 1h | sell | BITX | 25.25 | 0.23 | exit signal |
| 2026-10-06T15:30 | Z-score reversion · 1h | buy | LABU | 24.99 | — | entry signal |
| 2026-10-06T15:30 | Bollinger reversion · 1h | buy | LABU | 24.99 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | UPRO | 1.43 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | TQQQ | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | TNA | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | SPY | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | SOXL | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | QQQ | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | PLTR | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | IWM | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | ETHU | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | BITX | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | AMZN | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | buy | AAPL | 4.59 | — | entry signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | XRP-USD | 5.58 | -0.02 | rebalance down |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | SOL-USD | 5.59 | -0.02 | rebalance down |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | MSTR | 10.19 | -0.01 | exit signal |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | MSFT | 5.57 | -0.02 | rebalance down |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | ETH-USD | 5.58 | -0.03 | rebalance down |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | DOGE-USD | 5.60 | -0.03 | rebalance down |
| 2026-10-06T15:30 | VWAP momentum · 1h | sell | BTC-USD | 5.60 | -0.03 | rebalance down |
| 2026-10-06T15:30 | Z-score reversion | sell | TNA | 18.23 | 0.10 | exit signal |
| 2026-10-06T15:30 | Z-score reversion | sell | IWM | 18.19 | 0.02 | exit signal |
| 2026-10-06T15:30 | Connors RSI(2) | buy | TECL | 5.46 | — | entry signal |
| 2026-10-06T15:30 | Connors RSI(2) | buy | SOXL | 5.48 | — | entry signal |
| 2026-10-06T15:30 | Connors RSI(2) | buy | SOL-USD | 5.48 | — | entry signal |
| 2026-10-06T15:30 | Connors RSI(2) | buy | DOGE-USD | 5.48 | — | entry signal |
| 2026-10-06T15:30 | Connors RSI(2) | sell | NVDA | 3.67 | -0.00 | rebalance down |
| 2026-10-06T15:30 | Connors RSI(2) | sell | MSTR | 3.65 | -0.01 | rebalance down |
| 2026-10-06T15:30 | Connors RSI(2) | sell | MSFT | 3.68 | -0.01 | rebalance down |
| 2026-10-06T15:30 | Connors RSI(2) | sell | COIN | 3.63 | -0.02 | rebalance down |
| 2026-10-06T15:30 | Connors RSI(2) | sell | BTC-USD | 3.63 | -0.02 | rebalance down |
| 2026-10-06T15:30 | Connors RSI(2) | sell | BITX | 3.66 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 15:31:05.000166+00:00 -> 2026-10-06 15:41:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
