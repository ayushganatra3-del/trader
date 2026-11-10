# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T23:25:05.000124+00:00 · 55114 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.46 (-12.54%)

Closed trades 172, win rate 35.5%, fees £5.15, max drawdown -13.61%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.49 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 39845 decisions in 3489 calls, $0.4956 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T23:25 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-11-10T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-10T23:25 | 3 / 2 / 0 | ETH-USD 59% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 20.23 | 4.08 | -4.91 | 25 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.79 | 14.79 | 0 | — | 15.13 | 5.04 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.89 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.01 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.31 | 1.31 | 0 | — | 4.26 | 1.25 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.07 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.78 | 1.13 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -4.33 | -1.78 | -9.87 | 155 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.77 | -3.23 | 0 | — | -1.28 | -0.38 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 95.98 | -4.02 | 138 | 46.4 | -12.66 | -3.28 | -13.48 | 154 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.02 | -4.98 | 0 | — | -4.27 | -1.12 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -4.06 | -3.80 | -5.99 | 27 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.78 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 92.92 | -7.08 | 43 | 39.5 | -7.95 | -1.64 | -15.11 | 67 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.65 | -7.35 | 0 | — | -4.02 | -1.06 | -10.64 | 1 |
| 20 | Trend pullback · 1h | trend | 92.58 | -7.42 | 108 | 23.1 | -12.81 | -4.79 | -16.85 | 78 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.01 | -2.77 | -15.49 | 77 |
| 23 | Opening range 30m | breakout | 88.22 | -11.78 | 404 | 33.2 | -15.00 | -4.61 | -15.00 | 604 |
| 24 | Agent | meta | 87.46 | -12.54 | 172 | 35.5 | -13.34 | -6.79 | -14.27 | 203 |
| 25 | Daily: Bullish score | daily | 86.40 | -13.60 | 15 | 20.0 | -4.92 | -0.65 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 86.07 | -13.93 | 1 | 0.0 | -6.29 | -0.83 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.47 | -14.53 | 168 | 26.8 | -13.63 | -2.79 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.97 | -15.03 | 81 | 33.3 | -15.80 | -4.46 | -18.49 | 94 |
| 29 | Donchian 55/20 · 1h | breakout | 84.03 | -15.97 | 71 | 14.1 | -22.52 | -4.79 | -27.94 | 100 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.33 | -17.67 | 2 | 0.0 | -8.31 | -0.94 | -24.16 | 1 |
| 31 | Keltner breakout · 1h | breakout | 81.63 | -18.37 | 110 | 23.6 | -17.44 | -3.57 | -24.55 | 165 |
| 32 | Stochastic reversion · 1h | reversion | 81.19 | -18.81 | 284 | 47.5 | -24.47 | -3.61 | -27.06 | 393 |
| 33 | Connors RSI(2) · 1h | reversion | 80.91 | -19.09 | 207 | 40.1 | -19.42 | -6.50 | -19.98 | 125 |
| 34 | Opening range 15m | breakout | 80.79 | -19.21 | 500 | 31.4 | -20.74 | -5.63 | -20.74 | 733 |
| 35 | Max aggression: 5-day momentum | meta | 80.37 | -19.63 | 18 | 44.4 | -36.21 | -2.30 | -45.81 | 25 |
| 36 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -13.97 | -3.25 | -21.11 | 92 |
| 37 | ADX DI cross · 1h | trend | 79.35 | -20.65 | 185 | 18.9 | -26.12 | -4.57 | -30.45 | 280 |
| 38 | Heikin-Ashi · 1h | trend | 78.95 | -21.05 | 416 | 24.5 | -40.26 | -7.54 | -42.60 | 666 |
| 39 | MFI reversion · 1h | reversion | 77.01 | -22.99 | 365 | 34.5 | -17.99 | -2.32 | -22.84 | 158 |
| 40 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.39 | -4.47 | -27.99 | 235 |
| 41 | CCI reversion · 1h | reversion | 76.80 | -23.20 | 326 | 45.1 | -26.60 | -4.04 | -30.85 | 458 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.26 | -8.88 | -31.64 | 119 |
| 43 | MACD cross · 1h | trend | 74.96 | -25.04 | 360 | 21.9 | -31.60 | -5.19 | -39.47 | 472 |
| 44 | EMA 20/50 cross · 1h | trend | 74.89 | -25.11 | 102 | 10.8 | -26.23 | -4.50 | -36.26 | 117 |
| 45 | Bollinger reversion · 1h | reversion | 74.14 | -25.86 | 278 | 40.3 | -26.27 | -4.03 | -32.30 | 371 |
| 46 | MACD zero-line · 1h | trend | 73.89 | -26.11 | 159 | 16.4 | -25.71 | -5.19 | -31.08 | 213 |
| 47 | Supertrend · 1h | trend | 73.56 | -26.44 | 168 | 13.1 | -29.63 | -5.15 | -36.14 | 227 |
| 48 | RSI momentum · 1h | momentum | 73.39 | -26.61 | 159 | 12.6 | -25.28 | -4.12 | -34.73 | 209 |
| 49 | Triple EMA stack · 1h | trend | 72.23 | -27.77 | 144 | 14.6 | -28.19 | -5.00 | -36.37 | 207 |
| 50 | OBV trend · 1h | momentum | 71.61 | -28.39 | 277 | 18.4 | -28.88 | -5.29 | -35.94 | 283 |
| 51 | Williams %R · 1h | reversion | 71.60 | -28.40 | 346 | 45.7 | -35.30 | -5.59 | -35.97 | 535 |
| 52 | ROC + volume · 1h | momentum | 71.28 | -28.72 | 369 | 27.1 | -35.33 | -6.68 | -38.35 | 379 |
| 53 | Daily: Momentum burst | daily | 71.08 | -28.92 | 27 | 11.1 | -34.82 | -4.91 | -38.23 | 34 |
| 54 | Donchian 20/10 · 1h | breakout | 70.88 | -29.12 | 142 | 19.7 | -30.75 | -5.77 | -35.64 | 204 |
| 55 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -25.91 | -3.78 | -28.98 | 234 |
| 56 | Max aggression: 1-day momentum | meta | 68.35 | -31.65 | 27 | 25.9 | -29.50 | -1.43 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.58 | -33.42 | 170 | 30.6 | -31.74 | -4.93 | -33.96 | 234 |
| 58 | VWAP momentum · 1h | momentum | 65.88 | -34.12 | 841 | 21.9 | -53.83 | -11.54 | -55.02 | 1225 |
| 59 | EMA 9/21 cross · 1h | trend | 65.57 | -34.43 | 252 | 9.9 | -37.31 | -7.54 | -41.74 | 336 |
| 60 | Agent (ML meta-label) | meta | 65.50 | -34.50 | 1700 | 24.5 | -6.04 | -0.82 | -18.03 | 319 |
| 61 | Candlestick reversal · 1h | reversion | 63.92 | -36.08 | 447 | 28.0 | -38.58 | -7.26 | -40.19 | 589 |
| 62 | Three white soldiers | momentum | 60.50 | -39.50 | 511 | 14.7 | -49.11 | -22.91 | -49.11 | 652 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -46.08 | -98.95 | 5263 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.43 | -26.36 | -79.45 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.29 | -47.35 | -93.29 | 2519 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -32.35 | -89.25 | 1921 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.80 | -40.33 | -90.80 | 2329 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.22 | -32.64 | -90.33 | 2217 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -55.12 | -97.75 | 3462 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -58.79 | -96.20 | 3436 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -33.71 | -93.66 | 2368 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -34.71 | -82.31 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -55.29 | -99.54 | 5968 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.13 | -43.82 | -92.15 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.50 | -37.72 | -95.56 | 3431 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -77.51 | -99.80 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -44.09 | -92.02 | 2274 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.35 | -24.93 | -75.35 | 1608 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -63.75 | -97.73 | 3534 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.85 | -63.67 | -98.85 | 4897 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.78 | -69.09 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.57 | -94.58 | 2782 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.55 | -37.78 | -84.61 | 1776 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.44 | -99.65 | 6346 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.67 | -32.64 | -89.82 | 2291 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.02 | -20.07 | -78.32 | 1745 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -36.74 | -90.74 | 2204 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.78 | -52.72 | -96.79 | 3855 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -58.99 | -89.35 | 2155 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.52 | -28.22 | -66.19 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.25 | -22.95 | -71.37 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.70 | -19.40 | -79.94 | 1688 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.23 | -49.82 | -97.24 | 4290 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -117.20 | -99.93 | 8323 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T23:00 | Candlestick reversal · 1h | buy | DOGE-USD | 4.03 | — | rebalance up |
| 2026-11-10T23:00 | Candlestick reversal · 1h | sell | BTC-USD | 9.07 | -0.02 | exit signal |
| 2026-11-10T23:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 19.75 | — | entry signal |
| 2026-11-10T23:00 | Three white soldiers | sell | DOGE-USD | 15.03 | -0.13 | target is flat |
| 2026-11-10T22:55 | Three white soldiers | buy | DOGE-USD | 15.16 | — | entry signal |
| 2026-11-10T22:00 | CCI reversion · 1h | buy | BTC-USD | 4.33 | — | entry |
| 2026-11-10T22:00 | CCI reversion · 1h | sell | ETH-USD | 4.33 | -0.00 | rebalance down |
| 2026-11-10T21:00 | MFI reversion · 1h | buy | XRP-USD | 5.16 | — | rebalance up |
| 2026-11-10T21:00 | MFI reversion · 1h | buy | DOGE-USD | 5.13 | — | rebalance up |
| 2026-11-10T20:55 | Agent (aggressive) | sell | SQQQ | 42.23 | -0.26 | selected signal exited |
| 2026-11-10T20:55 | Agent (aggressive) | sell | COIN | 42.74 | 0.25 | selected signal exited |
| 2026-11-10T20:55 | Agent | sell | SQQQ | 17.39 | -0.11 | selected signal exited |
| 2026-11-10T20:55 | Agent | sell | COIN | 17.60 | 0.10 | selected signal exited |
| 2026-11-10T20:55 | MFI reversion · 1h | sell | UPRO | 7.69 | 0.03 | target is flat |
| 2026-11-10T20:55 | MFI reversion · 1h | sell | META | 7.68 | -0.03 | target is flat |
| 2026-11-10T20:51 | VWAP momentum · 1h | sell | TECL | 5.05 | -0.01 | target is flat |
| 2026-11-10T20:35 | Agent (ML meta-label) | buy | TSLA | 6.50 | — | following Ichimoku |
| 2026-11-10T20:35 | Agent (ML meta-label) | buy | META | 10.92 | — | entry |
| 2026-11-10T20:35 | Agent (ML meta-label) | sell | SPY | 5.46 | -0.00 | rebalance down |
| 2026-11-10T20:35 | Agent (ML meta-label) | sell | AMZN | 5.48 | -0.00 | rebalance down |
| 2026-11-10T20:30 | Agent (ML meta-label) | buy | AMZN | 3.29 | — | rebalance up |
| 2026-11-10T20:30 | Agent (ML meta-label) | sell | TSLA | 9.78 | -0.01 | selected signal exited |
| 2026-11-10T20:30 | Agent (aggressive) | buy | SQQQ | 42.49 | — | following Stochastic reversion |
| 2026-11-10T20:30 | Agent | buy | SQQQ | 17.49 | — | following Stochastic reversion |
| 2026-11-10T20:30 | MFI reversion · 1h | buy | UPRO | 7.66 | — | entry |
| 2026-11-10T20:30 | MFI reversion · 1h | buy | TQQQ | 7.71 | — | entry |
| 2026-11-10T20:30 | MFI reversion · 1h | buy | SOXL | 7.71 | — | entry signal |
| 2026-11-10T20:30 | MFI reversion · 1h | buy | META | 7.71 | — | entry |
| 2026-11-10T20:30 | MFI reversion · 1h | buy | BITX | 7.71 | — | entry |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | XRP-USD | 4.94 | -0.08 | rebalance down |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | TECL | 5.31 | 0.10 | rebalance down |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | SPY | 5.14 | 0.01 | rebalance down |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | NVDA | 12.88 | 0.12 | target is flat |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | DOGE-USD | 5.09 | -0.02 | rebalance down |
| 2026-11-10T20:30 | MFI reversion · 1h | sell | AAPL | 5.13 | -0.01 | rebalance down |
| 2026-11-10T20:30 | CCI reversion · 1h | buy | ETHU | 9.92 | — | entry signal |
| 2026-11-10T20:30 | CCI reversion · 1h | buy | BITX | 10.97 | — | entry signal |
| 2026-11-10T20:30 | CCI reversion · 1h | sell | XRP-USD | 7.64 | -0.12 | rebalance down |
| 2026-11-10T20:30 | CCI reversion · 1h | sell | SQQQ | 4.27 | 0.05 | rebalance down |
| 2026-11-10T20:30 | CCI reversion · 1h | sell | NVDA | 4.53 | 0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 23:25:05.000124+00:00 -> 2026-11-10 23:35:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
