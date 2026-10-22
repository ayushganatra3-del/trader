# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T21:15:05.000141+00:00 · 32273 ticks

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
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-22)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.30 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, TSLA 6.5, AAPL 6.2, MSFT 5.8, SQQQ 5.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38988 decisions in 3123 calls, $0.4817 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T21:15 | 3 / 2 / 0 | SOL-USD 17%, ETH-USD 15% |  |
| Breezy | 2026-10-22T21:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T21:15 | 5 / 0 / 0 | ETH-USD 72% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.20 | 7.20 | 0 | — | 8.93 | 4.37 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.01 | 0.96 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.90 | 4.90 | 16 | 50.0 | 7.57 | 2.33 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.82 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.81 | 0.81 | 0 | — | 4.24 | 1.83 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.43 | 0.43 | 78 | 46.2 | -9.09 | -2.48 | -13.79 | 142 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Max aggression: 5-day momentum | meta | 99.32 | -0.68 | 10 | 50.0 | -16.15 | -1.27 | -34.64 | 26 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.23 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.07 | -4.06 | 22 |
| 12 | Hold SPY | benchmark | 98.18 | -1.82 | 0 | — | -0.00 | 0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.47 | -2.00 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.55 | -3.45 | 118 | 31.4 | -3.72 | -1.63 | -7.58 | 234 |
| 15 | Hold BTC | benchmark | 96.09 | -3.91 | 0 | — | 3.21 | 0.65 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.77 | -4.23 | 0 | — | -0.52 | -0.14 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.02 | 0.71 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.95 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.42 | -4.58 | 0 | — | -4.72 | -1.77 | -7.04 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.56 | 2.06 | -7.38 | 194 |
| 21 | Copy: Insider buying | copy | 94.26 | -5.74 | 25 | 40.0 | -13.46 | -2.32 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.75 | -6.25 | 95 | 23.2 | -22.39 | -7.02 | -22.70 | 121 |
| 23 | Opening range 30m | breakout | 93.74 | -6.26 | 238 | 35.3 | -9.68 | -2.74 | -17.26 | 556 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.96 | 48 | 16.7 | -18.51 | -3.78 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.95 | -7.05 | 115 | 26.1 | -16.86 | -3.74 | -20.59 | 263 |
| 26 | Daily: Momentum burst | daily | 92.55 | -7.45 | 8 | 12.5 | -16.39 | -2.92 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.47 | -7.53 | 103 | 19.4 | -10.11 | -1.96 | -12.90 | 251 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.90 | -0.88 | -11.76 | 96 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.14 | -2.14 | -16.91 | 1 |
| 30 | Agent | meta | 90.11 | -9.89 | 98 | 39.8 | -15.21 | -6.01 | -16.29 | 270 |
| 31 | Daily: Bullish score | daily | 89.72 | -10.28 | 8 | 0.0 | -7.26 | -0.85 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.44 | -10.56 | 104 | 27.9 | -11.51 | -2.05 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -10.98 | -1.95 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.93 | -11.06 | 0 | — | -3.71 | -0.43 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.78 | -12.22 | 47 | 36.2 | -14.05 | -3.21 | -15.84 | 133 |
| 36 | EMA 20/50 cross · 1h | trend | 87.54 | -12.46 | 68 | 11.8 | -22.96 | -4.19 | -25.17 | 142 |
| 37 | Stochastic reversion · 1h | reversion | 87.14 | -12.86 | 179 | 45.3 | -16.35 | -2.71 | -22.24 | 389 |
| 38 | Supertrend · 1h | trend | 86.94 | -13.06 | 104 | 15.4 | -24.28 | -4.77 | -27.40 | 217 |
| 39 | RSI momentum · 1h | momentum | 86.66 | -13.34 | 96 | 16.7 | -22.17 | -4.27 | -22.88 | 215 |
| 40 | Opening range 15m | breakout | 86.45 | -13.55 | 302 | 30.5 | -15.91 | -4.30 | -17.99 | 698 |
| 41 | Keltner breakout · 1h | breakout | 86.22 | -13.78 | 73 | 23.3 | -22.94 | -4.45 | -24.29 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.06 | -14.94 | 168 | 39.9 | -26.16 | -7.15 | -26.16 | 203 |
| 43 | MACD cross · 1h | trend | 84.79 | -15.21 | 216 | 23.1 | -28.27 | -5.16 | -29.75 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.36 | -15.64 | 96 | 15.6 | -27.61 | -5.19 | -29.45 | 215 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.74 | -23.03 | 117 |
| 46 | Z-score reversion · 1h | reversion | 83.02 | -16.98 | 104 | 33.7 | -14.08 | -2.07 | -21.32 | 200 |
| 47 | Donchian 20/10 · 1h | breakout | 82.68 | -17.32 | 93 | 20.4 | -24.80 | -4.51 | -25.48 | 226 |
| 48 | OBV trend · 1h | momentum | 82.26 | -17.74 | 198 | 17.7 | -31.46 | -6.02 | -32.11 | 300 |
| 49 | MACD zero-line · 1h | trend | 82.22 | -17.78 | 103 | 15.5 | -24.32 | -4.72 | -25.17 | 226 |
| 50 | MFI reversion · 1h | reversion | 81.96 | -18.04 | 245 | 31.4 | -18.39 | -2.84 | -21.11 | 158 |
| 51 | Williams %R · 1h | reversion | 81.88 | -18.12 | 204 | 44.1 | -33.45 | -5.33 | -37.94 | 528 |
| 52 | Three white soldiers | momentum | 81.81 | -18.19 | 266 | 19.9 | -45.17 | -18.33 | -45.19 | 599 |
| 53 | CCI reversion · 1h | reversion | 80.60 | -19.40 | 193 | 43.0 | -23.90 | -3.25 | -28.13 | 445 |
| 54 | Agent (ML meta-label) | meta | 80.23 | -19.77 | 827 | 19.0 | -16.69 | -3.18 | -18.94 | 376 |
| 55 | Bollinger reversion · 1h | reversion | 80.08 | -19.92 | 168 | 35.1 | -31.11 | -6.01 | -32.64 | 363 |
| 56 | Heikin-Ashi · 1h | trend | 79.98 | -20.02 | 260 | 23.5 | -43.26 | -9.33 | -44.09 | 669 |
| 57 | ROC + volume · 1h | momentum | 79.71 | -20.29 | 233 | 24.0 | -28.78 | -5.23 | -29.26 | 378 |
| 58 | EMA 9/21 cross · 1h | trend | 78.18 | -21.82 | 155 | 11.6 | -34.48 | -6.60 | -35.38 | 336 |
| 59 | RSI(14) reversion · 1h | reversion | 77.71 | -22.29 | 90 | 23.3 | -22.73 | -4.12 | -24.19 | 191 |
| 60 | Candlestick reversal · 1h | reversion | 77.31 | -22.69 | 243 | 29.2 | -39.44 | -7.05 | -40.85 | 565 |
| 61 | VWAP momentum · 1h | momentum | 76.96 | -23.04 | 499 | 21.4 | -50.07 | -10.27 | -51.01 | 1231 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.68 | -2.85 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 59.07 | -40.92 | 691 | 23.2 | -78.78 | -23.06 | -79.56 | 1670 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -65.09 | -20.90 | -65.25 | 849 |
| 65 | Donchian 55/20 | breakout | 56.30 | -43.70 | 540 | 20.0 | -72.73 | -20.39 | -74.14 | 1265 |
| 66 | Squeeze breakout | breakout | 55.02 | -44.98 | 534 | 14.4 | -67.75 | -24.14 | -68.47 | 1201 |
| 67 | EMA 20/50 cross | trend | 54.24 | -45.76 | 587 | 20.6 | -79.70 | -21.08 | -79.75 | 1438 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.76 | -17.25 | -77.05 | 1680 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.47 | -14.58 | -73.75 | 1519 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.87 | -33.67 | -98.88 | 5256 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.11 | -35.26 | -94.40 | 2556 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.70 | -25.13 | -89.20 | 1887 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -29.90 | -91.99 | 2336 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.89 | -25.22 | -91.01 | 2208 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.88 | -36.91 | -97.93 | 3497 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -38.60 | -97.08 | 3526 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.33 | -28.49 | -94.34 | 2539 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.36 | -29.11 | -83.36 | 1717 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -37.24 | -99.49 | 5869 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.76 | -32.34 | -93.12 | 2616 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.96 | -95.67 | 3417 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -44.35 | -99.79 | 6197 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.24 | -32.86 | -92.27 | 2331 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -40.22 | -97.75 | 3573 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -39.02 | -98.65 | 4770 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -38.42 | -94.73 | 2786 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.00 | -29.59 | -84.67 | 1776 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -41.17 | -99.59 | 6230 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.08 | -23.96 | -88.13 | 2198 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.77 | -27.31 | -88.79 | 2179 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -34.68 | -96.28 | 3805 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.74 | -34.79 | -90.03 | 2103 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.21 | -35.21 | -96.22 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.83 | -99.91 | 8244 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-22T20:00 | RSI(14) reversion · 1h | buy | BTC-USD | 8.31 | — | entry signal |
| 2026-10-22T20:00 | RSI(14) reversion · 1h | sell | SOL-USD | 4.51 | -0.06 | rebalance down |
| 2026-10-22T19:56 | Agent (rotation) | sell | SQQQ | 32.28 | 0.38 | selected signal exited |
| 2026-10-22T19:56 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 104.90 | 1.73 | target is flat |
| 2026-10-22T19:56 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 105.90 | 1.26 | target is flat |
| 2026-10-22T19:56 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 98.21 | -0.09 | target is flat |
| 2026-10-22T19:56 | Triple EMA stack · 1h | buy | TNA | 4.23 | — | rebalance up |
| 2026-10-22T19:56 | Triple EMA stack · 1h | sell | TSLA | 4.23 | 0.04 | rebalance down |
| 2026-10-22T19:56 | Squeeze breakout | sell | TNA | 11.08 | 0.03 | end-of-day flatten |
| 2026-10-22T19:56 | Squeeze breakout | sell | IWM | 11.04 | 0.00 | end-of-day flatten |
| 2026-10-22T19:56 | Squeeze breakout | sell | AAPL | 11.05 | 0.00 | end-of-day flatten |
| 2026-10-22T19:56 | Opening range 30m | sell | SQQQ | 23.91 | 0.48 | end-of-day flatten |
| 2026-10-22T19:56 | Opening range 15m | sell | SQQQ | 17.65 | 0.40 | end-of-day flatten |
| 2026-10-22T19:56 | Donchian 55/20 | sell | SQQQ | 14.31 | 0.29 | end-of-day flatten |
| 2026-10-22T19:56 | Donchian 55/20 | sell | AAPL | 14.10 | 0.03 | end-of-day flatten |
| 2026-10-22T19:56 | EMA 20/50 cross | sell | TNA | 13.58 | 0.03 | end-of-day flatten |
| 2026-10-22T19:56 | EMA 20/50 cross | sell | IWM | 13.55 | 0.00 | end-of-day flatten |
| 2026-10-22T19:56 | EMA 20/50 cross | sell | AAPL | 13.76 | 0.08 | end-of-day flatten |
| 2026-10-22T19:50 | Agent (aggressive) | sell | ETHU | 44.08 | 0.39 | selected signal exited |
| 2026-10-22T19:50 | Agent | sell | ETHU | 18.04 | 0.08 | selected signal exited |
| 2026-10-22T19:50 | MFI reversion · 1h | buy | MSTR | 5.45 | — | entry |
| 2026-10-22T19:50 | MFI reversion · 1h | buy | MSFT | 9.07 | — | entry |
| 2026-10-22T19:50 | MFI reversion · 1h | buy | GOOGL | 9.07 | — | entry |
| 2026-10-22T19:50 | MFI reversion · 1h | buy | BITX | 9.07 | — | entry |
| 2026-10-22T19:50 | MFI reversion · 1h | sell | UPRO | 6.48 | -0.00 | target is flat |
| 2026-10-22T19:50 | MFI reversion · 1h | sell | TECL | 8.07 | -0.09 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 21:15:05.000141+00:00 -> 2026-10-22 21:25:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
