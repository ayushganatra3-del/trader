# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T16:15:05.000115+00:00 · 33242 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.46 (-10.54%)

Closed trades 100, win rate 39.0%, fees £3.18, max drawdown -10.95%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 22605 decisions in 2493 calls, $0.2877 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T16:15 | 1 / 8 / 21 | cash |  |
| Breezy | 2026-10-23T16:15 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-23T16:15 | 2 / 25 / 3 | MSTR 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| Stochastic reversion | BITX | 1.69 | +8.43% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.85 | 6.85 | 0 | — | 8.42 | 4.50 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.85 | 3.85 | 17 | 47.1 | 6.57 | 2.19 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.53 | -3.20 | -13.74 | 153 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.61 | 0.61 | 0 | — | 3.31 | 1.56 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.37 | -0.63 | 72 | 33.3 | 5.54 | 2.71 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 98.08 | -1.92 | 0 | — | -0.39 | -0.19 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.33 | -3.67 | 0 | — | 1.40 | 0.41 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.16 | -3.84 | 119 | 31.1 | -2.23 | -1.31 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.90 | -4.10 | 0 | — | -0.59 | -0.19 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.42 | -5.58 | 0 | — | -6.56 | -2.78 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.18 | -5.82 | 25 | 40.0 | -14.75 | -2.82 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.71 | -6.29 | 95 | 23.2 | -21.57 | -7.09 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.69 | -6.31 | 238 | 35.3 | -10.42 | -3.24 | -17.21 | 560 |
| 23 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -14.41 | -1.32 | -27.80 | 24 |
| 24 | Donchian 55/20 · 1h | breakout | 92.83 | -7.17 | 48 | 16.7 | -16.36 | -3.72 | -17.44 | 98 |
| 25 | Daily: Momentum burst | daily | 91.84 | -8.16 | 10 | 10.0 | -17.32 | -3.36 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.78 | -8.22 | 117 | 25.6 | -21.15 | -5.02 | -24.17 | 254 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.90 | -9.10 | 108 | 18.5 | -11.91 | -2.45 | -14.53 | 255 |
| 30 | Agent | meta | 89.46 | -10.54 | 100 | 39.0 | -10.80 | -7.53 | -11.52 | 204 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 32 | Daily: Bullish score | daily | 89.36 | -10.64 | 9 | 0.0 | -8.15 | -1.06 | -14.40 | 14 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.19 | -10.81 | 0 | — | -5.20 | -0.75 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.72 | -11.28 | 105 | 27.6 | -12.51 | -2.49 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.79 | -12.21 | 186 | 45.2 | -19.71 | -3.72 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | Opening range 15m | breakout | 86.63 | -13.37 | 305 | 30.2 | -15.40 | -4.48 | -17.87 | 702 |
| 38 | EMA 20/50 cross · 1h | trend | 86.31 | -13.69 | 71 | 11.3 | -22.66 | -4.54 | -25.11 | 138 |
| 39 | Keltner breakout · 1h | breakout | 86.02 | -13.98 | 73 | 23.3 | -22.94 | -4.89 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 85.89 | -14.11 | 108 | 14.8 | -23.84 | -5.04 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.29 | -14.71 | 101 | 15.8 | -21.74 | -4.67 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.19 | -14.81 | 172 | 40.1 | -26.46 | -8.12 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 84.91 | -15.09 | 216 | 23.1 | -22.75 | -4.56 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 84.20 | -15.80 | 106 | 34.0 | -14.44 | -2.43 | -21.48 | 197 |
| 45 | Triple EMA stack · 1h | trend | 83.78 | -16.22 | 98 | 15.3 | -25.92 | -5.20 | -28.44 | 210 |
| 46 | Ichimoku · 1h | trend | 83.63 | -16.37 | 65 | 12.3 | -23.95 | -5.01 | -25.68 | 110 |
| 47 | MFI reversion · 1h | reversion | 82.26 | -17.75 | 257 | 31.9 | -17.56 | -2.88 | -20.54 | 142 |
| 48 | MACD zero-line · 1h | trend | 82.13 | -17.87 | 103 | 15.5 | -21.16 | -4.43 | -24.81 | 217 |
| 49 | Williams %R · 1h | reversion | 81.42 | -18.57 | 213 | 44.1 | -35.05 | -6.29 | -36.69 | 522 |
| 50 | Three white soldiers | momentum | 81.33 | -18.67 | 274 | 20.1 | -43.50 | -21.10 | -43.62 | 588 |
| 51 | OBV trend · 1h | momentum | 81.23 | -18.77 | 201 | 17.4 | -31.98 | -7.07 | -33.61 | 304 |
| 52 | Donchian 20/10 · 1h | breakout | 81.20 | -18.80 | 96 | 19.8 | -24.51 | -4.78 | -27.45 | 217 |
| 53 | Bollinger reversion · 1h | reversion | 80.69 | -19.31 | 171 | 34.5 | -30.67 | -6.38 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.48 | -19.52 | 198 | 42.9 | -26.15 | -3.93 | -28.17 | 448 |
| 55 | Agent (ML meta-label) | meta | 80.18 | -19.82 | 846 | 18.8 | -11.92 | -2.12 | -16.80 | 378 |
| 56 | Heikin-Ashi · 1h | trend | 79.61 | -20.39 | 264 | 23.5 | -42.52 | -9.95 | -43.38 | 646 |
| 57 | RSI(14) reversion · 1h | reversion | 78.20 | -21.80 | 91 | 23.1 | -14.72 | -2.71 | -23.51 | 186 |
| 58 | ROC + volume · 1h | momentum | 78.08 | -21.92 | 239 | 23.8 | -30.99 | -6.23 | -32.05 | 380 |
| 59 | Candlestick reversal · 1h | reversion | 77.85 | -22.15 | 252 | 29.0 | -34.48 | -6.51 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.41 | -22.59 | 158 | 12.0 | -29.85 | -6.14 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 76.33 | -23.67 | 504 | 21.6 | -49.91 | -11.64 | -50.22 | 1207 |
| 62 | Max aggression: 1-day momentum | meta | 66.49 | -33.51 | 18 | 27.8 | -43.20 | -3.05 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.74 | -42.26 | 703 | 22.8 | -75.20 | -27.70 | -75.20 | 1545 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.79 | -26.33 | -60.79 | 760 |
| 65 | Squeeze breakout | breakout | 53.99 | -46.01 | 546 | 14.3 | -65.98 | -28.80 | -66.19 | 1138 |
| 66 | Donchian 55/20 | breakout | 53.60 | -46.40 | 558 | 19.4 | -71.27 | -23.92 | -71.45 | 1250 |
| 67 | RSI(14) reversion | reversion | 53.20 | -46.80 | 819 | 26.4 | -76.46 | -19.69 | -76.81 | 1664 |
| 68 | EMA 20/50 cross | trend | 52.26 | -47.74 | 606 | 20.3 | -78.64 | -23.90 | -78.97 | 1403 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.25 | -98.67 | 4997 |
| 70 | VWAP reversion | reversion | 50.55 | -49.45 | 813 | 25.0 | -74.62 | -17.59 | -74.79 | 1542 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.67 | -48.27 | -93.72 | 2495 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.27 | -30.19 | -88.50 | 1871 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.03 | -38.38 | -91.13 | 2299 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.29 | -31.57 | -90.32 | 2139 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.58 | -54.35 | -97.62 | 3424 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.92 | -62.64 | -95.94 | 3312 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.56 | -93.75 | 2425 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.48 | -36.48 | -82.52 | 1666 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -54.63 | -99.31 | 5628 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -42.13 | -92.20 | 2567 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.27 | -40.60 | -95.27 | 3344 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -85.00 | -99.74 | 6044 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -46.07 | -91.85 | 2294 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -66.44 | -97.48 | 3498 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.43 | -58.99 | -98.45 | 4676 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.12 | -60.18 | -94.15 | 2719 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.54 | -40.01 | -83.62 | 1766 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -65.59 | -99.52 | 6114 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.48 | -28.68 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -89.99 | -37.81 | -90.10 | 2224 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -47.15 | -95.87 | 3715 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -50.35 | -89.33 | 2075 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.99 | -47.89 | -96.06 | 4083 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -112.16 | -99.90 | 8091 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T16:15 | MFI reversion · 1h | sell | LABU | 20.78 | 0.22 | target is flat |
| 2026-10-23T16:15 | Squeeze breakout | sell | TECL | 13.64 | 0.14 | exit signal |
| 2026-10-23T16:10 | Agent (ML meta-label) | buy | ETH-USD | 4.47 | — | entry |
| 2026-10-23T16:05 | EMA 20/50 cross | buy | TNA | 4.75 | — | entry |
| 2026-10-23T16:05 | EMA 20/50 cross | buy | SPY | 4.77 | — | entry signal |
| 2026-10-23T16:05 | EMA 20/50 cross | buy | PLTR | 4.77 | — | entry signal |
| 2026-10-23T16:05 | EMA 20/50 cross | buy | IWM | 4.77 | — | entry |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | TQQQ | 2.70 | 0.01 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | TECL | 2.75 | 0.00 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | SOXL | 2.74 | 0.01 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | QQQ | 2.73 | -0.01 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | MSFT | 2.67 | -0.00 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | ETH-USD | 2.73 | -0.02 | rebalance down |
| 2026-10-23T16:05 | EMA 20/50 cross | sell | AMD | 2.73 | 0.01 | rebalance down |
| 2026-10-23T16:00 | Agent (rotation) | buy | TQQQ | 32.13 | — | entry |
| 2026-10-23T16:00 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 104.40 | — | entry |
| 2026-10-23T16:00 | ROC + volume · 1h | buy | DOGE-USD | 19.54 | — | entry signal |
| 2026-10-23T16:00 | RSI(14) reversion | sell | LABU | 10.88 | 0.36 | take-profit |
| 2026-10-23T15:50 | Agent (aggressive) | sell | TSLA | 43.35 | -0.54 | selected signal exited |
| 2026-10-23T15:50 | Agent | sell | TSLA | 17.72 | -0.22 | selected signal exited |
| 2026-10-23T15:50 | RSI(14) reversion | buy | XRP-USD | 2.69 | — | rebalance up |
| 2026-10-23T15:50 | RSI(14) reversion | buy | COIN | 2.72 | — | rebalance up |
| 2026-10-23T15:50 | RSI(14) reversion | buy | BTC-USD | 2.70 | — | rebalance up |
| 2026-10-23T15:50 | RSI(14) reversion | sell | DOGE-USD | 10.61 | 0.00 | exit signal |
| 2026-10-23T15:50 | ROC + volume | sell | TSLA | 14.35 | -0.13 | exit signal |
| 2026-10-23T15:47 | Agent (ML meta-label) | buy | IWM | 4.71 | — | entry |
| 2026-10-23T15:47 | Agent (ML meta-label) | sell | ETH-USD | 4.69 | -0.03 | selected signal exited |
| 2026-10-23T15:45 | Three white soldiers | sell | UPRO | 20.34 | -0.05 | exit signal |
| 2026-10-23T15:45 | Three white soldiers | sell | SPY | 20.36 | -0.04 | exit signal |
| 2026-10-23T15:45 | ROC + volume | sell | TQQQ | 14.43 | -0.08 | exit signal |
| 2026-10-23T15:45 | ROC + volume | sell | TECL | 14.48 | -0.01 | exit signal |
| 2026-10-23T15:40 | Agent (ML meta-label) | buy | ETH-USD | 4.72 | — | entry |
| 2026-10-23T15:35 | Agent (ML meta-label) | sell | IWM | 4.72 | -0.00 | selected signal exited |
| 2026-10-23T15:30 | Agent (rotation) | sell | TQQQ | 32.03 | -0.15 | selected signal exited |
| 2026-10-23T15:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 104.40 | -0.50 | target is flat |
| 2026-10-23T15:30 | Agent (ML meta-label) | buy | IWM | 4.72 | — | entry |
| 2026-10-23T15:30 | MFI reversion · 1h | buy | TSLA | 20.57 | — | entry signal |
| 2026-10-23T15:30 | MFI reversion · 1h | buy | LABU | 20.57 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | UPRO | 4.70 | — | entry signal |
| 2026-10-23T15:30 | CCI reversion · 1h | buy | TSLA | 4.75 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 16:15:05.000115+00:00 -> 2026-10-23 16:25:05.000115+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
