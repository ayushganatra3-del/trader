# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T18:15:05.000166+00:00 · 33327 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.30 (-10.70%)

Closed trades 101, win rate 38.6%, fees £3.19, max drawdown -11.12%.

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

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 30129 decisions in 2748 calls, $0.3757 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T18:15 | 12 / 10 / 8 | cash |  |
| Breezy | 2026-10-23T18:15 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-10-23T18:15 | 8 / 21 / 1 | ETHU 61% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.34 | 6.34 | 0 | — | 7.78 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.20 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.98 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.05 | -4.92 | 26 |
| 5 | VWAP reversion · 1h | reversion | 100.93 | 0.93 | 87 | 46.0 | -11.56 | -3.21 | -13.74 | 151 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.45 | 0.45 | 0 | — | 3.03 | 1.43 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.18 | -0.82 | 73 | 34.2 | 5.28 | 2.59 | -2.65 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.40 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.98 | -2.02 | 0 | — | -0.61 | -0.32 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.22 | -5.83 | 1 |
| 13 | Hold BTC | benchmark | 96.48 | -3.52 | 0 | — | 1.44 | 0.42 | -8.68 | 1 |
| 14 | Agent (rotation) | meta | 96.01 | -3.99 | 120 | 30.8 | -2.45 | -1.43 | -6.22 | 195 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.76 | -4.24 | 0 | — | -0.84 | -0.30 | -5.99 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.87 | -7.93 | 8 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.05 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.83 | -5.17 | 0 | — | -6.26 | -2.67 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.27 | -5.73 | 25 | 40.0 | -14.75 | -2.82 | -20.68 | 71 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.60 | -8.69 | 184 |
| 21 | Trend pullback · 1h | trend | 93.67 | -6.33 | 95 | 23.2 | -21.63 | -7.11 | -21.85 | 115 |
| 22 | Opening range 30m | breakout | 93.41 | -6.59 | 241 | 34.9 | -10.72 | -3.34 | -17.21 | 562 |
| 23 | Donchian 55/20 · 1h | breakout | 93.03 | -6.97 | 48 | 16.7 | -16.20 | -3.68 | -17.44 | 98 |
| 24 | Max aggression: 5-day momentum ⏸ | meta | 92.92 | -7.08 | 11 | 45.5 | -15.27 | -1.41 | -27.80 | 24 |
| 25 | Daily: Momentum burst | daily | 91.94 | -8.06 | 10 | 10.0 | -17.33 | -3.37 | -20.97 | 40 |
| 26 | Parabolic SAR · 1h | trend | 91.93 | -8.07 | 118 | 25.4 | -21.06 | -5.00 | -24.17 | 254 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.82 | -0.94 | -11.91 | 93 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.39 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.11 | -8.89 | 108 | 18.5 | -11.74 | -2.41 | -14.53 | 255 |
| 30 | Daily: Bullish score | daily | 89.40 | -10.60 | 9 | 0.0 | -8.23 | -1.08 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.22 | -2.80 | -15.92 | 109 |
| 32 | Agent | meta | 89.30 | -10.70 | 101 | 38.6 | -10.98 | -7.59 | -11.70 | 205 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.28 | -10.72 | 0 | — | -5.21 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.92 | -11.08 | 105 | 27.6 | -12.34 | -2.45 | -16.56 | 241 |
| 35 | Stochastic reversion · 1h | reversion | 87.69 | -12.31 | 186 | 45.2 | -19.93 | -3.77 | -22.47 | 385 |
| 36 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.78 | -4.42 | -15.12 | 95 |
| 37 | EMA 20/50 cross · 1h | trend | 86.57 | -13.43 | 71 | 11.3 | -22.44 | -4.49 | -25.11 | 138 |
| 38 | Opening range 15m | breakout | 86.48 | -13.52 | 305 | 30.2 | -15.64 | -4.56 | -17.87 | 703 |
| 39 | Keltner breakout · 1h | breakout | 86.21 | -13.79 | 73 | 23.3 | -22.79 | -4.85 | -24.32 | 190 |
| 40 | Supertrend · 1h | trend | 86.01 | -13.99 | 108 | 14.8 | -23.80 | -5.03 | -26.46 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.44 | -14.56 | 101 | 15.8 | -21.64 | -4.65 | -23.39 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.30 | -8.05 | -27.06 | 196 |
| 43 | MACD cross · 1h | trend | 85.00 | -15.00 | 217 | 23.0 | -22.76 | -4.56 | -26.15 | 451 |
| 44 | Z-score reversion · 1h | reversion | 84.01 | -15.99 | 106 | 34.0 | -14.73 | -2.49 | -21.48 | 197 |
| 45 | Ichimoku · 1h | trend | 83.81 | -16.19 | 65 | 12.3 | -23.81 | -4.98 | -25.68 | 110 |
| 46 | Triple EMA stack · 1h | trend | 83.79 | -16.21 | 98 | 15.3 | -25.98 | -5.21 | -28.44 | 211 |
| 47 | MFI reversion · 1h | reversion | 82.08 | -17.92 | 257 | 31.9 | -17.57 | -2.88 | -20.54 | 143 |
| 48 | MACD zero-line · 1h | trend | 81.97 | -18.03 | 103 | 15.5 | -21.38 | -4.49 | -24.85 | 218 |
| 49 | OBV trend · 1h | momentum | 81.45 | -18.55 | 202 | 17.3 | -31.87 | -7.05 | -33.61 | 304 |
| 50 | Donchian 20/10 · 1h | breakout | 81.38 | -18.62 | 96 | 19.8 | -24.39 | -4.76 | -27.45 | 217 |
| 51 | Williams %R · 1h | reversion | 81.35 | -18.65 | 213 | 44.1 | -35.18 | -6.32 | -36.69 | 522 |
| 52 | Three white soldiers | momentum | 81.32 | -18.68 | 274 | 20.1 | -43.50 | -21.10 | -43.64 | 589 |
| 53 | Bollinger reversion · 1h | reversion | 80.45 | -19.55 | 171 | 34.5 | -30.95 | -6.47 | -32.19 | 359 |
| 54 | CCI reversion · 1h | reversion | 80.40 | -19.60 | 198 | 42.9 | -26.36 | -3.97 | -28.17 | 451 |
| 55 | Agent (ML meta-label) | meta | 80.05 | -19.95 | 851 | 18.8 | -13.69 | -2.41 | -17.27 | 373 |
| 56 | Heikin-Ashi · 1h | trend | 79.09 | -20.91 | 268 | 23.1 | -42.92 | -10.09 | -43.65 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.16 | -21.84 | 239 | 23.8 | -30.95 | -6.22 | -32.05 | 380 |
| 58 | RSI(14) reversion · 1h | reversion | 78.12 | -21.88 | 91 | 23.1 | -14.94 | -2.76 | -23.51 | 186 |
| 59 | Candlestick reversal · 1h | reversion | 77.77 | -22.23 | 253 | 28.9 | -34.61 | -6.55 | -36.06 | 540 |
| 60 | EMA 9/21 cross · 1h | trend | 77.51 | -22.49 | 158 | 12.0 | -29.82 | -6.13 | -33.53 | 318 |
| 61 | VWAP momentum · 1h | momentum | 75.97 | -24.03 | 517 | 21.3 | -50.19 | -11.70 | -50.40 | 1209 |
| 62 | Max aggression: 1-day momentum | meta | 67.07 | -32.93 | 18 | 27.8 | -42.77 | -3.01 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.60 | -42.40 | 706 | 22.7 | -74.83 | -27.48 | -74.84 | 1547 |
| 64 | Volume breakout | breakout | 57.08 | -42.92 | 418 | 13.2 | -60.65 | -26.23 | -60.65 | 762 |
| 65 | Squeeze breakout | breakout | 53.90 | -46.10 | 547 | 14.3 | -66.04 | -28.84 | -66.19 | 1139 |
| 66 | RSI(14) reversion | reversion | 53.36 | -46.64 | 821 | 26.4 | -76.40 | -19.62 | -76.81 | 1665 |
| 67 | Donchian 55/20 | breakout | 53.20 | -46.80 | 564 | 19.1 | -71.51 | -23.74 | -71.66 | 1251 |
| 68 | EMA 20/50 cross | trend | 52.00 | -48.00 | 615 | 20.0 | -78.79 | -23.90 | -79.09 | 1408 |
| 69 | VWAP reversion | reversion | 50.69 | -49.31 | 814 | 25.1 | -74.52 | -17.57 | -74.75 | 1544 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -45.10 | -98.66 | 5009 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.76 | -47.64 | -93.80 | 2505 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.34 | -30.37 | -88.50 | 1873 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.08 | -38.59 | -91.16 | 2301 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.35 | -31.57 | -90.38 | 2147 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.62 | -54.82 | -97.64 | 3442 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -95.96 | -62.15 | -95.97 | 3323 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.71 | -35.54 | -93.75 | 2426 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.64 | -36.42 | -82.68 | 1677 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -55.06 | -99.31 | 5651 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -42.40 | -92.21 | 2569 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -40.60 | -95.29 | 3349 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -84.79 | -99.74 | 6072 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.90 | -46.37 | -91.91 | 2303 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -66.12 | -97.50 | 3510 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -59.43 | -98.46 | 4704 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.15 | -60.14 | -94.17 | 2722 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.58 | -39.90 | -83.65 | 1767 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -66.20 | -99.53 | 6148 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.46 | -28.62 | -87.65 | 2173 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.05 | -38.05 | -90.12 | 2216 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -47.49 | -95.87 | 3733 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -50.71 | -89.37 | 2077 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.00 | -47.95 | -96.06 | 4102 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -111.95 | -99.90 | 8111 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T18:15 | Three white soldiers | buy | TECL | 20.33 | — | entry |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | TNA | 2.69 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | TECL | 2.71 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | MSFT | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | IWM | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | ETH-USD | 2.66 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | buy | AMD | 2.68 | — | rebalance up |
| 2026-10-23T18:10 | EMA 20/50 cross | sell | BITX | 4.25 | -0.03 | exit signal |
| 2026-10-23T18:05 | Agent (ML meta-label) | buy | SPY | 1.32 | — | entry |
| 2026-10-23T18:05 | Agent (ML meta-label) | buy | ETH-USD | 4.37 | — | entry |
| 2026-10-23T18:05 | VWAP momentum · 1h | sell | DOGE-USD | 8.41 | -0.07 | target is flat |
| 2026-10-23T18:00 | Agent (ML meta-label) | buy | IWM | 4.72 | — | entry |
| 2026-10-23T18:00 | Agent (ML meta-label) | sell | ETH-USD | 4.69 | -0.02 | selected signal exited |
| 2026-10-23T18:00 | VWAP momentum · 1h | buy | TECL | 8.43 | — | entry |
| 2026-10-23T18:00 | VWAP momentum · 1h | sell | BTC-USD | 8.43 | -0.05 | exit signal |
| 2026-10-23T18:00 | MACD cross · 1h | buy | SOL-USD | 4.49 | — | rebalance up |
| 2026-10-23T18:00 | MACD cross · 1h | sell | XRP-USD | 12.09 | -0.11 | exit signal |
| 2026-10-23T18:00 | Squeeze breakout | sell | SQQQ | 13.41 | -0.09 | exit signal |
| 2026-10-23T18:00 | ROC + volume | sell | SQQQ | 14.42 | -0.01 | exit signal |
| 2026-10-23T17:55 | EMA 20/50 cross | sell | LABU | 5.18 | -0.02 | target is flat |
| 2026-10-23T17:50 | EMA 20/50 cross | sell | BTC-USD | 4.71 | -0.03 | exit signal |
| 2026-10-23T17:46 | Day trade: Stocks in Play ORB | buy | SOXL | 24.79 | — | entry |
| 2026-10-23T17:46 | Agent (ML meta-label) | buy | ETH-USD | 4.71 | — | entry |
| 2026-10-23T17:46 | Agent (ML meta-label) | sell | IWM | 4.45 | -0.01 | selected signal exited |
| 2026-10-23T17:46 | EMA 20/50 cross | buy | LABU | 5.20 | — | entry signal |
| 2026-10-23T17:40 | Agent | sell | MSTR | 17.72 | -0.17 | selected signal exited |
| 2026-10-23T17:40 | ROC + volume | sell | MSTR | 14.35 | -0.08 | exit signal |
| 2026-10-23T17:35 | OBV trend · 1h | sell | IWM | 20.28 | -0.01 | target is flat |
| 2026-10-23T17:35 | Opening range 30m | buy | TNA | 3.68 | — | entry |
| 2026-10-23T17:35 | Opening range 30m | buy | MSTR | 5.67 | — | rebalance up |
| 2026-10-23T17:35 | Opening range 30m | sell | GOOGL | 9.35 | -0.06 | stop-loss |
| 2026-10-23T17:30 | Connors RSI(2) · 1h | sell | SQQQ | 21.53 | 0.23 | exit signal |
| 2026-10-23T17:30 | Candlestick reversal · 1h | buy | PLTR | 1.79 | — | entry |
| 2026-10-23T17:30 | Candlestick reversal · 1h | buy | IWM | 5.55 | — | entry |
| 2026-10-23T17:30 | Candlestick reversal · 1h | sell | SOXL | 7.02 | -0.01 | exit signal |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | SOL-USD | 3.95 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | MSTR | 3.91 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | MSFT | 3.97 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | META | 3.97 | — | rebalance up |
| 2026-10-23T17:30 | VWAP momentum · 1h | buy | ETHU | 8.47 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 18:15:05.000166+00:00 -> 2026-10-23 18:25:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
