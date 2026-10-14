# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T23:25:05.000153+00:00 · 22966 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 21.14 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 38461 decisions in 3356 calls, $0.4795 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T23:25 | 0 / 4 / 1 | DOGE-USD 14%, TNA 15% |  |
| Breezy | 2026-10-14T23:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T23:25 | 2 / 3 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.86 | 4.86 | 0 | — | 4.16 | 2.01 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.71 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | VWAP reversion · 1h | reversion | 101.57 | 1.57 | 45 | 40.0 | -8.36 | -2.50 | -13.79 | 122 |
| 6 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.98 | -7.55 | 43 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.86 | 0.86 | 0 | — | 4.04 | 1.60 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.62 | 0.62 | 20 | 45.0 | -16.02 | -2.56 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 100.48 | 0.48 | 0 | — | -0.98 | -0.54 | -3.44 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.13 | -0.87 | 0 | — | -1.10 | -0.43 | -3.75 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 98.92 | -1.08 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.82 | -3.91 | 21 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 98.71 | -1.28 | 0 | — | -4.93 | -2.76 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.02 | -2.07 | 67 |
| 17 | Hold BTC | benchmark | 97.76 | -2.24 | 0 | — | 28.16 | 3.29 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.12 | -2.88 | 36 | 16.7 | 5.91 | 0.87 | -22.11 | 114 |
| 19 | Trend pullback · 1h | trend | 96.98 | -3.02 | 86 | 24.4 | -24.08 | -6.94 | -24.83 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.49 | -3.51 | 91 | 30.8 | -13.07 | -4.84 | -14.67 | 278 |
| 23 | ADX DI cross · 1h | trend | 95.93 | -4.07 | 70 | 21.4 | -10.96 | -2.02 | -14.52 | 256 |
| 24 | Daily: Bullish score | daily | 95.17 | -4.83 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 95.08 | -4.92 | 13 | 38.5 | -9.94 | -0.19 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.88 | -5.12 | 0 | — | -15.33 | -2.94 | -16.54 | 1 |
| 27 | EMA 20/50 cross · 1h | trend | 94.26 | -5.74 | 48 | 16.7 | 5.12 | 0.77 | -24.13 | 136 |
| 28 | Parabolic SAR · 1h | trend | 93.90 | -6.10 | 93 | 22.6 | 0.58 | 0.27 | -23.42 | 287 |
| 29 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.42 | -6.73 | 199 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.10 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.49 | -6.51 | 149 | 22.8 | -11.64 | -1.57 | -21.42 | 453 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 93.25 | -6.75 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 33 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -5.87 | -2.11 | -9.51 | 240 |
| 34 | Stochastic reversion · 1h | reversion | 92.68 | -7.32 | 114 | 49.1 | -17.06 | -3.21 | -17.93 | 359 |
| 35 | Max aggression: 5-day momentum | meta | 92.39 | -7.61 | 8 | 37.5 | -6.02 | -0.22 | -34.64 | 27 |
| 36 | Bollinger breakout · 1h | breakout | 91.91 | -8.09 | 78 | 29.5 | 7.55 | 1.13 | -14.21 | 277 |
| 37 | RSI momentum · 1h | momentum | 91.90 | -8.10 | 73 | 17.8 | 0.45 | 0.27 | -25.52 | 226 |
| 38 | Supertrend · 1h | trend | 91.85 | -8.15 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 39 | Z-score reversion · 1h | reversion | 91.31 | -8.69 | 60 | 38.3 | -7.30 | -1.32 | -12.17 | 163 |
| 40 | Volume breakout · 1h | breakout | 90.95 | -9.05 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 41 | Ichimoku · 1h | trend | 90.51 | -9.49 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 42 | Triple EMA stack · 1h | trend | 90.34 | -9.66 | 77 | 16.9 | -10.97 | -0.99 | -34.69 | 236 |
| 43 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.92 | -2.89 | -11.27 | 121 |
| 44 | MFI reversion · 1h | reversion | 90.28 | -9.72 | 177 | 29.9 | -15.85 | -2.80 | -17.12 | 136 |
| 45 | Connors RSI(2) · 1h | reversion | 89.77 | -10.23 | 137 | 40.1 | -22.95 | -6.87 | -24.82 | 253 |
| 46 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.02 | -17.60 | 556 |
| 47 | Agent (ML meta-label) | meta | 88.66 | -11.34 | 528 | 18.6 | -1.28 | -0.05 | -13.40 | 395 |
| 48 | OBV trend · 1h | momentum | 88.23 | -11.77 | 164 | 18.9 | -11.02 | -0.97 | -35.00 | 319 |
| 49 | Keltner breakout · 1h | breakout | 87.65 | -12.36 | 51 | 21.6 | -7.31 | -0.76 | -26.76 | 215 |
| 50 | MACD zero-line · 1h | trend | 87.36 | -12.64 | 74 | 16.2 | -23.45 | -4.57 | -23.94 | 228 |
| 51 | RSI(14) reversion · 1h | reversion | 87.07 | -12.93 | 49 | 26.5 | -3.01 | -0.36 | -13.96 | 150 |
| 52 | Donchian 20/10 · 1h | breakout | 86.73 | -13.27 | 71 | 19.7 | -1.06 | 0.07 | -20.38 | 217 |
| 53 | VWAP momentum · 1h | momentum | 85.95 | -14.05 | 347 | 21.9 | -37.10 | -5.63 | -42.60 | 1242 |
| 54 | ROC + volume · 1h | momentum | 85.73 | -14.27 | 179 | 21.2 | -11.94 | -1.64 | -25.35 | 397 |
| 55 | Heikin-Ashi · 1h | trend | 85.69 | -14.31 | 169 | 26.0 | -31.64 | -5.22 | -39.47 | 665 |
| 56 | Bollinger reversion · 1h | reversion | 85.56 | -14.44 | 105 | 34.3 | -25.55 | -5.41 | -28.60 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 85.15 | -14.86 | 120 | 12.5 | -11.20 | -1.31 | -26.92 | 330 |
| 58 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.95 | -21.41 | 692 |
| 59 | Williams %R · 1h | reversion | 84.57 | -15.43 | 154 | 43.5 | -31.81 | -5.28 | -32.32 | 508 |
| 60 | CCI reversion · 1h | reversion | 84.56 | -15.44 | 130 | 42.3 | -15.33 | -2.00 | -19.36 | 416 |
| 61 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -48.92 | -22.34 | -48.92 | 594 |
| 62 | Candlestick reversal · 1h | reversion | 82.32 | -17.68 | 158 | 27.8 | -30.54 | -5.64 | -31.03 | 509 |
| 63 | ROC + volume | momentum | 67.43 | -32.57 | 483 | 21.5 | -74.15 | -16.55 | -76.27 | 1667 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.20 | -17.90 | -63.21 | 887 |
| 65 | RSI(14) reversion | reversion | 65.26 | -34.73 | 541 | 26.2 | -74.37 | -17.26 | -74.49 | 1555 |
| 66 | Squeeze breakout | breakout | 65.07 | -34.93 | 398 | 14.8 | -63.06 | -17.88 | -63.06 | 1209 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.00 | -14.50 | -70.95 | 1270 |
| 68 | EMA 20/50 cross | trend | 62.94 | -37.06 | 408 | 19.4 | -77.14 | -15.11 | -77.85 | 1428 |
| 69 | VWAP reversion | reversion | 59.50 | -40.50 | 559 | 23.6 | -73.27 | -15.26 | -73.35 | 1451 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.29 | -43.71 | 551 | 14.2 | -83.32 | -26.68 | -83.34 | 1826 |
| 72 | Supertrend ⏸ | trend | 56.10 | -43.90 | 568 | 19.0 | -86.24 | -20.08 | -86.25 | 1889 |
| 73 | Ichimoku | trend | 54.18 | -45.82 | 486 | 9.9 | -81.80 | -22.43 | -81.85 | 1700 |
| 74 | AI bee: Bizzy | ai | 51.90 | -48.10 | 989 | 8.3 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.51 | -28.93 | -98.51 | 5266 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -29.50 | -93.40 | 2565 |
| 77 | MFI reversion | reversion | 50.48 | -49.52 | 746 | 19.8 | -87.92 | -27.15 | -87.92 | 2129 |
| 78 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.54 | -24.41 | -90.54 | 2338 |
| 79 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.72 | -26.80 | -91.75 | 2344 |
| 80 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -31.88 | -97.40 | 3498 |
| 81 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -34.92 | -96.50 | 3550 |
| 82 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -24.76 | -94.44 | 2627 |
| 83 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.46 | -99.40 | 5747 |
| 84 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.08 | -25.29 | -91.08 | 2613 |
| 85 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.17 | -96.36 | 3574 |
| 86 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.33 | -99.73 | 6150 |
| 87 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.74 | -29.00 | -91.74 | 2340 |
| 88 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -36.88 | -97.39 | 3633 |
| 89 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.68 | -98.52 | 4686 |
| 90 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.47 | -32.11 | -93.47 | 2775 |
| 91 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.44 | -99.55 | 6153 |
| 92 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.23 | -22.16 | -86.23 | 2103 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -31.97 | -96.01 | 3765 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -33.77 | -89.56 | 2101 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.10 | -95.74 | 4073 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.53 | -99.89 | 8203 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T23:15 | AI bee: Bizzy | buy | DOGE-USD | 7.40 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T23:15 | Squeeze breakout | buy | DOGE-USD | 16.28 | — | entry signal |
| 2026-10-14T23:00 | Candlestick reversal · 1h | buy | ETH-USD | 3.10 | — | entry signal |
| 2026-10-14T22:55 | MFI reversion | buy | BTC-USD | 12.63 | — | entry signal |
| 2026-10-14T22:45 | MFI reversion | sell | BTC-USD | 10.12 | -0.11 | stop-loss |
| 2026-10-14T22:45 | VWAP reversion | buy | ETH-USD | 3.07 | — | rebalance up |
| 2026-10-14T22:45 | VWAP reversion | sell | BTC-USD | 11.85 | -0.14 | stop-loss |
| 2026-10-14T22:45 | Squeeze breakout | sell | XRP-USD | 16.24 | -0.12 | exit signal |
| 2026-10-14T22:37 | AI bee: Bizzy | sell | XRP-USD | 7.13 | -0.05 | Jev: sell (sell p=0.77) after 12 min |
| 2026-10-14T22:30 | VWAP reversion | buy | ETH-USD | 2.97 | — | rebalance up |
| 2026-10-14T22:30 | VWAP reversion | sell | DOGE-USD | 2.97 | -0.02 | rebalance down |
| 2026-10-14T22:27 | Agent (ML meta-label) | sell | BTC-USD | 3.14 | -0.02 | selected signal exited |
| 2026-10-14T22:25 | AI bee: Bizzy | buy | XRP-USD | 7.18 | — | Jev: buy (buy p=0.55) |
| 2026-10-14T22:20 | MFI reversion | sell | SOL-USD | 10.17 | -0.09 | exit signal |
| 2026-10-14T22:20 | MFI reversion | sell | ETH-USD | 12.62 | -0.18 | stop-loss |
| 2026-10-14T22:20 | Squeeze breakout | sell | SOL-USD | 16.17 | -0.18 | exit signal |
| 2026-10-14T22:20 | Ichimoku | sell | SOL-USD | 13.45 | -0.15 | exit signal |
| 2026-10-14T22:15 | Agent (ML meta-label) | buy | BTC-USD | 3.17 | — | entry |
| 2026-10-14T22:15 | MFI reversion · 1h | buy | XRP-USD | 8.40 | — | rebalance up |
| 2026-10-14T22:15 | MFI reversion · 1h | sell | ETH-USD | 9.58 | -0.11 | rebalance down |
| 2026-10-14T22:15 | MFI reversion · 1h | sell | DOGE-USD | 5.13 | -0.05 | rebalance down |
| 2026-10-14T22:10 | Agent (ML meta-label) | sell | BTC-USD | 3.38 | -0.03 | selected signal exited |
| 2026-10-14T22:10 | MFI reversion | sell | DOGE-USD | 12.63 | -0.13 | stop-loss |
| 2026-10-14T22:10 | Three white soldiers | sell | SOL-USD | 20.86 | -0.20 | exit signal |
| 2026-10-14T22:10 | Keltner breakout | sell | XRP-USD | 13.97 | -0.14 | exit signal |
| 2026-10-14T22:00 | Agent (rotation) | buy | ETH-USD | 2.47 | — | entry |
| 2026-10-14T22:00 | Agent (rotation) | buy | DOGE-USD | 2.47 | — | entry |
| 2026-10-14T22:00 | Agent (ML meta-label) | buy | ETH-USD | 3.17 | — | entry |
| 2026-10-14T22:00 | MFI reversion · 1h | buy | XRP-USD | 4.51 | — | entry signal |
| 2026-10-14T22:00 | MFI reversion · 1h | sell | DOGE-USD | 4.51 | -0.03 | rebalance down |
| 2026-10-14T22:00 | CCI reversion · 1h | buy | SOL-USD | 6.67 | — | entry signal |
| 2026-10-14T22:00 | CCI reversion · 1h | sell | BTC-USD | 6.67 | -0.04 | rebalance down |
| 2026-10-14T22:00 | VWAP reversion · 1h | buy | DOGE-USD | 7.81 | — | entry signal |
| 2026-10-14T22:00 | MFI reversion | buy | ETH-USD | 2.55 | — | rebalance up |
| 2026-10-14T22:00 | MFI reversion | buy | DOGE-USD | 2.68 | — | rebalance up |
| 2026-10-14T22:00 | MFI reversion | sell | XRP-USD | 10.22 | -0.02 | exit signal |
| 2026-10-14T22:00 | EMA 20/50 cross | buy | XRP-USD | 15.76 | — | entry signal |
| 2026-10-14T21:55 | EMA 20/50 cross | buy | SOL-USD | 15.77 | — | entry signal |
| 2026-10-14T21:44 | AI bee: Bizzy | sell | DOGE-USD | 7.21 | -0.07 | Jev: sell (sell p=0.90) after 10 min |
| 2026-10-14T21:40 | AI bee: Bizzy | sell | XRP-USD | 8.29 | -0.04 | Jev: sell (sell p=0.65) after 10 min |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 23:25:05.000153+00:00 -> 2026-10-14 23:35:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
