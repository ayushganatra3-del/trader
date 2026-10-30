# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T17:15:05.000134+00:00 · 41599 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.53 (-8.47%)

Closed trades 127, win rate 40.2%, fees £3.71, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 18.40 | +0.06 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 24990 decisions in 2469 calls, $0.3150 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T17:15 | 5 / 13 / 12 | cash |  |
| Breezy | 2026-10-30T17:15 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-30T17:15 | 4 / 20 / 6 | ETHU 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| VWAP reversion | SQQQ | 2.64 | +4.39% | 5 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.17 | 7.17 | 0 | — | 8.45 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.03 | 5.04 | 22 | 45.5 | 8.97 | 2.93 | -4.92 | 27 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.45 | 0.45 | 0 | — | 3.77 | 1.64 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.43 | -2.58 | 96 | 35.4 | 6.26 | 2.93 | -2.21 | 94 |
| 10 | Hold SPY | benchmark | 97.09 | -2.91 | 0 | — | -1.40 | -0.69 | -3.34 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Agent (rotation) | meta | 95.15 | -4.85 | 129 | 31.0 | -3.21 | -2.06 | -8.29 | 164 |
| 15 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.63 | -5.37 | 0 | — | -7.12 | -2.73 | -7.83 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.17 | -5.83 | 0 | — | -3.39 | -1.26 | -6.92 | 1 |
| 19 | Copy: Insider buying | copy | 92.20 | -7.80 | 33 | 36.4 | -22.20 | -4.53 | -23.91 | 69 |
| 20 | Parabolic SAR · 1h | trend | 91.61 | -8.39 | 140 | 28.6 | -17.90 | -4.04 | -20.27 | 250 |
| 21 | Trend pullback · 1h | trend | 91.59 | -8.41 | 100 | 22.0 | -20.93 | -7.44 | -20.99 | 98 |
| 22 | Agent | meta | 91.53 | -8.47 | 127 | 40.2 | -9.48 | -5.52 | -12.21 | 224 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 91.18 | -8.82 | 308 | 35.1 | -11.65 | -3.47 | -17.21 | 591 |
| 25 | Hold BTC | benchmark | 91.09 | -8.91 | 0 | — | -1.52 | -0.08 | -12.47 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.60 | -2.08 | -12.70 | 94 |
| 27 | Donchian 55/20 · 1h | breakout | 89.67 | -10.33 | 54 | 14.8 | -16.45 | -3.65 | -17.41 | 103 |
| 28 | Daily: Bullish score | daily | 88.45 | -11.54 | 14 | 21.4 | -6.84 | -0.85 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -4.69 | -0.55 | -15.31 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 86.04 | -13.96 | 127 | 29.1 | -13.46 | -2.84 | -16.25 | 105 |
| 32 | Keltner breakout · 1h | breakout | 85.20 | -14.80 | 86 | 24.4 | -24.53 | -4.84 | -25.77 | 188 |
| 33 | ADX DI cross · 1h | trend | 85.19 | -14.81 | 141 | 19.1 | -17.33 | -3.38 | -20.33 | 261 |
| 34 | Stochastic reversion · 1h | reversion | 84.83 | -15.17 | 221 | 47.5 | -18.37 | -3.17 | -23.90 | 386 |
| 35 | Connors RSI(2) · 1h | reversion | 83.76 | -16.24 | 186 | 40.9 | -20.98 | -6.70 | -21.56 | 162 |
| 36 | Bollinger breakout · 1h | breakout | 83.52 | -16.48 | 132 | 26.5 | -16.25 | -3.01 | -21.61 | 242 |
| 37 | Opening range 15m | breakout | 83.43 | -16.57 | 383 | 31.6 | -16.78 | -4.81 | -18.77 | 723 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -26.33 | -3.43 | -28.79 | 35 |
| 39 | Ichimoku · 1h | trend | 82.36 | -17.64 | 78 | 14.1 | -20.47 | -4.09 | -24.80 | 118 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -36.11 | -2.60 | -36.37 | 25 |
| 41 | Supertrend · 1h | trend | 81.01 | -18.98 | 133 | 13.5 | -25.74 | -4.78 | -28.87 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.50 | -19.50 | 293 | 31.7 | -18.82 | -2.97 | -20.24 | 154 |
| 43 | CCI reversion · 1h | reversion | 80.41 | -19.59 | 246 | 46.3 | -26.03 | -4.02 | -28.85 | 448 |
| 44 | EMA 20/50 cross · 1h | trend | 79.94 | -20.06 | 88 | 11.4 | -23.08 | -4.34 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.63 | -20.37 | 282 | 24.1 | -30.08 | -5.36 | -32.86 | 474 |
| 46 | Williams %R · 1h | reversion | 79.21 | -20.79 | 252 | 47.2 | -34.97 | -6.17 | -35.60 | 529 |
| 47 | RSI momentum · 1h | momentum | 79.06 | -20.94 | 129 | 12.4 | -27.01 | -4.88 | -30.14 | 215 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.21 | -4.86 | -27.15 | 214 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.92 | -2.77 | -22.16 | 210 |
| 50 | Heikin-Ashi · 1h | trend | 78.60 | -21.40 | 333 | 23.7 | -41.70 | -9.02 | -42.17 | 668 |
| 51 | Triple EMA stack · 1h | trend | 78.28 | -21.71 | 117 | 13.7 | -30.50 | -5.69 | -33.05 | 208 |
| 52 | OBV trend · 1h | momentum | 77.64 | -22.36 | 231 | 17.7 | -34.28 | -6.83 | -36.80 | 300 |
| 53 | Bollinger reversion · 1h | reversion | 77.53 | -22.48 | 196 | 37.8 | -31.56 | -6.55 | -32.42 | 370 |
| 54 | Donchian 20/10 · 1h | breakout | 76.15 | -23.86 | 116 | 20.7 | -27.95 | -4.91 | -29.81 | 220 |
| 55 | ROC + volume · 1h | momentum | 75.92 | -24.08 | 292 | 25.7 | -29.74 | -5.08 | -31.91 | 386 |
| 56 | Three white soldiers | momentum | 74.11 | -25.89 | 370 | 17.6 | -44.51 | -20.64 | -44.54 | 614 |
| 57 | Max aggression: 1-day momentum | meta | 73.75 | -26.25 | 21 | 33.3 | -27.96 | -1.47 | -50.32 | 42 |
| 58 | VWAP momentum · 1h | momentum | 73.72 | -26.27 | 640 | 22.8 | -53.11 | -11.19 | -54.00 | 1234 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.79 | -3.64 | -25.90 | 193 |
| 60 | Candlestick reversal · 1h | reversion | 72.92 | -27.08 | 310 | 29.4 | -35.35 | -6.92 | -35.96 | 549 |
| 61 | Agent (ML meta-label) | meta | 72.31 | -27.69 | 1158 | 21.0 | -14.76 | -2.60 | -20.09 | 371 |
| 62 | EMA 9/21 cross · 1h | trend | 71.23 | -28.77 | 202 | 9.9 | -35.02 | -6.62 | -36.40 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -44.20 | -98.89 | 5245 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.58 | -23.85 | -79.58 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.60 | -44.62 | -93.61 | 2538 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.74 | -30.48 | -88.74 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.19 | -37.43 | -91.19 | 2346 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -30.50 | -90.02 | 2226 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -51.12 | -97.74 | 3515 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -56.16 | -96.13 | 3378 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.92 | -34.90 | -93.94 | 2461 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.77 | -32.34 | -81.91 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.51 | -99.48 | 5867 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.99 | -43.69 | -93.00 | 2635 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.18 | -95.46 | 3456 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.44 | -99.78 | 6213 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -43.97 | -92.00 | 2310 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.71 | -27.66 | -75.75 | 1577 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -59.63 | -97.68 | 3571 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.48 | -98.68 | 4831 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.29 | -28.54 | -69.45 | 1210 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -54.35 | -94.83 | 2799 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -38.28 | -84.88 | 1820 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.66 | -99.62 | 6344 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.29 | -30.01 | -88.31 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.56 | -19.71 | -77.57 | 1716 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.83 | -37.86 | -90.83 | 2273 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.39 | -50.22 | -96.39 | 3825 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.98 | -52.39 | -89.98 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.71 | -25.69 | -64.76 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.94 | -25.49 | -74.03 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.33 | -18.62 | -76.33 | 1573 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -50.29 | -96.79 | 4239 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.62 | -99.92 | 8324 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T17:15 | Agent (ML meta-label) | buy | SOL-USD | 8.04 | — | entry |
| 2026-10-30T17:15 | Agent | sell | PLTR | 18.14 | -0.19 | selected signal exited |
| 2026-10-30T17:05 | Agent (ML meta-label) | buy | SOXL | 4.14 | — | rebalance up |
| 2026-10-30T17:05 | Agent (ML meta-label) | sell | TSLA | 5.10 | -0.02 | selected signal exited |
| 2026-10-30T17:05 | Agent (ML meta-label) | sell | SOL-USD | 7.22 | -0.04 | selected signal exited |
| 2026-10-30T17:05 | Agent (ML meta-label) | sell | ETH-USD | 3.86 | -0.01 | selected signal exited |
| 2026-10-30T17:05 | Opening range 15m | buy | ETHU | 11.94 | — | entry signal |
| 2026-10-30T17:00 | Agent (ML meta-label) | buy | ETH-USD | 3.87 | — | entry |
| 2026-10-30T17:00 | Agent (ML meta-label) | sell | ETHU | 3.87 | 0.02 | rebalance down |
| 2026-10-30T17:00 | ROC + volume · 1h | sell | XRP-USD | 18.72 | -0.24 | exit signal |
| 2026-10-30T17:00 | VWAP momentum · 1h | buy | XRP-USD | 3.72 | — | rebalance up |
| 2026-10-30T17:00 | VWAP momentum · 1h | buy | SQQQ | 5.95 | — | rebalance up |
| 2026-10-30T17:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.73 | — | rebalance up |
| 2026-10-30T17:00 | VWAP momentum · 1h | sell | BTC-USD | 14.63 | -0.14 | exit signal |
| 2026-10-30T16:55 | Agent (ML meta-label) | buy | SOXL | 4.94 | — | following Connors RSI(2) |
| 2026-10-30T16:55 | Agent (ML meta-label) | buy | SOL-USD | 7.26 | — | entry |
| 2026-10-30T16:55 | Agent (ML meta-label) | buy | BITX | 7.26 | — | entry |
| 2026-10-30T16:55 | Agent (ML meta-label) | sell | TNA | 4.77 | -0.14 | rebalance down |
| 2026-10-30T16:55 | Agent (ML meta-label) | sell | SQQQ | 4.98 | 0.04 | rebalance down |
| 2026-10-30T16:55 | Agent (ML meta-label) | sell | META | 4.88 | -0.02 | rebalance down |
| 2026-10-30T16:55 | Agent (ML meta-label) | sell | COIN | 4.83 | -0.02 | rebalance down |
| 2026-10-30T16:50 | Agent (ML meta-label) | buy | TSLA | 5.11 | — | entry |
| 2026-10-30T16:50 | Agent (ML meta-label) | buy | ETHU | 6.95 | — | rebalance up |
| 2026-10-30T16:50 | Agent (ML meta-label) | sell | BITX | 12.06 | -0.11 | selected signal exited |
| 2026-10-30T16:50 | Candlestick reversal · 1h | sell | MSFT | 8.13 | -0.04 | target is flat |
| 2026-10-30T16:50 | Opening range 15m | sell | ETHU | 10.36 | -0.13 | exit signal |
| 2026-10-30T16:46 | MFI reversion · 1h | buy | COIN | 20.16 | — | entry |
| 2026-10-30T16:45 | Agent (ML meta-label) | buy | ETHU | 3.45 | — | entry |
| 2026-10-30T16:45 | Three white soldiers | sell | ETHU | 18.47 | -0.08 | exit signal |
| 2026-10-30T16:40 | Agent (ML meta-label) | buy | TNA | 3.99 | — | rebalance up |
| 2026-10-30T16:40 | Agent (ML meta-label) | buy | SQQQ | 3.98 | — | rebalance up |
| 2026-10-30T16:40 | Agent (ML meta-label) | buy | META | 3.98 | — | rebalance up |
| 2026-10-30T16:40 | Agent (ML meta-label) | buy | COIN | 3.97 | — | rebalance up |
| 2026-10-30T16:40 | Agent (ML meta-label) | buy | BITX | 3.99 | — | rebalance up |
| 2026-10-30T16:40 | Agent (ML meta-label) | sell | SOXL | 7.65 | -0.04 | selected signal exited |
| 2026-10-30T16:40 | Agent (ML meta-label) | sell | SOL-USD | 7.57 | -0.05 | selected signal exited |
| 2026-10-30T16:40 | Agent (ML meta-label) | sell | ETHU | 8.14 | -0.02 | selected signal exited |
| 2026-10-30T16:35 | Agent (ML meta-label) | buy | SOXL | 7.69 | — | following Connors RSI(2) |
| 2026-10-30T16:35 | Agent (ML meta-label) | buy | SOL-USD | 7.62 | — | entry |
| 2026-10-30T16:35 | Agent (ML meta-label) | buy | ETHU | 8.16 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 17:15:05.000134+00:00 -> 2026-10-30 17:25:05.000134+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
