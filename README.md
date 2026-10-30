# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T14:47:05.000368+00:00 · 41480 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.02 (-7.98%)

Closed trades 124, win rate 40.3%, fees £3.66, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| LABU | 18.62 | +0.31 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | — | — | No insider purchases returned |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-29)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.18 · VIX 17.20 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, IWM 5.9, LABU 5.7, AAPL 5.2, SQQQ 4.9, PLTR 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 14436 decisions in 2112 calls, $0.1914 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T14:47 | 2 / 19 / 9 | cash |  |
| Breezy | 2026-10-30T14:47 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-30T14:47 | 4 / 25 / 1 | MSTR 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.92 | 6.92 | 0 | — | 8.09 | 3.97 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.84 | 4.84 | 15 | 73.3 | 5.13 | 1.68 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.66 | 3.66 | 21 | 47.6 | 7.55 | 2.48 | -4.92 | 26 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 101.08 | 1.08 | 0 | — | 4.31 | 1.89 | -5.02 | 1 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.52 | -12.60 | 140 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.84 | -2.16 | 95 | 35.8 | 6.38 | 3.02 | -2.21 | 94 |
| 10 | Hold SPY | benchmark | 97.78 | -2.22 | 0 | — | -0.80 | -0.39 | -3.06 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -3.88 | -5.15 | -4.72 | 20 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 96.83 | -3.17 | 0 | — | -5.05 | -2.03 | -7.83 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 15 | Agent (rotation) | meta | 95.43 | -4.57 | 128 | 31.2 | -2.56 | -1.68 | -8.07 | 151 |
| 16 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.52 | -4.94 | 28 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.87 | -5.13 | 0 | — | -2.77 | -1.08 | -6.39 | 1 |
| 18 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.43 | 1.48 | -8.76 | 203 |
| 19 | Agent | meta | 92.02 | -7.98 | 124 | 40.3 | -8.95 | -5.22 | -12.21 | 221 |
| 20 | Opening range 30m | breakout | 91.83 | -8.17 | 305 | 35.4 | -11.07 | -3.32 | -17.21 | 584 |
| 21 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.11 | -7.49 | -21.17 | 98 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 23 | Parabolic SAR · 1h | trend | 91.21 | -8.79 | 139 | 28.1 | -18.30 | -4.23 | -20.27 | 250 |
| 24 | Hold BTC | benchmark | 90.83 | -9.17 | 0 | — | -1.75 | -0.13 | -12.47 | 1 |
| 25 | Donchian 55/20 · 1h | breakout | 90.78 | -9.22 | 54 | 14.8 | -15.72 | -3.55 | -17.32 | 103 |
| 26 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -7.65 | -2.11 | -12.70 | 94 |
| 27 | Daily: Bullish score | daily | 88.72 | -11.28 | 14 | 21.4 | -6.57 | -0.81 | -14.73 | 14 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 88.30 | -11.70 | 0 | — | -3.56 | -0.39 | -14.57 | 1 |
| 29 | Agent (aggressive) | meta | 87.34 | -12.66 | 63 | 34.9 | -11.10 | -3.69 | -15.04 | 101 |
| 30 | Stochastic reversion · 1h | reversion | 85.43 | -14.57 | 221 | 47.5 | -17.87 | -3.12 | -23.72 | 381 |
| 31 | Volume breakout · 1h | breakout | 85.43 | -14.57 | 127 | 29.1 | -13.64 | -2.92 | -16.21 | 105 |
| 32 | Max aggression: 5-day momentum | meta | 85.00 | -15.00 | 14 | 42.9 | -34.20 | -2.58 | -36.20 | 25 |
| 33 | Connors RSI(2) · 1h | reversion | 84.88 | -15.12 | 186 | 40.9 | -20.01 | -6.37 | -21.56 | 162 |
| 34 | ADX DI cross · 1h | trend | 84.64 | -15.36 | 141 | 19.1 | -17.51 | -3.37 | -20.33 | 261 |
| 35 | Keltner breakout · 1h | breakout | 84.59 | -15.41 | 86 | 24.4 | -25.46 | -5.09 | -25.74 | 189 |
| 36 | Opening range 15m | breakout | 84.20 | -15.80 | 379 | 31.9 | -16.09 | -4.64 | -18.52 | 716 |
| 37 | Bollinger breakout · 1h | breakout | 82.93 | -17.07 | 132 | 26.5 | -16.89 | -3.13 | -21.58 | 245 |
| 38 | Ichimoku · 1h | trend | 82.56 | -17.44 | 78 | 14.1 | -20.31 | -4.10 | -24.80 | 117 |
| 39 | Daily: Momentum burst ⏸ | daily | 82.42 | -17.58 | 19 | 15.8 | -22.39 | -3.46 | -26.56 | 35 |
| 40 | Supertrend · 1h | trend | 81.46 | -18.54 | 133 | 13.5 | -25.42 | -4.79 | -28.87 | 216 |
| 41 | MFI reversion · 1h | reversion | 80.55 | -19.45 | 292 | 31.8 | -17.68 | -2.82 | -20.24 | 152 |
| 42 | CCI reversion · 1h | reversion | 80.22 | -19.78 | 246 | 46.3 | -26.03 | -4.04 | -28.85 | 450 |
| 43 | EMA 20/50 cross · 1h | trend | 79.96 | -20.04 | 88 | 11.4 | -23.51 | -4.47 | -26.95 | 136 |
| 44 | RSI momentum · 1h | momentum | 79.67 | -20.33 | 127 | 12.6 | -26.66 | -4.92 | -30.13 | 215 |
| 45 | Williams %R · 1h | reversion | 79.44 | -20.56 | 252 | 47.2 | -34.81 | -6.20 | -35.60 | 528 |
| 46 | MACD cross · 1h | trend | 79.04 | -20.96 | 282 | 24.1 | -30.61 | -5.46 | -32.86 | 473 |
| 47 | Triple EMA stack · 1h | trend | 78.98 | -21.02 | 117 | 13.7 | -29.90 | -5.70 | -33.05 | 208 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.33 | -4.93 | -27.15 | 214 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 78.60 | -21.40 | 131 | 34.4 | -17.87 | -2.78 | -22.16 | 207 |
| 50 | Heikin-Ashi · 1h | trend | 78.18 | -21.82 | 333 | 23.7 | -42.01 | -9.21 | -42.16 | 667 |
| 51 | Bollinger reversion · 1h | reversion | 77.91 | -22.09 | 195 | 37.9 | -31.07 | -6.52 | -32.42 | 367 |
| 52 | OBV trend · 1h | momentum | 77.86 | -22.14 | 230 | 17.8 | -32.70 | -6.67 | -35.51 | 300 |
| 53 | Donchian 20/10 · 1h | breakout | 75.96 | -24.04 | 114 | 21.1 | -28.17 | -4.96 | -29.78 | 220 |
| 54 | ROC + volume · 1h | momentum | 75.65 | -24.35 | 291 | 25.8 | -29.81 | -5.17 | -31.91 | 384 |
| 55 | Three white soldiers | momentum | 74.33 | -25.66 | 365 | 17.8 | -44.42 | -20.84 | -44.48 | 614 |
| 56 | Agent (ML meta-label) | meta | 73.62 | -26.38 | 1138 | 20.9 | -11.59 | -1.85 | -17.70 | 344 |
| 57 | VWAP momentum · 1h | momentum | 73.34 | -26.66 | 638 | 22.9 | -52.37 | -11.24 | -52.79 | 1237 |
| 58 | RSI(14) reversion · 1h ⏸ | reversion | 73.26 | -26.74 | 118 | 26.3 | -20.28 | -3.56 | -25.90 | 195 |
| 59 | Candlestick reversal · 1h | reversion | 73.21 | -26.79 | 309 | 29.4 | -35.04 | -6.98 | -35.42 | 549 |
| 60 | EMA 9/21 cross · 1h | trend | 71.79 | -28.21 | 202 | 9.9 | -35.41 | -6.90 | -36.33 | 336 |
| 61 | Max aggression: 1-day momentum | meta | 71.68 | -28.32 | 21 | 33.3 | -30.06 | -1.67 | -50.32 | 42 |
| 62 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.18 | -98.90 | 5235 |
| 63 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.25 | -24.08 | -79.25 | 1416 |
| 64 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.54 | -45.90 | -93.54 | 2537 |
| 65 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.59 | -30.82 | -88.67 | 1910 |
| 66 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.13 | -37.70 | -91.15 | 2345 |
| 67 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.07 | -31.61 | -90.07 | 2231 |
| 68 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -52.04 | -97.69 | 3501 |
| 69 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.11 | -58.73 | -96.11 | 3384 |
| 70 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -36.81 | -94.06 | 2475 |
| 71 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.87 | -33.72 | -81.88 | 1682 |
| 72 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -57.75 | -99.47 | 5827 |
| 73 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.91 | -44.16 | -92.91 | 2627 |
| 74 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.47 | -38.62 | -95.47 | 3454 |
| 75 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -79.66 | -99.78 | 6200 |
| 76 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -43.91 | -91.87 | 2300 |
| 77 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.51 | -28.08 | -75.54 | 1575 |
| 78 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -63.92 | -97.68 | 3571 |
| 79 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -63.60 | -98.67 | 4816 |
| 80 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 81 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.33 | -28.93 | -69.53 | 1211 |
| 82 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -54.93 | -94.75 | 2789 |
| 83 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -38.46 | -84.69 | 1815 |
| 84 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -73.12 | -99.61 | 6317 |
| 85 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -30.56 | -88.23 | 2239 |
| 86 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.16 | -19.91 | -77.29 | 1704 |
| 87 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.75 | -38.72 | -90.81 | 2265 |
| 88 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.30 | -52.92 | -96.33 | 3808 |
| 89 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.82 | -54.42 | -89.82 | 2132 |
| 90 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.86 | -26.38 | -64.86 | 829 |
| 91 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.78 | -25.84 | -73.78 | 1276 |
| 92 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.84 | -18.56 | -75.88 | 1558 |
| 93 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.71 | -52.60 | -96.75 | 4218 |
| 94 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -107.46 | -99.92 | 8304 |
| 95 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T14:45 | Agent (ML meta-label) | sell | IWM | 12.23 | -0.00 | selected signal exited |
| 2026-10-30T14:45 | Donchian 55/20 · 1h | buy | SQQQ | 4.79 | — | rebalance up |
| 2026-10-30T14:45 | Donchian 55/20 · 1h | sell | LABU | 4.79 | -0.11 | rebalance down |
| 2026-10-30T14:45 | OBV trend · 1h | sell | IWM | 19.54 | 0.03 | target is flat |
| 2026-10-30T14:45 | Three white soldiers | buy | LABU | 18.59 | — | entry signal |
| 2026-10-30T14:45 | Opening range 30m | buy | AAPL | 22.96 | — | entry signal |
| 2026-10-30T14:45 | Opening range 15m | buy | AAPL | 21.05 | — | entry signal |
| 2026-10-30T14:41 | Agent (rotation) | sell | SQQQ | 7.51 | -0.11 | rebalance down |
| 2026-10-30T14:41 | Agent (ML meta-label) | buy | SOL-USD | 12.20 | — | entry |
| 2026-10-30T14:41 | Agent (ML meta-label) | buy | LABU | 12.23 | — | following Candlestick reversal |
| 2026-10-30T14:41 | Agent (ML meta-label) | buy | IWM | 12.23 | — | entry |
| 2026-10-30T14:41 | Agent (ML meta-label) | sell | TSLA | 18.41 | 0.05 | selected signal exited |
| 2026-10-30T14:41 | Agent (ML meta-label) | sell | TNA | 6.13 | -0.13 | rebalance down |
| 2026-10-30T14:41 | Agent (ML meta-label) | sell | SQQQ | 5.97 | 0.22 | rebalance down |
| 2026-10-30T14:41 | Agent (ML meta-label) | sell | ETH-USD | 6.14 | -0.01 | rebalance down |
| 2026-10-30T14:41 | Agent (aggressive) | sell | LABU | 43.64 | -0.07 | selected signal exited |
| 2026-10-30T14:41 | Agent | sell | TSLA | 18.51 | 0.19 | selected signal exited |
| 2026-10-30T14:41 | Three white soldiers | buy | TECL | 18.58 | — | entry signal |
| 2026-10-30T14:41 | Three white soldiers | buy | AAPL | 18.58 | — | entry signal |
| 2026-10-30T14:41 | Opening range 30m | sell | SQQQ | 22.55 | -0.37 | exit signal |
| 2026-10-30T14:41 | Opening range 15m | sell | SQQQ | 20.63 | -0.34 | exit signal |
| 2026-10-30T14:41 | Gap and go | sell | SQQQ | 23.55 | -0.22 | exit signal |
| 2026-10-30T14:36 | Agent (ML meta-label) | buy | TSLA | 18.36 | — | following Z-score reversion |
| 2026-10-30T14:36 | Agent (ML meta-label) | buy | ETH-USD | 18.36 | — | entry |
| 2026-10-30T14:36 | Agent (ML meta-label) | sell | LABU | 18.36 | -0.05 | selected signal exited |
| 2026-10-30T14:36 | Agent (ML meta-label) | sell | IWM | 18.39 | -0.19 | selected signal exited |
| 2026-10-30T14:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 104.82 | — | entry |
| 2026-10-30T14:30 | Agent (ML meta-label) | buy | TNA | 9.02 | — | rebalance up |
| 2026-10-30T14:30 | Agent (ML meta-label) | buy | SQQQ | 6.49 | — | rebalance up |
| 2026-10-30T14:30 | Agent (ML meta-label) | buy | LABU | 18.41 | — | following Candlestick reversal |
| 2026-10-30T14:30 | Agent (ML meta-label) | buy | IWM | 7.53 | — | rebalance up |
| 2026-10-30T14:30 | Agent (ML meta-label) | sell | TSLA | 8.06 | 0.01 | selected signal exited |
| 2026-10-30T14:30 | Agent (ML meta-label) | sell | SOL-USD | 12.23 | -0.04 | selected signal exited |
| 2026-10-30T14:30 | Agent (ML meta-label) | sell | META | 8.92 | -0.17 | selected signal exited |
| 2026-10-30T14:30 | Agent (ML meta-label) | sell | ETH-USD | 12.23 | -0.09 | selected signal exited |
| 2026-10-30T14:30 | Connors RSI(2) · 1h | buy | TSLA | 21.10 | — | entry signal |
| 2026-10-30T14:30 | Connors RSI(2) · 1h | buy | TNA | 21.10 | — | entry signal |
| 2026-10-30T14:30 | Connors RSI(2) · 1h | buy | IWM | 21.10 | — | entry signal |
| 2026-10-30T14:30 | Connors RSI(2) · 1h | buy | AAPL | 21.10 | — | entry signal |
| 2026-10-30T14:30 | Volume breakout · 1h | buy | SQQQ | 21.42 | — | entry signal |

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
