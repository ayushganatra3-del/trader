# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T19:36:05.000137+00:00 · 63517 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.68 (-15.32%)

Closed trades 216, win rate 35.6%, fees £6.03, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 16.92 | -0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 33915 decisions in 3060 calls, $0.4233 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T19:36 | 4 / 13 / 12 | cash |  |
| Breezy | 2026-11-17T19:36 | 0 / 24 / 5 | cash |  |
| Boozy | 2026-11-17T19:36 | 3 / 21 / 5 | COIN 54% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| MFI reversion | BITX | 2.14 | +2.14% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.43 | 17.43 | 0 | — | 14.95 | 5.17 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.22 | 11.21 | 24 | 62.5 | 15.37 | 3.12 | -5.42 | 29 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.73 | 2.73 | 0 | — | 5.31 | 1.47 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.75 | 2.15 | -9.06 | 222 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.49 | -2.96 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.44 | -1.56 | 38 | 39.5 | -2.77 | -0.50 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.74 | -4.26 | 8 | 50.0 | 0.04 | 0.30 | -18.69 | 6 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 12 | Hold SPY | benchmark | 95.20 | -4.80 | 0 | — | -3.92 | -1.27 | -6.90 | 1 |
| 13 | Agent (rotation) | meta | 94.01 | -6.00 | 197 | 29.9 | -2.78 | -0.95 | -8.23 | 153 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.43 | -8.63 | -5.59 | 20 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.18 | -7.82 | 0 | — | -8.40 | -2.20 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 18 | Copy: Insider buying | copy | 90.29 | -9.71 | 50 | 42.0 | -8.84 | -1.75 | -14.79 | 62 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.04 | -6.84 | -16.99 | 65 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.15 | -9.85 | 0 | — | -8.65 | -2.34 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.29 | -12.71 | 17 | 17.6 | -4.33 | -0.65 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -10.31 | -3.39 | -16.01 | 73 |
| 24 | Opening range 30m | breakout | 86.35 | -13.65 | 438 | 33.6 | -9.70 | -3.07 | -14.11 | 575 |
| 25 | Agent | meta | 84.68 | -15.32 | 216 | 35.6 | -16.55 | -7.46 | -18.54 | 209 |
| 26 | Agent (aggressive) | meta | 82.06 | -17.93 | 101 | 33.7 | -17.64 | -4.87 | -20.39 | 100 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.04 | -7.14 | -27.99 | 202 |
| 28 | Keltner breakout · 1h | breakout | 80.98 | -19.02 | 122 | 26.2 | -20.61 | -4.72 | -27.77 | 157 |
| 29 | Max aggression: 5-day momentum | meta | 80.70 | -19.30 | 21 | 42.9 | -47.43 | -3.11 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.30 | -19.70 | 215 | 40.0 | -14.50 | -6.40 | -14.88 | 94 |
| 31 | Volume breakout · 1h | breakout | 79.92 | -20.08 | 162 | 28.4 | -15.45 | -4.78 | -22.16 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.51 | -29.47 | 83 |
| 33 | Opening range 15m | breakout | 78.27 | -21.73 | 533 | 31.5 | -16.36 | -4.37 | -21.37 | 685 |
| 34 | Max aggression: 1-day momentum | meta | 77.42 | -22.58 | 30 | 26.7 | -23.45 | -0.87 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.28 | -23.72 | 2 | 0.0 | -17.88 | -2.37 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.25 | -24.75 | 208 | 19.2 | -26.21 | -4.14 | -34.71 | 259 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.81 | -8.35 | -29.33 | 109 |
| 38 | Hold BTC | benchmark | 74.31 | -25.69 | 2 | 0.0 | -16.51 | -2.34 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.19 | -5.67 | -33.28 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 72.68 | -27.32 | 345 | 42.6 | -34.77 | -5.25 | -36.06 | 425 |
| 41 | Supertrend · 1h | trend | 71.40 | -28.60 | 189 | 15.9 | -32.34 | -5.49 | -39.67 | 200 |
| 42 | Triple EMA stack · 1h | trend | 71.17 | -28.83 | 155 | 14.8 | -30.51 | -6.12 | -36.38 | 184 |
| 43 | RSI momentum · 1h | momentum | 71.10 | -28.90 | 176 | 14.2 | -30.15 | -5.50 | -36.65 | 197 |
| 44 | MACD zero-line · 1h | trend | 70.77 | -29.23 | 181 | 17.7 | -26.32 | -5.19 | -32.79 | 197 |
| 45 | MFI reversion · 1h | reversion | 70.37 | -29.63 | 430 | 33.7 | -28.54 | -4.24 | -30.74 | 165 |
| 46 | EMA 20/50 cross · 1h | trend | 70.00 | -30.00 | 115 | 10.4 | -36.79 | -9.82 | -39.81 | 116 |
| 47 | Heikin-Ashi · 1h | trend | 69.81 | -30.20 | 466 | 23.0 | -41.38 | -8.29 | -44.71 | 633 |
| 48 | ROC + volume · 1h | momentum | 69.57 | -30.43 | 408 | 28.2 | -30.43 | -4.92 | -39.50 | 353 |
| 49 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 50 | MACD cross · 1h | trend | 69.15 | -30.85 | 413 | 22.3 | -39.52 | -6.43 | -44.73 | 473 |
| 51 | OBV trend · 1h | momentum | 68.50 | -31.50 | 306 | 19.0 | -35.02 | -7.45 | -39.27 | 252 |
| 52 | Donchian 20/10 · 1h | breakout | 67.37 | -32.63 | 159 | 18.2 | -31.45 | -5.36 | -39.64 | 203 |
| 53 | CCI reversion · 1h | reversion | 66.43 | -33.57 | 382 | 41.6 | -41.51 | -6.79 | -44.29 | 469 |
| 54 | Bollinger reversion · 1h | reversion | 63.91 | -36.09 | 344 | 37.8 | -38.74 | -5.83 | -39.56 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.14 | -36.86 | 280 | 11.1 | -38.56 | -7.32 | -45.82 | 318 |
| 56 | Williams %R · 1h | reversion | 62.73 | -37.27 | 430 | 40.7 | -45.95 | -7.81 | -46.88 | 562 |
| 57 | Agent (ML meta-label) | meta | 60.07 | -39.93 | 1892 | 24.5 | -31.57 | -5.42 | -32.15 | 323 |
| 58 | RSI(14) reversion · 1h | reversion | 58.04 | -41.96 | 205 | 31.7 | -41.79 | -6.20 | -42.99 | 250 |
| 59 | Z-score reversion · 1h | reversion | 56.96 | -43.04 | 224 | 35.3 | -37.65 | -5.20 | -39.23 | 255 |
| 60 | VWAP momentum · 1h | momentum | 56.83 | -43.17 | 958 | 21.6 | -52.95 | -8.88 | -58.51 | 1187 |
| 61 | Three white soldiers | momentum | 55.09 | -44.91 | 584 | 14.6 | -49.68 | -21.53 | -50.22 | 662 |
| 62 | Candlestick reversal · 1h | reversion | 54.92 | -45.08 | 546 | 26.6 | -48.19 | -8.68 | -49.47 | 620 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.05 | -42.02 | -99.05 | 5266 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.85 | -25.90 | -82.05 | 1396 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.12 | -41.51 | -94.12 | 2486 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.22 | -31.23 | -90.42 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.62 | -38.08 | -91.64 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.92 | -30.57 | -89.92 | 2121 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.94 | -46.08 | -97.94 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -52.36 | -96.55 | 3409 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.48 | -36.99 | -93.57 | 2211 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.25 | -31.93 | -83.28 | 1609 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.20 | -99.60 | 6066 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -40.55 | -92.14 | 2563 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.98 | -37.79 | -95.01 | 3304 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -64.60 | -99.81 | 6175 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.44 | -42.14 | -92.44 | 2255 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.70 | -25.34 | -76.73 | 1642 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -57.00 | -97.67 | 3441 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.01 | -99.03 | 4947 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.61 | -26.82 | -68.62 | 1226 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.59 | -52.55 | -94.60 | 2736 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.47 | -36.29 | -84.49 | 1721 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -64.62 | -99.70 | 6373 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.79 | -30.21 | -90.90 | 2358 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.61 | -18.51 | -79.85 | 1824 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.20 | -35.37 | -91.25 | 2160 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.54 | -44.43 | -97.56 | 3902 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -56.35 | -89.41 | 2175 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.27 | -29.78 | -66.27 | 813 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.16 | -22.80 | -72.51 | 1226 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.44 | -17.58 | -80.70 | 1720 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -44.96 | -97.61 | 4341 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -91.07 | -99.94 | 8445 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T19:30 | Connors RSI(2) · 1h | buy | AAPL | 20.08 | — | entry signal |
| 2026-11-17T19:30 | Keltner breakout · 1h | buy | SQQQ | 20.24 | — | entry signal |
| 2026-11-17T19:30 | VWAP momentum · 1h | buy | SQQQ | 14.21 | — | entry signal |
| 2026-11-17T19:30 | MACD cross · 1h | buy | ETHU | 17.28 | — | entry signal |
| 2026-11-17T19:30 | MACD cross · 1h | buy | BITX | 17.28 | — | entry signal |
| 2026-11-17T19:15 | Agent (ML meta-label) | sell | SQQQ | 14.94 | -0.11 | selected signal exited |
| 2026-11-17T19:10 | Agent (ML meta-label) | buy | SQQQ | 15.04 | — | entry |
| 2026-11-17T19:10 | Agent (aggressive) | buy | COIN | 41.05 | — | following MACD cross |
| 2026-11-17T19:10 | Agent | buy | COIN | 16.94 | — | following MACD cross |
| 2026-11-17T19:10 | MFI reversion · 1h | buy | GOOGL | 7.05 | — | entry |
| 2026-11-17T19:07 | Agent (ML meta-label) | sell | SPY | 15.04 | -0.01 | selected signal exited |
| 2026-11-17T19:05 | Agent (ML meta-label) | buy | SPY | 15.05 | — | entry |
| 2026-11-17T19:05 | Agent (ML meta-label) | sell | SQQQ | 15.04 | -0.00 | selected signal exited |
| 2026-11-17T19:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 98.44 | — | entry |
| 2026-11-17T19:01 | Agent (ML meta-label) | buy | SQQQ | 15.05 | — | entry |
| 2026-11-17T19:01 | Agent | sell | BITX | 16.96 | 0.02 | selected signal exited |
| 2026-11-17T19:01 | MFI reversion · 1h | buy | SPY | 4.08 | — | rebalance up |
| 2026-11-17T19:01 | MFI reversion · 1h | buy | AMZN | 4.03 | — | rebalance up |
| 2026-11-17T19:01 | MFI reversion · 1h | sell | BITX | 8.77 | -0.04 | target is flat |
| 2026-11-17T18:56 | Agent (aggressive) | sell | COIN | 40.05 | -0.03 | selected signal exited |
| 2026-11-17T18:56 | Agent | sell | COIN | 16.71 | -0.01 | selected signal exited |
| 2026-11-17T18:50 | Agent | buy | BITX | 16.93 | — | following MFI reversion |
| 2026-11-17T18:50 | Three white soldiers | sell | META | 13.79 | -0.05 | exit signal |
| 2026-11-17T18:41 | Copy: Insider buying | buy | PAM | 8.71 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | buy | LILA | 11.34 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | buy | HUBS | 11.34 | — | entry |
| 2026-11-17T18:41 | Copy: Insider buying | sell | MDGL | 11.51 | -0.06 | target is flat |
| 2026-11-17T18:41 | Copy: Insider buying | sell | KOD | 10.51 | -0.94 | target is flat |
| 2026-11-17T18:41 | Copy: Insider buying | sell | KMI | 9.37 | 0.18 | target is flat |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | QQQ | 4.71 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | ETHU | 4.63 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | buy | BTC-USD | 4.70 | — | rebalance up |
| 2026-11-17T18:41 | MFI reversion · 1h | sell | GOOGL | 10.05 | -0.02 | target is flat |
| 2026-11-17T18:41 | Three white soldiers | sell | SOXL | 13.61 | -0.23 | exit signal |
| 2026-11-17T18:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 98.44 | -1.30 | target is flat |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | META | 7.43 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | LABU | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | GOOGL | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | COIN | 7.44 | — | entry signal |
| 2026-11-17T18:30 | CCI reversion · 1h | buy | AMD | 7.44 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 19:36:05.000137+00:00 -> 2026-11-17 19:46:05.000137+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 19:36:05.000137+00:00 -> 2026-11-17 19:46:05.000137+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
