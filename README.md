# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T18:00:05.000146+00:00 · 13714 ticks

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

Today: 27382 decisions in 2534 calls, $0.3429 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T18:00 | 6 / 17 / 7 | cash |  |
| Breezy | 2026-10-06T18:00 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-06T18:00 | 4 / 23 / 3 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.53 | 6.53 | 0 | — | -0.30 | 0.08 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.14 | -2.89 | -13.90 | 113 |
| 3 | Hold BTC | benchmark | 102.22 | 2.22 | 0 | — | 31.80 | 3.85 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 102.14 | 2.14 | 0 | — | 0.41 | 0.28 | -5.09 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 102.02 | 2.02 | 17 | 0.0 | 13.16 | 1.78 | -16.96 | 110 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.90 | 1.90 | 0 | — | 3.65 | 1.73 | -3.62 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 8 | Daily: Bullish score | daily | 101.73 | 1.73 | 3 | 0.0 | 5.84 | 0.97 | -12.76 | 10 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.17 | 1.17 | 0 | — | 1.01 | 0.66 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.49 | 0.49 | 67 | 38.8 | -19.72 | -4.31 | -21.86 | 492 |
| 13 | Stochastic reversion · 1h | reversion | 100.35 | 0.35 | 56 | 64.3 | -7.20 | -1.46 | -10.46 | 325 |
| 14 | EMA 20/50 cross · 1h | trend | 100.22 | 0.22 | 28 | 7.1 | 13.69 | 1.70 | -15.31 | 143 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 100.18 | 0.18 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.86 | 1.86 | -1.59 | 85 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 18 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 19 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 20 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 21 | Copy: Warren Buffett (BRK-B) | copy | 99.94 | -0.06 | 0 | — | -2.34 | -0.90 | -7.65 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 99.79 | -0.21 | 0 | — | 19.08 | 2.90 | -6.29 | 1 |
| 23 | Connors RSI(2) · 1h | reversion | 99.59 | -0.41 | 72 | 44.4 | -11.17 | -4.07 | -15.07 | 218 |
| 24 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 2.41 | 0.73 | -6.57 | 126 |
| 25 | Trend pullback · 1h | trend | 99.22 | -0.78 | 65 | 24.6 | -20.62 | -6.00 | -24.51 | 167 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.75 | -0.37 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.41 | -1.59 | 3 | 0.0 | 1.31 | 0.38 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.42 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.45 | -5.00 | -10.26 | 234 |
| 30 | Bollinger reversion · 1h | reversion | 98.17 | -1.83 | 49 | 46.9 | -15.52 | -3.97 | -16.98 | 303 |
| 31 | Z-score reversion · 1h | reversion | 98.10 | -1.90 | 23 | 52.2 | 3.61 | 0.88 | -8.60 | 150 |
| 32 | Copy: Insider buying | copy | 97.68 | -2.32 | 10 | 50.0 | -15.66 | -2.89 | -21.08 | 73 |
| 33 | ADX DI cross · 1h | trend | 97.25 | -2.75 | 43 | 11.6 | -1.94 | -0.18 | -13.84 | 252 |
| 34 | Agent (rotation) | meta | 97.23 | -2.77 | 63 | 28.6 | -0.51 | -0.02 | -11.86 | 256 |
| 35 | Daily: SMA 20/50 cross · AAPL | daily | 97.18 | -2.82 | 0 | — | -0.31 | -0.03 | -5.18 | 1 |
| 36 | Supertrend · 1h | trend | 97.15 | -2.85 | 32 | 9.4 | 3.15 | 0.61 | -16.43 | 213 |
| 37 | Agent (ML meta-label) | meta | 97.04 | -2.96 | 263 | 14.8 | 1.70 | 0.46 | -13.21 | 382 |
| 38 | Williams %R · 1h | reversion | 96.85 | -3.15 | 85 | 52.9 | -19.79 | -3.73 | -20.53 | 493 |
| 39 | Parabolic SAR · 1h | trend | 96.73 | -3.27 | 65 | 15.4 | -2.96 | -0.21 | -19.45 | 301 |
| 40 | CCI reversion · 1h | reversion | 96.67 | -3.33 | 71 | 49.3 | 0.10 | 0.18 | -12.41 | 408 |
| 41 | MACD cross · 1h | trend | 95.94 | -4.06 | 86 | 19.8 | -11.21 | -1.78 | -17.27 | 474 |
| 42 | RSI momentum · 1h | momentum | 95.82 | -4.18 | 45 | 2.2 | 0.57 | 0.27 | -16.65 | 229 |
| 43 | Squeeze breakout · 1h | breakout | 95.42 | -4.58 | 30 | 20.0 | 15.90 | 2.66 | -8.06 | 105 |
| 44 | Ichimoku · 1h | trend | 95.30 | -4.70 | 33 | 15.2 | 8.86 | 1.22 | -15.84 | 124 |
| 45 | MFI reversion · 1h | reversion | 95.16 | -4.84 | 74 | 28.4 | -10.21 | -1.77 | -16.99 | 119 |
| 46 | Triple EMA stack · 1h | trend | 95.07 | -4.92 | 56 | 10.7 | -9.82 | -1.02 | -24.06 | 256 |
| 47 | Max aggression: 1-day momentum | meta | 94.79 | -5.21 | 7 | 42.9 | -23.67 | -1.23 | -37.31 | 42 |
| 48 | Bollinger breakout · 1h | breakout | 94.72 | -5.28 | 50 | 24.0 | 7.87 | 1.17 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.32 | -5.68 | 46 | 6.5 | 6.79 | 1.78 | -6.47 | 201 |
| 50 | Opening range 30m | breakout | 94.05 | -5.95 | 97 | 21.6 | -17.56 | -5.46 | -17.83 | 572 |
| 51 | Volume breakout · 1h | breakout | 93.87 | -6.13 | 36 | 11.1 | 6.73 | 1.09 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 93.08 | -6.92 | 80 | 11.2 | -2.16 | -0.09 | -18.47 | 346 |
| 53 | Max aggression: 5-day momentum | meta | 93.07 | -6.93 | 5 | 40.0 | -18.37 | -1.54 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 92.50 | -7.50 | 113 | 19.5 | -18.54 | -5.50 | -19.24 | 692 |
| 55 | Donchian 20/10 · 1h | breakout | 91.57 | -8.43 | 39 | 15.4 | 3.04 | 0.58 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.51 | -8.49 | 47 | 17.0 | -2.73 | -0.17 | -18.32 | 248 |
| 57 | Three white soldiers | momentum | 91.01 | -8.99 | 99 | 20.2 | -49.30 | -24.90 | -49.52 | 590 |
| 58 | VWAP momentum · 1h | momentum | 90.89 | -9.11 | 228 | 22.8 | -37.49 | -5.79 | -37.51 | 1271 |
| 59 | OBV trend · 1h | momentum | 90.88 | -9.12 | 105 | 11.4 | -12.69 | -1.41 | -26.73 | 338 |
| 60 | Heikin-Ashi · 1h | trend | 90.16 | -9.84 | 115 | 24.3 | -31.63 | -5.46 | -34.24 | 691 |
| 61 | Keltner breakout · 1h | breakout | 89.95 | -10.05 | 30 | 6.7 | -11.58 | -1.35 | -23.31 | 229 |
| 62 | ROC + volume · 1h | momentum | 87.57 | -12.43 | 105 | 15.2 | -8.62 | -1.02 | -23.04 | 411 |
| 63 | RSI(14) reversion | reversion | 85.99 | -14.01 | 218 | 32.1 | -70.56 | -19.44 | -71.01 | 1415 |
| 64 | VWAP reversion | reversion | 77.88 | -22.12 | 262 | 29.0 | -68.87 | -16.11 | -69.32 | 1374 |
| 65 | Squeeze breakout | breakout | 77.73 | -22.27 | 246 | 15.9 | -62.41 | -19.13 | -62.42 | 1226 |
| 66 | ROC + volume | momentum | 76.92 | -23.08 | 318 | 20.8 | -73.91 | -17.81 | -73.91 | 1652 |
| 67 | Donchian 55/20 | breakout | 76.06 | -23.94 | 258 | 17.4 | -68.96 | -15.35 | -68.96 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.74 | -25.26 | 262 | 18.7 | -78.54 | -16.22 | -78.55 | 1478 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.15 | -19.60 | -65.16 | 932 |
| 70 | Z-score reversion | reversion | 71.93 | -28.07 | 348 | 28.2 | -85.09 | -25.50 | -85.14 | 2053 |
| 71 | MFI reversion | reversion | 70.30 | -29.70 | 343 | 21.0 | -86.95 | -30.69 | -86.97 | 2120 |
| 72 | Supertrend | trend | 69.98 | -30.02 | 348 | 20.4 | -87.00 | -22.48 | -87.00 | 1930 |
| 73 | Keltner breakout | breakout | 68.15 | -31.85 | 348 | 13.2 | -85.57 | -30.75 | -85.57 | 1891 |
| 74 | AI bee: Bizzy | ai | 67.75 | -32.25 | 600 | 9.0 | — | — | — | — |
| 75 | Ichimoku | trend | 66.93 | -33.07 | 316 | 8.9 | -82.22 | -24.91 | -82.22 | 1769 |
| 76 | AI bee: Boozy | ai | 66.38 | -33.62 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.83 | -35.17 | 389 | 9.5 | -89.67 | -37.53 | -89.67 | 2107 |
| 78 | MACD zero-line | trend | 63.56 | -36.44 | 443 | 15.8 | -91.56 | -31.18 | -91.56 | 2365 |
| 79 | Donchian 20/10 | breakout | 62.91 | -37.09 | 480 | 18.5 | -91.25 | -28.03 | -91.25 | 2670 |
| 80 | RSI momentum | momentum | 61.97 | -38.03 | 450 | 16.7 | -90.62 | -27.02 | -90.62 | 2377 |
| 81 | Triple EMA stack | trend | 60.43 | -39.57 | 496 | 15.5 | -93.37 | -32.63 | -93.37 | 2630 |
| 82 | Trend pullback | trend | 60.30 | -39.70 | 477 | 15.3 | -91.48 | -31.02 | -91.48 | 2349 |
| 83 | Bollinger breakout | breakout | 59.67 | -40.33 | 492 | 14.2 | -94.07 | -36.23 | -94.07 | 2825 |
| 84 | Stochastic reversion | reversion | 58.47 | -41.53 | 696 | 23.1 | -95.52 | -37.92 | -95.57 | 4030 |
| 85 | Bollinger reversion | reversion | 58.22 | -41.78 | 645 | 18.3 | -95.58 | -36.77 | -95.62 | 3684 |
| 86 | Consensus | meta | 57.55 | -42.45 | 468 | 10.0 | -94.73 | -27.48 | -94.73 | 2715 |
| 87 | EMA 9/21 cross | trend | 55.89 | -44.11 | 608 | 16.4 | -97.44 | -35.70 | -97.44 | 3551 |
| 88 | Connors RSI(2) | reversion | 54.05 | -45.95 | 661 | 20.1 | -96.59 | -35.60 | -96.59 | 3642 |
| 89 | OBV trend | momentum | 52.41 | -47.59 | 717 | 15.2 | -96.47 | -40.17 | -96.47 | 3610 |
| 90 | CCI reversion | reversion | 52.33 | -47.67 | 667 | 16.8 | -98.44 | -40.93 | -98.44 | 4698 |
| 91 | Candlestick reversal | reversion | 51.19 | -48.81 | 768 | 14.7 | -99.28 | -40.77 | -99.28 | 5612 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -32.43 | -98.72 | 5385 |
| 93 | Parabolic SAR | trend | 50.40 | -49.60 | 656 | 14.8 | -97.38 | -42.38 | -97.38 | 3677 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.78 | -99.73 | 6126 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -45.04 | -99.50 | 6094 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.18 | -99.90 | 8247 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T18:00 | Agent (ML meta-label) | sell | SOL-USD | 2.12 | -0.01 | selected signal exited |
| 2026-10-06T18:00 | Williams %R · 1h | buy | ETH-USD | 24.23 | — | entry signal |
| 2026-10-06T18:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 24.92 | — | entry signal |
| 2026-10-06T18:00 | Candlestick reversal · 1h | buy | BTC-USD | 25.14 | — | entry signal |
| 2026-10-06T18:00 | OBV trend · 1h | buy | ETHU | 4.96 | — | entry |
| 2026-10-06T18:00 | OBV trend · 1h | sell | DOGE-USD | 4.96 | -0.09 | exit signal |
| 2026-10-06T18:00 | Trend pullback · 1h | buy | SOL-USD | 16.55 | — | entry signal |
| 2026-10-06T18:00 | Trend pullback · 1h | sell | DOGE-USD | 16.39 | -0.19 | exit signal |
| 2026-10-06T18:00 | Parabolic SAR · 1h | buy | SOXL | 5.69 | — | entry |
| 2026-10-06T18:00 | Parabolic SAR · 1h | buy | SOL-USD | 5.69 | — | entry |
| 2026-10-06T18:00 | Parabolic SAR · 1h | sell | ETH-USD | 5.99 | -0.07 | exit signal |
| 2026-10-06T18:00 | Parabolic SAR · 1h | sell | DOGE-USD | 6.78 | -0.10 | exit signal |
| 2026-10-06T18:00 | MACD zero-line · 1h | buy | XRP-USD | 5.09 | — | rebalance up |
| 2026-10-06T18:00 | MACD zero-line · 1h | sell | DOGE-USD | 3.40 | -0.06 | exit signal |
| 2026-10-06T18:00 | MACD zero-line · 1h | sell | BTC-USD | 6.50 | -0.08 | exit signal |
| 2026-10-06T18:00 | MACD cross · 1h | buy | XRP-USD | 3.42 | — | entry |
| 2026-10-06T18:00 | MACD cross · 1h | buy | SOL-USD | 5.65 | — | entry |
| 2026-10-06T18:00 | MACD cross · 1h | sell | DOGE-USD | 5.02 | -0.03 | exit signal |
| 2026-10-06T18:00 | MACD cross · 1h | sell | BTC-USD | 4.05 | -0.05 | exit signal |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | buy | SOL-USD | 3.55 | — | entry signal |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | buy | IWM | 5.90 | — | entry |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | buy | GOOGL | 5.90 | — | entry |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | sell | TECL | 5.03 | 0.46 | rebalance down |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | sell | SPY | 5.09 | 0.05 | rebalance down |
| 2026-10-06T18:00 | EMA 20/50 cross · 1h | sell | SOXL | 5.22 | 0.50 | rebalance down |
| 2026-10-06T18:00 | CCI reversion | buy | UPRO | 1.71 | — | entry |
| 2026-10-06T18:00 | CCI reversion | buy | TSLA | 2.91 | — | entry |
| 2026-10-06T18:00 | CCI reversion | buy | TQQQ | 2.91 | — | entry |
| 2026-10-06T18:00 | CCI reversion | buy | TNA | 2.91 | — | entry |
| 2026-10-06T18:00 | CCI reversion | sell | SOL-USD | 2.92 | -0.02 | exit signal |
| 2026-10-06T18:00 | CCI reversion | sell | MSTR | 2.93 | 0.01 | exit signal |
| 2026-10-06T18:00 | CCI reversion | sell | BTC-USD | 4.02 | -0.02 | exit signal |
| 2026-10-06T18:00 | Stochastic reversion | sell | COIN | 2.80 | 0.02 | exit signal |
| 2026-10-06T18:00 | Bollinger reversion | buy | AMD | 3.89 | — | rebalance up |
| 2026-10-06T18:00 | Bollinger reversion | sell | COIN | 8.35 | 0.03 | exit signal |
| 2026-10-06T18:00 | Candlestick reversal | sell | SOL-USD | 2.70 | -0.00 | exit signal |
| 2026-10-06T18:00 | Candlestick reversal | sell | MSTR | 2.71 | 0.01 | exit signal |
| 2026-10-06T18:00 | Squeeze breakout | buy | MSTR | 19.43 | — | entry signal |
| 2026-10-06T18:00 | Bollinger breakout | buy | SOL-USD | 14.93 | — | entry signal |
| 2026-10-06T18:00 | Bollinger breakout | buy | MSTR | 14.93 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 18:00:05.000146+00:00 -> 2026-10-06 18:10:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
