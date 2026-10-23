# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-23T03:45:05.000139+00:00 · 32611 ticks

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

Today: 3000 decisions in 600 calls, $0.0419 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-23T03:45 | 1 / 4 / 0 | DOGE-USD 14% |  |
| Breezy | 2026-10-23T03:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-23T03:45 | 2 / 3 / 0 | ETH-USD 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.25 | 7.25 | 0 | — | 8.93 | 4.33 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.95 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.32 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.85 | 0.85 | 0 | — | 4.24 | 1.82 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.35 | 0.35 | 82 | 43.9 | -9.75 | -2.58 | -13.79 | 143 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.37 | -0.63 | 10 | 50.0 | -16.15 | -1.26 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 11 | Hold SPY | benchmark | 98.23 | -1.77 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.04 | -4.06 | 22 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -1.99 | -5.83 | 1 |
| 14 | Hold BTC | benchmark | 96.67 | -3.33 | 0 | — | 3.82 | 0.74 | -8.68 | 1 |
| 15 | Agent (rotation) | meta | 96.56 | -3.44 | 118 | 31.4 | -3.72 | -1.62 | -7.58 | 234 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.82 | -4.18 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.02 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.47 | -4.53 | 0 | — | -4.72 | -1.75 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.15 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.30 | -5.70 | 25 | 40.0 | -13.46 | -2.31 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.77 | -6.24 | 95 | 23.2 | -22.28 | -6.89 | -22.80 | 120 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.73 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.06 | -6.94 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.99 | -7.01 | 115 | 26.1 | -17.78 | -3.89 | -20.86 | 265 |
| 26 | Daily: Momentum burst | daily | 92.59 | -7.41 | 8 | 12.5 | -16.39 | -2.90 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.41 | -7.59 | 103 | 19.4 | -10.54 | -2.04 | -12.90 | 254 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.15 | -0.94 | -11.76 | 96 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.13 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -13.05 | -5.99 | -13.59 | 249 |
| 31 | Daily: Bullish score | daily | 89.76 | -10.24 | 8 | 0.0 | -7.26 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.45 | -10.55 | 104 | 27.9 | -11.50 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.14 | -10.86 | 101 | 22.8 | -13.00 | -2.33 | -14.76 | 108 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.98 | -11.02 | 0 | — | -3.71 | -0.42 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -18.96 | -4.61 | -19.81 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.58 | -12.42 | 68 | 11.8 | -23.50 | -4.22 | -26.13 | 144 |
| 37 | Stochastic reversion · 1h | reversion | 87.33 | -12.67 | 182 | 45.6 | -16.25 | -2.67 | -22.24 | 388 |
| 38 | Supertrend · 1h | trend | 86.97 | -13.03 | 104 | 15.4 | -23.81 | -4.64 | -27.15 | 218 |
| 39 | RSI momentum · 1h | momentum | 86.69 | -13.31 | 96 | 16.7 | -20.70 | -3.94 | -23.12 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.26 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.23 | -13.77 | 73 | 23.3 | -23.21 | -4.48 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.08 | -14.92 | 168 | 39.9 | -26.16 | -7.09 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 85.00 | -15.00 | 216 | 23.1 | -27.31 | -4.99 | -29.35 | 468 |
| 44 | Triple EMA stack · 1h | trend | 84.40 | -15.60 | 96 | 15.6 | -26.48 | -4.90 | -28.98 | 213 |
| 45 | Ichimoku · 1h | trend | 83.83 | -16.17 | 65 | 12.3 | -20.38 | -3.72 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.29 | -16.71 | 104 | 33.7 | -13.86 | -2.01 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.71 | -17.29 | 93 | 20.4 | -24.80 | -4.47 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.30 | -17.70 | 198 | 17.7 | -29.24 | -5.45 | -31.58 | 298 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.77 | 103 | 15.5 | -24.21 | -4.67 | -25.07 | 226 |
| 50 | Williams %R · 1h | reversion | 82.18 | -17.82 | 207 | 44.9 | -33.07 | -5.20 | -37.94 | 527 |
| 51 | MFI reversion · 1h | reversion | 82.05 | -17.95 | 245 | 31.4 | -18.29 | -2.77 | -21.11 | 147 |
| 52 | Three white soldiers | momentum | 81.44 | -18.57 | 269 | 19.7 | -45.39 | -18.14 | -45.39 | 600 |
| 53 | CCI reversion · 1h | reversion | 80.97 | -19.03 | 193 | 43.0 | -23.55 | -3.16 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.29 | -19.71 | 829 | 19.1 | -15.75 | -2.99 | -17.33 | 397 |
| 55 | Bollinger reversion · 1h | reversion | 80.12 | -19.88 | 168 | 35.1 | -31.11 | -5.96 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 80.00 | -20.00 | 260 | 23.5 | -43.26 | -9.25 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.72 | -20.28 | 233 | 24.0 | -28.37 | -5.09 | -28.88 | 381 |
| 58 | EMA 9/21 cross · 1h | trend | 78.22 | -21.78 | 155 | 11.6 | -32.96 | -6.22 | -33.48 | 332 |
| 59 | RSI(14) reversion · 1h | reversion | 77.85 | -22.15 | 90 | 23.3 | -22.16 | -3.95 | -24.19 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 77.33 | -22.67 | 245 | 29.0 | -38.76 | -6.91 | -40.01 | 567 |
| 61 | VWAP momentum · 1h | momentum | 77.00 | -23.00 | 499 | 21.4 | -50.38 | -10.29 | -51.02 | 1241 |
| 62 | Max aggression: 1-day momentum | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.83 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.45 | -41.55 | 696 | 23.0 | -78.40 | -22.96 | -78.40 | 1684 |
| 64 | Volume breakout | breakout | 57.88 | -42.12 | 411 | 13.4 | -65.09 | -20.64 | -65.19 | 853 |
| 65 | Donchian 55/20 | breakout | 55.31 | -44.69 | 547 | 19.7 | -72.86 | -20.52 | -72.90 | 1271 |
| 66 | Squeeze breakout | breakout | 54.49 | -45.51 | 539 | 14.3 | -68.57 | -24.37 | -68.57 | 1202 |
| 67 | EMA 20/50 cross | trend | 54.04 | -45.96 | 591 | 20.5 | -79.72 | -20.73 | -79.87 | 1445 |
| 68 | RSI(14) reversion | reversion | 53.11 | -46.89 | 808 | 26.0 | -76.99 | -17.23 | -77.07 | 1680 |
| 69 | VWAP reversion | reversion | 50.67 | -49.33 | 809 | 25.0 | -73.32 | -14.34 | -73.82 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.88 | -32.89 | -98.88 | 5257 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.93 | -33.87 | -93.95 | 2555 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.59 | -24.51 | -88.68 | 1887 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.48 | -29.11 | -91.52 | 2339 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.73 | -24.67 | -90.84 | 2202 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -35.29 | -97.85 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -37.50 | -96.94 | 3548 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.51 | -28.60 | -94.51 | 2554 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.26 | -28.33 | -83.26 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -35.92 | -99.49 | 5874 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.83 | -31.29 | -92.85 | 2621 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.66 | -30.33 | -95.67 | 3420 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.77 | -99.78 | 6197 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.32 | -32.01 | -92.36 | 2332 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -39.15 | -97.67 | 3575 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -37.52 | -98.66 | 4768 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -37.99 | -94.72 | 2793 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.33 | -29.50 | -84.36 | 1785 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -39.39 | -99.60 | 6227 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -23.39 | -88.13 | 2197 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.70 | -26.70 | -88.72 | 2174 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -33.57 | -96.30 | 3801 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.85 | -33.90 | -89.87 | 2100 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -33.88 | -96.22 | 4134 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.20 | -99.91 | 8244 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-23T02:35 | Donchian 55/20 | buy | ETH-USD | 13.88 | — | entry signal |
| 2026-10-23T02:35 | Donchian 55/20 | buy | BTC-USD | 13.88 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | XRP-USD | 14.70 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | ETH-USD | 14.70 | — | entry signal |
| 2026-10-23T02:35 | ROC + volume | buy | BTC-USD | 14.70 | — | entry signal |
| 2026-10-23T02:05 | Donchian 55/20 | sell | XRP-USD | 13.77 | -0.16 | stop-loss |
| 2026-10-23T02:05 | Donchian 55/20 | sell | SOL-USD | 13.83 | -0.15 | stop-loss |
| 2026-10-23T02:05 | EMA 20/50 cross | sell | BTC-USD | 8.04 | -0.07 | stop-loss |
| 2026-10-23T02:00 | Candlestick reversal · 1h | sell | BTC-USD | 5.11 | -0.04 | exit signal |
| 2026-10-23T02:00 | MACD cross · 1h | buy | SOL-USD | 9.65 | — | entry |
| 2026-10-23T02:00 | MACD cross · 1h | sell | DOGE-USD | 4.88 | -0.00 | rebalance down |
| 2026-10-23T02:00 | MACD cross · 1h | sell | BTC-USD | 4.77 | -0.03 | rebalance down |
| 2026-10-23T02:00 | Volume breakout | sell | XRP-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Volume breakout | sell | ETH-USD | 14.48 | -0.12 | exit signal |
| 2026-10-23T02:00 | Volume breakout | sell | DOGE-USD | 14.45 | -0.15 | exit signal |
| 2026-10-23T02:00 | Donchian 55/20 | sell | BTC-USD | 13.86 | -0.13 | stop-loss |
| 2026-10-23T01:50 | Volume breakout | buy | XRP-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Volume breakout | buy | DOGE-USD | 14.60 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | SOL-USD | 13.99 | — | entry signal |
| 2026-10-23T01:50 | Donchian 55/20 | buy | BTC-USD | 13.99 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-25 03:45:05.000139+00:00 -> 2026-10-23 03:55:05.000139+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
