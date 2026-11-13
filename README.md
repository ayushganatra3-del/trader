# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T00:40:05.000140+00:00 · 57554 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.55 (-14.45%)

Closed trades 190, win rate 35.3%, fees £5.54, max drawdown -14.98%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 585 decisions in 117 calls, $0.0082 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T00:40 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-13T00:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T00:40 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.59 | +2.90% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.02 | 17.02 | 0 | — | 14.68 | 4.88 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.29 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.97 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.98 | 3.98 | 0 | — | 6.13 | 1.68 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.31 | 2.87 | -3.96 | 88 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.58 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.51 | -1.49 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.87 | -2.13 | 1 | 0.0 | -2.09 | -1.41 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -1.25 | -0.40 | -8.69 | 172 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.05 | -3.95 | 0 | — | -4.19 | -1.06 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.30 | -4.70 | 143 | 47.6 | -12.92 | -3.33 | -13.44 | 156 |
| 16 | Copy: Insider buying | copy | 95.00 | -5.00 | 43 | 39.5 | -6.55 | -1.27 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.07 | -5.93 | 0 | — | -4.23 | -1.11 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.02 | -5.99 | 26 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.19 | -6.81 | 1 | 0.0 | -7.08 | -1.55 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.50 | -9.09 | 21 |
| 21 | Trend pullback · 1h | trend | 91.75 | -8.25 | 110 | 22.7 | -13.08 | -4.51 | -17.58 | 73 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 85.98 | -14.02 | 171 | 27.5 | -14.01 | -2.95 | -21.80 | 220 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.12 | -3.17 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -14.75 | -7.30 | -15.21 | 215 |
| 26 | Daily: Bullish score | daily | 84.73 | -15.27 | 16 | 18.8 | -11.13 | -1.78 | -19.56 | 15 |
| 27 | Donchian 55/20 · 1h | breakout | 83.95 | -16.05 | 73 | 13.7 | -22.57 | -4.70 | -29.68 | 94 |
| 28 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.53 | -4.89 | -18.70 | 104 |
| 29 | Hold BTC | benchmark | 83.53 | -16.47 | 1 | 0.0 | -8.58 | -1.19 | -18.82 | 1 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.33 | -17.67 | 2 | 0.0 | -8.05 | -0.87 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.66 | -18.34 | 114 | 23.7 | -15.25 | -3.01 | -25.14 | 169 |
| 32 | Max aggression: 5-day momentum | meta | 81.45 | -18.55 | 20 | 45.0 | -32.68 | -1.98 | -45.81 | 22 |
| 33 | ADX DI cross · 1h | trend | 81.41 | -18.59 | 191 | 19.4 | -19.89 | -3.01 | -29.51 | 270 |
| 34 | Connors RSI(2) · 1h | reversion | 80.94 | -19.06 | 210 | 40.5 | -17.91 | -6.24 | -18.41 | 116 |
| 35 | Volume breakout · 1h | breakout | 80.15 | -19.85 | 159 | 28.3 | -13.34 | -3.06 | -22.12 | 92 |
| 36 | MFI reversion · 1h | reversion | 79.77 | -20.23 | 385 | 35.8 | -18.76 | -2.40 | -23.40 | 162 |
| 37 | Stochastic reversion · 1h | reversion | 79.51 | -20.49 | 297 | 47.5 | -26.88 | -3.95 | -27.43 | 390 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.67 | -21.36 | 715 |
| 39 | Heikin-Ashi · 1h | trend | 77.49 | -22.51 | 435 | 24.6 | -36.03 | -6.66 | -38.20 | 657 |
| 40 | MACD cross · 1h | trend | 77.15 | -22.85 | 376 | 23.1 | -27.61 | -4.06 | -38.65 | 473 |
| 41 | Bollinger breakout · 1h | breakout | 76.61 | -23.39 | 179 | 22.3 | -20.87 | -4.27 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.33 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.78 | -24.22 | 168 | 17.9 | -21.64 | -4.19 | -30.99 | 204 |
| 44 | Supertrend · 1h | trend | 75.55 | -24.45 | 172 | 14.0 | -27.75 | -4.72 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.16 | -8.78 | -31.80 | 116 |
| 46 | RSI momentum · 1h | momentum | 75.06 | -24.94 | 162 | 13.6 | -24.08 | -3.69 | -36.35 | 213 |
| 47 | EMA 20/50 cross · 1h | trend | 74.72 | -25.28 | 105 | 10.5 | -27.42 | -4.58 | -38.62 | 124 |
| 48 | Daily: Momentum burst | daily | 74.14 | -25.86 | 27 | 11.1 | -30.29 | -4.05 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.44 | -26.56 | 147 | 14.3 | -26.18 | -4.24 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.91 | -27.09 | 390 | 28.7 | -29.72 | -5.40 | -38.37 | 376 |
| 51 | Donchian 20/10 · 1h | breakout | 72.17 | -27.83 | 145 | 19.3 | -27.07 | -4.85 | -35.90 | 209 |
| 52 | Bollinger reversion · 1h | reversion | 72.07 | -27.93 | 292 | 41.4 | -31.98 | -4.92 | -35.72 | 378 |
| 53 | CCI reversion · 1h | reversion | 71.94 | -28.06 | 340 | 44.1 | -37.12 | -5.80 | -37.20 | 458 |
| 54 | OBV trend · 1h | momentum | 71.63 | -28.36 | 290 | 19.3 | -27.36 | -4.71 | -36.64 | 276 |
| 55 | Z-score reversion · 1h | reversion | 67.80 | -32.20 | 199 | 38.2 | -28.05 | -3.92 | -29.08 | 231 |
| 56 | Williams %R · 1h | reversion | 67.71 | -32.29 | 372 | 43.8 | -42.17 | -6.83 | -42.43 | 529 |
| 57 | EMA 9/21 cross · 1h | trend | 67.27 | -32.73 | 259 | 10.0 | -35.10 | -7.12 | -41.97 | 329 |
| 58 | Agent (ML meta-label) | meta | 66.15 | -33.85 | 1820 | 24.8 | -19.45 | -2.84 | -21.67 | 354 |
| 59 | VWAP momentum · 1h | momentum | 66.12 | -33.88 | 896 | 22.3 | -51.32 | -10.40 | -51.82 | 1220 |
| 60 | RSI(14) reversion · 1h | reversion | 64.13 | -35.87 | 180 | 32.2 | -35.43 | -5.15 | -35.94 | 233 |
| 61 | Candlestick reversal · 1h | reversion | 62.50 | -37.50 | 471 | 28.5 | -44.17 | -8.05 | -44.20 | 589 |
| 62 | Three white soldiers | momentum | 58.39 | -41.61 | 539 | 14.5 | -49.71 | -22.15 | -49.71 | 663 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -42.89 | -99.01 | 5264 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.93 | -25.19 | -79.93 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -44.40 | -93.79 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.31 | -30.96 | -89.40 | 1914 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -40.09 | -91.28 | 2332 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.81 | -30.26 | -89.85 | 2197 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -50.58 | -97.92 | 3481 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -53.85 | -96.29 | 3432 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.56 | -31.82 | -93.56 | 2329 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.35 | -34.11 | -83.35 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -52.46 | -99.57 | 5997 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.31 | -42.44 | -92.31 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.34 | -35.27 | -95.34 | 3465 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.82 | -69.27 | -99.82 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.34 | -41.77 | -92.34 | 2265 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.39 | -24.92 | -75.39 | 1633 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -57.95 | -97.68 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -58.54 | -98.87 | 4917 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.92 | -26.92 | -68.92 | 1236 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.85 | -55.45 | -94.85 | 2788 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.12 | -37.99 | -85.12 | 1783 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -67.10 | -99.65 | 6347 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.96 | -31.48 | -89.98 | 2300 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.84 | -19.54 | -78.14 | 1761 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.83 | -35.86 | -90.83 | 2176 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.84 | -48.96 | -96.84 | 3854 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -53.87 | -89.21 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.27 | -29.54 | -66.27 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.56 | -22.85 | -71.58 | 1256 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.90 | -18.46 | -79.20 | 1703 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -47.10 | -97.31 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -90.13 | -99.93 | 8368 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T00:20 | Three white soldiers | sell | XRP-USD | 14.54 | -0.12 | exit signal |
| 2026-11-13T00:10 | Three white soldiers | sell | BTC-USD | 14.54 | -0.11 | exit signal |
| 2026-11-13T00:00 | CCI reversion · 1h | buy | XRP-USD | 7.23 | — | entry |
| 2026-11-13T00:00 | CCI reversion · 1h | buy | SOL-USD | 7.23 | — | entry |
| 2026-11-13T00:00 | CCI reversion · 1h | buy | ETH-USD | 7.23 | — | entry |
| 2026-11-13T00:00 | CCI reversion · 1h | buy | DOGE-USD | 7.23 | — | entry |
| 2026-11-13T00:00 | CCI reversion · 1h | buy | BTC-USD | 7.23 | — | entry |
| 2026-11-13T00:00 | Williams %R · 1h | buy | XRP-USD | 4.85 | — | entry |
| 2026-11-13T00:00 | Williams %R · 1h | buy | SOL-USD | 4.85 | — | entry |
| 2026-11-13T00:00 | Williams %R · 1h | buy | ETH-USD | 4.85 | — | entry |
| 2026-11-13T00:00 | Williams %R · 1h | buy | DOGE-USD | 4.85 | — | entry |
| 2026-11-13T00:00 | Williams %R · 1h | buy | BTC-USD | 4.85 | — | entry |
| 2026-11-13T00:00 | Bollinger reversion · 1h | buy | BTC-USD | 9.04 | — | entry |
| 2026-11-13T00:00 | Bollinger reversion · 1h | sell | XRP-USD | 9.23 | 0.08 | exit signal |
| 2026-11-13T00:00 | Bollinger reversion · 1h | sell | DOGE-USD | 9.18 | 0.08 | exit signal |
| 2026-11-13T00:00 | RSI(14) reversion · 1h | buy | SOL-USD | 8.04 | — | entry |
| 2026-11-13T00:00 | RSI(14) reversion · 1h | buy | ETH-USD | 8.04 | — | entry |
| 2026-11-13T00:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 8.04 | — | entry |
| 2026-11-13T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.68 | — | entry signal |
| 2026-11-13T00:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.70 | — | entry signal |
| 2026-11-13T00:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.45 | — | entry signal |
| 2026-11-13T00:00 | ADX DI cross · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-11-12T23:55 | Three white soldiers | buy | XRP-USD | 14.65 | — | entry signal |
| 2026-11-12T23:55 | Three white soldiers | buy | BTC-USD | 14.65 | — | entry signal |
| 2026-11-12T23:00 | Candlestick reversal · 1h | sell | ETH-USD | 5.71 | 0.02 | exit signal |
| 2026-11-12T23:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.66 | -0.06 | exit signal |
| 2026-11-12T23:00 | VWAP momentum · 1h | buy | XRP-USD | 4.04 | — | entry signal |
| 2026-11-12T22:00 | VWAP momentum · 1h | buy | DOGE-USD | 8.27 | — | entry signal |
| 2026-11-12T22:00 | VWAP momentum · 1h | sell | XRP-USD | 8.22 | -0.05 | exit signal |
| 2026-11-12T22:00 | Heikin-Ashi · 1h | buy | XRP-USD | 19.44 | — | entry signal |
| 2026-11-12T21:42 | Agent (ML meta-label) | sell | ETH-USD | 4.71 | -0.02 | selected signal exited |
| 2026-11-12T21:20 | Agent (ML meta-label) | buy | ETH-USD | 4.73 | — | entry |
| 2026-11-12T21:00 | VWAP reversion · 1h | sell | XRP-USD | 23.96 | 0.07 | exit signal |
| 2026-11-12T21:00 | VWAP momentum · 1h | buy | XRP-USD | 8.28 | — | entry signal |
| 2026-11-12T21:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.63 | -0.06 | exit signal |
| 2026-11-12T21:00 | MACD cross · 1h | buy | DOGE-USD | 9.64 | — | entry signal |
| 2026-11-12T20:55 | Agent (rotation) | sell | TQQQ | 65.29 | -0.77 | selected signal exited |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | UPRO | 24.86 | 0.04 | target is flat |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | TECL | 25.49 | 0.66 | target is flat |
| 2026-11-12T20:55 | Day trade: Stocks in Play ORB | sell | NVDA | 25.88 | 0.95 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 00:40:05.000140+00:00 -> 2026-11-13 00:50:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
