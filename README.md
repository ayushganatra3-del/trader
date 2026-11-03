# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T15:51:05.000135+00:00 · 46318 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.55 (-9.45%)

Closed trades 139, win rate 39.6%, fees £3.93, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 18.10 | -0.02 |

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

Today: 16218 decisions in 2346 calls, $0.2139 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T15:51 | 0 / 22 / 8 | cash |  |
| Breezy | 2026-11-03T15:51 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T15:51 | 4 / 25 / 1 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.86 | 8.86 | 0 | — | 9.48 | 4.10 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 1.96 | 0.80 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.58 | 0.58 | 26 | 26.9 | 8.38 | 2.13 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.71 | -3.12 | -13.44 | 143 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.85 | -3.15 | 0 | — | -1.32 | -0.66 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.34 | -3.66 | 107 | 34.6 | 4.34 | 2.08 | -3.79 | 94 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.21 | -3.79 | 5 | 40.0 | 3.19 | 0.83 | -7.93 | 8 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 94.99 | -5.01 | 0 | — | -1.62 | -0.51 | -6.60 | 1 |
| 14 | Agent (rotation) | meta | 94.59 | -5.41 | 152 | 28.9 | -4.56 | -2.74 | -8.64 | 185 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.14 | -5.86 | 0 | — | -2.32 | -0.84 | -7.64 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.02 | -5.98 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 93.16 | -6.84 | 144 | 27.1 | 2.62 | 0.89 | -8.76 | 226 |
| 19 | Hold BTC | benchmark | 91.37 | -8.63 | 0 | — | 0.09 | 0.19 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.82 | -9.18 | 101 | 21.8 | -16.77 | -6.23 | -17.77 | 80 |
| 22 | Agent | meta | 90.55 | -9.45 | 139 | 39.6 | -10.32 | -6.22 | -12.22 | 209 |
| 23 | Opening range 30m | breakout | 90.39 | -9.61 | 334 | 33.2 | -12.01 | -3.61 | -17.21 | 581 |
| 24 | Squeeze breakout · 1h | breakout | 89.43 | -10.57 | 61 | 23.0 | -7.76 | -2.58 | -13.79 | 89 |
| 25 | Parabolic SAR · 1h | trend | 88.55 | -11.45 | 149 | 26.8 | -14.10 | -3.26 | -17.40 | 242 |
| 26 | Donchian 55/20 · 1h | breakout | 88.52 | -11.48 | 60 | 13.3 | -14.44 | -3.25 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 88.49 | -11.51 | 35 | 37.1 | -22.01 | -4.47 | -23.13 | 61 |
| 28 | Daily: Bullish score | daily | 88.47 | -11.53 | 14 | 21.4 | -3.92 | -0.40 | -14.73 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.96 | -13.04 | 1 | 0.0 | -2.31 | -0.18 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.59 | -3.83 | -14.77 | 96 |
| 31 | Max aggression: 5-day momentum | meta | 84.84 | -15.16 | 15 | 40.0 | -29.44 | -1.95 | -36.71 | 25 |
| 32 | Stochastic reversion · 1h | reversion | 84.82 | -15.18 | 238 | 46.6 | -22.86 | -4.54 | -25.30 | 390 |
| 33 | Volume breakout · 1h | breakout | 84.64 | -15.36 | 129 | 28.7 | -15.74 | -3.63 | -18.08 | 96 |
| 34 | MFI reversion · 1h | reversion | 84.30 | -15.70 | 301 | 32.9 | -15.15 | -2.37 | -18.15 | 150 |
| 35 | Connors RSI(2) · 1h | reversion | 84.06 | -15.94 | 191 | 40.8 | -20.72 | -6.66 | -21.38 | 138 |
| 36 | Keltner breakout · 1h | breakout | 84.06 | -15.94 | 89 | 23.6 | -21.58 | -4.44 | -23.83 | 176 |
| 37 | ADX DI cross · 1h | trend | 83.38 | -16.62 | 148 | 18.2 | -17.61 | -3.40 | -21.37 | 248 |
| 38 | Opening range 15m | breakout | 83.10 | -16.90 | 409 | 30.3 | -17.40 | -4.99 | -20.73 | 712 |
| 39 | Bollinger breakout · 1h | breakout | 81.55 | -18.45 | 140 | 25.0 | -15.78 | -3.05 | -23.31 | 236 |
| 40 | Ichimoku · 1h | trend | 81.25 | -18.75 | 83 | 13.3 | -18.77 | -3.81 | -25.58 | 120 |
| 41 | EMA 20/50 cross · 1h | trend | 80.13 | -19.87 | 90 | 11.1 | -18.79 | -3.48 | -27.42 | 122 |
| 42 | CCI reversion · 1h | reversion | 79.07 | -20.93 | 268 | 44.8 | -27.07 | -4.26 | -28.63 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.34 | -21.66 | 224 | 38.4 | -29.11 | -5.67 | -31.68 | 377 |
| 44 | MACD zero-line · 1h | trend | 77.98 | -22.02 | 136 | 15.4 | -25.67 | -5.52 | -28.04 | 211 |
| 45 | Supertrend · 1h | trend | 77.85 | -22.15 | 141 | 12.8 | -27.67 | -5.27 | -29.54 | 220 |
| 46 | Z-score reversion · 1h | reversion | 77.81 | -22.19 | 140 | 34.3 | -13.98 | -2.02 | -23.02 | 218 |
| 47 | MACD cross · 1h | trend | 77.33 | -22.67 | 300 | 23.3 | -33.39 | -6.50 | -36.09 | 479 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -26.67 | -3.45 | -33.56 | 33 |
| 49 | Williams %R · 1h | reversion | 76.81 | -23.19 | 274 | 46.0 | -36.83 | -6.56 | -38.02 | 530 |
| 50 | Heikin-Ashi · 1h | trend | 76.45 | -23.55 | 357 | 22.4 | -40.10 | -8.46 | -43.24 | 660 |
| 51 | Triple EMA stack · 1h | trend | 76.43 | -23.57 | 125 | 14.4 | -27.54 | -5.60 | -30.69 | 203 |
| 52 | RSI momentum · 1h | momentum | 76.30 | -23.70 | 135 | 12.6 | -28.59 | -5.54 | -30.24 | 211 |
| 53 | OBV trend · 1h | momentum | 76.12 | -23.88 | 240 | 17.5 | -30.17 | -6.35 | -32.71 | 297 |
| 54 | Donchian 20/10 · 1h | breakout | 75.34 | -24.66 | 119 | 20.2 | -28.13 | -4.94 | -31.45 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.35 | -25.65 | 302 | 25.5 | -32.83 | -6.19 | -35.54 | 375 |
| 56 | RSI(14) reversion · 1h | reversion | 73.14 | -26.86 | 129 | 25.6 | -22.10 | -3.84 | -26.28 | 204 |
| 57 | Candlestick reversal · 1h | reversion | 71.75 | -28.25 | 352 | 28.4 | -34.11 | -6.03 | -38.08 | 550 |
| 58 | Agent (ML meta-label) | meta | 70.56 | -29.44 | 1324 | 20.9 | -10.90 | -2.01 | -18.09 | 280 |
| 59 | Three white soldiers | momentum | 69.44 | -30.56 | 411 | 16.1 | -46.05 | -21.61 | -46.07 | 615 |
| 60 | EMA 9/21 cross · 1h | trend | 68.93 | -31.07 | 218 | 9.6 | -37.37 | -7.61 | -39.06 | 327 |
| 61 | VWAP momentum · 1h | momentum | 68.75 | -31.25 | 699 | 21.6 | -53.17 | -10.44 | -56.25 | 1226 |
| 62 | Max aggression: 1-day momentum | meta | 68.36 | -31.64 | 23 | 30.4 | -32.64 | -1.85 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.31 | -98.96 | 5193 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.44 | -23.73 | -80.27 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -46.27 | -93.52 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.90 | -31.19 | -89.04 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -37.96 | -91.25 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.61 | -32.19 | -90.62 | 2220 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -52.56 | -97.75 | 3472 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -61.33 | -96.29 | 3373 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.39 | -34.30 | -93.50 | 2395 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.53 | -34.02 | -81.79 | 1668 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.63 | -99.48 | 5852 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.90 | -43.44 | -93.00 | 2621 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -36.90 | -95.41 | 3347 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.16 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -44.20 | -91.93 | 2264 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.26 | -26.29 | -74.83 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -61.69 | -97.78 | 3530 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.65 | -98.66 | 4817 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -28.12 | -70.06 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -53.99 | -94.74 | 2775 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.19 | -84.90 | 1812 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.14 | -99.62 | 6294 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.14 | -29.87 | -88.19 | 2231 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.54 | -19.08 | -76.66 | 1690 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -35.79 | -90.32 | 2242 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.68 | -96.46 | 3805 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.16 | -51.34 | -89.21 | 2126 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.27 | -25.04 | -65.64 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.46 | -24.88 | -74.05 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.04 | -18.96 | -77.13 | 1585 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.81 | -49.08 | -96.81 | 4227 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -99.50 | -99.92 | 8215 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T15:50 | Agent (ML meta-label) | buy | SQQQ | 3.67 | — | rebalance up |
| 2026-11-03T15:50 | Agent (ML meta-label) | sell | MSTR | 10.71 | 0.05 | selected signal exited |
| 2026-11-03T15:50 | Agent (ML meta-label) | sell | BITX | 14.10 | 0.09 | selected signal exited |
| 2026-11-03T15:50 | MFI reversion · 1h | sell | AMD | 12.00 | -0.01 | target is flat |
| 2026-11-03T15:50 | Three white soldiers | buy | MSTR | 17.36 | — | entry signal |
| 2026-11-03T15:45 | Agent (rotation) | buy | TQQQ | 7.88 | — | entry |
| 2026-11-03T15:45 | Agent (rotation) | buy | ETHU | 7.88 | — | entry |
| 2026-11-03T15:45 | Agent (rotation) | buy | BITX | 7.88 | — | following Z-score reversion |
| 2026-11-03T15:45 | Agent (ML meta-label) | buy | MSTR | 10.66 | — | entry |
| 2026-11-03T15:45 | Agent (ML meta-label) | sell | NVDA | 7.05 | 0.01 | selected signal exited |
| 2026-11-03T15:45 | Agent (ML meta-label) | sell | BITX | 3.61 | 0.02 | rebalance down |
| 2026-11-03T15:45 | VWAP momentum · 1h | sell | ETHU | 4.91 | 0.02 | target is flat |
| 2026-11-03T15:45 | Opening range 30m | buy | SPY | 8.19 | — | entry signal |
| 2026-11-03T15:45 | Opening range 30m | buy | LABU | 8.21 | — | entry |
| 2026-11-03T15:45 | Opening range 30m | buy | ETHU | 8.21 | — | entry signal |
| 2026-11-03T15:45 | Opening range 30m | buy | BITX | 8.21 | — | entry signal |
| 2026-11-03T15:45 | Opening range 30m | sell | UPRO | 4.60 | 0.00 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | TNA | 4.70 | 0.04 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | MSTR | 4.78 | 0.06 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | MSFT | 4.58 | 0.01 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | META | 4.60 | -0.00 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | IWM | 4.64 | 0.01 | rebalance down |
| 2026-11-03T15:45 | Opening range 30m | sell | COIN | 4.91 | 0.13 | rebalance down |
| 2026-11-03T15:45 | Opening range 15m | buy | UPRO | 7.49 | — | entry |
| 2026-11-03T15:45 | Opening range 15m | buy | ETHU | 7.54 | — | entry signal |
| 2026-11-03T15:45 | Opening range 15m | buy | BITX | 7.54 | — | entry signal |
| 2026-11-03T15:45 | Opening range 15m | sell | TNA | 4.37 | 0.06 | rebalance down |
| 2026-11-03T15:45 | Opening range 15m | sell | MSTR | 4.40 | 0.08 | rebalance down |
| 2026-11-03T15:45 | Opening range 15m | sell | META | 4.25 | 0.01 | rebalance down |
| 2026-11-03T15:45 | Opening range 15m | sell | IWM | 5.00 | 0.01 | rebalance down |
| 2026-11-03T15:45 | Opening range 15m | sell | COIN | 4.56 | 0.16 | rebalance down |
| 2026-11-03T15:45 | Gap and go | buy | TQQQ | 23.12 | — | entry signal |
| 2026-11-03T15:45 | Gap and go | buy | ETHU | 23.26 | — | entry signal |
| 2026-11-03T15:45 | Gap and go | buy | BITX | 23.26 | — | entry signal |
| 2026-11-03T15:43 | Agent (rotation) | sell | TQQQ | 7.85 | -0.03 | selected signal exited |
| 2026-11-03T15:43 | Agent (ML meta-label) | buy | NVDA | 7.05 | — | entry |
| 2026-11-03T15:43 | Agent (ML meta-label) | sell | SQQQ | 3.53 | -0.00 | rebalance down |
| 2026-11-03T15:43 | Agent (ML meta-label) | sell | ETHU | 3.52 | 0.02 | rebalance down |
| 2026-11-03T15:43 | ROC + volume · 1h | sell | TSLA | 7.39 | -0.18 | target is flat |
| 2026-11-03T15:43 | Opening range 15m | buy | LABU | 9.07 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 15:51:05.000135+00:00 -> 2026-11-03 16:01:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 15:51:05.000135+00:00 -> 2026-11-03 16:01:05.000135+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 15:51:05.000135+00:00 -> 2026-11-03 16:01:05.000135+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
