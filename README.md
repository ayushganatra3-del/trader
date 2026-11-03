# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T16:20:05.000145+00:00 · 46339 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.56 (-9.44%)

Closed trades 140, win rate 39.3%, fees £3.94, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 18108 decisions in 2409 calls, $0.2360 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T16:20 | 0 / 18 / 12 | cash |  |
| Breezy | 2026-11-03T16:20 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T16:20 | 4 / 24 / 2 | COIN 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| VWAP reversion | COIN | 1.90 | +3.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.17 | 9.17 | 0 | — | 9.88 | 4.24 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.62 | 2.62 | 25 | 48.0 | 1.19 | 0.52 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.69 | 0.69 | 26 | 26.9 | 8.50 | 2.16 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.85 | -3.55 | -13.12 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.91 | -3.10 | 0 | — | -1.20 | -0.59 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.38 | -3.62 | 107 | 34.6 | 4.39 | 2.10 | -3.79 | 94 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.35 | -3.65 | 5 | 40.0 | 3.13 | 0.82 | -7.93 | 8 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.58 | -4.42 | 0 | — | -1.01 | -0.30 | -6.60 | 1 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 15 | Agent (rotation) | meta | 94.36 | -5.64 | 153 | 28.8 | -4.79 | -2.87 | -8.64 | 185 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.33 | -5.67 | 0 | — | -2.10 | -0.75 | -7.64 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.02 | -5.98 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 92.94 | -7.06 | 145 | 26.9 | 2.38 | 0.82 | -8.76 | 226 |
| 19 | Hold BTC | benchmark | 91.26 | -8.74 | 0 | — | 0.23 | 0.21 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.73 | -9.27 | 102 | 21.6 | -16.86 | -6.27 | -17.80 | 80 |
| 22 | Agent | meta | 90.56 | -9.44 | 140 | 39.3 | -10.30 | -6.21 | -12.22 | 208 |
| 23 | Opening range 30m | breakout | 90.30 | -9.70 | 334 | 33.2 | -12.23 | -3.69 | -17.21 | 586 |
| 24 | Squeeze breakout · 1h | breakout | 89.18 | -10.82 | 61 | 23.0 | -8.50 | -2.86 | -13.79 | 90 |
| 25 | Copy: Insider buying | copy | 88.44 | -11.56 | 35 | 37.1 | -22.06 | -4.48 | -23.13 | 61 |
| 26 | Parabolic SAR · 1h | trend | 88.40 | -11.60 | 150 | 26.7 | -14.00 | -3.25 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.38 | -11.62 | 14 | 21.4 | -4.55 | -0.50 | -14.73 | 15 |
| 28 | Donchian 55/20 · 1h | breakout | 88.35 | -11.65 | 60 | 13.3 | -14.61 | -3.29 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.88 | -13.12 | 1 | 0.0 | -2.26 | -0.17 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.59 | -3.83 | -14.77 | 96 |
| 31 | Stochastic reversion · 1h | reversion | 84.81 | -15.19 | 238 | 46.6 | -22.85 | -4.54 | -25.29 | 390 |
| 32 | Max aggression: 5-day momentum | meta | 84.75 | -15.25 | 15 | 40.0 | -29.52 | -1.95 | -36.71 | 25 |
| 33 | Volume breakout · 1h | breakout | 84.58 | -15.42 | 129 | 28.7 | -15.80 | -3.65 | -18.08 | 96 |
| 34 | MFI reversion · 1h | reversion | 84.30 | -15.70 | 301 | 32.9 | -15.13 | -2.36 | -18.14 | 150 |
| 35 | Connors RSI(2) · 1h | reversion | 83.99 | -16.01 | 191 | 40.8 | -20.79 | -6.69 | -21.38 | 138 |
| 36 | Keltner breakout · 1h | breakout | 83.97 | -16.03 | 89 | 23.6 | -20.58 | -4.25 | -22.86 | 175 |
| 37 | ADX DI cross · 1h | trend | 83.20 | -16.80 | 148 | 18.2 | -17.96 | -3.47 | -21.37 | 249 |
| 38 | Opening range 15m | breakout | 83.01 | -17.00 | 409 | 30.3 | -17.63 | -5.09 | -20.73 | 717 |
| 39 | Bollinger breakout · 1h | breakout | 81.30 | -18.70 | 140 | 25.0 | -15.99 | -3.10 | -23.31 | 236 |
| 40 | Ichimoku · 1h | trend | 81.15 | -18.85 | 83 | 13.3 | -18.86 | -3.83 | -25.58 | 120 |
| 41 | EMA 20/50 cross · 1h | trend | 79.89 | -20.11 | 90 | 11.1 | -19.04 | -3.55 | -27.42 | 122 |
| 42 | CCI reversion · 1h | reversion | 79.14 | -20.86 | 268 | 44.8 | -26.74 | -4.21 | -28.37 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.36 | -21.64 | 224 | 38.4 | -29.01 | -5.65 | -31.61 | 377 |
| 44 | MACD zero-line · 1h | trend | 77.79 | -22.20 | 136 | 15.4 | -25.83 | -5.57 | -28.02 | 211 |
| 45 | Supertrend · 1h | trend | 77.77 | -22.23 | 141 | 12.8 | -27.73 | -5.29 | -29.54 | 222 |
| 46 | Z-score reversion · 1h | reversion | 77.75 | -22.25 | 142 | 34.5 | -14.05 | -2.03 | -23.02 | 218 |
| 47 | MACD cross · 1h | trend | 77.18 | -22.82 | 300 | 23.3 | -33.47 | -6.52 | -36.09 | 479 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.03 | -3.51 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 76.86 | -23.14 | 274 | 46.0 | -36.74 | -6.54 | -37.97 | 530 |
| 50 | Heikin-Ashi · 1h | trend | 76.26 | -23.74 | 357 | 22.4 | -40.28 | -8.52 | -43.24 | 660 |
| 51 | Triple EMA stack · 1h | trend | 76.16 | -23.84 | 126 | 14.3 | -27.80 | -5.65 | -30.87 | 204 |
| 52 | RSI momentum · 1h | momentum | 76.11 | -23.89 | 136 | 12.5 | -28.56 | -5.53 | -30.34 | 213 |
| 53 | OBV trend · 1h | momentum | 75.91 | -24.09 | 240 | 17.5 | -30.36 | -6.41 | -32.71 | 297 |
| 54 | Donchian 20/10 · 1h | breakout | 74.99 | -25.01 | 120 | 20.0 | -28.50 | -5.01 | -31.45 | 209 |
| 55 | ROC + volume · 1h | momentum | 74.17 | -25.83 | 302 | 25.5 | -33.03 | -6.24 | -35.56 | 376 |
| 56 | RSI(14) reversion · 1h | reversion | 73.13 | -26.87 | 130 | 26.2 | -22.07 | -3.84 | -26.28 | 204 |
| 57 | Candlestick reversal · 1h | reversion | 71.63 | -28.37 | 353 | 28.6 | -34.13 | -6.06 | -37.99 | 549 |
| 58 | Agent (ML meta-label) | meta | 70.29 | -29.71 | 1331 | 21.0 | -11.94 | -2.37 | -17.65 | 285 |
| 59 | Three white soldiers | momentum | 69.29 | -30.71 | 412 | 16.0 | -46.16 | -21.70 | -46.16 | 616 |
| 60 | EMA 9/21 cross · 1h | trend | 68.83 | -31.17 | 219 | 9.6 | -37.49 | -7.64 | -39.06 | 327 |
| 61 | VWAP momentum · 1h | momentum | 68.66 | -31.34 | 699 | 21.6 | -53.25 | -10.46 | -56.26 | 1226 |
| 62 | Max aggression: 1-day momentum | meta | 68.29 | -31.71 | 23 | 30.4 | -32.71 | -1.85 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.18 | -98.96 | 5186 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.36 | -23.43 | -80.27 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -46.01 | -93.50 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.82 | -30.74 | -89.04 | 1908 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -37.95 | -91.24 | 2327 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -32.05 | -90.63 | 2215 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -52.69 | -97.75 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -61.06 | -96.29 | 3380 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.44 | -34.44 | -93.54 | 2395 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.69 | -34.60 | -81.90 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.89 | -99.48 | 5859 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -43.51 | -93.00 | 2622 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -36.94 | -95.40 | 3350 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.54 | -99.80 | 6165 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -44.38 | -91.94 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.40 | -26.43 | -74.84 | 1562 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.48 | -97.76 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.42 | -98.66 | 4806 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.25 | -27.94 | -70.14 | 1196 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -53.65 | -94.73 | 2776 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.76 | -37.28 | -84.93 | 1815 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.87 | -99.61 | 6294 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.80 | -88.19 | 2231 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.47 | -19.01 | -76.66 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -35.70 | -90.34 | 2234 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.77 | -96.46 | 3804 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -53.34 | -89.33 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.54 | -25.08 | -65.71 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.31 | -24.60 | -74.04 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.95 | -18.82 | -77.16 | 1589 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -48.84 | -96.81 | 4216 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.23 | -99.92 | 8219 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T16:20 | Agent (rotation) | sell | ETHU | 7.85 | -0.03 | selected signal exited |
| 2026-11-03T16:20 | Agent (ML meta-label) | buy | TSLA | 5.56 | — | rebalance up |
| 2026-11-03T16:20 | Agent (ML meta-label) | buy | SQQQ | 5.50 | — | rebalance up |
| 2026-11-03T16:20 | Agent (ML meta-label) | buy | ETHU | 5.58 | — | rebalance up |
| 2026-11-03T16:20 | Agent (ML meta-label) | buy | BITX | 5.57 | — | rebalance up |
| 2026-11-03T16:20 | Agent (ML meta-label) | sell | TQQQ | 10.23 | -0.05 | selected signal exited |
| 2026-11-03T16:20 | Agent (ML meta-label) | sell | MSTR | 11.99 | -0.04 | selected signal exited |
| 2026-11-03T16:20 | Donchian 20/10 · 1h | buy | SOL-USD | 10.49 | — | rebalance up |
| 2026-11-03T16:20 | Donchian 20/10 · 1h | buy | ETH-USD | 3.76 | — | rebalance up |
| 2026-11-03T16:20 | Donchian 20/10 · 1h | sell | TSLA | 18.25 | -0.50 | stop-loss |
| 2026-11-03T16:20 | RSI momentum · 1h | buy | SOL-USD | 8.31 | — | entry |
| 2026-11-03T16:20 | RSI momentum · 1h | buy | BTC-USD | 4.36 | — | rebalance up |
| 2026-11-03T16:20 | RSI momentum · 1h | sell | TSLA | 12.66 | -0.34 | stop-loss |
| 2026-11-03T16:20 | Trend pullback · 1h | sell | TSLA | 22.22 | -0.61 | stop-loss |
| 2026-11-03T16:20 | Parabolic SAR · 1h | buy | XRP-USD | 9.29 | — | rebalance up |
| 2026-11-03T16:20 | Parabolic SAR · 1h | sell | TSLA | 14.67 | -0.35 | stop-loss |
| 2026-11-03T16:20 | Triple EMA stack · 1h | sell | TSLA | 18.68 | -0.51 | stop-loss |
| 2026-11-03T16:20 | EMA 9/21 cross · 1h | buy | SOL-USD | 7.52 | — | rebalance up |
| 2026-11-03T16:20 | EMA 9/21 cross · 1h | sell | TSLA | 11.44 | -0.31 | stop-loss |
| 2026-11-03T16:20 | Three white soldiers | sell | PLTR | 17.25 | -0.13 | exit signal |
| 2026-11-03T16:20 | Gap and go | sell | ETHU | 23.17 | -0.09 | exit signal |
| 2026-11-03T16:10 | Agent (ML meta-label) | buy | TQQQ | 10.27 | — | entry |
| 2026-11-03T16:10 | Agent (ML meta-label) | buy | MSTR | 12.03 | — | entry |
| 2026-11-03T16:10 | Agent (ML meta-label) | buy | BITX | 12.03 | — | following Z-score reversion |
| 2026-11-03T16:10 | Agent (ML meta-label) | sell | TSLA | 5.56 | -0.01 | rebalance down |
| 2026-11-03T16:10 | Agent (ML meta-label) | sell | SQQQ | 5.61 | -0.03 | rebalance down |
| 2026-11-03T16:10 | Agent (ML meta-label) | sell | ETHU | 5.57 | 0.02 | rebalance down |
| 2026-11-03T16:05 | Agent (ML meta-label) | buy | TSLA | 8.78 | — | rebalance up |
| 2026-11-03T16:05 | Agent (ML meta-label) | buy | SQQQ | 8.86 | — | rebalance up |
| 2026-11-03T16:05 | Agent (ML meta-label) | buy | ETHU | 8.83 | — | rebalance up |
| 2026-11-03T16:05 | Agent (ML meta-label) | sell | TQQQ | 8.88 | 0.06 | selected signal exited |
| 2026-11-03T16:05 | Agent (ML meta-label) | sell | MSTR | 8.77 | -0.05 | selected signal exited |
| 2026-11-03T16:05 | Agent (ML meta-label) | sell | BITX | 8.78 | -0.04 | selected signal exited |
| 2026-11-03T16:00 | Agent (rotation) | buy | TQQQ | 31.51 | — | rebalance up |
| 2026-11-03T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 103.14 | — | entry |
| 2026-11-03T16:00 | Agent (ML meta-label) | sell | UPRO | 8.82 | 0.01 | selected signal exited |
| 2026-11-03T16:00 | Agent (ML meta-label) | sell | NVDA | 8.83 | 0.01 | selected signal exited |
| 2026-11-03T16:00 | Z-score reversion · 1h | buy | UPRO | 4.46 | — | rebalance up |
| 2026-11-03T16:00 | Z-score reversion · 1h | sell | SOL-USD | 5.16 | 0.00 | exit signal |
| 2026-11-03T16:00 | Z-score reversion · 1h | sell | BTC-USD | 8.78 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 16:20:05.000145+00:00 -> 2026-11-03 16:30:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 16:20:05.000145+00:00 -> 2026-11-03 16:30:05.000145+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 16:20:05.000145+00:00 -> 2026-11-03 16:30:05.000145+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
