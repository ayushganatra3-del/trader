# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T16:45:05.000148+00:00 · 32059 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.18 (-9.82%)

Closed trades 95, win rate 40.0%, fees £3.08, max drawdown -10.24%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.00 | -0.06 |

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

Today: 24552 decisions in 2481 calls, $0.3104 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T16:45 | 1 / 5 / 24 | SQQQ 14% |  |
| Breezy | 2026-10-22T16:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-22T16:45 | 4 / 20 / 6 | COIN 55% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.83 | 7.83 | 0 | — | 10.41 | 4.61 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.40 | 5.40 | 12 | 66.7 | 2.39 | 0.78 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.41 | 4.41 | 15 | 46.7 | 6.92 | 2.17 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 101.77 | 1.77 | 75 | 48.0 | -8.97 | -2.44 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.10 | 0.10 | 0 | — | 2.95 | 1.32 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.02 | -0.98 | 68 | 35.3 | 2.77 | 1.62 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 11 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.40 | -0.17 | -3.13 | 1 |
| 12 | Max aggression: 5-day momentum | meta | 97.46 | -2.54 | 10 | 50.0 | -17.83 | -1.42 | -34.64 | 26 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.14 | -2.86 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.54 | -2.03 | -5.83 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 96.20 | -3.80 | 0 | — | -0.35 | -0.08 | -5.31 | 1 |
| 16 | Hold BTC | benchmark | 96.18 | -3.82 | 0 | — | 4.76 | 0.88 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 96.17 | -3.83 | 117 | 30.8 | -6.08 | -3.11 | -7.58 | 258 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.76 | 0.66 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.41 | 2.00 | -7.38 | 198 |
| 21 | Copy: Insider buying | copy | 94.03 | -5.97 | 25 | 40.0 | -13.79 | -2.36 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.91 | -6.09 | 93 | 23.7 | -23.23 | -7.25 | -23.36 | 125 |
| 23 | Opening range 30m | breakout | 93.63 | -6.37 | 237 | 35.0 | -10.34 | -2.92 | -17.26 | 558 |
| 24 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.62 | -3.76 | -19.63 | 103 |
| 25 | Parabolic SAR · 1h | trend | 92.34 | -7.66 | 115 | 26.1 | -17.55 | -3.88 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.31 | -7.69 | 102 | 18.6 | -10.42 | -1.98 | -13.26 | 251 |
| 27 | Daily: Momentum burst | daily | 92.29 | -7.71 | 8 | 12.5 | -16.79 | -2.96 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.19 | -0.97 | -11.76 | 96 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.37 | -2.18 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.52 | -9.48 | 8 | 0.0 | -7.01 | -0.81 | -13.10 | 13 |
| 31 | Agent | meta | 90.18 | -9.82 | 95 | 40.0 | -22.17 | -6.22 | -25.92 | 291 |
| 32 | Bollinger breakout · 1h | breakout | 89.45 | -10.55 | 103 | 28.2 | -11.54 | -2.04 | -15.91 | 257 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.23 | -10.77 | 0 | — | -4.94 | -0.62 | -14.37 | 1 |
| 34 | Volume breakout · 1h | breakout | 89.00 | -11.00 | 101 | 22.8 | -11.56 | -2.05 | -12.86 | 106 |
| 35 | Stochastic reversion · 1h | reversion | 87.91 | -12.09 | 176 | 46.0 | -15.69 | -2.58 | -22.24 | 380 |
| 36 | EMA 20/50 cross · 1h | trend | 87.44 | -12.56 | 68 | 11.8 | -23.69 | -4.30 | -25.25 | 144 |
| 37 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -17.93 | -4.82 | -21.93 | 136 |
| 38 | Supertrend · 1h | trend | 87.13 | -12.87 | 102 | 15.7 | -24.22 | -4.71 | -27.05 | 219 |
| 39 | RSI momentum · 1h | momentum | 86.89 | -13.12 | 94 | 17.0 | -20.49 | -3.99 | -21.80 | 219 |
| 40 | Opening range 15m | breakout | 86.51 | -13.49 | 298 | 30.5 | -16.63 | -4.45 | -18.82 | 703 |
| 41 | Keltner breakout · 1h | breakout | 86.09 | -13.90 | 73 | 23.3 | -23.21 | -4.47 | -24.15 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.53 | -14.47 | 168 | 39.9 | -25.85 | -7.14 | -25.85 | 204 |
| 43 | MACD cross · 1h | trend | 84.86 | -15.13 | 214 | 23.4 | -26.81 | -4.95 | -28.04 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.27 | -15.73 | 96 | 15.6 | -29.52 | -5.56 | -30.01 | 221 |
| 45 | Ichimoku · 1h | trend | 84.18 | -15.82 | 64 | 12.5 | -20.03 | -3.68 | -22.68 | 116 |
| 46 | Z-score reversion · 1h | reversion | 83.66 | -16.34 | 104 | 33.7 | -14.03 | -2.14 | -21.32 | 198 |
| 47 | MFI reversion · 1h | reversion | 83.42 | -16.58 | 231 | 32.9 | -18.29 | -2.81 | -21.11 | 149 |
| 48 | Donchian 20/10 · 1h | breakout | 83.33 | -16.67 | 92 | 20.7 | -24.31 | -4.43 | -24.99 | 226 |
| 49 | Williams %R · 1h | reversion | 82.36 | -17.64 | 201 | 44.8 | -33.31 | -5.28 | -37.96 | 522 |
| 50 | MACD zero-line · 1h | trend | 82.32 | -17.68 | 102 | 15.7 | -24.82 | -4.73 | -25.88 | 226 |
| 51 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.96 | -18.03 | -45.15 | 598 |
| 52 | OBV trend · 1h | momentum | 81.81 | -18.18 | 197 | 17.8 | -32.00 | -6.10 | -32.27 | 306 |
| 53 | CCI reversion · 1h | reversion | 81.00 | -19.00 | 191 | 43.5 | -22.28 | -2.96 | -27.44 | 443 |
| 54 | Agent (ML meta-label) | meta | 80.79 | -19.21 | 781 | 19.5 | -11.19 | -2.02 | -16.46 | 369 |
| 55 | Bollinger reversion · 1h | reversion | 80.59 | -19.41 | 165 | 35.8 | -30.64 | -5.91 | -32.60 | 360 |
| 56 | ROC + volume · 1h | momentum | 79.78 | -20.22 | 230 | 24.3 | -28.50 | -5.15 | -28.63 | 379 |
| 57 | Heikin-Ashi · 1h | trend | 79.75 | -20.25 | 260 | 23.5 | -43.67 | -9.31 | -44.32 | 672 |
| 58 | RSI(14) reversion · 1h | reversion | 78.48 | -21.52 | 87 | 24.1 | -18.99 | -3.57 | -23.28 | 180 |
| 59 | Candlestick reversal · 1h | reversion | 78.06 | -21.94 | 235 | 30.2 | -36.39 | -6.22 | -38.53 | 560 |
| 60 | EMA 9/21 cross · 1h | trend | 78.00 | -22.00 | 155 | 11.6 | -31.93 | -5.81 | -32.94 | 335 |
| 61 | VWAP momentum · 1h | momentum | 76.51 | -23.49 | 499 | 21.4 | -50.97 | -10.37 | -51.35 | 1234 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.25 | -2.81 | -47.87 | 43 |
| 63 | ROC + volume | momentum | 59.25 | -40.75 | 687 | 23.3 | -77.98 | -21.42 | -79.41 | 1691 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.37 | -19.25 | -65.33 | 859 |
| 65 | Donchian 55/20 | breakout | 56.21 | -43.79 | 538 | 19.7 | -72.23 | -19.40 | -74.18 | 1272 |
| 66 | Squeeze breakout | breakout | 55.28 | -44.72 | 528 | 14.0 | -67.36 | -22.86 | -68.37 | 1199 |
| 67 | EMA 20/50 cross | trend | 54.15 | -45.85 | 584 | 20.2 | -79.31 | -20.39 | -80.20 | 1438 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.29 | -17.01 | -76.51 | 1665 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.81 | -14.36 | -73.11 | 1512 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -31.65 | -98.88 | 5298 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.98 | -32.94 | -94.38 | 2571 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.08 | -23.20 | -89.05 | 1898 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.39 | -27.93 | -91.99 | 2350 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.02 | -25.08 | -91.05 | 2220 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -34.12 | -97.92 | 3495 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -35.97 | -97.07 | 3557 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -28.07 | -94.46 | 2549 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.06 | -27.55 | -83.55 | 1719 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -36.56 | -99.48 | 5830 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.39 | -29.56 | -93.00 | 2617 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.73 | -30.63 | -95.75 | 3445 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.40 | -99.78 | 6150 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -29.12 | -92.18 | 2327 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -38.96 | -97.76 | 3589 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -38.03 | -98.63 | 4748 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.31 | -34.55 | -94.67 | 2788 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.36 | -27.30 | -84.52 | 1788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -40.04 | -99.59 | 6221 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.72 | -23.33 | -87.76 | 2185 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.49 | -26.68 | -88.60 | 2185 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.20 | -33.69 | -96.24 | 3797 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.54 | -33.56 | -89.85 | 2110 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.20 | -34.41 | -96.22 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.24 | -99.91 | 8243 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T16:45 | Agent (ML meta-label) | buy | TQQQ | 3.37 | — | entry |
| 2026-10-22T16:45 | Agent (ML meta-label) | buy | TNA | 5.05 | — | entry |
| 2026-10-22T16:45 | Agent (ML meta-label) | buy | SPY | 5.05 | — | entry |
| 2026-10-22T16:45 | Agent (ML meta-label) | sell | SQQQ | 8.24 | 0.07 | selected signal exited |
| 2026-10-22T16:45 | Agent (ML meta-label) | sell | LABU | 5.23 | -0.21 | selected signal exited |
| 2026-10-22T16:45 | Agent | sell | ETHU | 17.72 | -0.41 | selected signal exited |
| 2026-10-22T16:45 | Opening range 15m | buy | TNA | 8.58 | — | rebalance up |
| 2026-10-22T16:45 | Opening range 15m | sell | MSTR | 17.15 | -0.28 | stop-loss |
| 2026-10-22T16:45 | ROC + volume | sell | TECL | 14.64 | -0.28 | stop-loss |
| 2026-10-22T16:45 | EMA 20/50 cross | sell | IWM | 13.51 | -0.07 | stop-loss |
| 2026-10-22T16:40 | Agent | buy | BITX | 18.07 | — | following VWAP reversion |
| 2026-10-22T16:40 | OBV trend · 1h | sell | LABU | 20.13 | -0.92 | stop-loss |
| 2026-10-22T16:40 | EMA 20/50 cross · 1h | buy | TNA | 4.41 | — | rebalance up |
| 2026-10-22T16:40 | EMA 20/50 cross · 1h | buy | IWM | 4.41 | — | rebalance up |
| 2026-10-22T16:40 | EMA 20/50 cross · 1h | sell | LABU | 17.05 | -0.70 | stop-loss |
| 2026-10-22T16:40 | RSI(14) reversion | sell | UPRO | 4.83 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | PLTR | 4.85 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | NVDA | 1.52 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | MSTR | 4.83 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | MSFT | 4.85 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | META | 4.78 | -0.07 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | GOOGL | 4.85 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | ETHU | 4.81 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | COIN | 4.85 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | BITX | 4.84 | -0.06 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | AMZN | 4.85 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | RSI(14) reversion | sell | AMD | 3.31 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T16:40 | ROC + volume | sell | UPRO | 14.79 | -0.12 | stop-loss |
| 2026-10-22T16:40 | EMA 20/50 cross | sell | TNA | 13.50 | -0.07 | exit signal |
| 2026-10-22T16:35 | Agent (ML meta-label) | buy | QQQ | 4.86 | — | entry |
| 2026-10-22T16:35 | Agent (ML meta-label) | buy | GOOGL | 3.27 | — | entry |
| 2026-10-22T16:35 | Agent (ML meta-label) | sell | SPY | 8.13 | -0.03 | selected signal exited |
| 2026-10-22T16:35 | MFI reversion · 1h | buy | SOXL | 8.09 | — | entry |
| 2026-10-22T16:35 | MFI reversion · 1h | buy | QQQ | 6.25 | — | rebalance up |
| 2026-10-22T16:35 | MFI reversion · 1h | buy | AMD | 9.30 | — | entry |
| 2026-10-22T16:35 | MFI reversion · 1h | sell | XRP-USD | 4.72 | -0.05 | rebalance down |
| 2026-10-22T16:35 | MFI reversion · 1h | sell | SOL-USD | 4.74 | -0.02 | rebalance down |
| 2026-10-22T16:35 | MFI reversion · 1h | sell | ETH-USD | 4.69 | -0.07 | rebalance down |
| 2026-10-22T16:35 | MFI reversion · 1h | sell | DOGE-USD | 4.68 | -0.07 | rebalance down |
| 2026-10-22T16:35 | MFI reversion · 1h | sell | BTC-USD | 4.81 | -0.05 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 16:45:05.000148+00:00 -> 2026-10-22 16:55:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
