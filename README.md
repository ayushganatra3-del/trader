# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-13T16:40:05.000172+00:00 · 58412 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.17 (-14.83%)

Closed trades 194, win rate 35.6%, fees £5.62, max drawdown -15.42%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TQQQ | 17.00 | -0.05 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-13 | MGM 12%, BBTX 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-12)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 28.55 · VIX 18.70 · last follow-through day 2026-11-11

Best bullish scores: AAPL 6.8, SQQQ 5.7, AMZN 5.6, AMD 5.4, TSLA 5.3, IWM 3.6

### AI bees (Jev: typesafe/jev-1.13)

Today: 22443 decisions in 2691 calls, $0.2896 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-13T16:40 | 2 / 11 / 17 | cash |  |
| Breezy | 2026-11-13T16:40 | 0 / 24 / 6 | cash |  |
| Boozy | 2026-11-13T16:40 | 4 / 21 / 5 | BITX 63% |  |

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
| 1 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 117.89 | 17.89 | 34 | 29.4 | 26.54 | 3.64 | -8.66 | 45 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 117.70 | 17.70 | 0 | — | 15.22 | 5.08 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 114.78 | 14.78 | 22 | 68.2 | 18.35 | 3.67 | -4.91 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.21 | 7.21 | 32 | 43.8 | 7.21 | 1.70 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 105.08 | 5.08 | 0 | — | 7.14 | 1.94 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 101.78 | 1.78 | 141 | 34.8 | 8.39 | 3.26 | -3.96 | 90 |
| 7 | Gap and go | momentum | 100.43 | 0.43 | 193 | 33.2 | 6.52 | 1.85 | -9.06 | 229 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | 0.44 | 0.34 | -18.69 | 5 |
| 11 | Hold SPY | benchmark | 97.65 | -2.35 | 0 | — | -1.20 | -0.34 | -6.18 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 96.16 | -3.84 | 0 | — | -4.19 | -1.07 | -9.25 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 95.93 | -4.07 | 1 | 0.0 | -4.13 | -2.48 | -6.65 | 2 |
| 14 | Agent (rotation) | meta | 95.46 | -4.54 | 191 | 30.4 | -3.44 | -1.14 | -8.69 | 161 |
| 15 | VWAP reversion · 1h | reversion | 95.29 | -4.71 | 144 | 47.2 | -12.88 | -3.34 | -13.44 | 155 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.21 | -3.05 | -5.99 | 26 |
| 17 | Copy: Insider buying | copy | 93.70 | -6.30 | 43 | 39.5 | -5.66 | -1.07 | -14.81 | 66 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -9.05 | -7.57 | -9.09 | 21 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.93 | -7.07 | 0 | — | -5.49 | -1.47 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 91.62 | -8.38 | 110 | 22.7 | -14.81 | -5.43 | -17.71 | 71 |
| 21 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -3.34 | -0.71 | -15.43 | 81 |
| 22 | Timing: Nasdaq FTD · TQQQ ⏸ | daily | 87.28 | -12.72 | 2 | 0.0 | -12.97 | -2.60 | -19.15 | 2 |
| 23 | Opening range 30m | breakout | 86.27 | -13.73 | 433 | 33.3 | -9.78 | -3.07 | -14.11 | 603 |
| 24 | Daily: Bullish score | daily | 86.17 | -13.83 | 16 | 18.8 | -9.74 | -1.52 | -19.56 | 15 |
| 25 | Agent | meta | 85.17 | -14.83 | 194 | 35.6 | -16.10 | -8.04 | -16.26 | 210 |
| 26 | Parabolic SAR · 1h | trend | 85.02 | -14.98 | 175 | 28.6 | -15.82 | -3.41 | -22.47 | 217 |
| 27 | Agent (aggressive) | meta | 83.49 | -16.51 | 95 | 34.7 | -18.60 | -5.23 | -19.31 | 101 |
| 28 | Donchian 55/20 · 1h | breakout | 81.39 | -18.61 | 73 | 13.7 | -23.60 | -4.90 | -30.83 | 90 |
| 29 | Hold BTC | benchmark | 81.03 | -18.97 | 1 | 0.0 | -11.37 | -1.59 | -22.00 | 1 |
| 30 | Connors RSI(2) · 1h | reversion | 80.57 | -19.43 | 211 | 40.3 | -18.20 | -6.40 | -18.30 | 114 |
| 31 | Volume breakout · 1h | breakout | 80.53 | -19.47 | 160 | 28.8 | -13.17 | -3.05 | -22.12 | 90 |
| 32 | Keltner breakout · 1h | breakout | 80.52 | -19.48 | 120 | 25.8 | -17.35 | -3.51 | -25.32 | 171 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 79.88 | -20.12 | 2 | 0.0 | -10.89 | -1.27 | -24.16 | 1 |
| 34 | Stochastic reversion · 1h | reversion | 78.77 | -21.23 | 302 | 47.4 | -26.98 | -3.99 | -28.24 | 395 |
| 35 | Opening range 15m | breakout | 78.67 | -21.33 | 526 | 31.2 | -17.08 | -4.56 | -21.36 | 719 |
| 36 | MFI reversion · 1h | reversion | 77.01 | -22.99 | 395 | 35.2 | -22.99 | -2.98 | -26.64 | 162 |
| 37 | ADX DI cross · 1h | trend | 76.96 | -23.04 | 198 | 19.7 | -23.73 | -3.59 | -32.07 | 272 |
| 38 | Max aggression: 5-day momentum ⏸ | meta | 76.15 | -23.85 | 21 | 42.9 | -44.26 | -2.82 | -50.62 | 22 |
| 39 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.92 | -8.77 | -31.41 | 114 |
| 40 | Bollinger breakout · 1h | breakout | 75.12 | -24.88 | 183 | 22.4 | -23.19 | -4.84 | -30.71 | 240 |
| 41 | Heikin-Ashi · 1h | trend | 75.10 | -24.90 | 442 | 24.2 | -37.81 | -7.05 | -39.26 | 661 |
| 42 | MACD cross · 1h | trend | 74.55 | -25.45 | 385 | 23.6 | -29.54 | -4.39 | -38.65 | 472 |
| 43 | MACD zero-line · 1h | trend | 73.46 | -26.54 | 171 | 18.7 | -23.16 | -4.53 | -30.99 | 203 |
| 44 | Max aggression: 1-day momentum | meta | 73.44 | -26.56 | 29 | 27.6 | -21.63 | -0.70 | -57.50 | 41 |
| 45 | Supertrend · 1h | trend | 72.42 | -27.58 | 180 | 15.0 | -30.63 | -5.23 | -36.51 | 215 |
| 46 | RSI momentum · 1h | momentum | 72.41 | -27.59 | 171 | 14.0 | -27.54 | -4.24 | -37.92 | 209 |
| 47 | EMA 20/50 cross · 1h | trend | 71.61 | -28.39 | 109 | 10.1 | -29.89 | -5.04 | -40.51 | 121 |
| 48 | ROC + volume · 1h | momentum | 71.53 | -28.46 | 397 | 28.7 | -31.20 | -5.75 | -38.37 | 377 |
| 49 | Bollinger reversion · 1h | reversion | 71.18 | -28.82 | 301 | 41.5 | -34.02 | -5.32 | -35.72 | 380 |
| 50 | Triple EMA stack · 1h | trend | 71.05 | -28.95 | 150 | 14.0 | -29.40 | -4.87 | -38.64 | 205 |
| 51 | CCI reversion · 1h | reversion | 70.54 | -29.46 | 346 | 43.4 | -39.00 | -6.15 | -39.55 | 462 |
| 52 | OBV trend · 1h | momentum | 69.46 | -30.54 | 298 | 19.1 | -30.41 | -5.36 | -38.08 | 276 |
| 53 | Daily: Momentum burst ⏸ | daily | 69.40 | -30.60 | 30 | 13.3 | -34.55 | -4.65 | -37.81 | 33 |
| 54 | Donchian 20/10 · 1h | breakout | 69.06 | -30.94 | 153 | 19.0 | -30.45 | -5.44 | -37.58 | 209 |
| 55 | Williams %R · 1h | reversion | 67.38 | -32.62 | 381 | 43.6 | -43.37 | -7.12 | -44.04 | 537 |
| 56 | Z-score reversion · 1h | reversion | 64.98 | -35.02 | 204 | 37.3 | -31.03 | -4.37 | -31.55 | 236 |
| 57 | EMA 9/21 cross · 1h | trend | 64.43 | -35.57 | 263 | 10.3 | -38.27 | -7.71 | -43.16 | 329 |
| 58 | Agent (ML meta-label) | meta | 63.90 | -36.10 | 1837 | 24.7 | -16.69 | -2.52 | -22.37 | 335 |
| 59 | RSI(14) reversion · 1h | reversion | 63.47 | -36.53 | 186 | 32.8 | -38.39 | -5.71 | -38.93 | 241 |
| 60 | VWAP momentum · 1h | momentum | 62.59 | -37.41 | 909 | 22.2 | -53.31 | -10.66 | -53.99 | 1220 |
| 61 | Candlestick reversal · 1h | reversion | 60.96 | -39.04 | 486 | 28.4 | -45.37 | -8.28 | -45.99 | 600 |
| 62 | Three white soldiers | momentum | 58.43 | -41.57 | 541 | 14.6 | -49.42 | -22.17 | -49.51 | 662 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.61 | -99.02 | 5275 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.09 | -25.67 | -80.18 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -46.39 | -93.83 | 2532 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.29 | -31.63 | -89.31 | 1919 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -41.38 | -91.32 | 2338 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.75 | -31.07 | -89.77 | 2194 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.90 | -52.47 | -97.90 | 3480 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -57.29 | -96.27 | 3438 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -33.55 | -93.73 | 2341 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.22 | -34.89 | -83.22 | 1661 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -55.68 | -99.59 | 6040 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -42.74 | -92.24 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -37.11 | -95.40 | 3469 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -73.41 | -99.81 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -42.85 | -92.30 | 2263 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.99 | -26.02 | -76.08 | 1651 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -60.54 | -97.64 | 3512 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.90 | -64.07 | -98.90 | 4949 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.70 | -26.90 | -68.85 | 1241 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.76 | -57.06 | -94.76 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.03 | -38.96 | -85.21 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.67 | -75.84 | -99.67 | 6386 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.20 | -32.73 | -90.22 | 2329 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.10 | -20.13 | -79.17 | 1805 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.97 | -36.96 | -91.00 | 2193 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.04 | -52.06 | -97.05 | 3893 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -58.33 | -89.49 | 2143 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.40 | -30.54 | -66.40 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.33 | -22.95 | -71.48 | 1257 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.49 | -19.21 | -80.56 | 1755 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.43 | -51.01 | -97.44 | 4356 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.32 | -99.93 | 8400 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-11-13T16:31 | Bollinger reversion · 1h | buy | LABU | 10.19 | — | entry signal |
| 2026-11-13T16:31 | Bollinger reversion · 1h | buy | IWM | 10.19 | — | entry signal |
| 2026-11-13T16:31 | Bollinger reversion · 1h | buy | COIN | 10.19 | — | entry signal |
| 2026-11-13T16:31 | Bollinger reversion · 1h | sell | MSFT | 7.94 | 0.09 | rebalance down |
| 2026-11-13T16:31 | Bollinger reversion · 1h | sell | META | 17.94 | 0.15 | exit signal |
| 2026-11-13T16:31 | Bollinger reversion · 1h | sell | ETH-USD | 7.32 | -0.13 | rebalance down |
| 2026-11-13T16:31 | Bollinger reversion · 1h | sell | BTC-USD | 7.50 | -0.08 | rebalance down |
| 2026-11-13T16:31 | RSI(14) reversion · 1h | buy | LABU | 9.62 | — | entry signal |
| 2026-11-13T16:31 | RSI(14) reversion · 1h | sell | NVDA | 3.21 | -0.08 | rebalance down |
| 2026-11-13T16:31 | RSI(14) reversion · 1h | sell | ETH-USD | 3.20 | -0.04 | rebalance down |
| 2026-11-13T16:31 | RSI(14) reversion · 1h | sell | BTC-USD | 3.21 | -0.03 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-15 16:40:05.000172+00:00 -> 2026-11-13 16:50:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
