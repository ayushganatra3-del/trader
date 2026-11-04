# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T19:55:05.000142+00:00 · 47546 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.61 (-10.39%)

Closed trades 144, win rate 38.2%, fees £4.02, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.83 | -0.12 |

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

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 32709 decisions in 2604 calls, $0.4028 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T19:55 | 4 / 14 / 13 | AMD 16% |  |
| Breezy | 2026-11-04T19:55 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-04T19:55 | 4 / 25 / 2 | COIN 73% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.60 | 12.60 | 0 | — | 13.98 | 5.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.38 | 6.38 | 17 | 70.6 | 5.76 | 1.82 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.55 | 1.55 | 0 | — | 5.43 | 1.54 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.12 | -13.53 | 140 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.58 | -0.41 | 5 | 40.0 | 4.24 | 1.03 | -7.85 | 8 |
| 8 | Hold SPY | benchmark | 98.18 | -1.82 | 0 | — | -0.52 | -0.21 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.59 | -1.02 | -9.60 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.13 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.34 | -3.66 | 112 | 34.8 | 6.01 | 2.80 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.83 | -6.25 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 95.17 | -4.83 | 0 | — | -2.06 | -0.74 | -7.64 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.95 | -5.33 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.38 | -5.62 | 0 | — | -4.91 | -1.87 | -6.35 | 1 |
| 17 | Hold BTC | benchmark | 93.98 | -6.02 | 0 | — | -2.18 | -0.11 | -13.22 | 1 |
| 18 | Agent (rotation) | meta | 93.87 | -6.13 | 164 | 27.4 | -8.98 | -7.12 | -10.30 | 188 |
| 19 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -0.87 | -0.23 | -8.76 | 220 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.70 | -9.29 | 103 | 22.3 | -16.68 | -6.25 | -17.97 | 79 |
| 22 | Max aggression: 5-day momentum | meta | 90.36 | -9.64 | 16 | 43.8 | -24.59 | -1.47 | -36.71 | 25 |
| 23 | Parabolic SAR · 1h | trend | 90.03 | -9.97 | 154 | 26.6 | -15.15 | -3.39 | -19.39 | 240 |
| 24 | Copy: Insider buying | copy | 89.86 | -10.14 | 38 | 39.5 | -21.38 | -4.33 | -23.32 | 63 |
| 25 | Agent | meta | 89.61 | -10.39 | 144 | 38.2 | -11.88 | -7.22 | -12.78 | 207 |
| 26 | Opening range 30m | breakout | 89.27 | -10.72 | 356 | 32.9 | -15.52 | -5.17 | -17.21 | 590 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.51 | -3.34 | -14.15 | 85 |
| 28 | Daily: Bullish score | daily | 87.16 | -12.84 | 14 | 21.4 | -12.07 | -1.93 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.66 | -13.34 | 249 | 47.8 | -20.48 | -3.93 | -24.84 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.57 | -13.43 | 62 | 12.9 | -14.82 | -3.21 | -19.85 | 107 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.17 | -13.83 | 1 | 0.0 | -6.49 | -0.94 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.55 | -14.45 | 69 | 31.9 | -12.26 | -4.08 | -14.77 | 96 |
| 33 | ADX DI cross · 1h | trend | 84.89 | -15.11 | 155 | 18.1 | -20.07 | -3.66 | -23.74 | 271 |
| 34 | Volume breakout · 1h | breakout | 84.69 | -15.31 | 130 | 28.5 | -14.00 | -3.22 | -18.08 | 104 |
| 35 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 322 | 34.5 | -14.71 | -2.30 | -18.78 | 153 |
| 36 | Keltner breakout · 1h | breakout | 83.79 | -16.20 | 94 | 24.5 | -20.89 | -4.38 | -22.84 | 184 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.43 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.54 | -17.46 | 434 | 30.2 | -19.85 | -6.11 | -21.19 | 719 |
| 39 | Ichimoku · 1h | trend | 81.71 | -18.29 | 85 | 12.9 | -20.21 | -4.34 | -26.10 | 127 |
| 40 | Bollinger breakout · 1h | breakout | 81.27 | -18.73 | 148 | 25.0 | -18.12 | -3.70 | -23.94 | 251 |
| 41 | CCI reversion · 1h | reversion | 80.72 | -19.28 | 278 | 46.4 | -21.85 | -3.27 | -27.71 | 455 |
| 42 | EMA 20/50 cross · 1h | trend | 78.95 | -21.05 | 92 | 10.9 | -19.15 | -3.65 | -26.60 | 137 |
| 43 | Heikin-Ashi · 1h | trend | 78.92 | -21.08 | 372 | 22.6 | -40.27 | -8.48 | -43.71 | 676 |
| 44 | MACD zero-line · 1h | trend | 78.26 | -21.74 | 141 | 15.6 | -24.34 | -5.25 | -28.88 | 222 |
| 45 | Z-score reversion · 1h | reversion | 78.19 | -21.81 | 152 | 37.5 | -15.44 | -2.28 | -23.02 | 219 |
| 46 | MACD cross · 1h | trend | 77.95 | -22.05 | 310 | 22.9 | -32.46 | -6.46 | -34.38 | 472 |
| 47 | Supertrend · 1h | trend | 77.87 | -22.13 | 147 | 12.9 | -28.38 | -5.32 | -30.97 | 236 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.07 | -4.45 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.77 | -23.23 | 290 | 47.6 | -33.15 | -5.98 | -34.63 | 528 |
| 50 | Bollinger reversion · 1h | reversion | 76.61 | -23.39 | 233 | 40.3 | -28.80 | -5.73 | -30.83 | 373 |
| 51 | RSI momentum · 1h | momentum | 76.43 | -23.57 | 142 | 12.0 | -28.35 | -5.49 | -30.44 | 225 |
| 52 | Triple EMA stack · 1h | trend | 75.80 | -24.20 | 131 | 13.7 | -28.31 | -5.56 | -32.08 | 210 |
| 53 | OBV trend · 1h | momentum | 75.18 | -24.82 | 248 | 17.3 | -29.43 | -6.40 | -30.61 | 289 |
| 54 | Donchian 20/10 · 1h | breakout | 74.34 | -25.66 | 124 | 19.4 | -27.40 | -5.02 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.03 | -25.96 | 320 | 25.6 | -34.41 | -6.79 | -36.83 | 389 |
| 56 | RSI(14) reversion · 1h | reversion | 71.96 | -28.04 | 136 | 28.7 | -21.05 | -3.45 | -26.28 | 220 |
| 57 | Agent (ML meta-label) | meta | 69.63 | -30.37 | 1434 | 22.4 | -4.33 | -0.84 | -16.03 | 268 |
| 58 | EMA 9/21 cross · 1h | trend | 69.50 | -30.50 | 225 | 9.8 | -37.02 | -7.54 | -40.23 | 343 |
| 59 | VWAP momentum · 1h | momentum | 69.43 | -30.57 | 726 | 22.2 | -54.88 | -11.51 | -56.00 | 1219 |
| 60 | Candlestick reversal · 1h | reversion | 69.36 | -30.64 | 376 | 30.1 | -35.88 | -6.68 | -38.39 | 559 |
| 61 | Three white soldiers | momentum | 68.34 | -31.66 | 436 | 16.5 | -46.97 | -22.11 | -47.38 | 629 |
| 62 | Max aggression: 1-day momentum | meta | 66.30 | -33.70 | 24 | 29.2 | -36.26 | -2.19 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.97 | -46.16 | -98.98 | 5161 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.15 | -25.51 | -80.15 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -47.07 | -93.36 | 2503 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -31.29 | -89.14 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.93 | -38.11 | -91.07 | 2308 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.21 | -32.43 | -90.21 | 2198 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -52.55 | -97.74 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.15 | -58.40 | -96.16 | 3347 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.61 | -34.17 | -93.62 | 2462 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -37.53 | -82.18 | 1653 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -56.56 | -99.48 | 5891 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -43.10 | -93.03 | 2601 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.59 | -38.12 | -95.59 | 3400 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -75.75 | -99.80 | 6148 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.64 | -42.47 | -91.79 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.65 | -26.90 | -74.66 | 1551 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -62.66 | -97.74 | 3515 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -64.18 | -98.70 | 4828 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.45 | -28.27 | -70.44 | 1192 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -54.57 | -94.81 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -37.15 | -84.78 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -75.05 | -99.62 | 6308 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.21 | -30.98 | -88.44 | 2236 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.55 | -19.30 | -77.02 | 1700 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -37.21 | -90.64 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -52.31 | -96.50 | 3827 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.13 | -53.22 | -89.25 | 2143 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.37 | -27.78 | -65.73 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.57 | -25.29 | -73.79 | 1264 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.77 | -18.72 | -77.56 | 1611 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.95 | -53.94 | -96.96 | 4254 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -115.28 | -99.93 | 8208 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T19:55 | Agent (rotation) | sell | ETHU | 3.09 | -0.08 | selected signal exited |
| 2026-11-04T19:55 | Agent (ML meta-label) | sell | COIN | 5.80 | -0.02 | selected signal exited |
| 2026-11-04T19:55 | Opening range 30m | buy | UPRO | 5.24 | — | rebalance up |
| 2026-11-04T19:55 | Opening range 30m | sell | ETHU | 8.77 | -0.22 | stop-loss |
| 2026-11-04T19:50 | Agent (ML meta-label) | sell | XRP-USD | 6.29 | -0.05 | selected signal exited |
| 2026-11-04T19:50 | Agent (ML meta-label) | sell | ETH-USD | 6.30 | -0.06 | selected signal exited |
| 2026-11-04T19:50 | Stochastic reversion · 1h | buy | TNA | 4.26 | — | rebalance up |
| 2026-11-04T19:45 | Agent (ML meta-label) | buy | COIN | 5.82 | — | entry |
| 2026-11-04T19:40 | Agent (ML meta-label) | sell | COIN | 6.34 | -0.02 | selected signal exited |
| 2026-11-04T19:36 | Agent (ML meta-label) | buy | XRP-USD | 6.34 | — | entry |
| 2026-11-04T19:36 | Agent (ML meta-label) | buy | ETH-USD | 6.36 | — | entry |
| 2026-11-04T19:36 | Agent (ML meta-label) | buy | COIN | 6.36 | — | entry |
| 2026-11-04T19:36 | Agent (ML meta-label) | buy | AMZN | 6.36 | — | entry |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | SQQQ | 3.69 | 0.03 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | SOL-USD | 3.58 | -0.03 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | MSTR | 3.61 | -0.01 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | MSFT | 3.64 | -0.00 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | ETHU | 3.61 | -0.00 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | BITX | 3.63 | -0.01 | rebalance down |
| 2026-11-04T19:36 | Agent (ML meta-label) | sell | AAPL | 3.65 | -0.00 | rebalance down |
| 2026-11-04T19:30 | Agent (ML meta-label) | buy | SOL-USD | 10.01 | — | entry |
| 2026-11-04T19:30 | Agent (ML meta-label) | buy | BITX | 10.02 | — | following Z-score reversion |
| 2026-11-04T19:30 | Agent (ML meta-label) | sell | SQQQ | 3.95 | 0.01 | rebalance down |
| 2026-11-04T19:30 | Agent (ML meta-label) | sell | MSTR | 4.03 | 0.01 | rebalance down |
| 2026-11-04T19:30 | Agent (ML meta-label) | sell | MSFT | 3.99 | 0.00 | rebalance down |
| 2026-11-04T19:30 | Agent (ML meta-label) | sell | ETHU | 4.05 | 0.01 | rebalance down |
| 2026-11-04T19:30 | Agent (ML meta-label) | sell | AAPL | 4.00 | 0.00 | rebalance down |
| 2026-11-04T19:30 | Agent (aggressive) | buy | BITX | 42.91 | — | following Z-score reversion |
| 2026-11-04T19:30 | Agent | buy | BITX | 17.95 | — | following Z-score reversion |
| 2026-11-04T19:30 | MFI reversion · 1h | buy | SOXL | 7.18 | — | rebalance up |
| 2026-11-04T19:30 | MFI reversion · 1h | buy | LABU | 7.02 | — | rebalance up |
| 2026-11-04T19:30 | MFI reversion · 1h | buy | AMZN | 7.03 | — | rebalance up |
| 2026-11-04T19:30 | MFI reversion · 1h | sell | COIN | 14.12 | 0.02 | exit signal |
| 2026-11-04T19:30 | CCI reversion · 1h | buy | TSLA | 5.78 | — | entry signal |
| 2026-11-04T19:30 | CCI reversion · 1h | sell | SQQQ | 4.33 | 0.02 | rebalance down |
| 2026-11-04T19:30 | Z-score reversion · 1h | buy | TSLA | 11.19 | — | entry signal |
| 2026-11-04T19:30 | Connors RSI(2) · 1h | sell | TSLA | 20.75 | 0.08 | exit signal |
| 2026-11-04T19:30 | Connors RSI(2) · 1h | sell | SQQQ | 21.03 | 0.37 | exit signal |
| 2026-11-04T19:30 | Candlestick reversal · 1h | buy | NVDA | 17.37 | — | entry signal |
| 2026-11-04T19:30 | VWAP momentum · 1h | buy | TNA | 3.67 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 19:55:05.000142+00:00 -> 2026-11-04 20:05:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 19:55:05.000142+00:00 -> 2026-11-04 20:05:05.000142+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 19:55:05.000142+00:00 -> 2026-11-04 20:05:05.000142+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
