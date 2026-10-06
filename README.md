# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T18:30:05.000121+00:00 · 13743 ticks

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

Today: 29977 decisions in 2621 calls, $0.3732 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T18:30 | 1 / 21 / 7 | AMZN 15% |  |
| Breezy | 2026-10-06T18:30 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-06T18:30 | 1 / 27 / 1 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.49 | 6.49 | 0 | — | -0.49 | 0.04 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.14 | -2.89 | -13.90 | 113 |
| 3 | Hold BTC | benchmark | 102.16 | 2.16 | 0 | — | 31.83 | 3.85 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 102.09 | 2.09 | 0 | — | 0.35 | 0.25 | -5.09 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 101.92 | 1.92 | 17 | 0.0 | 13.11 | 1.77 | -16.96 | 110 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.85 | 1.85 | 0 | — | 3.65 | 1.73 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 8 | Daily: Bullish score | daily | 101.64 | 1.64 | 3 | 0.0 | 5.86 | 0.97 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.12 | 1.12 | 0 | — | 1.02 | 0.66 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.48 | 0.48 | 67 | 38.8 | -19.70 | -4.33 | -21.84 | 490 |
| 13 | Stochastic reversion · 1h | reversion | 100.30 | 0.30 | 56 | 64.3 | -7.67 | -1.57 | -10.87 | 326 |
| 14 | EMA 20/50 cross · 1h | trend | 100.17 | 0.17 | 28 | 7.1 | 13.86 | 1.72 | -15.31 | 142 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 100.13 | 0.13 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.09 | 0.09 | 0 | — | -2.08 | -0.78 | -7.65 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 19 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 20 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 21 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.90 | -0.10 | 0 | — | 19.14 | 2.91 | -6.29 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.55 | -0.46 | 73 | 45.2 | -11.20 | -4.08 | -15.07 | 218 |
| 24 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 3.59 | 1.04 | -6.57 | 122 |
| 25 | Trend pullback · 1h | trend | 99.22 | -0.78 | 65 | 24.6 | -20.58 | -5.98 | -24.51 | 167 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | 0.03 | 0.07 | -4.23 | 104 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 28 | Daily: Momentum burst | daily | 98.29 | -1.71 | 3 | 0.0 | 1.32 | 0.38 | -16.91 | 41 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.30 | -4.88 | -10.11 | 232 |
| 30 | Copy: Insider buying | copy | 98.26 | -1.74 | 11 | 54.5 | -15.33 | -2.82 | -21.08 | 73 |
| 31 | Bollinger reversion · 1h | reversion | 98.15 | -1.84 | 49 | 46.9 | -15.54 | -3.97 | -16.99 | 302 |
| 32 | Z-score reversion · 1h | reversion | 98.12 | -1.88 | 23 | 52.2 | 3.66 | 0.89 | -8.60 | 150 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.31 | -2.69 | 0 | — | 0.12 | 0.13 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.17 | -2.83 | 63 | 28.6 | -0.56 | -0.03 | -11.86 | 256 |
| 35 | ADX DI cross · 1h | trend | 97.17 | -2.83 | 43 | 11.6 | -2.17 | -0.23 | -13.84 | 255 |
| 36 | Supertrend · 1h | trend | 97.05 | -2.95 | 32 | 9.4 | 3.25 | 0.62 | -16.43 | 213 |
| 37 | Agent (ML meta-label) | meta | 96.92 | -3.08 | 264 | 14.8 | -1.76 | -0.23 | -13.39 | 378 |
| 38 | Williams %R · 1h | reversion | 96.78 | -3.22 | 85 | 52.9 | -20.05 | -3.78 | -20.77 | 496 |
| 39 | Parabolic SAR · 1h | trend | 96.64 | -3.36 | 65 | 15.4 | -3.00 | -0.21 | -19.45 | 301 |
| 40 | CCI reversion · 1h | reversion | 96.43 | -3.57 | 71 | 49.3 | -0.45 | 0.09 | -12.41 | 409 |
| 41 | MACD cross · 1h | trend | 95.86 | -4.14 | 88 | 19.3 | -11.98 | -1.92 | -17.27 | 473 |
| 42 | RSI momentum · 1h | momentum | 95.69 | -4.31 | 45 | 2.2 | 0.71 | 0.29 | -16.65 | 229 |
| 43 | Squeeze breakout · 1h | breakout | 95.40 | -4.59 | 30 | 20.0 | 15.66 | 2.63 | -8.06 | 106 |
| 44 | Ichimoku · 1h | trend | 95.20 | -4.80 | 33 | 15.2 | 8.76 | 1.21 | -15.84 | 124 |
| 45 | MFI reversion · 1h | reversion | 95.11 | -4.89 | 75 | 28.0 | -10.96 | -1.91 | -16.99 | 121 |
| 46 | Triple EMA stack · 1h | trend | 94.95 | -5.05 | 56 | 10.7 | -9.84 | -1.02 | -24.06 | 256 |
| 47 | Max aggression: 1-day momentum | meta | 94.79 | -5.21 | 7 | 42.9 | -23.63 | -1.22 | -37.31 | 42 |
| 48 | Bollinger breakout · 1h | breakout | 94.68 | -5.32 | 50 | 24.0 | 7.23 | 1.09 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.32 | -5.67 | 46 | 6.5 | 6.82 | 1.78 | -6.47 | 201 |
| 50 | Opening range 30m | breakout | 94.04 | -5.96 | 98 | 21.4 | -17.50 | -5.44 | -17.82 | 573 |
| 51 | Volume breakout · 1h | breakout | 93.82 | -6.18 | 36 | 11.1 | 6.73 | 1.09 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.95 | -7.05 | 80 | 11.2 | -2.23 | -0.10 | -18.47 | 346 |
| 53 | Max aggression: 5-day momentum | meta | 92.65 | -7.35 | 5 | 40.0 | -18.70 | -1.58 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.51 | -7.49 | 113 | 19.5 | -18.50 | -5.49 | -19.25 | 692 |
| 55 | Donchian 20/10 · 1h | breakout | 91.53 | -8.46 | 39 | 15.4 | 3.02 | 0.58 | -16.18 | 222 |
| 56 | MACD zero-line · 1h | trend | 91.43 | -8.57 | 48 | 16.7 | -3.12 | -0.22 | -18.32 | 248 |
| 57 | VWAP momentum · 1h | momentum | 90.95 | -9.05 | 228 | 22.8 | -37.44 | -5.77 | -37.52 | 1274 |
| 58 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.32 | -24.94 | -49.52 | 590 |
| 59 | OBV trend · 1h | momentum | 90.81 | -9.19 | 106 | 12.3 | -12.61 | -1.39 | -26.73 | 337 |
| 60 | Heikin-Ashi · 1h | trend | 90.14 | -9.86 | 116 | 25.0 | -30.91 | -5.31 | -34.24 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.92 | -10.08 | 30 | 6.7 | -9.98 | -1.15 | -23.31 | 232 |
| 62 | ROC + volume · 1h | momentum | 87.50 | -12.50 | 107 | 15.9 | -9.07 | -1.08 | -23.04 | 413 |
| 63 | RSI(14) reversion | reversion | 85.95 | -14.05 | 218 | 32.1 | -71.02 | -19.80 | -71.48 | 1424 |
| 64 | VWAP reversion | reversion | 77.76 | -22.25 | 262 | 29.0 | -68.88 | -16.13 | -69.28 | 1375 |
| 65 | Squeeze breakout | breakout | 77.66 | -22.34 | 247 | 15.8 | -62.28 | -19.03 | -62.31 | 1226 |
| 66 | ROC + volume | momentum | 76.83 | -23.17 | 318 | 20.8 | -73.94 | -17.83 | -73.94 | 1651 |
| 67 | Donchian 55/20 | breakout | 76.06 | -23.94 | 258 | 17.4 | -68.96 | -15.35 | -68.96 | 1305 |
| 68 | EMA 20/50 cross | trend | 74.70 | -25.30 | 262 | 18.7 | -78.49 | -16.21 | -78.50 | 1479 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.25 | -19.60 | -65.25 | 935 |
| 70 | Z-score reversion | reversion | 71.86 | -28.14 | 349 | 28.1 | -85.03 | -25.35 | -85.06 | 2050 |
| 71 | MFI reversion | reversion | 70.18 | -29.82 | 344 | 20.9 | -86.91 | -30.57 | -86.93 | 2112 |
| 72 | Supertrend | trend | 69.79 | -30.21 | 348 | 20.4 | -87.05 | -22.50 | -87.06 | 1939 |
| 73 | Keltner breakout | breakout | 68.06 | -31.94 | 348 | 13.2 | -85.57 | -30.82 | -85.57 | 1893 |
| 74 | AI bee: Bizzy | ai | 67.61 | -32.40 | 602 | 9.0 | — | — | — | — |
| 75 | Ichimoku | trend | 66.94 | -33.06 | 316 | 8.9 | -82.22 | -24.90 | -82.23 | 1771 |
| 76 | AI bee: Boozy | ai | 66.15 | -33.85 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.62 | -35.38 | 398 | 9.3 | -89.70 | -37.38 | -89.72 | 2112 |
| 78 | MACD zero-line | trend | 63.44 | -36.56 | 445 | 15.7 | -91.56 | -31.20 | -91.56 | 2369 |
| 79 | Donchian 20/10 | breakout | 62.75 | -37.25 | 482 | 18.5 | -91.26 | -28.04 | -91.26 | 2676 |
| 80 | RSI momentum | momentum | 61.92 | -38.08 | 450 | 16.7 | -90.61 | -27.01 | -90.61 | 2379 |
| 81 | Triple EMA stack | trend | 60.38 | -39.62 | 497 | 15.5 | -93.34 | -32.65 | -93.34 | 2632 |
| 82 | Trend pullback | trend | 60.28 | -39.72 | 478 | 15.5 | -91.47 | -30.99 | -91.47 | 2350 |
| 83 | Bollinger breakout | breakout | 59.61 | -40.39 | 493 | 14.2 | -94.07 | -36.23 | -94.07 | 2827 |
| 84 | Stochastic reversion | reversion | 58.41 | -41.59 | 700 | 23.3 | -95.51 | -37.80 | -95.56 | 4030 |
| 85 | Bollinger reversion | reversion | 58.17 | -41.83 | 650 | 18.2 | -95.58 | -36.78 | -95.62 | 3685 |
| 86 | Consensus | meta | 57.48 | -42.52 | 471 | 10.0 | -94.75 | -27.36 | -94.75 | 2723 |
| 87 | EMA 9/21 cross | trend | 55.79 | -44.21 | 611 | 16.4 | -97.46 | -35.82 | -97.46 | 3559 |
| 88 | Connors RSI(2) | reversion | 54.02 | -45.98 | 662 | 20.2 | -96.56 | -35.36 | -96.56 | 3645 |
| 89 | OBV trend | momentum | 52.38 | -47.62 | 721 | 15.1 | -96.46 | -40.14 | -96.46 | 3606 |
| 90 | CCI reversion | reversion | 52.31 | -47.69 | 675 | 17.3 | -98.44 | -40.95 | -98.44 | 4699 |
| 91 | Candlestick reversal | reversion | 51.13 | -48.87 | 774 | 14.9 | -99.29 | -40.81 | -99.29 | 5634 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -32.34 | -98.72 | 5366 |
| 93 | Parabolic SAR | trend | 50.35 | -49.66 | 660 | 14.7 | -97.38 | -42.37 | -97.38 | 3680 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.82 | -99.73 | 6124 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.92 | -99.50 | 6089 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.00 | -99.90 | 8245 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T18:30 | Agent (ML meta-label) | buy | LABU | 2.11 | — | following EMA 20/50 cross |
| 2026-10-06T18:30 | Consensus | buy | TQQQ | 5.23 | — | entry |
| 2026-10-06T18:30 | MFI reversion · 1h | sell | SPY | 23.76 | -0.03 | exit signal |
| 2026-10-06T18:30 | Williams %R · 1h | buy | LABU | 23.53 | — | entry signal |
| 2026-10-06T18:30 | Stochastic reversion · 1h | buy | LABU | 25.08 | — | entry signal |
| 2026-10-06T18:30 | Bollinger reversion · 1h | buy | LABU | 24.54 | — | entry signal |
| 2026-10-06T18:30 | Connors RSI(2) · 1h | sell | AAPL | 24.97 | 0.06 | exit signal |
| 2026-10-06T18:30 | ROC + volume · 1h | sell | IWM | 4.83 | -0.03 | exit signal |
| 2026-10-06T18:30 | VWAP momentum · 1h | buy | UPRO | 12.98 | — | entry signal |
| 2026-10-06T18:30 | VWAP momentum · 1h | buy | TQQQ | 13.00 | — | entry signal |
| 2026-10-06T18:30 | VWAP momentum · 1h | buy | META | 13.00 | — | entry signal |
| 2026-10-06T18:30 | VWAP momentum · 1h | buy | GOOGL | 13.00 | — | entry signal |
| 2026-10-06T18:30 | VWAP momentum · 1h | sell | PLTR | 9.72 | -0.01 | rebalance down |
| 2026-10-06T18:30 | VWAP momentum · 1h | sell | AMZN | 9.85 | 0.03 | rebalance down |
| 2026-10-06T18:30 | VWAP momentum · 1h | sell | AMD | 9.73 | 0.06 | rebalance down |
| 2026-10-06T18:30 | Heikin-Ashi · 1h | buy | TQQQ | 4.69 | — | rebalance up |
| 2026-10-06T18:30 | Heikin-Ashi · 1h | buy | AMZN | 5.33 | — | rebalance up |
| 2026-10-06T18:30 | Heikin-Ashi · 1h | buy | AMD | 5.37 | — | rebalance up |
| 2026-10-06T18:30 | Heikin-Ashi · 1h | sell | MSFT | 10.11 | 0.03 | exit signal |
| 2026-10-06T18:30 | MACD zero-line · 1h | sell | ETHU | 9.08 | -0.14 | exit signal |
| 2026-10-06T18:30 | MACD cross · 1h | sell | ETHU | 5.96 | -0.05 | exit signal |
| 2026-10-06T18:30 | MACD cross · 1h | sell | BITX | 6.29 | -0.14 | exit signal |
| 2026-10-06T18:30 | MFI reversion | buy | TSLA | 1.45 | — | entry |
| 2026-10-06T18:30 | MFI reversion | buy | NVDA | 6.38 | — | entry |
| 2026-10-06T18:30 | MFI reversion | sell | XRP-USD | 7.83 | -0.03 | exit signal |
| 2026-10-06T18:30 | VWAP reversion | buy | COIN | 9.22 | — | entry signal |
| 2026-10-06T18:30 | Z-score reversion | buy | TSLA | 3.46 | — | entry signal |
| 2026-10-06T18:30 | Bollinger reversion | buy | COIN | 14.55 | — | entry signal |
| 2026-10-06T18:30 | Connors RSI(2) | buy | SPY | 6.75 | — | entry signal |
| 2026-10-06T18:30 | Connors RSI(2) | sell | BITX | 7.72 | 0.00 | target is flat |
| 2026-10-06T18:30 | Three white soldiers | sell | META | 22.73 | -0.04 | exit signal |
| 2026-10-06T18:30 | Candlestick reversal | buy | BITX | 3.94 | — | entry signal |
| 2026-10-06T18:30 | Donchian 20/10 | buy | AAPL | 5.71 | — | entry signal |
| 2026-10-06T18:30 | Donchian 20/10 | sell | SOXL | 6.25 | -0.05 | exit signal |
| 2026-10-06T18:30 | Parabolic SAR | buy | UPRO | 2.61 | — | rebalance up |
| 2026-10-06T18:30 | Parabolic SAR | buy | TSLA | 2.62 | — | rebalance up |
| 2026-10-06T18:30 | Parabolic SAR | buy | SPY | 2.61 | — | rebalance up |
| 2026-10-06T18:30 | Parabolic SAR | buy | PLTR | 2.62 | — | rebalance up |
| 2026-10-06T18:30 | Parabolic SAR | buy | META | 2.61 | — | rebalance up |
| 2026-10-06T18:30 | Parabolic SAR | buy | GOOGL | 2.60 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 18:30:05.000121+00:00 -> 2026-10-06 18:40:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
