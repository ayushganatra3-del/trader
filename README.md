# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T16:50:05.000129+00:00 · 46364 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.55 (-9.45%)

Closed trades 140, win rate 39.3%, fees £3.95, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 18.11 | -0.01 |

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

Today: 20376 decisions in 2484 calls, $0.2624 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T16:50 | 11 / 16 / 3 | cash |  |
| Breezy | 2026-11-03T16:50 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T16:50 | 5 / 24 / 1 | COIN 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.36 | 9.36 | 0 | — | 9.93 | 4.29 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.59 | 0.29 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.12 | 0.12 | 26 | 26.9 | 7.77 | 1.99 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.93 | -3.58 | -13.20 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.86 | -3.14 | 0 | — | -1.40 | -0.70 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 96.30 | -3.70 | 107 | 34.6 | 4.27 | 2.04 | -3.79 | 94 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.92 | -4.08 | 5 | 40.0 | 2.72 | 0.73 | -7.93 | 8 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.60 | -4.40 | 0 | — | -1.10 | -0.33 | -6.60 | 1 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.61 | -5.33 | 29 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.36 | -5.64 | 0 | — | -2.61 | -0.97 | -7.64 | 1 |
| 16 | Agent (rotation) | meta | 94.16 | -5.84 | 155 | 28.4 | -4.93 | -2.93 | -8.64 | 174 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.13 | -5.87 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 92.51 | -7.49 | 147 | 26.5 | 1.83 | 0.64 | -8.88 | 226 |
| 19 | Hold BTC | benchmark | 91.33 | -8.67 | 0 | — | -0.16 | 0.15 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.73 | -9.27 | 102 | 21.6 | -16.46 | -6.10 | -17.40 | 78 |
| 22 | Agent | meta | 90.55 | -9.45 | 140 | 39.3 | -10.28 | -6.19 | -12.22 | 209 |
| 23 | Opening range 30m | breakout | 89.97 | -10.03 | 337 | 32.9 | -12.89 | -3.95 | -17.21 | 587 |
| 24 | Squeeze breakout · 1h | breakout | 89.27 | -10.73 | 61 | 23.0 | -7.93 | -2.64 | -13.79 | 89 |
| 25 | Parabolic SAR · 1h | trend | 88.49 | -11.51 | 150 | 26.7 | -14.03 | -3.25 | -17.40 | 241 |
| 26 | Donchian 55/20 · 1h | breakout | 88.48 | -11.52 | 60 | 13.3 | -14.55 | -3.28 | -18.06 | 100 |
| 27 | Daily: Bullish score | daily | 88.47 | -11.53 | 14 | 21.4 | -4.57 | -0.50 | -14.73 | 15 |
| 28 | Copy: Insider buying | copy | 88.32 | -11.68 | 35 | 37.1 | -22.20 | -4.52 | -23.13 | 61 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.68 | -13.32 | 1 | 0.0 | -2.86 | -0.27 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.59 | -3.83 | -14.77 | 96 |
| 31 | Max aggression: 5-day momentum | meta | 85.44 | -14.56 | 15 | 40.0 | -29.03 | -1.91 | -36.71 | 25 |
| 32 | Stochastic reversion · 1h | reversion | 84.64 | -15.36 | 239 | 46.9 | -24.09 | -4.88 | -26.18 | 390 |
| 33 | Volume breakout · 1h | breakout | 84.62 | -15.38 | 129 | 28.7 | -15.79 | -3.64 | -18.08 | 96 |
| 34 | Keltner breakout · 1h | breakout | 84.18 | -15.82 | 89 | 23.6 | -20.03 | -3.97 | -23.85 | 176 |
| 35 | MFI reversion · 1h | reversion | 84.09 | -15.91 | 303 | 33.0 | -15.52 | -2.44 | -18.35 | 149 |
| 36 | Connors RSI(2) · 1h | reversion | 83.90 | -16.10 | 191 | 40.8 | -20.50 | -6.67 | -20.99 | 136 |
| 37 | ADX DI cross · 1h | trend | 83.22 | -16.78 | 148 | 18.2 | -17.84 | -3.36 | -21.64 | 250 |
| 38 | Opening range 15m | breakout | 82.76 | -17.24 | 411 | 30.2 | -18.16 | -5.29 | -20.73 | 718 |
| 39 | Bollinger breakout · 1h | breakout | 81.39 | -18.61 | 140 | 25.0 | -15.98 | -3.11 | -23.31 | 236 |
| 40 | Ichimoku · 1h | trend | 81.30 | -18.70 | 84 | 13.1 | -18.76 | -3.81 | -25.58 | 120 |
| 41 | EMA 20/50 cross · 1h | trend | 79.95 | -20.05 | 90 | 11.1 | -18.70 | -3.64 | -26.91 | 124 |
| 42 | CCI reversion · 1h | reversion | 78.93 | -21.07 | 268 | 44.8 | -26.55 | -4.21 | -27.92 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.07 | -21.93 | 224 | 38.4 | -27.82 | -5.50 | -30.13 | 375 |
| 44 | MACD zero-line · 1h | trend | 77.86 | -22.14 | 136 | 15.4 | -25.41 | -5.53 | -27.61 | 210 |
| 45 | Supertrend · 1h | trend | 77.73 | -22.27 | 141 | 12.8 | -27.96 | -5.35 | -29.55 | 223 |
| 46 | Z-score reversion · 1h | reversion | 77.52 | -22.48 | 142 | 34.5 | -14.48 | -2.10 | -23.02 | 217 |
| 47 | MACD cross · 1h | trend | 77.30 | -22.70 | 300 | 23.3 | -33.85 | -6.57 | -36.40 | 478 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.04 | -3.51 | -33.56 | 33 |
| 49 | Williams %R · 1h | reversion | 76.65 | -23.35 | 276 | 46.4 | -36.93 | -6.64 | -37.90 | 528 |
| 50 | Triple EMA stack · 1h | trend | 76.32 | -23.68 | 126 | 14.3 | -28.59 | -5.70 | -31.13 | 205 |
| 51 | RSI momentum · 1h | momentum | 76.26 | -23.74 | 136 | 12.5 | -30.12 | -5.75 | -31.98 | 215 |
| 52 | Heikin-Ashi · 1h | trend | 76.10 | -23.90 | 357 | 22.4 | -41.94 | -8.75 | -44.63 | 664 |
| 53 | OBV trend · 1h | momentum | 75.85 | -24.15 | 240 | 17.5 | -30.78 | -6.52 | -32.98 | 299 |
| 54 | Donchian 20/10 · 1h | breakout | 75.19 | -24.81 | 120 | 20.0 | -26.82 | -4.70 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.18 | -25.82 | 302 | 25.5 | -33.61 | -6.43 | -36.05 | 377 |
| 56 | RSI(14) reversion · 1h | reversion | 72.87 | -27.13 | 130 | 26.2 | -21.19 | -3.79 | -26.28 | 199 |
| 57 | Candlestick reversal · 1h | reversion | 71.23 | -28.77 | 354 | 28.5 | -33.97 | -6.29 | -37.45 | 546 |
| 58 | Agent (ML meta-label) | meta | 70.11 | -29.89 | 1335 | 21.0 | -9.39 | -1.83 | -16.50 | 291 |
| 59 | Three white soldiers | momentum | 69.23 | -30.77 | 414 | 16.2 | -46.19 | -21.66 | -46.19 | 616 |
| 60 | EMA 9/21 cross · 1h | trend | 68.95 | -31.05 | 219 | 9.6 | -37.37 | -7.60 | -38.97 | 327 |
| 61 | Max aggression: 1-day momentum | meta | 68.84 | -31.16 | 23 | 30.4 | -32.24 | -1.81 | -50.32 | 42 |
| 62 | VWAP momentum · 1h | momentum | 68.51 | -31.49 | 700 | 21.6 | -53.60 | -10.54 | -56.40 | 1233 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.26 | -98.96 | 5181 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.30 | -23.35 | -80.27 | 1401 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -45.87 | -93.44 | 2515 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.95 | -31.28 | -89.04 | 1907 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -37.45 | -91.13 | 2327 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.58 | -31.93 | -90.68 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -52.11 | -97.73 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -61.11 | -96.29 | 3379 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.40 | -34.41 | -93.52 | 2394 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.65 | -34.40 | -81.99 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -52.44 | -99.48 | 5850 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -43.64 | -93.00 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.39 | -37.06 | -95.40 | 3352 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.79 | -99.80 | 6157 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -44.01 | -91.89 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.40 | -26.39 | -74.79 | 1557 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -59.94 | -97.76 | 3522 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.52 | -98.66 | 4809 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.61 | -29.39 | -70.27 | 1194 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -53.38 | -94.74 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.92 | -37.54 | -84.96 | 1816 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.79 | -99.62 | 6290 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.20 | -30.10 | -88.28 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.58 | -19.13 | -76.73 | 1690 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.18 | -36.26 | -90.20 | 2233 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.79 | -96.46 | 3804 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -53.50 | -89.34 | 2132 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.68 | -25.49 | -65.70 | 817 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.37 | -24.62 | -74.04 | 1271 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.90 | -18.87 | -77.08 | 1586 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -48.78 | -96.81 | 4222 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.62 | -99.92 | 8214 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T16:50 | Agent (ML meta-label) | buy | BITX | 17.53 | — | following Z-score reversion |
| 2026-11-03T16:50 | Agent (ML meta-label) | sell | MSTR | 14.02 | -0.09 | selected signal exited |
| 2026-11-03T16:45 | Agent (ML meta-label) | buy | TSLA | 3.51 | — | rebalance up |
| 2026-11-03T16:45 | Agent (ML meta-label) | buy | SQQQ | 3.53 | — | rebalance up |
| 2026-11-03T16:45 | Agent (ML meta-label) | sell | BITX | 14.02 | -0.03 | selected signal exited |
| 2026-11-03T16:40 | Opening range 30m | buy | ETHU | 8.19 | — | entry signal |
| 2026-11-03T16:40 | Opening range 15m | buy | ETHU | 1.96 | — | entry signal |
| 2026-11-03T16:35 | Agent (rotation) | sell | TQQQ | 7.80 | -0.09 | selected signal exited |
| 2026-11-03T16:35 | Agent (ML meta-label) | buy | TSLA | 4.02 | — | rebalance up |
| 2026-11-03T16:35 | Agent (ML meta-label) | buy | SQQQ | 3.92 | — | rebalance up |
| 2026-11-03T16:35 | Agent (ML meta-label) | buy | MSTR | 3.55 | — | rebalance up |
| 2026-11-03T16:35 | Agent (ML meta-label) | buy | ETHU | 4.00 | — | rebalance up |
| 2026-11-03T16:35 | Agent (ML meta-label) | buy | BITX | 4.00 | — | rebalance up |
| 2026-11-03T16:35 | Agent (ML meta-label) | sell | UPRO | 9.51 | -0.04 | selected signal exited |
| 2026-11-03T16:35 | Agent (ML meta-label) | sell | TQQQ | 9.97 | -0.08 | selected signal exited |
| 2026-11-03T16:35 | Three white soldiers | sell | MSFT | 17.41 | 0.05 | exit signal |
| 2026-11-03T16:35 | Opening range 30m | sell | QQQ | 2.13 | -0.01 | stop-loss |
| 2026-11-03T16:35 | Opening range 30m | sell | LABU | 8.03 | -0.18 | stop-loss |
| 2026-11-03T16:35 | Opening range 15m | sell | QQQ | 1.96 | -0.01 | stop-loss |
| 2026-11-03T16:35 | Gap and go | sell | TQQQ | 22.98 | -0.14 | stop-loss |
| 2026-11-03T16:30 | Agent (rotation) | sell | TQQQ | 31.34 | -0.17 | rebalance down |
| 2026-11-03T16:30 | Agent (rotation) | sell | SOXL | 7.83 | -0.04 | selected signal exited |
| 2026-11-03T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 102.45 | -0.69 | target is flat |
| 2026-11-03T16:30 | Agent (ML meta-label) | buy | UPRO | 9.56 | — | entry |
| 2026-11-03T16:30 | Agent (ML meta-label) | buy | TQQQ | 10.05 | — | entry |
| 2026-11-03T16:30 | Agent (ML meta-label) | sell | TSLA | 7.50 | -0.03 | rebalance down |
| 2026-11-03T16:30 | Agent (ML meta-label) | sell | SQQQ | 4.06 | 0.01 | rebalance down |
| 2026-11-03T16:30 | Agent (ML meta-label) | sell | ETHU | 4.03 | 0.01 | rebalance down |
| 2026-11-03T16:30 | Agent (ML meta-label) | sell | BITX | 4.02 | -0.00 | rebalance down |
| 2026-11-03T16:30 | MFI reversion · 1h | buy | UPRO | 4.85 | — | rebalance up |
| 2026-11-03T16:30 | MFI reversion · 1h | buy | LABU | 4.76 | — | rebalance up |
| 2026-11-03T16:30 | MFI reversion · 1h | buy | DOGE-USD | 4.82 | — | rebalance up |
| 2026-11-03T16:30 | MFI reversion · 1h | buy | BTC-USD | 4.81 | — | rebalance up |
| 2026-11-03T16:30 | MFI reversion · 1h | buy | AMZN | 4.78 | — | rebalance up |
| 2026-11-03T16:30 | MFI reversion · 1h | sell | IWM | 14.03 | -0.02 | target is flat |
| 2026-11-03T16:30 | Williams %R · 1h | buy | PLTR | 6.40 | — | entry signal |
| 2026-11-03T16:30 | Williams %R · 1h | sell | NVDA | 5.90 | 0.02 | exit signal |
| 2026-11-03T16:30 | Williams %R · 1h | sell | COIN | 6.05 | 0.16 | exit signal |
| 2026-11-03T16:30 | Stochastic reversion · 1h | buy | AAPL | 6.52 | — | entry signal |
| 2026-11-03T16:30 | Stochastic reversion · 1h | sell | NVDA | 4.56 | 0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 16:50:05.000129+00:00 -> 2026-11-03 17:00:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 16:50:05.000129+00:00 -> 2026-11-03 17:00:05.000129+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 16:50:05.000129+00:00 -> 2026-11-03 17:00:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
