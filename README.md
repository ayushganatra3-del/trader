# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T23:25:05.000127+00:00 · 47742 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.32 · VIX 16.88 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 40223 decisions in 3191 calls, $0.4952 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T23:25 | 1 / 1 / 3 | cash |  |
| Breezy | 2026-11-04T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T23:25 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.97 | 12.97 | 0 | — | 14.28 | 5.01 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.90 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.64 | 0.64 | 0 | — | 4.55 | 1.39 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.12 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.11 | -0.89 | 5 | 40.0 | 4.49 | 1.09 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.00 | -2.00 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.59 | -1.02 | -9.60 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.13 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.74 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.22 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.32 | -4.68 | 0 | — | -3.89 | -1.45 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.88 | -5.12 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.95 | -5.33 | 26 |
| 17 | Hold BTC | benchmark | 94.44 | -5.56 | 0 | — | -1.25 | -0.04 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.41 | -0.41 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.03 | -6.68 | -8.48 | 183 |
| 20 | Max aggression: 5-day momentum | meta | 91.25 | -8.75 | 16 | 43.8 | -23.80 | -1.39 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.80 | -9.20 | 103 | 22.3 | -16.27 | -6.06 | -17.67 | 78 |
| 23 | Parabolic SAR · 1h | trend | 89.94 | -10.06 | 155 | 27.1 | -15.05 | -3.37 | -19.35 | 245 |
| 24 | Copy: Insider buying | copy | 89.55 | -10.45 | 38 | 39.5 | -21.61 | -4.39 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.98 | -7.23 | -12.78 | 212 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.20 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.20 | -3.57 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.01 | -12.98 | 14 | 21.4 | -8.59 | -1.32 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.82 | -13.18 | 249 | 47.8 | -20.42 | -3.88 | -24.97 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.79 | -13.21 | 62 | 12.9 | -12.97 | -2.78 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.13 | -13.87 | 1 | 0.0 | -6.85 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.52 | -4.17 | -14.77 | 97 |
| 33 | ADX DI cross · 1h | trend | 85.12 | -14.88 | 155 | 18.1 | -18.09 | -3.26 | -22.68 | 277 |
| 34 | Volume breakout · 1h | breakout | 84.52 | -15.48 | 132 | 28.8 | -14.07 | -3.24 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.40 | -15.60 | 324 | 34.3 | -13.76 | -2.10 | -18.47 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.67 | -16.33 | 94 | 24.5 | -20.13 | -4.16 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.43 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.14 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.08 | -17.92 | 85 | 12.9 | -20.32 | -4.33 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.39 | -18.61 | 148 | 25.0 | -18.07 | -3.70 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.94 | -19.06 | 278 | 46.4 | -21.87 | -3.16 | -27.71 | 448 |
| 42 | EMA 20/50 cross · 1h | trend | 79.46 | -20.54 | 92 | 10.9 | -18.81 | -3.34 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 78.80 | -21.20 | 375 | 22.7 | -40.45 | -8.50 | -43.89 | 676 |
| 44 | MACD zero-line · 1h | trend | 78.42 | -21.58 | 141 | 15.6 | -24.87 | -5.17 | -29.59 | 222 |
| 45 | MACD cross · 1h | trend | 78.10 | -21.90 | 310 | 22.9 | -30.48 | -5.98 | -33.62 | 474 |
| 46 | Z-score reversion · 1h | reversion | 77.99 | -22.01 | 152 | 37.5 | -15.60 | -2.31 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.87 | -22.13 | 147 | 12.9 | -29.37 | -5.34 | -32.06 | 232 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.29 | -33.56 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.90 | -23.10 | 233 | 40.3 | -28.20 | -5.57 | -30.68 | 367 |
| 50 | Williams %R · 1h | reversion | 76.64 | -23.36 | 290 | 47.6 | -33.22 | -6.03 | -34.64 | 525 |
| 51 | RSI momentum · 1h | momentum | 76.48 | -23.52 | 142 | 12.0 | -28.42 | -5.49 | -30.54 | 227 |
| 52 | Triple EMA stack · 1h | trend | 75.99 | -24.00 | 131 | 13.7 | -27.76 | -5.52 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.38 | -24.62 | 248 | 17.3 | -29.94 | -6.61 | -30.91 | 294 |
| 54 | Donchian 20/10 · 1h | breakout | 74.36 | -25.64 | 124 | 19.4 | -27.73 | -5.09 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.18 | -25.82 | 321 | 25.5 | -33.26 | -6.49 | -36.19 | 389 |
| 56 | RSI(14) reversion · 1h | reversion | 72.19 | -27.81 | 136 | 28.7 | -20.21 | -3.36 | -26.28 | 220 |
| 57 | EMA 9/21 cross · 1h | trend | 69.58 | -30.42 | 225 | 9.8 | -36.62 | -7.42 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.47 | -30.53 | 729 | 22.2 | -53.73 | -11.31 | -55.84 | 1223 |
| 59 | Agent (ML meta-label) | meta | 69.31 | -30.69 | 1442 | 22.3 | -11.20 | -2.16 | -20.33 | 287 |
| 60 | Candlestick reversal · 1h | reversion | 69.21 | -30.79 | 376 | 30.1 | -35.60 | -6.71 | -38.04 | 557 |
| 61 | Three white soldiers | momentum | 68.07 | -31.93 | 439 | 16.4 | -47.21 | -22.30 | -47.38 | 633 |
| 62 | Max aggression: 1-day momentum | meta | 66.59 | -33.41 | 24 | 29.2 | -35.94 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.47 | -98.95 | 5165 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.24 | -25.63 | -80.26 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -47.80 | -93.50 | 2519 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -31.74 | -89.07 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.92 | -39.30 | -90.99 | 2311 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.26 | -32.36 | -90.27 | 2212 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -54.55 | -97.70 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -59.93 | -96.22 | 3385 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -34.71 | -93.71 | 2470 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.12 | -37.62 | -82.12 | 1651 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.94 | -99.48 | 5870 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.89 | -44.69 | -92.91 | 2603 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -37.95 | -95.64 | 3417 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -77.98 | -99.79 | 6158 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -44.30 | -91.79 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.16 | -27.09 | -75.16 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -65.00 | -97.75 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -64.96 | -98.69 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.62 | -29.23 | -70.38 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -56.25 | -94.75 | 2759 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.63 | -37.67 | -84.65 | 1786 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -76.32 | -99.62 | 6308 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.26 | -31.17 | -88.44 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.43 | -19.21 | -76.92 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.67 | -37.87 | -90.69 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -52.72 | -96.48 | 3832 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.19 | -55.04 | -89.20 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.36 | -28.22 | -65.51 | 809 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.84 | -25.85 | -73.84 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.50 | -18.55 | -77.31 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.93 | -53.96 | -96.94 | 4249 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.22 | -99.93 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T23:05 | Three white soldiers | sell | SOL-USD | 17.05 | -0.03 | exit signal |
| 2026-11-04T23:05 | Three white soldiers | sell | ETH-USD | 16.99 | -0.10 | exit signal |
| 2026-11-04T23:00 | VWAP momentum · 1h | buy | SOL-USD | 3.06 | — | entry signal |
| 2026-11-04T22:55 | Three white soldiers | sell | BTC-USD | 16.97 | -0.14 | stop-loss |
| 2026-11-04T22:45 | Three white soldiers | buy | BTC-USD | 17.11 | — | entry signal |
| 2026-11-04T22:20 | EMA 20/50 cross · 1h | sell | XRP-USD | 3.96 | 0.12 | rebalance down |
| 2026-11-04T22:20 | Three white soldiers | buy | SOL-USD | 17.09 | — | entry signal |
| 2026-11-04T22:20 | Three white soldiers | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-11-04T21:15 | Agent (ML meta-label) | sell | ETH-USD | 5.31 | -0.02 | selected signal exited |
| 2026-11-04T21:05 | Agent (ML meta-label) | buy | ETH-USD | 5.33 | — | entry |
| 2026-11-04T21:00 | Parabolic SAR · 1h | sell | XRP-USD | 8.92 | 0.10 | exit signal |
| 2026-11-04T20:55 | Agent (rotation) | sell | UPRO | 3.12 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TSLA | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TQQQ | 31.06 | -0.34 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | SPY | 3.14 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSTR | 3.18 | 0.02 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSFT | 3.17 | 0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | GOOGL | 3.11 | -0.04 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | COIN | 2.44 | 0.00 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | BITX | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | AAPL | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | MSFT | 24.25 | 0.19 | target is flat |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | GOOGL | 23.88 | -0.21 | target is flat |
| 2026-11-04T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 105.47 | -1.14 | target is flat |
| 2026-11-04T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 95.46 | -0.80 | target is flat |
| 2026-11-04T20:55 | Agent (aggressive) | sell | BITX | 42.49 | -0.26 | selected signal exited |
| 2026-11-04T20:55 | Agent | sell | BITX | 17.81 | -0.11 | selected signal exited |
| 2026-11-04T20:55 | Opening range 30m | sell | UPRO | 9.86 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | TSLA | 8.96 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | SPY | 8.95 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSTR | 9.03 | 0.05 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSFT | 9.01 | 0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | GOOGL | 8.87 | -0.11 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | COIN | 12.79 | 0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | BITX | 8.96 | -0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | AAPL | 8.89 | -0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | UPRO | 7.48 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | TSLA | 5.92 | -0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | SPY | 7.52 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | PLTR | 5.80 | -0.08 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 23:25:05.000127+00:00 -> 2026-11-04 23:35:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 23:25:05.000127+00:00 -> 2026-11-04 23:35:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 23:25:05.000127+00:00 -> 2026-11-04 23:35:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
