# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T20:35:05.000126+00:00 · 63575 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £84.83 (-15.17%)

Closed trades 217, win rate 35.5%, fees £6.05, max drawdown -17.33%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 16.89 | -0.03 |
| SOXL | 17.16 | +0.23 |

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

Today: 39102 decisions in 3234 calls, $0.4840 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T20:35 | 5 / 19 / 6 | cash |  |
| Breezy | 2026-11-17T20:35 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-17T20:35 | 9 / 21 / 0 | BITX 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.20 | 17.20 | 0 | — | 15.42 | 5.42 | -3.70 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.86 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.00 | 11.00 | 24 | 62.5 | 16.47 | 3.37 | -5.42 | 28 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 102.97 | 2.97 | 0 | — | 5.46 | 1.53 | -6.60 | 0 |
| 5 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.99 | 2.23 | -9.06 | 212 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: Stocks in Play ORB | daytrade | 99.74 | -0.26 | 150 | 34.7 | -3.51 | -3.01 | -4.31 | 71 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 98.25 | -1.75 | 38 | 39.5 | -2.99 | -0.55 | -9.74 | 35 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.84 | -4.16 | 8 | 50.0 | -4.39 | -0.18 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 95.27 | -4.72 | 0 | — | -4.05 | -1.33 | -6.90 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -3.01 | -7.38 | 2 |
| 13 | Agent (rotation) | meta | 93.95 | -6.05 | 197 | 29.9 | -4.63 | -1.65 | -9.44 | 150 |
| 14 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -5.31 | -8.29 | -5.89 | 21 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 92.22 | -7.78 | 0 | — | -8.40 | -2.22 | -8.74 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.34 | -8.66 | 24 | 16.7 | -10.02 | -8.36 | -10.18 | 24 |
| 17 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.25 | -3.30 | -18.48 | 150 |
| 18 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -11.35 | -5.46 | -13.38 | 60 |
| 19 | Copy: Insider buying | copy | 89.99 | -10.01 | 50 | 42.0 | -9.24 | -1.85 | -14.79 | 62 |
| 20 | Copy: Congress Democrats (NANC) | copy | 89.78 | -10.22 | 0 | — | -8.90 | -2.41 | -12.67 | 1 |
| 21 | Daily: Bullish score | daily | 87.29 | -12.71 | 17 | 17.6 | -4.78 | -0.75 | -19.56 | 14 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.13 | -20.94 | 2 |
| 23 | Squeeze breakout · 1h | breakout | 87.03 | -12.97 | 68 | 20.6 | -15.77 | -6.33 | -19.02 | 76 |
| 24 | Opening range 30m | breakout | 86.31 | -13.69 | 438 | 33.6 | -9.11 | -2.89 | -14.11 | 570 |
| 25 | Agent | meta | 84.83 | -15.17 | 217 | 35.5 | -15.04 | -7.31 | -16.95 | 199 |
| 26 | Agent (aggressive) | meta | 81.87 | -18.13 | 102 | 33.3 | -17.19 | -4.76 | -19.74 | 96 |
| 27 | Parabolic SAR · 1h | trend | 81.57 | -18.43 | 184 | 27.7 | -26.05 | -7.20 | -27.99 | 202 |
| 28 | Keltner breakout · 1h | breakout | 80.94 | -19.06 | 122 | 26.2 | -18.57 | -3.94 | -27.13 | 153 |
| 29 | Max aggression: 5-day momentum | meta | 80.55 | -19.45 | 21 | 42.9 | -47.55 | -3.15 | -55.24 | 22 |
| 30 | Connors RSI(2) · 1h | reversion | 80.35 | -19.65 | 215 | 40.0 | -14.42 | -6.42 | -14.85 | 93 |
| 31 | Volume breakout · 1h | breakout | 79.88 | -20.12 | 162 | 28.4 | -15.55 | -4.86 | -22.20 | 79 |
| 32 | Donchian 55/20 · 1h | breakout | 79.82 | -20.18 | 77 | 13.0 | -25.03 | -6.57 | -29.47 | 83 |
| 33 | Opening range 15m | breakout | 78.23 | -21.77 | 533 | 31.5 | -16.13 | -4.33 | -21.37 | 680 |
| 34 | Max aggression: 1-day momentum | meta | 77.27 | -22.73 | 30 | 26.7 | -23.63 | -0.89 | -57.50 | 39 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 76.31 | -23.69 | 2 | 0.0 | -18.58 | -2.50 | -26.43 | 1 |
| 36 | ADX DI cross · 1h | trend | 75.21 | -24.79 | 208 | 19.2 | -27.06 | -4.35 | -35.42 | 262 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -28.72 | -8.40 | -29.33 | 109 |
| 38 | Hold BTC | benchmark | 74.68 | -25.32 | 2 | 0.0 | -16.01 | -2.28 | -28.91 | 1 |
| 39 | Bollinger breakout · 1h | breakout | 73.62 | -26.38 | 189 | 22.2 | -26.06 | -5.73 | -33.32 | 221 |
| 40 | Stochastic reversion · 1h | reversion | 72.87 | -27.13 | 345 | 42.6 | -34.58 | -5.27 | -36.02 | 424 |
| 41 | Supertrend · 1h | trend | 71.83 | -28.17 | 189 | 15.9 | -31.95 | -5.44 | -39.67 | 200 |
| 42 | RSI momentum · 1h | momentum | 71.20 | -28.80 | 176 | 14.2 | -31.03 | -5.65 | -37.58 | 197 |
| 43 | Triple EMA stack · 1h | trend | 71.16 | -28.84 | 155 | 14.8 | -32.51 | -6.61 | -38.02 | 182 |
| 44 | MACD zero-line · 1h | trend | 70.73 | -29.27 | 181 | 17.7 | -26.94 | -5.39 | -33.31 | 202 |
| 45 | MFI reversion · 1h | reversion | 70.70 | -29.30 | 430 | 33.7 | -27.29 | -4.09 | -30.07 | 164 |
| 46 | EMA 20/50 cross · 1h | trend | 69.96 | -30.04 | 115 | 10.4 | -36.14 | -10.13 | -39.15 | 114 |
| 47 | Heikin-Ashi · 1h | trend | 69.77 | -30.23 | 466 | 23.0 | -42.91 | -9.07 | -44.75 | 632 |
| 48 | ROC + volume · 1h | momentum | 69.53 | -30.47 | 408 | 28.2 | -30.70 | -5.04 | -39.54 | 354 |
| 49 | MACD cross · 1h | trend | 69.47 | -30.53 | 413 | 22.3 | -39.08 | -6.38 | -44.56 | 472 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.51 | -4.93 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.49 | -31.51 | 306 | 19.0 | -35.40 | -7.63 | -39.68 | 254 |
| 52 | Donchian 20/10 · 1h | breakout | 67.47 | -32.53 | 159 | 18.2 | -32.51 | -5.49 | -40.92 | 201 |
| 53 | CCI reversion · 1h | reversion | 66.67 | -33.33 | 382 | 41.6 | -41.35 | -6.82 | -44.29 | 470 |
| 54 | Bollinger reversion · 1h | reversion | 63.97 | -36.03 | 344 | 37.8 | -38.50 | -5.84 | -39.42 | 414 |
| 55 | EMA 9/21 cross · 1h | trend | 63.37 | -36.62 | 280 | 11.1 | -40.47 | -7.68 | -47.20 | 323 |
| 56 | Williams %R · 1h | reversion | 62.82 | -37.18 | 430 | 40.7 | -45.83 | -7.86 | -46.86 | 563 |
| 57 | Agent (ML meta-label) | meta | 59.99 | -40.01 | 1900 | 24.4 | -26.89 | -5.46 | -27.52 | 288 |
| 58 | RSI(14) reversion · 1h | reversion | 58.09 | -41.91 | 205 | 31.7 | -40.87 | -6.03 | -43.29 | 254 |
| 59 | Z-score reversion · 1h | reversion | 57.08 | -42.92 | 224 | 35.3 | -37.54 | -5.23 | -39.23 | 255 |
| 60 | VWAP momentum · 1h | momentum | 56.84 | -43.16 | 958 | 21.6 | -53.43 | -9.51 | -58.47 | 1194 |
| 61 | Three white soldiers | momentum | 55.08 | -44.92 | 584 | 14.6 | -49.63 | -21.89 | -50.23 | 661 |
| 62 | Candlestick reversal · 1h | reversion | 55.05 | -44.95 | 546 | 26.6 | -47.06 | -8.58 | -48.30 | 645 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.04 | -43.18 | -99.04 | 5263 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.74 | -25.62 | -82.11 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.04 | -41.80 | -94.07 | 2476 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.19 | -32.17 | -90.42 | 1941 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.60 | -40.06 | -91.60 | 2302 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.95 | -31.54 | -89.95 | 2116 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -48.34 | -97.93 | 3490 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -54.84 | -96.54 | 3404 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.42 | -38.77 | -93.46 | 2224 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.23 | -32.86 | -83.25 | 1609 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.60 | -54.70 | -99.60 | 6089 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.42 | -92.18 | 2567 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -94.95 | -39.45 | -94.98 | 3293 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.08 | -99.81 | 6189 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.47 | -43.97 | -92.49 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.59 | -26.02 | -76.61 | 1641 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -62.06 | -97.67 | 3436 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.01 | -56.54 | -99.01 | 4956 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.82 | -27.75 | -68.82 | 1227 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -56.66 | -94.67 | 2747 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.54 | -37.51 | -84.57 | 1720 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.70 | -69.40 | -99.70 | 6387 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.75 | -31.09 | -90.90 | 2359 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.41 | -18.59 | -79.91 | 1837 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.14 | -36.44 | -91.19 | 2147 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.52 | -45.79 | -97.55 | 3908 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -59.61 | -89.50 | 2170 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.14 | -30.37 | -66.14 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.28 | -23.22 | -72.51 | 1229 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.47 | -17.85 | -80.74 | 1725 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.53 | -46.39 | -97.58 | 4343 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -116.80 | -99.94 | 8457 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | TQQQ | 14.95 | — | entry |
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | SQQQ | 15.00 | — | entry |
| 2026-11-17T20:35 | Agent (ML meta-label) | buy | MSTR | 15.00 | — | entry |
| 2026-11-17T20:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 91.88 | — | entry |
| 2026-11-17T20:30 | Agent (ML meta-label) | sell | MSTR | 14.95 | -0.06 | selected signal exited |
| 2026-11-17T20:30 | VWAP reversion · 1h | buy | MSTR | 22.74 | — | entry signal |
| 2026-11-17T20:30 | VWAP reversion · 1h | buy | AAPL | 22.74 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | buy | MSFT | 6.24 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | buy | META | 6.32 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | buy | ETHU | 6.32 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | buy | BITX | 6.32 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | buy | AMZN | 6.32 | — | entry signal |
| 2026-11-17T20:30 | VWAP momentum · 1h | sell | XRP-USD | 7.79 | -0.03 | rebalance down |
| 2026-11-17T20:30 | VWAP momentum · 1h | sell | SQQQ | 7.94 | 0.03 | rebalance down |
| 2026-11-17T20:30 | VWAP momentum · 1h | sell | SOL-USD | 7.90 | -0.02 | rebalance down |
| 2026-11-17T20:30 | VWAP momentum · 1h | sell | DOGE-USD | 7.88 | -0.03 | rebalance down |
| 2026-11-17T20:25 | MFI reversion · 1h | buy | LABU | 8.03 | — | entry |
| 2026-11-17T20:25 | MFI reversion · 1h | sell | SPY | 3.98 | -0.03 | rebalance down |
| 2026-11-17T20:25 | MFI reversion · 1h | sell | AMZN | 4.04 | -0.00 | rebalance down |
| 2026-11-17T20:25 | Three white soldiers | buy | NVDA | 13.77 | — | entry signal |
| 2026-11-17T20:20 | Agent (ML meta-label) | buy | MSTR | 15.01 | — | entry |
| 2026-11-17T20:20 | Agent | buy | SOXL | 16.93 | — | following Z-score reversion, CCI reversion |
| 2026-11-17T20:15 | Agent (aggressive) | buy | COIN | 40.97 | — | following MACD cross |
| 2026-11-17T20:15 | Agent | buy | COIN | 16.93 | — | following MACD cross |
| 2026-11-17T20:10 | Agent (ML meta-label) | sell | MSTR | 14.99 | -0.03 | selected signal exited |
| 2026-11-17T20:05 | Agent (ML meta-label) | buy | SPY | 15.02 | — | entry |
| 2026-11-17T20:05 | Agent (ML meta-label) | buy | MSTR | 15.02 | — | entry |
| 2026-11-17T20:05 | Agent (ML meta-label) | sell | SQQQ | 15.00 | -0.02 | selected signal exited |
| 2026-11-17T20:00 | Agent (ML meta-label) | buy | SQQQ | 15.02 | — | entry |
| 2026-11-17T20:00 | Agent (ML meta-label) | sell | SPY | 10.21 | -0.02 | selected signal exited |
| 2026-11-17T20:00 | Z-score reversion · 1h | buy | COIN | 2.84 | — | entry |
| 2026-11-17T20:00 | Z-score reversion · 1h | sell | ETHU | 2.84 | -0.06 | rebalance down |
| 2026-11-17T20:00 | OBV trend · 1h | buy | SOL-USD | 17.16 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | XRP-USD | 14.15 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | SOL-USD | 14.24 | — | entry signal |
| 2026-11-17T20:00 | VWAP momentum · 1h | buy | DOGE-USD | 14.24 | — | entry signal |
| 2026-11-17T20:00 | Triple EMA stack · 1h | buy | SOL-USD | 17.83 | — | entry signal |
| 2026-11-17T19:56 | Agent (ML meta-label) | buy | SPY | 10.23 | — | entry |
| 2026-11-17T19:56 | Agent (ML meta-label) | sell | TSLA | 15.02 | -0.01 | selected signal exited |
| 2026-11-17T19:56 | Agent (aggressive) | sell | COIN | 40.90 | -0.16 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 20:35:05.000126+00:00 -> 2026-11-17 20:45:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 20:35:05.000126+00:00 -> 2026-11-17 20:45:05.000126+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
