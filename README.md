# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T13:45:05.000151+00:00 · 31909 ticks

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

Today: 11064 decisions in 2031 calls, $0.1525 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T13:45 | 0 / 14 / 16 | cash |  |
| Breezy | 2026-10-22T13:45 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-22T13:45 | 4 / 24 / 2 | COIN 59% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.19 | 6.19 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 1.58 | 0.55 | -7.48 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.01 | 4.01 | 18 | 33.3 | 7.46 | 1.88 | -5.96 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.54 | 2.54 | 75 | 48.0 | -8.37 | -2.27 | -13.82 | 135 |
| 6 | Max aggression: 5-day momentum | meta | 102.35 | 2.35 | 10 | 50.0 | -13.76 | -1.02 | -34.64 | 26 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.23 | 0.23 | 0 | — | 3.87 | 1.70 | -5.02 | 1 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.38 | -0.62 | 66 | 36.4 | 3.11 | 1.81 | -2.29 | 67 |
| 11 | Hold SPY | benchmark | 98.72 | -1.28 | 0 | — | 0.16 | 0.13 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 13 | Copy: Congress Democrats (NANC) | copy | 97.64 | -2.36 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 97.20 | -2.80 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.22 | -1.84 | -5.83 | 1 |
| 16 | Copy: Insider buying | copy | 96.83 | -3.17 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 17 | Hold BTC | benchmark | 96.62 | -3.38 | 0 | — | 5.28 | 0.96 | -8.68 | 1 |
| 18 | Agent (rotation) | meta | 95.98 | -4.02 | 117 | 30.8 | -8.77 | -4.88 | -8.79 | 267 |
| 19 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.77 | 0.84 | -7.93 | 8 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 21 | Trend pullback · 1h | trend | 94.61 | -5.39 | 93 | 23.7 | -21.59 | -6.78 | -21.74 | 127 |
| 22 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.26 | 1.96 | -7.38 | 197 |
| 23 | Daily: Momentum burst | daily | 93.94 | -6.06 | 8 | 12.5 | -14.96 | -2.64 | -20.58 | 39 |
| 24 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.29 | -2.90 | -17.26 | 556 |
| 25 | ADX DI cross · 1h | trend | 93.27 | -6.73 | 94 | 19.1 | -13.73 | -2.59 | -15.46 | 262 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 93.06 | -6.94 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 27 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.03 | -3.61 | -19.06 | 103 |
| 28 | Parabolic SAR · 1h | trend | 91.75 | -8.25 | 114 | 25.4 | -17.25 | -3.80 | -19.79 | 268 |
| 29 | Daily: Bullish score | daily | 91.58 | -8.42 | 8 | 0.0 | -4.72 | -0.48 | -13.10 | 13 |
| 30 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.53 | -1.02 | -11.76 | 102 |
| 31 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.49 | -1.98 | -16.91 | 1 |
| 32 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -17.23 | -6.86 | -18.15 | 268 |
| 33 | Bollinger breakout · 1h | breakout | 89.85 | -10.15 | 101 | 28.7 | -11.82 | -2.12 | -15.38 | 258 |
| 34 | Stochastic reversion · 1h | reversion | 89.10 | -10.90 | 174 | 46.0 | -14.93 | -2.46 | -22.24 | 371 |
| 35 | Volume breakout · 1h | breakout | 88.73 | -11.27 | 101 | 22.8 | -12.48 | -2.20 | -14.33 | 106 |
| 36 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.01 | -4.04 | -18.82 | 691 |
| 37 | Supertrend · 1h | trend | 88.27 | -11.72 | 93 | 15.1 | -23.32 | -4.62 | -26.77 | 218 |
| 38 | EMA 20/50 cross · 1h | trend | 87.90 | -12.10 | 67 | 11.9 | -22.99 | -4.14 | -25.14 | 141 |
| 39 | RSI momentum · 1h | momentum | 87.79 | -12.21 | 93 | 17.2 | -19.55 | -3.86 | -21.14 | 218 |
| 40 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -16.56 | -4.55 | -18.79 | 139 |
| 41 | Keltner breakout · 1h | breakout | 86.04 | -13.96 | 71 | 23.9 | -24.23 | -4.87 | -24.75 | 197 |
| 42 | MACD cross · 1h | trend | 85.82 | -14.18 | 204 | 22.1 | -26.17 | -4.97 | -27.34 | 470 |
| 43 | Connors RSI(2) · 1h | reversion | 85.76 | -14.24 | 167 | 40.1 | -25.68 | -7.16 | -25.71 | 202 |
| 44 | Z-score reversion · 1h | reversion | 85.44 | -14.56 | 102 | 34.3 | -12.92 | -2.02 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 85.22 | -14.78 | 64 | 12.5 | -19.49 | -3.64 | -22.25 | 117 |
| 46 | MFI reversion · 1h | reversion | 85.19 | -14.81 | 229 | 33.2 | -16.40 | -2.53 | -21.11 | 142 |
| 47 | Donchian 20/10 · 1h | breakout | 84.20 | -15.80 | 90 | 20.0 | -23.35 | -4.32 | -24.24 | 226 |
| 48 | Triple EMA stack · 1h | trend | 84.09 | -15.91 | 96 | 15.6 | -29.10 | -5.42 | -30.27 | 220 |
| 49 | Williams %R · 1h | reversion | 83.36 | -16.64 | 199 | 44.7 | -30.87 | -4.74 | -36.55 | 517 |
| 50 | MACD zero-line · 1h | trend | 82.95 | -17.05 | 96 | 14.6 | -24.41 | -4.71 | -25.37 | 227 |
| 51 | OBV trend · 1h | momentum | 82.64 | -17.36 | 194 | 18.0 | -32.12 | -6.17 | -32.78 | 308 |
| 52 | Agent (ML meta-label) | meta | 82.63 | -17.37 | 754 | 19.6 | -13.09 | -2.39 | -18.25 | 353 |
| 53 | Three white soldiers | momentum | 82.32 | -17.68 | 261 | 20.3 | -44.71 | -17.87 | -45.37 | 600 |
| 54 | CCI reversion · 1h | reversion | 81.87 | -18.14 | 188 | 43.6 | -20.70 | -2.70 | -27.44 | 439 |
| 55 | Bollinger reversion · 1h | reversion | 81.72 | -18.28 | 164 | 36.0 | -29.97 | -5.81 | -32.82 | 352 |
| 56 | ROC + volume · 1h | momentum | 80.49 | -19.51 | 227 | 24.7 | -26.81 | -4.85 | -26.95 | 374 |
| 57 | Heikin-Ashi · 1h | trend | 80.16 | -19.84 | 258 | 23.6 | -45.25 | -9.38 | -46.34 | 676 |
| 58 | RSI(14) reversion · 1h | reversion | 79.46 | -20.54 | 86 | 24.4 | -19.39 | -3.70 | -23.28 | 174 |
| 59 | Candlestick reversal · 1h | reversion | 79.29 | -20.71 | 233 | 30.0 | -36.98 | -6.38 | -40.06 | 545 |
| 60 | EMA 9/21 cross · 1h | trend | 78.86 | -21.14 | 152 | 11.8 | -29.47 | -5.67 | -30.56 | 336 |
| 61 | VWAP momentum · 1h | momentum | 77.00 | -23.00 | 492 | 21.7 | -51.81 | -10.51 | -53.07 | 1250 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -42.15 | -2.75 | -46.89 | 43 |
| 63 | ROC + volume | momentum | 59.66 | -40.34 | 680 | 23.4 | -77.73 | -21.66 | -78.98 | 1698 |
| 64 | Volume breakout | breakout | 58.65 | -41.35 | 404 | 13.6 | -64.52 | -19.67 | -65.24 | 862 |
| 65 | Donchian 55/20 | breakout | 56.12 | -43.88 | 536 | 19.8 | -71.86 | -18.76 | -74.04 | 1276 |
| 66 | Squeeze breakout | breakout | 55.67 | -44.33 | 526 | 14.1 | -67.29 | -23.08 | -68.22 | 1205 |
| 67 | EMA 20/50 cross | trend | 54.92 | -45.08 | 577 | 20.5 | -78.97 | -20.08 | -80.27 | 1444 |
| 68 | RSI(14) reversion | reversion | 53.57 | -46.43 | 790 | 26.3 | -75.82 | -16.88 | -76.19 | 1641 |
| 69 | VWAP reversion | reversion | 51.43 | -48.56 | 789 | 25.2 | -72.64 | -14.54 | -73.06 | 1484 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.79 | -31.05 | -98.85 | 5273 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.81 | -32.19 | -94.24 | 2576 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.86 | -23.06 | -88.81 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.18 | -27.50 | -91.80 | 2355 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.10 | -25.25 | -91.19 | 2235 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -34.17 | -97.86 | 3505 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -35.83 | -96.98 | 3576 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.51 | -28.26 | -94.51 | 2556 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.83 | -27.05 | -83.41 | 1722 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.51 | -99.47 | 5800 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.31 | -29.83 | -92.87 | 2623 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.77 | -30.63 | -95.78 | 3453 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.61 | -99.78 | 6160 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -29.76 | -92.03 | 2335 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -37.81 | -97.73 | 3604 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -38.33 | -98.62 | 4727 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.22 | -34.57 | -94.55 | 2795 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.32 | -27.26 | -84.47 | 1790 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.16 | -99.58 | 6208 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.76 | -23.50 | -87.80 | 2172 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.42 | -26.95 | -88.52 | 2159 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.18 | -33.88 | -96.19 | 3783 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.52 | -34.11 | -89.73 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.14 | -34.50 | -96.16 | 4112 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.53 | -99.91 | 8270 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T13:45 | Day trade: Stocks in Play ORB | buy | MSTR | 24.85 | — | entry |
| 2026-10-22T13:45 | Day trade: Stocks in Play ORB | sell | COIN | 24.92 | 0.10 | target is flat |
| 2026-10-22T13:45 | Agent (ML meta-label) | buy | ETHU | 11.81 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-22T13:45 | Agent (ML meta-label) | sell | IWM | 7.70 | -0.03 | selected signal exited |
| 2026-10-22T13:45 | Bollinger breakout · 1h | sell | NVDA | 22.42 | -0.09 | stop-loss |
| 2026-10-22T13:45 | RSI momentum · 1h | sell | AMZN | 10.81 | -0.22 | stop-loss |
| 2026-10-22T13:45 | VWAP momentum · 1h | buy | PLTR | 5.30 | — | rebalance up |
| 2026-10-22T13:45 | VWAP momentum · 1h | buy | MSTR | 5.41 | — | rebalance up |
| 2026-10-22T13:45 | VWAP momentum · 1h | sell | TQQQ | 7.69 | -0.12 | stop-loss |
| 2026-10-22T13:45 | VWAP momentum · 1h | sell | SPY | 7.70 | -0.03 | stop-loss |
| 2026-10-22T13:45 | MACD zero-line · 1h | buy | NVDA | 4.40 | — | rebalance up |
| 2026-10-22T13:45 | MACD zero-line · 1h | buy | LABU | 4.36 | — | rebalance up |
| 2026-10-22T13:45 | MACD zero-line · 1h | buy | BITX | 4.76 | — | rebalance up |
| 2026-10-22T13:45 | MACD zero-line · 1h | buy | AAPL | 4.28 | — | rebalance up |
| 2026-10-22T13:45 | MACD zero-line · 1h | sell | SPY | 8.41 | -0.06 | stop-loss |
| 2026-10-22T13:40 | Day trade: Stocks in Play ORB | buy | TSLA | 24.81 | — | entry |
| 2026-10-22T13:40 | Day trade: Stocks in Play ORB | buy | COIN | 24.81 | — | entry |
| 2026-10-22T13:40 | Agent (ML meta-label) | buy | UPRO | 4.26 | — | rebalance up |
| 2026-10-22T13:40 | Agent (ML meta-label) | buy | TNA | 4.20 | — | rebalance up |
| 2026-10-22T13:40 | Agent (ML meta-label) | buy | LABU | 4.16 | — | rebalance up |
| 2026-10-22T13:40 | Agent (ML meta-label) | sell | AMZN | 9.19 | -0.24 | selected signal exited |
| 2026-10-22T13:40 | Candlestick reversal · 1h | sell | GOOGL | 19.52 | -0.23 | stop-loss |
| 2026-10-22T13:40 | Volume breakout · 1h | sell | TSLA | 22.26 | -0.10 | target is flat |
| 2026-10-22T13:40 | Donchian 20/10 · 1h | sell | BITX | 13.83 | -0.35 | stop-loss |
| 2026-10-22T13:40 | ROC + volume · 1h | sell | PLTR | 20.19 | 0.19 | target is flat |
| 2026-10-22T13:40 | VWAP momentum · 1h | sell | UPRO | 7.70 | -0.05 | stop-loss |
| 2026-10-22T13:40 | ADX DI cross · 1h | buy | SQQQ | 9.33 | — | entry |
| 2026-10-22T13:40 | ADX DI cross · 1h | buy | NVDA | 5.99 | — | rebalance up |
| 2026-10-22T13:40 | ADX DI cross · 1h | sell | ETHU | 9.00 | -0.46 | stop-loss |
| 2026-10-22T13:40 | ADX DI cross · 1h | sell | BITX | 9.11 | -0.35 | stop-loss |
| 2026-10-22T13:40 | MACD zero-line · 1h | sell | MSTR | 5.74 | -0.26 | stop-loss |
| 2026-10-22T13:40 | EMA 9/21 cross · 1h | buy | PLTR | 5.01 | — | rebalance up |
| 2026-10-22T13:40 | EMA 9/21 cross · 1h | buy | LABU | 4.02 | — | rebalance up |
| 2026-10-22T13:40 | EMA 9/21 cross · 1h | sell | UPRO | 6.06 | -0.01 | stop-loss |
| 2026-10-22T13:40 | EMA 9/21 cross · 1h | sell | BITX | 4.69 | -0.18 | stop-loss |
| 2026-10-22T13:40 | EMA 9/21 cross · 1h | sell | AMZN | 4.16 | -0.13 | stop-loss |
| 2026-10-22T13:40 | RSI(14) reversion | buy | TSLA | 13.40 | — | entry signal |
| 2026-10-22T13:40 | RSI(14) reversion | buy | LABU | 13.40 | — | entry signal |
| 2026-10-22T13:40 | Volume breakout | sell | XRP-USD | 11.71 | -0.12 | stop-loss |
| 2026-10-22T13:40 | Volume breakout | sell | ETH-USD | 11.71 | -0.12 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 13:45:05.000151+00:00 -> 2026-10-22 13:55:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
