# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T10:45:05.000153+00:00 · 31767 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 8025 decisions in 1605 calls, $0.1125 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T10:45 | 0 / 5 / 0 | cash |  |
| Breezy | 2026-10-22T10:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T10:45 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.89 | +3.05% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.02 | 6.02 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.46 | 2.46 | 75 | 48.0 | -8.24 | -2.23 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 101.49 | 1.49 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.22 | 0.22 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.61 | -0.39 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.39 | -0.61 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.49 | -2.52 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.05 | -2.95 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 17 | Hold BTC | benchmark | 96.87 | -3.13 | 0 | — | 6.59 | 1.15 | -8.68 | 1 |
| 18 | Copy: Insider buying | copy | 96.68 | -3.32 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 21 | ADX DI cross · 1h | trend | 95.45 | -4.54 | 92 | 19.6 | -11.55 | -2.12 | -16.14 | 261 |
| 22 | Daily: Momentum burst | daily | 94.92 | -5.08 | 6 | 16.7 | -9.30 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.86 | -5.14 | 92 | 23.9 | -20.36 | -6.34 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.91 | -6.09 | 46 | 17.4 | -16.33 | -3.34 | -17.38 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.91 | -7.09 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.81 | -7.19 | 113 | 25.7 | -16.39 | -3.62 | -19.79 | 271 |
| 29 | Squeeze breakout · 1h | breakout | 92.49 | -7.51 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.18 | -7.82 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 93 | 30.1 | -8.39 | -1.50 | -14.43 | 258 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -14.00 | -7.03 | -16.67 | 255 |
| 34 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 95 | 24.2 | -10.83 | -1.90 | -12.46 | 106 |
| 35 | Supertrend · 1h | trend | 89.64 | -10.36 | 93 | 15.1 | -21.06 | -4.21 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.11 | -10.89 | 89 | 18.0 | -17.30 | -3.42 | -20.65 | 217 |
| 37 | Stochastic reversion · 1h | reversion | 88.36 | -11.64 | 173 | 46.2 | -15.12 | -2.49 | -22.24 | 371 |
| 38 | EMA 20/50 cross · 1h | trend | 88.30 | -11.70 | 63 | 12.7 | -21.83 | -3.78 | -23.52 | 143 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 67 | 23.9 | -20.71 | -4.02 | -22.53 | 199 |
| 41 | MACD cross · 1h | trend | 87.43 | -12.57 | 202 | 22.3 | -24.31 | -4.62 | -27.05 | 468 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -13.35 | -3.85 | -19.30 | 117 |
| 43 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.51 | -13.49 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 45 | Connors RSI(2) · 1h | reversion | 86.03 | -13.97 | 166 | 40.4 | -25.34 | -7.17 | -25.48 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.40 | -14.60 | 87 | 20.7 | -20.77 | -3.89 | -23.55 | 226 |
| 47 | MFI reversion · 1h | reversion | 85.26 | -14.74 | 229 | 33.2 | -13.60 | -2.02 | -21.11 | 143 |
| 48 | Triple EMA stack · 1h | trend | 85.17 | -14.83 | 94 | 16.0 | -26.78 | -4.94 | -27.71 | 220 |
| 49 | MACD zero-line · 1h | trend | 84.51 | -15.49 | 92 | 15.2 | -23.99 | -4.61 | -26.48 | 229 |
| 50 | Agent (ML meta-label) | meta | 83.58 | -16.41 | 748 | 19.8 | -8.60 | -1.59 | -16.88 | 347 |
| 51 | OBV trend · 1h | momentum | 83.50 | -16.50 | 191 | 18.3 | -30.67 | -5.76 | -31.39 | 305 |
| 52 | ROC + volume · 1h | momentum | 82.77 | -17.23 | 218 | 23.9 | -27.30 | -4.90 | -29.59 | 382 |
| 53 | Williams %R · 1h | reversion | 82.59 | -17.41 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Three white soldiers | momentum | 82.45 | -17.55 | 259 | 20.5 | -44.95 | -18.00 | -45.55 | 602 |
| 55 | CCI reversion · 1h | reversion | 82.12 | -17.88 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 56 | Bollinger reversion · 1h | reversion | 81.86 | -18.14 | 164 | 36.0 | -29.77 | -5.77 | -32.84 | 352 |
| 57 | Heikin-Ashi · 1h | trend | 81.40 | -18.60 | 251 | 23.9 | -42.96 | -9.08 | -46.07 | 675 |
| 58 | RSI(14) reversion · 1h | reversion | 80.89 | -19.11 | 85 | 24.7 | -17.49 | -3.02 | -24.99 | 177 |
| 59 | EMA 9/21 cross · 1h | trend | 80.74 | -19.26 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.01 | -20.99 | 231 | 30.3 | -38.79 | -7.12 | -41.73 | 549 |
| 61 | VWAP momentum · 1h | momentum | 78.98 | -21.02 | 483 | 22.2 | -49.90 | -10.08 | -52.16 | 1249 |
| 62 | Max aggression: 1-day momentum | meta | 77.13 | -22.87 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.79 | -40.21 | 679 | 23.4 | -77.76 | -21.80 | -78.97 | 1700 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.16 | -19.31 | -64.95 | 858 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -71.80 | -18.80 | -74.04 | 1274 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.04 | -22.78 | -67.93 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.81 | -19.09 | -80.87 | 1436 |
| 68 | RSI(14) reversion | reversion | 53.58 | -46.42 | 789 | 26.2 | -75.99 | -17.06 | -76.16 | 1636 |
| 69 | VWAP reversion | reversion | 51.59 | -48.41 | 786 | 25.3 | -72.39 | -14.51 | -72.87 | 1488 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.71 | -98.85 | 5290 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.98 | -33.41 | -94.26 | 2581 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.85 | -23.17 | -88.73 | 1893 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -28.16 | -91.74 | 2358 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.25 | -25.49 | -91.25 | 2250 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -35.47 | -97.84 | 3508 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -36.55 | -96.99 | 3594 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -28.17 | -94.46 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.07 | -27.81 | -83.42 | 1727 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.86 | -99.46 | 5775 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.24 | -29.89 | -92.75 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.84 | -30.76 | -95.84 | 3458 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.45 | -99.77 | 6155 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.81 | -30.35 | -91.95 | 2336 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -38.54 | -97.71 | 3611 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.60 | -38.30 | -98.60 | 4720 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -34.89 | -94.47 | 2793 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.32 | -27.55 | -84.44 | 1789 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.15 | -99.58 | 6207 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.73 | -23.49 | -87.79 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.35 | -26.88 | -88.48 | 2155 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.15 | -33.84 | -96.16 | 3776 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.61 | -34.50 | -89.61 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.10 | -34.32 | -96.13 | 4106 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.95 | -99.91 | 8279 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T10:35 | VWAP reversion | buy | ETH-USD | 2.58 | — | rebalance up |
| 2026-10-22T10:35 | VWAP reversion | sell | SOL-USD | 2.58 | 0.01 | rebalance down |
| 2026-10-22T10:10 | Agent (ML meta-label) | sell | XRP-USD | 6.26 | -0.05 | rebalance down |
| 2026-10-22T10:05 | Agent (ML meta-label) | buy | XRP-USD | 9.29 | — | entry |
| 2026-10-22T10:05 | RSI(14) reversion | sell | XRP-USD | 10.75 | -0.03 | exit signal |
| 2026-10-22T10:05 | RSI(14) reversion | sell | DOGE-USD | 10.74 | -0.03 | exit signal |
| 2026-10-22T10:05 | RSI(14) reversion | sell | BTC-USD | 10.72 | -0.04 | exit signal |
| 2026-10-22T10:05 | ROC + volume | buy | SOL-USD | 14.95 | — | entry signal |
| 2026-10-22T10:00 | MFI reversion · 1h | buy | SOL-USD | 21.31 | — | entry signal |
| 2026-10-22T10:00 | MFI reversion · 1h | buy | BTC-USD | 21.31 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | XRP-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | SOL-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | DOGE-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | BTC-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | Bollinger reversion · 1h | buy | ETH-USD | 20.33 | — | entry signal |
| 2026-10-22T10:00 | Bollinger reversion · 1h | buy | BTC-USD | 20.47 | — | entry signal |
| 2026-10-22T10:00 | RSI(14) reversion · 1h | buy | SOL-USD | 20.21 | — | entry signal |
| 2026-10-22T10:00 | Three white soldiers | buy | SOL-USD | 20.61 | — | entry signal |
| 2026-10-22T09:55 | RSI(14) reversion | buy | ETH-USD | 2.83 | — | rebalance up |
| 2026-10-22T09:55 | RSI(14) reversion | sell | SOL-USD | 10.79 | -0.05 | exit signal |
| 2026-10-22T09:50 | VWAP reversion | buy | ETH-USD | 5.15 | — | entry signal |
| 2026-10-22T09:50 | RSI(14) reversion | buy | ETH-USD | 10.60 | — | entry signal |
| 2026-10-22T09:50 | RSI(14) reversion | sell | BTC-USD | 2.67 | -0.02 | rebalance down |
| 2026-10-22T09:45 | Agent (ML meta-label) | sell | XRP-USD | 10.39 | -0.06 | selected signal exited |
| 2026-10-22T09:45 | VWAP reversion | buy | BTC-USD | 5.11 | — | rebalance up |
| 2026-10-22T09:45 | VWAP reversion | sell | ETH-USD | 10.25 | -0.10 | stop-loss |
| 2026-10-22T09:45 | RSI(14) reversion | buy | BTC-USD | 2.76 | — | rebalance up |
| 2026-10-22T09:45 | RSI(14) reversion | sell | ETH-USD | 10.69 | -0.11 | stop-loss |
| 2026-10-22T09:40 | Agent (ML meta-label) | buy | XRP-USD | 10.45 | — | entry |
| 2026-10-22T09:17 | RSI(14) reversion | buy | BTC-USD | 2.68 | — | rebalance up |
| 2026-10-22T09:17 | RSI(14) reversion | sell | ETH-USD | 2.68 | -0.02 | rebalance down |
| 2026-10-22T09:15 | VWAP reversion | buy | BTC-USD | 7.78 | — | entry signal |
| 2026-10-22T09:15 | VWAP reversion | sell | XRP-USD | 2.60 | -0.02 | rebalance down |
| 2026-10-22T09:15 | VWAP reversion | sell | ETH-USD | 2.58 | -0.02 | rebalance down |
| 2026-10-22T09:15 | VWAP reversion | sell | DOGE-USD | 2.61 | -0.01 | rebalance down |
| 2026-10-22T09:15 | RSI(14) reversion | buy | BTC-USD | 8.00 | — | entry signal |
| 2026-10-22T09:15 | RSI(14) reversion | sell | XRP-USD | 2.69 | -0.02 | rebalance down |
| 2026-10-22T09:15 | RSI(14) reversion | sell | DOGE-USD | 2.70 | -0.01 | rebalance down |
| 2026-10-22T09:10 | VWAP reversion | buy | SOL-USD | 12.82 | — | entry signal |
| 2026-10-22T09:10 | RSI(14) reversion | buy | XRP-USD | 2.70 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 10:45:05.000153+00:00 -> 2026-10-22 10:55:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
