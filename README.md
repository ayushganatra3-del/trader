# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T06:15:05.000124+00:00 · 32743 ticks

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
| Copy: Insider buying | 2026-10-22 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.72 · VIX 19.03 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 4980 decisions in 996 calls, $0.0695 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T06:15 | 2 / 3 / 0 | XRP-USD 15% |  |
| Breezy | 2026-10-23T06:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T06:15 | 4 / 1 / 0 | ETH-USD 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| Keltner breakout | MSTR | 1.75 | +9.96% | 5 |
| VWAP momentum | NVDA | 1.72 | +2.48% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.28 | 7.28 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.88 | 0.88 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.37 | 0.37 | 82 | 43.9 | -10.04 | -2.69 | -13.79 | 139 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.40 | -0.60 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Hold SPY | benchmark | 98.25 | -1.75 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.68 | -3.33 | 0 | — | 5.55 | 1.00 | -8.68 | 1 |
| 15 | Agent (rotation) | meta | 96.57 | -3.43 | 118 | 31.4 | -3.69 | -1.56 | -7.58 | 234 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.85 | -4.15 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.03 | 0.71 | -7.93 | 8 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 95.50 | -4.50 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.33 | -5.67 | 25 | 40.0 | -14.11 | -2.47 | -20.50 | 73 |
| 22 | Trend pullback · 1h | trend | 93.77 | -6.23 | 95 | 23.2 | -22.97 | -7.15 | -23.14 | 123 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.06 | -6.94 | 48 | 16.7 | -18.56 | -3.75 | -19.66 | 104 |
| 25 | Parabolic SAR · 1h | trend | 93.02 | -6.98 | 115 | 26.1 | -18.49 | -4.09 | -21.20 | 268 |
| 26 | Daily: Momentum burst | daily | 92.62 | -7.38 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.15 | -7.85 | 104 | 19.2 | -10.27 | -1.98 | -12.90 | 253 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.42 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -13.90 | -5.93 | -14.40 | 247 |
| 31 | Daily: Bullish score | daily | 89.79 | -10.21 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.46 | -10.54 | 104 | 27.9 | -10.75 | -1.89 | -15.91 | 256 |
| 33 | Volume breakout · 1h | breakout | 89.14 | -10.86 | 101 | 22.8 | -12.69 | -2.27 | -14.45 | 107 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.00 | -11.00 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -18.49 | -4.52 | -19.35 | 132 |
| 36 | EMA 20/50 cross · 1h | trend | 87.60 | -12.40 | 68 | 11.8 | -22.85 | -4.14 | -25.08 | 141 |
| 37 | Stochastic reversion · 1h | reversion | 87.35 | -12.65 | 183 | 45.9 | -16.25 | -2.67 | -22.24 | 388 |
| 38 | Supertrend · 1h | trend | 86.99 | -13.01 | 104 | 15.4 | -23.81 | -4.64 | -27.15 | 218 |
| 39 | RSI momentum · 1h | momentum | 86.71 | -13.29 | 96 | 16.7 | -20.01 | -3.78 | -22.22 | 212 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.23 | -13.77 | 73 | 23.3 | -23.21 | -4.48 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.09 | -14.91 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 85.08 | -14.92 | 216 | 23.1 | -26.80 | -4.87 | -29.35 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.42 | -15.58 | 96 | 15.6 | -26.75 | -4.97 | -28.98 | 213 |
| 45 | Ichimoku · 1h | trend | 83.84 | -16.16 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.34 | -16.66 | 104 | 33.7 | -13.82 | -2.01 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.72 | -17.28 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.32 | -17.68 | 198 | 17.7 | -29.22 | -5.43 | -31.74 | 299 |
| 49 | MACD zero-line · 1h | trend | 82.23 | -17.77 | 103 | 15.5 | -23.26 | -4.50 | -25.07 | 223 |
| 50 | Williams %R · 1h | reversion | 82.22 | -17.78 | 208 | 45.2 | -33.05 | -5.19 | -37.94 | 527 |
| 51 | MFI reversion · 1h | reversion | 82.08 | -17.91 | 245 | 31.4 | -17.71 | -2.67 | -21.11 | 147 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.42 | -18.17 | -45.42 | 601 |
| 53 | CCI reversion · 1h | reversion | 81.02 | -18.98 | 194 | 42.8 | -23.52 | -3.15 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.25 | -19.75 | 832 | 19.0 | -18.40 | -3.58 | -19.31 | 385 |
| 55 | Bollinger reversion · 1h | reversion | 80.14 | -19.86 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 80.04 | -19.96 | 260 | 23.5 | -41.99 | -8.92 | -43.75 | 666 |
| 57 | ROC + volume · 1h | momentum | 79.73 | -20.27 | 233 | 24.0 | -28.53 | -5.11 | -29.04 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 78.24 | -21.76 | 155 | 11.6 | -31.52 | -5.90 | -33.29 | 329 |
| 59 | RSI(14) reversion · 1h | reversion | 77.90 | -22.10 | 90 | 23.3 | -23.08 | -4.16 | -24.19 | 197 |
| 60 | Candlestick reversal · 1h | reversion | 77.41 | -22.59 | 245 | 29.0 | -38.97 | -6.87 | -41.12 | 569 |
| 61 | VWAP momentum · 1h | momentum | 77.02 | -22.98 | 499 | 21.4 | -50.02 | -10.18 | -50.94 | 1241 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.45 | -41.55 | 696 | 23.0 | -78.26 | -22.81 | -78.26 | 1680 |
| 64 | Volume breakout | breakout | 57.79 | -42.21 | 412 | 13.3 | -65.15 | -20.68 | -65.25 | 854 |
| 65 | Donchian 55/20 | breakout | 55.01 | -44.99 | 550 | 19.6 | -73.01 | -20.62 | -73.05 | 1273 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -68.50 | -24.37 | -68.50 | 1201 |
| 67 | EMA 20/50 cross | trend | 54.18 | -45.82 | 591 | 20.5 | -79.65 | -20.64 | -79.86 | 1445 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.82 | -17.08 | -77.05 | 1678 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -73.45 | -14.46 | -73.61 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.90 | -33.02 | -98.91 | 5283 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.98 | -34.26 | -93.99 | 2560 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.45 | -24.47 | -88.51 | 1889 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.48 | -29.15 | -91.52 | 2340 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.80 | -24.73 | -90.84 | 2208 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -35.23 | -97.81 | 3501 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.97 | -37.98 | -96.98 | 3564 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -28.19 | -94.40 | 2539 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.28 | -28.37 | -83.30 | 1721 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -35.72 | -99.48 | 5865 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -31.27 | -92.73 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.66 | -30.30 | -95.66 | 3423 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.90 | -99.78 | 6204 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.30 | -31.97 | -92.31 | 2335 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -39.51 | -97.69 | 3581 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -37.79 | -98.66 | 4768 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -37.63 | -94.67 | 2790 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.39 | -29.56 | -84.43 | 1787 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.55 | -99.60 | 6228 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.98 | -23.32 | -88.13 | 2196 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.64 | -26.65 | -88.66 | 2176 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.30 | -33.88 | -96.31 | 3800 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.82 | -33.87 | -89.88 | 2100 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.23 | -34.07 | -96.23 | 4137 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.93 | -99.91 | 8252 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-23T06:05 | Volume breakout | sell | XRP-USD | 14.38 | -0.08 | exit signal |
| 2026-10-23T06:00 | Agent (ML meta-label) | sell | XRP-USD | 3.33 | -0.01 | selected signal exited |
| 2026-10-23T06:00 | Williams %R · 1h | sell | XRP-USD | 8.21 | 0.07 | exit signal |
| 2026-10-23T06:00 | Stochastic reversion · 1h | sell | XRP-USD | 2.41 | 0.03 | exit signal |
| 2026-10-23T06:00 | ADX DI cross · 1h | buy | SOL-USD | 6.59 | — | entry signal |
| 2026-10-23T06:00 | ADX DI cross · 1h | buy | DOGE-USD | 15.36 | — | entry signal |
| 2026-10-23T05:45 | Donchian 55/20 | buy | XRP-USD | 13.76 | — | entry signal |
| 2026-10-23T05:20 | Agent (ML meta-label) | buy | XRP-USD | 3.34 | — | entry |
| 2026-10-23T05:17 | Agent (ML meta-label) | sell | XRP-USD | 3.63 | -0.02 | selected signal exited |
| 2026-10-23T05:15 | Agent (ML meta-label) | buy | XRP-USD | 3.65 | — | entry |
| 2026-10-23T05:15 | Donchian 55/20 | buy | DOGE-USD | 13.76 | — | entry signal |
| 2026-10-23T05:10 | Volume breakout | buy | XRP-USD | 14.47 | — | entry signal |
| 2026-10-23T05:00 | ADX DI cross · 1h | sell | ETH-USD | 21.95 | -0.34 | exit signal |
| 2026-10-23T04:46 | Agent (ML meta-label) | sell | XRP-USD | 3.80 | -0.03 | selected signal exited |
| 2026-10-23T04:30 | Donchian 55/20 | sell | ETH-USD | 13.74 | -0.15 | exit signal |
| 2026-10-23T04:30 | Donchian 55/20 | sell | BTC-USD | 13.76 | -0.12 | exit signal |
| 2026-10-23T04:20 | Donchian 55/20 | sell | DOGE-USD | 14.00 | -0.01 | target is flat |
| 2026-10-23T04:05 | Agent (ML meta-label) | buy | XRP-USD | 3.82 | — | entry |
| 2026-10-23T04:00 | CCI reversion · 1h | buy | XRP-USD | 9.27 | — | rebalance up |
| 2026-10-23T04:00 | CCI reversion · 1h | sell | DOGE-USD | 11.61 | 0.04 | exit signal |
| 2026-10-23T04:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 20.00 | — | entry signal |
| 2026-10-23T03:45 | Agent (ML meta-label) | sell | XRP-USD | 2.27 | -0.01 | selected signal exited |
| 2026-10-23T03:40 | Agent (ML meta-label) | buy | XRP-USD | 2.28 | — | entry |
| 2026-10-23T03:35 | ROC + volume | sell | ETH-USD | 14.61 | -0.09 | exit signal |
| 2026-10-23T03:35 | ROC + volume | sell | BTC-USD | 14.60 | -0.09 | exit signal |
| 2026-10-23T03:20 | Volume breakout | sell | BTC-USD | 14.39 | -0.11 | exit signal |
| 2026-10-23T03:20 | Donchian 55/20 | sell | XRP-USD | 13.55 | -0.14 | stop-loss |
| 2026-10-23T03:20 | ROC + volume | sell | XRP-USD | 14.54 | -0.15 | stop-loss |
| 2026-10-23T03:05 | EMA 20/50 cross | buy | SOL-USD | 2.70 | — | rebalance up |
| 2026-10-23T03:00 | Agent (ML meta-label) | sell | ETH-USD | 3.99 | 0.03 | selected signal exited |
| 2026-10-23T03:00 | Williams %R · 1h | sell | ETH-USD | 8.23 | 0.06 | exit signal |
| 2026-10-23T03:00 | Williams %R · 1h | sell | DOGE-USD | 8.24 | 0.08 | exit signal |
| 2026-10-23T03:00 | Williams %R · 1h | sell | BTC-USD | 8.18 | 0.02 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | ETH-USD | 8.04 | 0.06 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | DOGE-USD | 7.42 | -0.01 | exit signal |
| 2026-10-23T03:00 | Stochastic reversion · 1h | sell | BTC-USD | 4.85 | 0.01 | exit signal |
| 2026-10-23T03:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.16 | — | entry signal |
| 2026-10-23T03:00 | ADX DI cross · 1h | buy | ETH-USD | 22.29 | — | entry signal |
| 2026-10-23T02:35 | Volume breakout | buy | BTC-USD | 14.50 | — | entry signal |
| 2026-10-23T02:35 | Donchian 55/20 | buy | XRP-USD | 13.69 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 06:15:05.000124+00:00 -> 2026-10-23 06:25:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
