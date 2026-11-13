# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T13:10:05.000163+00:00 · 58223 ticks

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
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 10620 decisions in 2124 calls, $0.1487 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T13:10 | 3 / 1 / 1 | cash |  |
| Breezy | 2026-11-13T13:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-13T13:10 | 2 / 3 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.03 | 17.03 | 0 | — | 14.68 | 4.92 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.62 | 12.62 | 22 | 68.2 | 16.23 | 3.32 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.73 | 11.73 | 34 | 29.4 | 20.04 | 2.99 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.99 | 3.99 | 0 | — | 6.13 | 1.70 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.73 | 0.73 | 140 | 35.0 | 7.31 | 2.89 | -3.96 | 88 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.58 | 1.87 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 98.52 | -1.48 | 0 | — | -0.22 | 0.00 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.88 | -2.12 | 1 | 0.0 | -2.09 | -1.42 | -5.83 | 2 |
| 13 | Agent (rotation) | meta | 97.84 | -2.16 | 191 | 30.4 | -0.60 | -0.16 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.06 | -3.94 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Copy: Insider buying | copy | 95.01 | -4.99 | 43 | 39.5 | -4.17 | -0.75 | -14.81 | 66 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.08 | -5.92 | 0 | — | -4.23 | -1.12 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 93.20 | -6.80 | 1 | 0.0 | -7.08 | -1.56 | -16.91 | 2 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 21 | Trend pullback · 1h | trend | 91.76 | -8.24 | 110 | 22.7 | -13.31 | -4.55 | -17.58 | 72 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 23 | Parabolic SAR · 1h | trend | 85.99 | -14.01 | 171 | 27.5 | -14.92 | -3.21 | -21.80 | 217 |
| 24 | Opening range 30m | breakout | 85.89 | -14.11 | 433 | 33.3 | -10.12 | -3.20 | -14.11 | 601 |
| 25 | Agent | meta | 85.55 | -14.45 | 190 | 35.3 | -15.04 | -7.57 | -15.21 | 210 |
| 26 | Daily: Bullish score | daily | 84.73 | -15.27 | 16 | 18.8 | -11.13 | -1.80 | -19.56 | 15 |
| 27 | Donchian 55/20 · 1h | breakout | 83.96 | -16.04 | 73 | 13.7 | -22.11 | -4.64 | -29.68 | 92 |
| 28 | Agent (aggressive) | meta | 83.73 | -16.27 | 92 | 33.7 | -17.67 | -4.98 | -18.51 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 82.34 | -17.66 | 2 | 0.0 | -8.05 | -0.88 | -24.16 | 1 |
| 30 | Keltner breakout · 1h | breakout | 81.67 | -18.33 | 114 | 23.7 | -15.25 | -3.04 | -25.14 | 169 |
| 31 | Hold BTC | benchmark | 81.54 | -18.46 | 1 | 0.0 | -10.87 | -1.50 | -22.00 | 1 |
| 32 | Max aggression: 5-day momentum | meta | 81.45 | -18.55 | 20 | 45.0 | -32.68 | -1.99 | -45.81 | 22 |
| 33 | ADX DI cross · 1h | trend | 81.42 | -18.58 | 192 | 19.3 | -20.51 | -3.15 | -29.51 | 272 |
| 34 | Connors RSI(2) · 1h | reversion | 80.95 | -19.05 | 210 | 40.5 | -17.80 | -6.24 | -18.30 | 114 |
| 35 | Volume breakout · 1h | breakout | 80.15 | -19.84 | 159 | 28.3 | -13.17 | -3.05 | -22.12 | 90 |
| 36 | Stochastic reversion · 1h | reversion | 79.44 | -20.55 | 298 | 47.3 | -26.35 | -3.88 | -27.61 | 390 |
| 37 | MFI reversion · 1h | reversion | 78.84 | -21.16 | 390 | 35.4 | -20.05 | -2.61 | -23.48 | 162 |
| 38 | Opening range 15m | breakout | 78.23 | -21.77 | 524 | 31.3 | -17.52 | -4.71 | -21.36 | 715 |
| 39 | MACD cross · 1h | trend | 76.75 | -23.25 | 377 | 23.1 | -27.57 | -4.10 | -38.65 | 471 |
| 40 | Heikin-Ashi · 1h | trend | 76.73 | -23.27 | 438 | 24.4 | -36.50 | -6.83 | -38.20 | 660 |
| 41 | Bollinger breakout · 1h | breakout | 76.62 | -23.38 | 179 | 22.3 | -20.87 | -4.31 | -29.92 | 239 |
| 42 | Max aggression: 1-day momentum | meta | 76.00 | -24.00 | 29 | 27.6 | -15.60 | -0.34 | -57.50 | 40 |
| 43 | MACD zero-line · 1h | trend | 75.78 | -24.22 | 168 | 17.9 | -21.43 | -4.17 | -30.99 | 203 |
| 44 | Supertrend · 1h | trend | 75.56 | -24.45 | 172 | 14.0 | -27.80 | -4.76 | -36.51 | 212 |
| 45 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 46 | RSI momentum · 1h | momentum | 75.07 | -24.93 | 162 | 13.6 | -24.10 | -3.73 | -36.35 | 210 |
| 47 | EMA 20/50 cross · 1h | trend | 74.73 | -25.27 | 105 | 10.5 | -26.75 | -4.53 | -38.62 | 121 |
| 48 | Daily: Momentum burst | daily | 74.14 | -25.86 | 27 | 11.1 | -30.29 | -4.08 | -36.97 | 33 |
| 49 | Triple EMA stack · 1h | trend | 73.44 | -26.55 | 147 | 14.3 | -27.13 | -4.46 | -37.19 | 205 |
| 50 | ROC + volume · 1h | momentum | 72.92 | -27.08 | 390 | 28.7 | -29.63 | -5.42 | -38.37 | 374 |
| 51 | Donchian 20/10 · 1h | breakout | 72.18 | -27.82 | 145 | 19.3 | -27.07 | -4.89 | -35.90 | 209 |
| 52 | Bollinger reversion · 1h | reversion | 71.99 | -28.01 | 298 | 41.6 | -32.22 | -5.01 | -35.72 | 381 |
| 53 | OBV trend · 1h | momentum | 71.64 | -28.36 | 290 | 19.3 | -27.76 | -4.85 | -36.64 | 275 |
| 54 | CCI reversion · 1h | reversion | 71.28 | -28.72 | 345 | 43.5 | -37.53 | -5.93 | -37.93 | 461 |
| 55 | Williams %R · 1h | reversion | 67.48 | -32.52 | 377 | 43.2 | -42.49 | -6.96 | -42.89 | 533 |
| 56 | EMA 9/21 cross · 1h | trend | 67.28 | -32.72 | 259 | 10.0 | -35.13 | -7.20 | -41.97 | 329 |
| 57 | Z-score reversion · 1h | reversion | 66.31 | -33.69 | 203 | 37.4 | -29.57 | -4.19 | -29.97 | 236 |
| 58 | Agent (ML meta-label) | meta | 66.16 | -33.84 | 1820 | 24.8 | -14.63 | -2.11 | -23.69 | 343 |
| 59 | VWAP momentum · 1h | momentum | 65.94 | -34.06 | 899 | 22.2 | -50.51 | -10.30 | -51.42 | 1216 |
| 60 | RSI(14) reversion · 1h | reversion | 63.71 | -36.29 | 183 | 31.7 | -36.12 | -5.33 | -36.65 | 237 |
| 61 | Candlestick reversal · 1h | reversion | 62.35 | -37.65 | 477 | 28.3 | -44.11 | -8.10 | -44.66 | 592 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.92 | -98.99 | 5256 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.78 | -25.38 | -79.89 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.75 | -45.67 | -93.77 | 2527 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -31.32 | -89.31 | 1916 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.20 | -40.62 | -91.22 | 2331 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.67 | -30.71 | -89.71 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -51.76 | -97.88 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -55.90 | -96.22 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.74 | -33.37 | -93.74 | 2345 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -34.43 | -83.16 | 1656 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.12 | -99.59 | 6011 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -42.66 | -92.25 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.31 | -36.28 | -95.31 | 3460 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -71.29 | -99.81 | 6143 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.24 | -42.25 | -92.25 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.60 | -25.63 | -75.61 | 1631 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -59.39 | -97.62 | 3505 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -63.63 | -98.90 | 4925 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.52 | -26.71 | -68.57 | 1233 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -55.45 | -94.72 | 2780 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.04 | -39.04 | -85.04 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -75.57 | -99.66 | 6350 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.19 | -32.57 | -90.20 | 2308 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.85 | -20.15 | -78.96 | 1781 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.78 | -36.44 | -90.82 | 2173 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.99 | -52.75 | -96.99 | 3867 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -57.42 | -89.32 | 2133 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.99 | -29.62 | -66.04 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.30 | -22.91 | -71.35 | 1252 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.16 | -19.28 | -80.39 | 1730 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.37 | -50.34 | -97.37 | 4311 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -106.82 | -99.93 | 8367 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T13:00 | Bollinger reversion · 1h | sell | DOGE-USD | 10.43 | 0.19 | exit signal |
| 2026-11-13T13:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.78 | — | rebalance up |
| 2026-11-13T13:00 | Candlestick reversal · 1h | sell | XRP-USD | 6.90 | 0.01 | exit signal |
| 2026-11-13T12:00 | Bollinger reversion · 1h | sell | SOL-USD | 8.02 | 0.04 | exit signal |
| 2026-11-13T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 18.83 | — | entry signal |
| 2026-11-13T12:00 | Heikin-Ashi · 1h | buy | ETH-USD | 19.22 | — | entry signal |
| 2026-11-13T11:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.23 | — | entry signal |
| 2026-11-13T11:00 | Heikin-Ashi · 1h | sell | XRP-USD | 19.07 | -0.20 | exit signal |
| 2026-11-13T10:00 | MFI reversion · 1h | buy | BTC-USD | 13.14 | — | entry signal |
| 2026-11-13T10:00 | CCI reversion · 1h | buy | ETH-USD | 7.12 | — | entry signal |
| 2026-11-13T10:00 | CCI reversion · 1h | buy | BTC-USD | 7.12 | — | entry signal |
| 2026-11-13T10:00 | CCI reversion · 1h | sell | XRP-USD | 4.74 | -0.01 | rebalance down |
| 2026-11-13T10:00 | Z-score reversion · 1h | buy | ETH-USD | 8.40 | — | entry signal |
| 2026-11-13T10:00 | Z-score reversion · 1h | buy | BTC-USD | 11.04 | — | entry signal |
| 2026-11-13T10:00 | Z-score reversion · 1h | sell | XRP-USD | 5.54 | -0.01 | rebalance down |
| 2026-11-13T10:00 | Z-score reversion · 1h | sell | SOL-USD | 5.44 | -0.04 | rebalance down |
| 2026-11-13T10:00 | Z-score reversion · 1h | sell | DOGE-USD | 5.53 | -0.01 | rebalance down |
| 2026-11-13T10:00 | RSI(14) reversion · 1h | buy | ETH-USD | 6.36 | — | entry signal |
| 2026-11-13T10:00 | RSI(14) reversion · 1h | buy | BTC-USD | 6.36 | — | entry signal |
| 2026-11-13T10:00 | RSI(14) reversion · 1h | sell | XRP-USD | 4.35 | 0.05 | rebalance down |
| 2026-11-13T10:00 | Candlestick reversal · 1h | buy | ETH-USD | 2.44 | — | entry signal |
| 2026-11-13T10:00 | Candlestick reversal · 1h | buy | BTC-USD | 5.67 | — | entry signal |
| 2026-11-13T09:00 | Bollinger reversion · 1h | buy | SOL-USD | 6.77 | — | rebalance up |
| 2026-11-13T09:00 | Bollinger reversion · 1h | sell | XRP-USD | 10.33 | 0.10 | exit signal |
| 2026-11-13T09:00 | Heikin-Ashi · 1h | buy | XRP-USD | 19.27 | — | entry signal |
| 2026-11-13T09:00 | MACD cross · 1h | buy | XRP-USD | 9.69 | — | entry signal |
| 2026-11-13T08:00 | CCI reversion · 1h | buy | SOL-USD | 8.89 | — | entry signal |
| 2026-11-13T08:00 | CCI reversion · 1h | buy | DOGE-USD | 8.89 | — | entry signal |
| 2026-11-13T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.84 | — | entry signal |
| 2026-11-13T07:41 | Three white soldiers | sell | SOL-USD | 14.69 | 0.09 | exit signal |
| 2026-11-13T07:30 | Three white soldiers | sell | BTC-USD | 14.55 | -0.05 | exit signal |
| 2026-11-13T07:00 | CCI reversion · 1h | buy | XRP-USD | 11.85 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | SOL-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | ETH-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | DOGE-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Williams %R · 1h | buy | BTC-USD | 4.82 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | XRP-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | SOL-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Z-score reversion · 1h | buy | DOGE-USD | 16.57 | — | entry signal |
| 2026-11-13T07:00 | Bollinger reversion · 1h | buy | SOL-USD | 1.22 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 13:10:05.000163+00:00 -> 2026-11-13 13:20:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
