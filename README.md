# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T16:49:05.000122+00:00 · 45198 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.69 (-8.31%)

Closed trades 131, win rate 41.2%, fees £3.78, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.30 | -0.01 |

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

Today: 17910 decisions in 2478 calls, $0.2351 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T16:49 | 2 / 15 / 13 | cash |  |
| Breezy | 2026-11-02T16:49 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-02T16:49 | 3 / 23 / 4 | MSTR 69% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.96 | 7.96 | 0 | — | 9.59 | 4.47 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 5.93 | 1.92 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.35 | 2.35 | 24 | 45.8 | 2.96 | 1.12 | -5.32 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.72 | -1.28 | 99 | 45.5 | -13.27 | -3.67 | -13.28 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.30 | -1.70 | 0 | — | 1.70 | 0.75 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.58 | -2.42 | 0 | — | -0.23 | -0.07 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.34 | -2.66 | 101 | 35.6 | 4.10 | 2.08 | -2.46 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.88 | -1.99 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.94 | 0.96 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.12 | -4.88 | 0 | — | -5.22 | -1.98 | -6.49 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.97 | -5.03 | 0 | — | -1.19 | -0.39 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 17 | Gap and go | momentum | 94.18 | -5.82 | 136 | 28.7 | 3.33 | 1.12 | -8.76 | 215 |
| 18 | Agent (rotation) | meta | 94.12 | -5.88 | 142 | 29.6 | -6.86 | -4.78 | -9.57 | 143 |
| 19 | Agent | meta | 91.69 | -8.31 | 131 | 41.2 | -9.01 | -5.49 | -12.48 | 207 |
| 20 | Hold BTC | benchmark | 91.32 | -8.68 | 0 | — | -0.28 | 0.13 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 91.32 | -8.68 | 101 | 21.8 | -17.32 | -6.39 | -18.32 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.31 | -2.14 | -16.91 | 1 |
| 23 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -6.25 | -1.91 | -13.40 | 88 |
| 24 | Opening range 30m | breakout | 89.44 | -10.56 | 325 | 33.8 | -12.94 | -3.96 | -17.21 | 584 |
| 25 | Parabolic SAR · 1h | trend | 89.44 | -10.56 | 145 | 27.6 | -15.35 | -3.63 | -16.86 | 241 |
| 26 | Copy: Insider buying | copy | 89.34 | -10.66 | 34 | 35.3 | -21.44 | -4.32 | -23.10 | 62 |
| 27 | Daily: Bullish score | daily | 89.08 | -10.92 | 14 | 21.4 | -5.64 | -0.67 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.54 | -11.46 | 60 | 13.3 | -14.04 | -3.16 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.22 | -12.78 | 1 | 0.0 | -3.02 | -0.31 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -10.06 | -3.24 | -14.77 | 99 |
| 31 | Stochastic reversion · 1h | reversion | 85.41 | -14.59 | 227 | 47.6 | -22.45 | -4.71 | -24.78 | 387 |
| 32 | Volume breakout · 1h | breakout | 85.03 | -14.97 | 128 | 28.9 | -17.13 | -3.84 | -18.61 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.35 | -15.65 | 88 | 23.9 | -21.97 | -4.41 | -25.06 | 173 |
| 34 | Connors RSI(2) · 1h | reversion | 84.04 | -15.96 | 190 | 40.5 | -20.60 | -6.57 | -21.22 | 143 |
| 35 | ADX DI cross · 1h | trend | 84.03 | -15.97 | 142 | 19.0 | -19.41 | -3.60 | -21.80 | 260 |
| 36 | MFI reversion · 1h | reversion | 83.26 | -16.74 | 299 | 32.8 | -16.13 | -2.58 | -18.06 | 145 |
| 37 | Max aggression: 5-day momentum | meta | 82.50 | -17.50 | 15 | 40.0 | -34.44 | -2.49 | -37.35 | 26 |
| 38 | Opening range 15m | breakout | 82.30 | -17.70 | 399 | 30.8 | -18.20 | -5.31 | -20.26 | 716 |
| 39 | Bollinger breakout · 1h | breakout | 81.95 | -18.05 | 139 | 25.2 | -15.24 | -2.82 | -22.52 | 233 |
| 40 | Ichimoku · 1h | trend | 81.27 | -18.73 | 82 | 13.4 | -21.42 | -4.32 | -25.58 | 120 |
| 41 | CCI reversion · 1h | reversion | 80.25 | -19.75 | 258 | 45.7 | -26.03 | -4.08 | -28.68 | 444 |
| 42 | Daily: Momentum burst | daily | 79.14 | -20.86 | 19 | 15.8 | -25.57 | -3.64 | -30.47 | 33 |
| 43 | Supertrend · 1h | trend | 78.54 | -21.46 | 138 | 13.0 | -27.10 | -5.21 | -28.66 | 222 |
| 44 | Bollinger reversion · 1h | reversion | 78.44 | -21.56 | 209 | 39.2 | -29.30 | -6.07 | -30.59 | 370 |
| 45 | EMA 20/50 cross · 1h | trend | 78.10 | -21.90 | 90 | 11.1 | -24.36 | -5.08 | -27.72 | 129 |
| 46 | Williams %R · 1h | reversion | 77.93 | -22.07 | 261 | 47.1 | -35.10 | -6.41 | -35.96 | 517 |
| 47 | Z-score reversion · 1h | reversion | 77.71 | -22.30 | 137 | 34.3 | -14.27 | -2.10 | -22.55 | 206 |
| 48 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.08 | -4.48 | -28.03 | 215 |
| 49 | MACD cross · 1h | trend | 77.61 | -22.39 | 294 | 23.8 | -33.47 | -6.65 | -35.38 | 465 |
| 50 | Triple EMA stack · 1h | trend | 77.17 | -22.83 | 122 | 14.8 | -30.74 | -6.24 | -31.30 | 207 |
| 51 | Heikin-Ashi · 1h | trend | 77.04 | -22.96 | 344 | 23.3 | -38.66 | -7.90 | -42.63 | 660 |
| 52 | RSI momentum · 1h | momentum | 76.79 | -23.21 | 134 | 12.7 | -31.08 | -6.00 | -31.43 | 214 |
| 53 | OBV trend · 1h | momentum | 76.23 | -23.77 | 237 | 17.7 | -35.98 | -7.85 | -36.42 | 308 |
| 54 | Donchian 20/10 · 1h | breakout | 75.27 | -24.73 | 119 | 20.2 | -26.55 | -4.48 | -30.86 | 206 |
| 55 | ROC + volume · 1h | momentum | 74.50 | -25.50 | 299 | 25.4 | -29.64 | -5.05 | -34.36 | 373 |
| 56 | RSI(14) reversion · 1h | reversion | 72.36 | -27.64 | 124 | 26.6 | -21.31 | -3.77 | -26.17 | 196 |
| 57 | Candlestick reversal · 1h | reversion | 70.69 | -29.31 | 337 | 28.5 | -36.12 | -7.31 | -36.67 | 547 |
| 58 | Max aggression: 1-day momentum | meta | 70.41 | -29.59 | 22 | 31.8 | -33.75 | -1.97 | -50.32 | 42 |
| 59 | Three white soldiers | momentum | 70.22 | -29.77 | 404 | 16.1 | -45.54 | -21.17 | -45.89 | 618 |
| 60 | Agent (ML meta-label) | meta | 69.91 | -30.09 | 1233 | 20.9 | -14.94 | -2.65 | -20.49 | 331 |
| 61 | VWAP momentum · 1h | momentum | 69.55 | -30.45 | 687 | 21.8 | -51.58 | -10.61 | -52.92 | 1225 |
| 62 | EMA 9/21 cross · 1h | trend | 69.50 | -30.50 | 215 | 9.8 | -36.65 | -6.77 | -40.39 | 329 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.50 | -98.95 | 5205 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.00 | -24.17 | -80.04 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.71 | -43.92 | -93.72 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.10 | -31.94 | -89.10 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.47 | -38.03 | -91.48 | 2339 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.93 | -31.98 | -90.93 | 2240 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -53.25 | -97.79 | 3488 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.31 | -57.89 | -96.31 | 3402 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.66 | -35.38 | -93.67 | 2445 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.29 | -33.72 | -82.29 | 1689 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -54.31 | -99.46 | 5818 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.01 | -43.63 | -93.03 | 2618 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.62 | -37.36 | -95.63 | 3402 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -75.36 | -99.78 | 6150 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.05 | -45.27 | -92.05 | 2286 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.07 | -26.24 | -75.09 | 1571 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -60.03 | -97.76 | 3548 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -60.92 | -98.66 | 4822 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.20 | -28.11 | -69.21 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -53.98 | -94.74 | 2770 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.96 | -37.54 | -85.01 | 1811 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -71.33 | -99.62 | 6303 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.99 | -30.05 | -88.01 | 2204 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.23 | -18.86 | -76.57 | 1675 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.22 | -37.40 | -90.22 | 2224 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.39 | -52.01 | -96.40 | 3806 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.71 | -54.46 | -89.72 | 2142 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.18 | -25.25 | -64.67 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.21 | -25.49 | -74.28 | 1275 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.74 | -18.64 | -75.84 | 1582 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -51.12 | -96.80 | 4223 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.72 | -99.92 | 8234 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T16:45 | Agent (ML meta-label) | buy | SOXL | 13.80 | — | entry |
| 2026-11-02T16:45 | Agent (ML meta-label) | buy | MSTR | 13.99 | — | following Williams %R |
| 2026-11-02T16:45 | Agent (ML meta-label) | buy | ETHU | 13.99 | — | following Stochastic reversion |
| 2026-11-02T16:45 | Agent (ML meta-label) | sell | TSLA | 3.52 | -0.01 | rebalance down |
| 2026-11-02T16:45 | Agent | sell | MSTR | 18.47 | 0.18 | selected signal exited |
| 2026-11-02T16:45 | MACD cross · 1h | buy | TSLA | 3.88 | — | rebalance up |
| 2026-11-02T16:45 | MACD cross · 1h | sell | MSFT | 3.88 | -0.03 | rebalance down |
| 2026-11-02T16:40 | Agent (ML meta-label) | sell | SOXL | 7.78 | -0.10 | selected signal exited |
| 2026-11-02T16:40 | Agent (ML meta-label) | sell | ETHU | 15.23 | -0.07 | selected signal exited |
| 2026-11-02T16:40 | Agent (ML meta-label) | sell | BITX | 15.25 | -0.04 | selected signal exited |
| 2026-11-02T16:35 | Agent (ML meta-label) | buy | SOXL | 7.87 | — | entry |
| 2026-11-02T16:35 | Agent (ML meta-label) | buy | ETHU | 15.29 | — | following Stochastic reversion |
| 2026-11-02T16:35 | Agent (ML meta-label) | buy | BITX | 15.29 | — | following Z-score reversion |
| 2026-11-02T16:35 | Agent (ML meta-label) | sell | GOOGL | 17.55 | 0.01 | selected signal exited |
| 2026-11-02T16:35 | MACD cross · 1h | buy | TSLA | 3.88 | — | rebalance up |
| 2026-11-02T16:35 | MACD cross · 1h | sell | GOOGL | 3.88 | -0.03 | rebalance down |
| 2026-11-02T16:31 | Agent (rotation) | sell | TSLA | 3.17 | -0.00 | selected signal exited |
| 2026-11-02T16:31 | Agent (ML meta-label) | sell | MSTR | 14.04 | 0.03 | selected signal exited |
| 2026-11-02T16:31 | Bollinger reversion · 1h | buy | AAPL | 6.53 | — | entry signal |
| 2026-11-02T16:31 | Candlestick reversal · 1h | buy | TECL | 6.29 | — | rebalance up |
| 2026-11-02T16:31 | Candlestick reversal · 1h | buy | MSTR | 6.13 | — | rebalance up |
| 2026-11-02T16:31 | Candlestick reversal · 1h | buy | GOOGL | 6.20 | — | rebalance up |
| 2026-11-02T16:31 | Candlestick reversal · 1h | buy | COIN | 6.30 | — | rebalance up |
| 2026-11-02T16:31 | Candlestick reversal · 1h | buy | BITX | 6.31 | — | rebalance up |
| 2026-11-02T16:31 | Candlestick reversal · 1h | sell | SOXL | 6.71 | -0.46 | exit signal |
| 2026-11-02T16:31 | Candlestick reversal · 1h | sell | PLTR | 7.96 | 0.03 | exit signal |
| 2026-11-02T16:31 | Candlestick reversal · 1h | sell | MSFT | 7.95 | 0.02 | exit signal |
| 2026-11-02T16:31 | Donchian 55/20 · 1h | sell | ETH-USD | 21.40 | -0.39 | stop-loss |
| 2026-11-02T16:31 | RSI momentum · 1h | buy | TSLA | 6.93 | — | rebalance up |
| 2026-11-02T16:31 | RSI momentum · 1h | buy | ETH-USD | 3.85 | — | rebalance up |
| 2026-11-02T16:31 | RSI momentum · 1h | sell | LABU | 18.00 | -2.04 | exit signal |
| 2026-11-02T16:31 | ROC + volume · 1h | sell | MSFT | 18.37 | -0.21 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | buy | TSLA | 12.96 | — | rebalance up |
| 2026-11-02T16:31 | VWAP momentum · 1h | buy | MSTR | 12.98 | — | rebalance up |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | UPRO | 4.28 | -0.06 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | TQQQ | 4.30 | -0.11 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | TNA | 4.36 | -0.04 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | TECL | 4.24 | -0.16 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | SPY | 4.38 | -0.02 | exit signal |
| 2026-11-02T16:31 | VWAP momentum · 1h | sell | QQQ | 4.36 | -0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 16:49:05.000122+00:00 -> 2026-11-02 16:59:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
