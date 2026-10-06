# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T14:30:05.000149+00:00 · 13557 ticks

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

Today: 13258 decisions in 2063 calls, $0.1775 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T14:30 | 1 / 13 / 16 | NANC 20% |  |
| Breezy | 2026-10-06T14:30 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-06T14:30 | 0 / 28 / 2 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |
| VWAP reversion | TECL | 1.77 | +2.87% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.29 | 6.29 | 0 | — | -2.14 | -0.27 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.17 | -2.90 | -13.93 | 113 |
| 3 | Hold BTC | benchmark | 102.61 | 2.61 | 0 | — | 32.89 | 3.96 | -8.68 | 1 |
| 4 | Daily: Bullish score | daily | 102.27 | 2.27 | 3 | 0.0 | 5.09 | 0.87 | -12.76 | 10 |
| 5 | Timing: Nasdaq FTD · QQQ | daily | 102.09 | 2.09 | 0 | — | -0.21 | -0.07 | -5.09 | 1 |
| 6 | Copy: Congress Democrats (NANC) | copy | 102.03 | 2.03 | 0 | — | 3.20 | 1.51 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.97 | 1.97 | 17 | 0.0 | 9.34 | 1.32 | -16.96 | 111 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.08 | 1.08 | 0 | — | 0.85 | 0.56 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Copy: Cathie Wood (ARKK) | copy | 100.96 | 0.96 | 0 | — | 19.75 | 3.01 | -6.29 | 1 |
| 13 | Stochastic reversion · 1h | reversion | 100.50 | 0.50 | 55 | 65.5 | -7.86 | -1.61 | -11.15 | 326 |
| 14 | Copy: Warren Buffett (BRK-B) | copy | 100.50 | 0.50 | 0 | — | -1.13 | -0.39 | -7.65 | 1 |
| 15 | EMA 20/50 cross · 1h | trend | 100.42 | 0.42 | 28 | 7.1 | 14.83 | 1.82 | -15.31 | 141 |
| 16 | Candlestick reversal · 1h | reversion | 100.34 | 0.34 | 62 | 35.5 | -20.65 | -4.56 | -22.41 | 500 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 100.21 | 0.21 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.81 | 1.84 | -1.59 | 85 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 20 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 21 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 22 | Z-score reversion · 1h | reversion | 99.98 | -0.02 | 22 | 54.5 | 7.49 | 1.66 | -8.60 | 150 |
| 23 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -5.19 | -1.82 | -9.74 | 23 |
| 24 | Bollinger reversion · 1h | reversion | 99.94 | -0.06 | 48 | 47.9 | -14.42 | -3.74 | -17.04 | 302 |
| 25 | Connors RSI(2) · 1h | reversion | 99.63 | -0.37 | 72 | 44.4 | -12.99 | -4.49 | -16.84 | 221 |
| 26 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 0.26 | 0.17 | -7.81 | 132 |
| 27 | Trend pullback · 1h | trend | 99.53 | -0.47 | 62 | 25.8 | -18.84 | -5.39 | -23.07 | 168 |
| 28 | Daily: Momentum burst | daily | 98.71 | -1.29 | 3 | 0.0 | -0.07 | 0.17 | -16.91 | 41 |
| 29 | Williams %R · 1h | reversion | 98.69 | -1.31 | 82 | 53.7 | -18.56 | -3.45 | -20.90 | 498 |
| 30 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -1.80 | -0.96 | -4.66 | 105 |
| 31 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 32 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -9.76 | -5.93 | -11.17 | 231 |
| 33 | Agent (rotation) | meta | 98.04 | -1.96 | 61 | 27.9 | 1.03 | 0.37 | -10.09 | 266 |
| 34 | ADX DI cross · 1h | trend | 97.60 | -2.40 | 41 | 12.2 | -3.00 | -0.36 | -13.84 | 260 |
| 35 | CCI reversion · 1h | reversion | 97.48 | -2.52 | 70 | 48.6 | 0.79 | 0.29 | -12.41 | 407 |
| 36 | Agent (ML meta-label) | meta | 97.46 | -2.54 | 247 | 15.0 | -0.60 | 0.05 | -13.99 | 373 |
| 37 | Daily: SMA 20/50 cross · AAPL | daily | 97.46 | -2.54 | 0 | — | 0.66 | 0.33 | -5.18 | 1 |
| 38 | Supertrend · 1h | trend | 97.38 | -2.62 | 32 | 9.4 | 3.54 | 0.66 | -16.43 | 207 |
| 39 | Copy: Insider buying | copy | 97.34 | -2.66 | 9 | 55.6 | -16.09 | -2.98 | -21.08 | 73 |
| 40 | Parabolic SAR · 1h | trend | 96.97 | -3.03 | 62 | 16.1 | -2.49 | -0.14 | -19.45 | 299 |
| 41 | MACD cross · 1h | trend | 96.36 | -3.63 | 82 | 19.5 | -7.71 | -1.09 | -17.27 | 481 |
| 42 | Squeeze breakout · 1h | breakout | 96.13 | -3.87 | 27 | 22.2 | 16.22 | 2.69 | -8.06 | 106 |
| 43 | RSI momentum · 1h | momentum | 95.97 | -4.03 | 45 | 2.2 | 2.36 | 0.50 | -16.65 | 231 |
| 44 | Ichimoku · 1h | trend | 95.69 | -4.31 | 31 | 16.1 | 9.39 | 1.28 | -15.84 | 123 |
| 45 | Triple EMA stack · 1h | trend | 95.17 | -4.83 | 56 | 10.7 | -7.64 | -0.74 | -23.99 | 253 |
| 46 | Bollinger breakout · 1h | breakout | 95.16 | -4.84 | 46 | 26.1 | 6.44 | 1.00 | -12.06 | 294 |
| 47 | MFI reversion · 1h | reversion | 95.15 | -4.85 | 73 | 27.4 | -9.73 | -1.68 | -16.99 | 121 |
| 48 | Max aggression: 1-day momentum | meta | 95.03 | -4.97 | 7 | 42.9 | -23.50 | -1.21 | -37.31 | 42 |
| 49 | Gap and go | momentum | 94.53 | -5.47 | 42 | 7.1 | 7.00 | 1.83 | -6.28 | 198 |
| 50 | Opening range 30m | breakout | 94.23 | -5.77 | 92 | 22.8 | -17.01 | -5.31 | -17.22 | 561 |
| 51 | Volume breakout · 1h | breakout | 94.07 | -5.93 | 35 | 11.4 | 6.42 | 1.05 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 93.18 | -6.82 | 78 | 11.5 | -1.81 | -0.05 | -18.47 | 345 |
| 53 | Max aggression: 5-day momentum | meta | 92.89 | -7.11 | 5 | 40.0 | -18.56 | -1.56 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.79 | -7.21 | 105 | 21.0 | -18.13 | -5.38 | -18.88 | 683 |
| 55 | Donchian 20/10 · 1h | breakout | 91.79 | -8.21 | 36 | 16.7 | 1.52 | 0.40 | -16.18 | 221 |
| 56 | MACD zero-line · 1h | trend | 91.68 | -8.32 | 43 | 18.6 | 1.14 | 0.35 | -18.32 | 248 |
| 57 | VWAP momentum · 1h | momentum | 91.61 | -8.39 | 209 | 24.4 | -37.49 | -5.76 | -37.85 | 1279 |
| 58 | OBV trend · 1h | momentum | 91.01 | -8.99 | 103 | 11.7 | -12.12 | -1.33 | -26.62 | 338 |
| 59 | Three white soldiers | momentum | 90.67 | -9.33 | 96 | 19.8 | -49.55 | -25.43 | -49.59 | 586 |
| 60 | Heikin-Ashi · 1h | trend | 90.51 | -9.49 | 108 | 24.1 | -31.26 | -5.39 | -34.14 | 701 |
| 61 | Keltner breakout · 1h | breakout | 89.89 | -10.11 | 30 | 6.7 | -10.56 | -1.22 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.83 | -12.17 | 101 | 15.8 | -9.36 | -1.12 | -23.04 | 421 |
| 63 | RSI(14) reversion | reversion | 84.95 | -15.05 | 215 | 31.6 | -70.92 | -19.78 | -71.22 | 1424 |
| 64 | Squeeze breakout | breakout | 77.80 | -22.20 | 243 | 15.6 | -62.92 | -19.41 | -62.92 | 1234 |
| 65 | VWAP reversion | reversion | 77.06 | -22.94 | 256 | 28.1 | -69.32 | -16.40 | -69.35 | 1374 |
| 66 | ROC + volume | momentum | 76.95 | -23.05 | 307 | 20.2 | -73.84 | -17.85 | -73.90 | 1665 |
| 67 | Donchian 55/20 | breakout | 76.49 | -23.51 | 244 | 18.0 | -69.14 | -15.50 | -69.14 | 1303 |
| 68 | EMA 20/50 cross | trend | 75.23 | -24.77 | 257 | 19.1 | -78.40 | -16.17 | -78.46 | 1484 |
| 69 | Volume breakout | breakout | 73.62 | -26.38 | 210 | 12.4 | -65.28 | -19.74 | -65.46 | 932 |
| 70 | Z-score reversion | reversion | 72.33 | -27.67 | 340 | 27.6 | -84.97 | -25.45 | -85.04 | 2061 |
| 71 | Supertrend | trend | 70.70 | -29.30 | 338 | 21.0 | -86.99 | -22.56 | -86.99 | 1929 |
| 72 | MFI reversion | reversion | 70.64 | -29.36 | 329 | 21.0 | -86.90 | -30.45 | -86.94 | 2100 |
| 73 | Keltner breakout | breakout | 68.33 | -31.67 | 335 | 13.4 | -85.47 | -30.53 | -85.55 | 1889 |
| 74 | AI bee: Bizzy | ai | 67.78 | -32.22 | 591 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 67.26 | -32.74 | 300 | 9.0 | -82.55 | -25.13 | -82.55 | 1774 |
| 76 | AI bee: Boozy | ai | 66.82 | -33.18 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.22 | -34.77 | 375 | 9.1 | -89.78 | -38.36 | -89.78 | 2107 |
| 78 | MACD zero-line | trend | 64.18 | -35.82 | 433 | 15.7 | -91.54 | -31.36 | -91.54 | 2362 |
| 79 | Donchian 20/10 | breakout | 63.28 | -36.72 | 464 | 18.5 | -91.26 | -28.22 | -91.28 | 2676 |
| 80 | RSI momentum | momentum | 62.54 | -37.46 | 435 | 16.6 | -90.69 | -27.45 | -90.69 | 2385 |
| 81 | Trend pullback | trend | 61.07 | -38.93 | 452 | 15.7 | -91.48 | -31.33 | -91.48 | 2353 |
| 82 | Triple EMA stack | trend | 60.89 | -39.11 | 484 | 15.7 | -93.43 | -33.10 | -93.43 | 2638 |
| 83 | Bollinger breakout | breakout | 60.13 | -39.87 | 477 | 14.0 | -94.10 | -36.65 | -94.10 | 2842 |
| 84 | Consensus | meta | 58.13 | -41.87 | 443 | 10.2 | -94.58 | -27.34 | -94.58 | 2688 |
| 85 | Stochastic reversion | reversion | 58.03 | -41.97 | 666 | 22.5 | -95.57 | -38.17 | -95.57 | 4025 |
| 86 | Bollinger reversion | reversion | 57.81 | -42.19 | 621 | 17.2 | -95.60 | -36.92 | -95.63 | 3665 |
| 87 | EMA 9/21 cross | trend | 56.44 | -43.56 | 592 | 16.7 | -97.44 | -36.05 | -97.44 | 3555 |
| 88 | Connors RSI(2) | reversion | 54.76 | -45.24 | 602 | 18.8 | -96.56 | -35.53 | -96.56 | 3610 |
| 89 | OBV trend | momentum | 52.94 | -47.06 | 693 | 15.2 | -96.49 | -41.25 | -96.49 | 3627 |
| 90 | CCI reversion | reversion | 52.75 | -47.25 | 643 | 16.3 | -98.44 | -40.99 | -98.45 | 4682 |
| 91 | VWAP momentum | momentum | 51.37 | -48.63 | 667 | 8.5 | -98.71 | -32.58 | -98.71 | 5373 |
| 92 | Candlestick reversal | reversion | 51.35 | -48.65 | 734 | 14.0 | -99.28 | -40.76 | -99.29 | 5601 |
| 93 | Parabolic SAR | trend | 51.06 | -48.94 | 636 | 14.9 | -97.42 | -43.30 | -97.42 | 3672 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.47 | -99.73 | 6141 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -45.01 | -99.50 | 6084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -54.19 | -99.90 | 8259 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T14:30 | Agent (rotation) | sell | COIN | 6.32 | -0.02 | rebalance down |
| 2026-10-06T14:30 | Consensus | buy | TECL | 7.25 | — | rebalance up |
| 2026-10-06T14:30 | Consensus | buy | MSFT | 8.06 | — | rebalance up |
| 2026-10-06T14:30 | Consensus | buy | AMZN | 7.27 | — | rebalance up |
| 2026-10-06T14:30 | Consensus | buy | AMD | 7.23 | — | rebalance up |
| 2026-10-06T14:30 | Consensus | sell | XRP-USD | 8.72 | -0.08 | target is flat |
| 2026-10-06T14:30 | Consensus | sell | UPRO | 6.68 | -0.04 | target is flat |
| 2026-10-06T14:30 | Consensus | sell | TQQQ | 7.26 | -0.05 | target is flat |
| 2026-10-06T14:30 | Consensus | sell | SPY | 6.48 | -0.01 | target is flat |
| 2026-10-06T14:30 | Williams %R · 1h | buy | PLTR | 8.09 | — | rebalance up |
| 2026-10-06T14:30 | Williams %R · 1h | buy | ETHU | 8.26 | — | rebalance up |
| 2026-10-06T14:30 | Williams %R · 1h | buy | ETH-USD | 8.22 | — | rebalance up |
| 2026-10-06T14:30 | Williams %R · 1h | buy | BITX | 8.26 | — | rebalance up |
| 2026-10-06T14:30 | Williams %R · 1h | sell | MSTR | 16.40 | 0.41 | exit signal |
| 2026-10-06T14:30 | Williams %R · 1h | sell | COIN | 16.44 | -0.01 | exit signal |
| 2026-10-06T14:30 | Stochastic reversion · 1h | buy | SQQQ | 8.31 | — | rebalance up |
| 2026-10-06T14:30 | Stochastic reversion · 1h | buy | PLTR | 8.26 | — | rebalance up |
| 2026-10-06T14:30 | Stochastic reversion · 1h | buy | ETHU | 8.42 | — | rebalance up |
| 2026-10-06T14:30 | Stochastic reversion · 1h | buy | BITX | 8.42 | — | rebalance up |
| 2026-10-06T14:30 | Stochastic reversion · 1h | sell | MSTR | 16.68 | 0.33 | exit signal |
| 2026-10-06T14:30 | Stochastic reversion · 1h | sell | COIN | 16.73 | 0.28 | exit signal |
| 2026-10-06T14:30 | Z-score reversion · 1h | sell | COIN | 25.92 | 1.05 | exit signal |
| 2026-10-06T14:30 | Volume breakout · 1h | buy | MSFT | 11.76 | — | entry signal |
| 2026-10-06T14:30 | Volume breakout · 1h | sell | TNA | 9.27 | -0.13 | exit signal |
| 2026-10-06T14:30 | Volume breakout · 1h | sell | IWM | 9.33 | -0.06 | exit signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | META | 2.86 | — | entry signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | GOOGL | 4.39 | — | entry signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | ETHU | 4.39 | — | entry signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | BITX | 4.39 | — | entry signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | AMZN | 4.39 | — | entry signal |
| 2026-10-06T14:30 | ROC + volume · 1h | buy | AMD | 4.39 | — | entry signal |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | XRP-USD | 10.20 | — | entry |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | SOL-USD | 10.20 | — | entry |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | MSTR | 10.20 | — | entry |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | MSFT | 10.20 | — | entry signal |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | ETH-USD | 8.71 | — | rebalance up |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | DOGE-USD | 5.61 | — | rebalance up |
| 2026-10-06T14:30 | VWAP momentum · 1h | buy | BTC-USD | 5.61 | — | rebalance up |
| 2026-10-06T14:30 | VWAP momentum · 1h | sell | UPRO | 6.10 | 0.10 | exit signal |
| 2026-10-06T14:30 | VWAP momentum · 1h | sell | TSLA | 6.15 | 0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 14:30:05.000149+00:00 -> 2026-10-06 14:40:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
