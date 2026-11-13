# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T17:10:05.000124+00:00 · 58431 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.48 (-14.52%)

Closed trades 194, win rate 35.6%, fees £5.62, max drawdown -15.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 17.30 | +0.25 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 24144 decisions in 2748 calls, $0.3095 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T17:10 | 14 / 13 / 3 | TECL 15%, ARKK 15%, SOXL 15%, TNA 14% |  |
| Breezy | 2026-11-13T17:10 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-11-13T17:10 | 11 / 18 / 1 | COIN 75% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | TSLA | 2.54 | +2.98% | 10 |
| VWAP reversion | PLTR | 1.87 | +4.07% | 5 |
| Z-score reversion | TQQQ | 1.81 | +3.75% | 6 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.59 | +2.90% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.92 | 17.92 | 0 | — | 15.44 | 5.14 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 115.97 | 15.97 | 34 | 29.4 | 24.48 | 3.48 | -8.66 | 45 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 112.91 | 12.91 | 22 | 68.2 | 16.42 | 3.35 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.46 | 5.46 | 32 | 43.8 | 5.46 | 1.37 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 105.22 | 5.22 | 0 | — | 7.28 | 1.97 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.35 | 1.35 | 141 | 34.8 | 7.95 | 3.12 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.94 | -2.06 | 0 | — | -0.90 | -0.24 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 96.47 | -3.52 | 1 | 0.0 | -3.59 | -2.29 | -6.65 | 2 |
| 13 | Agent (rotation) | meta | 96.20 | -3.80 | 191 | 30.4 | -2.68 | -0.91 | -8.69 | 161 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.16 | -3.84 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 17 | Copy: Insider buying | copy | 93.24 | -6.76 | 43 | 39.5 | -6.13 | -1.16 | -14.81 | 66 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.94 | -7.06 | 0 | — | -5.48 | -1.47 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.93 | -8.07 | 110 | 22.7 | -14.52 | -5.30 | -17.77 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -11.41 | -2.42 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 85.95 | -14.04 | 433 | 33.3 | -10.11 | -3.19 | -14.11 | 603 |
| 24 | Daily: Bullish score | daily | 85.89 | -14.11 | 16 | 18.8 | -10.01 | -1.58 | -19.56 | 15 |
| 25 | Agent | meta | 85.48 | -14.52 | 194 | 35.6 | -15.64 | -7.73 | -16.35 | 214 |
| 26 | Parabolic SAR · 1h | trend | 85.25 | -14.75 | 175 | 28.6 | -15.58 | -3.36 | -22.50 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -19.13 | -5.29 | -20.04 | 102 |
| 28 | Donchian 55/20 · 1h | breakout | 81.81 | -18.19 | 73 | 13.7 | -23.20 | -4.84 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.20 | -18.80 | 1 | 0.0 | -11.10 | -1.56 | -22.00 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.63 | -19.37 | 211 | 40.3 | -18.14 | -6.38 | -18.32 | 114 |
| 31 | Keltner breakout · 1h | breakout | 80.55 | -19.45 | 120 | 25.8 | -16.43 | -3.29 | -25.32 | 169 |
| 32 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 80.23 | -19.77 | 2 | 0.0 | -10.51 | -1.22 | -24.16 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 79.19 | -20.81 | 302 | 47.4 | -26.58 | -3.92 | -28.25 | 395 |
| 35 | Opening range 15m | breakout | 78.37 | -21.62 | 526 | 31.2 | -17.38 | -4.67 | -21.36 | 719 |
| 36 | MFI reversion · 1h | reversion | 77.54 | -22.46 | 395 | 35.2 | -22.45 | -2.92 | -26.64 | 162 |
| 37 | ADX DI cross · 1h | trend | 76.78 | -23.22 | 198 | 19.7 | -23.78 | -3.59 | -32.07 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -41.88 | -2.70 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -22.42 | -4.65 | -30.71 | 239 |
| 41 | Heikin-Ashi · 1h | trend | 75.12 | -24.88 | 442 | 24.2 | -37.79 | -7.05 | -39.26 | 661 |
| 42 | MACD cross · 1h | trend | 74.52 | -25.48 | 385 | 23.6 | -29.53 | -4.39 | -38.65 | 469 |
| 43 | Max aggression: 1-day momentum | meta | 73.81 | -26.19 | 29 | 27.6 | -21.23 | -0.68 | -57.50 | 41 |
| 44 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.16 | -4.53 | -30.99 | 203 |
| 45 | RSI momentum · 1h | momentum | 72.72 | -27.28 | 171 | 14.0 | -26.90 | -4.14 | -37.92 | 208 |
| 46 | Supertrend · 1h | trend | 72.48 | -27.52 | 180 | 15.0 | -30.68 | -5.25 | -36.51 | 215 |
| 47 | EMA 20/50 cross · 1h | trend | 72.12 | -27.88 | 109 | 10.1 | -29.05 | -4.91 | -40.51 | 120 |
| 48 | Bollinger reversion · 1h | reversion | 71.61 | -28.39 | 301 | 41.5 | -33.62 | -5.26 | -35.72 | 380 |
| 49 | Triple EMA stack · 1h | trend | 71.46 | -28.54 | 150 | 14.0 | -28.59 | -4.73 | -38.65 | 204 |
| 50 | ROC + volume · 1h | momentum | 71.33 | -28.67 | 397 | 28.7 | -31.38 | -5.77 | -38.37 | 376 |
| 51 | CCI reversion · 1h | reversion | 70.77 | -29.23 | 346 | 43.4 | -38.81 | -6.13 | -39.59 | 462 |
| 52 | OBV trend · 1h | momentum | 69.64 | -30.36 | 298 | 19.1 | -30.64 | -5.41 | -38.11 | 276 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -33.73 | -4.57 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.36 | -30.64 | 153 | 19.0 | -30.15 | -5.41 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.68 | -32.32 | 382 | 43.5 | -42.96 | -7.05 | -44.04 | 535 |
| 56 | Z-score reversion · 1h | reversion | 65.18 | -34.82 | 204 | 37.3 | -30.79 | -4.35 | -31.55 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 64.86 | -35.15 | 263 | 10.3 | -37.90 | -7.70 | -43.16 | 329 |
| 58 | Agent (ML meta-label) | meta | 64.48 | -35.52 | 1839 | 24.7 | -11.27 | -1.65 | -20.52 | 343 |
| 59 | RSI(14) reversion · 1h | reversion | 63.91 | -36.09 | 186 | 32.8 | -37.88 | -5.64 | -38.84 | 241 |
| 60 | VWAP momentum · 1h | momentum | 62.49 | -37.51 | 911 | 22.2 | -53.41 | -10.63 | -53.93 | 1219 |
| 61 | Candlestick reversal · 1h | reversion | 61.62 | -38.38 | 486 | 28.4 | -45.00 | -8.27 | -46.04 | 600 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.58 | -99.02 | 5285 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.14 | -25.71 | -80.18 | 1411 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -46.41 | -93.83 | 2533 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.63 | -89.31 | 1922 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -41.46 | -91.31 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.79 | -31.23 | -89.79 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.35 | -97.91 | 3484 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -57.55 | -96.28 | 3435 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -33.57 | -93.75 | 2340 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -34.92 | -83.28 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.58 | -55.62 | -99.58 | 6045 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.23 | -43.08 | -92.24 | 2622 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.11 | -95.40 | 3470 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.39 | -99.81 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -42.88 | -92.30 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.85 | -25.99 | -76.00 | 1646 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -60.43 | -97.64 | 3510 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -64.02 | -98.90 | 4947 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -26.91 | -68.80 | 1242 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -56.92 | -94.75 | 2795 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.09 | -39.31 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.88 | -99.67 | 6386 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.11 | -32.66 | -90.22 | 2329 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.95 | -20.17 | -79.19 | 1808 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.90 | -36.81 | -91.01 | 2202 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.04 | -52.02 | -97.04 | 3892 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -58.22 | -89.56 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.44 | -30.62 | -66.44 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.45 | -23.07 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.31 | -19.28 | -80.59 | 1753 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.41 | -51.01 | -97.43 | 4353 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.45 | -99.93 | 8401 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-13T17:10 | VWAP momentum · 1h | buy | SQQQ | 3.03 | — | rebalance up |
| 2026-11-13T17:00 | Agent (ML meta-label) | sell | GOOGL | 6.27 | -0.01 | selected signal exited |
| 2026-11-13T17:00 | Agent (ML meta-label) | sell | AAPL | 5.81 | 0.01 | selected signal exited |
| 2026-11-13T17:00 | VWAP momentum · 1h | buy | TSLA | 10.52 | — | rebalance up |
| 2026-11-13T17:00 | VWAP momentum · 1h | buy | META | 6.21 | — | rebalance up |
| 2026-11-13T17:00 | VWAP momentum · 1h | buy | DOGE-USD | 3.14 | — | rebalance up |
| 2026-11-13T17:00 | VWAP momentum · 1h | sell | XRP-USD | 10.43 | -0.14 | exit signal |
| 2026-11-13T17:00 | VWAP momentum · 1h | sell | SOL-USD | 12.48 | -0.22 | exit signal |
| 2026-11-13T16:48 | Williams %R · 1h | sell | SPY | 6.74 | -0.02 | target is flat |
| 2026-11-13T16:48 | VWAP momentum · 1h | buy | TSLA | 5.11 | — | entry |
| 2026-11-13T16:48 | VWAP momentum · 1h | sell | XRP-USD | 5.11 | -0.09 | rebalance down |
| 2026-11-13T16:31 | Agent (ML meta-label) | buy | TQQQ | 5.35 | — | following Z-score reversion |
| 2026-11-13T16:31 | Agent (ML meta-label) | buy | SOXL | 5.83 | — | entry |
| 2026-11-13T16:31 | Agent (ML meta-label) | buy | LABU | 5.83 | — | entry |
| 2026-11-13T16:31 | Agent (ML meta-label) | buy | COIN | 5.83 | — | entry |
| 2026-11-13T16:31 | Agent (ML meta-label) | buy | BITX | 5.83 | — | entry |
| 2026-11-13T16:31 | Agent (ML meta-label) | sell | TECL | 7.04 | 0.04 | rebalance down |
| 2026-11-13T16:31 | Agent (ML meta-label) | sell | SQQQ | 5.03 | 0.16 | rebalance down |
| 2026-11-13T16:31 | Agent (ML meta-label) | sell | NVDA | 4.78 | -0.10 | rebalance down |
| 2026-11-13T16:31 | Agent (ML meta-label) | sell | AMZN | 4.78 | -0.07 | rebalance down |
| 2026-11-13T16:31 | Agent (ML meta-label) | sell | AAPL | 7.03 | 0.02 | rebalance down |
| 2026-11-13T16:31 | Williams %R · 1h | buy | TSLA | 6.70 | — | entry signal |
| 2026-11-13T16:31 | Williams %R · 1h | buy | TNA | 6.76 | — | entry signal |
| 2026-11-13T16:31 | Williams %R · 1h | buy | SPY | 6.76 | — | entry signal |
| 2026-11-13T16:31 | Williams %R · 1h | buy | PLTR | 6.76 | — | entry signal |
| 2026-11-13T16:31 | Williams %R · 1h | buy | IWM | 6.76 | — | entry signal |
| 2026-11-13T16:31 | Williams %R · 1h | sell | XRP-USD | 4.31 | -0.05 | rebalance down |
| 2026-11-13T16:31 | Williams %R · 1h | sell | META | 6.86 | 0.04 | rebalance down |
| 2026-11-13T16:31 | Williams %R · 1h | sell | ETH-USD | 6.74 | -0.08 | rebalance down |
| 2026-11-13T16:31 | Williams %R · 1h | sell | BTC-USD | 6.75 | -0.06 | rebalance down |
| 2026-11-13T16:31 | Williams %R · 1h | sell | AMZN | 6.71 | -0.05 | rebalance down |
| 2026-11-13T16:31 | Stochastic reversion · 1h | buy | LABU | 8.76 | — | entry signal |
| 2026-11-13T16:31 | Stochastic reversion · 1h | buy | COIN | 8.76 | — | entry signal |
| 2026-11-13T16:31 | Stochastic reversion · 1h | buy | BITX | 8.76 | — | entry signal |
| 2026-11-13T16:31 | Stochastic reversion · 1h | sell | MSFT | 6.98 | 0.02 | rebalance down |
| 2026-11-13T16:31 | Stochastic reversion · 1h | sell | META | 6.89 | 0.07 | rebalance down |
| 2026-11-13T16:31 | Stochastic reversion · 1h | sell | IWM | 4.39 | 0.02 | rebalance down |
| 2026-11-13T16:31 | Stochastic reversion · 1h | sell | BTC-USD | 4.18 | -0.01 | rebalance down |
| 2026-11-13T16:31 | Stochastic reversion · 1h | sell | AMZN | 6.92 | -0.02 | rebalance down |
| 2026-11-13T16:31 | Bollinger reversion · 1h | buy | TNA | 10.13 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 17:10:05.000124+00:00 -> 2026-11-13 17:20:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
