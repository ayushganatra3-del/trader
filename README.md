# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T00:15:05.000126+00:00 · 32427 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.11 (-9.89%)

Closed trades 98, win rate 39.8%, fees £3.14, max drawdown -10.53%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-22 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 240 decisions in 48 calls, $0.0034 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T00:15 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-23T00:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T00:15 | 2 / 3 / 0 | ETH-USD 51% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.21 | 7.21 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.36 | 0.36 | 78 | 46.2 | -10.22 | -2.72 | -13.79 | 140 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.33 | -0.67 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.55 | -3.45 | 118 | 31.4 | -3.72 | -1.62 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 95.85 | -4.15 | 0 | — | 3.71 | 0.73 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.79 | -4.21 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.02 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.44 | -4.56 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.27 | -5.73 | 25 | 40.0 | -13.46 | -2.31 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -22.50 | -7.00 | -23.01 | 121 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.95 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.96 | -7.04 | 115 | 26.1 | -16.55 | -3.63 | -20.59 | 264 |
| 26 | Daily: Momentum burst | daily | 92.56 | -7.44 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.48 | -7.52 | 103 | 19.4 | -10.11 | -1.94 | -12.90 | 251 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.42 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -14.68 | -6.12 | -15.83 | 260 |
| 31 | Daily: Bullish score | daily | 89.73 | -10.27 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.44 | -10.56 | 104 | 27.9 | -11.50 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -13.00 | -2.33 | -14.76 | 108 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.95 | -11.05 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -15.79 | -3.52 | -16.68 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.55 | -12.45 | 68 | 11.8 | -24.69 | -4.51 | -25.56 | 144 |
| 37 | Stochastic reversion · 1h | reversion | 87.13 | -12.87 | 179 | 45.3 | -16.36 | -2.69 | -22.24 | 389 |
| 38 | Supertrend · 1h | trend | 86.95 | -13.05 | 104 | 15.4 | -24.19 | -4.71 | -27.40 | 217 |
| 39 | RSI momentum · 1h | momentum | 86.67 | -13.33 | 96 | 16.7 | -20.77 | -3.92 | -22.88 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.22 | -13.78 | 73 | 23.3 | -23.21 | -4.48 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.06 | -14.94 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.64 | -15.36 | 216 | 23.1 | -28.57 | -5.17 | -29.90 | 469 |
| 44 | Triple EMA stack · 1h | trend | 84.37 | -15.63 | 96 | 15.6 | -27.44 | -5.11 | -29.45 | 215 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.01 | -16.98 | 104 | 33.7 | -14.10 | -2.05 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.69 | -17.32 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.27 | -17.73 | 198 | 17.7 | -30.19 | -5.70 | -31.80 | 300 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.78 | 103 | 15.5 | -24.66 | -4.77 | -25.18 | 226 |
| 50 | MFI reversion · 1h | reversion | 81.94 | -18.05 | 245 | 31.4 | -18.86 | -2.87 | -21.11 | 148 |
| 51 | Williams %R · 1h | reversion | 81.84 | -18.16 | 204 | 44.1 | -33.55 | -5.32 | -37.94 | 529 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.39 | -18.14 | -45.39 | 600 |
| 53 | CCI reversion · 1h | reversion | 80.49 | -19.51 | 193 | 43.0 | -24.03 | -3.24 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.24 | -19.76 | 827 | 19.0 | -17.26 | -3.29 | -18.75 | 385 |
| 55 | Bollinger reversion · 1h | reversion | 80.09 | -19.91 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.99 | -20.02 | 260 | 23.5 | -43.26 | -9.25 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.71 | -20.29 | 233 | 24.0 | -28.37 | -5.09 | -28.88 | 381 |
| 58 | EMA 9/21 cross · 1h | trend | 78.19 | -21.81 | 155 | 11.6 | -32.66 | -6.16 | -33.29 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 77.68 | -22.32 | 90 | 23.3 | -23.02 | -4.14 | -24.19 | 195 |
| 60 | Candlestick reversal · 1h | reversion | 77.23 | -22.77 | 244 | 29.1 | -39.41 | -6.98 | -41.18 | 571 |
| 61 | VWAP momentum · 1h | momentum | 76.98 | -23.02 | 499 | 21.4 | -50.08 | -10.18 | -51.02 | 1232 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.79 | -41.21 | 693 | 23.1 | -78.90 | -22.65 | -79.56 | 1687 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -65.14 | -20.55 | -65.30 | 852 |
| 65 | Donchian 55/20 | breakout | 56.05 | -43.95 | 542 | 19.9 | -73.14 | -20.10 | -73.15 | 1264 |
| 66 | Squeeze breakout | breakout | 54.94 | -45.06 | 535 | 14.4 | -67.96 | -23.87 | -68.49 | 1200 |
| 67 | EMA 20/50 cross | trend | 53.86 | -46.14 | 590 | 20.5 | -79.78 | -20.82 | -79.78 | 1441 |
| 68 | RSI(14) reversion | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.97 | -17.22 | -77.07 | 1679 |
| 69 | VWAP reversion | reversion | 50.70 | -49.30 | 808 | 25.0 | -73.65 | -14.56 | -73.82 | 1519 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -32.11 | -98.88 | 5245 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.26 | -34.24 | -94.26 | 2555 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.65 | -24.69 | -88.65 | 1884 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.80 | -29.29 | -91.80 | 2336 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.80 | -24.90 | -90.91 | 2205 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -35.69 | -97.91 | 3499 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.99 | -37.75 | -97.09 | 3544 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -28.02 | -94.37 | 2537 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.43 | -28.61 | -83.43 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -35.90 | -99.49 | 5872 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -31.11 | -93.21 | 2619 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.19 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -42.43 | -99.79 | 6194 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.28 | -31.80 | -92.32 | 2330 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.25 | -97.77 | 3571 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -37.50 | -98.66 | 4769 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -36.76 | -94.77 | 2787 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.04 | -28.67 | -84.77 | 1778 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.38 | -99.60 | 6230 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.08 | -23.53 | -88.13 | 2198 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.76 | -26.83 | -88.79 | 2180 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -33.57 | -96.30 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.87 | -33.94 | -89.87 | 2100 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -33.88 | -96.22 | 4134 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.33 | -99.91 | 8241 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T00:15 | VWAP reversion | buy | BTC-USD | 2.56 | — | rebalance up |
| 2026-10-23T00:15 | VWAP reversion | sell | XRP-USD | 10.14 | -0.06 | exit signal |
| 2026-10-23T00:15 | VWAP reversion | sell | SOL-USD | 10.14 | -0.06 | exit signal |
| 2026-10-23T00:15 | VWAP reversion | sell | ETH-USD | 10.14 | -0.06 | exit signal |
| 2026-10-23T00:15 | VWAP reversion | sell | DOGE-USD | 10.14 | -0.06 | exit signal |
| 2026-10-23T00:05 | Three white soldiers | sell | ETH-USD | 20.25 | -0.15 | exit signal |
| 2026-10-23T00:01 | MACD cross · 1h | buy | ETH-USD | 4.23 | — | rebalance up |
| 2026-10-23T00:01 | MACD cross · 1h | sell | DOGE-USD | 4.23 | -0.02 | rebalance down |
| 2026-10-23T00:00 | MACD cross · 1h | buy | ETH-USD | 7.87 | — | entry signal |
| 2026-10-23T00:00 | MACD cross · 1h | buy | BTC-USD | 16.96 | — | entry signal |
| 2026-10-23T00:00 | VWAP reversion | buy | XRP-USD | 10.20 | — | entry |
| 2026-10-23T00:00 | VWAP reversion | buy | SOL-USD | 10.20 | — | entry |
| 2026-10-23T00:00 | VWAP reversion | buy | ETH-USD | 10.20 | — | entry |
| 2026-10-23T00:00 | VWAP reversion | buy | DOGE-USD | 10.20 | — | entry |
| 2026-10-23T00:00 | VWAP reversion | buy | BTC-USD | 10.20 | — | entry |
| 2026-10-22T23:55 | Three white soldiers | buy | ETH-USD | 20.40 | — | entry signal |
| 2026-10-22T23:55 | EMA 20/50 cross | buy | DOGE-USD | 13.47 | — | entry signal |
| 2026-10-22T23:40 | EMA 20/50 cross | sell | DOGE-USD | 13.43 | -0.11 | exit signal |
| 2026-10-22T23:00 | CCI reversion · 1h | buy | XRP-USD | 4.19 | — | entry signal |
| 2026-10-22T23:00 | CCI reversion · 1h | buy | ETH-USD | 4.95 | — | rebalance up |
| 2026-10-22T23:00 | CCI reversion · 1h | sell | DOGE-USD | 4.57 | -0.04 | rebalance down |
| 2026-10-22T23:00 | CCI reversion · 1h | sell | BTC-USD | 4.57 | -0.04 | rebalance down |
| 2026-10-22T23:00 | Candlestick reversal · 1h | sell | SOL-USD | 5.11 | -0.05 | exit signal |
| 2026-10-22T23:00 | MACD cross · 1h | buy | DOGE-USD | 21.20 | — | entry signal |
| 2026-10-22T22:45 | EMA 20/50 cross | sell | BTC-USD | 13.44 | -0.10 | exit signal |
| 2026-10-22T22:20 | Squeeze breakout | sell | ETH-USD | 13.65 | -0.11 | stop-loss |
| 2026-10-22T22:20 | Donchian 55/20 | sell | ETH-USD | 13.94 | -0.14 | stop-loss |
| 2026-10-22T22:20 | Donchian 55/20 | sell | BTC-USD | 13.96 | -0.11 | stop-loss |
| 2026-10-22T22:20 | EMA 20/50 cross | sell | ETH-USD | 13.42 | -0.14 | stop-loss |
| 2026-10-22T22:15 | ROC + volume | sell | ETH-USD | 14.64 | -0.13 | exit signal |
| 2026-10-22T22:10 | Three white soldiers | sell | BTC-USD | 20.32 | -0.14 | exit signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.15 | — | entry signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | ETH-USD | 5.15 | — | entry signal |
| 2026-10-22T22:00 | Candlestick reversal · 1h | buy | DOGE-USD | 5.15 | — | entry signal |
| 2026-10-22T21:55 | EMA 20/50 cross | buy | DOGE-USD | 13.54 | — | entry signal |
| 2026-10-22T21:35 | Three white soldiers | sell | XRP-USD | 20.34 | -0.13 | exit signal |
| 2026-10-22T21:35 | ROC + volume | sell | SOL-USD | 14.61 | -0.16 | stop-loss |
| 2026-10-22T21:35 | EMA 20/50 cross | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-10-22T21:25 | Donchian 55/20 | buy | BTC-USD | 14.07 | — | entry signal |
| 2026-10-22T21:25 | EMA 20/50 cross | buy | ETH-USD | 13.56 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 00:15:05.000126+00:00 -> 2026-10-23 00:25:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
