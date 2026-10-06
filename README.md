# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T14:00:05.000162+00:00 · 13537 ticks

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

Today: 11440 decisions in 2003 calls, $0.1562 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T14:00 | 0 / 26 / 4 | NANC 20%, TECL 18%, AMD 17% |  |
| Breezy | 2026-10-06T14:00 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-06T14:00 | 2 / 25 / 3 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.72 | 6.72 | 0 | — | -3.00 | -0.41 | -15.27 | 1 |
| 2 | Copy: Cathie Wood (ARKK) | copy | 103.37 | 3.37 | 0 | — | 22.91 | 3.42 | -6.29 | 1 |
| 3 | Hold BTC | benchmark | 102.90 | 2.90 | 0 | — | 33.36 | 4.01 | -8.68 | 1 |
| 4 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 5 | Daily: Bullish score | daily | 102.69 | 2.69 | 3 | 0.0 | 5.27 | 0.89 | -12.76 | 10 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 102.19 | 2.19 | 0 | — | -0.51 | -0.23 | -5.09 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 102.09 | 2.09 | 17 | 0.0 | 9.65 | 1.36 | -16.96 | 111 |
| 8 | Copy: Congress Democrats (NANC) | copy | 101.94 | 1.95 | 0 | — | 3.22 | 1.53 | -3.62 | 1 |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 10 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.23 | 1.23 | 6 | 33.3 | 5.39 | 1.63 | -7.55 | 43 |
| 12 | Hold SPY | benchmark | 101.16 | 1.16 | 0 | — | 0.75 | 0.49 | -3.66 | 1 |
| 13 | Stochastic reversion · 1h | reversion | 100.89 | 0.89 | 53 | 64.2 | -7.54 | -1.52 | -11.23 | 326 |
| 14 | EMA 20/50 cross · 1h | trend | 100.70 | 0.70 | 28 | 7.1 | 14.83 | 1.82 | -15.31 | 141 |
| 15 | Candlestick reversal · 1h | reversion | 100.55 | 0.55 | 62 | 35.5 | -19.79 | -4.31 | -21.84 | 496 |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.47 | 0.47 | 0 | — | -1.49 | -0.54 | -7.65 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 100.28 | 0.28 | 24 | 37.5 | 4.07 | 1.97 | -1.59 | 85 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 100.17 | 0.17 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 20 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 21 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 22 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -5.19 | -1.82 | -9.74 | 23 |
| 23 | Bollinger reversion · 1h | reversion | 99.94 | -0.06 | 48 | 47.9 | -14.68 | -3.80 | -17.21 | 303 |
| 24 | Z-score reversion · 1h | reversion | 99.87 | -0.14 | 21 | 52.4 | 7.22 | 1.60 | -8.60 | 150 |
| 25 | Connors RSI(2) · 1h | reversion | 99.63 | -0.37 | 72 | 44.4 | -12.99 | -4.49 | -16.84 | 221 |
| 26 | Trend pullback · 1h | trend | 99.61 | -0.39 | 62 | 25.8 | -19.13 | -5.50 | -23.07 | 170 |
| 27 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 3.15 | 0.89 | -6.57 | 126 |
| 28 | Williams %R · 1h | reversion | 99.22 | -0.78 | 80 | 53.8 | -17.92 | -3.29 | -20.74 | 498 |
| 29 | Daily: Momentum burst | daily | 98.82 | -1.18 | 3 | 0.0 | -0.30 | 0.13 | -16.91 | 41 |
| 30 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -2.85 | -1.51 | -5.35 | 105 |
| 31 | CCI reversion · 1h | reversion | 98.38 | -1.62 | 69 | 49.3 | 2.51 | 0.57 | -12.41 | 405 |
| 32 | Agent (rotation) | meta | 98.34 | -1.66 | 60 | 28.3 | -0.01 | 0.09 | -10.29 | 258 |
| 33 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.07 | -2.42 | -3.95 | 25 |
| 34 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -9.89 | -6.21 | -11.49 | 225 |
| 35 | ADX DI cross · 1h | trend | 98.10 | -1.90 | 41 | 12.2 | -2.26 | -0.23 | -13.84 | 259 |
| 36 | Copy: Insider buying | copy | 98.05 | -1.95 | 9 | 55.6 | -15.72 | -2.91 | -21.08 | 73 |
| 37 | Agent (ML meta-label) | meta | 97.73 | -2.27 | 245 | 15.1 | -4.73 | -0.76 | -13.86 | 396 |
| 38 | Supertrend · 1h | trend | 97.64 | -2.36 | 32 | 9.4 | 3.46 | 0.65 | -16.43 | 205 |
| 39 | Parabolic SAR · 1h | trend | 96.99 | -3.01 | 62 | 16.1 | -2.38 | -0.13 | -19.45 | 296 |
| 40 | Daily: SMA 20/50 cross · AAPL | daily | 96.85 | -3.15 | 0 | — | -0.34 | -0.04 | -5.18 | 1 |
| 41 | MACD cross · 1h | trend | 96.65 | -3.35 | 81 | 19.8 | -7.41 | -1.04 | -17.27 | 479 |
| 42 | RSI momentum · 1h | momentum | 96.23 | -3.77 | 45 | 2.2 | 2.83 | 0.56 | -16.65 | 230 |
| 43 | Squeeze breakout · 1h | breakout | 95.94 | -4.06 | 27 | 22.2 | 14.32 | 2.41 | -8.06 | 110 |
| 44 | Ichimoku · 1h | trend | 95.86 | -4.14 | 31 | 16.1 | 9.64 | 1.30 | -15.84 | 120 |
| 45 | Triple EMA stack · 1h | trend | 95.42 | -4.58 | 56 | 10.7 | -7.57 | -0.73 | -23.99 | 253 |
| 46 | Bollinger breakout · 1h | breakout | 95.21 | -4.79 | 46 | 26.1 | 6.38 | 0.99 | -12.06 | 293 |
| 47 | MFI reversion · 1h | reversion | 95.17 | -4.83 | 73 | 27.4 | -9.98 | -1.73 | -16.99 | 122 |
| 48 | Gap and go | momentum | 95.11 | -4.89 | 39 | 7.7 | 8.14 | 2.12 | -5.39 | 195 |
| 49 | Max aggression: 1-day momentum | meta | 94.84 | -5.16 | 7 | 42.9 | -23.62 | -1.22 | -37.31 | 42 |
| 50 | Opening range 30m | breakout | 94.80 | -5.20 | 87 | 24.1 | -16.51 | -5.13 | -17.14 | 552 |
| 51 | Volume breakout · 1h | breakout | 94.30 | -5.71 | 33 | 12.1 | 7.23 | 1.16 | -12.60 | 130 |
| 52 | Max aggression: 5-day momentum | meta | 93.54 | -6.46 | 5 | 40.0 | -17.94 | -1.49 | -29.56 | 29 |
| 53 | EMA 9/21 cross · 1h | trend | 93.36 | -6.64 | 78 | 11.5 | -1.48 | -0.00 | -18.47 | 344 |
| 54 | Opening range 15m | breakout | 93.21 | -6.79 | 102 | 21.6 | -17.74 | -5.24 | -18.88 | 677 |
| 55 | VWAP momentum · 1h | momentum | 92.31 | -7.69 | 197 | 21.8 | -37.02 | -5.67 | -37.83 | 1277 |
| 56 | MACD zero-line · 1h | trend | 91.95 | -8.05 | 43 | 18.6 | 1.64 | 0.41 | -18.32 | 248 |
| 57 | Donchian 20/10 · 1h | breakout | 91.94 | -8.06 | 36 | 16.7 | 2.58 | 0.52 | -16.18 | 220 |
| 58 | OBV trend · 1h | momentum | 91.14 | -8.86 | 103 | 11.7 | -11.84 | -1.29 | -26.62 | 336 |
| 59 | Heikin-Ashi · 1h | trend | 90.85 | -9.15 | 104 | 25.0 | -30.94 | -5.31 | -34.14 | 700 |
| 60 | Three white soldiers | momentum | 90.69 | -9.30 | 95 | 20.0 | -49.53 | -25.39 | -49.58 | 586 |
| 61 | Keltner breakout · 1h | breakout | 89.93 | -10.07 | 30 | 6.7 | -11.42 | -1.35 | -23.32 | 222 |
| 62 | ROC + volume · 1h | momentum | 88.04 | -11.96 | 99 | 15.2 | -9.22 | -1.10 | -23.04 | 416 |
| 63 | RSI(14) reversion | reversion | 84.80 | -15.20 | 214 | 31.3 | -71.09 | -19.92 | -71.23 | 1428 |
| 64 | Squeeze breakout | breakout | 77.97 | -22.03 | 240 | 15.8 | -62.58 | -19.21 | -62.59 | 1235 |
| 65 | ROC + volume | momentum | 77.28 | -22.71 | 304 | 20.4 | -73.97 | -17.89 | -74.06 | 1666 |
| 66 | VWAP reversion | reversion | 77.25 | -22.75 | 256 | 28.1 | -69.19 | -16.33 | -69.30 | 1372 |
| 67 | Donchian 55/20 | breakout | 76.84 | -23.16 | 240 | 18.3 | -68.91 | -15.41 | -68.93 | 1299 |
| 68 | EMA 20/50 cross | trend | 75.35 | -24.65 | 257 | 19.1 | -78.48 | -16.19 | -78.58 | 1483 |
| 69 | Volume breakout | breakout | 73.81 | -26.19 | 208 | 12.5 | -65.41 | -19.69 | -65.60 | 931 |
| 70 | Z-score reversion | reversion | 72.25 | -27.75 | 339 | 27.4 | -84.99 | -25.46 | -85.04 | 2058 |
| 71 | Supertrend | trend | 70.80 | -29.20 | 338 | 21.0 | -86.96 | -22.53 | -86.96 | 1928 |
| 72 | MFI reversion | reversion | 70.58 | -29.42 | 329 | 21.0 | -86.93 | -30.59 | -86.95 | 2098 |
| 73 | Keltner breakout | breakout | 68.55 | -31.45 | 332 | 13.6 | -85.36 | -30.20 | -85.48 | 1886 |
| 74 | AI bee: Bizzy | ai | 67.72 | -32.28 | 589 | 8.5 | — | — | — | — |
| 75 | Ichimoku | trend | 67.67 | -32.33 | 296 | 9.1 | -82.43 | -24.96 | -82.44 | 1762 |
| 76 | AI bee: Boozy | ai | 67.13 | -32.87 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 65.44 | -34.56 | 373 | 9.1 | -89.73 | -38.34 | -89.76 | 2112 |
| 78 | MACD zero-line | trend | 64.35 | -35.65 | 431 | 15.8 | -91.57 | -31.55 | -91.57 | 2365 |
| 79 | Donchian 20/10 | breakout | 63.71 | -36.29 | 459 | 18.7 | -91.22 | -28.19 | -91.22 | 2673 |
| 80 | RSI momentum | momentum | 62.66 | -37.34 | 433 | 16.6 | -90.67 | -27.43 | -90.69 | 2384 |
| 81 | Trend pullback | trend | 61.26 | -38.74 | 448 | 15.8 | -91.44 | -31.17 | -91.44 | 2346 |
| 82 | Triple EMA stack | trend | 61.12 | -38.88 | 481 | 15.8 | -93.40 | -33.07 | -93.40 | 2636 |
| 83 | Bollinger breakout | breakout | 60.35 | -39.65 | 470 | 14.3 | -94.07 | -36.50 | -94.08 | 2844 |
| 84 | Consensus | meta | 58.40 | -41.59 | 436 | 10.3 | -94.57 | -27.15 | -94.57 | 2683 |
| 85 | Stochastic reversion | reversion | 58.36 | -41.64 | 664 | 22.4 | -95.54 | -38.05 | -95.54 | 4028 |
| 86 | Bollinger reversion | reversion | 57.62 | -42.38 | 619 | 17.0 | -95.65 | -37.26 | -95.65 | 3668 |
| 87 | EMA 9/21 cross | trend | 56.66 | -43.34 | 589 | 16.8 | -97.43 | -35.96 | -97.43 | 3561 |
| 88 | Connors RSI(2) | reversion | 55.02 | -44.98 | 597 | 18.6 | -96.54 | -35.37 | -96.54 | 3602 |
| 89 | OBV trend | momentum | 53.17 | -46.83 | 686 | 15.3 | -96.46 | -41.27 | -96.46 | 3620 |
| 90 | CCI reversion | reversion | 52.62 | -47.38 | 642 | 16.2 | -98.44 | -41.10 | -98.45 | 4682 |
| 91 | Candlestick reversal | reversion | 51.48 | -48.52 | 732 | 14.1 | -99.27 | -40.54 | -99.28 | 5615 |
| 92 | VWAP momentum | momentum | 51.44 | -48.56 | 662 | 8.3 | -98.72 | -32.65 | -98.72 | 5375 |
| 93 | Parabolic SAR | trend | 51.36 | -48.64 | 630 | 15.1 | -97.41 | -43.26 | -97.41 | 3671 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -48.36 | -99.73 | 6130 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -45.13 | -99.50 | 6088 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -54.45 | -99.90 | 8260 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T14:00 | Agent (rotation) | sell | DOGE-USD | 3.29 | 0.00 | selected signal exited |
| 2026-10-06T14:00 | Agent (ML meta-label) | buy | COIN | 3.35 | — | entry |
| 2026-10-06T14:00 | Agent (ML meta-label) | sell | SOL-USD | 3.35 | -0.02 | selected signal exited |
| 2026-10-06T14:00 | Consensus | buy | SPY | 4.82 | — | entry |
| 2026-10-06T14:00 | Consensus | sell | BTC-USD | 4.82 | -0.03 | rebalance down |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | SOL-USD | 6.49 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | LABU | 6.94 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | ETHU | 6.52 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | ETH-USD | 6.57 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | COIN | 6.37 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | buy | AAPL | 6.62 | — | rebalance up |
| 2026-10-06T14:00 | CCI reversion · 1h | sell | DOGE-USD | 9.91 | 0.01 | exit signal |
| 2026-10-06T14:00 | ROC + volume · 1h | buy | XRP-USD | 6.29 | — | entry signal |
| 2026-10-06T14:00 | ROC + volume · 1h | buy | DOGE-USD | 6.29 | — | entry signal |
| 2026-10-06T14:00 | ROC + volume · 1h | buy | BTC-USD | 6.29 | — | entry signal |
| 2026-10-06T14:00 | Ichimoku · 1h | buy | XRP-USD | 15.98 | — | entry signal |
| 2026-10-06T14:00 | Ichimoku · 1h | buy | DOGE-USD | 16.00 | — | entry signal |
| 2026-10-06T14:00 | Ichimoku · 1h | sell | SPY | 7.49 | 0.06 | rebalance down |
| 2026-10-06T14:00 | Ichimoku · 1h | sell | SOXL | 8.24 | 0.61 | rebalance down |
| 2026-10-06T14:00 | Ichimoku · 1h | sell | NVDA | 8.06 | 0.20 | rebalance down |
| 2026-10-06T14:00 | Ichimoku · 1h | sell | AMD | 8.18 | 0.05 | rebalance down |
| 2026-10-06T14:00 | Parabolic SAR · 1h | buy | ETH-USD | 6.06 | — | entry signal |
| 2026-10-06T14:00 | Stochastic reversion | buy | GOOGL | 14.59 | — | entry signal |
| 2026-10-06T14:00 | Stochastic reversion | buy | AAPL | 14.59 | — | entry signal |
| 2026-10-06T14:00 | Bollinger reversion | buy | META | 14.41 | — | entry signal |
| 2026-10-06T14:00 | Bollinger reversion | buy | AAPL | 14.41 | — | entry signal |
| 2026-10-06T14:00 | RSI(14) reversion | buy | AAPL | 21.20 | — | entry signal |
| 2026-10-06T14:00 | Candlestick reversal | buy | GOOGL | 12.85 | — | entry signal |
| 2026-10-06T14:00 | OBV trend | buy | AMZN | 3.04 | — | entry signal |
| 2026-10-06T14:00 | OBV trend | sell | SOL-USD | 3.04 | -0.01 | rebalance down |
| 2026-10-06T14:00 | Ichimoku | buy | DOGE-USD | 16.93 | — | entry signal |
| 2026-10-06T13:57 | Consensus | buy | XRP-USD | 2.91 | — | rebalance up |
| 2026-10-06T13:57 | Consensus | sell | ETH-USD | 2.91 | -0.02 | rebalance down |
| 2026-10-06T13:55 | Agent (ML meta-label) | buy | SOL-USD | 3.37 | — | entry |
| 2026-10-06T13:55 | Agent (ML meta-label) | buy | DOGE-USD | 4.25 | — | following Stochastic reversion · 1h, VWAP reversion · 1h |
| 2026-10-06T13:55 | Consensus | buy | XRP-USD | 5.88 | — | entry |
| 2026-10-06T13:55 | Consensus | buy | AMD | 11.70 | — | entry |
| 2026-10-06T13:55 | Consensus | sell | DOGE-USD | 2.93 | -0.01 | rebalance down |
| 2026-10-06T13:55 | ROC + volume · 1h | sell | AMZN | 4.86 | -0.01 | target is flat |
| 2026-10-06T13:55 | Stochastic reversion | buy | LABU | 14.63 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 14:00:05.000162+00:00 -> 2026-10-06 14:10:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
