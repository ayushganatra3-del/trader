# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T18:50:05.000111+00:00 · 45295 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.24 (-8.76%)

Closed trades 132, win rate 40.9%, fees £3.81, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.25 | -0.03 |
| MSTR | 18.17 | -0.12 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 26613 decisions in 2769 calls, $0.3371 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T18:50 | 2 / 22 / 6 | cash |  |
| Breezy | 2026-11-02T18:50 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-02T18:50 | 4 / 23 / 3 | MSTR 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.67 | 8.67 | 0 | — | 10.48 | 4.65 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 5.93 | 1.92 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.60 | 1.00 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.72 | -1.28 | 99 | 45.5 | -13.27 | -3.67 | -13.28 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 97.40 | -2.60 | 0 | — | 0.77 | 0.37 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.22 | -2.78 | 0 | — | -0.50 | -0.22 | -3.94 | 1 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.64 | -1.81 | -5.83 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.84 | -3.16 | 103 | 35.0 | 3.57 | 1.81 | -2.52 | 94 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.50 | 1.07 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.11 | -4.89 | 0 | — | -5.22 | -1.98 | -6.49 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.69 | -5.31 | 0 | — | -1.97 | -0.70 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Agent (rotation) | meta | 94.10 | -5.90 | 143 | 30.1 | -6.91 | -4.80 | -9.58 | 143 |
| 18 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.16 | 1.06 | -8.76 | 215 |
| 19 | Agent | meta | 91.24 | -8.76 | 132 | 40.9 | -9.04 | -5.37 | -12.34 | 215 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.59 | -1.95 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 91.17 | -8.84 | 101 | 21.8 | -16.55 | -6.12 | -17.51 | 80 |
| 22 | Hold BTC | benchmark | 90.70 | -9.30 | 0 | — | -0.67 | 0.06 | -12.65 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -5.92 | -1.73 | -13.40 | 89 |
| 24 | Copy: Insider buying | copy | 89.46 | -10.54 | 35 | 37.1 | -21.64 | -4.37 | -23.10 | 62 |
| 25 | Opening range 30m | breakout | 89.00 | -11.00 | 331 | 33.2 | -13.48 | -4.10 | -17.21 | 585 |
| 26 | Daily: Bullish score | daily | 88.93 | -11.06 | 14 | 21.4 | -5.15 | -0.59 | -14.73 | 14 |
| 27 | Donchian 55/20 · 1h | breakout | 88.78 | -11.22 | 60 | 13.3 | -13.70 | -3.09 | -18.06 | 99 |
| 28 | Parabolic SAR · 1h | trend | 88.73 | -11.27 | 147 | 27.2 | -15.64 | -3.66 | -17.23 | 242 |
| 29 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.03 | -3.21 | -14.77 | 98 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 86.26 | -13.74 | 1 | 0.0 | -3.91 | -0.45 | -15.96 | 1 |
| 31 | Volume breakout · 1h | breakout | 84.89 | -15.11 | 128 | 28.9 | -17.43 | -3.90 | -18.69 | 98 |
| 32 | Keltner breakout · 1h | breakout | 84.28 | -15.72 | 88 | 23.9 | -23.67 | -4.89 | -25.75 | 174 |
| 33 | Stochastic reversion · 1h | reversion | 84.26 | -15.74 | 228 | 47.4 | -23.78 | -5.01 | -24.99 | 391 |
| 34 | Connors RSI(2) · 1h | reversion | 84.16 | -15.84 | 191 | 40.8 | -20.11 | -6.33 | -20.84 | 142 |
| 35 | Max aggression: 5-day momentum | meta | 83.95 | -16.05 | 15 | 40.0 | -33.28 | -2.35 | -37.35 | 26 |
| 36 | ADX DI cross · 1h | trend | 83.41 | -16.59 | 145 | 18.6 | -20.85 | -3.90 | -22.67 | 254 |
| 37 | MFI reversion · 1h | reversion | 83.09 | -16.91 | 299 | 32.8 | -16.40 | -2.64 | -18.25 | 144 |
| 38 | Opening range 15m | breakout | 81.82 | -18.18 | 405 | 30.4 | -18.75 | -5.45 | -20.73 | 717 |
| 39 | Bollinger breakout · 1h | breakout | 81.81 | -18.19 | 139 | 25.2 | -15.54 | -2.87 | -22.60 | 233 |
| 40 | Ichimoku · 1h | trend | 81.54 | -18.46 | 82 | 13.4 | -19.30 | -3.83 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 79.53 | -20.47 | 258 | 45.7 | -26.77 | -4.24 | -28.68 | 440 |
| 42 | EMA 20/50 cross · 1h | trend | 78.26 | -21.74 | 90 | 11.1 | -23.36 | -4.55 | -27.86 | 126 |
| 43 | Supertrend · 1h | trend | 77.97 | -22.03 | 141 | 12.8 | -27.85 | -5.40 | -29.22 | 220 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.50 | -5.52 | -27.99 | 211 |
| 45 | MACD cross · 1h | trend | 77.47 | -22.53 | 295 | 23.7 | -33.26 | -6.64 | -35.15 | 470 |
| 46 | Bollinger reversion · 1h | reversion | 77.42 | -22.58 | 210 | 39.0 | -30.20 | -6.27 | -30.54 | 370 |
| 47 | Daily: Momentum burst ⏸ | daily | 77.04 | -22.96 | 23 | 13.0 | -26.72 | -3.72 | -31.17 | 33 |
| 48 | Triple EMA stack · 1h | trend | 76.76 | -23.24 | 123 | 14.6 | -30.41 | -5.85 | -30.89 | 207 |
| 49 | RSI momentum · 1h | momentum | 76.72 | -23.29 | 135 | 12.6 | -29.43 | -5.67 | -29.76 | 213 |
| 50 | Williams %R · 1h | reversion | 76.61 | -23.39 | 264 | 46.6 | -36.10 | -6.58 | -36.92 | 518 |
| 51 | Z-score reversion · 1h | reversion | 76.38 | -23.62 | 137 | 34.3 | -15.61 | -2.36 | -22.55 | 207 |
| 52 | Heikin-Ashi · 1h | trend | 76.15 | -23.85 | 355 | 22.5 | -40.84 | -8.76 | -43.06 | 659 |
| 53 | OBV trend · 1h | momentum | 75.80 | -24.20 | 237 | 17.7 | -35.95 | -7.77 | -35.95 | 308 |
| 54 | Donchian 20/10 · 1h | breakout | 75.48 | -24.52 | 119 | 20.2 | -26.32 | -4.43 | -30.83 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.56 | -25.45 | 299 | 25.4 | -29.61 | -5.03 | -34.38 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 71.42 | -28.58 | 125 | 26.4 | -21.92 | -3.95 | -26.17 | 193 |
| 57 | Three white soldiers | momentum | 70.35 | -29.65 | 405 | 16.3 | -45.11 | -20.71 | -45.80 | 609 |
| 58 | Candlestick reversal · 1h | reversion | 69.93 | -30.07 | 338 | 28.4 | -36.90 | -7.47 | -37.31 | 541 |
| 59 | VWAP momentum · 1h | momentum | 69.14 | -30.86 | 689 | 21.8 | -52.24 | -10.73 | -53.52 | 1224 |
| 60 | EMA 9/21 cross · 1h | trend | 69.04 | -30.96 | 216 | 9.7 | -37.86 | -6.87 | -41.67 | 329 |
| 61 | Max aggression: 1-day momentum ⏸ | meta | 68.78 | -31.22 | 23 | 30.4 | -34.96 | -2.06 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.76 | -31.24 | 1280 | 20.5 | -21.77 | -4.52 | -22.41 | 316 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.15 | -98.94 | 5174 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.19 | -23.82 | -80.19 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -44.46 | -93.79 | 2526 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.91 | -31.25 | -88.92 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.59 | -37.41 | -91.61 | 2332 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.95 | -32.27 | -90.96 | 2240 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -52.11 | -97.75 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -56.79 | -96.39 | 3391 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -34.15 | -93.50 | 2419 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.20 | -33.66 | -82.21 | 1688 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -53.14 | -99.46 | 5841 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.01 | -43.11 | -93.03 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -37.29 | -95.61 | 3391 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -74.38 | -99.79 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -44.19 | -91.95 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -26.06 | -75.00 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -60.46 | -97.78 | 3547 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -61.72 | -98.68 | 4821 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.24 | -28.10 | -69.24 | 1200 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.69 | -53.31 | -94.70 | 2765 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.92 | -36.98 | -84.96 | 1804 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.95 | -99.62 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.22 | -30.38 | -88.24 | 2206 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.73 | -19.44 | -76.75 | 1680 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.26 | -37.01 | -90.27 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.37 | -50.71 | -96.37 | 3800 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -53.60 | -89.55 | 2121 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.91 | -24.94 | -64.67 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.28 | -25.51 | -74.28 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.13 | -18.82 | -76.23 | 1578 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -49.94 | -96.80 | 4223 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.84 | -99.92 | 8222 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | UPRO | 7.28 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | TQQQ | 7.30 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | TECL | 7.30 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | NVDA | 7.30 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | COIN | 7.30 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | buy | AMD | 3.11 | — | entry |
| 2026-11-02T18:50 | Agent (ML meta-label) | sell | TSLA | 9.85 | -0.02 | rebalance down |
| 2026-11-02T18:50 | Agent (ML meta-label) | sell | SQQQ | 9.92 | 0.04 | rebalance down |
| 2026-11-02T18:50 | Agent (ML meta-label) | sell | ETHU | 9.89 | -0.02 | rebalance down |
| 2026-11-02T18:50 | Agent (ML meta-label) | sell | BITX | 9.92 | -0.00 | rebalance down |
| 2026-11-02T18:45 | Daily: Momentum burst | sell | TECL | 19.64 | -0.96 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-02T18:45 | Daily: Momentum burst | sell | SOXL | 19.06 | -1.55 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-02T18:45 | Daily: Momentum burst | sell | LABU | 18.95 | -1.65 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-02T18:45 | Daily: Momentum burst | sell | AMD | 19.39 | -1.22 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-11-02T18:45 | Bollinger reversion · 1h | sell | AAPL | 6.43 | -0.10 | stop-loss |
| 2026-11-02T18:45 | ADX DI cross · 1h | buy | TNA | 4.21 | — | rebalance up |
| 2026-11-02T18:45 | ADX DI cross · 1h | buy | IWM | 4.17 | — | rebalance up |
| 2026-11-02T18:35 | Agent (ML meta-label) | buy | TSLA | 11.23 | — | rebalance up |
| 2026-11-02T18:35 | Agent (ML meta-label) | buy | SQQQ | 11.24 | — | rebalance up |
| 2026-11-02T18:35 | Agent (ML meta-label) | buy | ETHU | 11.25 | — | rebalance up |
| 2026-11-02T18:35 | Agent (ML meta-label) | buy | BITX | 11.26 | — | rebalance up |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | UPRO | 5.13 | -0.01 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | TQQQ | 5.91 | -0.02 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | TECL | 5.90 | -0.03 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | SOXL | 5.89 | -0.04 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | NVDA | 5.92 | -0.01 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | MSTR | 5.93 | -0.01 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | COIN | 4.01 | -0.02 | selected signal exited |
| 2026-11-02T18:35 | Agent (ML meta-label) | sell | AMD | 4.38 | -0.02 | selected signal exited |
| 2026-11-02T18:35 | Heikin-Ashi · 1h | buy | AMZN | 3.82 | — | rebalance up |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | UPRO | 5.14 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | TQQQ | 5.94 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | TECL | 5.94 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | SOXL | 5.94 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | NVDA | 5.94 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | MSTR | 5.94 | — | following Williams %R |
| 2026-11-02T18:30 | Agent (ML meta-label) | buy | AMD | 4.40 | — | entry |
| 2026-11-02T18:30 | Agent (ML meta-label) | sell | TSLA | 10.27 | -0.03 | rebalance down |
| 2026-11-02T18:30 | Agent (ML meta-label) | sell | SQQQ | 10.36 | 0.03 | rebalance down |
| 2026-11-02T18:30 | Agent (ML meta-label) | sell | ETHU | 10.25 | -0.07 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 18:50:05.000111+00:00 -> 2026-11-02 19:00:05.000111+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
