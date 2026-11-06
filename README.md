# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-06T02:25:05.000123+00:00 · 49139 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £88.46 (-11.54%)

Closed trades 148, win rate 37.2%, fees £4.17, max drawdown -11.95%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-06 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-05)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 38.26 · VIX 28.18 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, AMZN 5.2, AAPL 5.0, MSFT 4.9, TSLA 1.2, MSTR 1.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 1785 decisions in 357 calls, $0.0249 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-06T02:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-06T02:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-06T02:25 | 4 / 1 / 0 | ETH-USD 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| OBV trend | AMZN | 2.23 | +2.74% | 6 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |
| VWAP reversion | COIN | 1.83 | +4.26% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| MFI reversion | SQQQ | 1.81 | +4.81% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 19 | 68.4 | 14.68 | 3.16 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 111.62 | 11.62 | 0 | — | 13.22 | 4.50 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 107.82 | 7.82 | 29 | 27.6 | 16.51 | 2.72 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 29 | 44.8 | 2.05 | 0.61 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.23 | -0.77 | 0 | — | 2.97 | 0.93 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.19 | -1.81 | 111 | 44.1 | -13.63 | -3.31 | -14.24 | 149 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.77 | -2.23 | 117 | 35.0 | 4.93 | 2.51 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.31 | -4.69 | 20 | 20.0 | -5.72 | -5.40 | -6.50 | 21 |
| 12 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.06 | 0.10 | -9.18 | 218 |
| 13 | Agent (rotation) | meta | 95.11 | -4.89 | 175 | 28.0 | -7.17 | -4.37 | -10.36 | 173 |
| 14 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 15 | Hold SPY | benchmark | 93.82 | -6.17 | 0 | — | -4.45 | -1.64 | -6.18 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 92.31 | -7.68 | 7 | 42.9 | -13.09 | -1.39 | -18.69 | 8 |
| 17 | Trend pullback · 1h | trend | 92.09 | -7.91 | 105 | 22.9 | -15.25 | -5.48 | -17.86 | 81 |
| 18 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 90.66 | -9.34 | 0 | — | -8.33 | -2.52 | -9.25 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.00 | -10.00 | 0 | — | -7.33 | -2.17 | -10.64 | 1 |
| 21 | Opening range 30m | breakout | 89.90 | -10.10 | 366 | 33.1 | -15.95 | -5.09 | -17.56 | 579 |
| 22 | Daily: Bullish score | daily | 89.03 | -10.97 | 14 | 21.4 | -4.51 | -0.57 | -16.58 | 14 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.53 | -3.65 | -14.68 | 86 |
| 24 | Agent | meta | 88.46 | -11.54 | 148 | 37.2 | -14.20 | -7.57 | -14.60 | 211 |
| 25 | Hold BTC | benchmark | 88.28 | -11.72 | 1 | 0.0 | -4.66 | -0.57 | -13.74 | 1 |
| 26 | Parabolic SAR · 1h | trend | 87.58 | -12.42 | 166 | 27.1 | -14.67 | -3.22 | -20.02 | 241 |
| 27 | Donchian 55/20 · 1h | breakout | 86.63 | -13.37 | 71 | 14.1 | -12.50 | -2.52 | -19.94 | 104 |
| 28 | Copy: Insider buying | copy | 86.43 | -13.57 | 40 | 37.5 | -25.08 | -4.95 | -26.04 | 65 |
| 29 | Max aggression: 5-day momentum | meta | 85.13 | -14.87 | 17 | 47.1 | -30.71 | -1.88 | -37.55 | 24 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.57 | -5.53 | -19.02 | 99 |
| 31 | Opening range 15m | breakout | 83.67 | -16.33 | 446 | 30.7 | -19.82 | -5.84 | -21.31 | 705 |
| 32 | Volume breakout · 1h | breakout | 82.74 | -17.26 | 144 | 27.8 | -16.20 | -3.64 | -21.39 | 103 |
| 33 | Keltner breakout · 1h | breakout | 81.99 | -18.01 | 106 | 23.6 | -21.55 | -4.42 | -24.41 | 175 |
| 34 | Stochastic reversion · 1h | reversion | 81.59 | -18.41 | 255 | 46.7 | -28.48 | -4.42 | -29.24 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 80.64 | -19.36 | 203 | 39.9 | -20.51 | -6.77 | -21.05 | 129 |
| 36 | Copy: Cathie Wood (ARKK) | copy | 80.06 | -19.94 | 2 | 0.0 | -14.78 | -2.03 | -24.16 | 1 |
| 37 | ADX DI cross · 1h | trend | 79.76 | -20.23 | 171 | 18.1 | -24.29 | -4.03 | -26.36 | 264 |
| 38 | Bollinger breakout · 1h | breakout | 79.18 | -20.82 | 165 | 23.6 | -22.56 | -4.67 | -26.52 | 247 |
| 39 | MFI reversion · 1h | reversion | 79.06 | -20.95 | 328 | 33.8 | -18.86 | -2.69 | -19.96 | 152 |
| 40 | Ichimoku · 1h | trend | 78.71 | -21.29 | 94 | 14.9 | -22.37 | -4.53 | -28.82 | 125 |
| 41 | CCI reversion · 1h | reversion | 77.48 | -22.52 | 284 | 45.8 | -29.28 | -4.72 | -30.63 | 451 |
| 42 | Heikin-Ashi · 1h | trend | 77.12 | -22.88 | 385 | 23.1 | -43.20 | -9.08 | -43.91 | 673 |
| 43 | EMA 20/50 cross · 1h | trend | 76.57 | -23.43 | 102 | 10.8 | -22.75 | -4.07 | -30.17 | 131 |
| 44 | Triple EMA stack · 1h | trend | 75.04 | -24.96 | 142 | 14.8 | -29.58 | -6.19 | -33.06 | 207 |
| 45 | MACD zero-line · 1h | trend | 74.77 | -25.23 | 155 | 16.8 | -26.31 | -5.43 | -29.20 | 211 |
| 46 | RSI momentum · 1h | momentum | 73.98 | -26.02 | 158 | 12.7 | -27.86 | -5.27 | -32.33 | 220 |
| 47 | Supertrend · 1h | trend | 73.89 | -26.11 | 166 | 13.3 | -29.83 | -5.14 | -34.26 | 217 |
| 48 | MACD cross · 1h | trend | 73.30 | -26.70 | 334 | 23.1 | -36.11 | -6.35 | -38.81 | 472 |
| 49 | Z-score reversion · 1h | reversion | 73.14 | -26.86 | 159 | 35.8 | -28.03 | -4.33 | -28.35 | 225 |
| 50 | Donchian 20/10 · 1h | breakout | 72.39 | -27.61 | 140 | 20.0 | -29.75 | -5.46 | -34.25 | 214 |
| 51 | Daily: Momentum burst | daily | 72.30 | -27.70 | 26 | 11.5 | -35.53 | -4.93 | -37.46 | 30 |
| 52 | Bollinger reversion · 1h | reversion | 72.09 | -27.91 | 244 | 38.9 | -34.01 | -6.24 | -34.52 | 375 |
| 53 | Williams %R · 1h | reversion | 71.90 | -28.10 | 310 | 44.8 | -39.29 | -6.54 | -39.57 | 527 |
| 54 | ROC + volume · 1h | momentum | 71.59 | -28.41 | 344 | 25.6 | -36.68 | -7.13 | -37.60 | 383 |
| 55 | OBV trend · 1h | momentum | 71.29 | -28.71 | 266 | 17.3 | -32.79 | -6.93 | -33.98 | 296 |
| 56 | VWAP momentum · 1h | momentum | 68.35 | -31.65 | 758 | 22.3 | -55.32 | -12.13 | -56.28 | 1216 |
| 57 | EMA 9/21 cross · 1h | trend | 68.00 | -32.00 | 241 | 10.0 | -39.20 | -8.00 | -39.91 | 335 |
| 58 | RSI(14) reversion · 1h | reversion | 66.36 | -33.64 | 142 | 27.5 | -28.01 | -4.33 | -30.81 | 204 |
| 59 | Three white soldiers | momentum | 66.21 | -33.79 | 453 | 16.1 | -47.97 | -22.18 | -47.97 | 640 |
| 60 | Candlestick reversal · 1h | reversion | 65.06 | -34.94 | 395 | 28.6 | -38.85 | -7.17 | -39.20 | 563 |
| 61 | Agent (ML meta-label) | meta | 65.06 | -34.94 | 1508 | 22.3 | -9.45 | -1.35 | -19.46 | 332 |
| 62 | Max aggression: 1-day momentum | meta | 62.20 | -37.80 | 26 | 26.9 | -41.38 | -2.54 | -54.67 | 41 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -44.65 | -98.89 | 5125 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.09 | -25.32 | -80.14 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.24 | -46.18 | -93.25 | 2492 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.03 | -30.78 | -89.09 | 1897 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.59 | -38.64 | -90.67 | 2286 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.46 | -31.99 | -90.54 | 2211 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -52.03 | -97.64 | 3434 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -59.63 | -96.16 | 3359 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -32.15 | -93.58 | 2419 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.60 | -35.74 | -81.71 | 1631 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -51.10 | -99.51 | 5936 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.53 | -42.84 | -92.54 | 2584 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.84 | -37.55 | -95.86 | 3422 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -65.16 | -99.79 | 6115 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.60 | -42.60 | -91.61 | 2246 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.70 | -74.99 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -60.06 | -97.66 | 3488 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.76 | -56.95 | -98.76 | 4838 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.38 | -28.47 | -70.08 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.47 | -52.81 | -94.47 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.78 | -37.07 | -84.79 | 1775 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -67.19 | -99.64 | 6313 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.86 | -29.78 | -88.97 | 2259 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.68 | -19.41 | -77.97 | 1737 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.91 | -35.80 | -90.95 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.53 | -49.13 | -96.55 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.43 | -54.82 | -89.43 | 2159 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.50 | -27.53 | -65.83 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.26 | -24.28 | -73.80 | 1259 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.25 | -17.46 | -78.35 | 1648 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.23 | -47.18 | -97.25 | 4303 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -91.49 | -99.93 | 8204 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-06T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 17.00 | — | entry signal |
| 2026-11-06T02:00 | VWAP momentum · 1h | sell | BTC-USD | 17.00 | -0.16 | exit signal |
| 2026-11-06T01:45 | MFI reversion · 1h | buy | DOGE-USD | 4.42 | — | rebalance up |
| 2026-11-06T01:15 | MFI reversion · 1h | sell | DOGE-USD | 4.34 | -0.03 | rebalance down |
| 2026-11-06T01:05 | Three white soldiers | sell | SOL-USD | 16.46 | -0.18 | exit signal |
| 2026-11-06T01:05 | Three white soldiers | sell | DOGE-USD | 16.49 | -0.14 | exit signal |
| 2026-11-06T01:00 | MFI reversion · 1h | buy | DOGE-USD | 13.18 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | ETH-USD | 1.34 | — | rebalance up |
| 2026-11-06T01:00 | CCI reversion · 1h | buy | DOGE-USD | 11.09 | — | entry signal |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | SOL-USD | 4.51 | -0.00 | rebalance down |
| 2026-11-06T01:00 | CCI reversion · 1h | sell | BTC-USD | 7.93 | 0.05 | rebalance down |
| 2026-11-06T01:00 | Williams %R · 1h | buy | SOL-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | DOGE-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | Williams %R · 1h | buy | BTC-USD | 5.54 | — | entry signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | SOL-USD | 9.92 | -0.04 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | ETH-USD | 9.87 | -0.12 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 9.82 | -0.01 | exit signal |
| 2026-11-06T01:00 | VWAP reversion · 1h | sell | BTC-USD | 9.91 | -0.05 | exit signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | XRP-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.14 | — | entry signal |
| 2026-11-06T01:00 | RSI(14) reversion · 1h | buy | ETH-USD | 16.57 | — | entry signal |
| 2026-11-06T01:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 16.64 | — | entry signal |
| 2026-11-06T01:00 | VWAP momentum · 1h | buy | SOL-USD | 15.93 | — | entry signal |
| 2026-11-06T01:00 | VWAP momentum · 1h | buy | BTC-USD | 17.15 | — | entry signal |
| 2026-11-06T00:45 | Three white soldiers | buy | SOL-USD | 16.63 | — | entry signal |
| 2026-11-06T00:35 | Three white soldiers | buy | DOGE-USD | 16.63 | — | entry |
| 2026-11-06T00:05 | CCI reversion · 1h | buy | ETH-USD | 3.88 | — | entry |
| 2026-11-06T00:05 | CCI reversion · 1h | sell | SOL-USD | 3.88 | -0.03 | rebalance down |
| 2026-11-06T00:00 | Hold BTC | buy | BTC-USD | 88.43 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | XRP-USD | 5.82 | — | entry signal |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | SOL-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | ETH-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | DOGE-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Stochastic reversion · 1h | buy | BTC-USD | 5.82 | — | entry |
| 2026-11-06T00:00 | Z-score reversion · 1h | buy | SOL-USD | 10.45 | — | entry |
| 2026-11-06T00:00 | Z-score reversion · 1h | buy | BTC-USD | 10.45 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | SOL-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | ETH-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | DOGE-USD | 4.00 | — | entry |
| 2026-11-06T00:00 | Bollinger reversion · 1h | buy | BTC-USD | 4.00 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-08 02:25:05.000123+00:00 -> 2026-11-06 02:35:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-08 02:25:05.000123+00:00 -> 2026-11-06 02:35:05.000123+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-08 02:25:05.000123+00:00 -> 2026-11-06 02:35:05.000123+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
