# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T06:40:05.000151+00:00 · 56606 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 5220 decisions in 1044 calls, $0.0730 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T06:40 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-12T06:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-12T06:40 | 1 / 4 / 0 | ETH-USD 51% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| RSI momentum | SQQQ | 1.43 | +6.62% | 7 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.47 | 16.47 | 0 | — | 16.04 | 5.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.75 | 15.75 | 20 | 70.0 | 17.89 | 3.60 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.74 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.04 | 4.04 | 0 | — | 6.40 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.38 | 1.82 | -9.06 | 231 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.14 | 3.51 | -3.44 | 86 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | 0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.66 | -1.34 | 0 | — | -0.64 | -0.12 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.11 | -1.89 | 188 | 30.3 | -2.49 | -0.89 | -8.79 | 163 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.18 | -2.82 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.19 | -13.44 | 153 |
| 16 | Copy: Insider buying | copy | 95.62 | -4.38 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.53 | -5.47 | 0 | — | -3.37 | -0.85 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Trend pullback · 1h | trend | 91.76 | -8.24 | 109 | 22.9 | -12.91 | -4.84 | -16.41 | 75 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.91 | -11.09 | 404 | 33.2 | -12.12 | -3.50 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -4.89 | -0.99 | -17.04 | 78 |
| 24 | Max aggression: 5-day momentum | meta | 87.70 | -12.30 | 19 | 47.4 | -27.43 | -1.45 | -45.81 | 25 |
| 25 | Parabolic SAR · 1h | trend | 86.57 | -13.43 | 168 | 26.8 | -13.80 | -2.93 | -21.94 | 223 |
| 26 | Hold BTC | benchmark | 86.55 | -13.45 | 1 | 0.0 | -5.06 | -0.59 | -16.64 | 1 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 28 | Daily: Bullish score | daily | 84.44 | -15.56 | 16 | 18.8 | -9.92 | -1.69 | -19.56 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.28 | -15.72 | 2 | 0.0 | -6.49 | -0.62 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 83.00 | -17.00 | 72 | 13.9 | -22.99 | -4.88 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.36 | -17.64 | 186 | 18.8 | -21.59 | -3.67 | -29.87 | 273 |
| 33 | Stochastic reversion · 1h | reversion | 82.25 | -17.75 | 292 | 48.3 | -23.78 | -3.48 | -27.08 | 391 |
| 34 | Keltner breakout · 1h | breakout | 82.10 | -17.91 | 111 | 24.3 | -16.75 | -3.42 | -24.55 | 169 |
| 35 | Max aggression: 1-day momentum | meta | 81.30 | -18.70 | 27 | 25.9 | -17.50 | -0.43 | -57.50 | 40 |
| 36 | Opening range 15m | breakout | 80.95 | -19.05 | 501 | 31.3 | -18.42 | -4.93 | -21.11 | 722 |
| 37 | Volume breakout · 1h | breakout | 80.86 | -19.14 | 149 | 27.5 | -13.25 | -3.06 | -21.11 | 91 |
| 38 | Heikin-Ashi · 1h | trend | 80.34 | -19.66 | 418 | 24.6 | -34.80 | -6.42 | -38.20 | 658 |
| 39 | Connors RSI(2) · 1h | reversion | 80.33 | -19.67 | 208 | 39.9 | -20.31 | -6.82 | -20.74 | 121 |
| 40 | MFI reversion · 1h | reversion | 79.21 | -20.79 | 375 | 35.5 | -15.81 | -2.00 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.15 | -21.85 | 366 | 22.1 | -27.27 | -3.96 | -39.83 | 461 |
| 42 | CCI reversion · 1h | reversion | 78.01 | -21.99 | 332 | 45.2 | -28.16 | -4.36 | -31.08 | 449 |
| 43 | Bollinger breakout · 1h | breakout | 77.03 | -22.97 | 176 | 22.2 | -21.58 | -4.59 | -28.24 | 240 |
| 44 | Bollinger reversion · 1h | reversion | 76.05 | -23.95 | 286 | 41.6 | -27.67 | -4.22 | -34.84 | 367 |
| 45 | MACD zero-line · 1h | trend | 75.82 | -24.18 | 162 | 16.7 | -20.71 | -4.06 | -30.74 | 210 |
| 46 | Supertrend · 1h | trend | 75.48 | -24.52 | 168 | 13.1 | -28.51 | -5.00 | -36.14 | 220 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | RSI momentum · 1h | momentum | 75.03 | -24.96 | 159 | 12.6 | -25.81 | -3.90 | -37.48 | 215 |
| 49 | Daily: Momentum burst | daily | 74.89 | -25.11 | 27 | 11.1 | -33.22 | -4.55 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.51 | -25.49 | 103 | 10.7 | -27.23 | -4.60 | -37.26 | 118 |
| 51 | Triple EMA stack · 1h | trend | 74.16 | -25.84 | 144 | 14.6 | -24.69 | -4.05 | -35.90 | 206 |
| 52 | ROC + volume · 1h | momentum | 72.99 | -27.01 | 377 | 27.6 | -31.93 | -5.82 | -38.35 | 378 |
| 53 | Williams %R · 1h | reversion | 72.32 | -27.68 | 353 | 46.2 | -35.33 | -5.51 | -36.06 | 524 |
| 54 | Donchian 20/10 · 1h | breakout | 72.01 | -27.99 | 144 | 19.4 | -28.32 | -5.20 | -35.64 | 209 |
| 55 | OBV trend · 1h | momentum | 71.85 | -28.15 | 281 | 19.2 | -27.93 | -4.84 | -37.06 | 286 |
| 56 | Z-score reversion · 1h | reversion | 71.05 | -28.95 | 197 | 38.6 | -23.22 | -3.21 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.16 | -30.84 | 175 | 32.6 | -26.70 | -3.84 | -32.54 | 229 |
| 58 | VWAP momentum · 1h | momentum | 67.91 | -32.09 | 867 | 22.6 | -50.49 | -10.30 | -51.73 | 1223 |
| 59 | EMA 9/21 cross · 1h | trend | 67.27 | -32.73 | 255 | 9.8 | -33.74 | -6.39 | -41.65 | 339 |
| 60 | Agent (ML meta-label) | meta | 66.36 | -33.65 | 1750 | 24.7 | -11.79 | -1.43 | -24.77 | 350 |
| 61 | Candlestick reversal · 1h | reversion | 65.35 | -34.65 | 461 | 28.9 | -38.14 | -6.82 | -40.29 | 582 |
| 62 | Three white soldiers | momentum | 60.15 | -39.84 | 521 | 15.0 | -48.86 | -22.16 | -48.88 | 651 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -43.99 | -99.03 | 5276 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.66 | -25.17 | -80.39 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -43.29 | -93.66 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.46 | -31.99 | -89.67 | 1927 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.98 | -39.99 | -91.39 | 2330 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -32.36 | -90.25 | 2201 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.81 | -52.87 | -97.88 | 3466 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -53.63 | -96.46 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -33.01 | -93.58 | 2354 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.90 | -33.64 | -83.50 | 1659 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -54.61 | -99.56 | 5998 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.05 | -42.21 | -92.37 | 2607 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.39 | -95.46 | 3451 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.20 | -99.81 | 6139 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.89 | -43.06 | -92.10 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.38 | -24.75 | -75.85 | 1619 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -57.84 | -97.71 | 3510 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.85 | -60.80 | -98.85 | 4902 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.28 | -26.44 | -68.79 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.35 | -94.80 | 2780 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -37.88 | -85.17 | 1780 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.59 | -99.65 | 6340 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.47 | -31.85 | -89.47 | 2291 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.64 | -19.59 | -77.69 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -35.63 | -90.67 | 2175 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.79 | -50.66 | -96.79 | 3847 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -57.07 | -89.30 | 2141 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.95 | -29.99 | -66.47 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.10 | -22.71 | -72.14 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.33 | -18.34 | -78.52 | 1696 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.30 | -47.78 | -97.30 | 4302 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -103.63 | -99.93 | 8354 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T06:35 | Three white soldiers | sell | ETH-USD | 14.95 | -0.11 | exit signal |
| 2026-11-12T06:15 | Three white soldiers | buy | ETH-USD | 15.07 | — | entry signal |
| 2026-11-12T05:15 | MFI reversion · 1h | sell | XRP-USD | 13.10 | -0.28 | stop-loss |
| 2026-11-12T04:55 | MFI reversion · 1h | sell | XRP-USD | 6.35 | -0.10 | rebalance down |
| 2026-11-12T04:20 | MFI reversion · 1h | buy | XRP-USD | 6.39 | — | rebalance up |
| 2026-11-12T04:00 | VWAP momentum · 1h | sell | ETH-USD | 5.19 | -0.03 | exit signal |
| 2026-11-12T03:20 | MFI reversion · 1h | sell | XRP-USD | 6.22 | -0.11 | rebalance down |
| 2026-11-12T03:05 | VWAP momentum · 1h | sell | DOGE-USD | 5.19 | -0.03 | target is flat |
| 2026-11-12T03:00 | VWAP momentum · 1h | buy | ETH-USD | 5.22 | — | entry signal |
| 2026-11-12T03:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.22 | — | entry signal |
| 2026-11-12T03:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 3.18 | -0.05 | exit signal |
| 2026-11-12T02:00 | Candlestick reversal · 1h | buy | XRP-USD | 6.13 | — | entry |
| 2026-11-12T02:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.79 | — | rebalance up |
| 2026-11-12T02:00 | Candlestick reversal · 1h | sell | ETH-USD | 9.28 | -0.08 | exit signal |
| 2026-11-12T02:00 | MACD cross · 1h | sell | BTC-USD | 4.40 | -0.01 | exit signal |
| 2026-11-12T01:00 | Agent (ML meta-label) | buy | ETH-USD | 9.48 | — | entry |
| 2026-11-12T01:00 | CCI reversion · 1h | buy | XRP-USD | 3.98 | — | entry signal |
| 2026-11-12T01:00 | CCI reversion · 1h | buy | ETH-USD | 15.62 | — | entry signal |
| 2026-11-12T01:00 | MACD cross · 1h | sell | ETH-USD | 4.42 | 0.01 | exit signal |
| 2026-11-12T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 9.36 | — | entry signal |
| 2026-11-12T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 9.36 | — | entry signal |
| 2026-11-12T00:00 | MACD cross · 1h | sell | SOL-USD | 3.78 | -0.03 | exit signal |
| 2026-11-11T23:15 | Donchian 20/10 · 1h | sell | BTC-USD | 6.39 | -0.08 | stop-loss |
| 2026-11-11T23:15 | MACD zero-line · 1h | sell | BTC-USD | 4.27 | -0.04 | stop-loss |
| 2026-11-11T23:15 | EMA 9/21 cross · 1h | sell | SOL-USD | 4.68 | -0.11 | stop-loss |
| 2026-11-11T23:10 | MACD zero-line · 1h | buy | BTC-USD | 4.30 | — | entry |
| 2026-11-11T23:10 | MACD zero-line · 1h | sell | SOL-USD | 4.30 | -0.12 | stop-loss |
| 2026-11-11T23:00 | Squeeze breakout · 1h | sell | BTC-USD | 21.86 | -0.29 | exit signal |
| 2026-11-11T23:00 | Bollinger breakout · 1h | sell | BTC-USD | 10.95 | -0.13 | exit signal |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | buy | BTC-USD | 6.46 | — | entry |
| 2026-11-11T23:00 | Donchian 20/10 · 1h | sell | SOL-USD | 6.46 | -0.10 | exit signal |
| 2026-11-11T23:00 | ROC + volume · 1h | sell | SOL-USD | 7.19 | -0.10 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | SOL-USD | 4.75 | -0.06 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | ETH-USD | 6.76 | -0.08 | exit signal |
| 2026-11-11T23:00 | VWAP momentum · 1h | sell | BTC-USD | 4.24 | -0.03 | exit signal |
| 2026-11-11T23:00 | ADX DI cross · 1h | sell | SOL-USD | 8.98 | -0.12 | exit signal |
| 2026-11-11T23:00 | MACD cross · 1h | buy | SOL-USD | 3.81 | — | entry |
| 2026-11-11T23:00 | MACD cross · 1h | sell | DOGE-USD | 3.81 | -0.07 | exit signal |
| 2026-11-11T22:46 | Squeeze breakout · 1h | sell | SOL-USD | 21.77 | -0.41 | stop-loss |
| 2026-11-11T22:46 | Bollinger breakout · 1h | buy | BTC-USD | 3.94 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 06:40:05.000151+00:00 -> 2026-11-12 06:50:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
