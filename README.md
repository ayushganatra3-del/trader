# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T15:00:05.000178+00:00 · 13578 ticks

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

Today: 15148 decisions in 2126 calls, $0.1996 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T15:00 | 4 / 21 / 5 | NANC 20%, AMD 15% |  |
| Breezy | 2026-10-06T15:00 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-06T15:00 | 5 / 22 / 3 | MSTR 70% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 107.10 | 7.10 | 0 | — | -0.72 | 0.00 | -15.27 | 1 |
| 2 | Hold BTC | benchmark | 103.31 | 3.31 | 0 | — | 34.14 | 4.09 | -8.68 | 1 |
| 3 | Daily: Bullish score | daily | 102.93 | 2.93 | 3 | 0.0 | 6.22 | 1.01 | -12.76 | 10 |
| 4 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 5 | Donchian 55/20 · 1h | breakout | 102.46 | 2.46 | 17 | 0.0 | 9.87 | 1.38 | -16.96 | 111 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 102.35 | 2.35 | 0 | — | 0.27 | 0.20 | -5.09 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 102.03 | 2.03 | 0 | — | 3.20 | 1.51 | -3.62 | 1 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 10 | Hold SPY | benchmark | 101.29 | 1.29 | 0 | — | 1.19 | 0.77 | -3.66 | 1 |
| 11 | EMA 20/50 cross · 1h | trend | 101.05 | 1.05 | 28 | 7.1 | 15.17 | 1.85 | -15.31 | 142 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 13 | Stochastic reversion · 1h | reversion | 100.95 | 0.95 | 55 | 65.5 | -6.99 | -1.41 | -10.71 | 326 |
| 14 | Candlestick reversal · 1h | reversion | 100.85 | 0.85 | 66 | 39.4 | -22.82 | -5.35 | -24.91 | 489 |
| 15 | Copy: Cathie Wood (ARKK) | copy | 100.69 | 0.69 | 0 | — | 19.68 | 3.00 | -6.29 | 1 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.35 | 0.35 | 0 | — | -1.39 | -0.50 | -7.65 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 100.21 | 0.21 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.90 | 1.88 | -1.59 | 84 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 20 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 21 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 22 | Trend pullback · 1h | trend | 100.00 | 0.00 | 62 | 25.8 | -19.61 | -5.65 | -24.20 | 167 |
| 23 | Z-score reversion · 1h | reversion | 99.95 | -0.05 | 22 | 54.5 | 6.44 | 1.47 | -8.60 | 149 |
| 24 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.71 | -1.65 | -9.74 | 23 |
| 25 | Bollinger reversion · 1h | reversion | 99.94 | -0.06 | 48 | 47.9 | -14.64 | -3.80 | -17.18 | 303 |
| 26 | Connors RSI(2) · 1h | reversion | 99.63 | -0.37 | 72 | 44.4 | -13.16 | -4.50 | -17.01 | 220 |
| 27 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 4.02 | 1.18 | -6.57 | 118 |
| 28 | Williams %R · 1h | reversion | 99.38 | -0.62 | 83 | 53.0 | -18.24 | -3.36 | -21.13 | 493 |
| 29 | Daily: Momentum burst | daily | 98.99 | -1.01 | 3 | 0.0 | 0.57 | 0.27 | -16.91 | 41 |
| 30 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -2.09 | -1.11 | -4.94 | 104 |
| 31 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.42 | -3.95 | 25 |
| 32 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.60 | -5.59 | -9.92 | 230 |
| 33 | Agent (rotation) | meta | 98.17 | -1.83 | 62 | 29.0 | 0.07 | 0.12 | -10.19 | 252 |
| 34 | ADX DI cross · 1h | trend | 98.04 | -1.96 | 41 | 12.2 | -1.58 | -0.12 | -13.84 | 255 |
| 35 | CCI reversion · 1h | reversion | 97.93 | -2.06 | 71 | 49.3 | 2.09 | 0.50 | -12.41 | 405 |
| 36 | Agent (ML meta-label) | meta | 97.91 | -2.09 | 251 | 15.1 | 4.98 | 1.05 | -13.48 | 371 |
| 37 | Copy: Insider buying | copy | 97.80 | -2.20 | 9 | 55.6 | -15.85 | -2.93 | -21.08 | 73 |
| 38 | Supertrend · 1h | trend | 97.77 | -2.23 | 32 | 9.4 | 4.17 | 0.74 | -16.43 | 211 |
| 39 | Parabolic SAR · 1h | trend | 97.44 | -2.56 | 62 | 16.1 | -2.33 | -0.12 | -19.45 | 301 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 97.35 | -2.65 | 0 | — | -0.94 | -0.28 | -5.18 | 1 |
| 41 | MACD cross · 1h | trend | 96.89 | -3.11 | 82 | 19.5 | -6.78 | -0.90 | -17.27 | 479 |
| 42 | RSI momentum · 1h | momentum | 96.50 | -3.50 | 45 | 2.2 | 2.15 | 0.48 | -16.65 | 227 |
| 43 | Ichimoku · 1h | trend | 96.34 | -3.66 | 31 | 16.1 | 10.10 | 1.35 | -15.84 | 124 |
| 44 | Squeeze breakout · 1h | breakout | 96.34 | -3.66 | 27 | 22.2 | 15.08 | 2.51 | -8.06 | 113 |
| 45 | Triple EMA stack · 1h | trend | 95.83 | -4.17 | 56 | 10.7 | -6.66 | -0.62 | -24.34 | 244 |
| 46 | Bollinger breakout · 1h | breakout | 95.49 | -4.51 | 46 | 26.1 | 6.78 | 1.04 | -12.06 | 298 |
| 47 | MFI reversion · 1h | reversion | 95.20 | -4.80 | 73 | 27.4 | -10.19 | -1.77 | -16.99 | 119 |
| 48 | Max aggression: 1-day momentum | meta | 95.05 | -4.95 | 7 | 42.9 | -23.49 | -1.21 | -37.31 | 42 |
| 49 | Gap and go | momentum | 94.62 | -5.38 | 43 | 7.0 | 7.08 | 1.85 | -6.42 | 201 |
| 50 | Volume breakout · 1h | breakout | 94.36 | -5.64 | 35 | 11.4 | 7.31 | 1.17 | -12.60 | 132 |
| 51 | Opening range 30m | breakout | 94.35 | -5.65 | 93 | 22.6 | -16.93 | -5.28 | -17.27 | 570 |
| 52 | EMA 9/21 cross · 1h | trend | 93.74 | -6.26 | 78 | 11.5 | -1.15 | 0.04 | -18.47 | 347 |
| 53 | Max aggression: 5-day momentum | meta | 93.57 | -6.43 | 5 | 40.0 | -17.96 | -1.49 | -29.56 | 29 |
| 54 | Opening range 15m | breakout | 93.05 | -6.95 | 105 | 21.0 | -17.89 | -5.30 | -18.88 | 690 |
| 55 | MACD zero-line · 1h | trend | 92.17 | -7.83 | 43 | 18.6 | -0.59 | 0.12 | -18.32 | 249 |
| 56 | VWAP momentum · 1h | momentum | 92.16 | -7.84 | 209 | 24.4 | -37.02 | -5.66 | -37.80 | 1279 |
| 57 | Donchian 20/10 · 1h | breakout | 92.08 | -7.92 | 36 | 16.7 | 2.42 | 0.50 | -16.18 | 227 |
| 58 | OBV trend · 1h | momentum | 91.45 | -8.55 | 103 | 11.7 | -11.43 | -1.24 | -26.71 | 339 |
| 59 | Heikin-Ashi · 1h | trend | 90.89 | -9.11 | 108 | 24.1 | -30.93 | -5.31 | -34.14 | 701 |
| 60 | Three white soldiers | momentum | 90.66 | -9.35 | 96 | 19.8 | -49.56 | -25.44 | -49.59 | 587 |
| 61 | Keltner breakout · 1h | breakout | 90.30 | -9.70 | 30 | 6.7 | -10.61 | -1.23 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 88.33 | -11.67 | 101 | 15.8 | -8.86 | -1.04 | -23.04 | 422 |
| 63 | RSI(14) reversion | reversion | 85.06 | -14.94 | 216 | 31.5 | -71.09 | -19.96 | -71.24 | 1416 |
| 64 | Squeeze breakout | breakout | 78.06 | -21.94 | 243 | 15.6 | -62.44 | -19.10 | -62.58 | 1228 |
| 65 | VWAP reversion | reversion | 77.88 | -22.12 | 256 | 28.1 | -68.52 | -15.90 | -69.03 | 1368 |
| 66 | ROC + volume | momentum | 77.27 | -22.73 | 311 | 19.9 | -73.78 | -17.80 | -73.91 | 1665 |
| 67 | Donchian 55/20 | breakout | 76.71 | -23.29 | 244 | 18.0 | -68.97 | -15.41 | -69.04 | 1309 |
| 68 | EMA 20/50 cross | trend | 75.67 | -24.33 | 257 | 19.1 | -78.23 | -16.05 | -78.42 | 1483 |
| 69 | Volume breakout | breakout | 73.57 | -26.43 | 210 | 12.4 | -65.38 | -19.84 | -65.47 | 933 |
| 70 | Z-score reversion | reversion | 72.32 | -27.68 | 341 | 27.6 | -84.99 | -25.48 | -85.06 | 2064 |
| 71 | Supertrend | trend | 71.09 | -28.91 | 338 | 21.0 | -86.95 | -22.54 | -87.00 | 1930 |
| 72 | MFI reversion | reversion | 70.73 | -29.27 | 329 | 21.0 | -86.77 | -30.15 | -86.86 | 2110 |
| 73 | Keltner breakout | breakout | 68.54 | -31.46 | 336 | 13.4 | -85.38 | -30.21 | -85.53 | 1897 |
| 74 | AI bee: Bizzy | ai | 67.83 | -32.16 | 592 | 8.8 | — | — | — | — |
| 75 | Ichimoku | trend | 67.48 | -32.52 | 301 | 9.0 | -82.49 | -24.97 | -82.55 | 1776 |
| 76 | AI bee: Boozy | ai | 67.35 | -32.65 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.47 | -34.53 | 376 | 9.0 | -89.69 | -38.08 | -89.73 | 2099 |
| 78 | MACD zero-line | trend | 64.28 | -35.72 | 433 | 15.7 | -91.51 | -31.19 | -91.52 | 2366 |
| 79 | Donchian 20/10 | breakout | 63.50 | -36.50 | 464 | 18.5 | -91.29 | -28.34 | -91.31 | 2683 |
| 80 | RSI momentum | momentum | 62.97 | -37.03 | 435 | 16.6 | -90.66 | -27.43 | -90.72 | 2391 |
| 81 | Trend pullback | trend | 61.45 | -38.55 | 454 | 15.9 | -91.33 | -30.97 | -91.38 | 2351 |
| 82 | Triple EMA stack | trend | 61.20 | -38.80 | 484 | 15.7 | -93.39 | -33.10 | -93.42 | 2641 |
| 83 | Bollinger breakout | breakout | 60.26 | -39.74 | 477 | 14.0 | -94.07 | -36.47 | -94.09 | 2840 |
| 84 | Stochastic reversion | reversion | 58.54 | -41.46 | 668 | 22.6 | -95.50 | -37.72 | -95.57 | 4016 |
| 85 | Bollinger reversion | reversion | 58.36 | -41.64 | 622 | 17.4 | -95.57 | -36.75 | -95.63 | 3664 |
| 86 | Consensus | meta | 58.25 | -41.75 | 444 | 10.1 | -94.57 | -27.23 | -94.58 | 2692 |
| 87 | EMA 9/21 cross | trend | 56.63 | -43.37 | 592 | 16.7 | -97.42 | -35.80 | -97.43 | 3552 |
| 88 | Connors RSI(2) | reversion | 54.98 | -45.02 | 609 | 19.4 | -96.54 | -35.41 | -96.56 | 3610 |
| 89 | OBV trend | momentum | 53.16 | -46.84 | 693 | 15.2 | -96.47 | -41.17 | -96.49 | 3630 |
| 90 | CCI reversion | reversion | 52.83 | -47.17 | 647 | 16.5 | -98.43 | -40.83 | -98.45 | 4680 |
| 91 | Candlestick reversal | reversion | 51.66 | -48.34 | 740 | 14.5 | -99.28 | -40.69 | -99.28 | 5592 |
| 92 | VWAP momentum | momentum | 51.57 | -48.43 | 670 | 8.7 | -98.70 | -32.34 | -98.71 | 5399 |
| 93 | Parabolic SAR | trend | 51.12 | -48.88 | 636 | 14.9 | -97.40 | -43.12 | -97.41 | 3676 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.43 | -99.73 | 6134 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -44.88 | -99.50 | 6084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -53.78 | -99.90 | 8267 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T15:00 | Agent (rotation) | buy | ETH-USD | 4.91 | — | rebalance up |
| 2026-10-06T15:00 | Agent (rotation) | sell | SOL-USD | 3.29 | 0.01 | selected signal exited |
| 2026-10-06T15:00 | Agent (ML meta-label) | buy | ETH-USD | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | buy | SPY | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | buy | SOL-USD | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | buy | ETHU | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | buy | DOGE-USD | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | buy | BITX | 3.89 | — | entry |
| 2026-10-06T15:00 | Consensus | sell | TECL | 3.40 | 0.00 | rebalance down |
| 2026-10-06T15:00 | Consensus | sell | MSFT | 3.39 | -0.00 | rebalance down |
| 2026-10-06T15:00 | Consensus | sell | GOOGL | 3.38 | 0.00 | rebalance down |
| 2026-10-06T15:00 | Consensus | sell | BTC-USD | 3.39 | -0.01 | rebalance down |
| 2026-10-06T15:00 | Consensus | sell | AMZN | 3.39 | 0.01 | rebalance down |
| 2026-10-06T15:00 | Consensus | sell | AMD | 3.44 | 0.05 | rebalance down |
| 2026-10-06T15:00 | CCI reversion · 1h | buy | ETHU | 7.93 | — | rebalance up |
| 2026-10-06T15:00 | CCI reversion · 1h | buy | ETH-USD | 8.06 | — | rebalance up |
| 2026-10-06T15:00 | CCI reversion · 1h | buy | COIN | 7.95 | — | rebalance up |
| 2026-10-06T15:00 | CCI reversion · 1h | buy | AAPL | 8.01 | — | rebalance up |
| 2026-10-06T15:00 | CCI reversion · 1h | sell | SOL-USD | 16.43 | 0.05 | exit signal |
| 2026-10-06T15:00 | Williams %R · 1h | sell | ETH-USD | 24.72 | -0.11 | exit signal |
| 2026-10-06T15:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.17 | — | rebalance up |
| 2026-10-06T15:00 | Candlestick reversal · 1h | sell | XRP-USD | 20.16 | 0.02 | exit signal |
| 2026-10-06T15:00 | Candlestick reversal · 1h | sell | DOGE-USD | 21.73 | 0.15 | exit signal |
| 2026-10-06T15:00 | Candlestick reversal · 1h | sell | COIN | 20.88 | 1.04 | take-profit |
| 2026-10-06T15:00 | Candlestick reversal · 1h | sell | BTC-USD | 16.71 | 0.03 | exit signal |
| 2026-10-06T15:00 | Volume breakout · 1h | buy | BTC-USD | 10.49 | — | entry signal |
| 2026-10-06T15:00 | Squeeze breakout · 1h | buy | XRP-USD | 13.76 | — | entry signal |
| 2026-10-06T15:00 | Squeeze breakout · 1h | buy | DOGE-USD | 13.78 | — | entry signal |
| 2026-10-06T15:00 | Squeeze breakout · 1h | buy | BTC-USD | 13.78 | — | entry signal |
| 2026-10-06T15:00 | Squeeze breakout · 1h | sell | NVDA | 5.96 | 0.12 | rebalance down |
| 2026-10-06T15:00 | Squeeze breakout · 1h | sell | MSFT | 10.28 | 0.10 | rebalance down |
| 2026-10-06T15:00 | Squeeze breakout · 1h | sell | META | 9.77 | -0.11 | rebalance down |
| 2026-10-06T15:00 | Squeeze breakout · 1h | sell | AMD | 10.79 | 0.17 | rebalance down |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | XRP-USD | 5.60 | — | entry signal |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | SOL-USD | 5.62 | — | entry signal |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | PLTR | 5.62 | — | entry |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | MSTR | 5.62 | — | entry |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | MSFT | 5.62 | — | entry |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | META | 5.62 | — | entry |
| 2026-10-06T15:00 | Bollinger breakout · 1h | buy | DOGE-USD | 5.62 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 15:00:05.000178+00:00 -> 2026-10-06 15:10:05.000178+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
