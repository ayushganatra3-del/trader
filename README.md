# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-24T11:40:05.000162+00:00 · 34211 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 8976 decisions in 1797 calls, $0.1257 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-24T11:40 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-24T11:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-24T11:40 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |
| RSI(14) reversion | TSLA | 1.70 | +3.99% | 7 |
| Opening range 30m | PLTR | 1.69 | +3.38% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.17 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.19 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.97 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.03 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.61 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -11.85 | -3.28 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 4.88 | 2.37 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.37 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.20 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.34 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.86 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.03 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.28 | -4.72 | 0 | — | 0.21 | 0.21 | -8.68 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.74 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.16 | -5.84 | 25 | 40.0 | -16.19 | -3.12 | -21.83 | 67 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.58 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -7.01 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.53 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.45 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.37 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.89 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.38 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.83 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.37 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.23 | -8.77 | 108 | 18.5 | -11.79 | -2.40 | -14.69 | 256 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.04 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -12.82 | -2.71 | -16.01 | 113 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.54 | -7.77 | -12.26 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.77 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 89.03 | -10.97 | 105 | 27.6 | -12.06 | -2.37 | -16.41 | 240 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.26 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.56 | -3.88 | -22.47 | 389 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.76 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.50 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.67 | -17.87 | 703 |
| 40 | Supertrend · 1h | trend | 85.63 | -14.37 | 109 | 14.7 | -24.13 | -5.06 | -26.68 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.62 | -14.38 | 101 | 15.8 | -21.39 | -4.55 | -23.32 | 215 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.99 | -26.96 | 196 |
| 43 | MACD cross · 1h | trend | 84.49 | -15.51 | 221 | 23.1 | -23.36 | -4.66 | -26.51 | 454 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.79 | -25.24 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.56 | -16.44 | 106 | 34.0 | -15.41 | -2.61 | -21.48 | 201 |
| 46 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.18 | -28.32 | 211 |
| 47 | MFI reversion · 1h | reversion | 81.75 | -18.25 | 258 | 31.8 | -17.57 | -2.83 | -20.54 | 145 |
| 48 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.70 | -4.53 | -25.14 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 81.26 | -18.73 | 97 | 19.6 | -24.19 | -4.66 | -27.15 | 216 |
| 50 | Three white soldiers | momentum | 81.10 | -18.90 | 276 | 19.9 | -43.56 | -20.34 | -43.68 | 587 |
| 51 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.66 | -6.94 | -33.18 | 306 |
| 52 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -35.97 | -6.42 | -36.69 | 530 |
| 53 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.72 | -6.63 | -32.19 | 367 |
| 54 | CCI reversion · 1h | reversion | 79.85 | -20.15 | 200 | 42.5 | -26.90 | -4.04 | -28.17 | 456 |
| 55 | Agent (ML meta-label) | meta | 79.50 | -20.50 | 858 | 18.6 | -15.03 | -2.90 | -16.34 | 384 |
| 56 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 271 | 22.9 | -43.24 | -10.07 | -43.93 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.20 | -6.01 | -31.38 | 379 |
| 58 | RSI(14) reversion · 1h | reversion | 77.06 | -22.94 | 93 | 22.6 | -16.02 | -2.97 | -23.70 | 189 |
| 59 | EMA 9/21 cross · 1h | trend | 77.02 | -22.98 | 161 | 11.8 | -30.34 | -6.19 | -33.63 | 318 |
| 60 | Candlestick reversal · 1h | reversion | 77.00 | -23.00 | 257 | 28.4 | -35.48 | -6.72 | -36.26 | 545 |
| 61 | VWAP momentum · 1h | momentum | 75.45 | -24.55 | 528 | 21.0 | -50.99 | -11.77 | -51.13 | 1222 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.95 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.53 | -42.48 | 707 | 22.6 | -74.97 | -27.03 | -74.98 | 1548 |
| 64 | Volume breakout | breakout | 56.85 | -43.16 | 420 | 13.1 | -61.21 | -25.88 | -61.21 | 766 |
| 65 | Squeeze breakout | breakout | 53.36 | -46.64 | 552 | 14.1 | -66.65 | -28.58 | -66.71 | 1150 |
| 66 | Donchian 55/20 | breakout | 53.11 | -46.89 | 565 | 19.1 | -71.48 | -23.15 | -71.62 | 1249 |
| 67 | RSI(14) reversion | reversion | 51.96 | -48.04 | 842 | 26.0 | -77.01 | -19.91 | -77.16 | 1683 |
| 68 | EMA 20/50 cross | trend | 51.68 | -48.32 | 624 | 20.0 | -78.94 | -23.60 | -79.23 | 1410 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -44.57 | -98.71 | 5035 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.83 | -45.92 | -93.87 | 2514 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.73 | -30.57 | -88.84 | 1886 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -38.47 | -91.36 | 2312 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -30.49 | -90.36 | 2147 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -54.76 | -97.80 | 3486 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.05 | -59.32 | -96.06 | 3331 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.66 | -34.19 | -93.71 | 2419 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.76 | -35.49 | -82.80 | 1683 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -55.96 | -99.39 | 5741 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.37 | -42.24 | -92.42 | 2584 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -38.80 | -95.29 | 3350 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -80.32 | -99.76 | 6118 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.21 | -45.68 | -92.22 | 2325 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -61.29 | -97.53 | 3519 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -60.46 | -98.55 | 4747 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.35 | -58.64 | -94.37 | 2743 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.68 | -38.36 | -83.74 | 1768 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.56 | -67.22 | -99.56 | 6202 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.03 | -29.37 | -88.06 | 2209 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.43 | -38.18 | -90.49 | 2250 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.06 | -48.34 | -96.07 | 3771 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.66 | -51.05 | -89.75 | 2097 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.19 | -17.78 | -75.40 | 1561 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.25 | -49.45 | -96.29 | 4149 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -102.38 | -99.91 | 8157 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-24T11:00 | RSI(14) reversion · 1h | buy | SOL-USD | 5.29 | — | entry signal |
| 2026-10-24T11:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 8.57 | — | entry signal |
| 2026-10-24T10:35 | RSI(14) reversion | sell | XRP-USD | 12.99 | -0.01 | exit signal |
| 2026-10-24T10:35 | RSI(14) reversion | sell | SOL-USD | 12.97 | -0.03 | exit signal |
| 2026-10-24T10:35 | RSI(14) reversion | sell | ETH-USD | 13.01 | -0.03 | exit signal |
| 2026-10-24T10:35 | RSI(14) reversion | sell | DOGE-USD | 12.98 | -0.02 | exit signal |
| 2026-10-24T10:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.91 | — | entry signal |
| 2026-10-24T09:55 | RSI(14) reversion | buy | SOL-USD | 13.00 | — | entry signal |
| 2026-10-24T09:55 | RSI(14) reversion | buy | DOGE-USD | 13.00 | — | entry signal |
| 2026-10-24T09:50 | RSI(14) reversion | buy | XRP-USD | 13.00 | — | entry signal |
| 2026-10-24T09:45 | RSI(14) reversion | sell | XRP-USD | 12.94 | -0.13 | stop-loss |
| 2026-10-24T09:30 | RSI(14) reversion | sell | DOGE-USD | 12.95 | -0.13 | stop-loss |
| 2026-10-24T09:25 | RSI(14) reversion | buy | ETH-USD | 13.04 | — | entry signal |
| 2026-10-24T09:15 | RSI(14) reversion | buy | XRP-USD | 13.07 | — | entry signal |
| 2026-10-24T09:10 | RSI(14) reversion · 1h | sell | BTC-USD | 12.76 | -0.23 | stop-loss |
| 2026-10-24T09:10 | RSI(14) reversion | buy | DOGE-USD | 13.08 | — | entry signal |
| 2026-10-24T09:05 | RSI(14) reversion | sell | XRP-USD | 13.01 | -0.13 | stop-loss |
| 2026-10-24T08:55 | RSI(14) reversion | sell | DOGE-USD | 13.02 | -0.13 | stop-loss |
| 2026-10-24T08:50 | CCI reversion · 1h | buy | ETH-USD | 1.08 | — | entry |
| 2026-10-24T08:50 | CCI reversion · 1h | buy | BTC-USD | 3.47 | — | entry |
| 2026-10-24T08:50 | CCI reversion · 1h | sell | DOGE-USD | 3.91 | -0.09 | stop-loss |
| 2026-10-24T08:25 | RSI(14) reversion | buy | XRP-USD | 13.14 | — | entry signal |
| 2026-10-24T08:25 | RSI(14) reversion | buy | DOGE-USD | 13.14 | — | entry signal |
| 2026-10-24T08:00 | Candlestick reversal · 1h | sell | DOGE-USD | 4.91 | -0.10 | stop-loss |
| 2026-10-24T07:30 | Squeeze breakout | sell | ETH-USD | 13.26 | -0.11 | exit signal |
| 2026-10-24T07:25 | RSI(14) reversion | sell | DOGE-USD | 13.06 | -0.12 | stop-loss |
| 2026-10-24T07:25 | Volume breakout | sell | ETH-USD | 14.13 | -0.11 | exit signal |
| 2026-10-24T07:20 | Volume breakout | buy | ETH-USD | 14.24 | — | entry signal |
| 2026-10-24T07:20 | Squeeze breakout | buy | ETH-USD | 13.37 | — | entry signal |
| 2026-10-24T07:10 | Squeeze breakout | sell | BTC-USD | 13.29 | -0.10 | stop-loss |
| 2026-10-24T07:05 | Squeeze breakout | buy | BTC-USD | 13.39 | — | entry signal |
| 2026-10-24T06:00 | VWAP momentum · 1h | sell | BTC-USD | 6.80 | -0.06 | exit signal |
| 2026-10-24T05:40 | RSI(14) reversion | buy | DOGE-USD | 13.17 | — | entry |
| 2026-10-24T05:10 | EMA 20/50 cross | sell | DOGE-USD | 12.86 | -0.12 | stop-loss |
| 2026-10-24T04:20 | EMA 20/50 cross | sell | ETH-USD | 12.86 | -0.10 | exit signal |
| 2026-10-24T04:15 | Three white soldiers | sell | XRP-USD | 20.15 | -0.16 | exit signal |
| 2026-10-24T04:05 | Three white soldiers | buy | XRP-USD | 20.32 | — | entry signal |
| 2026-10-24T03:50 | Squeeze breakout | sell | SOL-USD | 13.31 | -0.14 | stop-loss |
| 2026-10-24T03:50 | Squeeze breakout | sell | ETH-USD | 13.36 | -0.09 | exit signal |
| 2026-10-24T03:30 | Volume breakout | sell | SOL-USD | 14.15 | -0.12 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-26 11:40:05.000162+00:00 -> 2026-10-24 11:50:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
