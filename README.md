# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T14:50:05.000130+00:00 · 46272 ticks

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

Today: 12051 decisions in 2208 calls, $0.1654 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T14:50 | 1 / 25 / 4 | cash |  |
| Breezy | 2026-11-03T14:50 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-03T14:50 | 3 / 24 / 3 | MSTR 74% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.09 | 8.09 | 0 | — | 8.93 | 3.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.67 | 1.05 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.51 | 0.51 | 26 | 26.9 | 8.25 | 2.10 | -6.10 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.19 | 0.19 | 103 | 45.6 | -11.50 | -3.03 | -13.44 | 143 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.72 | -3.28 | 0 | — | -1.52 | -0.77 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.50 | -3.50 | 106 | 34.9 | 5.23 | 2.52 | -2.93 | 94 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 96.44 | -3.56 | 0 | — | -0.17 | 0.01 | -6.60 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.91 | -4.09 | 5 | 40.0 | 2.42 | 0.67 | -7.93 | 8 |
| 14 | Agent (rotation) | meta | 95.06 | -4.94 | 144 | 30.6 | -4.09 | -2.46 | -8.61 | 179 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Gap and go | momentum | 94.39 | -5.61 | 137 | 28.5 | 4.13 | 1.36 | -8.76 | 220 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.07 | -5.93 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.97 | -6.03 | 0 | — | -2.62 | -0.96 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Hold BTC | benchmark | 91.06 | -8.94 | 0 | — | -0.23 | 0.14 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 90.84 | -9.16 | 101 | 21.8 | -16.73 | -6.21 | -17.69 | 80 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.30 | -6.21 | -12.22 | 208 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -12.84 | -3.92 | -17.21 | 570 |
| 24 | Squeeze breakout · 1h | breakout | 89.31 | -10.69 | 61 | 23.0 | -8.07 | -2.70 | -13.71 | 89 |
| 25 | Donchian 55/20 · 1h | breakout | 88.57 | -11.43 | 60 | 13.3 | -14.44 | -3.25 | -18.06 | 100 |
| 26 | Daily: Bullish score | daily | 88.53 | -11.47 | 14 | 21.4 | -5.23 | -0.61 | -14.73 | 15 |
| 27 | Parabolic SAR · 1h | trend | 88.33 | -11.67 | 149 | 26.8 | -14.24 | -3.30 | -17.40 | 241 |
| 28 | Copy: Insider buying | copy | 88.30 | -11.71 | 35 | 37.1 | -22.06 | -4.48 | -23.13 | 61 |
| 29 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 86.57 | -13.43 | 1 | 0.0 | -2.90 | -0.28 | -16.59 | 1 |
| 31 | Max aggression: 5-day momentum | meta | 84.99 | -15.01 | 15 | 40.0 | -29.36 | -1.94 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.63 | -15.37 | 129 | 28.7 | -16.53 | -3.70 | -18.02 | 97 |
| 33 | Stochastic reversion · 1h | reversion | 84.47 | -15.53 | 236 | 46.2 | -23.36 | -4.71 | -25.34 | 389 |
| 34 | MFI reversion · 1h | reversion | 84.30 | -15.70 | 300 | 33.0 | -15.27 | -2.39 | -18.25 | 148 |
| 35 | Keltner breakout · 1h | breakout | 84.09 | -15.91 | 89 | 23.6 | -22.90 | -4.79 | -25.07 | 175 |
| 36 | Connors RSI(2) · 1h | reversion | 84.08 | -15.92 | 191 | 40.8 | -20.90 | -6.69 | -21.57 | 139 |
| 37 | ADX DI cross · 1h | trend | 83.26 | -16.75 | 148 | 18.2 | -17.98 | -3.48 | -21.24 | 244 |
| 38 | Opening range 15m | breakout | 82.14 | -17.86 | 408 | 30.4 | -18.22 | -5.31 | -20.73 | 703 |
| 39 | Bollinger breakout · 1h | breakout | 81.37 | -18.63 | 140 | 25.0 | -17.04 | -3.31 | -23.31 | 238 |
| 40 | Ichimoku · 1h | trend | 81.30 | -18.70 | 83 | 13.3 | -18.74 | -3.80 | -25.58 | 120 |
| 41 | EMA 20/50 cross · 1h | trend | 80.00 | -20.00 | 90 | 11.1 | -20.61 | -3.80 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 78.79 | -21.20 | 268 | 44.8 | -27.29 | -4.34 | -28.58 | 445 |
| 43 | Bollinger reversion · 1h | reversion | 78.17 | -21.83 | 220 | 37.7 | -29.15 | -5.72 | -31.57 | 376 |
| 44 | MACD zero-line · 1h | trend | 77.91 | -22.09 | 136 | 15.4 | -25.25 | -5.46 | -27.53 | 210 |
| 45 | Supertrend · 1h | trend | 77.70 | -22.30 | 141 | 12.8 | -28.05 | -5.38 | -29.63 | 220 |
| 46 | Z-score reversion · 1h | reversion | 77.33 | -22.67 | 140 | 34.3 | -14.47 | -2.12 | -23.02 | 211 |
| 47 | MACD cross · 1h | trend | 77.15 | -22.85 | 299 | 23.4 | -33.90 | -6.59 | -36.34 | 472 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.93 | -3.66 | -33.57 | 33 |
| 49 | Triple EMA stack · 1h | trend | 76.47 | -23.53 | 125 | 14.4 | -26.92 | -4.89 | -31.06 | 196 |
| 50 | Williams %R · 1h | reversion | 76.37 | -23.63 | 273 | 45.8 | -36.51 | -6.59 | -37.34 | 518 |
| 51 | Heikin-Ashi · 1h | trend | 76.30 | -23.70 | 356 | 22.5 | -40.61 | -8.69 | -43.29 | 663 |
| 52 | RSI momentum · 1h | momentum | 76.28 | -23.73 | 135 | 12.6 | -28.77 | -5.56 | -30.54 | 213 |
| 53 | OBV trend · 1h | momentum | 75.82 | -24.18 | 240 | 17.5 | -30.66 | -6.50 | -32.87 | 295 |
| 54 | Donchian 20/10 · 1h | breakout | 75.31 | -24.69 | 119 | 20.2 | -27.59 | -4.83 | -30.87 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.13 | -25.87 | 300 | 25.3 | -31.42 | -5.86 | -34.27 | 370 |
| 56 | RSI(14) reversion · 1h | reversion | 72.53 | -27.47 | 128 | 25.8 | -21.77 | -3.86 | -26.28 | 202 |
| 57 | Candlestick reversal · 1h | reversion | 70.73 | -29.27 | 350 | 28.6 | -33.43 | -6.29 | -36.54 | 546 |
| 58 | Agent (ML meta-label) | meta | 70.30 | -29.70 | 1304 | 20.5 | -11.48 | -2.37 | -14.59 | 282 |
| 59 | Three white soldiers | momentum | 69.78 | -30.23 | 409 | 16.1 | -45.83 | -21.46 | -45.83 | 613 |
| 60 | EMA 9/21 cross · 1h | trend | 68.89 | -31.11 | 218 | 9.6 | -37.24 | -7.55 | -38.88 | 326 |
| 61 | VWAP momentum · 1h | momentum | 68.49 | -31.51 | 697 | 21.5 | -52.51 | -10.40 | -55.42 | 1218 |
| 62 | Max aggression: 1-day momentum | meta | 68.47 | -31.53 | 23 | 30.4 | -32.56 | -1.84 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.44 | -98.96 | 5181 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.74 | -24.18 | -80.27 | 1400 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -46.61 | -93.53 | 2498 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -31.39 | -89.04 | 1906 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -38.01 | -91.25 | 2316 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.71 | -32.17 | -90.71 | 2220 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -52.46 | -97.75 | 3468 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -61.57 | -96.29 | 3373 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -34.24 | -93.47 | 2392 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.63 | -34.35 | -81.75 | 1665 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.79 | -99.48 | 5876 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -43.81 | -92.99 | 2614 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.12 | -95.45 | 3357 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.20 | -99.80 | 6182 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -44.93 | -91.91 | 2273 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.62 | -26.26 | -74.92 | 1560 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -61.78 | -97.78 | 3533 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.46 | -98.66 | 4814 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.99 | -27.72 | -70.00 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -53.94 | -94.71 | 2770 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.79 | -37.34 | -84.85 | 1805 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.44 | -99.61 | 6296 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -29.83 | -88.14 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.58 | -19.13 | -76.68 | 1700 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.26 | -35.92 | -90.30 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -49.60 | -96.45 | 3813 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -51.33 | -89.18 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.45 | -25.08 | -65.62 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.73 | -25.31 | -74.05 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.77 | -18.76 | -77.05 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -48.46 | -96.80 | 4235 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -102.40 | -99.92 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T14:50 | Day trade: Stocks in Play ORB | sell | SOXL | 24.27 | 0.15 | target is flat |
| 2026-11-03T14:50 | Day trade: Stocks in Play ORB | sell | PLTR | 23.89 | -0.23 | target is flat |
| 2026-11-03T14:50 | Agent (ML meta-label) | buy | UPRO | 6.37 | — | entry |
| 2026-11-03T14:50 | Agent (ML meta-label) | buy | TQQQ | 6.66 | — | rebalance up |
| 2026-11-03T14:50 | Agent (ML meta-label) | buy | NVDA | 7.81 | — | entry |
| 2026-11-03T14:50 | Agent (ML meta-label) | sell | SQQQ | 3.84 | -0.01 | rebalance down |
| 2026-11-03T14:50 | Agent (ML meta-label) | sell | SOXL | 5.01 | -0.03 | rebalance down |
| 2026-11-03T14:50 | Agent (ML meta-label) | sell | GOOGL | 8.14 | -0.01 | selected signal exited |
| 2026-11-03T14:50 | Agent (ML meta-label) | sell | ETHU | 3.87 | 0.12 | rebalance down |
| 2026-11-03T14:50 | ROC + volume · 1h | sell | AMZN | 12.34 | -0.34 | target is flat |
| 2026-11-03T14:50 | Opening range 15m | buy | MSTR | 20.54 | — | entry signal |
| 2026-11-03T14:50 | Opening range 15m | buy | COIN | 20.54 | — | entry signal |
| 2026-11-03T14:50 | Opening range 15m | buy | AAPL | 20.54 | — | entry signal |
| 2026-11-03T14:45 | Agent (rotation) | buy | TQQQ | 5.29 | — | entry |
| 2026-11-03T14:45 | Day trade: Stocks in Play ORB | buy | AAPL | 24.12 | — | entry |
| 2026-11-03T14:45 | Agent (ML meta-label) | buy | TQQQ | 1.15 | — | entry |
| 2026-11-03T14:45 | Agent (ML meta-label) | buy | SOXL | 5.05 | — | following Connors RSI(2) |
| 2026-11-03T14:45 | Agent (ML meta-label) | buy | GOOGL | 8.15 | — | entry |
| 2026-11-03T14:45 | Agent (ML meta-label) | sell | TSLA | 3.52 | -0.04 | rebalance down |
| 2026-11-03T14:45 | Agent (ML meta-label) | sell | MSTR | 3.57 | 0.01 | rebalance down |
| 2026-11-03T14:45 | Agent (ML meta-label) | sell | COIN | 3.74 | 0.13 | rebalance down |
| 2026-11-03T14:45 | Agent (ML meta-label) | sell | BITX | 3.52 | -0.01 | rebalance down |
| 2026-11-03T14:45 | Three white soldiers | buy | LABU | 17.49 | — | entry signal |
| 2026-11-03T14:45 | Three white soldiers | buy | AMD | 17.49 | — | entry signal |
| 2026-11-03T14:42 | Agent (rotation) | buy | TECL | 6.33 | — | entry |
| 2026-11-03T14:42 | Agent (rotation) | buy | SOXL | 6.33 | — | following Connors RSI(2) |
| 2026-11-03T14:42 | Agent (rotation) | buy | NVDA | 6.33 | — | entry |
| 2026-11-03T14:42 | Agent (rotation) | buy | LABU | 6.33 | — | following Candlestick reversal |
| 2026-11-03T14:42 | Agent (rotation) | buy | AMD | 6.33 | — | following Supertrend |
| 2026-11-03T14:42 | Day trade: Stocks in Play ORB | buy | UPRO | 24.12 | — | entry |
| 2026-11-03T14:42 | Day trade: Stocks in Play ORB | buy | SOXL | 24.12 | — | entry |
| 2026-11-03T14:42 | Day trade: Stocks in Play ORB | buy | PLTR | 24.12 | — | entry |
| 2026-11-03T14:42 | Gap and go | buy | TECL | 18.80 | — | entry signal |
| 2026-11-03T14:42 | Gap and go | buy | SOXL | 18.80 | — | entry signal |
| 2026-11-03T14:42 | Gap and go | buy | NVDA | 18.80 | — | entry signal |
| 2026-11-03T14:42 | Gap and go | buy | LABU | 18.80 | — | entry signal |
| 2026-11-03T14:42 | Gap and go | buy | AMD | 18.80 | — | entry signal |
| 2026-11-03T14:38 | Copy: Insider buying | buy | BBTX | 1.01 | — | entry |
| 2026-11-03T14:35 | Max aggression: 1-day momentum | buy | SQQQ | 68.78 | — | entry |
| 2026-11-03T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | TQQQ | 100.19 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 14:50:05.000130+00:00 -> 2026-11-03 15:00:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 14:50:05.000130+00:00 -> 2026-11-03 15:00:05.000130+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 14:50:05.000130+00:00 -> 2026-11-03 15:00:05.000130+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
