# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T19:20:05.000153+00:00 · 45319 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.05 (-8.95%)

Closed trades 133, win rate 40.6%, fees £3.83, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMZN | 18.19 | -0.02 |
| ETHU | 18.21 | -0.07 |

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

Today: 28773 decisions in 2841 calls, $0.3625 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T19:20 | 3 / 3 / 23 | cash |  |
| Breezy | 2026-11-02T19:20 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-11-02T19:20 | 3 / 20 / 6 | BITX 55% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.69 | 8.69 | 0 | — | 10.18 | 4.53 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.54 | 4.54 | 16 | 68.8 | 4.98 | 1.62 | -4.91 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.17 | 0.85 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.47 | -1.52 | 99 | 45.5 | -13.70 | -3.78 | -13.74 | 140 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 97.38 | -2.62 | 0 | — | 0.75 | 0.37 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.82 | -1.94 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.99 | -3.01 | 0 | — | -0.93 | -0.45 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.74 | -3.26 | 103 | 35.0 | 3.47 | 1.76 | -2.61 | 94 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.93 | 0.96 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.66 | -5.34 | 0 | — | -4.73 | -1.83 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.43 | -5.57 | 0 | — | -2.07 | -0.74 | -7.64 | 1 |
| 17 | Agent (rotation) | meta | 94.08 | -5.92 | 143 | 30.1 | -6.91 | -4.88 | -9.45 | 147 |
| 18 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.84 | 1.28 | -8.76 | 214 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.13 | -2.09 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 91.06 | -8.94 | 101 | 21.8 | -16.65 | -6.17 | -17.60 | 80 |
| 21 | Agent | meta | 91.05 | -8.95 | 133 | 40.6 | -9.23 | -5.47 | -12.34 | 216 |
| 22 | Hold BTC | benchmark | 90.64 | -9.36 | 0 | — | -0.96 | 0.02 | -12.65 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.26 | -1.92 | -13.40 | 88 |
| 24 | Copy: Insider buying | copy | 89.39 | -10.61 | 35 | 37.1 | -21.69 | -4.38 | -23.10 | 62 |
| 25 | Opening range 30m | breakout | 89.09 | -10.91 | 333 | 33.0 | -13.39 | -4.08 | -17.21 | 585 |
| 26 | Donchian 55/20 · 1h | breakout | 88.95 | -11.05 | 60 | 13.3 | -13.54 | -3.04 | -18.06 | 99 |
| 27 | Daily: Bullish score | daily | 88.84 | -11.16 | 14 | 21.4 | -6.04 | -0.74 | -14.73 | 14 |
| 28 | Parabolic SAR · 1h | trend | 88.73 | -11.27 | 147 | 27.2 | -16.02 | -3.76 | -17.23 | 241 |
| 29 | Agent (aggressive) | meta | 87.14 | -12.86 | 64 | 34.4 | -10.08 | -3.23 | -14.77 | 99 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 85.85 | -14.14 | 1 | 0.0 | -4.48 | -0.55 | -15.96 | 1 |
| 31 | Max aggression: 5-day momentum | meta | 84.99 | -15.01 | 15 | 40.0 | -32.45 | -2.25 | -37.35 | 26 |
| 32 | Volume breakout · 1h | breakout | 84.79 | -15.21 | 128 | 28.9 | -17.36 | -3.89 | -18.78 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.46 | -15.54 | 88 | 23.9 | -19.55 | -3.93 | -22.97 | 175 |
| 34 | Connors RSI(2) · 1h | reversion | 84.16 | -15.84 | 191 | 40.8 | -20.11 | -6.33 | -20.84 | 142 |
| 35 | Stochastic reversion · 1h | reversion | 83.83 | -16.17 | 229 | 47.2 | -24.76 | -5.26 | -24.94 | 389 |
| 36 | ADX DI cross · 1h | trend | 83.44 | -16.56 | 145 | 18.6 | -19.94 | -3.58 | -22.82 | 258 |
| 37 | MFI reversion · 1h | reversion | 83.01 | -16.99 | 299 | 32.8 | -16.33 | -2.63 | -18.11 | 144 |
| 38 | Opening range 15m | breakout | 81.90 | -18.10 | 406 | 30.3 | -18.71 | -5.45 | -20.73 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.71 | -18.29 | 139 | 25.2 | -15.44 | -2.85 | -22.68 | 233 |
| 40 | Ichimoku · 1h | trend | 81.70 | -18.30 | 82 | 13.4 | -19.17 | -3.80 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 79.18 | -20.82 | 262 | 45.0 | -26.93 | -4.26 | -28.51 | 440 |
| 42 | EMA 20/50 cross · 1h | trend | 78.63 | -21.37 | 90 | 11.1 | -22.75 | -4.40 | -27.86 | 126 |
| 43 | Supertrend · 1h | trend | 77.88 | -22.12 | 141 | 12.8 | -27.93 | -5.32 | -29.40 | 222 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.49 | -5.51 | -27.99 | 211 |
| 45 | MACD cross · 1h | trend | 77.29 | -22.71 | 295 | 23.7 | -33.37 | -6.65 | -35.21 | 470 |
| 46 | Bollinger reversion · 1h | reversion | 77.08 | -22.92 | 211 | 38.9 | -30.60 | -6.36 | -30.76 | 370 |
| 47 | Daily: Momentum burst ⏸ | daily | 77.04 | -22.96 | 23 | 13.0 | -27.97 | -3.87 | -31.84 | 33 |
| 48 | Triple EMA stack · 1h | trend | 76.85 | -23.15 | 123 | 14.6 | -30.41 | -5.83 | -30.87 | 207 |
| 49 | RSI momentum · 1h | momentum | 76.75 | -23.25 | 135 | 12.6 | -29.42 | -5.67 | -29.84 | 213 |
| 50 | Williams %R · 1h | reversion | 76.32 | -23.68 | 265 | 46.4 | -36.32 | -6.58 | -37.07 | 519 |
| 51 | Heikin-Ashi · 1h | trend | 76.08 | -23.92 | 355 | 22.5 | -41.03 | -8.78 | -43.23 | 659 |
| 52 | Z-score reversion · 1h | reversion | 75.85 | -24.16 | 137 | 34.3 | -16.22 | -2.48 | -22.55 | 207 |
| 53 | OBV trend · 1h | momentum | 75.84 | -24.16 | 237 | 17.7 | -35.29 | -7.68 | -35.53 | 306 |
| 54 | Donchian 20/10 · 1h | breakout | 75.63 | -24.37 | 119 | 20.2 | -26.21 | -4.41 | -30.86 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.64 | -25.36 | 299 | 25.4 | -29.70 | -5.06 | -34.52 | 371 |
| 56 | RSI(14) reversion · 1h | reversion | 71.12 | -28.88 | 127 | 26.0 | -22.61 | -4.10 | -26.17 | 196 |
| 57 | Three white soldiers | momentum | 70.30 | -29.70 | 405 | 16.3 | -45.21 | -20.81 | -45.85 | 611 |
| 58 | Candlestick reversal · 1h | reversion | 69.61 | -30.39 | 338 | 28.4 | -37.44 | -7.68 | -37.81 | 542 |
| 59 | VWAP momentum · 1h | momentum | 69.07 | -30.93 | 689 | 21.8 | -52.29 | -10.73 | -53.55 | 1224 |
| 60 | EMA 9/21 cross · 1h | trend | 69.05 | -30.95 | 216 | 9.7 | -38.07 | -6.99 | -41.62 | 330 |
| 61 | Max aggression: 1-day momentum ⏸ | meta | 68.78 | -31.22 | 23 | 30.4 | -35.11 | -2.07 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.61 | -31.39 | 1292 | 20.4 | -22.50 | -4.77 | -23.40 | 299 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -43.87 | -98.94 | 5171 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.06 | -24.19 | -80.12 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.73 | -44.74 | -93.76 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.90 | -31.22 | -88.92 | 1904 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.52 | -37.66 | -91.56 | 2331 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.86 | -32.17 | -90.90 | 2237 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -51.49 | -97.76 | 3465 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.36 | -57.62 | -96.36 | 3381 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.49 | -34.50 | -93.59 | 2431 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.25 | -33.60 | -82.25 | 1686 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -53.92 | -99.47 | 5863 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.05 | -42.92 | -93.08 | 2609 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.31 | -95.62 | 3390 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -71.90 | -99.79 | 6155 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -44.40 | -91.86 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.85 | -26.17 | -74.99 | 1560 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -60.39 | -97.77 | 3544 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -60.62 | -98.68 | 4816 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.28 | -28.02 | -69.28 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -53.40 | -94.74 | 2760 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -37.15 | -85.04 | 1806 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.67 | -99.62 | 6291 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -30.39 | -88.24 | 2210 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.90 | -19.53 | -76.91 | 1684 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.28 | -36.98 | -90.28 | 2223 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -51.07 | -96.42 | 3800 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -53.76 | -89.56 | 2125 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -63.91 | -24.94 | -64.67 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.23 | -25.51 | -74.28 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.26 | -18.87 | -76.32 | 1588 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.82 | -49.95 | -96.82 | 4232 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.16 | -99.92 | 8222 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T19:20 | Agent (rotation) | buy | SQQQ | 31.37 | — | entry |
| 2026-11-02T19:20 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 104.59 | — | entry |
| 2026-11-02T19:20 | Opening range 30m | sell | TSLA | 22.04 | -0.32 | stop-loss |
| 2026-11-02T19:15 | Agent (ML meta-label) | sell | TQQQ | 8.14 | -0.01 | selected signal exited |
| 2026-11-02T19:10 | Agent (ML meta-label) | buy | TSLA | 3.84 | — | rebalance up |
| 2026-11-02T19:10 | Agent (ML meta-label) | buy | SQQQ | 4.57 | — | rebalance up |
| 2026-11-02T19:10 | Agent (ML meta-label) | buy | COIN | 4.60 | — | rebalance up |
| 2026-11-02T19:10 | Agent (ML meta-label) | buy | BITX | 4.58 | — | rebalance up |
| 2026-11-02T19:10 | Agent (ML meta-label) | sell | UPRO | 1.30 | -0.00 | selected signal exited |
| 2026-11-02T19:10 | Agent (ML meta-label) | sell | TECL | 8.15 | -0.00 | selected signal exited |
| 2026-11-02T19:10 | Agent (ML meta-label) | sell | NVDA | 8.14 | -0.01 | selected signal exited |
| 2026-11-02T19:10 | Agent (aggressive) | buy | AMZN | 43.60 | — | following Bollinger reversion |
| 2026-11-02T19:10 | Agent | buy | AMZN | 18.21 | — | following Bollinger reversion |
| 2026-11-02T19:10 | Agent | sell | MSTR | 18.04 | -0.26 | selected signal exited |
| 2026-11-02T19:10 | CCI reversion · 1h | sell | UPRO | 19.79 | -0.35 | stop-loss |
| 2026-11-02T19:05 | Agent (ML meta-label) | buy | UPRO | 1.30 | — | entry |
| 2026-11-02T19:05 | Agent (ML meta-label) | buy | TQQQ | 8.15 | — | entry |
| 2026-11-02T19:05 | Agent (ML meta-label) | buy | TECL | 8.15 | — | entry |
| 2026-11-02T19:05 | Agent (ML meta-label) | buy | NVDA | 8.15 | — | entry |
| 2026-11-02T19:05 | Agent (ML meta-label) | sell | TSLA | 9.01 | -0.02 | rebalance down |
| 2026-11-02T19:05 | Agent (ML meta-label) | sell | SQQQ | 5.62 | 0.04 | rebalance down |
| 2026-11-02T19:05 | Agent (ML meta-label) | sell | COIN | 5.56 | -0.02 | rebalance down |
| 2026-11-02T19:05 | Agent (ML meta-label) | sell | BITX | 5.56 | -0.02 | rebalance down |
| 2026-11-02T19:05 | CCI reversion · 1h | buy | UPRO | 3.98 | — | rebalance up |
| 2026-11-02T19:05 | CCI reversion · 1h | buy | PLTR | 3.97 | — | rebalance up |
| 2026-11-02T19:05 | CCI reversion · 1h | buy | BITX | 3.96 | — | rebalance up |
| 2026-11-02T19:05 | CCI reversion · 1h | sell | SPY | 15.86 | -0.12 | stop-loss |
| 2026-11-02T19:05 | Opening range 30m | sell | AMZN | 22.05 | -0.23 | stop-loss |
| 2026-11-02T19:00 | Agent (ML meta-label) | buy | ETHU | 10.33 | — | following Stochastic reversion |
| 2026-11-02T19:00 | Agent (ML meta-label) | buy | COIN | 13.74 | — | entry |
| 2026-11-02T19:00 | Agent (ML meta-label) | buy | BITX | 13.74 | — | following Z-score reversion |
| 2026-11-02T19:00 | Agent (ML meta-label) | sell | SQQQ | 3.49 | 0.02 | rebalance down |
| 2026-11-02T19:00 | CCI reversion · 1h | buy | UPRO | 4.57 | — | rebalance up |
| 2026-11-02T19:00 | CCI reversion · 1h | buy | SPY | 4.38 | — | rebalance up |
| 2026-11-02T19:00 | CCI reversion · 1h | buy | PLTR | 4.53 | — | rebalance up |
| 2026-11-02T19:00 | CCI reversion · 1h | buy | BITX | 4.55 | — | rebalance up |
| 2026-11-02T19:00 | CCI reversion · 1h | buy | AMZN | 4.45 | — | rebalance up |
| 2026-11-02T19:00 | CCI reversion · 1h | sell | TQQQ | 11.06 | -0.53 | stop-loss |
| 2026-11-02T19:00 | CCI reversion · 1h | sell | QQQ | 11.41 | -0.19 | stop-loss |
| 2026-11-02T19:00 | Stochastic reversion · 1h | sell | AMD | 4.25 | -0.19 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 19:20:05.000153+00:00 -> 2026-11-02 19:30:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
