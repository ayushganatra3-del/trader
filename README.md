# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T02:05:05.000206+00:00 · 37342 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 110, win rate 39.1%, fees £3.39, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-26 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, RAPP 12%, THRM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 1495 decisions in 299 calls, $0.0209 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T02:05 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-27T02:05 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-27T02:05 | 1 / 3 / 1 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.20 | +6.90% | 7 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 4 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.95 | 7.95 | 0 | — | 8.51 | 4.26 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.08 | 6.08 | 14 | 71.4 | 3.48 | 1.14 | -6.79 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.57 | 5.57 | 21 | 33.3 | 10.57 | 2.73 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 19 | 47.4 | 6.21 | 2.01 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -11.45 | -3.14 | -14.02 | 153 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.97 | -0.03 | 0 | — | 2.80 | 1.29 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 98.75 | -1.25 | 0 | — | -0.04 | 0.03 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.33 | -1.67 | 78 | 34.6 | 8.31 | 3.46 | -1.94 | 102 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -4.13 | -4.73 | -4.49 | 23 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.15 | -1.99 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.52 | -3.48 | 0 | — | -0.27 | -0.05 | -5.99 | 1 |
| 14 | Agent (rotation) | meta | 96.13 | -3.87 | 121 | 31.4 | -1.91 | -1.09 | -6.28 | 186 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.47 | 1.06 | -7.93 | 8 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.88 | -5.12 | 0 | — | -6.95 | -2.93 | -7.83 | 1 |
| 18 | Hold BTC | benchmark | 94.73 | -5.27 | 0 | — | 0.75 | 0.29 | -9.28 | 1 |
| 19 | Gap and go | momentum | 94.72 | -5.28 | 106 | 25.5 | 5.02 | 1.64 | -8.76 | 200 |
| 20 | Trend pullback · 1h | trend | 93.52 | -6.48 | 96 | 22.9 | -21.89 | -6.98 | -22.19 | 114 |
| 21 | Opening range 30m | breakout | 92.62 | -7.38 | 271 | 34.3 | -10.97 | -3.34 | -17.21 | 577 |
| 22 | Copy: Insider buying | copy | 92.14 | -7.86 | 27 | 37.0 | -17.34 | -3.30 | -21.73 | 60 |
| 23 | Donchian 55/20 · 1h | breakout | 91.55 | -8.45 | 49 | 16.3 | -16.01 | -3.62 | -16.70 | 98 |
| 24 | Daily: Momentum burst | daily | 91.29 | -8.71 | 10 | 10.0 | -19.39 | -3.78 | -20.15 | 40 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.24 | -2.16 | -16.91 | 1 |
| 26 | Max aggression: 5-day momentum | meta | 91.10 | -8.90 | 11 | 45.5 | -15.58 | -1.42 | -27.80 | 25 |
| 27 | Squeeze breakout · 1h | breakout | 90.99 | -9.01 | 51 | 23.5 | -2.89 | -0.68 | -11.89 | 93 |
| 28 | Daily: Bullish score | daily | 90.62 | -9.38 | 11 | 18.2 | -6.77 | -0.82 | -14.40 | 13 |
| 29 | Agent | meta | 90.18 | -9.82 | 110 | 39.1 | -10.89 | -6.82 | -12.54 | 214 |
| 30 | Parabolic SAR · 1h | trend | 89.79 | -10.21 | 121 | 25.6 | -21.66 | -5.51 | -21.66 | 246 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 89.28 | -10.72 | 0 | — | -4.64 | -0.64 | -14.57 | 1 |
| 32 | ADX DI cross · 1h | trend | 88.74 | -11.26 | 114 | 17.5 | -13.54 | -2.94 | -14.58 | 265 |
| 33 | Volume breakout · 1h | breakout | 88.69 | -11.30 | 103 | 23.3 | -12.98 | -2.70 | -16.04 | 112 |
| 34 | Agent (aggressive) | meta | 88.57 | -11.43 | 54 | 37.0 | -10.03 | -3.27 | -14.77 | 95 |
| 35 | Stochastic reversion · 1h | reversion | 87.70 | -12.30 | 198 | 47.0 | -21.82 | -3.99 | -23.11 | 392 |
| 36 | Bollinger breakout · 1h | breakout | 87.29 | -12.71 | 108 | 26.9 | -14.05 | -2.80 | -17.70 | 239 |
| 37 | Opening range 15m | breakout | 86.22 | -13.78 | 337 | 30.9 | -14.53 | -4.11 | -17.87 | 704 |
| 38 | Keltner breakout · 1h | breakout | 85.58 | -14.42 | 74 | 23.0 | -20.41 | -3.99 | -23.13 | 184 |
| 39 | Connors RSI(2) · 1h | reversion | 85.07 | -14.93 | 174 | 40.2 | -26.47 | -7.95 | -26.96 | 198 |
| 40 | Z-score reversion · 1h | reversion | 84.73 | -15.27 | 116 | 33.6 | -14.51 | -2.38 | -21.48 | 210 |
| 41 | EMA 20/50 cross · 1h | trend | 84.40 | -15.60 | 72 | 11.1 | -21.74 | -4.28 | -23.13 | 129 |
| 42 | RSI momentum · 1h | momentum | 83.42 | -16.58 | 104 | 15.4 | -22.10 | -4.31 | -23.76 | 201 |
| 43 | MACD cross · 1h | trend | 82.94 | -17.06 | 240 | 22.5 | -29.56 | -6.20 | -30.18 | 475 |
| 44 | Supertrend · 1h | trend | 82.81 | -17.19 | 114 | 14.0 | -27.65 | -5.91 | -28.20 | 223 |
| 45 | MFI reversion · 1h | reversion | 82.50 | -17.50 | 263 | 31.6 | -15.39 | -2.32 | -20.54 | 154 |
| 46 | Ichimoku · 1h | trend | 82.13 | -17.87 | 68 | 11.8 | -21.80 | -4.56 | -24.73 | 109 |
| 47 | Triple EMA stack · 1h | trend | 81.51 | -18.50 | 101 | 14.9 | -30.12 | -6.03 | -30.71 | 204 |
| 48 | Bollinger reversion · 1h | reversion | 81.15 | -18.85 | 179 | 37.4 | -29.91 | -6.16 | -31.08 | 368 |
| 49 | CCI reversion · 1h | reversion | 81.07 | -18.93 | 222 | 44.6 | -25.68 | -3.69 | -28.06 | 464 |
| 50 | Williams %R · 1h | reversion | 81.04 | -18.96 | 228 | 46.1 | -34.80 | -5.89 | -35.64 | 540 |
| 51 | MACD zero-line · 1h | trend | 80.27 | -19.73 | 110 | 15.5 | -24.40 | -5.23 | -24.91 | 218 |
| 52 | Donchian 20/10 · 1h | breakout | 79.68 | -20.32 | 99 | 20.2 | -24.83 | -4.75 | -27.40 | 213 |
| 53 | OBV trend · 1h | momentum | 78.82 | -21.18 | 206 | 17.5 | -33.87 | -7.13 | -34.01 | 290 |
| 54 | Agent (ML meta-label) | meta | 78.72 | -21.27 | 924 | 19.4 | -13.61 | -2.61 | -17.46 | 368 |
| 55 | Three white soldiers | momentum | 78.69 | -21.31 | 303 | 19.5 | -43.64 | -19.83 | -44.12 | 597 |
| 56 | RSI(14) reversion · 1h | reversion | 78.16 | -21.84 | 100 | 24.0 | -17.23 | -2.75 | -24.48 | 211 |
| 57 | ROC + volume · 1h | momentum | 76.51 | -23.49 | 248 | 24.2 | -31.11 | -6.10 | -32.96 | 373 |
| 58 | Heikin-Ashi · 1h | trend | 76.45 | -23.55 | 289 | 22.1 | -45.08 | -10.24 | -45.66 | 662 |
| 59 | Candlestick reversal · 1h | reversion | 76.23 | -23.77 | 272 | 27.9 | -34.49 | -6.40 | -34.99 | 570 |
| 60 | EMA 9/21 cross · 1h | trend | 75.08 | -24.92 | 175 | 10.9 | -33.33 | -7.12 | -34.54 | 333 |
| 61 | VWAP momentum · 1h | momentum | 74.94 | -25.06 | 557 | 21.0 | -49.16 | -10.79 | -50.15 | 1241 |
| 62 | Max aggression: 1-day momentum | meta | 67.05 | -32.95 | 19 | 26.3 | -42.14 | -2.87 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 55.14 | -44.86 | 761 | 22.2 | -74.06 | -26.01 | -74.15 | 1564 |
| 64 | Volume breakout | breakout | 54.10 | -45.90 | 457 | 12.9 | -62.57 | -25.75 | -62.73 | 798 |
| 65 | Squeeze breakout | breakout | 50.79 | -49.21 | 596 | 14.3 | -67.42 | -28.07 | -67.91 | 1175 |
| 66 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.57 | -98.94 | 5167 |
| 67 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.06 | -22.99 | -79.14 | 1425 |
| 68 | Donchian 55/20 | breakout | 50.52 | -49.48 | 614 | 19.5 | -72.11 | -23.49 | -72.49 | 1277 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.84 | -45.50 | -93.84 | 2539 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.19 | -30.30 | -89.19 | 1928 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.38 | -37.20 | -91.38 | 2339 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.69 | -30.38 | -90.70 | 2172 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.95 | -53.13 | -97.95 | 3532 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -55.32 | -96.16 | 3379 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.08 | -35.74 | -94.11 | 2445 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.45 | -33.39 | -82.60 | 1687 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.44 | -53.02 | -99.44 | 5796 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.65 | -41.24 | -92.66 | 2616 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.56 | -37.24 | -95.56 | 3384 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.76 | -99.78 | 6173 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.43 | -44.95 | -92.43 | 2341 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -61.51 | -97.72 | 3575 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -58.32 | -98.67 | 4809 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -54.10 | -94.53 | 2768 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.30 | -38.57 | -84.30 | 1807 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.00 | -99.61 | 6304 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.33 | -28.94 | -88.39 | 2232 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.12 | -19.33 | -77.51 | 1711 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.69 | -36.91 | -90.69 | 2287 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.33 | -47.78 | -96.33 | 3833 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.20 | -49.92 | -90.20 | 2145 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.07 | -18.00 | -76.25 | 1585 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.54 | -48.27 | -96.54 | 4204 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -89.39 | -99.91 | 8262 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T02:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 12.75 | — | entry signal |
| 2026-10-27T02:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 21.12 | — | entry signal |
| 2026-10-27T02:00 | Donchian 55/20 | sell | XRP-USD | 12.59 | -0.09 | exit signal |
| 2026-10-27T01:26 | Squeeze breakout | sell | ETH-USD | 12.65 | -0.07 | stop-loss |
| 2026-10-27T01:26 | Squeeze breakout | sell | DOGE-USD | 12.69 | -0.04 | stop-loss |
| 2026-10-27T01:26 | Donchian 55/20 | buy | XRP-USD | 2.54 | — | rebalance up |
| 2026-10-27T01:26 | Donchian 55/20 | sell | SOL-USD | 12.59 | -0.12 | stop-loss |
| 2026-10-27T01:26 | Donchian 55/20 | sell | ETH-USD | 12.62 | -0.10 | exit signal |
| 2026-10-27T01:26 | Donchian 55/20 | sell | BTC-USD | 5.09 | -0.05 | stop-loss |
| 2026-10-27T01:26 | ROC + volume | sell | ETH-USD | 13.72 | -0.11 | stop-loss |
| 2026-10-27T01:00 | Squeeze breakout · 1h | buy | XRP-USD | 22.81 | — | entry signal |
| 2026-10-27T01:00 | VWAP momentum · 1h | sell | ETH-USD | 3.15 | -0.01 | exit signal |
| 2026-10-27T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 9.41 | 0.05 | exit signal |
| 2026-10-27T01:00 | VWAP momentum · 1h | sell | BTC-USD | 7.46 | -0.04 | exit signal |
| 2026-10-27T01:00 | MACD cross · 1h | buy | BTC-USD | 4.61 | — | entry signal |
| 2026-10-27T01:00 | Three white soldiers | sell | ETH-USD | 19.69 | 0.00 | exit signal |
| 2026-10-27T01:00 | Volume breakout | sell | XRP-USD | 13.46 | -0.08 | exit signal |
| 2026-10-27T01:00 | ROC + volume | sell | XRP-USD | 13.83 | 0.02 | exit signal |
| 2026-10-27T00:30 | Three white soldiers | sell | SOL-USD | 19.64 | -0.04 | exit signal |
| 2026-10-27T00:10 | Donchian 55/20 | buy | BTC-USD | 5.14 | — | entry signal |
| 2026-10-27T00:10 | Donchian 55/20 | sell | XRP-USD | 2.58 | 0.00 | rebalance down |
| 2026-10-27T00:10 | Donchian 55/20 | sell | DOGE-USD | 2.55 | -0.00 | rebalance down |
| 2026-10-27T00:05 | ROC + volume | buy | ETH-USD | 13.83 | — | entry signal |
| 2026-10-27T00:00 | Volume breakout · 1h | buy | XRP-USD | 22.23 | — | entry signal |
| 2026-10-27T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 4.03 | — | entry signal |
| 2026-10-27T00:00 | Donchian 20/10 · 1h | sell | DOGE-USD | 4.03 | -0.03 | rebalance down |
| 2026-10-27T00:00 | VWAP momentum · 1h | buy | ETH-USD | 3.17 | — | entry signal |
| 2026-10-27T00:00 | VWAP momentum · 1h | buy | BTC-USD | 7.50 | — | entry signal |
| 2026-10-27T00:00 | MACD cross · 1h | buy | ETH-USD | 4.89 | — | entry signal |
| 2026-10-27T00:00 | MACD cross · 1h | buy | DOGE-USD | 4.89 | — | entry signal |
| 2026-10-27T00:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 7.52 | — | entry signal |
| 2026-10-27T00:00 | Volume breakout | buy | XRP-USD | 13.55 | — | entry signal |
| 2026-10-26T23:41 | Donchian 55/20 | buy | XRP-USD | 12.72 | — | entry signal |
| 2026-10-26T23:41 | Donchian 55/20 | buy | SOL-USD | 12.72 | — | entry signal |
| 2026-10-26T23:41 | Donchian 55/20 | buy | ETH-USD | 12.72 | — | entry signal |
| 2026-10-26T23:35 | ROC + volume | buy | XRP-USD | 13.81 | — | entry signal |
| 2026-10-26T23:30 | Squeeze breakout | buy | ETH-USD | 12.72 | — | entry signal |
| 2026-10-26T23:30 | Squeeze breakout | buy | DOGE-USD | 12.72 | — | entry signal |
| 2026-10-26T23:30 | Donchian 55/20 | buy | DOGE-USD | 12.72 | — | entry signal |
| 2026-10-26T23:20 | Three white soldiers | buy | SOL-USD | 19.68 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 02:05:05.000206+00:00 -> 2026-10-27 02:15:05.000206+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
