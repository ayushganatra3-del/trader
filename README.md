# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T16:45:05.000133+00:00 · 41570 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.89 (-8.11%)

Closed trades 126, win rate 40.5%, fees £3.70, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 18.56 | +0.22 |
| PLTR | 18.35 | +0.01 |

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

Today: 22395 decisions in 2382 calls, $0.2846 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T16:45 | 1 / 7 / 16 | cash |  |
| Breezy | 2026-10-30T16:45 | 0 / 20 / 4 | cash |  |
| Boozy | 2026-10-30T16:45 | 3 / 19 / 2 | MSTR 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| VWAP reversion | SQQQ | 2.67 | +4.28% | 5 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.17 | 7.17 | 0 | — | 8.45 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.58 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.56 | 3.56 | 22 | 45.5 | 7.45 | 2.42 | -4.92 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.72 | 0.71 | 0 | — | 4.05 | 1.76 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.85 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.61 | -2.39 | 96 | 35.4 | 6.71 | 3.16 | -1.98 | 94 |
| 10 | Hold SPY | benchmark | 97.39 | -2.61 | 0 | — | -1.09 | -0.54 | -3.13 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.47 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.11 | -4.72 | 20 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 14 | Agent (rotation) | meta | 95.24 | -4.76 | 129 | 31.0 | -3.12 | -2.02 | -8.29 | 164 |
| 15 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.46 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.63 | -5.37 | 0 | — | -7.12 | -2.73 | -7.83 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.42 | -5.58 | 0 | — | -3.13 | -1.18 | -6.66 | 1 |
| 19 | Copy: Insider buying | copy | 92.27 | -7.73 | 33 | 36.4 | -22.14 | -4.51 | -23.91 | 69 |
| 20 | Agent | meta | 91.89 | -8.11 | 126 | 40.5 | -9.15 | -5.31 | -12.21 | 224 |
| 21 | Trend pullback · 1h | trend | 91.66 | -8.35 | 100 | 22.0 | -20.88 | -7.42 | -20.99 | 98 |
| 22 | Opening range 30m | breakout | 91.57 | -8.43 | 308 | 35.1 | -11.21 | -3.34 | -17.21 | 591 |
| 23 | Hold BTC | benchmark | 91.36 | -8.64 | 0 | — | -1.22 | -0.03 | -12.47 | 1 |
| 24 | Parabolic SAR · 1h | trend | 91.28 | -8.72 | 140 | 28.6 | -18.19 | -4.15 | -20.27 | 250 |
| 25 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.62 | -16.91 | 1 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.23 | -1.99 | -12.70 | 94 |
| 27 | Donchian 55/20 · 1h | breakout | 90.00 | -10.00 | 54 | 14.8 | -16.23 | -3.61 | -17.38 | 103 |
| 28 | Daily: Bullish score | daily | 88.61 | -11.39 | 14 | 21.4 | -6.66 | -0.82 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) ⏸ | copy | 87.72 | -12.28 | 1 | 0.0 | -4.00 | -0.45 | -14.74 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.10 | -3.66 | -15.04 | 101 |
| 31 | Volume breakout · 1h | breakout | 85.73 | -14.27 | 127 | 29.1 | -13.31 | -2.82 | -16.25 | 105 |
| 32 | Stochastic reversion · 1h | reversion | 85.43 | -14.57 | 221 | 47.5 | -17.78 | -3.08 | -23.72 | 386 |
| 33 | ADX DI cross · 1h | trend | 84.91 | -15.09 | 141 | 19.1 | -16.99 | -3.27 | -20.33 | 260 |
| 34 | Keltner breakout · 1h | breakout | 84.90 | -15.10 | 86 | 24.4 | -24.77 | -4.90 | -25.77 | 189 |
| 35 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 186 | 40.9 | -20.56 | -6.55 | -21.56 | 162 |
| 36 | Opening range 15m | breakout | 83.96 | -16.04 | 382 | 31.7 | -16.14 | -4.62 | -18.52 | 722 |
| 37 | Bollinger breakout · 1h | breakout | 83.23 | -16.77 | 132 | 26.5 | -16.20 | -2.98 | -21.61 | 245 |
| 38 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -24.94 | -3.44 | -27.68 | 35 |
| 39 | Ichimoku · 1h | trend | 82.24 | -17.76 | 78 | 14.1 | -20.58 | -4.11 | -24.80 | 118 |
| 40 | Max aggression: 5-day momentum ⏸ | meta | 82.08 | -17.92 | 15 | 40.0 | -35.57 | -2.59 | -36.37 | 25 |
| 41 | Supertrend · 1h | trend | 81.13 | -18.86 | 133 | 13.5 | -25.63 | -4.77 | -28.87 | 216 |
| 42 | MFI reversion · 1h | reversion | 80.63 | -19.37 | 293 | 31.7 | -18.70 | -2.96 | -20.24 | 153 |
| 43 | CCI reversion · 1h | reversion | 80.41 | -19.59 | 246 | 46.3 | -25.94 | -4.00 | -28.85 | 448 |
| 44 | EMA 20/50 cross · 1h | trend | 79.82 | -20.18 | 88 | 11.4 | -23.62 | -4.46 | -26.95 | 136 |
| 45 | Williams %R · 1h | reversion | 79.35 | -20.65 | 252 | 47.2 | -34.84 | -6.15 | -35.60 | 529 |
| 46 | MACD cross · 1h | trend | 79.34 | -20.66 | 282 | 24.1 | -30.30 | -5.38 | -32.86 | 474 |
| 47 | RSI momentum · 1h | momentum | 79.06 | -20.94 | 129 | 12.4 | -26.99 | -4.88 | -30.14 | 215 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.89 | -27.15 | 214 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.57 | -2.73 | -22.16 | 209 |
| 50 | Triple EMA stack · 1h | trend | 78.43 | -21.57 | 117 | 13.7 | -30.33 | -5.69 | -33.05 | 208 |
| 51 | Heikin-Ashi · 1h | trend | 78.32 | -21.68 | 333 | 23.7 | -41.90 | -9.09 | -42.17 | 668 |
| 52 | Bollinger reversion · 1h | reversion | 78.04 | -21.96 | 196 | 37.8 | -31.06 | -6.48 | -32.42 | 370 |
| 53 | OBV trend · 1h | momentum | 77.52 | -22.48 | 231 | 17.7 | -34.34 | -6.83 | -36.79 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.87 | -24.13 | 116 | 20.7 | -27.93 | -4.88 | -29.81 | 220 |
| 55 | ROC + volume · 1h | momentum | 75.78 | -24.22 | 291 | 25.8 | -29.66 | -5.08 | -31.91 | 386 |
| 56 | Three white soldiers | momentum | 74.11 | -25.89 | 370 | 17.6 | -44.58 | -20.68 | -44.61 | 615 |
| 57 | VWAP momentum · 1h | momentum | 73.53 | -26.47 | 639 | 22.8 | -53.51 | -11.26 | -54.03 | 1238 |
| 58 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -19.90 | -3.48 | -25.90 | 195 |
| 59 | Candlestick reversal · 1h | reversion | 73.25 | -26.75 | 309 | 29.4 | -35.60 | -7.01 | -36.11 | 552 |
| 60 | Agent (ML meta-label) | meta | 72.81 | -27.19 | 1154 | 21.1 | -14.79 | -2.44 | -20.27 | 363 |
| 61 | Max aggression: 1-day momentum | meta | 72.72 | -27.28 | 21 | 33.3 | -28.97 | -1.56 | -50.32 | 42 |
| 62 | EMA 9/21 cross · 1h | trend | 71.37 | -28.63 | 202 | 9.9 | -35.11 | -6.68 | -36.38 | 334 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.97 | -98.88 | 5242 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.39 | -23.74 | -79.39 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -44.45 | -93.56 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.66 | -30.31 | -88.69 | 1918 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.14 | -37.07 | -91.14 | 2347 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -30.50 | -90.01 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -50.83 | -97.72 | 3517 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.14 | -56.47 | -96.14 | 3380 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.04 | -35.45 | -94.04 | 2470 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -32.60 | -81.91 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.35 | -99.47 | 5861 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -43.61 | -92.99 | 2636 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -37.12 | -95.45 | 3456 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.77 | -99.78 | 6209 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.91 | -43.27 | -91.91 | 2309 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.67 | -27.67 | -75.71 | 1573 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -59.80 | -97.67 | 3570 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.67 | -59.73 | -98.67 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.37 | -28.73 | -69.54 | 1212 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -53.83 | -94.81 | 2798 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.89 | -38.70 | -84.91 | 1821 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.53 | -99.61 | 6335 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.21 | -29.91 | -88.24 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.40 | -19.67 | -77.43 | 1713 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.78 | -37.87 | -90.78 | 2263 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.36 | -50.46 | -96.36 | 3812 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.99 | -52.42 | -89.99 | 2145 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.71 | -25.67 | -64.71 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.03 | -25.49 | -74.03 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.85 | -18.33 | -75.89 | 1566 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.75 | -50.38 | -96.75 | 4227 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.91 | -99.92 | 8326 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-30T16:35 | Agent (ML meta-label) | sell | TNA | 4.55 | -0.13 | rebalance down |
| 2026-10-30T16:35 | Agent (ML meta-label) | sell | SQQQ | 6.40 | -0.00 | rebalance down |
| 2026-10-30T16:35 | Agent (ML meta-label) | sell | META | 4.58 | -0.03 | rebalance down |
| 2026-10-30T16:35 | Agent (ML meta-label) | sell | COIN | 3.97 | -0.01 | rebalance down |
| 2026-10-30T16:35 | Agent (ML meta-label) | sell | BITX | 3.97 | -0.01 | rebalance down |
| 2026-10-30T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 103.67 | — | entry |
| 2026-10-30T16:30 | Agent (ML meta-label) | buy | MSTR | 8.63 | — | entry |
| 2026-10-30T16:30 | Agent (ML meta-label) | buy | COIN | 12.17 | — | entry |
| 2026-10-30T16:30 | Agent (ML meta-label) | buy | BITX | 12.17 | — | entry |
| 2026-10-30T16:30 | Agent (ML meta-label) | sell | TSLA | 14.60 | 0.01 | selected signal exited |
| 2026-10-30T16:30 | Agent (ML meta-label) | sell | ETHU | 14.78 | 0.02 | selected signal exited |
| 2026-10-30T16:30 | Stochastic reversion · 1h | buy | SOXL | 9.41 | — | entry signal |
| 2026-10-30T16:30 | Stochastic reversion · 1h | buy | PLTR | 9.52 | — | entry signal |
| 2026-10-30T16:30 | Stochastic reversion · 1h | buy | ETHU | 9.52 | — | entry signal |
| 2026-10-30T16:30 | Stochastic reversion · 1h | buy | COIN | 9.52 | — | entry signal |
| 2026-10-30T16:30 | Stochastic reversion · 1h | buy | BITX | 9.52 | — | entry signal |
| 2026-10-30T16:30 | Stochastic reversion · 1h | sell | SOL-USD | 11.43 | -0.11 | rebalance down |
| 2026-10-30T16:30 | Stochastic reversion · 1h | sell | GOOGL | 12.20 | -0.14 | rebalance down |
| 2026-10-30T16:30 | Stochastic reversion · 1h | sell | ETH-USD | 11.94 | 0.01 | rebalance down |
| 2026-10-30T16:30 | Stochastic reversion · 1h | sell | BTC-USD | 11.92 | -0.01 | rebalance down |
| 2026-10-30T16:30 | Bollinger reversion · 1h | buy | PLTR | 1.04 | — | entry signal |
| 2026-10-30T16:30 | Bollinger reversion · 1h | buy | MSTR | 8.67 | — | entry signal |
| 2026-10-30T16:30 | Candlestick reversal · 1h | buy | PLTR | 8.11 | — | entry signal |
| 2026-10-30T16:30 | Candlestick reversal · 1h | buy | MSFT | 8.17 | — | entry signal |
| 2026-10-30T16:30 | Candlestick reversal · 1h | buy | BITX | 8.17 | — | entry signal |
| 2026-10-30T16:30 | Candlestick reversal · 1h | sell | XRP-USD | 4.06 | 0.00 | rebalance down |
| 2026-10-30T16:30 | Candlestick reversal · 1h | sell | MSTR | 4.15 | 0.05 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 16:45:05.000133+00:00 -> 2026-10-30 16:55:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
