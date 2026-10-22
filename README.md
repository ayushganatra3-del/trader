# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T05:20:05.000158+00:00 · 31491 ticks

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

Today: 3885 decisions in 777 calls, $0.0544 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T05:20 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-22T05:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T05:20 | 2 / 3 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.00 | 6.00 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.47 | 1.47 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.20 | 0.20 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.59 | -0.41 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.37 | -0.63 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Hold BTC | benchmark | 97.80 | -2.20 | 0 | — | 9.78 | 1.59 | -8.68 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 97.46 | -2.54 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.03 | -2.98 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.65 | -3.35 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 21 | ADX DI cross · 1h | trend | 95.44 | -4.56 | 92 | 19.6 | -9.89 | -1.79 | -16.14 | 257 |
| 22 | Daily: Momentum burst | daily | 94.89 | -5.11 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.84 | -5.16 | 92 | 23.9 | -20.41 | -6.36 | -20.58 | 129 |
| 24 | Donchian 55/20 · 1h | breakout | 94.48 | -5.52 | 44 | 18.2 | -15.84 | -3.24 | -17.04 | 103 |
| 25 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.89 | -7.11 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.80 | -7.20 | 113 | 25.7 | -16.62 | -3.68 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.49 | -7.51 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.16 | -7.84 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 91.99 | -8.01 | 93 | 30.1 | -9.96 | -1.80 | -14.57 | 261 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -16.67 | -6.28 | -20.74 | 261 |
| 34 | Volume breakout · 1h | breakout | 90.35 | -9.65 | 95 | 24.2 | -14.07 | -2.45 | -14.11 | 109 |
| 35 | Supertrend · 1h | trend | 89.62 | -10.38 | 93 | 15.1 | -21.15 | -4.23 | -26.66 | 218 |
| 36 | Stochastic reversion · 1h | reversion | 89.23 | -10.77 | 169 | 47.3 | -13.97 | -2.29 | -22.24 | 368 |
| 37 | RSI momentum · 1h | momentum | 89.09 | -10.91 | 89 | 18.0 | -18.37 | -3.68 | -20.65 | 219 |
| 38 | EMA 20/50 cross · 1h | trend | 88.49 | -11.51 | 62 | 12.9 | -21.45 | -3.70 | -23.57 | 142 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.66 | -12.34 | 67 | 23.9 | -20.11 | -3.87 | -22.65 | 200 |
| 41 | MACD cross · 1h | trend | 87.42 | -12.58 | 202 | 22.3 | -23.77 | -4.50 | -26.95 | 467 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -16.29 | -4.44 | -20.40 | 133 |
| 43 | Connors RSI(2) · 1h | reversion | 87.31 | -12.69 | 163 | 41.1 | -24.24 | -7.15 | -24.33 | 202 |
| 44 | Z-score reversion · 1h | reversion | 86.77 | -13.22 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.49 | -13.51 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.39 | -14.61 | 87 | 20.7 | -23.70 | -4.39 | -28.87 | 229 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 48 | Triple EMA stack · 1h | trend | 85.15 | -14.85 | 94 | 16.0 | -26.59 | -4.89 | -27.70 | 221 |
| 49 | MACD zero-line · 1h | trend | 84.49 | -15.51 | 92 | 15.2 | -23.42 | -4.56 | -26.06 | 228 |
| 50 | Agent (ML meta-label) | meta | 84.46 | -15.54 | 736 | 20.1 | -12.62 | -2.39 | -15.94 | 365 |
| 51 | OBV trend · 1h | momentum | 83.55 | -16.45 | 190 | 18.4 | -30.58 | -5.73 | -31.52 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.75 | -17.25 | 218 | 23.9 | -28.46 | -5.00 | -32.98 | 387 |
| 53 | Williams %R · 1h | reversion | 82.58 | -17.42 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Bollinger reversion · 1h | reversion | 82.46 | -17.54 | 163 | 36.2 | -29.20 | -5.64 | -32.84 | 349 |
| 55 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.32 | -18.08 | -46.47 | 603 |
| 56 | CCI reversion · 1h | reversion | 82.11 | -17.89 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.40 | -18.61 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.87 | -19.13 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.72 | -19.28 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 78.99 | -21.01 | 231 | 30.3 | -38.54 | -7.06 | -41.81 | 543 |
| 61 | VWAP momentum · 1h | momentum | 78.96 | -21.04 | 483 | 22.2 | -48.57 | -9.74 | -52.95 | 1253 |
| 62 | Max aggression: 1-day momentum | meta | 77.11 | -22.89 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.77 | -21.83 | -78.97 | 1710 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.22 | -19.41 | -64.95 | 861 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.25 | -19.51 | -74.04 | 1277 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -66.90 | -22.49 | -67.93 | 1203 |
| 67 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.93 | -19.36 | -80.87 | 1438 |
| 68 | RSI(14) reversion | reversion | 55.13 | -44.87 | 774 | 26.7 | -75.28 | -17.02 | -75.45 | 1628 |
| 69 | VWAP reversion | reversion | 53.58 | -46.42 | 768 | 25.9 | -71.20 | -14.28 | -72.15 | 1471 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -32.24 | -98.87 | 5306 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.20 | -34.71 | -94.26 | 2593 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.97 | -23.58 | -88.71 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.36 | -28.57 | -91.74 | 2360 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.19 | -25.48 | -91.26 | 2261 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.76 | -35.44 | -97.82 | 3507 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.95 | -37.85 | -96.98 | 3596 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.66 | -28.61 | -94.70 | 2562 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.21 | -28.18 | -83.41 | 1729 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -37.54 | -99.43 | 5751 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.28 | -30.24 | -92.71 | 2625 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.88 | -31.01 | -95.88 | 3470 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.21 | -99.77 | 6154 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -30.55 | -91.92 | 2336 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -39.28 | -97.77 | 3621 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.55 | -37.64 | -98.56 | 4712 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.24 | -35.22 | -94.46 | 2797 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.44 | -27.99 | -84.44 | 1796 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.57 | -40.31 | -99.57 | 6203 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.41 | -23.20 | -87.49 | 2160 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.06 | -88.22 | 2146 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.09 | -33.65 | -96.09 | 3773 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -33.96 | -89.56 | 2097 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.02 | -34.45 | -96.04 | 4100 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.35 | -99.91 | 8294 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T05:05 | RSI(14) reversion | buy | DOGE-USD | 2.78 | — | rebalance up |
| 2026-10-22T05:05 | RSI(14) reversion | buy | BTC-USD | 8.23 | — | rebalance up |
| 2026-10-22T05:05 | RSI(14) reversion | sell | XRP-USD | 13.74 | -0.00 | exit signal |
| 2026-10-22T04:55 | VWAP reversion | buy | DOGE-USD | 2.68 | — | rebalance up |
| 2026-10-22T04:55 | VWAP reversion | sell | XRP-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-22T04:50 | VWAP reversion | buy | DOGE-USD | 2.73 | — | entry |
| 2026-10-22T04:50 | VWAP reversion | sell | ETH-USD | 2.73 | -0.02 | rebalance down |
| 2026-10-22T04:05 | Agent (ML meta-label) | buy | XRP-USD | 6.85 | — | rebalance up |
| 2026-10-22T04:05 | Agent (ML meta-label) | sell | SOL-USD | 6.85 | -0.04 | selected signal exited |
| 2026-10-22T04:00 | Agent (ML meta-label) | buy | XRP-USD | 2.79 | — | entry |
| 2026-10-22T04:00 | Agent (ML meta-label) | buy | SOL-USD | 6.89 | — | entry |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | SOL-USD | 6.26 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | ETH-USD | 12.78 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | BTC-USD | 12.78 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | sell | DOGE-USD | 9.48 | -0.07 | rebalance down |
| 2026-10-22T04:00 | Bollinger reversion · 1h | buy | SOL-USD | 20.65 | — | entry signal |
| 2026-10-22T04:00 | Connors RSI(2) · 1h | buy | SOL-USD | 21.82 | — | entry signal |
| 2026-10-22T04:00 | Triple EMA stack · 1h | sell | BTC-USD | 11.99 | -0.08 | exit signal |
| 2026-10-22T04:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 4.19 | -0.04 | exit signal |
| 2026-10-22T03:45 | RSI(14) reversion | buy | BTC-USD | 5.61 | — | entry signal |
| 2026-10-22T03:45 | RSI(14) reversion | sell | ETH-USD | 2.82 | -0.02 | rebalance down |
| 2026-10-22T03:45 | RSI(14) reversion | sell | DOGE-USD | 2.80 | -0.02 | rebalance down |
| 2026-10-22T03:40 | RSI(14) reversion | buy | XRP-USD | 13.74 | — | entry signal |
| 2026-10-22T03:40 | RSI(14) reversion | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-22T03:35 | Connors RSI(2) · 1h | sell | SOL-USD | 17.46 | -0.44 | stop-loss |
| 2026-10-22T03:35 | RSI(14) reversion | sell | XRP-USD | 13.74 | -0.18 | stop-loss |
| 2026-10-22T03:35 | RSI(14) reversion | sell | SOL-USD | 13.76 | -0.19 | stop-loss |
| 2026-10-22T03:00 | Agent (ML meta-label) | buy | DOGE-USD | 8.47 | — | entry |
| 2026-10-22T03:00 | Stochastic reversion · 1h | buy | DOGE-USD | 22.39 | — | entry signal |
| 2026-10-22T03:00 | Connors RSI(2) · 1h | buy | XRP-USD | 21.95 | — | entry signal |
| 2026-10-22T03:00 | Connors RSI(2) · 1h | buy | ETH-USD | 21.95 | — | entry signal |
| 2026-10-22T03:00 | Donchian 55/20 · 1h | buy | XRP-USD | 4.82 | — | rebalance up |
| 2026-10-22T03:00 | Donchian 55/20 · 1h | buy | BTC-USD | 4.87 | — | rebalance up |
| 2026-10-22T03:00 | Donchian 55/20 · 1h | sell | SOL-USD | 18.80 | -0.21 | exit signal |
| 2026-10-22T03:00 | OBV trend · 1h | sell | SOL-USD | 7.46 | -0.11 | exit signal |
| 2026-10-22T03:00 | Supertrend · 1h | sell | SOL-USD | 5.78 | -0.03 | exit signal |
| 2026-10-22T03:00 | Triple EMA stack · 1h | sell | ETH-USD | 11.95 | -0.06 | exit signal |
| 2026-10-22T03:00 | RSI(14) reversion | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-22T03:00 | RSI(14) reversion | buy | ETH-USD | 13.93 | — | entry signal |
| 2026-10-22T03:00 | RSI(14) reversion | buy | DOGE-USD | 13.93 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 05:20:05.000158+00:00 -> 2026-10-22 05:30:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
