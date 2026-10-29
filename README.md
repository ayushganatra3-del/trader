# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-29T18:15:05.000137+00:00 · 40496 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.41 (-8.59%)

Closed trades 120, win rate 39.2%, fees £3.58, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 18.39 | +0.11 |

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

Today: 29454 decisions in 2721 calls, $0.3684 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-29T18:15 | 6 / 19 / 5 | cash |  |
| Breezy | 2026-10-29T18:15 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-29T18:15 | 5 / 23 / 2 | COIN 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.86 | 6.86 | 0 | — | 7.62 | 3.71 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.48 | 6.48 | 15 | 73.3 | 6.05 | 1.97 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.82 | 4.82 | 21 | 47.6 | 8.75 | 2.86 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.77 | 1.77 | 24 | 29.2 | 8.74 | 2.23 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.56 | 1.56 | 0 | — | 4.69 | 2.00 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 101.12 | 1.12 | 93 | 46.2 | -10.97 | -3.00 | -12.63 | 140 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.89 | -1.11 | 0 | — | -0.24 | -0.09 | -3.00 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.86 | -2.14 | 92 | 35.9 | 7.05 | 3.33 | -1.98 | 90 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.54 | -2.46 | 15 | 20.0 | -4.59 | -5.34 | -4.72 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.84 | 0 | — | -4.83 | -1.91 | -7.83 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.73 | -2.51 | -5.83 | 1 |
| 14 | Copy: Congress Democrats (NANC) | copy | 96.97 | -3.03 | 0 | — | -0.66 | -0.22 | -5.99 | 1 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 16 | Agent (rotation) | meta | 95.68 | -4.32 | 128 | 31.2 | -3.33 | -2.07 | -7.48 | 177 |
| 17 | Hold BTC | benchmark | 95.63 | -4.37 | 0 | — | 3.69 | 0.78 | -9.28 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.09 | -4.91 | 16 | 12.5 | -2.55 | -2.33 | -4.76 | 27 |
| 19 | Gap and go | momentum | 95.07 | -4.93 | 123 | 29.3 | 4.92 | 1.61 | -8.76 | 204 |
| 20 | Copy: Cathie Wood (ARKK) | copy | 93.44 | -6.56 | 0 | — | 1.54 | 0.43 | -14.57 | 1 |
| 21 | Copy: Insider buying | copy | 92.61 | -7.39 | 33 | 36.4 | -20.17 | -3.97 | -24.43 | 67 |
| 22 | Opening range 30m | breakout | 92.13 | -7.87 | 297 | 36.0 | -10.44 | -3.09 | -17.21 | 581 |
| 23 | Donchian 55/20 · 1h | breakout | 92.04 | -7.96 | 53 | 15.1 | -14.17 | -3.18 | -15.47 | 102 |
| 24 | Trend pullback · 1h | trend | 91.65 | -8.35 | 100 | 22.0 | -21.01 | -7.24 | -21.10 | 102 |
| 25 | Agent | meta | 91.41 | -8.59 | 120 | 39.2 | -8.88 | -5.28 | -12.20 | 211 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.71 | -2.66 | -16.91 | 1 |
| 27 | Parabolic SAR · 1h | trend | 91.12 | -8.88 | 133 | 29.3 | -18.88 | -4.47 | -19.74 | 248 |
| 28 | Daily: Momentum burst | daily | 90.95 | -9.05 | 15 | 13.3 | -14.24 | -2.65 | -17.57 | 35 |
| 29 | Squeeze breakout · 1h | breakout | 90.72 | -9.28 | 56 | 23.2 | -4.77 | -1.39 | -12.65 | 92 |
| 30 | Daily: Bullish score | daily | 90.35 | -9.65 | 12 | 25.0 | -6.24 | -0.77 | -14.40 | 14 |
| 31 | ADX DI cross · 1h | trend | 89.43 | -10.57 | 133 | 18.0 | -13.93 | -2.80 | -16.21 | 262 |
| 32 | Stochastic reversion · 1h | reversion | 87.81 | -12.19 | 217 | 47.9 | -15.14 | -2.60 | -22.29 | 370 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 87.67 | -12.33 | 14 | 42.9 | -16.27 | -1.42 | -27.23 | 25 |
| 34 | Volume breakout · 1h | breakout | 86.71 | -13.29 | 123 | 30.1 | -14.63 | -3.12 | -17.17 | 108 |
| 35 | Agent (aggressive) | meta | 86.64 | -13.36 | 61 | 34.4 | -9.67 | -3.10 | -14.77 | 99 |
| 36 | Z-score reversion · 1h | reversion | 86.35 | -13.65 | 125 | 36.0 | -12.35 | -1.89 | -21.48 | 205 |
| 37 | Bollinger breakout · 1h | breakout | 86.01 | -13.99 | 128 | 26.6 | -13.42 | -2.43 | -18.95 | 249 |
| 38 | Keltner breakout · 1h | breakout | 85.26 | -14.74 | 84 | 23.8 | -19.35 | -3.66 | -22.67 | 189 |
| 39 | Opening range 15m | breakout | 84.59 | -15.41 | 369 | 32.0 | -15.25 | -4.34 | -17.87 | 710 |
| 40 | Supertrend · 1h | trend | 84.41 | -15.59 | 122 | 14.8 | -22.45 | -4.46 | -25.16 | 233 |
| 41 | Ichimoku · 1h | trend | 84.19 | -15.81 | 73 | 11.0 | -19.10 | -3.84 | -24.73 | 118 |
| 42 | Connors RSI(2) · 1h | reversion | 83.71 | -16.29 | 185 | 40.5 | -21.34 | -6.82 | -21.67 | 163 |
| 43 | RSI momentum · 1h | momentum | 83.34 | -16.66 | 118 | 13.6 | -20.50 | -4.01 | -23.77 | 213 |
| 44 | MACD cross · 1h | trend | 82.52 | -17.48 | 269 | 24.9 | -27.86 | -5.06 | -28.66 | 477 |
| 45 | Triple EMA stack · 1h | trend | 82.49 | -17.51 | 111 | 14.4 | -27.60 | -5.32 | -30.32 | 208 |
| 46 | CCI reversion · 1h | reversion | 82.48 | -17.52 | 242 | 46.7 | -20.14 | -2.75 | -28.07 | 447 |
| 47 | EMA 20/50 cross · 1h | trend | 82.07 | -17.93 | 84 | 11.9 | -21.29 | -3.84 | -24.49 | 136 |
| 48 | MFI reversion · 1h | reversion | 82.03 | -17.97 | 287 | 32.4 | -15.39 | -2.38 | -19.60 | 153 |
| 49 | Williams %R · 1h | reversion | 81.69 | -18.31 | 248 | 47.6 | -32.68 | -5.74 | -34.63 | 527 |
| 50 | Bollinger reversion · 1h | reversion | 80.88 | -19.12 | 191 | 38.7 | -28.33 | -5.72 | -30.50 | 360 |
| 51 | Donchian 20/10 · 1h | breakout | 80.37 | -19.63 | 108 | 21.3 | -23.48 | -4.31 | -26.02 | 220 |
| 52 | OBV trend · 1h | momentum | 79.90 | -20.10 | 221 | 17.2 | -35.77 | -7.15 | -37.13 | 306 |
| 53 | RSI(14) reversion · 1h | reversion | 79.79 | -20.21 | 109 | 27.5 | -16.78 | -3.11 | -24.48 | 185 |
| 54 | MACD zero-line · 1h | trend | 79.59 | -20.41 | 125 | 16.0 | -22.31 | -4.46 | -25.05 | 214 |
| 55 | Agent (ML meta-label) | meta | 78.04 | -21.96 | 1083 | 21.0 | -16.00 | -2.95 | -20.82 | 365 |
| 56 | Heikin-Ashi · 1h | trend | 77.62 | -22.38 | 324 | 24.1 | -42.26 | -9.20 | -42.85 | 670 |
| 57 | ROC + volume · 1h | momentum | 77.25 | -22.75 | 277 | 26.7 | -30.22 | -5.56 | -31.11 | 392 |
| 58 | Candlestick reversal · 1h | reversion | 76.73 | -23.27 | 303 | 30.0 | -33.72 | -6.54 | -34.65 | 541 |
| 59 | VWAP momentum · 1h | momentum | 75.56 | -24.44 | 622 | 23.3 | -49.65 | -10.65 | -50.30 | 1233 |
| 60 | EMA 9/21 cross · 1h | trend | 74.73 | -25.27 | 191 | 10.5 | -31.29 | -6.27 | -32.13 | 339 |
| 61 | Three white soldiers | momentum | 74.65 | -25.35 | 353 | 17.6 | -44.95 | -20.99 | -44.95 | 609 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 72.15 | -27.85 | 21 | 33.3 | -37.06 | -2.24 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -44.03 | -98.90 | 5197 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.16 | -23.64 | -79.16 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -44.31 | -93.71 | 2551 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.78 | -30.51 | -88.81 | 1925 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -38.35 | -91.47 | 2361 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.74 | -32.29 | -90.75 | 2270 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -51.98 | -97.80 | 3520 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -56.61 | -96.22 | 3384 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.15 | -35.41 | -94.16 | 2483 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.43 | -33.77 | -82.46 | 1702 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -54.00 | -99.41 | 5756 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.96 | -43.16 | -92.96 | 2634 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.61 | -37.69 | -95.61 | 3488 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.56 | -99.78 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.05 | -44.21 | -92.09 | 2313 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.75 | -27.44 | -74.75 | 1560 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.92 | -97.76 | 3603 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.60 | -58.94 | -98.60 | 4779 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.73 | -29.58 | -69.76 | 1213 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.82 | -55.41 | -94.83 | 2800 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.88 | -38.55 | -84.88 | 1832 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -67.23 | -99.58 | 6281 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.40 | -28.72 | -87.42 | 2191 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.22 | -19.40 | -76.40 | 1659 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.37 | -37.63 | -90.38 | 2226 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.10 | -50.56 | -96.10 | 3775 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -49.96 | -89.54 | 2121 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.62 | -25.91 | -64.62 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.81 | -25.59 | -73.81 | 1284 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.43 | -18.22 | -75.46 | 1571 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.57 | -50.90 | -96.58 | 4196 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.09 | -99.92 | 8290 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-29T18:10 | Agent (ML meta-label) | buy | SQQQ | 13.01 | — | following VWAP reversion |
| 2026-10-29T18:10 | Agent (ML meta-label) | sell | IWM | 12.99 | -0.01 | selected signal exited |
| 2026-10-29T18:10 | ROC + volume | sell | SQQQ | 12.49 | -0.05 | Kill switch: down 50% from peak |
| 2026-10-29T18:08 | Copy: Insider buying | buy | ACN | 11.57 | — | entry |
| 2026-10-29T18:08 | Copy: Insider buying | sell | APLD | 12.08 | -0.04 | target is flat |
| 2026-10-29T18:05 | Agent (ML meta-label) | buy | TSLA | 13.00 | — | following Z-score reversion |
| 2026-10-29T18:05 | Agent (ML meta-label) | buy | IWM | 13.00 | — | entry |
| 2026-10-29T18:05 | Agent (ML meta-label) | sell | SQQQ | 11.23 | 0.05 | selected signal exited |
| 2026-10-29T18:05 | Agent (ML meta-label) | sell | MSFT | 13.00 | -0.01 | selected signal exited |
| 2026-10-29T18:05 | Opening range 15m | sell | SOXL | 7.56 | -0.20 | exit signal |
| 2026-10-29T18:00 | Agent (ML meta-label) | buy | MSFT | 13.01 | — | following MACD zero-line |
| 2026-10-29T18:00 | Agent (ML meta-label) | sell | TSLA | 13.01 | 0.00 | selected signal exited |
| 2026-10-29T18:00 | ROC + volume · 1h | buy | MSTR | 5.94 | — | entry |
| 2026-10-29T18:00 | ROC + volume · 1h | sell | LABU | 6.92 | 0.08 | stop-loss |
| 2026-10-29T18:00 | VWAP momentum · 1h | buy | MSTR | 4.15 | — | rebalance up |
| 2026-10-29T18:00 | VWAP momentum · 1h | sell | XRP-USD | 6.28 | -0.06 | exit signal |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | buy | TNA | 4.42 | — | rebalance up |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | buy | SQQQ | 4.41 | — | rebalance up |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | buy | META | 4.46 | — | rebalance up |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | buy | IWM | 4.44 | — | rebalance up |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | buy | AAPL | 4.43 | — | rebalance up |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | sell | ETH-USD | 11.08 | -0.09 | exit signal |
| 2026-10-29T18:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 11.07 | -0.04 | exit signal |
| 2026-10-29T18:00 | Ichimoku · 1h | buy | DOGE-USD | 5.10 | — | rebalance up |
| 2026-10-29T18:00 | Ichimoku · 1h | sell | ETH-USD | 11.92 | -0.05 | exit signal |
| 2026-10-29T17:55 | Agent (ML meta-label) | buy | TSLA | 13.01 | — | following Z-score reversion |
| 2026-10-29T17:55 | Agent (ML meta-label) | sell | XRP-USD | 9.73 | -0.20 | selected signal exited |
| 2026-10-29T17:55 | Agent (ML meta-label) | sell | IWM | 11.15 | -0.02 | selected signal exited |
| 2026-10-29T17:55 | Bollinger breakout · 1h | buy | TNA | 4.31 | — | rebalance up |
| 2026-10-29T17:55 | ADX DI cross · 1h | buy | META | 5.83 | — | entry |
| 2026-10-29T17:55 | ADX DI cross · 1h | sell | XRP-USD | 5.83 | -0.13 | stop-loss |
| 2026-10-29T17:55 | Triple EMA stack · 1h | buy | BTC-USD | 9.17 | — | entry |
| 2026-10-29T17:55 | Triple EMA stack · 1h | sell | SPY | 9.21 | -0.09 | stop-loss |
| 2026-10-29T17:55 | EMA 20/50 cross · 1h | buy | BTC-USD | 8.23 | — | rebalance up |
| 2026-10-29T17:55 | EMA 20/50 cross · 1h | sell | UPRO | 13.81 | -0.16 | stop-loss |
| 2026-10-29T17:55 | Opening range 30m | buy | TSLA | 4.75 | — | rebalance up |
| 2026-10-29T17:55 | Opening range 30m | buy | SOXL | 4.82 | — | rebalance up |
| 2026-10-29T17:55 | Opening range 30m | buy | MSTR | 4.76 | — | rebalance up |
| 2026-10-29T17:55 | Opening range 30m | buy | META | 4.66 | — | rebalance up |
| 2026-10-29T17:55 | Opening range 30m | buy | IWM | 4.71 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-31 18:15:05.000137+00:00 -> 2026-10-29 18:25:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
