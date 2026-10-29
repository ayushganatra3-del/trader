# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-29T19:45:05.000119+00:00 · 40560 ticks

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
| Copy: Insider buying | 2026-10-29 | MSM 12%, LRN 12%, SRRK 12%, IAM 12%, BPRE 12%, RENT 12%, CTY 12%, ACN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-28)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 23.78 · VIX 16.91 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.5, MSFT 5.4, PLTR 5.0, AAPL 4.2, LABU 3.9, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 35202 decisions in 2913 calls, $0.4356 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-29T19:45 | 1 / 16 / 13 | cash |  |
| Breezy | 2026-10-29T19:45 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-29T19:45 | 4 / 21 / 5 | MSTR 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Candlestick reversal | LABU | 2.83 | +8.30% | 12 |
| VWAP momentum · 1h | LABU | 2.51 | +26.96% | 3 |
| VWAP reversion | SQQQ | 2.50 | +4.75% | 5 |
| MACD zero-line | MSFT | 2.39 | +0.71% | 6 |
| Z-score reversion | TSLA | 2.35 | +3.07% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.74 | 6.74 | 0 | — | 7.65 | 3.77 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.23 | 2.05 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.88 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.25 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.41 | 1.41 | 0 | — | 4.49 | 1.95 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.12 | 1.12 | 93 | 46.2 | -10.42 | -2.84 | -12.63 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.99 | -1.01 | 0 | — | 0.23 | 0.18 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.36 | -1.98 | 90 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.67 | -2.33 | 15 | 20.0 | -4.46 | -5.21 | -5.01 | 22 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.76 | -2.54 | -5.83 | 1 |
| 13 | Copy: Congress Democrats (NANC) | copy | 96.88 | -3.12 | 0 | — | -0.83 | -0.30 | -5.99 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.69 | -3.31 | 0 | — | -5.34 | -2.16 | -7.83 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.27 | -2.11 | -7.46 | 173 |
| 17 | Hold BTC | benchmark | 95.66 | -4.34 | 0 | — | 4.01 | 0.80 | -9.28 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.35 | -4.76 | 27 |
| 19 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 5.00 | 1.65 | -8.76 | 204 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 93.36 | -6.64 | 0 | — | 2.29 | 0.55 | -14.57 | 1 |
| 21 | Copy: Insider buying | copy | 92.88 | -7.12 | 33 | 36.4 | -19.94 | -3.95 | -24.43 | 67 |
| 22 | Donchian 55/20 · 1h | breakout | 92.14 | -7.86 | 54 | 14.8 | -14.10 | -3.19 | -15.52 | 102 |
| 23 | Opening range 30m | breakout | 91.77 | -8.23 | 300 | 35.7 | -11.06 | -3.31 | -17.21 | 581 |
| 24 | Agent | meta | 91.68 | -8.32 | 122 | 40.2 | -9.39 | -5.54 | -12.20 | 216 |
| 25 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.67 | -7.63 | -21.67 | 101 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.80 | -2.70 | -16.91 | 1 |
| 27 | Daily: Momentum burst | daily | 91.18 | -8.82 | 15 | 13.3 | -14.22 | -2.60 | -17.57 | 35 |
| 28 | Parabolic SAR · 1h | trend | 90.95 | -9.05 | 134 | 29.1 | -19.12 | -4.55 | -19.74 | 248 |
| 29 | Squeeze breakout · 1h | breakout | 90.69 | -9.31 | 56 | 23.2 | -5.72 | -1.56 | -12.65 | 96 |
| 30 | Daily: Bullish score | daily | 90.15 | -9.85 | 12 | 25.0 | -6.46 | -0.77 | -14.40 | 14 |
| 31 | ADX DI cross · 1h | trend | 89.31 | -10.69 | 137 | 19.7 | -15.33 | -3.08 | -16.59 | 260 |
| 32 | Stochastic reversion · 1h | reversion | 87.77 | -12.23 | 218 | 48.2 | -15.23 | -2.64 | -22.29 | 372 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 87.67 | -12.33 | 14 | 42.9 | -16.21 | -1.43 | -27.23 | 25 |
| 34 | Agent (aggressive) | meta | 87.41 | -12.59 | 62 | 35.5 | -11.10 | -3.69 | -15.04 | 101 |
| 35 | Volume breakout · 1h | breakout | 86.59 | -13.41 | 124 | 29.8 | -14.77 | -3.17 | -17.43 | 108 |
| 36 | Z-score reversion · 1h | reversion | 86.03 | -13.97 | 125 | 36.0 | -12.71 | -1.97 | -21.48 | 205 |
| 37 | Bollinger breakout · 1h | breakout | 86.01 | -13.99 | 128 | 26.6 | -13.11 | -2.37 | -19.10 | 246 |
| 38 | Keltner breakout · 1h | breakout | 85.26 | -14.74 | 84 | 23.8 | -20.94 | -3.89 | -24.24 | 191 |
| 39 | Supertrend · 1h | trend | 84.40 | -15.60 | 122 | 14.8 | -22.10 | -4.14 | -26.01 | 217 |
| 40 | Opening range 15m | breakout | 84.37 | -15.63 | 372 | 31.7 | -16.06 | -4.65 | -18.10 | 709 |
| 41 | Ichimoku · 1h | trend | 84.33 | -15.67 | 75 | 10.7 | -19.05 | -3.86 | -24.73 | 118 |
| 42 | Connors RSI(2) · 1h | reversion | 84.10 | -15.90 | 185 | 40.5 | -21.18 | -6.83 | -21.83 | 163 |
| 43 | RSI momentum · 1h | momentum | 83.31 | -16.69 | 120 | 13.3 | -20.53 | -4.10 | -23.98 | 214 |
| 44 | Triple EMA stack · 1h | trend | 82.57 | -17.43 | 111 | 14.4 | -27.68 | -5.39 | -30.37 | 208 |
| 45 | MACD cross · 1h | trend | 82.42 | -17.58 | 271 | 25.1 | -27.96 | -5.12 | -28.78 | 477 |
| 46 | EMA 20/50 cross · 1h | trend | 82.22 | -17.78 | 84 | 11.9 | -21.30 | -3.89 | -24.80 | 137 |
| 47 | CCI reversion · 1h | reversion | 82.20 | -17.80 | 243 | 46.9 | -20.99 | -2.96 | -28.07 | 447 |
| 48 | MFI reversion · 1h | reversion | 82.14 | -17.86 | 288 | 32.3 | -16.16 | -2.56 | -19.60 | 152 |
| 49 | Williams %R · 1h | reversion | 81.66 | -18.34 | 249 | 47.8 | -32.66 | -5.75 | -34.57 | 521 |
| 50 | Bollinger reversion · 1h | reversion | 80.87 | -19.13 | 191 | 38.7 | -29.20 | -6.03 | -31.30 | 360 |
| 51 | Donchian 20/10 · 1h | breakout | 80.40 | -19.60 | 108 | 21.3 | -22.98 | -4.25 | -26.02 | 219 |
| 52 | OBV trend · 1h | momentum | 79.90 | -20.10 | 223 | 17.0 | -34.32 | -6.79 | -36.18 | 302 |
| 53 | RSI(14) reversion · 1h | reversion | 79.49 | -20.51 | 109 | 27.5 | -19.43 | -3.58 | -24.98 | 201 |
| 54 | MACD zero-line · 1h | trend | 79.42 | -20.58 | 128 | 16.4 | -23.93 | -4.87 | -26.69 | 213 |
| 55 | Heikin-Ashi · 1h | trend | 77.50 | -22.50 | 327 | 23.9 | -42.27 | -9.28 | -42.75 | 669 |
| 56 | Agent (ML meta-label) | meta | 77.05 | -22.95 | 1101 | 21.1 | -14.48 | -2.89 | -19.29 | 352 |
| 57 | ROC + volume · 1h | momentum | 76.98 | -23.02 | 284 | 26.1 | -29.56 | -5.30 | -31.30 | 389 |
| 58 | Candlestick reversal · 1h | reversion | 76.64 | -23.36 | 304 | 29.9 | -34.72 | -6.97 | -35.95 | 544 |
| 59 | VWAP momentum · 1h | momentum | 75.05 | -24.95 | 630 | 23.0 | -50.12 | -10.81 | -50.34 | 1233 |
| 60 | EMA 9/21 cross · 1h | trend | 74.69 | -25.31 | 194 | 10.3 | -31.27 | -6.29 | -32.40 | 339 |
| 61 | Three white soldiers | momentum | 74.50 | -25.50 | 356 | 17.4 | -45.07 | -21.33 | -45.07 | 612 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 72.15 | -27.85 | 21 | 33.3 | -36.36 | -2.21 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.89 | -45.34 | -98.89 | 5187 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.07 | -24.03 | -79.08 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.72 | -46.48 | -93.72 | 2548 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.77 | -31.37 | -88.78 | 1913 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.47 | -39.73 | -91.47 | 2356 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.70 | -33.24 | -90.70 | 2267 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -55.38 | -97.80 | 3519 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -60.97 | -96.23 | 3371 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -36.74 | -94.10 | 2473 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.25 | -34.78 | -82.25 | 1695 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -57.41 | -99.41 | 5768 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.04 | -45.35 | -93.04 | 2634 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -39.59 | -95.65 | 3488 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -81.89 | -99.78 | 6185 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.11 | -46.55 | -92.13 | 2313 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.94 | -27.89 | -74.94 | 1549 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -66.00 | -97.75 | 3591 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.59 | -63.27 | -98.59 | 4786 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.17 | -30.27 | -70.17 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.87 | -58.78 | -94.87 | 2798 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.02 | -39.97 | -85.02 | 1830 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -74.39 | -99.58 | 6292 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.45 | -29.65 | -87.48 | 2200 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -75.88 | -19.28 | -75.99 | 1669 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.35 | -38.68 | -90.37 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -52.96 | -96.07 | 3765 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.75 | -54.38 | -89.76 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.61 | -26.21 | -64.61 | 810 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.65 | -25.91 | -73.65 | 1280 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.44 | -18.48 | -75.57 | 1579 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.56 | -53.72 | -96.57 | 4197 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -112.34 | -99.92 | 8306 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-29T19:45 | Agent (ML meta-label) | buy | SOL-USD | 7.19 | — | entry |
| 2026-10-29T19:45 | Parabolic SAR · 1h | sell | SOL-USD | 11.17 | -0.28 | stop-loss |
| 2026-10-29T19:45 | Three white soldiers | buy | SPY | 18.63 | — | entry |
| 2026-10-29T19:40 | Agent (ML meta-label) | buy | SQQQ | 11.02 | — | following VWAP reversion |
| 2026-10-29T19:40 | Agent (ML meta-label) | sell | SOL-USD | 10.98 | -0.09 | selected signal exited |
| 2026-10-29T19:40 | MACD zero-line · 1h | sell | SOL-USD | 19.66 | -0.34 | stop-loss |
| 2026-10-29T19:35 | Agent (ML meta-label) | buy | SOL-USD | 6.49 | — | rebalance up |
| 2026-10-29T19:35 | Agent (ML meta-label) | buy | IWM | 11.05 | — | entry |
| 2026-10-29T19:35 | Agent (ML meta-label) | sell | SQQQ | 9.54 | -0.07 | selected signal exited |
| 2026-10-29T19:35 | Agent (ML meta-label) | sell | MSFT | 5.58 | -0.01 | selected signal exited |
| 2026-10-29T19:35 | Agent (ML meta-label) | sell | AAPL | 9.65 | 0.00 | selected signal exited |
| 2026-10-29T19:35 | Three white soldiers | sell | IWM | 18.62 | -0.00 | target is flat |
| 2026-10-29T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 97.54 | — | entry |
| 2026-10-29T19:30 | Agent (ML meta-label) | buy | MSFT | 5.59 | — | following MACD zero-line |
| 2026-10-29T19:30 | Agent (ML meta-label) | buy | META | 9.09 | — | entry |
| 2026-10-29T19:30 | Agent (ML meta-label) | sell | XRP-USD | 9.60 | -0.05 | selected signal exited |
| 2026-10-29T19:30 | Agent (ML meta-label) | sell | SOL-USD | 5.08 | -0.04 | rebalance down |
| 2026-10-29T19:30 | Agent (aggressive) | sell | LABU | 44.09 | 0.77 | selected signal exited |
| 2026-10-29T19:30 | Agent | sell | LABU | 18.60 | 0.32 | selected signal exited |
| 2026-10-29T19:30 | Williams %R · 1h | buy | UPRO | 20.43 | — | entry signal |
| 2026-10-29T19:30 | Williams %R · 1h | buy | SPY | 20.43 | — | entry signal |
| 2026-10-29T19:30 | Stochastic reversion · 1h | buy | UPRO | 21.96 | — | entry signal |
| 2026-10-29T19:30 | Stochastic reversion · 1h | buy | SPY | 21.96 | — | entry signal |
| 2026-10-29T19:30 | Stochastic reversion · 1h | buy | GOOGL | 21.96 | — | entry signal |
| 2026-10-29T19:30 | Candlestick reversal · 1h | buy | QQQ | 19.15 | — | entry signal |
| 2026-10-29T19:30 | Candlestick reversal · 1h | buy | NVDA | 19.18 | — | entry signal |
| 2026-10-29T19:30 | Candlestick reversal · 1h | sell | PLTR | 19.13 | -0.04 | exit signal |
| 2026-10-29T19:30 | VWAP momentum · 1h | buy | MSFT | 12.47 | — | entry signal |
| 2026-10-29T19:30 | VWAP momentum · 1h | buy | META | 12.52 | — | entry signal |
| 2026-10-29T19:30 | VWAP momentum · 1h | sell | SQQQ | 6.19 | -0.01 | rebalance down |
| 2026-10-29T19:30 | VWAP momentum · 1h | sell | DOGE-USD | 6.23 | -0.05 | rebalance down |
| 2026-10-29T19:30 | VWAP momentum · 1h | sell | BTC-USD | 6.26 | -0.03 | rebalance down |
| 2026-10-29T19:30 | VWAP momentum · 1h | sell | AAPL | 6.32 | 0.01 | rebalance down |
| 2026-10-29T19:30 | Heikin-Ashi · 1h | buy | SQQQ | 3.88 | — | rebalance up |
| 2026-10-29T19:30 | MACD zero-line · 1h | sell | LABU | 20.16 | 0.07 | exit signal |
| 2026-10-29T19:30 | MACD cross · 1h | sell | LABU | 4.58 | 0.13 | exit signal |
| 2026-10-29T19:30 | Three white soldiers | buy | IWM | 18.63 | — | entry signal |
| 2026-10-29T19:25 | MFI reversion · 1h | buy | COIN | 4.34 | — | entry |
| 2026-10-29T19:25 | MFI reversion · 1h | sell | SQQQ | 4.34 | 0.09 | rebalance down |
| 2026-10-29T19:25 | Three white soldiers | sell | AMZN | 18.63 | -0.03 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-31 19:45:05.000119+00:00 -> 2026-10-29 19:55:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
