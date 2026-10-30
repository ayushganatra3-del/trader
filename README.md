# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T02:45:05.000172+00:00 · 40912 ticks

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

Today: 2040 decisions in 408 calls, $0.0286 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T02:45 | 1 / 3 / 1 | SOL-USD 16% |  |
| Breezy | 2026-10-30T02:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T02:45 | 3 / 2 / 0 | SOL-USD 62% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.23 | 6.23 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.03 | 1.03 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.94 | -1.06 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.03 | -2.97 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.76 | -3.24 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.20 | -2.06 | -7.40 | 174 |
| 17 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 18 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.27 | 1.72 | -8.76 | 204 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.43 | -6.57 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.64 | -7.36 | 33 | 36.4 | -20.02 | -3.94 | -24.43 | 67 |
| 21 | Donchian 55/20 · 1h | breakout | 92.27 | -7.73 | 54 | 14.8 | -13.77 | -3.09 | -15.52 | 102 |
| 22 | Daily: Momentum burst | daily | 91.95 | -8.05 | 15 | 13.3 | -12.93 | -2.43 | -17.57 | 35 |
| 23 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 24 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.47 | -5.57 | -12.21 | 218 |
| 25 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.65 | -7.55 | -21.65 | 101 |
| 26 | Hold BTC | benchmark | 91.39 | -8.61 | 0 | — | -0.61 | 0.07 | -12.47 | 1 |
| 27 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.60 | -9.40 | 56 | 23.2 | -4.80 | -1.30 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.47 | -9.53 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.04 | -9.96 | 137 | 28.5 | -19.98 | -4.64 | -20.21 | 248 |
| 31 | ADX DI cross · 1h | trend | 89.44 | -10.56 | 137 | 19.7 | -15.80 | -3.18 | -16.82 | 263 |
| 32 | Stochastic reversion · 1h | reversion | 87.89 | -12.11 | 218 | 48.2 | -16.49 | -2.86 | -22.69 | 379 |
| 33 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.60 | -13.40 | 124 | 29.8 | -14.65 | -3.12 | -17.33 | 107 |
| 36 | Bollinger breakout · 1h | breakout | 85.96 | -14.04 | 128 | 26.6 | -11.97 | -2.15 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.81 | -14.19 | 126 | 35.7 | -12.93 | -1.99 | -21.48 | 205 |
| 38 | Keltner breakout · 1h | breakout | 85.35 | -14.65 | 84 | 23.8 | -22.86 | -4.61 | -23.96 | 196 |
| 39 | Ichimoku · 1h | trend | 84.45 | -15.55 | 75 | 10.7 | -18.75 | -3.76 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 185 | 40.5 | -21.05 | -6.72 | -21.83 | 163 |
| 42 | Supertrend · 1h | trend | 83.74 | -16.26 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.31 | -16.69 | 122 | 13.1 | -20.40 | -4.04 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.47 | -17.53 | 113 | 14.2 | -27.69 | -5.34 | -30.37 | 208 |
| 45 | MFI reversion · 1h | reversion | 82.08 | -17.92 | 288 | 32.3 | -15.87 | -2.48 | -19.58 | 152 |
| 46 | Williams %R · 1h | reversion | 81.79 | -18.21 | 249 | 47.8 | -33.78 | -5.96 | -34.73 | 526 |
| 47 | MACD cross · 1h | trend | 81.65 | -18.35 | 275 | 24.7 | -28.41 | -5.10 | -29.24 | 476 |
| 48 | EMA 20/50 cross · 1h | trend | 81.60 | -18.40 | 86 | 11.6 | -21.93 | -3.94 | -24.96 | 137 |
| 49 | CCI reversion · 1h | reversion | 81.57 | -18.43 | 245 | 46.5 | -21.56 | -3.03 | -28.07 | 447 |
| 50 | Bollinger reversion · 1h | reversion | 81.03 | -18.97 | 191 | 38.7 | -30.55 | -6.33 | -31.60 | 364 |
| 51 | Donchian 20/10 · 1h | breakout | 80.56 | -19.44 | 108 | 21.3 | -22.28 | -4.08 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.52 | -20.48 | 225 | 16.9 | -34.08 | -6.63 | -36.19 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.11 | -20.89 | 129 | 16.3 | -24.19 | -4.86 | -26.72 | 213 |
| 54 | RSI(14) reversion · 1h | reversion | 78.21 | -21.79 | 113 | 26.5 | -20.96 | -3.81 | -24.99 | 203 |
| 55 | Heikin-Ashi · 1h | trend | 77.24 | -22.76 | 327 | 23.9 | -42.25 | -9.15 | -42.58 | 668 |
| 56 | Candlestick reversal · 1h | reversion | 76.84 | -23.16 | 304 | 29.9 | -34.86 | -6.96 | -36.08 | 550 |
| 57 | ROC + volume · 1h | momentum | 76.52 | -23.48 | 286 | 25.9 | -30.41 | -5.32 | -31.81 | 389 |
| 58 | Agent (ML meta-label) | meta | 76.47 | -23.53 | 1110 | 20.9 | -15.37 | -2.87 | -19.16 | 343 |
| 59 | EMA 9/21 cross · 1h | trend | 74.67 | -25.33 | 195 | 10.3 | -30.97 | -6.16 | -32.26 | 339 |
| 60 | Three white soldiers | momentum | 74.60 | -25.40 | 357 | 17.6 | -44.64 | -20.67 | -44.75 | 609 |
| 61 | VWAP momentum · 1h | momentum | 73.83 | -26.18 | 632 | 22.9 | -51.57 | -10.88 | -51.57 | 1237 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -43.78 | -98.90 | 5207 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.74 | -23.26 | -78.74 | 1407 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -43.75 | -93.50 | 2531 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.67 | -30.32 | -88.67 | 1910 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.24 | -37.59 | -91.24 | 2341 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.57 | -31.88 | -90.57 | 2258 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -51.40 | -97.75 | 3509 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -55.57 | -96.12 | 3383 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -34.73 | -94.05 | 2476 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -33.12 | -81.98 | 1687 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.45 | -55.05 | -99.45 | 5782 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -42.93 | -92.95 | 2631 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.58 | -37.49 | -95.58 | 3477 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.65 | -99.78 | 6183 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -43.56 | -91.95 | 2301 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.09 | -27.05 | -75.09 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -59.31 | -97.69 | 3574 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -59.08 | -98.63 | 4783 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.92 | -29.16 | -70.04 | 1211 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.81 | -53.80 | -94.82 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -38.01 | -84.81 | 1824 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -68.35 | -99.61 | 6293 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.04 | -29.54 | -88.18 | 2206 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.18 | -19.69 | -77.42 | 1682 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.63 | -37.66 | -90.72 | 2238 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -50.89 | -96.27 | 3778 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.80 | -51.28 | -89.81 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.43 | -25.43 | -64.43 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.48 | -25.18 | -73.48 | 1276 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.85 | -18.29 | -75.89 | 1563 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.68 | -50.34 | -96.69 | 4192 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.97 | -99.92 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-30T02:20 | Three white soldiers | buy | SOL-USD | 18.63 | — | entry signal |
| 2026-10-30T02:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.02 | — | entry |
| 2026-10-30T02:00 | Agent (ML meta-label) | sell | DOGE-USD | 9.02 | -0.03 | selected signal exited |
| 2026-10-30T01:25 | Agent (ML meta-label) | buy | DOGE-USD | 9.04 | — | entry |
| 2026-10-30T01:20 | Agent (ML meta-label) | sell | DOGE-USD | 9.04 | -0.06 | selected signal exited |
| 2026-10-30T01:05 | Agent (ML meta-label) | buy | DOGE-USD | 9.11 | — | entry |
| 2026-10-30T01:05 | Agent (ML meta-label) | sell | SOL-USD | 9.11 | -0.09 | selected signal exited |
| 2026-10-30T01:00 | Agent (ML meta-label) | buy | SOL-USD | 9.20 | — | entry |
| 2026-10-30T00:30 | Agent (ML meta-label) | sell | XRP-USD | 9.20 | -0.12 | selected signal exited |
| 2026-10-30T00:25 | Agent (ML meta-label) | buy | XRP-USD | 9.32 | — | entry |
| 2026-10-30T00:25 | VWAP reversion · 1h | sell | XRP-USD | 24.38 | -0.90 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | XRP-USD | 6.26 | -0.08 | stop-loss |
| 2026-10-30T00:25 | RSI(14) reversion · 1h | sell | DOGE-USD | 12.59 | -0.62 | stop-loss |
| 2026-10-30T00:20 | VWAP reversion · 1h | sell | BTC-USD | 24.60 | -0.68 | stop-loss |
| 2026-10-30T00:20 | RSI(14) reversion · 1h | buy | XRP-USD | 6.34 | — | entry |
| 2026-10-30T00:20 | RSI(14) reversion · 1h | sell | SOL-USD | 6.34 | -0.27 | stop-loss |
| 2026-10-30T00:16 | Agent (ML meta-label) | sell | SOL-USD | 9.32 | -0.06 | selected signal exited |
| 2026-10-30T00:00 | Agent (ML meta-label) | buy | SOL-USD | 9.38 | — | entry |
| 2026-10-29T22:00 | VWAP reversion · 1h | buy | XRP-USD | 25.28 | — | entry signal |
| 2026-10-29T22:00 | VWAP reversion · 1h | buy | BTC-USD | 25.28 | — | entry signal |
| 2026-10-29T22:00 | RSI(14) reversion · 1h | buy | SOL-USD | 6.61 | — | entry signal |
| 2026-10-29T22:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 13.21 | — | entry signal |
| 2026-10-29T21:01 | Agent (ML meta-label) | sell | XRP-USD | 2.44 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-29T21:01 | Agent (ML meta-label) | sell | SOL-USD | 6.95 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-29T21:00 | Agent (ML meta-label) | buy | XRP-USD | 2.45 | — | entry |
| 2026-10-29T21:00 | Agent (ML meta-label) | buy | SOL-USD | 6.99 | — | entry |
| 2026-10-29T21:00 | Supertrend · 1h | sell | SOL-USD | 2.96 | -0.22 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | ETH-USD | 4.76 | -0.27 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | DOGE-USD | 4.68 | -0.35 | exit signal |
| 2026-10-29T21:00 | Supertrend · 1h | sell | BTC-USD | 5.86 | -0.23 | exit signal |
| 2026-10-29T20:45 | VWAP momentum · 1h | sell | DOGE-USD | 11.92 | -0.66 | stop-loss |
| 2026-10-29T20:45 | VWAP momentum · 1h | sell | BTC-USD | 12.18 | -0.36 | stop-loss |
| 2026-10-29T20:45 | MACD cross · 1h | sell | ETH-USD | 11.45 | -0.38 | stop-loss |
| 2026-10-29T20:40 | CCI reversion · 1h | sell | SOL-USD | 19.80 | -0.71 | stop-loss |
| 2026-10-29T20:40 | ROC + volume · 1h | sell | BTC-USD | 6.18 | -0.04 | stop-loss |
| 2026-10-29T20:35 | Agent (ML meta-label) | sell | DOGE-USD | 9.44 | -0.32 | selected signal exited |
| 2026-10-29T20:35 | OBV trend · 1h | sell | DOGE-USD | 7.14 | -0.20 | stop-loss |
| 2026-10-29T20:35 | OBV trend · 1h | sell | BTC-USD | 8.75 | -0.19 | stop-loss |
| 2026-10-29T20:35 | RSI momentum · 1h | sell | BTC-USD | 5.88 | -0.17 | stop-loss |
| 2026-10-29T20:35 | ROC + volume · 1h | buy | BTC-USD | 6.22 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 02:45:05.000172+00:00 -> 2026-10-30 02:55:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
