# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T12:15:05.000154+00:00 · 31842 ticks

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

Today: 9150 decisions in 1830 calls, $0.1282 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T12:15 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-22T12:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T12:15 | 2 / 3 / 0 | ETH-USD 53% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.15 | 6.15 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.31 | 2.31 | 75 | 48.0 | -8.48 | -2.30 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 101.61 | 1.61 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.34 | 0.34 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.73 | -0.27 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.51 | -0.49 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.60 | -2.40 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.84 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Insider buying | copy | 96.79 | -3.21 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 18 | Hold BTC | benchmark | 96.66 | -3.34 | 0 | — | 5.87 | 1.05 | -8.68 | 1 |
| 19 | Agent (rotation) | meta | 95.81 | -4.19 | 117 | 30.8 | -8.74 | -5.13 | -8.79 | 235 |
| 20 | ADX DI cross · 1h | trend | 95.56 | -4.44 | 92 | 19.6 | -10.11 | -1.83 | -16.14 | 258 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 22 | Daily: Momentum burst | daily | 95.03 | -4.97 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.91 | -5.09 | 92 | 23.9 | -20.36 | -6.35 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.93 | -6.07 | 46 | 17.4 | -16.33 | -3.34 | -17.38 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 93.02 | -6.98 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.86 | -7.14 | 113 | 25.7 | -15.82 | -3.48 | -19.79 | 270 |
| 29 | Squeeze breakout · 1h | breakout | 92.51 | -7.49 | 50 | 24.0 | -3.00 | -0.66 | -11.48 | 101 |
| 30 | Daily: Bullish score | daily | 92.27 | -7.73 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.08 | -7.92 | 93 | 30.1 | -8.39 | -1.50 | -14.43 | 258 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -17.56 | -5.38 | -19.40 | 263 |
| 34 | Volume breakout · 1h | breakout | 90.43 | -9.57 | 95 | 24.2 | -10.79 | -1.89 | -12.43 | 107 |
| 35 | Supertrend · 1h | trend | 89.71 | -10.29 | 93 | 15.1 | -21.06 | -4.21 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.17 | -10.83 | 89 | 18.0 | -19.32 | -3.89 | -20.84 | 221 |
| 37 | Stochastic reversion · 1h | reversion | 88.38 | -11.62 | 173 | 46.2 | -15.25 | -2.51 | -22.24 | 371 |
| 38 | EMA 20/50 cross · 1h | trend | 88.35 | -11.65 | 64 | 12.5 | -21.84 | -3.78 | -23.52 | 142 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.73 | -12.27 | 67 | 23.9 | -20.71 | -4.02 | -22.53 | 199 |
| 41 | MACD cross · 1h | trend | 87.52 | -12.48 | 202 | 22.3 | -24.10 | -4.57 | -27.05 | 468 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.37 | -4.44 | -19.93 | 133 |
| 43 | Z-score reversion · 1h | reversion | 86.84 | -13.16 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.59 | -13.41 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 45 | Connors RSI(2) · 1h | reversion | 85.90 | -14.10 | 166 | 40.4 | -25.50 | -7.15 | -25.51 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.47 | -14.53 | 87 | 20.7 | -20.77 | -3.89 | -23.55 | 226 |
| 47 | Triple EMA stack · 1h | trend | 85.24 | -14.76 | 94 | 16.0 | -26.90 | -4.97 | -27.82 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.17 | -14.83 | 229 | 33.2 | -13.74 | -2.05 | -21.11 | 143 |
| 49 | MACD zero-line · 1h | trend | 84.61 | -15.39 | 92 | 15.2 | -23.99 | -4.61 | -26.48 | 229 |
| 50 | Agent (ML meta-label) | meta | 83.59 | -16.41 | 750 | 19.7 | -9.74 | -1.75 | -15.73 | 337 |
| 51 | OBV trend · 1h | momentum | 83.57 | -16.43 | 191 | 18.3 | -31.06 | -5.84 | -31.64 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.85 | -17.15 | 218 | 23.9 | -24.79 | -4.46 | -26.88 | 381 |
| 53 | Williams %R · 1h | reversion | 82.55 | -17.45 | 199 | 44.7 | -31.60 | -4.90 | -36.62 | 518 |
| 54 | Three white soldiers | momentum | 82.37 | -17.63 | 260 | 20.4 | -44.97 | -18.03 | -45.55 | 601 |
| 55 | CCI reversion · 1h | reversion | 82.07 | -17.93 | 188 | 43.6 | -20.41 | -2.65 | -27.44 | 439 |
| 56 | Bollinger reversion · 1h | reversion | 81.88 | -18.12 | 164 | 36.0 | -29.84 | -5.79 | -32.84 | 352 |
| 57 | Heikin-Ashi · 1h | trend | 81.38 | -18.62 | 251 | 23.9 | -43.92 | -9.04 | -46.07 | 676 |
| 58 | EMA 9/21 cross · 1h | trend | 80.83 | -19.17 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 80.81 | -19.19 | 85 | 24.7 | -17.10 | -2.92 | -24.99 | 174 |
| 60 | Candlestick reversal · 1h | reversion | 79.10 | -20.90 | 231 | 30.3 | -39.24 | -7.25 | -41.79 | 545 |
| 61 | VWAP momentum · 1h | momentum | 79.05 | -20.95 | 483 | 22.2 | -49.74 | -10.09 | -51.99 | 1250 |
| 62 | Max aggression: 1-day momentum | meta | 77.22 | -22.77 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.75 | -40.25 | 680 | 23.4 | -77.78 | -21.81 | -78.97 | 1701 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.20 | -19.37 | -64.95 | 857 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -71.80 | -18.80 | -74.04 | 1274 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.04 | -22.78 | -67.93 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.18 | -44.82 | 575 | 20.5 | -79.00 | -19.91 | -80.44 | 1433 |
| 68 | RSI(14) reversion | reversion | 53.57 | -46.43 | 789 | 26.2 | -75.96 | -17.03 | -76.18 | 1640 |
| 69 | VWAP reversion | reversion | 51.41 | -48.59 | 787 | 25.3 | -72.53 | -14.49 | -72.93 | 1488 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -31.48 | -98.85 | 5289 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -32.48 | -94.27 | 2577 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.79 | -22.90 | -88.75 | 1890 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.13 | -27.35 | -91.74 | 2353 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.21 | -25.43 | -91.23 | 2249 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.73 | -34.82 | -97.84 | 3500 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -36.25 | -96.98 | 3582 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -28.16 | -94.43 | 2549 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -27.66 | -83.41 | 1726 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.80 | -99.46 | 5775 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.28 | -30.07 | -92.78 | 2620 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.83 | -30.76 | -95.83 | 3457 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.77 | -99.77 | 6149 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -29.33 | -92.00 | 2328 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -38.25 | -97.72 | 3608 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.61 | -38.32 | -98.61 | 4722 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.17 | -34.33 | -94.49 | 2790 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.25 | -27.26 | -84.44 | 1788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.29 | -99.58 | 6208 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.73 | -23.49 | -87.79 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.38 | -26.92 | -88.50 | 2156 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.16 | -33.86 | -96.17 | 3778 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.47 | -34.15 | -89.64 | 2096 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.13 | -34.50 | -96.15 | 4107 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.80 | -99.91 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T12:15 | VWAP reversion | buy | XRP-USD | 10.20 | — | entry signal |
| 2026-10-22T12:15 | VWAP reversion | sell | ETH-USD | 2.57 | -0.02 | rebalance down |
| 2026-10-22T12:15 | VWAP reversion | sell | BTC-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-22T12:10 | VWAP reversion | buy | ETH-USD | 2.61 | — | rebalance up |
| 2026-10-22T12:10 | VWAP reversion | buy | BTC-USD | 2.58 | — | rebalance up |
| 2026-10-22T12:10 | VWAP reversion | sell | XRP-USD | 10.26 | -0.08 | stop-loss |
| 2026-10-22T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 16.29 | — | entry signal |
| 2026-10-22T11:25 | ROC + volume | sell | SOL-USD | 14.90 | -0.05 | exit signal |
| 2026-10-22T11:10 | EMA 20/50 cross | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-22T11:00 | CCI reversion · 1h | buy | SOL-USD | 20.53 | — | entry signal |
| 2026-10-22T11:00 | CCI reversion · 1h | buy | DOGE-USD | 20.53 | — | entry signal |
| 2026-10-22T11:00 | Williams %R · 1h | buy | SOL-USD | 20.65 | — | entry signal |
| 2026-10-22T11:00 | RSI(14) reversion · 1h | buy | BTC-USD | 20.22 | — | entry signal |
| 2026-10-22T11:00 | EMA 20/50 cross · 1h | sell | ETH-USD | 8.55 | -0.18 | exit signal |
| 2026-10-22T10:55 | Agent (ML meta-label) | sell | XRP-USD | 10.39 | -0.06 | selected signal exited |
| 2026-10-22T10:55 | VWAP reversion | buy | ETH-USD | 2.57 | — | rebalance up |
| 2026-10-22T10:55 | VWAP reversion | sell | BTC-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-22T10:50 | Agent (ML meta-label) | buy | XRP-USD | 10.45 | — | entry |
| 2026-10-22T10:50 | Three white soldiers | sell | SOL-USD | 20.55 | -0.06 | exit signal |
| 2026-10-22T10:47 | Agent (ML meta-label) | sell | XRP-USD | 2.96 | -0.02 | selected signal exited |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 12:15:05.000154+00:00 -> 2026-10-22 12:25:05.000154+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
