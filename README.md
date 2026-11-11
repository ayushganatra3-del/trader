# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T20:20:05.000114+00:00 · 56168 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.91 (-14.09%)

Closed trades 181, win rate 35.4%, fees £5.39, max drawdown -14.66%.

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

Today: 37872 decisions in 3090 calls, $0.4671 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T20:20 | 2 / 17 / 11 | cash |  |
| Breezy | 2026-11-11T20:20 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-11T20:20 | 6 / 19 / 5 | BITX 65% |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.06 | 16.07 | 20 | 70.0 | 18.66 | 3.77 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.84 | 15.84 | 0 | — | 15.54 | 5.16 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.69 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.68 | 3.68 | 0 | — | 6.14 | 1.71 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.36 | 0.36 | 191 | 33.0 | 6.64 | 1.88 | -9.06 | 232 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.71 | -0.29 | 134 | 34.3 | 10.31 | 3.58 | -3.28 | 85 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 11 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -0.58 | -0.12 | -6.18 | 1 |
| 12 | Agent (rotation) | meta | 98.21 | -1.79 | 188 | 30.3 | -2.78 | -1.00 | -9.81 | 165 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 97.01 | -2.99 | 0 | — | -2.30 | -0.54 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -10.98 | -2.76 | -13.44 | 155 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.59 | -5.41 | 0 | — | -3.21 | -0.81 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.44 | -5.56 | 43 | 39.5 | -6.81 | -1.37 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.56 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.69 | -8.31 | 109 | 22.9 | -13.53 | -5.04 | -16.41 | 76 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 89.08 | -10.93 | 404 | 33.2 | -11.84 | -3.77 | -14.11 | 597 |
| 23 | Squeeze breakout · 1h | breakout | 88.68 | -11.32 | 64 | 21.9 | -4.10 | -0.81 | -16.46 | 77 |
| 24 | Max aggression: 5-day momentum | meta | 88.33 | -11.67 | 19 | 47.4 | -26.83 | -1.39 | -45.81 | 25 |
| 25 | Hold BTC | benchmark | 87.54 | -12.46 | 1 | 0.0 | -3.83 | -0.25 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.60 | -13.40 | 168 | 26.8 | -14.04 | -2.97 | -21.94 | 224 |
| 27 | Agent | meta | 85.91 | -14.09 | 181 | 35.4 | -15.30 | -7.74 | -15.66 | 208 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 84.45 | -15.55 | 2 | 0.0 | -6.20 | -0.63 | -24.16 | 1 |
| 29 | Daily: Bullish score | daily | 84.34 | -15.66 | 16 | 18.8 | -9.98 | -1.56 | -19.56 | 15 |
| 30 | Agent (aggressive) | meta | 83.84 | -16.16 | 88 | 34.1 | -18.10 | -5.16 | -18.67 | 98 |
| 31 | Donchian 55/20 · 1h | breakout | 83.29 | -16.71 | 72 | 13.9 | -22.66 | -4.81 | -29.34 | 92 |
| 32 | ADX DI cross · 1h | trend | 82.67 | -17.33 | 185 | 18.9 | -21.01 | -3.52 | -29.87 | 273 |
| 33 | Keltner breakout · 1h | breakout | 82.33 | -17.67 | 111 | 24.3 | -16.52 | -3.36 | -24.55 | 169 |
| 34 | Stochastic reversion · 1h | reversion | 82.25 | -17.75 | 292 | 48.3 | -23.63 | -3.45 | -27.08 | 391 |
| 35 | Max aggression: 1-day momentum | meta | 81.88 | -18.12 | 27 | 25.9 | -16.82 | -0.38 | -57.50 | 40 |
| 36 | Volume breakout · 1h | breakout | 81.13 | -18.87 | 148 | 27.7 | -12.03 | -2.71 | -21.11 | 96 |
| 37 | Opening range 15m | breakout | 81.06 | -18.94 | 501 | 31.3 | -18.16 | -4.93 | -21.11 | 722 |
| 38 | Heikin-Ashi · 1h | trend | 80.42 | -19.58 | 418 | 24.6 | -35.93 | -6.66 | -39.41 | 663 |
| 39 | Connors RSI(2) · 1h | reversion | 80.22 | -19.78 | 208 | 39.9 | -20.53 | -6.91 | -20.96 | 123 |
| 40 | MFI reversion · 1h | reversion | 79.64 | -20.36 | 374 | 35.6 | -15.41 | -1.93 | -23.02 | 158 |
| 41 | MACD cross · 1h | trend | 78.43 | -21.57 | 362 | 22.1 | -27.61 | -3.99 | -39.83 | 466 |
| 42 | CCI reversion · 1h | reversion | 78.19 | -21.81 | 332 | 45.2 | -27.71 | -4.27 | -31.08 | 447 |
| 43 | Bollinger breakout · 1h | breakout | 77.55 | -22.45 | 172 | 22.7 | -20.93 | -4.41 | -28.24 | 240 |
| 44 | MACD zero-line · 1h | trend | 76.05 | -23.95 | 160 | 16.9 | -20.24 | -3.90 | -30.74 | 211 |
| 45 | Bollinger reversion · 1h | reversion | 75.81 | -24.19 | 286 | 41.6 | -27.83 | -4.26 | -34.84 | 367 |
| 46 | Supertrend · 1h | trend | 75.50 | -24.50 | 168 | 13.1 | -28.70 | -5.01 | -36.14 | 221 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.16 | -8.87 | -31.80 | 116 |
| 48 | RSI momentum · 1h | momentum | 75.14 | -24.86 | 159 | 12.6 | -25.40 | -3.81 | -37.48 | 214 |
| 49 | Daily: Momentum burst | daily | 74.98 | -25.02 | 27 | 11.1 | -33.10 | -4.46 | -38.23 | 33 |
| 50 | EMA 20/50 cross · 1h | trend | 74.64 | -25.36 | 103 | 10.7 | -26.66 | -4.48 | -37.12 | 116 |
| 51 | Triple EMA stack · 1h | trend | 74.20 | -25.80 | 144 | 14.6 | -25.43 | -4.19 | -35.90 | 210 |
| 52 | ROC + volume · 1h | momentum | 73.25 | -26.75 | 376 | 27.7 | -32.30 | -5.78 | -38.61 | 380 |
| 53 | Williams %R · 1h | reversion | 72.57 | -27.43 | 353 | 46.2 | -34.63 | -5.30 | -36.33 | 526 |
| 54 | Donchian 20/10 · 1h | breakout | 72.41 | -27.59 | 142 | 19.7 | -27.63 | -5.00 | -35.64 | 209 |
| 55 | OBV trend · 1h | momentum | 71.79 | -28.21 | 281 | 19.2 | -27.17 | -4.65 | -36.82 | 288 |
| 56 | Z-score reversion · 1h | reversion | 71.44 | -28.56 | 197 | 38.6 | -22.74 | -3.11 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.01 | -30.99 | 175 | 32.6 | -26.06 | -3.72 | -32.54 | 231 |
| 58 | VWAP momentum · 1h | momentum | 68.34 | -31.66 | 861 | 22.8 | -52.26 | -11.06 | -54.23 | 1225 |
| 59 | EMA 9/21 cross · 1h | trend | 67.51 | -32.49 | 253 | 9.9 | -33.29 | -6.21 | -41.65 | 339 |
| 60 | Agent (ML meta-label) | meta | 66.49 | -33.51 | 1750 | 24.7 | -7.11 | -0.79 | -21.08 | 336 |
| 61 | Candlestick reversal · 1h | reversion | 65.42 | -34.58 | 460 | 28.9 | -38.15 | -6.78 | -40.71 | 579 |
| 62 | Three white soldiers | momentum | 60.27 | -39.73 | 520 | 15.0 | -49.25 | -22.72 | -49.38 | 654 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -45.62 | -99.03 | 5282 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.76 | -25.98 | -80.30 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -45.73 | -93.62 | 2525 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.30 | -32.25 | -89.48 | 1926 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.08 | -40.76 | -91.29 | 2338 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.42 | -33.25 | -90.54 | 2212 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -54.30 | -97.80 | 3469 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.38 | -59.96 | -96.46 | 3430 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.43 | -32.73 | -93.43 | 2349 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.16 | -34.61 | -83.49 | 1670 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -55.09 | -99.54 | 5974 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.12 | -43.25 | -92.34 | 2614 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.57 | -39.05 | -95.57 | 3474 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -76.43 | -99.80 | 6139 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.94 | -43.71 | -91.98 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.35 | -24.35 | -75.69 | 1613 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -63.57 | -97.72 | 3531 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.59 | -98.84 | 4898 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.44 | -27.06 | -68.93 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -55.22 | -94.76 | 2785 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.71 | -37.17 | -85.18 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -75.79 | -99.64 | 6333 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.36 | -32.13 | -89.37 | 2281 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.78 | -19.61 | -77.94 | 1753 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -36.02 | -90.64 | 2164 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.73 | -52.43 | -96.73 | 3843 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.08 | -57.32 | -89.11 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.64 | -29.07 | -66.40 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.35 | -23.01 | -72.14 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.30 | -18.28 | -78.59 | 1688 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.20 | -49.15 | -97.20 | 4287 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.88 | -99.93 | 8360 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T20:15 | Agent (rotation) | sell | TSLA | 8.14 | -0.04 | selected signal exited |
| 2026-11-11T20:15 | Day trade: Stocks in Play ORB | sell | TSLA | 24.90 | -0.13 | target is flat |
| 2026-11-11T20:15 | Agent (ML meta-label) | sell | TQQQ | 9.48 | -0.03 | selected signal exited |
| 2026-11-11T20:10 | VWAP momentum · 1h | sell | SPY | 5.16 | 0.10 | target is flat |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | TQQQ | 9.50 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | GOOGL | 9.51 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | AMZN | 9.51 | — | following Supertrend |
| 2026-11-11T20:05 | Agent (ML meta-label) | buy | AAPL | 9.51 | — | entry |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | TSLA | 7.15 | -0.02 | rebalance down |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | TECL | 7.11 | -0.10 | rebalance down |
| 2026-11-11T20:05 | Agent (ML meta-label) | sell | AMD | 7.08 | -0.05 | rebalance down |
| 2026-11-11T20:05 | EMA 20/50 cross · 1h | buy | SPY | 3.74 | — | rebalance up |
| 2026-11-11T20:05 | EMA 20/50 cross · 1h | sell | META | 3.74 | -0.01 | rebalance down |
| 2026-11-11T20:00 | Bollinger breakout · 1h | sell | XRP-USD | 7.04 | -0.13 | exit signal |
| 2026-11-11T20:00 | Heikin-Ashi · 1h | buy | BITX | 1.65 | — | entry |
| 2026-11-11T20:00 | Heikin-Ashi · 1h | buy | AMD | 5.04 | — | entry |
| 2026-11-11T20:00 | Heikin-Ashi · 1h | sell | SOL-USD | 6.69 | 0.05 | exit signal |
| 2026-11-11T19:55 | VWAP momentum · 1h | buy | TQQQ | 2.53 | — | entry |
| 2026-11-11T19:55 | VWAP momentum · 1h | buy | TECL | 3.26 | — | entry |
| 2026-11-11T19:55 | VWAP momentum · 1h | sell | UPRO | 5.30 | 0.26 | target is flat |
| 2026-11-11T19:55 | Three white soldiers | sell | SQQQ | 15.16 | 0.13 | exit signal |
| 2026-11-11T19:50 | Agent (ML meta-label) | buy | TSLA | 16.70 | — | entry |
| 2026-11-11T19:50 | Agent (ML meta-label) | sell | TQQQ | 16.68 | -0.04 | selected signal exited |
| 2026-11-11T19:50 | OBV trend · 1h | buy | TSLA | 4.87 | — | rebalance up |
| 2026-11-11T19:50 | OBV trend · 1h | buy | LABU | 4.57 | — | rebalance up |
| 2026-11-11T19:50 | OBV trend · 1h | sell | IWM | 14.40 | 0.15 | target is flat |
| 2026-11-11T19:40 | Agent (ML meta-label) | buy | TQQQ | 16.71 | — | entry |
| 2026-11-11T19:40 | Agent (ML meta-label) | sell | TSLA | 16.69 | -0.02 | selected signal exited |
| 2026-11-11T19:35 | Agent (ML meta-label) | buy | TSLA | 16.71 | — | entry |
| 2026-11-11T19:35 | Agent (ML meta-label) | buy | AMD | 16.71 | — | entry |
| 2026-11-11T19:35 | Agent (ML meta-label) | sell | AMZN | 13.46 | -0.01 | selected signal exited |
| 2026-11-11T19:35 | Agent (ML meta-label) | sell | AAPL | 16.72 | -0.01 | selected signal exited |
| 2026-11-11T19:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 103.89 | -0.08 | target is flat |
| 2026-11-11T19:30 | Agent (ML meta-label) | buy | AAPL | 16.72 | — | entry |
| 2026-11-11T19:30 | Agent (ML meta-label) | sell | TSLA | 16.70 | -0.01 | selected signal exited |
| 2026-11-11T19:30 | Agent (ML meta-label) | sell | AMD | 16.74 | -0.07 | selected signal exited |
| 2026-11-11T19:30 | MFI reversion · 1h | buy | SQQQ | 19.92 | — | entry signal |
| 2026-11-11T19:30 | Stochastic reversion · 1h | buy | SQQQ | 11.75 | — | entry signal |
| 2026-11-11T19:30 | RSI(14) reversion · 1h | buy | SQQQ | 7.01 | — | entry signal |
| 2026-11-11T19:30 | RSI(14) reversion · 1h | sell | ETHU | 3.55 | 0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 20:20:05.000114+00:00 -> 2026-11-11 20:30:05.000114+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
