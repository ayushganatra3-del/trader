# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T16:20:05.000111+00:00 · 45177 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.45 (-8.55%)

Closed trades 130, win rate 40.8%, fees £3.77, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.24 | -0.07 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16020 decisions in 2415 calls, $0.2130 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T16:20 | 6 / 17 / 7 | cash |  |
| Breezy | 2026-11-02T16:20 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-02T16:20 | 4 / 24 / 2 | MSTR 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.77 | 7.77 | 0 | — | 9.16 | 4.28 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 6.19 | 2.00 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.96 | 1.12 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.72 | -1.28 | 99 | 45.5 | -13.27 | -3.67 | -13.28 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.43 | -1.57 | 0 | — | 1.90 | 0.84 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.57 | -2.43 | 0 | — | -0.18 | -0.04 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.32 | -2.68 | 101 | 35.6 | 4.12 | 2.09 | -2.46 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.05 | -2.11 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.19 | 0.80 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.11 | -4.89 | 0 | — | -5.17 | -1.96 | -6.49 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.04 | -4.96 | 0 | — | -1.07 | -0.33 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Gap and go | momentum | 94.14 | -5.87 | 135 | 28.9 | 3.37 | 1.13 | -8.76 | 215 |
| 18 | Agent (rotation) | meta | 94.12 | -5.88 | 141 | 29.8 | -6.89 | -4.82 | -9.52 | 144 |
| 19 | Agent | meta | 91.45 | -8.55 | 130 | 40.8 | -9.23 | -5.65 | -12.48 | 206 |
| 20 | Trend pullback · 1h | trend | 91.42 | -8.58 | 101 | 21.8 | -17.22 | -6.35 | -18.32 | 82 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.76 | -2.25 | -16.91 | 1 |
| 22 | Hold BTC | benchmark | 91.15 | -8.85 | 0 | — | -0.59 | 0.08 | -12.65 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -4.82 | -1.45 | -13.40 | 90 |
| 24 | Opening range 30m | breakout | 89.37 | -10.63 | 325 | 33.8 | -13.03 | -3.98 | -17.21 | 584 |
| 25 | Parabolic SAR · 1h | trend | 89.28 | -10.72 | 145 | 27.6 | -15.44 | -3.65 | -16.86 | 241 |
| 26 | Copy: Insider buying | copy | 89.24 | -10.77 | 34 | 35.3 | -21.49 | -4.33 | -23.10 | 62 |
| 27 | Daily: Bullish score | daily | 89.17 | -10.83 | 14 | 21.4 | -5.74 | -0.69 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.61 | -11.39 | 59 | 13.6 | -13.94 | -3.14 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.23 | -12.78 | 1 | 0.0 | -2.98 | -0.30 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.06 | -3.24 | -14.77 | 99 |
| 31 | Stochastic reversion · 1h | reversion | 85.53 | -14.47 | 227 | 47.6 | -22.26 | -4.66 | -24.78 | 387 |
| 32 | Volume breakout · 1h | breakout | 85.13 | -14.87 | 128 | 28.9 | -17.00 | -3.81 | -18.61 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.34 | -15.66 | 88 | 23.9 | -22.81 | -4.60 | -25.85 | 176 |
| 34 | Connors RSI(2) · 1h | reversion | 83.93 | -16.07 | 190 | 40.5 | -20.53 | -6.53 | -21.05 | 147 |
| 35 | ADX DI cross · 1h | trend | 83.88 | -16.12 | 142 | 19.0 | -18.80 | -3.48 | -21.07 | 258 |
| 36 | MFI reversion · 1h | reversion | 83.25 | -16.75 | 299 | 32.8 | -16.23 | -2.60 | -18.25 | 144 |
| 37 | Opening range 15m | breakout | 82.21 | -17.79 | 399 | 30.8 | -18.28 | -5.34 | -20.17 | 716 |
| 38 | Max aggression: 5-day momentum | meta | 82.06 | -17.94 | 15 | 40.0 | -34.75 | -2.52 | -37.35 | 26 |
| 39 | Bollinger breakout · 1h | breakout | 82.04 | -17.96 | 139 | 25.2 | -15.13 | -2.80 | -22.52 | 233 |
| 40 | Ichimoku · 1h | trend | 81.16 | -18.84 | 82 | 13.4 | -21.49 | -4.34 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 80.29 | -19.71 | 258 | 45.7 | -25.55 | -4.03 | -28.01 | 445 |
| 42 | Daily: Momentum burst | daily | 79.49 | -20.51 | 19 | 15.8 | -25.47 | -3.63 | -30.47 | 33 |
| 43 | Bollinger reversion · 1h | reversion | 78.52 | -21.48 | 209 | 39.2 | -29.12 | -6.01 | -30.60 | 369 |
| 44 | Supertrend · 1h | trend | 78.49 | -21.51 | 138 | 13.0 | -27.15 | -5.26 | -28.59 | 221 |
| 45 | Williams %R · 1h | reversion | 78.03 | -21.97 | 261 | 47.1 | -34.99 | -6.39 | -35.81 | 517 |
| 46 | Z-score reversion · 1h | reversion | 77.73 | -22.27 | 137 | 34.3 | -14.18 | -2.08 | -22.55 | 206 |
| 47 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -22.69 | -4.39 | -27.66 | 214 |
| 48 | EMA 20/50 cross · 1h | trend | 77.58 | -22.42 | 90 | 11.1 | -26.24 | -5.38 | -27.76 | 131 |
| 49 | MACD cross · 1h | trend | 77.47 | -22.53 | 294 | 23.8 | -33.14 | -6.62 | -34.99 | 465 |
| 50 | Triple EMA stack · 1h | trend | 77.06 | -22.94 | 122 | 14.8 | -30.89 | -6.26 | -31.36 | 206 |
| 51 | Heikin-Ashi · 1h | trend | 76.92 | -23.09 | 344 | 23.3 | -41.37 | -8.96 | -42.99 | 662 |
| 52 | RSI momentum · 1h | momentum | 76.58 | -23.42 | 133 | 12.8 | -31.02 | -5.99 | -31.30 | 214 |
| 53 | OBV trend · 1h | momentum | 76.09 | -23.91 | 237 | 17.7 | -35.69 | -7.78 | -36.03 | 308 |
| 54 | Donchian 20/10 · 1h | breakout | 75.25 | -24.75 | 119 | 20.2 | -26.49 | -4.47 | -30.80 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.50 | -25.50 | 298 | 25.5 | -29.60 | -5.04 | -34.36 | 373 |
| 56 | RSI(14) reversion · 1h | reversion | 72.32 | -27.68 | 124 | 26.6 | -20.40 | -3.60 | -26.17 | 198 |
| 57 | Candlestick reversal · 1h | reversion | 70.62 | -29.38 | 334 | 28.1 | -36.51 | -7.51 | -36.79 | 542 |
| 58 | Max aggression: 1-day momentum | meta | 70.18 | -29.82 | 22 | 31.8 | -33.93 | -1.98 | -50.32 | 42 |
| 59 | Three white soldiers | momentum | 70.13 | -29.87 | 404 | 16.1 | -45.68 | -21.22 | -45.96 | 619 |
| 60 | Agent (ML meta-label) | meta | 70.09 | -29.91 | 1227 | 20.8 | -16.17 | -3.29 | -20.13 | 311 |
| 61 | VWAP momentum · 1h | momentum | 69.56 | -30.43 | 674 | 22.1 | -51.51 | -10.69 | -52.44 | 1228 |
| 62 | EMA 9/21 cross · 1h | trend | 69.41 | -30.59 | 215 | 9.8 | -36.52 | -6.71 | -40.19 | 328 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.69 | -98.96 | 5218 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.01 | -24.25 | -80.02 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.74 | -43.56 | -93.74 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.08 | -31.96 | -89.09 | 1927 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.46 | -37.80 | -91.46 | 2337 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.94 | -31.90 | -90.94 | 2241 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -53.34 | -97.79 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -57.32 | -96.33 | 3402 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.62 | -35.20 | -93.63 | 2439 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.28 | -33.74 | -82.28 | 1691 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -55.96 | -99.47 | 5839 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.03 | -43.76 | -93.03 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.37 | -95.63 | 3407 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -75.77 | -99.79 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.03 | -45.06 | -92.04 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.06 | -26.36 | -75.06 | 1572 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.48 | -97.76 | 3551 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.34 | -98.66 | 4812 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.22 | -28.13 | -69.25 | 1199 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.72 | -53.85 | -94.72 | 2770 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.05 | -37.66 | -85.05 | 1812 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -71.79 | -99.62 | 6302 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.92 | -29.97 | -87.92 | 2207 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.91 | -19.59 | -77.00 | 1702 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.32 | -37.79 | -90.33 | 2227 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -52.72 | -96.42 | 3815 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.72 | -54.44 | -89.72 | 2136 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.18 | -25.25 | -64.70 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.29 | -25.49 | -74.29 | 1280 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.17 | -18.96 | -76.17 | 1593 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -50.86 | -96.78 | 4215 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.94 | -99.92 | 8235 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T16:20 | Agent (rotation) | sell | AMZN | 3.15 | 0.02 | selected signal exited |
| 2026-11-02T16:20 | Agent (ML meta-label) | buy | TSLA | 5.94 | — | rebalance up |
| 2026-11-02T16:20 | Agent (ML meta-label) | buy | MSTR | 7.85 | — | rebalance up |
| 2026-11-02T16:20 | Agent (ML meta-label) | sell | ETHU | 11.52 | 0.02 | rebalance down |
| 2026-11-02T16:20 | Agent (ML meta-label) | sell | COIN | 11.51 | -0.09 | selected signal exited |
| 2026-11-02T16:20 | Agent (ML meta-label) | sell | BITX | 11.60 | -0.00 | selected signal exited |
| 2026-11-02T16:20 | Gap and go | sell | AMZN | 23.44 | -0.02 | exit signal |
| 2026-11-02T16:15 | Agent (ML meta-label) | buy | MSTR | 9.67 | — | following Williams %R |
| 2026-11-02T16:15 | Agent (ML meta-label) | buy | ETHU | 11.60 | — | following Stochastic reversion |
| 2026-11-02T16:15 | Agent (ML meta-label) | buy | COIN | 11.60 | — | entry |
| 2026-11-02T16:15 | Agent (ML meta-label) | buy | BITX | 11.60 | — | following Z-score reversion |
| 2026-11-02T16:15 | Agent (ML meta-label) | sell | TSLA | 5.95 | 0.01 | rebalance down |
| 2026-11-02T16:15 | Agent (ML meta-label) | sell | GOOGL | 17.54 | -0.01 | selected signal exited |
| 2026-11-02T16:15 | Candlestick reversal · 1h | sell | BTC-USD | 7.05 | -0.09 | stop-loss |
| 2026-11-02T16:15 | Opening range 30m | buy | TSLA | 4.77 | — | rebalance up |
| 2026-11-02T16:15 | Opening range 30m | sell | TQQQ | 7.42 | -0.07 | exit signal |
| 2026-11-02T16:15 | Opening range 30m | sell | QQQ | 5.99 | -0.03 | exit signal |
| 2026-11-02T16:15 | Opening range 15m | buy | TSLA | 5.49 | — | rebalance up |
| 2026-11-02T16:15 | Opening range 15m | sell | TQQQ | 7.45 | -0.03 | exit signal |
| 2026-11-02T16:15 | Opening range 15m | sell | QQQ | 7.50 | -0.03 | exit signal |
| 2026-11-02T16:10 | Agent (ML meta-label) | buy | TSLA | 3.52 | — | rebalance up |
| 2026-11-02T16:10 | Agent (ML meta-label) | buy | GOOGL | 3.51 | — | rebalance up |
| 2026-11-02T16:10 | Agent (ML meta-label) | sell | ETHU | 13.99 | -0.12 | selected signal exited |
| 2026-11-02T16:10 | Agent (ML meta-label) | sell | COIN | 10.56 | -0.02 | selected signal exited |
| 2026-11-02T16:05 | Agent (ML meta-label) | buy | TSLA | 3.53 | — | rebalance up |
| 2026-11-02T16:05 | Agent (ML meta-label) | buy | SQQQ | 3.54 | — | rebalance up |
| 2026-11-02T16:05 | Agent (ML meta-label) | buy | GOOGL | 14.04 | — | entry |
| 2026-11-02T16:05 | Agent (ML meta-label) | buy | ETHU | 3.51 | — | rebalance up |
| 2026-11-02T16:05 | Agent (ML meta-label) | sell | TQQQ | 10.52 | -0.02 | selected signal exited |
| 2026-11-02T16:05 | Agent (ML meta-label) | sell | SOXL | 6.68 | 0.00 | selected signal exited |
| 2026-11-02T16:05 | Agent (ML meta-label) | sell | BITX | 10.55 | -0.03 | selected signal exited |
| 2026-11-02T16:05 | Opening range 30m | sell | MSFT | 5.23 | -0.06 | stop-loss |
| 2026-11-02T16:05 | Opening range 15m | sell | MSFT | 5.45 | -0.07 | stop-loss |
| 2026-11-02T16:00 | Agent (rotation) | sell | UPRO | 3.13 | 0.01 | selected signal exited |
| 2026-11-02T16:00 | Agent (rotation) | sell | TQQQ | 34.27 | -0.53 | selected signal exited |
| 2026-11-02T16:00 | Agent (rotation) | sell | PLTR | 5.22 | -0.02 | selected signal exited |
| 2026-11-02T16:00 | Agent (rotation) | sell | MSTR | 3.12 | -0.02 | selected signal exited |
| 2026-11-02T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 102.35 | -1.79 | target is flat |
| 2026-11-02T16:00 | Agent (ML meta-label) | buy | TSLA | 3.84 | — | rebalance up |
| 2026-11-02T16:00 | Agent (ML meta-label) | buy | TQQQ | 3.86 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 16:20:05.000111+00:00 -> 2026-11-02 16:30:05.000111+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
