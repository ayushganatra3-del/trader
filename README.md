# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T00:55:05.000123+00:00 · 47815 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 735 decisions in 147 calls, $0.0103 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T00:55 | 1 / 1 / 3 | cash |  |
| Breezy | 2026-11-05T00:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T00:55 | 2 / 3 / 0 | SOL-USD 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.04 | 13.04 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.70 | 0.70 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.44 | -2.99 | -13.17 | 139 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.18 | -0.82 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.06 | -1.94 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.86 | 2.71 | -3.27 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.38 | -4.62 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.94 | -5.06 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Hold BTC | benchmark | 94.73 | -5.27 | 0 | — | -0.78 | 0.04 | -13.22 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.40 | -0.40 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Max aggression: 5-day momentum | meta | 91.31 | -8.69 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.82 | -9.18 | 103 | 22.3 | -16.33 | -6.04 | -17.67 | 78 |
| 23 | Parabolic SAR · 1h | trend | 90.02 | -9.98 | 155 | 27.1 | -15.25 | -3.38 | -19.35 | 246 |
| 24 | Copy: Insider buying | copy | 89.61 | -10.39 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.20 | -3.54 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.04 | -12.96 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.91 | -13.09 | 62 | 12.9 | -12.92 | -2.74 | -19.91 | 105 |
| 30 | Stochastic reversion · 1h | reversion | 86.88 | -13.12 | 249 | 47.8 | -20.45 | -3.86 | -24.97 | 383 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.17 | -13.83 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.18 | -14.82 | 155 | 18.1 | -18.21 | -3.26 | -22.68 | 278 |
| 34 | Volume breakout · 1h | breakout | 84.59 | -15.41 | 132 | 28.8 | -14.12 | -3.23 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.45 | -15.55 | 324 | 34.3 | -14.09 | -2.15 | -18.47 | 154 |
| 36 | Keltner breakout · 1h | breakout | 83.74 | -16.26 | 94 | 24.5 | -19.92 | -4.07 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.38 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.14 | -17.86 | 85 | 12.9 | -20.31 | -4.29 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.46 | -18.54 | 148 | 25.0 | -18.06 | -3.67 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.99 | -19.01 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.56 | -20.44 | 92 | 10.9 | -18.46 | -3.24 | -27.87 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 78.86 | -21.14 | 375 | 22.7 | -40.49 | -8.45 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.54 | -21.46 | 141 | 15.6 | -25.06 | -5.17 | -29.62 | 222 |
| 45 | MACD cross · 1h | trend | 78.18 | -21.82 | 310 | 22.9 | -30.60 | -5.96 | -33.62 | 475 |
| 46 | Z-score reversion · 1h | reversion | 78.04 | -21.96 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.95 | -22.05 | 147 | 12.9 | -29.34 | -5.29 | -32.06 | 232 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.95 | -23.05 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.70 | -23.30 | 290 | 47.6 | -33.15 | -5.96 | -34.67 | 525 |
| 51 | RSI momentum · 1h | momentum | 76.56 | -23.44 | 142 | 12.0 | -28.74 | -5.52 | -30.70 | 228 |
| 52 | Triple EMA stack · 1h | trend | 76.04 | -23.96 | 131 | 13.7 | -27.92 | -5.50 | -31.75 | 213 |
| 53 | OBV trend · 1h | momentum | 75.45 | -24.55 | 248 | 17.3 | -29.67 | -6.47 | -30.91 | 294 |
| 54 | Donchian 20/10 · 1h | breakout | 74.44 | -25.56 | 124 | 19.4 | -27.70 | -5.04 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.23 | -25.77 | 321 | 25.5 | -33.20 | -6.41 | -36.19 | 387 |
| 56 | RSI(14) reversion · 1h | reversion | 72.23 | -27.77 | 136 | 28.7 | -20.47 | -3.39 | -26.28 | 217 |
| 57 | EMA 9/21 cross · 1h | trend | 69.65 | -30.35 | 225 | 9.8 | -36.60 | -7.34 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.54 | -30.46 | 729 | 22.2 | -53.71 | -11.18 | -55.84 | 1223 |
| 59 | Agent (ML meta-label) | meta | 69.32 | -30.68 | 1443 | 22.3 | -9.80 | -1.92 | -19.15 | 290 |
| 60 | Candlestick reversal · 1h | reversion | 69.23 | -30.77 | 376 | 30.1 | -35.41 | -6.60 | -37.86 | 555 |
| 61 | Three white soldiers | momentum | 68.07 | -31.93 | 439 | 16.4 | -47.00 | -21.72 | -47.18 | 634 |
| 62 | Max aggression: 1-day momentum | meta | 66.64 | -33.36 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.10 | -98.93 | 5164 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.30 | -25.24 | -80.30 | 1425 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -45.79 | -93.53 | 2519 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.83 | -30.88 | -88.96 | 1898 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.82 | -38.10 | -90.88 | 2306 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.36 | -31.78 | -90.37 | 2220 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -51.39 | -97.71 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -57.14 | -96.22 | 3389 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -33.63 | -93.70 | 2469 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -36.50 | -82.16 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.33 | -99.48 | 5873 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.88 | -42.36 | -92.91 | 2603 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.68 | -36.66 | -95.68 | 3422 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -70.27 | -99.79 | 6160 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -42.39 | -91.73 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.10 | -26.46 | -75.10 | 1564 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -60.28 | -97.74 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -59.47 | -98.69 | 4829 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.73 | -28.53 | -70.47 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.70 | -52.37 | -94.75 | 2760 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -36.19 | -84.62 | 1785 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -67.91 | -99.62 | 6305 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.27 | -30.28 | -88.44 | 2239 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.48 | -18.94 | -76.94 | 1703 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.66 | -36.41 | -90.66 | 2230 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -49.04 | -96.45 | 3826 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.19 | -51.20 | -89.20 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.28 | -27.27 | -65.55 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.80 | -25.29 | -73.81 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.47 | -18.22 | -77.27 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.92 | -50.01 | -96.92 | 4248 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -91.99 | -99.93 | 8230 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T00:55 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:45 | Agent (ML meta-label) | sell | ETH-USD | 4.93 | -0.02 | selected signal exited |
| 2026-11-04T23:40 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:05 | Three white soldiers | sell | SOL-USD | 17.05 | -0.03 | exit signal |
| 2026-11-04T23:05 | Three white soldiers | sell | ETH-USD | 16.99 | -0.10 | exit signal |
| 2026-11-04T23:00 | VWAP momentum · 1h | buy | SOL-USD | 3.06 | — | entry signal |
| 2026-11-04T22:55 | Three white soldiers | sell | BTC-USD | 16.97 | -0.14 | stop-loss |
| 2026-11-04T22:45 | Three white soldiers | buy | BTC-USD | 17.11 | — | entry signal |
| 2026-11-04T22:20 | EMA 20/50 cross · 1h | sell | XRP-USD | 3.96 | 0.12 | rebalance down |
| 2026-11-04T22:20 | Three white soldiers | buy | SOL-USD | 17.09 | — | entry signal |
| 2026-11-04T22:20 | Three white soldiers | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-11-04T21:15 | Agent (ML meta-label) | sell | ETH-USD | 5.31 | -0.02 | selected signal exited |
| 2026-11-04T21:05 | Agent (ML meta-label) | buy | ETH-USD | 5.33 | — | entry |
| 2026-11-04T21:00 | Parabolic SAR · 1h | sell | XRP-USD | 8.92 | 0.10 | exit signal |
| 2026-11-04T20:55 | Agent (rotation) | sell | UPRO | 3.12 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TSLA | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | TQQQ | 31.06 | -0.34 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | SPY | 3.14 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSTR | 3.18 | 0.02 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | MSFT | 3.17 | 0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | GOOGL | 3.11 | -0.04 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | COIN | 2.44 | 0.00 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | BITX | 3.15 | -0.01 | selected signal exited |
| 2026-11-04T20:55 | Agent (rotation) | sell | AAPL | 3.13 | -0.03 | selected signal exited |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | MSFT | 24.25 | 0.19 | target is flat |
| 2026-11-04T20:55 | Day trade: Stocks in Play ORB | sell | GOOGL | 23.88 | -0.21 | target is flat |
| 2026-11-04T20:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 105.47 | -1.14 | target is flat |
| 2026-11-04T20:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | TQQQ | 95.46 | -0.80 | target is flat |
| 2026-11-04T20:55 | Agent (aggressive) | sell | BITX | 42.49 | -0.26 | selected signal exited |
| 2026-11-04T20:55 | Agent | sell | BITX | 17.81 | -0.11 | selected signal exited |
| 2026-11-04T20:55 | Opening range 30m | sell | UPRO | 9.86 | -0.07 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | TSLA | 8.96 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | SPY | 8.95 | -0.03 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSTR | 9.03 | 0.05 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | MSFT | 9.01 | 0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | GOOGL | 8.87 | -0.11 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | COIN | 12.79 | 0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | BITX | 8.96 | -0.02 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 30m | sell | AAPL | 8.89 | -0.09 | end-of-day flatten |
| 2026-11-04T20:55 | Opening range 15m | sell | UPRO | 7.48 | -0.07 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 00:55:05.000123+00:00 -> 2026-11-05 01:05:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 00:55:05.000123+00:00 -> 2026-11-05 01:05:05.000123+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 00:55:05.000123+00:00 -> 2026-11-05 01:05:05.000123+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
