# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T16:09:05.000143+00:00 · 63342 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.55 (-15.45%)

Closed trades 207, win rate 36.2%, fees £5.87, max drawdown -16.43%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SOXL | 33.82 | +0.44 |

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

Today: 18174 decisions in 2535 calls, $0.2391 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T16:09 | 14 / 13 / 3 | TECL 14% |  |
| Breezy | 2026-11-17T16:09 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-11-17T16:09 | 9 / 19 / 2 | COIN 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.55% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.13 | 17.13 | 0 | — | 13.31 | 4.42 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.12 | 11.12 | 24 | 62.5 | 16.40 | 3.33 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 103.49 | 3.49 | 0 | — | 5.73 | 1.57 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 100.60 | 0.60 | 36 | 41.7 | -0.84 | -0.07 | -9.64 | 33 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.63 | 2.12 | -9.06 | 224 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -2.71 | -2.27 | -4.31 | 71 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.35 | -3.65 | 8 | 50.0 | -2.91 | -0.01 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.57 | -4.43 | 0 | — | -3.65 | -1.15 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.98 | -6.02 | 197 | 29.9 | -1.74 | -0.55 | -8.15 | 159 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.03 | -7.97 | 0 | — | -8.67 | -2.26 | -8.69 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 17 | Copy: Insider buying | copy | 91.18 | -8.82 | 47 | 42.6 | -9.37 | -1.86 | -14.79 | 62 |
| 18 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 19 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.36 | -6.94 | -17.30 | 65 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.18 | -9.82 | 0 | — | -8.54 | -2.30 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.42 | -12.58 | 17 | 17.6 | -3.63 | -0.52 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -11.28 | -4.41 | -16.01 | 72 |
| 24 | Opening range 30m | breakout | 86.33 | -13.67 | 438 | 33.6 | -9.78 | -3.09 | -14.11 | 575 |
| 25 | Agent | meta | 84.55 | -15.45 | 207 | 36.2 | -15.90 | -7.55 | -16.46 | 199 |
| 26 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.32 | -7.19 | -28.08 | 203 |
| 27 | Agent (aggressive) | meta | 81.26 | -18.74 | 99 | 33.3 | -17.97 | -4.87 | -19.41 | 97 |
| 28 | Keltner breakout · 1h | breakout | 81.24 | -18.76 | 121 | 25.6 | -18.50 | -3.90 | -27.29 | 156 |
| 29 | Max aggression: 5-day momentum | meta | 80.64 | -19.36 | 21 | 42.9 | -47.58 | -3.13 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.33 | -19.68 | 215 | 40.0 | -14.47 | -6.39 | -14.87 | 94 |
| 31 | Volume breakout · 1h | breakout | 79.91 | -20.09 | 162 | 28.4 | -15.94 | -5.06 | -22.00 | 81 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.40 | -6.63 | -29.47 | 84 |
| 33 | Opening range 15m | breakout | 78.25 | -21.75 | 533 | 31.5 | -16.57 | -4.44 | -21.37 | 686 |
| 34 | Max aggression: 1-day momentum | meta | 77.35 | -22.65 | 30 | 26.7 | -23.67 | -0.88 | -57.50 | 39 |
| 35 | ADX DI cross · 1h | trend | 75.25 | -24.75 | 207 | 19.3 | -28.30 | -4.54 | -35.87 | 261 |
| 36 | Hold BTC | benchmark | 75.23 | -24.77 | 2 | 0.0 | -15.19 | -2.13 | -28.91 | 1 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 75.23 | -24.77 | 2 | 0.0 | -16.98 | -2.12 | -26.43 | 1 |
| 38 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.30 | -8.51 | -29.91 | 112 |
| 39 | Bollinger breakout · 1h | breakout | 73.87 | -26.13 | 188 | 21.8 | -25.80 | -5.58 | -33.01 | 222 |
| 40 | Stochastic reversion · 1h | reversion | 73.09 | -26.91 | 344 | 42.7 | -33.75 | -5.03 | -35.89 | 417 |
| 41 | Supertrend · 1h | trend | 71.73 | -28.27 | 187 | 16.0 | -31.40 | -5.32 | -38.41 | 203 |
| 42 | RSI momentum · 1h | momentum | 71.16 | -28.84 | 176 | 14.2 | -31.82 | -5.87 | -38.20 | 202 |
| 43 | Triple EMA stack · 1h | trend | 71.15 | -28.85 | 155 | 14.8 | -30.61 | -6.16 | -36.55 | 191 |
| 44 | MACD zero-line · 1h | trend | 71.00 | -29.00 | 180 | 17.8 | -26.52 | -5.25 | -32.74 | 199 |
| 45 | MFI reversion · 1h | reversion | 70.69 | -29.30 | 423 | 34.0 | -25.77 | -3.71 | -30.29 | 164 |
| 46 | EMA 20/50 cross · 1h | trend | 70.15 | -29.85 | 114 | 9.6 | -36.05 | -9.92 | -38.97 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.79 | -30.21 | 466 | 23.0 | -40.26 | -7.67 | -44.54 | 638 |
| 48 | ROC + volume · 1h | momentum | 69.55 | -30.45 | 408 | 28.2 | -29.34 | -4.83 | -37.89 | 355 |
| 49 | MACD cross · 1h | trend | 69.41 | -30.59 | 412 | 22.1 | -35.28 | -5.17 | -44.36 | 476 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.49 | -31.51 | 306 | 19.0 | -34.90 | -7.43 | -39.38 | 262 |
| 52 | Donchian 20/10 · 1h | breakout | 67.42 | -32.58 | 159 | 18.2 | -30.84 | -5.17 | -39.11 | 206 |
| 53 | CCI reversion · 1h | reversion | 66.70 | -33.30 | 382 | 41.6 | -41.56 | -6.82 | -44.29 | 460 |
| 54 | Bollinger reversion · 1h | reversion | 64.73 | -35.27 | 344 | 37.8 | -38.50 | -5.84 | -39.92 | 407 |
| 55 | EMA 9/21 cross · 1h | trend | 63.28 | -36.72 | 280 | 11.1 | -40.51 | -8.09 | -45.77 | 320 |
| 56 | Williams %R · 1h | reversion | 62.84 | -37.16 | 429 | 40.8 | -45.99 | -7.82 | -46.52 | 546 |
| 57 | Agent (ML meta-label) | meta | 60.06 | -39.94 | 1884 | 24.5 | -21.84 | -3.79 | -26.35 | 317 |
| 58 | RSI(14) reversion · 1h | reversion | 58.47 | -41.53 | 205 | 31.7 | -41.17 | -6.06 | -42.88 | 241 |
| 59 | Z-score reversion · 1h | reversion | 57.39 | -42.61 | 224 | 35.3 | -37.31 | -5.16 | -39.23 | 244 |
| 60 | VWAP momentum · 1h | momentum | 56.96 | -43.04 | 956 | 21.7 | -53.64 | -9.68 | -58.13 | 1201 |
| 61 | Three white soldiers | momentum | 55.68 | -44.32 | 579 | 14.7 | -49.58 | -22.13 | -49.63 | 661 |
| 62 | Candlestick reversal · 1h | reversion | 55.16 | -44.84 | 545 | 26.6 | -47.62 | -8.63 | -48.20 | 614 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.04 | -99.01 | 5275 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.41 | -25.40 | -82.00 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.05 | -43.42 | -94.05 | 2499 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.15 | -31.57 | -90.21 | 1940 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -39.15 | -91.32 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.89 | -30.59 | -89.90 | 2128 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -47.47 | -97.92 | 3463 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -53.71 | -96.51 | 3431 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -37.61 | -93.72 | 2242 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.98 | -32.11 | -83.06 | 1619 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -52.64 | -99.60 | 6077 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.00 | -41.13 | -92.02 | 2580 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.13 | -37.72 | -95.14 | 3328 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -66.32 | -99.80 | 6130 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.22 | -41.88 | -92.23 | 2247 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.45 | -26.28 | -76.51 | 1672 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -56.98 | -97.64 | 3456 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.02 | -54.81 | -99.03 | 4971 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.55 | -27.16 | -68.66 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -54.31 | -94.64 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.56 | -37.50 | -84.60 | 1751 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -65.64 | -99.70 | 6409 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.73 | -30.12 | -90.79 | 2355 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.61 | -18.53 | -79.87 | 1844 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.09 | -35.27 | -91.19 | 2180 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.55 | -45.07 | -97.58 | 3960 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -58.93 | -89.54 | 2166 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.56 | -30.51 | -66.58 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.97 | -22.89 | -72.51 | 1240 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.59 | -17.72 | -80.73 | 1763 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.56 | -45.09 | -97.63 | 4377 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -96.95 | -99.94 | 8385 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T16:06 | Agent | buy | SOXL | 16.58 | — | rebalance up |
| 2026-11-17T16:06 | Agent | sell | BITX | 16.93 | 0.13 | selected signal exited |
| 2026-11-17T16:06 | Three white soldiers | sell | SQQQ | 13.77 | -0.20 | stop-loss |
| 2026-11-17T16:01 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 101.39 | — | entry |
| 2026-11-17T16:01 | Agent (ML meta-label) | sell | SQQQ | 15.19 | 0.15 | selected signal exited |
| 2026-11-17T16:01 | Agent (aggressive) | buy | SOXL | 40.09 | — | following Z-score reversion, CCI reversion |
| 2026-11-17T16:01 | Agent | buy | SOXL | 16.79 | — | following Z-score reversion, CCI reversion |
| 2026-11-17T16:01 | Agent | buy | BITX | 16.79 | — | following MFI reversion |
| 2026-11-17T16:01 | Parabolic SAR · 1h | sell | SOL-USD | 20.61 | -0.24 | exit signal |
| 2026-11-17T15:55 | CCI reversion · 1h | sell | AMD | 16.30 | -0.58 | stop-loss |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | TSLA | 3.90 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | SOXL | 4.22 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | NVDA | 3.97 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | GOOGL | 4.12 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | COIN | 3.99 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | BITX | 4.03 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | AMZN | 3.89 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | buy | AAPL | 3.85 | — | rebalance up |
| 2026-11-17T15:55 | Stochastic reversion · 1h | sell | ETHU | 3.83 | -0.29 | stop-loss |
| 2026-11-17T15:55 | Z-score reversion · 1h | sell | BITX | 11.30 | -0.69 | stop-loss |
| 2026-11-17T15:55 | Bollinger reversion · 1h | buy | TSLA | 6.72 | — | rebalance up |
| 2026-11-17T15:55 | Bollinger reversion · 1h | buy | COIN | 6.79 | — | rebalance up |
| 2026-11-17T15:55 | Bollinger reversion · 1h | buy | BITX | 6.89 | — | rebalance up |
| 2026-11-17T15:55 | Bollinger reversion · 1h | buy | AAPL | 6.69 | — | rebalance up |
| 2026-11-17T15:55 | Bollinger reversion · 1h | sell | SOXL | 8.96 | -0.66 | stop-loss |
| 2026-11-17T15:55 | Bollinger reversion · 1h | sell | ETHU | 9.02 | -0.49 | stop-loss |
| 2026-11-17T15:51 | MFI reversion · 1h | buy | SPY | 3.78 | — | rebalance up |
| 2026-11-17T15:51 | MFI reversion · 1h | buy | COIN | 4.05 | — | rebalance up |
| 2026-11-17T15:51 | MFI reversion · 1h | buy | AMZN | 3.78 | — | rebalance up |
| 2026-11-17T15:51 | MFI reversion · 1h | sell | MSTR | 9.81 | -0.49 | stop-loss |
| 2026-11-17T15:51 | CCI reversion · 1h | buy | SOXL | 7.50 | — | rebalance up |
| 2026-11-17T15:51 | CCI reversion · 1h | buy | AMZN | 6.89 | — | rebalance up |
| 2026-11-17T15:51 | CCI reversion · 1h | buy | AMD | 7.08 | — | rebalance up |
| 2026-11-17T15:51 | CCI reversion · 1h | buy | AAPL | 6.83 | — | rebalance up |
| 2026-11-17T15:51 | CCI reversion · 1h | sell | DOGE-USD | 9.39 | -0.34 | stop-loss |
| 2026-11-17T15:51 | CCI reversion · 1h | sell | BTC-USD | 9.44 | -0.25 | stop-loss |
| 2026-11-17T15:51 | Williams %R · 1h | sell | META | 12.55 | -0.18 | stop-loss |
| 2026-11-17T15:51 | Williams %R · 1h | sell | ETH-USD | 10.36 | -0.31 | stop-loss |
| 2026-11-17T15:51 | Williams %R · 1h | sell | COIN | 12.47 | -0.45 | stop-loss |
| 2026-11-17T15:51 | Stochastic reversion · 1h | sell | MSTR | 3.92 | -0.20 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 16:09:05.000143+00:00 -> 2026-11-17 16:19:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 16:09:05.000143+00:00 -> 2026-11-17 16:19:05.000143+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
