# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T17:23:05.000125+00:00 · 56003 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.97 (-14.03%)

Closed trades 174, win rate 35.1%, fees £5.24, max drawdown -14.43%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.48 | +0.14 |
| SQQQ | 34.23 | -0.37 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 22968 decisions in 2595 calls, $0.2931 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T17:23 | 12 / 15 / 3 | AMD 15%, ETHU 15%, SOXL 15% |  |
| Breezy | 2026-11-11T17:23 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-11T17:23 | 9 / 19 / 2 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| MFI reversion | LABU | 1.66 | +5.37% | 3 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.11 | 3.83 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.55 | 14.55 | 0 | — | 14.46 | 4.76 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.44 | 4.45 | 31 | 45.2 | 4.59 | 1.17 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.54 | 3.54 | 0 | — | 6.05 | 1.67 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.45 | 0.45 | 184 | 30.4 | 7.50 | 2.07 | -9.06 | 247 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.81 | -0.19 | 133 | 34.6 | 10.44 | 3.60 | -3.22 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Agent (rotation) | meta | 98.67 | -1.33 | 181 | 28.2 | -1.22 | -0.39 | -8.53 | 161 |
| 12 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | 0.31 | 0.19 | -6.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.11 | -3.89 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.68 | -5.32 | 0 | — | -3.18 | -0.79 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.30 | -5.70 | 43 | 39.5 | -6.89 | -1.38 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.63 | -3.32 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.66 | -8.34 | 109 | 22.9 | -16.20 | -5.68 | -18.84 | 80 |
| 21 | Max aggression: 5-day momentum | meta | 91.23 | -8.77 | 19 | 47.4 | -24.39 | -1.13 | -45.81 | 25 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 89.81 | -10.19 | 404 | 33.2 | -12.66 | -3.78 | -14.11 | 600 |
| 24 | Squeeze breakout · 1h | breakout | 88.81 | -11.19 | 64 | 21.9 | -7.59 | -2.33 | -14.28 | 75 |
| 25 | Hold BTC | benchmark | 87.62 | -12.38 | 1 | 0.0 | -3.53 | -0.38 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.70 | -13.30 | 168 | 26.8 | -13.95 | -2.92 | -21.98 | 225 |
| 27 | Agent | meta | 85.97 | -14.03 | 174 | 35.1 | -15.35 | -7.73 | -15.44 | 203 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.17 | -14.83 | 2 | 0.0 | -4.65 | -0.40 | -24.16 | 1 |
| 29 | Max aggression: 1-day momentum | meta | 84.57 | -15.43 | 27 | 25.9 | -14.05 | -0.17 | -57.50 | 40 |
| 30 | Daily: Bullish score | daily | 84.09 | -15.91 | 16 | 18.8 | -8.84 | -1.32 | -19.40 | 15 |
| 31 | Agent (aggressive) | meta | 83.97 | -16.03 | 84 | 33.3 | -18.02 | -5.10 | -18.56 | 97 |
| 32 | Donchian 55/20 · 1h | breakout | 83.44 | -16.55 | 72 | 13.9 | -23.12 | -4.79 | -29.08 | 97 |
| 33 | ADX DI cross · 1h | trend | 83.33 | -16.67 | 185 | 18.9 | -21.20 | -3.30 | -30.55 | 273 |
| 34 | Keltner breakout · 1h | breakout | 83.21 | -16.79 | 110 | 23.6 | -19.93 | -3.99 | -25.10 | 181 |
| 35 | Stochastic reversion · 1h | reversion | 82.87 | -17.13 | 290 | 47.9 | -23.40 | -3.29 | -27.17 | 392 |
| 36 | Opening range 15m | breakout | 81.77 | -18.23 | 501 | 31.3 | -18.43 | -4.92 | -21.11 | 734 |
| 37 | Volume breakout · 1h | breakout | 81.75 | -18.25 | 148 | 27.7 | -13.55 | -3.03 | -21.11 | 96 |
| 38 | Heikin-Ashi · 1h | trend | 81.02 | -18.98 | 417 | 24.5 | -37.92 | -6.88 | -41.76 | 671 |
| 39 | MFI reversion · 1h | reversion | 80.16 | -19.84 | 372 | 35.2 | -15.63 | -1.89 | -23.02 | 158 |
| 40 | Connors RSI(2) · 1h | reversion | 80.00 | -20.00 | 208 | 39.9 | -20.83 | -6.93 | -20.87 | 124 |
| 41 | MACD cross · 1h | trend | 78.90 | -21.10 | 362 | 22.1 | -28.46 | -4.47 | -38.69 | 474 |
| 42 | CCI reversion · 1h | reversion | 78.66 | -21.34 | 331 | 45.0 | -26.38 | -3.95 | -31.08 | 451 |
| 43 | Bollinger breakout · 1h | breakout | 78.51 | -21.49 | 171 | 22.8 | -19.49 | -3.90 | -28.24 | 241 |
| 44 | MACD zero-line · 1h | trend | 76.49 | -23.51 | 160 | 16.9 | -20.43 | -3.78 | -31.20 | 213 |
| 45 | Bollinger reversion · 1h | reversion | 76.48 | -23.52 | 285 | 41.4 | -24.50 | -3.61 | -32.51 | 370 |
| 46 | Supertrend · 1h | trend | 75.58 | -24.42 | 168 | 13.1 | -28.37 | -4.81 | -36.07 | 230 |
| 47 | RSI momentum · 1h | momentum | 75.52 | -24.48 | 159 | 12.6 | -24.69 | -3.65 | -37.44 | 211 |
| 48 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 49 | Daily: Momentum burst | daily | 75.15 | -24.85 | 27 | 11.1 | -31.97 | -4.16 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.80 | -25.20 | 102 | 10.8 | -26.00 | -4.42 | -36.22 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.28 | -25.72 | 144 | 14.6 | -26.12 | -4.31 | -36.49 | 209 |
| 52 | ROC + volume · 1h | momentum | 73.79 | -26.21 | 376 | 27.7 | -35.45 | -6.20 | -39.14 | 389 |
| 53 | Williams %R · 1h | reversion | 73.40 | -26.60 | 352 | 46.0 | -34.97 | -5.32 | -37.04 | 528 |
| 54 | Donchian 20/10 · 1h | breakout | 72.96 | -27.04 | 142 | 19.7 | -30.42 | -5.41 | -35.62 | 216 |
| 55 | Z-score reversion · 1h | reversion | 72.15 | -27.85 | 196 | 38.3 | -21.89 | -2.89 | -28.98 | 234 |
| 56 | OBV trend · 1h | momentum | 71.85 | -28.15 | 279 | 18.6 | -25.77 | -4.52 | -34.92 | 284 |
| 57 | RSI(14) reversion · 1h | reversion | 69.68 | -30.32 | 175 | 32.6 | -24.55 | -3.41 | -32.54 | 236 |
| 58 | VWAP momentum · 1h | momentum | 68.74 | -31.26 | 853 | 22.4 | -51.63 | -10.31 | -54.86 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 67.67 | -32.33 | 253 | 9.9 | -33.67 | -6.16 | -41.69 | 338 |
| 60 | Agent (ML meta-label) | meta | 67.14 | -32.86 | 1728 | 24.9 | -14.72 | -2.44 | -19.79 | 343 |
| 61 | Candlestick reversal · 1h | reversion | 65.56 | -34.44 | 460 | 28.9 | -37.67 | -6.76 | -40.48 | 589 |
| 62 | Three white soldiers | momentum | 60.23 | -39.77 | 515 | 14.8 | -49.18 | -22.50 | -49.19 | 654 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -45.11 | -99.04 | 5328 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.82 | -25.86 | -80.45 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -44.73 | -93.58 | 2546 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -31.32 | -89.40 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.93 | -38.92 | -91.22 | 2343 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.27 | -31.77 | -90.41 | 2206 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.81 | -53.19 | -97.84 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -55.31 | -96.41 | 3462 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.40 | -32.51 | -93.48 | 2343 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.04 | -34.10 | -83.50 | 1677 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -52.72 | -99.54 | 5944 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -42.36 | -92.31 | 2630 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.16 | -95.51 | 3428 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.61 | -99.80 | 6136 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.99 | -42.08 | -92.02 | 2272 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.65 | -24.54 | -75.52 | 1644 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -58.59 | -97.73 | 3543 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -61.09 | -98.84 | 4883 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.92 | -25.48 | -69.11 | 1238 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -52.15 | -94.75 | 2789 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.81 | -37.08 | -85.28 | 1806 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.43 | -99.63 | 6325 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.45 | -31.68 | -89.46 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.59 | -19.64 | -77.75 | 1748 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -35.62 | -90.65 | 2174 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.36 | -96.69 | 3822 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.01 | -53.07 | -89.03 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.48 | -27.48 | -66.81 | 824 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.93 | -22.15 | -72.04 | 1269 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.34 | -18.43 | -78.59 | 1692 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.17 | -47.53 | -97.18 | 4263 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.37 | -99.93 | 8354 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T17:20 | Agent (ML meta-label) | buy | TECL | 12.97 | — | entry |
| 2026-11-11T17:20 | Agent (ML meta-label) | sell | AMD | 16.80 | 0.01 | selected signal exited |
| 2026-11-11T17:15 | Agent (ML meta-label) | buy | AMD | 16.79 | — | entry |
| 2026-11-11T17:15 | Z-score reversion · 1h | buy | NVDA | 3.59 | — | rebalance up |
| 2026-11-11T17:10 | Agent | buy | SQQQ | 17.14 | — | rebalance up |
| 2026-11-11T17:05 | Agent (ML meta-label) | sell | AMD | 16.91 | 0.13 | selected signal exited |
| 2026-11-11T17:05 | VWAP momentum · 1h | buy | MSTR | 1.79 | — | entry |
| 2026-11-11T17:05 | VWAP momentum · 1h | buy | META | 3.43 | — | entry |
| 2026-11-11T17:05 | VWAP momentum · 1h | sell | ETHU | 5.22 | 0.16 | target is flat |
| 2026-11-11T17:00 | Agent (ML meta-label) | sell | TECL | 16.85 | 0.09 | selected signal exited |
| 2026-11-11T17:00 | Agent | sell | SQQQ | 16.84 | -0.26 | rebalance down |
| 2026-11-11T17:00 | Z-score reversion · 1h | buy | XRP-USD | 3.67 | — | rebalance up |
| 2026-11-11T17:00 | Z-score reversion · 1h | buy | ETH-USD | 3.59 | — | rebalance up |
| 2026-11-11T17:00 | Z-score reversion · 1h | sell | BTC-USD | 14.32 | 0.01 | exit signal |
| 2026-11-11T17:00 | RSI(14) reversion · 1h | buy | MSTR | 3.55 | — | rebalance up |
| 2026-11-11T17:00 | RSI(14) reversion · 1h | buy | ETHU | 10.19 | — | rebalance up |
| 2026-11-11T17:00 | RSI(14) reversion · 1h | sell | ETH-USD | 17.20 | 0.12 | exit signal |
| 2026-11-11T17:00 | Candlestick reversal · 1h | sell | BTC-USD | 16.26 | 0.00 | exit signal |
| 2026-11-11T17:00 | VWAP momentum · 1h | buy | LABU | 1.91 | — | entry |
| 2026-11-11T17:00 | VWAP momentum · 1h | buy | IWM | 3.27 | — | entry |
| 2026-11-11T17:00 | VWAP momentum · 1h | sell | BITX | 5.17 | 0.11 | target is flat |
| 2026-11-11T17:00 | MACD zero-line · 1h | buy | SOL-USD | 4.43 | — | entry signal |
| 2026-11-11T17:00 | MACD zero-line · 1h | sell | QQQ | 4.43 | 0.16 | rebalance down |
| 2026-11-11T16:56 | Agent (ML meta-label) | sell | COIN | 13.53 | -0.04 | selected signal exited |
| 2026-11-11T16:50 | Agent (ML meta-label) | buy | TECL | 16.76 | — | entry |
| 2026-11-11T16:50 | Agent (ML meta-label) | buy | COIN | 13.57 | — | following Donchian 20/10 |
| 2026-11-11T16:45 | Agent (ML meta-label) | sell | COIN | 9.66 | -0.06 | selected signal exited |
| 2026-11-11T16:45 | Agent (aggressive) | buy | COIN | 41.98 | — | following Donchian 20/10 |
| 2026-11-11T16:45 | Three white soldiers | sell | COIN | 15.07 | 0.00 | exit signal |
| 2026-11-11T16:41 | Triple EMA stack · 1h | buy | LABU | 3.73 | — | rebalance up |
| 2026-11-11T16:41 | Triple EMA stack · 1h | sell | AAPL | 3.73 | 0.07 | rebalance down |
| 2026-11-11T16:41 | Three white soldiers | sell | IWM | 15.04 | -0.04 | exit signal |
| 2026-11-11T16:35 | Agent (ML meta-label) | buy | COIN | 9.72 | — | following Donchian 20/10 |
| 2026-11-11T16:35 | Agent (ML meta-label) | sell | TSLA | 16.72 | -0.05 | selected signal exited |
| 2026-11-11T16:35 | Agent (ML meta-label) | sell | TECL | 16.75 | -0.02 | selected signal exited |
| 2026-11-11T16:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 103.97 | — | entry |
| 2026-11-11T16:30 | Williams %R · 1h | buy | META | 12.18 | — | entry signal |
| 2026-11-11T16:30 | Williams %R · 1h | sell | GOOGL | 10.26 | 0.15 | exit signal |
| 2026-11-11T16:30 | Williams %R · 1h | sell | COIN | 10.51 | 0.39 | exit signal |
| 2026-11-11T16:30 | Stochastic reversion · 1h | buy | NVDA | 7.06 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 17:23:05.000125+00:00 -> 2026-11-11 17:33:05.000125+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
