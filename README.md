# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T19:22:05.000159+00:00 · 46473 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.54 (-9.46%)

Closed trades 141, win rate 39.0%, fees £3.96, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 30168 decisions in 2811 calls, $0.3766 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T19:22 | 8 / 16 / 7 | NANC 20% |  |
| Breezy | 2026-11-03T19:22 | 0 / 31 / 0 | cash |  |
| Boozy | 2026-11-03T19:22 | 6 / 24 / 1 | COIN 71% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.29 | 9.29 | 0 | — | 10.10 | 4.39 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 1.16 | 0.50 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.62 | 0.62 | 26 | 26.9 | 8.34 | 2.12 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.85 | -3.55 | -13.12 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.97 | -3.03 | 0 | — | -1.85 | -0.97 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.39 | -3.61 | 107 | 34.6 | 4.38 | 2.10 | -3.79 | 94 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.33 | -3.67 | 5 | 40.0 | 2.53 | 0.69 | -7.93 | 8 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 96.01 | -3.98 | 0 | — | -0.63 | -0.17 | -6.60 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.24 | -4.76 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.54 | -5.46 | 0 | — | -3.19 | -1.21 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.61 | -5.33 | 29 |
| 17 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -5.15 | -3.05 | -8.68 | 185 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | 0.34 | 0.20 | -9.15 | 218 |
| 19 | Hold BTC | benchmark | 91.39 | -8.61 | 0 | — | -0.20 | 0.14 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.69 | -9.31 | 102 | 21.6 | -16.50 | -6.11 | -17.45 | 79 |
| 22 | Agent | meta | 90.54 | -9.46 | 141 | 39.0 | -10.29 | -6.20 | -12.22 | 209 |
| 23 | Opening range 30m | breakout | 89.98 | -10.02 | 337 | 32.9 | -12.76 | -3.89 | -17.21 | 591 |
| 24 | Squeeze breakout · 1h | breakout | 89.32 | -10.69 | 61 | 23.0 | -8.21 | -2.76 | -13.79 | 86 |
| 25 | Parabolic SAR · 1h | trend | 88.51 | -11.49 | 150 | 26.7 | -14.09 | -3.28 | -17.40 | 242 |
| 26 | Donchian 55/20 · 1h | breakout | 88.45 | -11.55 | 60 | 13.3 | -14.56 | -3.28 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 88.42 | -11.59 | 35 | 37.1 | -22.31 | -4.55 | -23.13 | 61 |
| 28 | Daily: Bullish score | daily | 88.41 | -11.59 | 14 | 21.4 | -5.40 | -0.64 | -14.82 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.63 | -13.37 | 1 | 0.0 | -6.05 | -0.84 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 84.96 | -15.04 | 15 | 40.0 | -29.41 | -1.94 | -36.71 | 25 |
| 32 | Stochastic reversion · 1h | reversion | 84.71 | -15.29 | 241 | 46.9 | -23.96 | -4.83 | -26.15 | 390 |
| 33 | Volume breakout · 1h | breakout | 84.64 | -15.36 | 129 | 28.7 | -16.38 | -3.78 | -18.08 | 96 |
| 34 | MFI reversion · 1h | reversion | 84.37 | -15.63 | 306 | 33.3 | -14.76 | -2.29 | -18.08 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.09 | -15.91 | 89 | 23.6 | -22.72 | -4.73 | -23.75 | 172 |
| 36 | Connors RSI(2) · 1h | reversion | 83.97 | -16.04 | 191 | 40.8 | -20.00 | -6.54 | -20.56 | 134 |
| 37 | ADX DI cross · 1h | trend | 83.12 | -16.88 | 148 | 18.2 | -18.28 | -3.56 | -21.54 | 252 |
| 38 | Opening range 15m | breakout | 82.72 | -17.28 | 411 | 30.2 | -17.64 | -5.00 | -20.73 | 722 |
| 39 | Bollinger breakout · 1h | breakout | 81.44 | -18.56 | 140 | 25.0 | -17.33 | -3.50 | -23.31 | 231 |
| 40 | Ichimoku · 1h | trend | 81.18 | -18.82 | 84 | 13.1 | -17.87 | -3.62 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.72 | -20.28 | 90 | 11.1 | -19.84 | -3.73 | -27.42 | 124 |
| 42 | CCI reversion · 1h | reversion | 79.09 | -20.91 | 268 | 44.8 | -25.43 | -4.02 | -27.71 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.21 | -21.79 | 225 | 38.7 | -27.75 | -5.47 | -30.25 | 376 |
| 44 | MACD zero-line · 1h | trend | 77.81 | -22.19 | 136 | 15.4 | -25.05 | -5.49 | -27.28 | 214 |
| 45 | Supertrend · 1h | trend | 77.75 | -22.25 | 141 | 12.8 | -27.81 | -5.30 | -29.54 | 222 |
| 46 | Z-score reversion · 1h | reversion | 77.44 | -22.56 | 142 | 34.5 | -14.53 | -2.11 | -23.02 | 218 |
| 47 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.10 | -3.53 | -33.57 | 33 |
| 48 | MACD cross · 1h | trend | 76.99 | -23.01 | 301 | 23.6 | -34.33 | -6.64 | -36.66 | 484 |
| 49 | Williams %R · 1h | reversion | 76.74 | -23.25 | 278 | 46.4 | -36.55 | -6.53 | -37.66 | 531 |
| 50 | RSI momentum · 1h | momentum | 76.41 | -23.59 | 136 | 12.5 | -28.55 | -5.57 | -30.59 | 214 |
| 51 | Triple EMA stack · 1h | trend | 76.17 | -23.83 | 126 | 14.3 | -28.67 | -5.70 | -31.34 | 205 |
| 52 | Heikin-Ashi · 1h | trend | 75.91 | -24.09 | 357 | 22.4 | -41.42 | -8.76 | -44.15 | 667 |
| 53 | OBV trend · 1h | momentum | 75.65 | -24.35 | 240 | 17.5 | -30.60 | -6.44 | -32.67 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.16 | -24.84 | 120 | 20.0 | -29.49 | -5.39 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 73.95 | -26.05 | 304 | 25.7 | -36.58 | -7.27 | -36.71 | 377 |
| 56 | RSI(14) reversion · 1h | reversion | 72.90 | -27.10 | 130 | 26.2 | -20.46 | -3.58 | -26.28 | 208 |
| 57 | Candlestick reversal · 1h | reversion | 70.92 | -29.07 | 359 | 28.7 | -34.99 | -6.62 | -38.24 | 551 |
| 58 | Agent (ML meta-label) | meta | 69.80 | -30.20 | 1366 | 21.7 | -11.37 | -2.11 | -16.32 | 285 |
| 59 | Three white soldiers | momentum | 69.09 | -30.91 | 416 | 16.1 | -46.39 | -21.73 | -46.39 | 619 |
| 60 | EMA 9/21 cross · 1h | trend | 69.07 | -30.93 | 219 | 9.6 | -37.18 | -7.50 | -38.85 | 330 |
| 61 | Max aggression: 1-day momentum | meta | 68.45 | -31.55 | 23 | 30.4 | -32.60 | -1.84 | -50.32 | 42 |
| 62 | VWAP momentum · 1h | momentum | 68.39 | -31.61 | 701 | 21.7 | -53.50 | -10.55 | -56.27 | 1236 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.26 | -98.96 | 5159 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.29 | -23.21 | -80.26 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -44.57 | -93.40 | 2520 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.74 | -30.39 | -89.04 | 1905 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -36.56 | -91.10 | 2328 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.63 | -31.95 | -90.74 | 2218 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -50.63 | -97.70 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -56.22 | -96.28 | 3379 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.58 | -34.28 | -93.58 | 2396 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.67 | -33.94 | -82.13 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -52.09 | -99.48 | 5863 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -42.61 | -92.96 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.36 | -36.92 | -95.36 | 3364 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.00 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.86 | -43.84 | -91.89 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.73 | -25.81 | -75.14 | 1552 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -59.99 | -97.79 | 3526 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -60.37 | -98.68 | 4804 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.42 | -28.52 | -70.34 | 1190 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -52.24 | -94.71 | 2778 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -36.23 | -84.74 | 1808 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.43 | -99.62 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.07 | -29.65 | -88.21 | 2225 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.12 | -18.55 | -76.65 | 1688 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.06 | -36.13 | -90.10 | 2208 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.42 | -96.43 | 3802 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -52.65 | -89.31 | 2130 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.46 | -26.98 | -65.97 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.40 | -24.65 | -74.10 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.92 | -18.81 | -77.14 | 1588 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.81 | -48.97 | -96.81 | 4227 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -96.40 | -99.92 | 8204 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T19:10 | Agent (ML meta-label) | buy | TSLA | 6.17 | — | rebalance up |
| 2026-11-03T19:10 | Agent (ML meta-label) | buy | SQQQ | 6.16 | — | rebalance up |
| 2026-11-03T19:10 | Agent (ML meta-label) | buy | MSTR | 6.20 | — | rebalance up |
| 2026-11-03T19:10 | Agent (ML meta-label) | buy | ETHU | 6.20 | — | rebalance up |
| 2026-11-03T19:10 | Agent (ML meta-label) | buy | BITX | 6.21 | — | rebalance up |
| 2026-11-03T19:10 | Agent (ML meta-label) | sell | UPRO | 7.74 | -0.03 | selected signal exited |
| 2026-11-03T19:10 | Agent (ML meta-label) | sell | TQQQ | 7.75 | -0.03 | selected signal exited |
| 2026-11-03T19:10 | Agent (ML meta-label) | sell | SOXL | 7.71 | -0.07 | selected signal exited |
| 2026-11-03T19:10 | Agent (ML meta-label) | sell | COIN | 7.75 | -0.02 | selected signal exited |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | UPRO | 7.76 | — | entry |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | TQQQ | 7.78 | — | entry |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | SOXL | 7.78 | — | following Connors RSI(2) |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | MSTR | 7.78 | — | entry |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | COIN | 7.78 | — | entry |
| 2026-11-03T19:05 | Agent (ML meta-label) | buy | BITX | 7.78 | — | following Z-score reversion |
| 2026-11-03T19:05 | Agent (ML meta-label) | sell | TSLA | 9.73 | 0.00 | rebalance down |
| 2026-11-03T19:05 | Agent (ML meta-label) | sell | SQQQ | 9.74 | 0.00 | rebalance down |
| 2026-11-03T19:05 | Agent (ML meta-label) | sell | ETHU | 9.70 | -0.03 | rebalance down |
| 2026-11-03T19:00 | Agent (ML meta-label) | buy | TSLA | 8.75 | — | rebalance up |
| 2026-11-03T19:00 | Agent (ML meta-label) | buy | SQQQ | 8.76 | — | rebalance up |
| 2026-11-03T19:00 | Agent (ML meta-label) | buy | ETHU | 8.75 | — | rebalance up |
| 2026-11-03T19:00 | Agent (ML meta-label) | sell | UPRO | 8.74 | 0.00 | selected signal exited |
| 2026-11-03T19:00 | Agent (ML meta-label) | sell | TQQQ | 8.76 | 0.01 | selected signal exited |
| 2026-11-03T19:00 | Agent (ML meta-label) | sell | SOXL | 8.77 | 0.02 | selected signal exited |
| 2026-11-03T19:00 | Agent (ML meta-label) | sell | MSTR | 8.75 | -0.04 | selected signal exited |
| 2026-11-03T19:00 | Agent (ML meta-label) | sell | BITX | 8.74 | -0.04 | selected signal exited |
| 2026-11-03T18:55 | Agent (ML meta-label) | buy | UPRO | 8.74 | — | entry |
| 2026-11-03T18:55 | Agent (ML meta-label) | buy | TQQQ | 8.75 | — | entry |
| 2026-11-03T18:55 | Agent (ML meta-label) | buy | SOXL | 8.75 | — | following Connors RSI(2) |
| 2026-11-03T18:55 | Agent (ML meta-label) | sell | TSLA | 5.26 | 0.00 | rebalance down |
| 2026-11-03T18:55 | Agent (ML meta-label) | sell | SQQQ | 5.29 | 0.00 | rebalance down |
| 2026-11-03T18:55 | Agent (ML meta-label) | sell | MSTR | 5.23 | -0.02 | rebalance down |
| 2026-11-03T18:55 | Agent (ML meta-label) | sell | ETHU | 5.23 | -0.02 | rebalance down |
| 2026-11-03T18:55 | Agent (ML meta-label) | sell | BITX | 5.22 | -0.02 | rebalance down |
| 2026-11-03T18:55 | MFI reversion · 1h | buy | TSLA | 16.89 | — | entry |
| 2026-11-03T18:55 | MFI reversion · 1h | sell | LABU | 16.96 | 0.55 | target is flat |
| 2026-11-03T18:53 | Candlestick reversal · 1h | buy | AMD | 4.60 | — | rebalance up |
| 2026-11-03T18:53 | Candlestick reversal · 1h | sell | ETHU | 4.60 | -0.01 | target is flat |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | TSLA | 4.38 | — | rebalance up |
| 2026-11-03T18:50 | Agent (ML meta-label) | buy | SQQQ | 4.40 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 19:22:05.000159+00:00 -> 2026-11-03 19:32:05.000159+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 19:22:05.000159+00:00 -> 2026-11-03 19:32:05.000159+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 19:22:05.000159+00:00 -> 2026-11-03 19:32:05.000159+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
