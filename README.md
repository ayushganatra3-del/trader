# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T15:20:05.000146+00:00 · 46292 ticks

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
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 13869 decisions in 2268 calls, $0.1866 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T15:20 | 3 / 20 / 7 | cash |  |
| Breezy | 2026-11-03T15:20 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-03T15:20 | 4 / 24 / 2 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| MACD zero-line | MSFT | 1.87 | +0.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.36 | 8.36 | 0 | — | 9.00 | 3.89 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.17 | 0.87 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 26 | 26.9 | 8.28 | 2.11 | -6.54 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.20 | 0.20 | 103 | 45.6 | -11.49 | -3.03 | -13.44 | 143 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.78 | -3.22 | 0 | — | -1.42 | -0.71 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.46 | -3.54 | 106 | 34.9 | 4.45 | 2.14 | -3.74 | 94 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.06 | -3.94 | 5 | 40.0 | 2.74 | 0.74 | -7.93 | 8 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 96.04 | -3.96 | 0 | — | -0.59 | -0.15 | -6.60 | 1 |
| 14 | Agent (rotation) | meta | 94.55 | -5.45 | 151 | 29.1 | -4.52 | -2.72 | -8.59 | 170 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.08 | -5.92 | 0 | — | -2.35 | -0.85 | -7.64 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.07 | -5.93 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 93.04 | -6.96 | 143 | 27.3 | 2.62 | 0.90 | -8.76 | 222 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Hold BTC | benchmark | 91.00 | -9.00 | 0 | — | -0.71 | 0.06 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 90.83 | -9.17 | 101 | 21.8 | -16.74 | -6.21 | -17.70 | 80 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.51 | -6.36 | -12.22 | 208 |
| 23 | Opening range 30m | breakout | 89.59 | -10.41 | 334 | 33.2 | -12.80 | -3.91 | -17.21 | 576 |
| 24 | Squeeze breakout · 1h | breakout | 89.08 | -10.92 | 61 | 23.0 | -7.66 | -2.50 | -13.74 | 90 |
| 25 | Daily: Bullish score | daily | 88.51 | -11.49 | 14 | 21.4 | -4.51 | -0.49 | -14.73 | 15 |
| 26 | Donchian 55/20 · 1h | breakout | 88.46 | -11.54 | 60 | 13.3 | -14.54 | -3.27 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 88.37 | -11.63 | 35 | 37.1 | -21.98 | -4.46 | -23.13 | 61 |
| 28 | Parabolic SAR · 1h | trend | 88.33 | -11.67 | 149 | 26.8 | -14.38 | -3.34 | -17.40 | 241 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.75 | -13.26 | 1 | 0.0 | -2.80 | -0.26 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.59 | -3.83 | -14.77 | 96 |
| 31 | Max aggression: 5-day momentum | meta | 84.97 | -15.03 | 15 | 40.0 | -29.38 | -1.94 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.55 | -15.45 | 129 | 28.7 | -16.63 | -3.72 | -18.06 | 97 |
| 33 | Stochastic reversion · 1h | reversion | 84.52 | -15.48 | 236 | 46.2 | -23.27 | -4.69 | -25.32 | 389 |
| 34 | MFI reversion · 1h | reversion | 84.35 | -15.65 | 300 | 33.0 | -15.11 | -2.37 | -18.15 | 148 |
| 35 | Connors RSI(2) · 1h | reversion | 84.07 | -15.93 | 191 | 40.8 | -20.91 | -6.69 | -21.57 | 139 |
| 36 | Keltner breakout · 1h | breakout | 83.99 | -16.00 | 89 | 23.6 | -20.67 | -4.27 | -22.86 | 175 |
| 37 | ADX DI cross · 1h | trend | 83.11 | -16.89 | 148 | 18.2 | -18.34 | -3.57 | -21.32 | 244 |
| 38 | Opening range 15m | breakout | 82.44 | -17.56 | 408 | 30.4 | -17.98 | -5.22 | -20.73 | 709 |
| 39 | Ichimoku · 1h | trend | 81.29 | -18.71 | 83 | 13.3 | -18.75 | -3.80 | -25.58 | 120 |
| 40 | Bollinger breakout · 1h | breakout | 81.16 | -18.84 | 140 | 25.0 | -17.25 | -3.36 | -23.31 | 238 |
| 41 | EMA 20/50 cross · 1h | trend | 79.85 | -20.15 | 90 | 11.1 | -20.75 | -3.83 | -27.42 | 126 |
| 42 | CCI reversion · 1h | reversion | 78.84 | -21.16 | 268 | 44.8 | -27.08 | -4.28 | -28.42 | 445 |
| 43 | Bollinger reversion · 1h | reversion | 78.17 | -21.83 | 220 | 37.7 | -29.28 | -5.74 | -31.68 | 376 |
| 44 | Supertrend · 1h | trend | 77.78 | -22.22 | 141 | 12.8 | -27.79 | -5.31 | -29.54 | 220 |
| 45 | MACD zero-line · 1h | trend | 77.70 | -22.30 | 136 | 15.4 | -25.53 | -5.53 | -27.61 | 211 |
| 46 | Z-score reversion · 1h | reversion | 77.29 | -22.71 | 140 | 34.3 | -14.56 | -2.14 | -23.02 | 211 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.48 | -3.59 | -33.56 | 33 |
| 48 | MACD cross · 1h | trend | 77.01 | -22.99 | 299 | 23.4 | -34.02 | -6.62 | -36.33 | 472 |
| 49 | Triple EMA stack · 1h | trend | 76.38 | -23.62 | 125 | 14.4 | -27.01 | -4.91 | -31.08 | 196 |
| 50 | Williams %R · 1h | reversion | 76.36 | -23.64 | 273 | 45.8 | -36.48 | -6.57 | -37.30 | 520 |
| 51 | RSI momentum · 1h | momentum | 76.22 | -23.78 | 135 | 12.6 | -29.07 | -5.64 | -30.58 | 213 |
| 52 | Heikin-Ashi · 1h | trend | 76.14 | -23.86 | 356 | 22.5 | -40.39 | -8.56 | -43.24 | 660 |
| 53 | OBV trend · 1h | momentum | 75.67 | -24.33 | 240 | 17.5 | -30.80 | -6.54 | -32.87 | 296 |
| 54 | Donchian 20/10 · 1h | breakout | 75.18 | -24.82 | 119 | 20.2 | -27.78 | -4.87 | -30.93 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.00 | -26.00 | 301 | 25.6 | -32.91 | -6.19 | -35.18 | 371 |
| 56 | RSI(14) reversion · 1h | reversion | 72.61 | -27.39 | 128 | 25.8 | -22.27 | -3.96 | -26.28 | 204 |
| 57 | Candlestick reversal · 1h | reversion | 70.77 | -29.23 | 351 | 28.5 | -35.01 | -6.64 | -38.02 | 548 |
| 58 | Agent (ML meta-label) | meta | 70.28 | -29.72 | 1312 | 20.6 | -16.64 | -3.09 | -18.69 | 304 |
| 59 | Three white soldiers | momentum | 69.43 | -30.57 | 411 | 16.1 | -46.06 | -21.62 | -46.07 | 614 |
| 60 | EMA 9/21 cross · 1h | trend | 68.83 | -31.17 | 218 | 9.6 | -37.37 | -7.58 | -38.90 | 328 |
| 61 | Max aggression: 1-day momentum | meta | 68.46 | -31.54 | 23 | 30.4 | -32.57 | -1.84 | -50.32 | 42 |
| 62 | VWAP momentum · 1h | momentum | 68.34 | -31.66 | 697 | 21.5 | -52.53 | -10.42 | -55.34 | 1218 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.10 | -98.95 | 5168 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.67 | -24.16 | -80.27 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -46.66 | -93.52 | 2495 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.89 | -31.07 | -89.04 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.21 | -38.00 | -91.24 | 2318 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.66 | -32.32 | -90.66 | 2220 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -52.76 | -97.75 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.30 | -62.31 | -96.31 | 3373 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.41 | -34.31 | -93.51 | 2392 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.60 | -34.23 | -81.79 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.69 | -99.48 | 5874 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -43.75 | -93.01 | 2615 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -36.97 | -95.43 | 3356 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.72 | -99.80 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -44.90 | -91.97 | 2269 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.33 | -26.50 | -74.75 | 1559 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -61.72 | -97.78 | 3527 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.75 | -98.66 | 4818 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.13 | -28.00 | -70.00 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -53.78 | -94.73 | 2771 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.05 | -84.84 | 1806 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.94 | -99.61 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.82 | -88.15 | 2230 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.58 | -19.14 | -76.70 | 1702 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.30 | -35.38 | -90.39 | 2236 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.48 | -96.45 | 3813 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -52.15 | -89.25 | 2135 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.42 | -25.08 | -65.71 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.80 | -25.41 | -74.05 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.97 | -18.84 | -77.16 | 1598 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.81 | -49.00 | -96.81 | 4230 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -100.97 | -99.92 | 8210 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T15:20 | Agent (rotation) | sell | BITX | 7.84 | -0.04 | selected signal exited |
| 2026-11-03T15:20 | Agent (ML meta-label) | buy | SOXL | 6.39 | — | following Connors RSI(2) |
| 2026-11-03T15:20 | Agent (ML meta-label) | buy | GOOGL | 6.39 | — | entry |
| 2026-11-03T15:20 | Opening range 15m | buy | SPY | 4.51 | — | entry signal |
| 2026-11-03T15:20 | Opening range 15m | sell | AAPL | 4.51 | -0.02 | rebalance down |
| 2026-11-03T15:20 | Gap and go | sell | BITX | 23.17 | -0.11 | exit signal |
| 2026-11-03T15:15 | Agent (ML meta-label) | sell | SOXL | 6.44 | 0.06 | selected signal exited |
| 2026-11-03T15:15 | Agent (ML meta-label) | sell | GOOGL | 6.38 | 0.00 | selected signal exited |
| 2026-11-03T15:15 | Three white soldiers | buy | MSFT | 17.36 | — | entry signal |
| 2026-11-03T15:15 | Opening range 30m | buy | TNA | 17.93 | — | entry signal |
| 2026-11-03T15:15 | Opening range 30m | buy | MSTR | 17.93 | — | entry signal |
| 2026-11-03T15:15 | Opening range 30m | buy | IWM | 17.93 | — | entry signal |
| 2026-11-03T15:15 | Opening range 30m | sell | MSFT | 4.50 | 0.01 | rebalance down |
| 2026-11-03T15:15 | Opening range 30m | sell | COIN | 4.52 | 0.01 | rebalance down |
| 2026-11-03T15:10 | Agent (rotation) | buy | TQQQ | 7.88 | — | entry |
| 2026-11-03T15:10 | Agent (rotation) | buy | BITX | 7.88 | — | following Z-score reversion |
| 2026-11-03T15:10 | Agent (rotation) | sell | LABU | 6.29 | -0.04 | selected signal exited |
| 2026-11-03T15:10 | ROC + volume · 1h | sell | SQQQ | 12.37 | 0.68 | target is flat |
| 2026-11-03T15:10 | Opening range 30m | buy | MSFT | 22.39 | — | entry signal |
| 2026-11-03T15:10 | Opening range 30m | buy | COIN | 22.39 | — | entry signal |
| 2026-11-03T15:10 | Opening range 15m | buy | MSFT | 9.09 | — | entry signal |
| 2026-11-03T15:10 | Opening range 15m | buy | META | 4.98 | — | rebalance up |
| 2026-11-03T15:10 | Opening range 15m | sell | TNA | 4.66 | 0.00 | rebalance down |
| 2026-11-03T15:10 | Opening range 15m | sell | MSTR | 4.68 | 0.01 | rebalance down |
| 2026-11-03T15:10 | Opening range 15m | sell | COIN | 4.72 | 0.03 | rebalance down |
| 2026-11-03T15:10 | Gap and go | buy | TQQQ | 23.28 | — | entry signal |
| 2026-11-03T15:10 | Gap and go | buy | BITX | 23.28 | — | entry signal |
| 2026-11-03T15:10 | Gap and go | sell | LABU | 23.38 | -0.09 | target is flat |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | UPRO | 6.36 | — | entry |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | TQQQ | 6.38 | — | entry |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | SOXL | 6.38 | — | following Connors RSI(2) |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | NVDA | 6.38 | — | entry |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | GOOGL | 6.38 | — | entry |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | COIN | 6.38 | — | entry |
| 2026-11-03T15:05 | Agent (ML meta-label) | buy | BITX | 6.38 | — | following Z-score reversion |
| 2026-11-03T15:05 | Agent (ML meta-label) | sell | TSLA | 11.18 | -0.04 | rebalance down |
| 2026-11-03T15:05 | Agent (ML meta-label) | sell | SQQQ | 11.19 | 0.01 | rebalance down |
| 2026-11-03T15:05 | Agent (ML meta-label) | sell | MSTR | 11.17 | 0.04 | rebalance down |
| 2026-11-03T15:05 | Agent (ML meta-label) | sell | ETHU | 11.12 | 0.09 | rebalance down |
| 2026-11-03T15:05 | Opening range 15m | buy | META | 6.78 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 15:20:05.000146+00:00 -> 2026-11-03 15:30:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 15:20:05.000146+00:00 -> 2026-11-03 15:30:05.000146+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 15:20:05.000146+00:00 -> 2026-11-03 15:30:05.000146+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
