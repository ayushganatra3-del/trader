# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-30T00:45:05.000121+00:00 · 40816 ticks

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

Today: 600 decisions in 120 calls, $0.0085 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-30T00:45 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-30T00:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-30T00:45 | 1 / 4 / 0 | ETH-USD 50% |  |

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
| 2 | Copy: Warren Buffett (BRK-B) | copy | 106.28 | 6.28 | 0 | — | 7.59 | 3.72 | -5.18 | 1 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.09 | 1.09 | 0 | — | 4.35 | 1.89 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 95 | 45.3 | -12.58 | -3.49 | -12.60 | 140 |
| 9 | Hold SPY | benchmark | 98.99 | -1.01 | 0 | — | 0.56 | 0.37 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 6.78 | 3.18 | -1.98 | 91 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.08 | -2.92 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.74 | -2.52 | -5.83 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.03 | -2.97 | 16 | 18.8 | -5.09 | -5.81 | -5.22 | 22 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.81 | -3.19 | 0 | — | -5.05 | -2.01 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.31 | -2.12 | -7.50 | 174 |
| 17 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 18 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 4.93 | 1.61 | -8.76 | 204 |
| 19 | Copy: Cathie Wood (ARKK) | copy | 93.48 | -6.52 | 0 | — | 2.42 | 0.57 | -14.57 | 1 |
| 20 | Copy: Insider buying | copy | 92.69 | -7.31 | 33 | 36.4 | -20.02 | -3.94 | -24.43 | 67 |
| 21 | Donchian 55/20 · 1h | breakout | 92.31 | -7.69 | 54 | 14.8 | -13.77 | -3.09 | -15.51 | 102 |
| 22 | Daily: Momentum burst | daily | 92.00 | -8.00 | 15 | 13.3 | -12.93 | -2.42 | -17.57 | 35 |
| 23 | Opening range 30m | breakout | 91.77 | -8.23 | 304 | 35.5 | -11.10 | -3.30 | -17.21 | 580 |
| 24 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.57 | -5.72 | -12.21 | 221 |
| 25 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.65 | -7.55 | -21.65 | 101 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.75 | -2.67 | -16.91 | 1 |
| 27 | Hold BTC | benchmark | 90.95 | -9.05 | 0 | — | -1.43 | -0.06 | -11.95 | 1 |
| 28 | Squeeze breakout · 1h | breakout | 90.63 | -9.38 | 56 | 23.2 | -4.82 | -1.31 | -12.65 | 93 |
| 29 | Daily: Bullish score | daily | 90.51 | -9.49 | 12 | 25.0 | -5.76 | -0.69 | -14.40 | 14 |
| 30 | Parabolic SAR · 1h | trend | 90.05 | -9.95 | 137 | 28.5 | -19.98 | -4.64 | -20.21 | 248 |
| 31 | ADX DI cross · 1h | trend | 89.49 | -10.51 | 137 | 19.7 | -15.01 | -3.01 | -16.59 | 260 |
| 32 | Stochastic reversion · 1h | reversion | 87.94 | -12.06 | 218 | 48.2 | -16.59 | -2.88 | -22.33 | 376 |
| 33 | Max aggression: 5-day momentum | meta | 87.67 | -12.33 | 14 | 42.9 | -14.69 | -1.27 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.66 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.63 | -13.37 | 124 | 29.8 | -14.65 | -3.12 | -17.33 | 107 |
| 36 | Bollinger breakout · 1h | breakout | 86.01 | -13.99 | 128 | 26.6 | -11.99 | -2.16 | -19.10 | 244 |
| 37 | Z-score reversion · 1h | reversion | 85.85 | -14.15 | 126 | 35.7 | -12.78 | -1.96 | -21.48 | 205 |
| 38 | Keltner breakout · 1h | breakout | 85.37 | -14.63 | 84 | 23.8 | -22.93 | -4.63 | -23.96 | 196 |
| 39 | Ichimoku · 1h | trend | 84.49 | -15.51 | 75 | 10.7 | -18.75 | -3.76 | -24.73 | 118 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 376 | 32.2 | -16.00 | -4.59 | -18.10 | 709 |
| 41 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 185 | 40.5 | -21.05 | -6.72 | -21.83 | 163 |
| 42 | Supertrend · 1h | trend | 83.77 | -16.23 | 126 | 14.3 | -23.64 | -4.52 | -26.18 | 218 |
| 43 | RSI momentum · 1h | momentum | 83.34 | -16.66 | 122 | 13.1 | -20.37 | -4.04 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.50 | -17.50 | 113 | 14.2 | -27.74 | -5.35 | -30.37 | 208 |
| 45 | MFI reversion · 1h | reversion | 82.12 | -17.88 | 288 | 32.3 | -17.87 | -2.83 | -19.58 | 151 |
| 46 | Williams %R · 1h | reversion | 81.84 | -18.16 | 249 | 47.8 | -33.91 | -5.99 | -34.58 | 524 |
| 47 | MACD cross · 1h | trend | 81.67 | -18.33 | 275 | 24.7 | -28.58 | -5.13 | -29.24 | 476 |
| 48 | EMA 20/50 cross · 1h | trend | 81.63 | -18.37 | 86 | 11.6 | -21.93 | -3.94 | -24.96 | 137 |
| 49 | CCI reversion · 1h | reversion | 81.58 | -18.42 | 245 | 46.5 | -21.56 | -3.03 | -28.07 | 447 |
| 50 | Bollinger reversion · 1h | reversion | 81.07 | -18.93 | 191 | 38.7 | -30.55 | -6.33 | -31.60 | 364 |
| 51 | Donchian 20/10 · 1h | breakout | 80.59 | -19.41 | 108 | 21.3 | -22.33 | -4.09 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.55 | -20.45 | 225 | 16.9 | -34.03 | -6.62 | -36.14 | 300 |
| 53 | MACD zero-line · 1h | trend | 79.12 | -20.88 | 129 | 16.3 | -24.19 | -4.85 | -26.72 | 213 |
| 54 | RSI(14) reversion · 1h | reversion | 78.24 | -21.76 | 113 | 26.5 | -21.44 | -3.93 | -24.99 | 202 |
| 55 | Heikin-Ashi · 1h | trend | 77.26 | -22.74 | 327 | 23.9 | -42.48 | -9.22 | -42.81 | 669 |
| 56 | Candlestick reversal · 1h | reversion | 76.88 | -23.11 | 304 | 29.9 | -35.02 | -7.00 | -36.03 | 546 |
| 57 | ROC + volume · 1h | momentum | 76.56 | -23.44 | 286 | 25.9 | -30.60 | -5.38 | -31.92 | 390 |
| 58 | Agent (ML meta-label) | meta | 76.52 | -23.48 | 1107 | 21.0 | -12.84 | -2.44 | -18.01 | 342 |
| 59 | EMA 9/21 cross · 1h | trend | 74.70 | -25.30 | 195 | 10.3 | -31.18 | -6.22 | -32.26 | 340 |
| 60 | Three white soldiers | momentum | 74.52 | -25.48 | 357 | 17.6 | -44.55 | -20.66 | -44.56 | 607 |
| 61 | VWAP momentum · 1h | momentum | 73.85 | -26.15 | 632 | 22.9 | -51.25 | -10.75 | -51.50 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 72.15 | -27.85 | 21 | 33.3 | -35.91 | -2.16 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -43.07 | -98.88 | 5188 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -78.87 | -23.40 | -78.87 | 1409 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -43.99 | -93.55 | 2534 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.74 | -30.42 | -88.74 | 1911 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.29 | -37.73 | -91.29 | 2342 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.59 | -31.93 | -90.59 | 2260 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -51.35 | -97.76 | 3508 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -55.99 | -96.18 | 3390 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -34.77 | -94.04 | 2474 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -33.14 | -81.99 | 1687 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.45 | -54.57 | -99.45 | 5782 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.94 | -42.84 | -92.95 | 2627 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.81 | -95.62 | 3483 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.27 | -99.78 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.00 | -43.87 | -92.02 | 2304 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.10 | -27.03 | -75.11 | 1563 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -59.67 | -97.70 | 3578 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.63 | -59.37 | -98.63 | 4786 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.90 | -29.12 | -69.98 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.79 | -53.64 | -94.80 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -38.01 | -84.81 | 1824 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.36 | -99.61 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.06 | -29.64 | -88.06 | 2206 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.41 | -19.92 | -77.41 | 1683 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.65 | -37.17 | -90.65 | 2242 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.28 | -51.09 | -96.28 | 3784 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.76 | -50.76 | -89.76 | 2124 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.48 | -25.44 | -64.48 | 822 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.54 | -25.25 | -73.54 | 1277 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.09 | -18.35 | -76.09 | 1565 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.69 | -50.50 | -96.70 | 4197 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -90.01 | -99.92 | 8289 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-29T20:35 | ROC + volume · 1h | sell | DOGE-USD | 6.22 | -0.18 | stop-loss |
| 2026-10-29T20:35 | Parabolic SAR · 1h | sell | ETH-USD | 17.91 | -0.42 | stop-loss |
| 2026-10-29T20:35 | Parabolic SAR · 1h | sell | BTC-USD | 17.93 | -0.35 | stop-loss |
| 2026-10-29T20:35 | MACD cross · 1h | buy | ETH-USD | 5.91 | — | rebalance up |
| 2026-10-29T20:35 | MACD cross · 1h | sell | DOGE-USD | 5.88 | -0.16 | stop-loss |
| 2026-10-29T20:35 | MACD cross · 1h | sell | BTC-USD | 5.41 | -0.13 | stop-loss |
| 2026-10-29T20:35 | Triple EMA stack · 1h | sell | BTC-USD | 9.03 | -0.14 | stop-loss |
| 2026-10-29T20:35 | EMA 20/50 cross · 1h | sell | DOGE-USD | 16.23 | -0.45 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-01 00:45:05.000121+00:00 -> 2026-10-30 00:55:05.000121+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
