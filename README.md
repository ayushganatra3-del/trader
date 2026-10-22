# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T17:15:05.000158+00:00 · 32079 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.03 (-9.97%)

Closed trades 96, win rate 39.6%, fees £3.11, max drawdown -10.39%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.96 | -0.08 |
| ETHU | 35.99 | +0.06 |

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

Today: 26358 decisions in 2541 calls, $0.3316 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T17:15 | 7 / 14 / 9 | cash |  |
| Breezy | 2026-10-22T17:15 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-22T17:15 | 5 / 23 / 2 | COIN 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.74 | 7.74 | 0 | — | 10.37 | 4.61 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.62 | 5.62 | 12 | 66.7 | 2.60 | 0.84 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.63 | 4.63 | 15 | 46.7 | 7.13 | 2.22 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.90 | 0.90 | 77 | 46.8 | -9.80 | -2.64 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.27 | 0.27 | 0 | — | 2.83 | 1.26 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.60 | 1.52 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 11 | Hold SPY | benchmark | 98.16 | -1.84 | 0 | — | -0.40 | -0.18 | -3.13 | 1 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 97.14 | -2.86 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.51 | -2.02 | -5.83 | 1 |
| 14 | Max aggression: 5-day momentum | meta | 96.46 | -3.54 | 10 | 50.0 | -18.67 | -1.50 | -34.64 | 26 |
| 15 | Agent (rotation) | meta | 96.29 | -3.71 | 117 | 30.8 | -6.48 | -3.34 | -7.58 | 258 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.02 | -3.98 | 0 | — | -0.44 | -0.11 | -5.31 | 1 |
| 17 | Hold BTC | benchmark | 95.87 | -4.13 | 0 | — | 4.40 | 0.82 | -8.68 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.85 | 0.68 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.41 | 2.00 | -7.38 | 198 |
| 21 | Copy: Insider buying | copy | 93.93 | -6.07 | 25 | 40.0 | -13.89 | -2.37 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.79 | -6.21 | 94 | 23.4 | -23.33 | -7.28 | -23.53 | 125 |
| 23 | Opening range 30m | breakout | 93.68 | -6.32 | 237 | 35.0 | -10.30 | -2.90 | -17.26 | 558 |
| 24 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.62 | -3.76 | -19.64 | 103 |
| 25 | Parabolic SAR · 1h | trend | 92.49 | -7.51 | 115 | 26.1 | -17.41 | -3.85 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.20 | -7.80 | 102 | 18.6 | -10.52 | -2.00 | -13.26 | 251 |
| 27 | Daily: Momentum burst | daily | 91.93 | -8.07 | 8 | 12.5 | -17.53 | -3.09 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.63 | -1.08 | -11.76 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.29 | -2.16 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.33 | -9.66 | 8 | 0.0 | -6.98 | -0.80 | -13.10 | 13 |
| 31 | Agent | meta | 90.03 | -9.97 | 96 | 39.6 | -20.42 | -7.12 | -22.80 | 297 |
| 32 | Bollinger breakout · 1h | breakout | 89.36 | -10.64 | 104 | 27.9 | -11.59 | -2.05 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.05 | -10.95 | 101 | 22.8 | -11.09 | -1.96 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.64 | -11.36 | 0 | — | -5.36 | -0.67 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.66 | -12.34 | 46 | 34.8 | -20.05 | -4.89 | -22.76 | 154 |
| 36 | Stochastic reversion · 1h | reversion | 87.62 | -12.38 | 178 | 45.5 | -15.69 | -2.55 | -22.21 | 381 |
| 37 | EMA 20/50 cross · 1h | trend | 87.45 | -12.55 | 68 | 11.8 | -23.15 | -4.18 | -25.25 | 142 |
| 38 | Supertrend · 1h | trend | 86.97 | -13.03 | 102 | 15.7 | -24.36 | -4.72 | -27.31 | 219 |
| 39 | RSI momentum · 1h | momentum | 86.73 | -13.27 | 94 | 17.0 | -20.15 | -3.88 | -22.06 | 218 |
| 40 | Opening range 15m | breakout | 86.46 | -13.54 | 300 | 30.3 | -16.66 | -4.46 | -18.82 | 702 |
| 41 | Keltner breakout · 1h | breakout | 86.14 | -13.86 | 73 | 23.3 | -23.51 | -4.54 | -24.32 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 168 | 39.9 | -25.96 | -7.13 | -25.98 | 204 |
| 43 | MACD cross · 1h | trend | 84.83 | -15.17 | 214 | 23.4 | -26.83 | -4.95 | -28.18 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.26 | -15.74 | 96 | 15.6 | -29.62 | -5.57 | -30.02 | 221 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.02 | 116 |
| 46 | Z-score reversion · 1h | reversion | 83.73 | -16.27 | 104 | 33.7 | -13.95 | -2.12 | -21.32 | 198 |
| 47 | Donchian 20/10 · 1h | breakout | 83.14 | -16.86 | 92 | 20.7 | -24.48 | -4.45 | -25.18 | 226 |
| 48 | MFI reversion · 1h | reversion | 82.85 | -17.15 | 235 | 32.3 | -18.57 | -2.85 | -21.11 | 149 |
| 49 | MACD zero-line · 1h | trend | 82.34 | -17.66 | 102 | 15.7 | -24.80 | -4.72 | -25.99 | 226 |
| 50 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.96 | -18.03 | -45.15 | 598 |
| 51 | Williams %R · 1h | reversion | 81.93 | -18.07 | 204 | 44.1 | -33.71 | -5.35 | -37.95 | 524 |
| 52 | OBV trend · 1h | momentum | 81.81 | -18.19 | 197 | 17.8 | -32.44 | -6.16 | -32.68 | 306 |
| 53 | Agent (ML meta-label) | meta | 80.48 | -19.52 | 793 | 19.4 | -12.64 | -2.33 | -16.02 | 363 |
| 54 | CCI reversion · 1h | reversion | 80.41 | -19.59 | 192 | 43.2 | -22.88 | -3.05 | -27.44 | 443 |
| 55 | Bollinger reversion · 1h | reversion | 80.33 | -19.67 | 168 | 35.1 | -30.86 | -5.94 | -32.59 | 360 |
| 56 | Heikin-Ashi · 1h | trend | 79.79 | -20.21 | 260 | 23.5 | -43.61 | -9.29 | -44.28 | 672 |
| 57 | ROC + volume · 1h | momentum | 79.64 | -20.36 | 231 | 24.2 | -28.89 | -5.19 | -29.02 | 378 |
| 58 | RSI(14) reversion · 1h | reversion | 77.91 | -22.09 | 90 | 23.3 | -20.00 | -3.74 | -23.32 | 181 |
| 59 | EMA 9/21 cross · 1h | trend | 77.87 | -22.13 | 155 | 11.6 | -32.02 | -5.82 | -33.15 | 335 |
| 60 | Candlestick reversal · 1h | reversion | 77.70 | -22.30 | 238 | 29.8 | -36.73 | -6.29 | -38.37 | 564 |
| 61 | VWAP momentum · 1h | momentum | 76.58 | -23.42 | 499 | 21.4 | -50.84 | -10.36 | -51.28 | 1234 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.28 | -2.81 | -48.18 | 43 |
| 63 | ROC + volume | momentum | 59.21 | -40.78 | 687 | 23.3 | -77.99 | -21.28 | -79.47 | 1694 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.39 | -19.26 | -65.34 | 857 |
| 65 | Donchian 55/20 | breakout | 56.24 | -43.76 | 538 | 19.7 | -72.72 | -20.03 | -74.23 | 1272 |
| 66 | Squeeze breakout | breakout | 55.28 | -44.72 | 528 | 14.0 | -67.40 | -22.95 | -68.37 | 1197 |
| 67 | EMA 20/50 cross | trend | 54.18 | -45.82 | 584 | 20.2 | -79.36 | -20.38 | -80.23 | 1439 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.50 | -17.02 | -76.67 | 1685 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.97 | -14.26 | -73.30 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.32 | -98.88 | 5290 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.07 | -33.81 | -94.38 | 2570 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.08 | -23.20 | -89.06 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -28.96 | -91.99 | 2350 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -24.92 | -91.00 | 2216 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -34.10 | -97.93 | 3498 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.89 | -36.36 | -97.09 | 3560 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.45 | -28.13 | -94.47 | 2549 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -28.05 | -83.52 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -36.58 | -99.49 | 5849 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -29.49 | -93.00 | 2615 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.69 | -30.44 | -95.72 | 3443 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.80 | -99.78 | 6161 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -30.30 | -92.21 | 2328 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.27 | -97.75 | 3587 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.63 | -37.96 | -98.64 | 4749 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.32 | -34.65 | -94.68 | 2786 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.27 | -26.96 | -84.51 | 1786 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -39.92 | -99.59 | 6237 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.96 | -23.59 | -88.01 | 2180 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.72 | -26.74 | -88.87 | 2192 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.21 | -33.64 | -96.25 | 3811 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -33.39 | -89.85 | 2104 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.19 | -34.17 | -96.22 | 4145 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.17 | -99.91 | 8243 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T17:15 | Agent (ML meta-label) | buy | SPY | 2.87 | — | entry |
| 2026-10-22T17:15 | Agent (ML meta-label) | sell | MSFT | 2.87 | -0.00 | selected signal exited |
| 2026-10-22T17:10 | Day trade: Stocks in Play ORB | sell | TSLA | 24.65 | -0.16 | target is flat |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | QQQ | 3.27 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | MSFT | 2.88 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | GOOGL | 4.56 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | sell | TSLA | 5.34 | -0.05 | selected signal exited |
| 2026-10-22T17:10 | Agent (ML meta-label) | sell | TNA | 5.36 | -0.00 | selected signal exited |
| 2026-10-22T17:10 | ROC + volume · 1h | buy | PLTR | 4.00 | — | rebalance up |
| 2026-10-22T17:10 | ROC + volume · 1h | buy | MSTR | 4.23 | — | rebalance up |
| 2026-10-22T17:10 | ROC + volume · 1h | sell | TSLA | 15.60 | -0.42 | stop-loss |
| 2026-10-22T17:10 | Trend pullback · 1h | sell | TSLA | 22.99 | -0.62 | stop-loss |
| 2026-10-22T17:10 | EMA 20/50 cross · 1h | buy | TSLA | 4.40 | — | rebalance up |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | TQQQ | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | TNA | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | IWM | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | ETH-USD | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | BITX | 5.36 | — | following VWAP reversion |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | AMZN | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | AMD | 5.36 | — | entry |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | TSLA | 5.94 | -0.03 | rebalance down |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | TECL | 5.87 | -0.08 | rebalance down |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | SPY | 5.04 | -0.01 | selected signal exited |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | NVDA | 5.94 | -0.03 | rebalance down |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | LABU | 5.82 | -0.08 | rebalance down |
| 2026-10-22T17:05 | Agent (ML meta-label) | sell | AAPL | 5.97 | -0.01 | rebalance down |
| 2026-10-22T17:05 | Opening range 15m | sell | TSLA | 21.37 | -0.39 | stop-loss |
| 2026-10-22T17:00 | Agent (ML meta-label) | buy | TSLA | 5.91 | — | rebalance up |
| 2026-10-22T17:00 | Agent (ML meta-label) | buy | TECL | 7.64 | — | rebalance up |
| 2026-10-22T17:00 | Agent (ML meta-label) | buy | NVDA | 5.92 | — | rebalance up |
| 2026-10-22T17:00 | Agent (ML meta-label) | buy | LABU | 11.34 | — | following Connors RSI(2) |
| 2026-10-22T17:00 | Agent (ML meta-label) | buy | AAPL | 7.13 | — | rebalance up |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | TQQQ | 3.37 | 0.00 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | TNA | 5.08 | 0.03 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | QQQ | 4.85 | -0.01 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | IWM | 8.13 | -0.02 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | GOOGL | 3.27 | -0.00 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | BITX | 5.39 | -0.05 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | AMZN | 5.42 | -0.02 | selected signal exited |
| 2026-10-22T17:00 | Agent (ML meta-label) | sell | AMD | 5.40 | -0.04 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 17:15:05.000158+00:00 -> 2026-10-22 17:25:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
