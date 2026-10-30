# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T13:15:05.000135+00:00 · 41418 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.68 (-8.32%)

Closed trades 122, win rate 40.2%, fees £3.61, max drawdown -11.45%.

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

Today: 9630 decisions in 1926 calls, $0.1347 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T13:15 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-10-30T13:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T13:15 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.77 | +1.01% | 7 |
| Candlestick reversal | LABU | 2.56 | +7.90% | 14 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Candlestick reversal | PLTR | 2.37 | +5.05% | 17 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.23 | 2.03 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 105.94 | 5.94 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.76 | 0.76 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.67 | -1.33 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 6.78 | 3.18 | -1.98 | 91 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.77 | -3.23 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.50 | -3.50 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.20 | -2.06 | -7.40 | 174 |
| 17 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.27 | 1.72 | -8.76 | 204 |
| 18 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.74 | -2.50 | -4.94 | 28 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.18 | -6.82 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.40 | -7.60 | 33 | 36.4 | -21.70 | -4.41 | -23.91 | 67 |
| 21 | Donchian 55/20 · 1h | breakout | 92.06 | -7.94 | 54 | 14.8 | -13.77 | -3.09 | -15.51 | 102 |
| 22 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 23 | Daily: Momentum burst | daily | 91.71 | -8.29 | 15 | 13.3 | -12.93 | -2.42 | -17.57 | 35 |
| 24 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.57 | -5.72 | -12.21 | 221 |
| 25 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.17 | -7.34 | -21.50 | 99 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 27 | Hold BTC | benchmark | 90.95 | -9.05 | 0 | — | -0.94 | 0.02 | -12.47 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.49 | -9.51 | 56 | 23.2 | -4.98 | -1.35 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.29 | -9.71 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 89.94 | -10.06 | 137 | 28.5 | -19.83 | -4.61 | -19.94 | 247 |
| 31 | ADX DI cross · 1h | trend | 89.20 | -10.79 | 137 | 19.7 | -15.02 | -3.02 | -16.59 | 260 |
| 32 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 33 | Stochastic reversion · 1h | reversion | 87.66 | -12.34 | 218 | 48.2 | -16.18 | -2.81 | -22.69 | 381 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.42 | -13.58 | 124 | 29.8 | -14.59 | -3.11 | -17.32 | 106 |
| 36 | Bollinger breakout · 1h | breakout | 85.74 | -14.26 | 128 | 26.6 | -11.99 | -2.16 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.36 | -14.64 | 126 | 35.7 | -14.06 | -2.20 | -21.48 | 207 |
| 38 | Keltner breakout · 1h | breakout | 85.23 | -14.77 | 84 | 23.8 | -22.88 | -4.62 | -23.96 | 196 |
| 39 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 40 | Ichimoku · 1h | trend | 84.22 | -15.78 | 75 | 10.7 | -18.45 | -3.69 | -24.73 | 117 |
| 41 | Connors RSI(2) · 1h | reversion | 84.14 | -15.86 | 185 | 40.5 | -20.46 | -6.51 | -21.55 | 159 |
| 42 | Supertrend · 1h | trend | 83.58 | -16.42 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.17 | -16.83 | 122 | 13.1 | -20.32 | -4.02 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.30 | -17.70 | 113 | 14.2 | -27.60 | -5.32 | -30.37 | 207 |
| 45 | MFI reversion · 1h | reversion | 81.86 | -18.14 | 288 | 32.3 | -17.80 | -2.82 | -19.58 | 152 |
| 46 | Williams %R · 1h | reversion | 81.57 | -18.43 | 249 | 47.8 | -33.74 | -5.95 | -34.73 | 529 |
| 47 | EMA 20/50 cross · 1h | trend | 81.47 | -18.53 | 86 | 11.6 | -21.79 | -3.91 | -24.96 | 137 |
| 48 | MACD cross · 1h | trend | 80.98 | -19.02 | 276 | 24.6 | -27.72 | -4.96 | -29.62 | 475 |
| 49 | Bollinger reversion · 1h | reversion | 80.81 | -19.19 | 191 | 38.7 | -30.21 | -6.26 | -31.74 | 369 |
| 50 | CCI reversion · 1h | reversion | 80.80 | -19.20 | 245 | 46.5 | -22.18 | -3.13 | -28.07 | 452 |
| 51 | Donchian 20/10 · 1h | breakout | 80.38 | -19.62 | 108 | 21.3 | -22.28 | -4.08 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.37 | -20.63 | 225 | 16.9 | -33.81 | -6.56 | -36.19 | 299 |
| 53 | MACD zero-line · 1h | trend | 79.07 | -20.93 | 129 | 16.3 | -23.89 | -4.78 | -26.72 | 212 |
| 54 | RSI(14) reversion · 1h | reversion | 78.00 | -22.00 | 113 | 26.5 | -21.53 | -3.97 | -24.99 | 204 |
| 55 | Candlestick reversal · 1h | reversion | 76.64 | -23.36 | 304 | 29.9 | -34.48 | -6.87 | -35.61 | 545 |
| 56 | Heikin-Ashi · 1h | trend | 76.59 | -23.41 | 331 | 23.6 | -42.27 | -9.16 | -42.43 | 667 |
| 57 | ROC + volume · 1h | momentum | 76.34 | -23.66 | 286 | 25.9 | -30.63 | -5.37 | -32.03 | 387 |
| 58 | Agent (ML meta-label) | meta | 75.75 | -24.25 | 1121 | 20.9 | -16.35 | -3.51 | -20.71 | 350 |
| 59 | EMA 9/21 cross · 1h | trend | 74.51 | -25.49 | 195 | 10.3 | -31.26 | -6.23 | -32.26 | 340 |
| 60 | Three white soldiers | momentum | 74.32 | -25.68 | 365 | 17.8 | -44.40 | -20.53 | -44.43 | 612 |
| 61 | VWAP momentum · 1h | momentum | 73.25 | -26.75 | 633 | 22.9 | -51.62 | -10.92 | -51.88 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -43.40 | -98.88 | 5188 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.86 | -23.45 | -78.86 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -44.11 | -93.49 | 2528 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.66 | -30.32 | -88.66 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.13 | -36.94 | -91.16 | 2339 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.13 | -30.81 | -90.13 | 2232 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -50.36 | -97.69 | 3497 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -55.36 | -96.09 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.96 | -35.21 | -93.96 | 2467 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.82 | -32.63 | -81.83 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -54.71 | -99.46 | 5790 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -42.23 | -92.84 | 2626 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.45 | -36.93 | -95.45 | 3451 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -73.68 | -99.78 | 6180 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.81 | -42.48 | -91.83 | 2298 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.29 | -27.46 | -75.29 | 1569 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -59.82 | -97.67 | 3570 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -59.57 | -98.64 | 4786 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.70 | -28.62 | -69.90 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -52.71 | -94.75 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.72 | -37.82 | -84.72 | 1824 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -68.04 | -99.60 | 6290 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.73 | -88.15 | 2211 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.17 | -19.65 | -77.34 | 1683 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.68 | -37.74 | -90.68 | 2239 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -50.64 | -96.28 | 3778 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.78 | -51.55 | -89.78 | 2133 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.41 | -25.44 | -64.41 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.49 | -25.28 | -73.49 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.76 | -18.21 | -75.80 | 1558 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.70 | -50.23 | -96.70 | 4194 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -99.66 | -99.92 | 8294 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T12:45 | Agent (ML meta-label) | buy | ETH-USD | 4.29 | — | entry |
| 2026-10-30T12:45 | Agent (ML meta-label) | sell | SOL-USD | 4.29 | -0.04 | rebalance down |
| 2026-10-30T12:20 | Agent (ML meta-label) | buy | SOL-USD | 5.89 | — | rebalance up |
| 2026-10-30T12:20 | Agent (ML meta-label) | sell | ETH-USD | 5.89 | -0.03 | selected signal exited |
| 2026-10-30T12:16 | Agent (ML meta-label) | buy | SOL-USD | 2.83 | — | entry |
| 2026-10-30T12:05 | Agent (ML meta-label) | sell | SOL-USD | 2.83 | -0.02 | selected signal exited |
| 2026-10-30T12:00 | VWAP momentum · 1h | buy | ETH-USD | 9.07 | — | entry |
| 2026-10-30T12:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.42 | — | rebalance up |
| 2026-10-30T12:00 | VWAP momentum · 1h | sell | BTC-USD | 14.49 | -0.27 | exit signal |
| 2026-10-30T11:00 | Agent (ML meta-label) | buy | ETH-USD | 2.85 | — | rebalance up |
| 2026-10-30T11:00 | Agent (ML meta-label) | sell | DOGE-USD | 2.85 | 0.01 | selected signal exited |
| 2026-10-30T11:00 | MACD cross · 1h | buy | ETH-USD | 8.14 | — | entry signal |
| 2026-10-30T10:15 | Agent (ML meta-label) | buy | ETH-USD | 3.08 | — | entry |
| 2026-10-30T10:15 | Agent (ML meta-label) | buy | DOGE-USD | 2.84 | — | entry |
| 2026-10-30T10:15 | Agent (ML meta-label) | sell | SOL-USD | 5.56 | -0.03 | rebalance down |
| 2026-10-30T10:05 | Agent (ML meta-label) | buy | SOL-USD | 8.44 | — | entry |
| 2026-10-30T10:05 | Agent (ML meta-label) | sell | ETH-USD | 1.95 | -0.02 | selected signal exited |
| 2026-10-30T10:05 | Agent (ML meta-label) | sell | DOGE-USD | 6.85 | -0.06 | selected signal exited |
| 2026-10-30T10:00 | MACD cross · 1h | buy | DOGE-USD | 9.03 | — | entry signal |
| 2026-10-30T09:46 | Agent (ML meta-label) | buy | ETH-USD | 1.96 | — | entry |
| 2026-10-30T09:46 | Agent (ML meta-label) | buy | DOGE-USD | 6.91 | — | entry |
| 2026-10-30T09:40 | Agent (ML meta-label) | sell | DOGE-USD | 8.34 | -0.14 | selected signal exited |
| 2026-10-30T09:25 | Three white soldiers | sell | XRP-USD | 18.42 | -0.21 | stop-loss |
| 2026-10-30T09:05 | MACD cross · 1h | sell | DOGE-USD | 9.01 | -0.04 | target is flat |
| 2026-10-30T09:05 | Three white soldiers | buy | XRP-USD | 18.63 | — | entry signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | SOL-USD | 15.30 | -0.07 | exit signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | ETH-USD | 7.59 | -0.08 | exit signal |
| 2026-10-30T09:00 | Heikin-Ashi · 1h | sell | BTC-USD | 19.12 | -0.23 | exit signal |
| 2026-10-30T09:00 | MACD cross · 1h | buy | DOGE-USD | 9.05 | — | entry signal |
| 2026-10-30T08:30 | Three white soldiers | sell | SOL-USD | 18.50 | -0.17 | exit signal |
| 2026-10-30T08:25 | Three white soldiers | buy | SOL-USD | 18.68 | — | entry signal |
| 2026-10-30T08:00 | Three white soldiers · 1h | sell | XRP-USD | 23.59 | -0.18 | exit signal |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | buy | ETH-USD | 7.67 | — | entry |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | buy | BTC-USD | 7.57 | — | rebalance up |
| 2026-10-30T08:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 15.24 | -0.19 | exit signal |
| 2026-10-30T07:00 | MACD cross · 1h | buy | SOL-USD | 10.21 | — | entry signal |
| 2026-10-30T06:45 | Three white soldiers | sell | DOGE-USD | 18.58 | -0.12 | exit signal |
| 2026-10-30T06:30 | Heikin-Ashi · 1h | buy | BTC-USD | 3.89 | — | rebalance up |
| 2026-10-30T06:30 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.89 | 0.00 | rebalance down |
| 2026-10-30T06:20 | Three white soldiers | buy | DOGE-USD | 18.71 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 13:15:05.000135+00:00 -> 2026-10-30 13:25:05.000135+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
