# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T19:29:05.000117+00:00 · 13790 ticks

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

Today: 34174 decisions in 2762 calls, $0.4225 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T19:29 | 2 / 21 / 7 | AAPL 14% |  |
| Breezy | 2026-10-06T19:29 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-06T19:29 | 2 / 25 / 3 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| Volume breakout | LABU | 1.81 | +2.37% | 3 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 106.38 | 6.38 | 0 | — | -0.51 | 0.04 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -9.14 | -2.89 | -13.90 | 113 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.06 | 2.06 | 0 | — | 0.34 | 0.24 | -5.09 | 1 |
| 4 | Hold BTC | benchmark | 101.87 | 1.87 | 0 | — | 31.23 | 3.79 | -8.68 | 1 |
| 5 | Donchian 55/20 · 1h | breakout | 101.79 | 1.79 | 17 | 0.0 | 12.97 | 1.76 | -16.96 | 110 |
| 6 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.69 | 1.69 | 0 | — | 3.37 | 1.61 | -3.62 | 1 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 9 | Daily: Bullish score | daily | 101.22 | 1.22 | 3 | 0.0 | 5.50 | 0.93 | -12.76 | 10 |
| 10 | Hold SPY | benchmark | 101.11 | 1.11 | 0 | — | 1.09 | 0.70 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.34 | 0.34 | 68 | 38.2 | -19.90 | -4.45 | -21.70 | 495 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 100.14 | 0.14 | 0 | — | -2.81 | -1.36 | -5.14 | 1 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 15 | Copy: Warren Buffett (BRK-B) | copy | 100.02 | 0.02 | 0 | — | -2.56 | -0.99 | -7.65 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 100.01 | 0.01 | 4 | 50.0 | -0.77 | -0.84 | -2.30 | 20 |
| 17 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 18 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 19 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 20 | EMA 20/50 cross · 1h | trend | 99.91 | -0.09 | 28 | 7.1 | 13.68 | 1.70 | -15.31 | 141 |
| 21 | Stochastic reversion · 1h | reversion | 99.63 | -0.37 | 56 | 64.3 | -7.83 | -1.61 | -10.46 | 326 |
| 22 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 3.58 | 0.97 | -6.57 | 132 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 99.35 | -0.65 | 0 | — | 19.77 | 2.99 | -6.29 | 1 |
| 24 | Connors RSI(2) · 1h | reversion | 99.30 | -0.70 | 73 | 45.2 | -11.06 | -4.00 | -14.73 | 218 |
| 25 | Trend pullback · 1h | trend | 98.98 | -1.02 | 65 | 24.6 | -20.58 | -6.06 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | 0.03 | 0.07 | -4.23 | 104 |
| 27 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 28 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -8.85 | -5.37 | -10.05 | 228 |
| 29 | Daily: Momentum burst | daily | 98.17 | -1.83 | 3 | 0.0 | 1.33 | 0.38 | -16.91 | 41 |
| 30 | Z-score reversion · 1h | reversion | 98.16 | -1.84 | 23 | 52.2 | 3.70 | 0.90 | -8.60 | 150 |
| 31 | Copy: Insider buying | copy | 98.15 | -1.85 | 11 | 54.5 | -15.41 | -2.84 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.76 | -2.24 | 49 | 46.9 | -15.36 | -3.84 | -17.05 | 301 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.36 | -2.64 | 0 | — | -0.38 | -0.06 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.04 | -2.96 | 63 | 28.6 | -5.06 | -1.20 | -11.73 | 269 |
| 35 | ADX DI cross · 1h | trend | 96.95 | -3.05 | 43 | 11.6 | -3.18 | -0.40 | -13.84 | 255 |
| 36 | Supertrend · 1h | trend | 96.84 | -3.16 | 32 | 9.4 | 1.77 | 0.43 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.66 | -3.34 | 265 | 14.7 | -0.11 | 0.11 | -12.31 | 376 |
| 38 | Parabolic SAR · 1h | trend | 96.46 | -3.54 | 65 | 15.4 | -3.20 | -0.24 | -19.45 | 301 |
| 39 | Williams %R · 1h | reversion | 96.00 | -4.00 | 85 | 52.9 | -20.54 | -3.84 | -20.60 | 495 |
| 40 | CCI reversion · 1h | reversion | 95.88 | -4.12 | 71 | 49.3 | -0.31 | 0.11 | -12.41 | 407 |
| 41 | MACD cross · 1h | trend | 95.70 | -4.30 | 89 | 19.1 | -13.79 | -2.23 | -17.27 | 468 |
| 42 | RSI momentum · 1h | momentum | 95.50 | -4.50 | 45 | 2.2 | 0.63 | 0.28 | -16.65 | 230 |
| 43 | Squeeze breakout · 1h | breakout | 95.35 | -4.65 | 30 | 20.0 | 15.75 | 2.65 | -8.06 | 105 |
| 44 | MFI reversion · 1h | reversion | 94.99 | -5.01 | 75 | 28.0 | -10.82 | -1.89 | -16.99 | 120 |
| 45 | Ichimoku · 1h | trend | 94.92 | -5.08 | 33 | 15.2 | 8.38 | 1.17 | -15.84 | 125 |
| 46 | Max aggression: 1-day momentum | meta | 94.78 | -5.22 | 7 | 42.9 | -23.65 | -1.22 | -37.31 | 42 |
| 47 | Triple EMA stack · 1h | trend | 94.69 | -5.31 | 56 | 10.7 | -10.29 | -1.10 | -24.32 | 255 |
| 48 | Bollinger breakout · 1h | breakout | 94.59 | -5.41 | 50 | 24.0 | 7.47 | 1.12 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 6.64 | 1.74 | -6.49 | 199 |
| 50 | Opening range 30m | breakout | 94.00 | -6.00 | 98 | 21.4 | -17.56 | -5.46 | -17.83 | 572 |
| 51 | Volume breakout · 1h | breakout | 93.77 | -6.23 | 36 | 11.1 | 6.64 | 1.08 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.66 | -7.34 | 81 | 11.1 | -2.74 | -0.17 | -18.47 | 346 |
| 53 | Opening range 15m | breakout | 92.49 | -7.51 | 113 | 19.5 | -18.50 | -5.49 | -19.17 | 689 |
| 54 | Max aggression: 5-day momentum | meta | 92.19 | -7.81 | 5 | 40.0 | -19.11 | -1.63 | -29.56 | 29 |
| 55 | Donchian 20/10 · 1h | breakout | 91.38 | -8.62 | 40 | 15.0 | 2.85 | 0.56 | -16.18 | 223 |
| 56 | MACD zero-line · 1h | trend | 91.25 | -8.75 | 49 | 16.3 | -4.70 | -0.44 | -18.32 | 245 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.29 | -24.92 | -49.49 | 589 |
| 58 | VWAP momentum · 1h | momentum | 90.90 | -9.10 | 228 | 22.8 | -37.23 | -5.74 | -37.28 | 1269 |
| 59 | OBV trend · 1h | momentum | 90.63 | -9.37 | 107 | 12.1 | -12.83 | -1.43 | -26.73 | 337 |
| 60 | Heikin-Ashi · 1h | trend | 90.10 | -9.90 | 116 | 25.0 | -30.94 | -5.32 | -34.24 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.84 | -10.15 | 30 | 6.7 | -9.99 | -1.15 | -23.31 | 232 |
| 62 | ROC + volume · 1h | momentum | 87.34 | -12.66 | 107 | 15.9 | -9.13 | -1.09 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.68 | -14.32 | 222 | 32.0 | -71.08 | -19.75 | -71.44 | 1408 |
| 64 | Squeeze breakout | breakout | 77.45 | -22.55 | 250 | 15.6 | -62.30 | -18.99 | -62.33 | 1223 |
| 65 | VWAP reversion | reversion | 77.17 | -22.83 | 271 | 28.0 | -69.25 | -16.31 | -69.39 | 1384 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.81 | -17.80 | -73.81 | 1638 |
| 67 | Donchian 55/20 | breakout | 76.06 | -23.94 | 258 | 17.4 | -68.90 | -15.33 | -68.91 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.54 | -25.46 | 263 | 18.6 | -78.60 | -16.24 | -78.61 | 1480 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.08 | -19.59 | -65.08 | 915 |
| 70 | Z-score reversion | reversion | 71.24 | -28.76 | 353 | 27.8 | -85.06 | -25.35 | -85.06 | 2043 |
| 71 | MFI reversion | reversion | 69.98 | -30.02 | 350 | 20.9 | -87.10 | -30.77 | -87.10 | 2097 |
| 72 | Supertrend | trend | 69.51 | -30.49 | 353 | 20.1 | -87.17 | -22.48 | -87.17 | 1925 |
| 73 | Keltner breakout | breakout | 67.94 | -32.06 | 350 | 13.1 | -85.47 | -30.55 | -85.49 | 1885 |
| 74 | AI bee: Bizzy | ai | 67.54 | -32.46 | 606 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 66.89 | -33.11 | 317 | 8.8 | -82.25 | -24.92 | -82.26 | 1772 |
| 76 | AI bee: Boozy | ai | 66.05 | -33.95 | 217 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.33 | -35.67 | 401 | 9.2 | -89.73 | -37.54 | -89.73 | 2105 |
| 78 | MACD zero-line | trend | 63.17 | -36.83 | 454 | 15.4 | -91.56 | -31.23 | -91.56 | 2366 |
| 79 | Donchian 20/10 | breakout | 62.58 | -37.42 | 490 | 18.2 | -91.12 | -27.73 | -91.12 | 2666 |
| 80 | RSI momentum | momentum | 61.71 | -38.29 | 453 | 16.8 | -90.62 | -27.01 | -90.63 | 2380 |
| 81 | Triple EMA stack | trend | 60.17 | -39.83 | 505 | 15.2 | -93.38 | -32.68 | -93.38 | 2635 |
| 82 | Trend pullback | trend | 60.12 | -39.88 | 487 | 15.2 | -91.43 | -30.74 | -91.43 | 2346 |
| 83 | Bollinger breakout | breakout | 59.32 | -40.68 | 499 | 14.0 | -93.99 | -35.82 | -93.99 | 2820 |
| 84 | Stochastic reversion | reversion | 58.18 | -41.82 | 706 | 23.4 | -95.54 | -37.68 | -95.57 | 4040 |
| 85 | Bollinger reversion | reversion | 57.71 | -42.29 | 659 | 18.1 | -95.70 | -36.89 | -95.70 | 3680 |
| 86 | Consensus | meta | 57.26 | -42.74 | 483 | 9.7 | -94.73 | -27.32 | -94.73 | 2724 |
| 87 | EMA 9/21 cross | trend | 55.54 | -44.46 | 622 | 16.1 | -97.44 | -35.58 | -97.44 | 3553 |
| 88 | Connors RSI(2) | reversion | 53.83 | -46.17 | 676 | 20.3 | -96.58 | -35.52 | -96.58 | 3650 |
| 89 | OBV trend | momentum | 52.15 | -47.85 | 733 | 14.9 | -96.47 | -40.10 | -96.47 | 3604 |
| 90 | CCI reversion | reversion | 52.10 | -47.90 | 687 | 17.3 | -98.46 | -40.70 | -98.46 | 4692 |
| 91 | Candlestick reversal | reversion | 50.80 | -49.20 | 790 | 14.7 | -99.29 | -40.69 | -99.29 | 5625 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -32.15 | -98.71 | 5359 |
| 93 | Parabolic SAR | trend | 50.18 | -49.82 | 667 | 14.5 | -97.40 | -42.47 | -97.40 | 3680 |
| 94 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -47.97 | -99.73 | 6134 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -44.79 | -99.51 | 6096 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.74 | -99.90 | 8245 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T19:28 | AI bee: Bizzy | sell | AMZN | 9.73 | -0.02 | Jev: sell (sell p=0.68) after 11 min |
| 2026-10-06T19:27 | AI bee: Bizzy | buy | AAPL | 9.50 | — | Jev: buy (buy p=0.56) |
| 2026-10-06T19:25 | Consensus | buy | TSLA | 8.19 | — | rebalance up |
| 2026-10-06T19:25 | Consensus | sell | UPRO | 9.55 | -0.01 | target is flat |
| 2026-10-06T19:25 | MFI reversion | buy | UPRO | 3.88 | — | rebalance up |
| 2026-10-06T19:25 | MFI reversion | buy | TSLA | 3.88 | — | rebalance up |
| 2026-10-06T19:25 | MFI reversion | buy | SPY | 4.65 | — | rebalance up |
| 2026-10-06T19:25 | MFI reversion | buy | MSTR | 3.92 | — | rebalance up |
| 2026-10-06T19:25 | MFI reversion | buy | BITX | 3.88 | — | rebalance up |
| 2026-10-06T19:25 | MFI reversion | sell | IWM | 7.00 | -0.03 | stop-loss |
| 2026-10-06T19:25 | CCI reversion | buy | BTC-USD | 4.33 | — | entry signal |
| 2026-10-06T19:25 | CCI reversion | buy | BITX | 6.51 | — | entry signal |
| 2026-10-06T19:25 | Stochastic reversion | buy | SOL-USD | 3.41 | — | entry |
| 2026-10-06T19:25 | Stochastic reversion | buy | LABU | 3.88 | — | entry signal |
| 2026-10-06T19:25 | Stochastic reversion | sell | TNA | 3.63 | -0.03 | stop-loss |
| 2026-10-06T19:25 | Stochastic reversion | sell | IWM | 3.64 | -0.01 | stop-loss |
| 2026-10-06T19:25 | VWAP reversion | buy | TSLA | 8.24 | — | rebalance up |
| 2026-10-06T19:25 | VWAP reversion | buy | NVDA | 6.43 | — | rebalance up |
| 2026-10-06T19:25 | VWAP reversion | buy | MSTR | 8.27 | — | rebalance up |
| 2026-10-06T19:25 | VWAP reversion | buy | BITX | 8.21 | — | rebalance up |
| 2026-10-06T19:25 | VWAP reversion | sell | TNA | 11.00 | -0.06 | stop-loss |
| 2026-10-06T19:25 | VWAP reversion | sell | IWM | 9.20 | -0.02 | stop-loss |
| 2026-10-06T19:25 | VWAP reversion | sell | COIN | 9.14 | -0.07 | stop-loss |
| 2026-10-06T19:25 | Bollinger reversion | buy | XRP-USD | 8.07 | — | rebalance up |
| 2026-10-06T19:25 | Bollinger reversion | buy | SOXL | 8.03 | — | rebalance up |
| 2026-10-06T19:25 | Bollinger reversion | buy | NVDA | 8.01 | — | rebalance up |
| 2026-10-06T19:25 | Bollinger reversion | sell | TNA | 6.41 | -0.03 | stop-loss |
| 2026-10-06T19:25 | Bollinger reversion | sell | IWM | 6.43 | -0.01 | stop-loss |
| 2026-10-06T19:25 | Bollinger reversion | sell | ETH-USD | 6.39 | -0.05 | stop-loss |
| 2026-10-06T19:25 | Bollinger reversion | sell | COIN | 6.42 | -0.05 | stop-loss |
| 2026-10-06T19:25 | Connors RSI(2) | buy | SOL-USD | 2.70 | — | rebalance up |
| 2026-10-06T19:25 | Connors RSI(2) | buy | NVDA | 2.69 | — | rebalance up |
| 2026-10-06T19:25 | Connors RSI(2) | buy | COIN | 2.70 | — | rebalance up |
| 2026-10-06T19:25 | Connors RSI(2) | sell | TSLA | 10.77 | 0.00 | exit signal |
| 2026-10-06T19:25 | Connors RSI(2) | sell | GOOGL | 10.77 | -0.01 | exit signal |
| 2026-10-06T19:25 | Candlestick reversal | buy | TSLA | 5.08 | — | entry |
| 2026-10-06T19:25 | Candlestick reversal | buy | LABU | 3.11 | — | rebalance up |
| 2026-10-06T19:25 | Candlestick reversal | sell | UPRO | 4.63 | -0.01 | target is flat |
| 2026-10-06T19:25 | Candlestick reversal | sell | BITX | 4.62 | -0.01 | exit signal |
| 2026-10-06T19:25 | OBV trend | buy | TQQQ | 7.44 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 19:29:05.000117+00:00 -> 2026-10-06 19:39:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
