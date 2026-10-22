# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T13:15:05.000145+00:00 · 31887 ticks

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

Today: 9825 decisions in 1965 calls, $0.1377 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T13:15 | 1 / 1 / 3 | cash |  |
| Breezy | 2026-10-22T13:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T13:15 | 0 / 5 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.20 | 6.20 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.11 | 2.11 | 75 | 48.0 | -8.76 | -2.38 | -13.79 | 135 |
| 6 | Max aggression: 5-day momentum | meta | 101.67 | 1.67 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.39 | 0.39 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.78 | -0.22 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.56 | -0.44 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.65 | -2.35 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.21 | -2.79 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Insider buying | copy | 96.84 | -3.16 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 18 | Hold BTC | benchmark | 96.48 | -3.52 | 0 | — | 6.02 | 1.06 | -8.68 | 1 |
| 19 | Agent (rotation) | meta | 95.83 | -4.17 | 117 | 30.8 | -8.74 | -5.13 | -8.79 | 235 |
| 20 | ADX DI cross · 1h | trend | 95.61 | -4.39 | 92 | 19.6 | -11.67 | -2.14 | -16.14 | 261 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 22 | Daily: Momentum burst | daily | 95.08 | -4.92 | 6 | 16.7 | -9.30 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.94 | -5.06 | 92 | 23.9 | -20.36 | -6.34 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.56 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.95 | -6.05 | 46 | 17.4 | -16.33 | -3.34 | -17.38 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 93.07 | -6.93 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.88 | -7.12 | 113 | 25.7 | -15.71 | -3.45 | -19.79 | 268 |
| 29 | Squeeze breakout · 1h | breakout | 92.52 | -7.48 | 50 | 24.0 | -3.00 | -0.66 | -11.48 | 101 |
| 30 | Daily: Bullish score | daily | 92.31 | -7.69 | 8 | 0.0 | -2.44 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.11 | -7.89 | 93 | 30.1 | -8.40 | -1.50 | -14.43 | 258 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -16.65 | -6.60 | -17.51 | 273 |
| 34 | Volume breakout · 1h | breakout | 90.46 | -9.54 | 95 | 24.2 | -10.83 | -1.90 | -12.46 | 106 |
| 35 | Supertrend · 1h | trend | 89.75 | -10.25 | 93 | 15.1 | -21.15 | -4.23 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.21 | -10.79 | 89 | 18.0 | -18.06 | -3.61 | -20.65 | 219 |
| 37 | EMA 20/50 cross · 1h | trend | 88.39 | -11.61 | 64 | 12.5 | -21.77 | -3.78 | -23.52 | 141 |
| 38 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 39 | Stochastic reversion · 1h | reversion | 88.22 | -11.78 | 174 | 46.0 | -15.46 | -2.55 | -22.24 | 371 |
| 40 | Keltner breakout · 1h | breakout | 87.75 | -12.25 | 67 | 23.9 | -20.72 | -4.03 | -22.53 | 199 |
| 41 | MACD cross · 1h | trend | 87.56 | -12.45 | 202 | 22.3 | -24.39 | -4.63 | -27.05 | 468 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.13 | -4.87 | -21.02 | 130 |
| 43 | Z-score reversion · 1h | reversion | 86.86 | -13.14 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.63 | -13.37 | 61 | 13.1 | -17.69 | -3.31 | -20.25 | 117 |
| 45 | Connors RSI(2) · 1h | reversion | 85.73 | -14.27 | 167 | 40.1 | -25.66 | -7.14 | -25.66 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.49 | -14.51 | 87 | 20.7 | -20.77 | -3.89 | -23.55 | 226 |
| 47 | Triple EMA stack · 1h | trend | 85.27 | -14.73 | 94 | 16.0 | -26.58 | -4.89 | -27.82 | 221 |
| 48 | MFI reversion · 1h | reversion | 85.12 | -14.88 | 229 | 33.2 | -13.81 | -2.06 | -21.11 | 143 |
| 49 | MACD zero-line · 1h | trend | 84.66 | -15.34 | 92 | 15.2 | -24.00 | -4.61 | -26.48 | 229 |
| 50 | OBV trend · 1h | momentum | 83.60 | -16.40 | 191 | 18.3 | -30.97 | -5.82 | -31.44 | 306 |
| 51 | Agent (ML meta-label) | meta | 83.47 | -16.53 | 752 | 19.7 | -10.13 | -1.97 | -16.51 | 354 |
| 52 | ROC + volume · 1h | momentum | 82.88 | -17.12 | 218 | 23.9 | -24.85 | -4.47 | -26.88 | 380 |
| 53 | Williams %R · 1h | reversion | 82.57 | -17.43 | 199 | 44.7 | -31.61 | -4.90 | -36.62 | 518 |
| 54 | Three white soldiers | momentum | 82.37 | -17.63 | 260 | 20.4 | -44.74 | -17.90 | -45.37 | 601 |
| 55 | CCI reversion · 1h | reversion | 82.07 | -17.93 | 188 | 43.6 | -20.45 | -2.66 | -27.44 | 439 |
| 56 | Bollinger reversion · 1h | reversion | 81.79 | -18.21 | 164 | 36.0 | -29.95 | -5.81 | -32.84 | 352 |
| 57 | Heikin-Ashi · 1h | trend | 81.38 | -18.62 | 252 | 23.8 | -44.27 | -9.01 | -46.39 | 676 |
| 58 | EMA 9/21 cross · 1h | trend | 80.86 | -19.14 | 145 | 11.7 | -26.54 | -5.13 | -29.94 | 331 |
| 59 | RSI(14) reversion · 1h | reversion | 80.79 | -19.21 | 85 | 24.7 | -17.78 | -3.08 | -24.99 | 175 |
| 60 | Candlestick reversal · 1h | reversion | 79.14 | -20.86 | 231 | 30.3 | -38.94 | -7.17 | -41.74 | 544 |
| 61 | VWAP momentum · 1h | momentum | 79.08 | -20.92 | 483 | 22.2 | -49.72 | -10.08 | -51.99 | 1249 |
| 62 | Max aggression: 1-day momentum | meta | 77.26 | -22.74 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.75 | -40.25 | 680 | 23.4 | -77.59 | -21.35 | -78.97 | 1696 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.20 | -19.37 | -64.95 | 857 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -71.70 | -18.61 | -74.04 | 1273 |
| 66 | Squeeze breakout | breakout | 56.05 | -43.95 | 524 | 14.1 | -67.03 | -22.73 | -67.99 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.04 | -44.96 | 577 | 20.5 | -79.05 | -19.96 | -80.44 | 1434 |
| 68 | RSI(14) reversion | reversion | 53.55 | -46.45 | 789 | 26.2 | -76.01 | -17.06 | -76.19 | 1636 |
| 69 | VWAP reversion | reversion | 51.23 | -48.77 | 789 | 25.2 | -72.60 | -14.42 | -73.06 | 1491 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.80 | -31.18 | -98.85 | 5284 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -32.42 | -94.27 | 2576 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.81 | -22.94 | -88.77 | 1891 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.13 | -27.29 | -91.75 | 2353 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.12 | -25.30 | -91.21 | 2247 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -34.54 | -97.85 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -35.98 | -97.00 | 3592 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -28.14 | -94.47 | 2545 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.84 | -27.05 | -83.42 | 1722 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -37.83 | -99.47 | 5779 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.30 | -30.13 | -92.80 | 2621 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.78 | -30.68 | -95.78 | 3453 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.77 | -99.77 | 6151 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -29.62 | -92.00 | 2330 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -37.89 | -97.72 | 3604 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.61 | -38.34 | -98.61 | 4722 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.19 | -34.47 | -94.50 | 2791 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.24 | -27.24 | -84.44 | 1788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.22 | -99.58 | 6204 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.73 | -23.49 | -87.79 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.41 | -26.91 | -88.52 | 2154 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.16 | -33.85 | -96.18 | 3778 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.49 | -34.21 | -89.66 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.15 | -34.49 | -96.16 | 4109 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.61 | -99.91 | 8273 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T13:15 | VWAP reversion | buy | XRP-USD | 12.82 | — | entry signal |
| 2026-10-22T13:15 | VWAP reversion | sell | BTC-USD | 10.24 | -0.07 | stop-loss |
| 2026-10-22T13:10 | Stochastic reversion · 1h | buy | BTC-USD | 14.64 | — | entry |
| 2026-10-22T13:10 | Stochastic reversion · 1h | sell | XRP-USD | 14.64 | -0.14 | stop-loss |
| 2026-10-22T13:10 | Connors RSI(2) · 1h | sell | XRP-USD | 21.42 | -0.54 | stop-loss |
| 2026-10-22T13:10 | VWAP reversion | sell | XRP-USD | 10.11 | -0.09 | stop-loss |
| 2026-10-22T13:10 | EMA 20/50 cross | sell | DOGE-USD | 13.67 | -0.12 | stop-loss |
| 2026-10-22T13:00 | VWAP reversion · 1h | buy | ETH-USD | 10.32 | — | entry signal |
| 2026-10-22T13:00 | VWAP reversion · 1h | sell | SOL-USD | 5.15 | -0.01 | rebalance down |
| 2026-10-22T13:00 | VWAP reversion · 1h | sell | DOGE-USD | 5.17 | -0.01 | rebalance down |
| 2026-10-22T13:00 | Heikin-Ashi · 1h | sell | SOL-USD | 16.20 | -0.09 | exit signal |
| 2026-10-22T12:55 | Agent (ML meta-label) | sell | XRP-USD | 10.37 | -0.07 | selected signal exited |
| 2026-10-22T12:55 | Squeeze breakout | sell | DOGE-USD | 13.94 | -0.10 | exit signal |
| 2026-10-22T12:45 | Agent (ML meta-label) | buy | XRP-USD | 10.44 | — | entry |
| 2026-10-22T12:45 | EMA 20/50 cross | buy | DOGE-USD | 13.79 | — | entry signal |
| 2026-10-22T12:40 | Agent (ML meta-label) | sell | XRP-USD | 10.37 | -0.09 | selected signal exited |
| 2026-10-22T12:30 | Agent (ML meta-label) | buy | XRP-USD | 10.45 | — | entry |
| 2026-10-22T12:26 | Squeeze breakout | buy | DOGE-USD | 14.04 | — | entry signal |
| 2026-10-22T12:20 | EMA 20/50 cross | sell | SOL-USD | 13.73 | -0.08 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 13:15:05.000145+00:00 -> 2026-10-22 13:25:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
