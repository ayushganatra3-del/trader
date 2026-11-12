# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T10:40:05.000241+00:00 · 56818 ticks

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

Today: 8388 decisions in 1680 calls, $0.1173 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T10:40 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-12T10:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-12T10:40 | 1 / 3 / 1 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 116.37 | 16.37 | 0 | — | 16.04 | 5.08 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.65 | 15.65 | 20 | 70.0 | 17.89 | 3.60 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.74 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.95 | 3.96 | 0 | — | 6.40 | 1.76 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.52 | 1.85 | -9.06 | 231 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.31 | 3.58 | -3.28 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | 0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.57 | -1.43 | 0 | — | -0.64 | -0.12 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.08 | -1.93 | 188 | 30.3 | -2.40 | -0.86 | -8.79 | 162 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.10 | -2.90 | 0 | — | -2.23 | -0.51 | -9.25 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 15 | VWAP reversion · 1h | reversion | 96.07 | -3.93 | 141 | 47.5 | -12.28 | -3.17 | -13.44 | 154 |
| 16 | Copy: Insider buying | copy | 95.54 | -4.46 | 43 | 39.5 | -5.77 | -1.11 | -15.11 | 67 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.45 | -5.55 | 0 | — | -3.37 | -0.85 | -10.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 20 | Trend pullback · 1h | trend | 91.73 | -8.27 | 109 | 22.9 | -12.37 | -4.63 | -16.41 | 74 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 88.84 | -11.16 | 404 | 33.2 | -12.12 | -3.50 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -4.89 | -0.99 | -17.04 | 78 |
| 24 | Max aggression: 5-day momentum | meta | 87.63 | -12.37 | 19 | 47.4 | -27.43 | -1.45 | -45.81 | 25 |
| 25 | Parabolic SAR · 1h | trend | 86.50 | -13.50 | 168 | 26.8 | -13.80 | -2.93 | -21.94 | 223 |
| 26 | Hold BTC | benchmark | 86.36 | -13.64 | 1 | 0.0 | -4.74 | -0.61 | -16.64 | 1 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -14.97 | -7.46 | -15.33 | 209 |
| 28 | Daily: Bullish score | daily | 84.41 | -15.59 | 16 | 18.8 | -9.91 | -1.69 | -19.56 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 84.21 | -15.79 | 2 | 0.0 | -6.49 | -0.62 | -24.16 | 1 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -16.78 | -4.70 | -18.51 | 97 |
| 31 | Donchian 55/20 · 1h | breakout | 82.97 | -17.03 | 72 | 13.9 | -22.99 | -4.88 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.29 | -17.71 | 186 | 18.8 | -21.91 | -3.73 | -29.87 | 274 |
| 33 | Stochastic reversion · 1h | reversion | 82.21 | -17.79 | 292 | 48.3 | -23.76 | -3.47 | -27.08 | 393 |
| 34 | Keltner breakout · 1h | breakout | 82.03 | -17.97 | 111 | 24.3 | -16.80 | -3.44 | -24.55 | 169 |
| 35 | Max aggression: 1-day momentum | meta | 81.23 | -18.77 | 27 | 25.9 | -17.50 | -0.43 | -57.50 | 40 |
| 36 | Opening range 15m | breakout | 80.88 | -19.12 | 501 | 31.3 | -18.42 | -4.93 | -21.11 | 722 |
| 37 | Volume breakout · 1h | breakout | 80.80 | -19.20 | 149 | 27.5 | -13.25 | -3.06 | -21.11 | 91 |
| 38 | Connors RSI(2) · 1h | reversion | 80.31 | -19.69 | 208 | 39.9 | -20.31 | -6.82 | -20.74 | 121 |
| 39 | Heikin-Ashi · 1h | trend | 80.27 | -19.73 | 418 | 24.6 | -34.67 | -6.42 | -38.20 | 657 |
| 40 | MFI reversion · 1h | reversion | 79.17 | -20.84 | 375 | 35.5 | -16.30 | -2.10 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.10 | -21.90 | 366 | 22.1 | -27.44 | -3.98 | -39.83 | 462 |
| 42 | CCI reversion · 1h | reversion | 77.95 | -22.05 | 332 | 45.2 | -28.10 | -4.35 | -31.08 | 452 |
| 43 | Bollinger breakout · 1h | breakout | 76.99 | -23.01 | 176 | 22.2 | -21.58 | -4.59 | -28.24 | 240 |
| 44 | Bollinger reversion · 1h | reversion | 76.12 | -23.89 | 286 | 41.6 | -27.55 | -4.20 | -34.84 | 368 |
| 45 | MACD zero-line · 1h | trend | 75.76 | -24.24 | 162 | 16.7 | -20.72 | -4.06 | -30.74 | 210 |
| 46 | Supertrend · 1h | trend | 75.42 | -24.58 | 168 | 13.1 | -28.51 | -5.00 | -36.14 | 220 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | RSI momentum · 1h | momentum | 74.97 | -25.03 | 159 | 12.6 | -25.81 | -3.90 | -37.48 | 215 |
| 49 | Daily: Momentum burst | daily | 74.84 | -25.16 | 27 | 11.1 | -33.22 | -4.55 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.45 | -25.55 | 103 | 10.7 | -26.81 | -4.50 | -37.26 | 117 |
| 51 | Triple EMA stack · 1h | trend | 74.10 | -25.90 | 144 | 14.6 | -24.74 | -4.06 | -35.90 | 206 |
| 52 | ROC + volume · 1h | momentum | 72.93 | -27.07 | 377 | 27.6 | -32.05 | -5.85 | -38.40 | 377 |
| 53 | Williams %R · 1h | reversion | 72.37 | -27.63 | 353 | 46.2 | -35.54 | -5.50 | -36.33 | 527 |
| 54 | Donchian 20/10 · 1h | breakout | 71.96 | -28.04 | 144 | 19.4 | -28.32 | -5.20 | -35.64 | 209 |
| 55 | OBV trend · 1h | momentum | 71.80 | -28.20 | 281 | 19.2 | -27.62 | -4.77 | -37.06 | 287 |
| 56 | Z-score reversion · 1h | reversion | 71.19 | -28.81 | 197 | 38.6 | -23.08 | -3.19 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.11 | -30.89 | 175 | 32.6 | -26.66 | -3.83 | -32.54 | 228 |
| 58 | VWAP momentum · 1h | momentum | 67.85 | -32.16 | 867 | 22.6 | -50.45 | -10.32 | -51.55 | 1222 |
| 59 | EMA 9/21 cross · 1h | trend | 67.22 | -32.78 | 255 | 9.8 | -33.01 | -6.22 | -41.65 | 335 |
| 60 | Agent (ML meta-label) | meta | 66.28 | -33.72 | 1750 | 24.7 | -12.94 | -1.55 | -26.16 | 350 |
| 61 | Candlestick reversal · 1h | reversion | 65.37 | -34.63 | 461 | 28.9 | -38.15 | -6.79 | -40.67 | 583 |
| 62 | Three white soldiers | momentum | 60.03 | -39.97 | 522 | 14.9 | -48.80 | -22.29 | -48.83 | 649 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.99 | -44.22 | -99.03 | 5271 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.63 | -25.24 | -79.64 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -43.40 | -93.59 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.36 | -32.16 | -89.47 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -40.05 | -91.30 | 2332 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.31 | -32.44 | -90.31 | 2205 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -53.87 | -97.91 | 3471 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -53.77 | -96.42 | 3439 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -33.02 | -93.53 | 2348 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.10 | -33.75 | -83.10 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.56 | -55.01 | -99.56 | 5994 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.03 | -42.41 | -92.40 | 2609 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.37 | -95.45 | 3450 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -77.65 | -99.81 | 6147 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.14 | -43.97 | -92.14 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.47 | -24.89 | -75.85 | 1625 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -58.22 | -97.67 | 3507 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.88 | -98.84 | 4895 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.37 | -26.64 | -68.79 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.98 | -94.82 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.45 | -38.18 | -85.18 | 1781 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -73.36 | -99.64 | 6339 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.50 | -32.10 | -89.52 | 2290 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.42 | -19.60 | -77.46 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -35.82 | -90.66 | 2165 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -51.24 | -96.78 | 3845 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.12 | -57.17 | -89.12 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.95 | -30.01 | -66.48 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.19 | -22.76 | -71.22 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.21 | -18.38 | -78.38 | 1687 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.27 | -48.12 | -97.29 | 4291 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -111.58 | -99.93 | 8370 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T10:35 | Three white soldiers | sell | DOGE-USD | 14.92 | -0.12 | stop-loss |
| 2026-11-12T10:25 | Three white soldiers | buy | DOGE-USD | 15.04 | — | entry signal |
| 2026-11-12T10:00 | VWAP reversion · 1h | sell | XRP-USD | 24.08 | 0.08 | exit signal |
| 2026-11-12T10:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.89 | — | entry signal |
| 2026-11-12T10:00 | Candlestick reversal · 1h | sell | DOGE-USD | 4.89 | -0.04 | rebalance down |
| 2026-11-12T10:00 | VWAP momentum · 1h | buy | XRP-USD | 5.66 | — | entry signal |
| 2026-11-12T08:25 | Agent (ML meta-label) | buy | BTC-USD | 3.85 | — | entry |
| 2026-11-12T08:25 | Agent (ML meta-label) | sell | ETH-USD | 3.85 | -0.05 | rebalance down |
| 2026-11-12T08:00 | CCI reversion · 1h | buy | BTC-USD | 5.75 | — | entry signal |
| 2026-11-12T08:00 | CCI reversion · 1h | sell | ETH-USD | 5.75 | -0.05 | rebalance down |
| 2026-11-12T08:00 | Williams %R · 1h | buy | DOGE-USD | 3.95 | — | rebalance up |
| 2026-11-12T08:00 | Williams %R · 1h | sell | XRP-USD | 3.95 | -0.06 | rebalance down |
| 2026-11-12T07:00 | VWAP reversion · 1h | buy | XRP-USD | 24.00 | — | entry signal |
| 2026-11-12T07:00 | Bollinger reversion · 1h | buy | XRP-USD | 19.01 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 10:40:05.000241+00:00 -> 2026-11-12 10:50:05.000241+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
