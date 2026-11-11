# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T17:52:05.000145+00:00 · 56031 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.94 (-14.06%)

Closed trades 175, win rate 35.4%, fees £5.29, max drawdown -14.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.55 | +0.21 |
| SQQQ | 34.39 | -0.22 |
| UPRO | 17.19 | -0.01 |

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

Today: 25503 decisions in 2679 calls, $0.3226 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T17:52 | 2 / 21 / 7 | NANC 15% |  |
| Breezy | 2026-11-11T17:52 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-11T17:52 | 5 / 24 / 1 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.42 | 17.42 | 20 | 70.0 | 18.97 | 3.81 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.56 | 14.56 | 0 | — | 14.50 | 4.77 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.70 | 4.70 | 31 | 45.2 | 4.82 | 1.22 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.55 | 3.55 | 0 | — | 6.03 | 1.67 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.80 | 0.80 | 184 | 30.4 | 7.87 | 2.15 | -9.06 | 247 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.84 | -0.16 | 133 | 34.6 | 10.46 | 3.61 | -3.22 | 85 |
| 10 | Agent (rotation) | meta | 98.82 | -1.18 | 181 | 28.2 | -1.01 | -0.31 | -8.41 | 166 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 12 | Hold SPY | benchmark | 98.71 | -1.29 | 0 | — | 0.38 | 0.21 | -6.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.13 | -3.87 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.70 | -5.30 | 0 | — | -3.18 | -0.79 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.24 | -5.76 | 43 | 39.5 | -6.99 | -1.40 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.59 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Max aggression: 5-day momentum | meta | 91.78 | -8.22 | 19 | 47.4 | -23.95 | -1.08 | -45.81 | 25 |
| 21 | Trend pullback · 1h | trend | 91.62 | -8.38 | 109 | 22.9 | -16.24 | -5.69 | -18.84 | 80 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 89.98 | -10.02 | 404 | 33.2 | -12.51 | -3.71 | -14.11 | 601 |
| 24 | Squeeze breakout · 1h | breakout | 88.79 | -11.21 | 64 | 21.9 | -7.51 | -2.60 | -14.28 | 75 |
| 25 | Hold BTC | benchmark | 87.50 | -12.50 | 1 | 0.0 | -3.91 | -0.44 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.87 | -13.13 | 168 | 26.8 | -13.81 | -2.88 | -21.98 | 225 |
| 27 | Agent | meta | 85.94 | -14.06 | 175 | 35.4 | -15.48 | -7.93 | -15.65 | 205 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.48 | -14.52 | 2 | 0.0 | -4.32 | -0.35 | -24.16 | 1 |
| 29 | Max aggression: 1-day momentum | meta | 85.08 | -14.92 | 27 | 25.9 | -13.55 | -0.13 | -57.50 | 40 |
| 30 | Daily: Bullish score | daily | 84.00 | -16.00 | 16 | 18.8 | -9.41 | -1.41 | -19.51 | 15 |
| 31 | Agent (aggressive) | meta | 83.99 | -16.01 | 85 | 32.9 | -18.71 | -5.37 | -19.25 | 99 |
| 32 | Donchian 55/20 · 1h | breakout | 83.70 | -16.30 | 72 | 13.9 | -22.89 | -4.74 | -29.08 | 97 |
| 33 | ADX DI cross · 1h | trend | 83.63 | -16.37 | 185 | 18.9 | -19.55 | -3.01 | -30.84 | 274 |
| 34 | Keltner breakout · 1h | breakout | 83.54 | -16.46 | 110 | 23.6 | -17.69 | -3.54 | -25.10 | 177 |
| 35 | Stochastic reversion · 1h | reversion | 82.60 | -17.40 | 290 | 47.9 | -23.41 | -3.34 | -26.97 | 392 |
| 36 | Volume breakout · 1h | breakout | 81.98 | -18.02 | 148 | 27.7 | -13.13 | -2.92 | -21.11 | 97 |
| 37 | Opening range 15m | breakout | 81.94 | -18.06 | 501 | 31.3 | -18.28 | -4.86 | -21.11 | 735 |
| 38 | Heikin-Ashi · 1h | trend | 81.22 | -18.78 | 417 | 24.5 | -37.36 | -6.79 | -41.37 | 671 |
| 39 | MFI reversion · 1h | reversion | 80.05 | -19.95 | 373 | 35.4 | -16.03 | -1.96 | -23.02 | 158 |
| 40 | Connors RSI(2) · 1h | reversion | 79.94 | -20.06 | 208 | 39.9 | -20.88 | -6.95 | -20.95 | 124 |
| 41 | MACD cross · 1h | trend | 79.11 | -20.89 | 362 | 22.1 | -27.76 | -4.25 | -38.68 | 473 |
| 42 | CCI reversion · 1h | reversion | 78.59 | -21.41 | 331 | 45.0 | -26.59 | -4.00 | -31.08 | 450 |
| 43 | Bollinger breakout · 1h | breakout | 78.50 | -21.50 | 171 | 22.8 | -19.52 | -3.90 | -28.24 | 241 |
| 44 | MACD zero-line · 1h | trend | 76.73 | -23.27 | 160 | 16.9 | -18.87 | -3.29 | -31.28 | 209 |
| 45 | Bollinger reversion · 1h | reversion | 76.30 | -23.70 | 286 | 41.6 | -25.28 | -3.75 | -33.00 | 369 |
| 46 | Supertrend · 1h | trend | 75.80 | -24.20 | 168 | 13.1 | -28.14 | -4.73 | -36.07 | 230 |
| 47 | RSI momentum · 1h | momentum | 75.72 | -24.28 | 159 | 12.6 | -24.95 | -3.71 | -37.27 | 213 |
| 48 | Daily: Momentum burst | daily | 75.69 | -24.31 | 27 | 11.1 | -31.59 | -4.05 | -38.23 | 33 |
| 49 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 50 | EMA 20/50 cross · 1h | trend | 75.22 | -24.77 | 102 | 10.8 | -25.84 | -4.28 | -36.88 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.71 | -25.29 | 144 | 14.6 | -25.91 | -4.24 | -36.71 | 209 |
| 52 | ROC + volume · 1h | momentum | 73.99 | -26.01 | 376 | 27.7 | -35.52 | -6.19 | -39.25 | 390 |
| 53 | Williams %R · 1h | reversion | 73.24 | -26.77 | 352 | 46.0 | -34.93 | -5.36 | -36.83 | 527 |
| 54 | Donchian 20/10 · 1h | breakout | 73.16 | -26.84 | 142 | 19.7 | -30.42 | -5.38 | -35.62 | 216 |
| 55 | OBV trend · 1h | momentum | 72.22 | -27.78 | 279 | 18.6 | -25.31 | -4.39 | -35.07 | 284 |
| 56 | Z-score reversion · 1h | reversion | 71.94 | -28.06 | 196 | 38.3 | -22.15 | -2.95 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.53 | -30.47 | 175 | 32.6 | -24.30 | -3.31 | -32.54 | 230 |
| 58 | VWAP momentum · 1h | momentum | 68.87 | -31.13 | 853 | 22.4 | -51.24 | -10.16 | -54.61 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 67.89 | -32.11 | 253 | 9.9 | -33.52 | -6.10 | -41.69 | 338 |
| 60 | Agent (ML meta-label) | meta | 67.20 | -32.80 | 1730 | 25.0 | -8.22 | -1.09 | -18.12 | 329 |
| 61 | Candlestick reversal · 1h | reversion | 65.44 | -34.56 | 460 | 28.9 | -36.28 | -6.43 | -39.02 | 579 |
| 62 | Three white soldiers | momentum | 60.23 | -39.77 | 515 | 14.8 | -49.17 | -22.49 | -49.25 | 657 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.03 | -45.19 | -99.05 | 5330 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.87 | -25.94 | -80.45 | 1426 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -44.33 | -93.57 | 2543 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -31.35 | -89.40 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.02 | -39.30 | -91.32 | 2345 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.28 | -31.87 | -90.43 | 2208 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.81 | -52.88 | -97.84 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.29 | -55.53 | -96.43 | 3461 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -32.41 | -93.47 | 2341 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.06 | -34.03 | -83.49 | 1676 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -53.02 | -99.54 | 5942 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.18 | -42.32 | -92.31 | 2629 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.12 | -95.50 | 3427 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -69.96 | -99.80 | 6139 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -41.83 | -91.98 | 2268 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.55 | -24.44 | -75.44 | 1649 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -58.44 | -97.73 | 3538 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -60.52 | -98.84 | 4873 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.91 | -25.44 | -69.13 | 1240 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -52.20 | -94.75 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.69 | -36.51 | -85.22 | 1803 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.35 | -99.63 | 6314 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.46 | -31.68 | -89.46 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.62 | -19.66 | -77.76 | 1741 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.74 | -35.14 | -90.76 | 2158 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.37 | -96.69 | 3820 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.97 | -52.56 | -88.98 | 2128 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.45 | -27.36 | -66.88 | 826 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.01 | -22.25 | -72.14 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.39 | -18.47 | -78.61 | 1687 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -47.40 | -97.16 | 4259 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.40 | -99.93 | 8371 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T17:45 | Agent (ML meta-label) | sell | AAPL | 16.78 | -0.02 | selected signal exited |
| 2026-11-11T17:45 | Agent | buy | UPRO | 17.20 | — | following Gap and go |
| 2026-11-11T17:40 | Agent (aggressive) | buy | SQQQ | 41.53 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T17:40 | Agent | buy | SQQQ | 17.18 | — | rebalance up |
| 2026-11-11T17:40 | Agent | sell | UPRO | 17.20 | 0.01 | selected signal exited |
| 2026-11-11T17:40 | Three white soldiers | buy | UPRO | 15.05 | — | entry |
| 2026-11-11T17:35 | Agent (ML meta-label) | buy | AMD | 16.80 | — | entry |
| 2026-11-11T17:35 | Agent (ML meta-label) | buy | AAPL | 16.80 | — | entry |
| 2026-11-11T17:35 | Agent (aggressive) | sell | SQQQ | 41.41 | -0.70 | selected signal exited |
| 2026-11-11T17:35 | Agent | sell | SQQQ | 16.92 | -0.25 | rebalance down |
| 2026-11-11T17:30 | Agent | buy | UPRO | 17.19 | — | following Gap and go |
| 2026-11-11T17:30 | MFI reversion · 1h | sell | AAPL | 20.01 | 0.20 | exit signal |
| 2026-11-11T17:30 | Stochastic reversion · 1h | buy | MSFT | 11.78 | — | entry signal |
| 2026-11-11T17:30 | Stochastic reversion · 1h | buy | AMZN | 11.80 | — | entry signal |
| 2026-11-11T17:30 | Stochastic reversion · 1h | sell | NVDA | 4.68 | 0.14 | rebalance down |
| 2026-11-11T17:30 | Stochastic reversion · 1h | sell | MSTR | 4.61 | 0.06 | rebalance down |
| 2026-11-11T17:30 | Stochastic reversion · 1h | sell | ETHU | 4.86 | 0.21 | rebalance down |
| 2026-11-11T17:30 | Stochastic reversion · 1h | sell | DOGE-USD | 4.67 | 0.02 | rebalance down |
| 2026-11-11T17:30 | Stochastic reversion · 1h | sell | BITX | 4.75 | 0.10 | rebalance down |
| 2026-11-11T17:30 | Bollinger reversion · 1h | buy | MSFT | 19.07 | — | entry signal |
| 2026-11-11T17:30 | Bollinger reversion · 1h | sell | BITX | 15.34 | 0.44 | exit signal |
| 2026-11-11T17:30 | Volume breakout · 1h | buy | SPY | 8.01 | — | entry signal |
| 2026-11-11T17:30 | Volume breakout · 1h | buy | QQQ | 4.84 | — | rebalance up |
| 2026-11-11T17:30 | Volume breakout · 1h | sell | TSLA | 6.55 | -0.04 | rebalance down |
| 2026-11-11T17:30 | Volume breakout · 1h | sell | ETH-USD | 6.30 | 0.01 | rebalance down |
| 2026-11-11T17:30 | EMA 20/50 cross · 1h | buy | TSLA | 9.58 | — | entry signal |
| 2026-11-11T17:30 | EMA 20/50 cross · 1h | sell | META | 3.77 | 0.04 | rebalance down |
| 2026-11-11T17:30 | EMA 20/50 cross · 1h | sell | AMD | 5.59 | 0.49 | rebalance down |
| 2026-11-11T17:25 | Agent (rotation) | buy | TQQQ | 32.89 | — | rebalance up |
| 2026-11-11T17:25 | Day trade: Open breakout · TQQQ/SQQQ | buy | TQQQ | 117.56 | — | entry |
| 2026-11-11T17:25 | Agent (ML meta-label) | sell | TECL | 13.01 | 0.03 | selected signal exited |
| 2026-11-11T17:25 | Three white soldiers | buy | TQQQ | 15.06 | — | entry signal |
| 2026-11-11T17:25 | Three white soldiers | buy | TNA | 15.06 | — | entry signal |
| 2026-11-11T17:20 | Agent (ML meta-label) | buy | TECL | 12.97 | — | entry |
| 2026-11-11T17:20 | Agent (ML meta-label) | sell | AMD | 16.80 | 0.01 | selected signal exited |
| 2026-11-11T17:15 | Agent (ML meta-label) | buy | AMD | 16.79 | — | entry |
| 2026-11-11T17:15 | Z-score reversion · 1h | buy | NVDA | 3.59 | — | rebalance up |
| 2026-11-11T17:10 | Agent | buy | SQQQ | 17.14 | — | rebalance up |
| 2026-11-11T17:05 | Agent (ML meta-label) | sell | AMD | 16.91 | 0.13 | selected signal exited |
| 2026-11-11T17:05 | VWAP momentum · 1h | buy | MSTR | 1.79 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 17:52:05.000145+00:00 -> 2026-11-11 18:02:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
