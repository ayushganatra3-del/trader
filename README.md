# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-31T00:55:05.000184+00:00 · 41946 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-30 | MSM 12%, LRN 12%, SRRK 12%, BPRE 12%, RENT 12%, ACN 12%, SCQCU 12%, FBK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.7, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 675 decisions in 135 calls, $0.0094 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-31T00:55 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-31T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-31T00:55 | 3 / 2 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.83 | +1.03% | 6 |
| Candlestick reversal | LABU | 2.63 | +8.02% | 17 |
| Connors RSI(2) | SOXL | 2.47 | +5.40% | 16 |
| Stochastic reversion | ETHU | 2.47 | +6.74% | 16 |
| Connors RSI(2) | SQQQ | 2.21 | +2.50% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.51 | 6.51 | 0 | — | 7.73 | 3.81 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 4.88 | 1.60 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 8.04 | 2.65 | -4.92 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.34 | 0.34 | 25 | 28.0 | 7.20 | 1.87 | -5.89 | 44 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.94 | -0.06 | 95 | 45.3 | -12.25 | -3.43 | -12.61 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.86 | -0.14 | 0 | — | 3.11 | 1.36 | -5.02 | 1 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.65 | -2.35 | 97 | 36.1 | 6.23 | 2.94 | -2.46 | 95 |
| 10 | Hold SPY | benchmark | 97.19 | -2.81 | 0 | — | -1.35 | -0.67 | -3.94 | 1 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.68 | -2.49 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.54 | 0.67 | -7.93 | 8 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.61 | -6.20 | 21 |
| 14 | Agent (rotation) | meta | 94.97 | -5.03 | 129 | 31.0 | -4.42 | -3.16 | -8.60 | 144 |
| 15 | Three white soldiers · 1h | momentum | 94.90 | -5.09 | 17 | 11.8 | -2.52 | -2.32 | -4.94 | 27 |
| 16 | Gap and go | momentum | 94.85 | -5.15 | 124 | 29.0 | 4.44 | 1.48 | -8.76 | 203 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.65 | -5.35 | 0 | — | -7.15 | -2.76 | -8.12 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.06 | -5.94 | 0 | — | -3.56 | -1.32 | -7.64 | 1 |
| 19 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -8.87 | -5.40 | -12.21 | 219 |
| 20 | Parabolic SAR · 1h | trend | 91.49 | -8.51 | 140 | 28.6 | -18.26 | -4.16 | -20.29 | 251 |
| 21 | Hold BTC | benchmark | 91.40 | -8.60 | 0 | — | -1.26 | 0.10 | -12.65 | 1 |
| 22 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -20.58 | -7.54 | -20.58 | 96 |
| 23 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.54 | -2.64 | -16.91 | 1 |
| 24 | Opening range 30m | breakout | 90.72 | -9.29 | 315 | 34.9 | -12.27 | -3.68 | -17.21 | 591 |
| 25 | Squeeze breakout · 1h | breakout | 90.25 | -9.76 | 58 | 24.1 | -6.03 | -1.66 | -12.70 | 88 |
| 26 | Copy: Insider buying | copy | 89.48 | -10.52 | 34 | 35.3 | -23.46 | -4.82 | -23.91 | 69 |
| 27 | Donchian 55/20 · 1h | breakout | 89.34 | -10.66 | 57 | 14.0 | -16.81 | -3.73 | -17.83 | 103 |
| 28 | Daily: Bullish score | daily | 88.57 | -11.43 | 14 | 21.4 | -6.72 | -0.84 | -14.73 | 14 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.72 | -12.28 | 1 | 0.0 | -3.89 | -0.44 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.15 | -3.71 | -15.04 | 98 |
| 31 | Volume breakout · 1h | breakout | 85.93 | -14.07 | 127 | 29.1 | -14.35 | -3.08 | -17.96 | 104 |
| 32 | Stochastic reversion · 1h | reversion | 85.52 | -14.48 | 221 | 47.5 | -17.83 | -3.08 | -24.77 | 395 |
| 33 | ADX DI cross · 1h | trend | 85.09 | -14.91 | 141 | 19.1 | -17.42 | -3.40 | -20.33 | 263 |
| 34 | Keltner breakout · 1h | breakout | 85.09 | -14.91 | 86 | 24.4 | -23.75 | -4.70 | -25.77 | 184 |
| 35 | Bollinger breakout · 1h | breakout | 83.42 | -16.58 | 132 | 26.5 | -15.87 | -2.94 | -21.61 | 240 |
| 36 | Connors RSI(2) · 1h | reversion | 83.39 | -16.61 | 188 | 40.4 | -21.38 | -6.88 | -22.05 | 161 |
| 37 | Opening range 15m | breakout | 83.02 | -16.98 | 390 | 31.5 | -17.35 | -4.98 | -19.32 | 723 |
| 38 | Daily: Momentum burst | daily | 82.42 | -17.58 | 19 | 15.8 | -24.65 | -3.47 | -30.47 | 35 |
| 39 | MFI reversion · 1h | reversion | 82.37 | -17.63 | 295 | 31.9 | -19.68 | -3.17 | -22.47 | 154 |
| 40 | Max aggression: 5-day momentum | meta | 82.08 | -17.92 | 15 | 40.0 | -35.31 | -2.61 | -37.35 | 25 |
| 41 | Ichimoku · 1h | trend | 82.08 | -17.92 | 79 | 13.9 | -20.76 | -4.17 | -24.80 | 118 |
| 42 | CCI reversion · 1h | reversion | 80.53 | -19.47 | 248 | 46.0 | -25.88 | -4.02 | -28.85 | 451 |
| 43 | Supertrend · 1h | trend | 80.36 | -19.64 | 137 | 13.1 | -26.47 | -4.89 | -29.25 | 216 |
| 44 | EMA 20/50 cross · 1h | trend | 80.09 | -19.91 | 88 | 11.4 | -22.94 | -4.34 | -26.95 | 135 |
| 45 | MACD cross · 1h | trend | 79.72 | -20.28 | 283 | 24.0 | -28.74 | -5.12 | -32.85 | 469 |
| 46 | Williams %R · 1h | reversion | 79.53 | -20.47 | 253 | 47.0 | -34.80 | -6.07 | -36.14 | 528 |
| 47 | RSI momentum · 1h | momentum | 79.11 | -20.89 | 130 | 13.1 | -26.63 | -4.83 | -30.14 | 214 |
| 48 | MACD zero-line · 1h | trend | 78.90 | -21.10 | 130 | 16.2 | -24.16 | -4.88 | -27.15 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 78.78 | -21.22 | 333 | 23.7 | -41.48 | -8.96 | -41.96 | 667 |
| 50 | Z-score reversion · 1h | reversion | 78.59 | -21.41 | 131 | 34.4 | -17.59 | -2.74 | -22.55 | 213 |
| 51 | Bollinger reversion · 1h | reversion | 78.10 | -21.90 | 198 | 37.9 | -31.07 | -6.54 | -33.02 | 381 |
| 52 | Triple EMA stack · 1h | trend | 78.04 | -21.96 | 120 | 15.0 | -30.81 | -5.76 | -33.28 | 208 |
| 53 | OBV trend · 1h | momentum | 77.91 | -22.09 | 232 | 17.7 | -32.92 | -6.70 | -35.72 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 76.05 | -23.95 | 116 | 20.7 | -26.43 | -4.64 | -29.81 | 215 |
| 55 | ROC + volume · 1h | momentum | 75.63 | -24.37 | 293 | 25.6 | -30.03 | -5.21 | -32.80 | 382 |
| 56 | VWAP momentum · 1h | momentum | 73.74 | -26.26 | 643 | 22.7 | -51.30 | -10.88 | -51.83 | 1232 |
| 57 | Three white soldiers | momentum | 73.58 | -26.42 | 375 | 17.3 | -44.77 | -20.64 | -44.77 | 620 |
| 58 | Max aggression: 1-day momentum | meta | 73.37 | -26.62 | 21 | 33.3 | -28.37 | -1.52 | -50.32 | 42 |
| 59 | RSI(14) reversion · 1h | reversion | 73.25 | -26.75 | 118 | 26.3 | -19.90 | -3.48 | -26.17 | 197 |
| 60 | Candlestick reversal · 1h | reversion | 72.04 | -27.96 | 320 | 28.4 | -36.41 | -6.99 | -37.03 | 559 |
| 61 | Agent (ML meta-label) | meta | 71.72 | -28.28 | 1176 | 21.0 | -19.91 | -3.89 | -21.90 | 361 |
| 62 | EMA 9/21 cross · 1h | trend | 71.17 | -28.83 | 205 | 10.2 | -35.10 | -6.67 | -36.61 | 333 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -43.29 | -98.87 | 5241 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.18 | -23.33 | -79.40 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -43.62 | -93.55 | 2536 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.57 | -30.01 | -88.79 | 1934 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.99 | -36.79 | -91.07 | 2345 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.01 | -30.78 | -90.02 | 2218 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.46 | -97.73 | 3525 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.12 | -55.83 | -96.14 | 3396 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.91 | -35.91 | -93.91 | 2465 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.77 | -32.90 | -81.89 | 1686 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -52.52 | -99.48 | 5926 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.84 | -42.24 | -92.91 | 2637 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -36.92 | -95.39 | 3445 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -72.46 | -99.78 | 6251 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.90 | -43.54 | -91.90 | 2310 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.76 | -27.38 | -75.76 | 1587 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -59.51 | -97.64 | 3572 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.96 | -98.68 | 4861 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.98 | -27.74 | -69.29 | 1216 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -52.04 | -94.73 | 2802 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.62 | -36.98 | -84.74 | 1821 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -65.26 | -99.61 | 6375 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.22 | -29.65 | -88.35 | 2254 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.78 | -19.41 | -78.09 | 1744 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.75 | -36.99 | -90.88 | 2278 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.38 | -48.55 | -96.40 | 3842 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.82 | -50.62 | -89.99 | 2160 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.72 | -25.55 | -64.76 | 825 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.83 | -25.07 | -73.98 | 1282 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.23 | -18.29 | -76.75 | 1593 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.70 | -96.79 | 4262 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.33 | -99.92 | 8350 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-31T00:55 | Three white soldiers | sell | XRP-USD | 18.42 | -0.05 | exit signal |
| 2026-10-31T00:50 | Three white soldiers | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-10-31T00:47 | Agent (ML meta-label) | sell | SOL-USD | 10.23 | -0.04 | selected signal exited |
| 2026-10-31T00:47 | Agent (ML meta-label) | sell | ETH-USD | 10.20 | -0.06 | selected signal exited |
| 2026-10-31T00:45 | Agent (ML meta-label) | buy | ETH-USD | 10.26 | — | entry |
| 2026-10-31T00:45 | Agent (ML meta-label) | sell | SOL-USD | 7.68 | -0.03 | rebalance down |
| 2026-10-31T00:45 | Three white soldiers | buy | BTC-USD | 18.44 | — | entry signal |
| 2026-10-31T00:30 | Three white soldiers | sell | SOL-USD | 18.37 | -0.10 | exit signal |
| 2026-10-31T00:30 | Three white soldiers | sell | BTC-USD | 18.47 | -0.03 | exit signal |
| 2026-10-31T00:26 | Agent (ML meta-label) | buy | SOL-USD | 7.69 | — | rebalance up |
| 2026-10-31T00:26 | Agent (ML meta-label) | sell | ETH-USD | 10.22 | -0.05 | selected signal exited |
| 2026-10-31T00:05 | Agent (ML meta-label) | buy | ETH-USD | 10.27 | — | entry |
| 2026-10-31T00:05 | Agent (ML meta-label) | sell | SOL-USD | 4.07 | -0.02 | rebalance down |
| 2026-10-31T00:00 | Agent (ML meta-label) | buy | SOL-USD | 14.39 | — | entry |
| 2026-10-31T00:00 | Z-score reversion · 1h | buy | XRP-USD | 9.83 | — | entry |
| 2026-10-31T00:00 | Z-score reversion · 1h | buy | ETH-USD | 9.83 | — | entry |
| 2026-10-31T00:00 | Z-score reversion · 1h | buy | DOGE-USD | 9.83 | — | entry |
| 2026-10-31T00:00 | Bollinger reversion · 1h | sell | SOL-USD | 4.14 | 0.00 | exit signal |
| 2026-10-31T00:00 | RSI(14) reversion · 1h | buy | XRP-USD | 7.33 | — | entry |
| 2026-10-31T00:00 | RSI(14) reversion · 1h | buy | SOL-USD | 7.33 | — | entry |
| 2026-10-31T00:00 | RSI(14) reversion · 1h | buy | ETH-USD | 7.33 | — | entry |
| 2026-10-31T00:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 7.33 | — | entry |
| 2026-10-31T00:00 | RSI(14) reversion · 1h | buy | BTC-USD | 7.33 | — | entry |
| 2026-10-31T00:00 | Candlestick reversal · 1h | buy | XRP-USD | 6.00 | — | entry |
| 2026-10-31T00:00 | Candlestick reversal · 1h | buy | SOL-USD | 6.00 | — | entry |
| 2026-10-31T00:00 | Candlestick reversal · 1h | buy | ETH-USD | 6.00 | — | entry signal |
| 2026-10-31T00:00 | Candlestick reversal · 1h | buy | DOGE-USD | 6.00 | — | entry |
| 2026-10-30T23:35 | Three white soldiers | buy | XRP-USD | 18.47 | — | entry signal |
| 2026-10-30T23:35 | Three white soldiers | buy | SOL-USD | 18.47 | — | entry signal |
| 2026-10-30T23:20 | Three white soldiers | sell | SOL-USD | 18.37 | -0.13 | exit signal |
| 2026-10-30T23:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.04 | — | entry signal |
| 2026-10-30T23:00 | VWAP momentum · 1h | sell | ETH-USD | 6.04 | -0.02 | rebalance down |
| 2026-10-30T22:35 | Three white soldiers | buy | SOL-USD | 18.50 | — | entry signal |
| 2026-10-30T22:35 | Three white soldiers | buy | BTC-USD | 18.50 | — | entry signal |
| 2026-10-30T22:00 | Heikin-Ashi · 1h | buy | XRP-USD | 19.62 | — | entry signal |
| 2026-10-30T22:00 | Heikin-Ashi · 1h | buy | SOL-USD | 19.62 | — | entry signal |
| 2026-10-30T21:00 | CCI reversion · 1h | buy | SOL-USD | 2.51 | — | entry |
| 2026-10-30T21:00 | CCI reversion · 1h | buy | BTC-USD | 11.46 | — | entry signal |
| 2026-10-30T21:00 | CCI reversion · 1h | sell | XRP-USD | 4.63 | -0.01 | rebalance down |
| 2026-10-30T21:00 | CCI reversion · 1h | sell | ETH-USD | 4.66 | 0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-02 00:55:05.000184+00:00 -> 2026-10-31 01:05:05.000184+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
