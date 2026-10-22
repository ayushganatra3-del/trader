# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T23:15:05.000133+00:00 · 32376 ticks

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

Today: 40533 decisions in 3432 calls, $0.5034 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T23:15 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-22T23:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T23:15 | 3 / 2 / 0 | ETH-USD 52% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.23 | 7.23 | 0 | — | 8.93 | 4.37 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.96 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.33 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.82 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.83 | 0.83 | 0 | — | 4.24 | 1.83 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.33 | 0.33 | 78 | 46.2 | -10.27 | -2.76 | -13.79 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.35 | -0.65 | 10 | 50.0 | -16.15 | -1.27 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.23 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.07 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.21 | -1.79 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -2.00 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.56 | -3.44 | 118 | 31.4 | -3.72 | -1.63 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 96.01 | -3.99 | 0 | — | 3.80 | 0.74 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.80 | -4.20 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.03 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.95 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.45 | -4.55 | 0 | — | -4.72 | -1.77 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.96 | 2.17 | -7.13 | 194 |
| 21 | Copy: Insider buying | copy | 94.28 | -5.71 | 25 | 40.0 | -13.46 | -2.32 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -22.45 | -7.03 | -22.70 | 121 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.74 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.95 | 48 | 16.7 | -18.51 | -3.78 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.97 | -7.03 | 115 | 26.1 | -16.86 | -3.74 | -20.59 | 263 |
| 26 | Daily: Momentum burst | daily | 92.58 | -7.42 | 8 | 12.5 | -16.39 | -2.92 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.49 | -7.51 | 103 | 19.4 | -10.11 | -1.96 | -12.90 | 251 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.87 | -0.88 | -11.76 | 96 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.14 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -14.38 | -6.35 | -15.74 | 272 |
| 31 | Daily: Bullish score | daily | 89.74 | -10.26 | 8 | 0.0 | -7.26 | -0.85 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.44 | -10.56 | 104 | 27.9 | -11.51 | -2.05 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -12.69 | -2.29 | -14.45 | 107 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.96 | -11.04 | 0 | — | -3.71 | -0.43 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -15.67 | -3.52 | -16.68 | 131 |
| 36 | EMA 20/50 cross · 1h | trend | 87.56 | -12.44 | 68 | 11.8 | -24.31 | -4.46 | -25.66 | 144 |
| 37 | Stochastic reversion · 1h | reversion | 87.13 | -12.87 | 179 | 45.3 | -16.37 | -2.71 | -22.24 | 389 |
| 38 | Supertrend · 1h | trend | 86.96 | -13.04 | 104 | 15.4 | -24.19 | -4.75 | -27.40 | 217 |
| 39 | RSI momentum · 1h | momentum | 86.68 | -13.32 | 96 | 16.7 | -20.78 | -3.95 | -22.88 | 213 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.30 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.22 | -13.78 | 73 | 23.3 | -23.38 | -4.55 | -24.29 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.07 | -14.93 | 168 | 39.9 | -26.16 | -7.15 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.75 | -15.25 | 216 | 23.1 | -28.47 | -5.19 | -29.90 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.38 | -15.62 | 96 | 15.6 | -27.44 | -5.15 | -29.45 | 215 |
| 45 | Ichimoku · 1h | trend | 83.83 | -16.17 | 65 | 12.3 | -20.38 | -3.74 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 82.99 | -17.01 | 104 | 33.7 | -14.14 | -2.07 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.69 | -17.31 | 93 | 20.4 | -24.80 | -4.51 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.28 | -17.72 | 198 | 17.7 | -29.98 | -5.68 | -31.86 | 299 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.78 | 103 | 15.5 | -24.65 | -4.80 | -25.17 | 226 |
| 50 | MFI reversion · 1h | reversion | 81.96 | -18.04 | 245 | 31.4 | -18.76 | -2.89 | -21.11 | 149 |
| 51 | Williams %R · 1h | reversion | 81.83 | -18.17 | 204 | 44.1 | -33.65 | -5.39 | -37.94 | 529 |
| 52 | Three white soldiers | momentum | 81.58 | -18.42 | 268 | 19.8 | -45.32 | -18.35 | -45.32 | 600 |
| 53 | CCI reversion · 1h | reversion | 80.47 | -19.53 | 193 | 43.0 | -24.07 | -3.27 | -28.13 | 446 |
| 54 | Agent (ML meta-label) | meta | 80.25 | -19.75 | 827 | 19.0 | -16.89 | -3.21 | -19.16 | 396 |
| 55 | Bollinger reversion · 1h | reversion | 80.10 | -19.90 | 168 | 35.1 | -31.11 | -6.01 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.99 | -20.01 | 260 | 23.5 | -43.26 | -9.33 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.72 | -20.28 | 233 | 24.0 | -28.53 | -5.15 | -29.04 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 78.20 | -21.80 | 155 | 11.6 | -33.17 | -6.33 | -33.69 | 333 |
| 59 | RSI(14) reversion · 1h | reversion | 77.69 | -22.31 | 90 | 23.3 | -23.63 | -4.32 | -24.19 | 194 |
| 60 | Candlestick reversal · 1h | reversion | 77.23 | -22.77 | 244 | 29.1 | -39.42 | -7.04 | -41.12 | 569 |
| 61 | VWAP momentum · 1h | momentum | 76.99 | -23.01 | 499 | 21.4 | -50.00 | -10.26 | -50.94 | 1231 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.85 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 58.79 | -41.21 | 693 | 23.1 | -78.67 | -23.05 | -79.49 | 1684 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -65.16 | -20.89 | -65.32 | 853 |
| 65 | Donchian 55/20 | breakout | 56.05 | -43.95 | 542 | 19.9 | -73.73 | -19.95 | -74.14 | 1266 |
| 66 | Squeeze breakout | breakout | 54.94 | -45.06 | 535 | 14.4 | -67.76 | -24.14 | -68.49 | 1201 |
| 67 | EMA 20/50 cross | trend | 53.95 | -46.05 | 589 | 20.5 | -80.10 | -21.19 | -80.10 | 1443 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.76 | -17.25 | -77.05 | 1680 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.62 | -14.65 | -73.85 | 1518 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -33.09 | -98.88 | 5260 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.16 | -35.48 | -94.34 | 2555 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.63 | -25.12 | -88.64 | 1884 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.89 | -29.84 | -92.03 | 2339 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.76 | -25.28 | -90.87 | 2204 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -36.86 | -97.97 | 3500 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -97.00 | -39.18 | -97.10 | 3555 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -28.75 | -94.42 | 2539 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.43 | -29.30 | -83.43 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -37.10 | -99.49 | 5874 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.76 | -31.97 | -93.19 | 2619 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.96 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -44.30 | -99.79 | 6192 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.24 | -32.57 | -92.36 | 2333 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -40.58 | -97.76 | 3569 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -38.93 | -98.65 | 4769 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -37.91 | -94.74 | 2785 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.90 | -29.29 | -84.77 | 1778 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -40.96 | -99.60 | 6230 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.08 | -23.96 | -88.13 | 2198 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.76 | -27.31 | -88.79 | 2179 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -34.58 | -96.29 | 3801 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.91 | -35.12 | -90.08 | 2103 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.21 | -35.00 | -96.21 | 4135 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.35 | -99.91 | 8244 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-22T21:20 | Three white soldiers | buy | BTC-USD | 20.46 | — | entry signal |
| 2026-10-22T21:20 | Donchian 55/20 | buy | ETH-USD | 14.08 | — | entry signal |
| 2026-10-22T21:20 | ROC + volume | buy | SOL-USD | 14.77 | — | entry signal |
| 2026-10-22T21:20 | ROC + volume | buy | ETH-USD | 14.77 | — | entry signal |
| 2026-10-22T21:15 | Squeeze breakout | buy | ETH-USD | 13.76 | — | entry signal |
| 2026-10-22T21:10 | Three white soldiers | buy | XRP-USD | 20.46 | — | entry signal |
| 2026-10-22T21:00 | Stochastic reversion · 1h | buy | XRP-USD | 2.38 | — | entry signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.68 | -0.05 | exit signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.67 | -0.06 | exit signal |
| 2026-10-22T21:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.68 | -0.05 | exit signal |
| 2026-10-22T20:46 | Agent (ML meta-label) | buy | ETH-USD | 3.96 | — | entry |
| 2026-10-22T20:25 | Agent (ML meta-label) | sell | ETH-USD | 3.96 | -0.03 | selected signal exited |
| 2026-10-22T20:20 | Stochastic reversion · 1h | buy | BTC-USD | 4.84 | — | entry |
| 2026-10-22T20:20 | Stochastic reversion · 1h | sell | XRP-USD | 7.22 | -0.19 | stop-loss |
| 2026-10-22T20:00 | MFI reversion · 1h | buy | BTC-USD | 4.82 | — | entry signal |
| 2026-10-22T20:00 | MFI reversion · 1h | sell | SOL-USD | 4.82 | -0.04 | rebalance down |
| 2026-10-22T20:00 | CCI reversion · 1h | buy | ETH-USD | 6.57 | — | entry signal |
| 2026-10-22T20:00 | CCI reversion · 1h | sell | SOL-USD | 6.57 | -0.08 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 23:15:05.000133+00:00 -> 2026-10-22 23:25:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
