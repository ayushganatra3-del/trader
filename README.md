# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T22:20:05.000141+00:00 · 45462 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.57 (-9.43%)

Closed trades 139, win rate 39.6%, fees £3.92, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.96 · VIX 21.31 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 35754 decisions in 3270 calls, $0.4470 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T22:20 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-11-02T22:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-02T22:20 | 2 / 3 / 0 | ETH-USD 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.08 | 9.08 | 0 | — | 9.79 | 4.25 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.55 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.13 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.99 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.39 | -1.61 | 100 | 46.0 | -13.43 | -3.74 | -13.81 | 142 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.05 | -1.95 | 0 | — | 1.41 | 0.64 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.91 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.56 | -3.44 | 0 | — | -1.85 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.25 | 1.65 | -2.89 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.92 | -3.04 | -8.91 | 159 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.67 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.15 | -5.85 | 0 | — | -5.27 | -2.07 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.84 | 1.29 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.65 | -6.35 | 0 | — | -2.94 | -1.10 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.05 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.97 | -9.03 | 101 | 21.8 | -16.63 | -6.22 | -17.67 | 80 |
| 21 | Hold BTC | benchmark | 90.69 | -9.31 | 0 | — | -0.84 | 0.06 | -12.65 | 1 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.41 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.04 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.80 | -2.14 | -13.40 | 88 |
| 25 | Donchian 55/20 · 1h | breakout | 89.41 | -10.59 | 60 | 13.3 | -13.71 | -3.10 | -18.06 | 99 |
| 26 | Daily: Bullish score | daily | 88.75 | -11.25 | 14 | 21.4 | -5.96 | -0.73 | -14.73 | 14 |
| 27 | Parabolic SAR · 1h | trend | 88.75 | -11.25 | 149 | 26.8 | -16.02 | -3.80 | -17.40 | 241 |
| 28 | Copy: Insider buying | copy | 88.51 | -11.48 | 35 | 37.1 | -22.66 | -4.63 | -23.82 | 62 |
| 29 | Max aggression: 5-day momentum | meta | 87.08 | -12.92 | 15 | 40.0 | -30.82 | -2.07 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.96 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.11 | -14.89 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.97 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.75 | -15.24 | 89 | 23.6 | -20.47 | -3.98 | -24.08 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 191 | 40.8 | -20.81 | -6.71 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.65 | -16.35 | 148 | 18.2 | -19.40 | -3.61 | -22.16 | 250 |
| 36 | Stochastic reversion · 1h | reversion | 83.03 | -16.97 | 232 | 46.6 | -25.68 | -5.44 | -25.91 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.50 | -17.50 | 299 | 32.8 | -16.88 | -2.76 | -18.26 | 147 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.52 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 82.14 | -17.86 | 82 | 13.4 | -17.96 | -3.66 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -15.69 | -2.92 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.87 | -21.13 | 90 | 11.1 | -22.14 | -4.19 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 78.55 | -21.45 | 263 | 44.9 | -27.53 | -4.43 | -28.51 | 441 |
| 43 | Supertrend · 1h | trend | 77.66 | -22.34 | 141 | 12.8 | -27.98 | -5.34 | -29.57 | 221 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.79 | -5.63 | -27.67 | 208 |
| 45 | Triple EMA stack · 1h | trend | 77.19 | -22.80 | 125 | 14.4 | -30.13 | -5.60 | -30.89 | 208 |
| 46 | Daily: Momentum burst ⏸ | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.80 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.91 | -23.09 | 299 | 23.4 | -33.18 | -6.65 | -35.02 | 467 |
| 48 | RSI momentum · 1h | momentum | 76.86 | -23.14 | 135 | 12.6 | -30.29 | -5.86 | -30.86 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 76.49 | -23.51 | 356 | 22.5 | -40.63 | -8.79 | -43.18 | 659 |
| 50 | Bollinger reversion · 1h | reversion | 76.33 | -23.67 | 215 | 38.1 | -31.26 | -6.56 | -31.50 | 375 |
| 51 | Williams %R · 1h | reversion | 76.12 | -23.88 | 267 | 46.1 | -36.61 | -6.72 | -36.86 | 519 |
| 52 | OBV trend · 1h | momentum | 76.05 | -23.95 | 239 | 17.6 | -32.97 | -7.10 | -33.42 | 301 |
| 53 | Donchian 20/10 · 1h | breakout | 76.03 | -23.97 | 119 | 20.2 | -25.95 | -4.39 | -30.95 | 206 |
| 54 | Z-score reversion · 1h | reversion | 74.92 | -25.08 | 139 | 33.8 | -17.19 | -2.67 | -22.92 | 209 |
| 55 | ROC + volume · 1h | momentum | 74.85 | -25.15 | 299 | 25.4 | -29.53 | -5.07 | -34.50 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 70.82 | -29.18 | 128 | 25.8 | -21.46 | -3.89 | -26.27 | 193 |
| 57 | Three white soldiers | momentum | 70.13 | -29.86 | 407 | 16.2 | -45.48 | -21.45 | -45.61 | 609 |
| 58 | Candlestick reversal · 1h | reversion | 69.25 | -30.75 | 342 | 28.1 | -38.13 | -7.92 | -38.47 | 543 |
| 59 | VWAP momentum · 1h | momentum | 69.18 | -30.82 | 691 | 21.7 | -53.47 | -10.97 | -54.95 | 1224 |
| 60 | EMA 9/21 cross · 1h | trend | 69.07 | -30.93 | 218 | 9.6 | -36.68 | -7.07 | -39.66 | 326 |
| 61 | Max aggression: 1-day momentum ⏸ | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.10 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.36 | -31.64 | 1302 | 20.4 | -22.96 | -4.27 | -24.51 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.01 | -98.92 | 5153 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.89 | -24.44 | -79.98 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -46.81 | -93.71 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -31.81 | -88.99 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.42 | -39.06 | -91.48 | 2325 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.88 | -33.31 | -90.92 | 2237 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -55.08 | -97.74 | 3467 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -62.79 | -96.33 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.31 | -35.32 | -93.47 | 2407 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.14 | -34.91 | -82.14 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -57.11 | -99.48 | 5878 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.03 | -44.96 | -93.04 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -38.82 | -95.63 | 3388 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -80.98 | -99.79 | 6167 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -46.21 | -91.86 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.67 | -26.62 | -74.81 | 1561 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -66.01 | -97.75 | 3542 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -64.70 | -98.69 | 4832 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.15 | -28.47 | -69.34 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -56.76 | -94.71 | 2761 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.82 | -38.42 | -84.87 | 1798 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -75.90 | -99.62 | 6312 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.37 | -31.22 | -88.39 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.51 | -20.04 | -77.59 | 1709 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.32 | -37.68 | -90.33 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.48 | -53.28 | -96.49 | 3818 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -55.98 | -89.61 | 2138 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.96 | -25.52 | -64.71 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.11 | -26.07 | -74.28 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.50 | -19.20 | -76.68 | 1604 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.87 | -52.62 | -96.87 | 4246 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -111.23 | -99.92 | 8221 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T22:00 | MFI reversion · 1h | buy | SOL-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | MFI reversion · 1h | buy | DOGE-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.77 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | sell | XRP-USD | 8.77 | -0.05 | exit signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.46 | — | entry signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | ETH-USD | 5.46 | — | entry signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | sell | XRP-USD | 6.38 | -0.03 | exit signal |
| 2026-11-02T22:00 | VWAP momentum · 1h | buy | XRP-USD | 17.31 | — | entry signal |
| 2026-11-02T21:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.52 | — | entry signal |
| 2026-11-02T21:00 | Bollinger reversion · 1h | buy | DOGE-USD | 5.87 | — | entry signal |
| 2026-11-02T21:00 | VWAP momentum · 1h | sell | XRP-USD | 17.09 | -0.18 | exit signal |
| 2026-11-02T20:55 | Agent (rotation) | sell | SQQQ | 63.46 | 0.85 | selected signal exited |
| 2026-11-02T20:55 | Day trade: Stocks in Play ORB | sell | AMZN | 24.03 | -0.38 | target is flat |
| 2026-11-02T20:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.14 | 0.79 | target is flat |
| 2026-11-02T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 106.61 | 2.02 | target is flat |
| 2026-11-02T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 96.26 | 0.74 | target is flat |
| 2026-11-02T20:55 | Agent | sell | MSTR | 18.08 | -0.05 | selected signal exited |
| 2026-11-02T20:55 | Keltner breakout · 1h | sell | AMZN | 20.53 | -0.58 | stop-loss |
| 2026-11-02T20:55 | Opening range 30m | sell | SQQQ | 23.23 | 1.02 | end-of-day flatten |
| 2026-11-02T20:55 | Opening range 15m | sell | SQQQ | 17.11 | 0.75 | end-of-day flatten |
| 2026-11-02T20:52 | Candlestick reversal · 1h | buy | SOXL | 7.69 | — | entry |
| 2026-11-02T20:52 | Candlestick reversal · 1h | sell | ETHU | 6.91 | -0.01 | target is flat |
| 2026-11-02T20:35 | Agent (aggressive) | sell | AMZN | 43.15 | -0.32 | selected signal exited |
| 2026-11-02T20:35 | Agent | sell | AMZN | 18.00 | -0.13 | selected signal exited |
| 2026-11-02T20:35 | Three white soldiers | sell | DOGE-USD | 17.43 | -0.13 | exit signal |
| 2026-11-02T20:30 | Agent (rotation) | buy | SQQQ | 31.25 | — | rebalance up |
| 2026-11-02T20:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 102.35 | — | entry |
| 2026-11-02T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 95.53 | — | entry |
| 2026-11-02T20:30 | Agent (ML meta-label) | buy | SOXL | 15.37 | — | entry |
| 2026-11-02T20:30 | Agent (ML meta-label) | buy | COIN | 7.00 | — | entry |
| 2026-11-02T20:30 | Agent (ML meta-label) | sell | BITX | 15.29 | -0.05 | selected signal exited |
| 2026-11-02T20:30 | Williams %R · 1h | buy | AAPL | 10.88 | — | entry signal |
| 2026-11-02T20:30 | VWAP reversion · 1h | buy | LABU | 24.61 | — | entry signal |
| 2026-11-02T20:30 | Connors RSI(2) · 1h | buy | TSLA | 21.04 | — | entry signal |
| 2026-11-02T20:30 | Candlestick reversal · 1h | buy | ETHU | 6.92 | — | entry signal |
| 2026-11-02T20:30 | Candlestick reversal · 1h | sell | BITX | 7.70 | -0.08 | exit signal |
| 2026-11-02T20:30 | ADX DI cross · 1h | sell | TSLA | 20.60 | -0.34 | exit signal |
| 2026-11-02T20:30 | MACD cross · 1h | buy | SQQQ | 9.29 | — | rebalance up |
| 2026-11-02T20:30 | MACD cross · 1h | buy | GOOGL | 9.65 | — | rebalance up |
| 2026-11-02T20:30 | MACD cross · 1h | buy | ETHU | 9.59 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 22:20:05.000141+00:00 -> 2026-11-02 22:30:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
