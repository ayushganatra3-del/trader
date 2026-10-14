# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T22:55:05.000177+00:00 · 22945 ticks

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

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 21.14 · VIX 16.89 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 38146 decisions in 3293 calls, $0.4751 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T22:55 | 1 / 2 / 2 | TNA 15% |  |
| Breezy | 2026-10-14T22:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T22:55 | 2 / 3 / 0 | COIN 77% |  |

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
| 5 | VWAP reversion · 1h | reversion | 101.57 | 1.57 | 45 | 40.0 | -8.71 | -2.62 | -13.79 | 125 |
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
| 17 | Hold BTC | benchmark | 97.84 | -2.16 | 0 | — | 28.18 | 3.30 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.12 | -2.88 | 36 | 16.7 | 5.91 | 0.87 | -22.11 | 114 |
| 19 | Trend pullback · 1h | trend | 96.98 | -3.02 | 86 | 24.4 | -24.08 | -6.94 | -24.83 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.49 | -3.51 | 91 | 30.8 | -13.07 | -4.85 | -14.67 | 278 |
| 23 | ADX DI cross · 1h | trend | 95.93 | -4.07 | 70 | 21.4 | -10.89 | -2.00 | -14.52 | 256 |
| 24 | Daily: Bullish score | daily | 95.17 | -4.83 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 95.08 | -4.92 | 13 | 38.5 | -9.94 | -0.19 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.88 | -5.12 | 0 | — | -15.33 | -2.94 | -16.54 | 1 |
| 27 | EMA 20/50 cross · 1h | trend | 94.26 | -5.74 | 48 | 16.7 | 5.12 | 0.77 | -24.13 | 136 |
| 28 | Parabolic SAR · 1h | trend | 93.90 | -6.10 | 93 | 22.6 | 0.58 | 0.27 | -23.42 | 287 |
| 29 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.42 | -6.73 | 199 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.10 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.49 | -6.51 | 149 | 22.8 | -11.64 | -1.57 | -21.42 | 453 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 93.25 | -6.75 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 33 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -4.83 | -1.72 | -8.85 | 238 |
| 34 | Stochastic reversion · 1h | reversion | 92.69 | -7.32 | 114 | 49.1 | -17.28 | -3.25 | -17.94 | 361 |
| 35 | Max aggression: 5-day momentum | meta | 92.39 | -7.61 | 8 | 37.5 | -6.02 | -0.22 | -34.64 | 27 |
| 36 | Bollinger breakout · 1h | breakout | 91.91 | -8.09 | 78 | 29.5 | 7.55 | 1.13 | -14.21 | 277 |
| 37 | RSI momentum · 1h | momentum | 91.90 | -8.10 | 73 | 17.8 | 0.45 | 0.27 | -25.52 | 226 |
| 38 | Supertrend · 1h | trend | 91.85 | -8.15 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 39 | Z-score reversion · 1h | reversion | 91.32 | -8.68 | 60 | 38.3 | -7.29 | -1.32 | -12.17 | 163 |
| 40 | Volume breakout · 1h | breakout | 90.95 | -9.05 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 41 | Ichimoku · 1h | trend | 90.51 | -9.49 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 42 | Triple EMA stack · 1h | trend | 90.34 | -9.66 | 77 | 16.9 | -10.98 | -0.99 | -34.69 | 236 |
| 43 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.92 | -2.89 | -11.27 | 121 |
| 44 | MFI reversion · 1h | reversion | 90.27 | -9.73 | 177 | 29.9 | -15.85 | -2.80 | -17.12 | 136 |
| 45 | Connors RSI(2) · 1h | reversion | 89.77 | -10.23 | 137 | 40.1 | -23.04 | -6.92 | -24.82 | 253 |
| 46 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.02 | -17.60 | 556 |
| 47 | Agent (ML meta-label) | meta | 88.66 | -11.34 | 528 | 18.6 | -5.57 | -0.75 | -15.47 | 389 |
| 48 | OBV trend · 1h | momentum | 88.23 | -11.77 | 164 | 18.9 | -11.02 | -0.97 | -35.00 | 319 |
| 49 | Keltner breakout · 1h | breakout | 87.65 | -12.36 | 51 | 21.6 | -7.31 | -0.76 | -26.76 | 215 |
| 50 | MACD zero-line · 1h | trend | 87.36 | -12.64 | 74 | 16.2 | -23.45 | -4.57 | -23.94 | 228 |
| 51 | RSI(14) reversion · 1h | reversion | 87.08 | -12.92 | 49 | 26.5 | -3.14 | -0.39 | -13.96 | 153 |
| 52 | Donchian 20/10 · 1h | breakout | 86.73 | -13.27 | 71 | 19.7 | -1.06 | 0.07 | -20.38 | 217 |
| 53 | VWAP momentum · 1h | momentum | 85.95 | -14.05 | 347 | 21.9 | -37.10 | -5.63 | -42.60 | 1242 |
| 54 | ROC + volume · 1h | momentum | 85.73 | -14.27 | 179 | 21.2 | -11.94 | -1.64 | -25.35 | 397 |
| 55 | Heikin-Ashi · 1h | trend | 85.69 | -14.31 | 169 | 26.0 | -31.64 | -5.22 | -39.47 | 665 |
| 56 | Bollinger reversion · 1h | reversion | 85.57 | -14.43 | 105 | 34.3 | -25.54 | -5.41 | -28.60 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 85.15 | -14.86 | 120 | 12.5 | -10.91 | -1.28 | -26.92 | 328 |
| 58 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.95 | -21.41 | 692 |
| 59 | CCI reversion · 1h | reversion | 84.58 | -15.42 | 130 | 42.3 | -15.23 | -1.99 | -19.36 | 414 |
| 60 | Williams %R · 1h | reversion | 84.56 | -15.44 | 154 | 43.5 | -31.78 | -5.28 | -32.32 | 508 |
| 61 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -49.01 | -22.45 | -49.01 | 595 |
| 62 | Candlestick reversal · 1h | reversion | 82.34 | -17.66 | 158 | 27.8 | -31.15 | -5.78 | -31.47 | 512 |
| 63 | ROC + volume | momentum | 67.43 | -32.57 | 483 | 21.5 | -74.15 | -16.55 | -76.27 | 1667 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.20 | -17.90 | -63.21 | 887 |
| 65 | RSI(14) reversion | reversion | 65.26 | -34.73 | 541 | 26.2 | -74.45 | -17.28 | -74.56 | 1557 |
| 66 | Squeeze breakout | breakout | 65.14 | -34.86 | 398 | 14.8 | -63.02 | -17.89 | -63.02 | 1208 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.00 | -14.50 | -70.95 | 1270 |
| 68 | EMA 20/50 cross | trend | 62.96 | -37.04 | 408 | 19.4 | -77.18 | -15.13 | -77.85 | 1429 |
| 69 | VWAP reversion | reversion | 59.50 | -40.50 | 559 | 23.6 | -73.27 | -15.26 | -73.35 | 1451 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.29 | -43.71 | 551 | 14.2 | -83.34 | -26.74 | -83.37 | 1827 |
| 72 | Supertrend ⏸ | trend | 56.10 | -43.90 | 568 | 19.0 | -86.23 | -20.09 | -86.25 | 1889 |
| 73 | Ichimoku | trend | 54.19 | -45.81 | 486 | 9.9 | -81.80 | -22.42 | -81.85 | 1700 |
| 74 | AI bee: Bizzy | ai | 51.93 | -48.07 | 989 | 8.3 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.53 | -29.05 | -98.53 | 5274 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.39 | -29.50 | -93.40 | 2565 |
| 77 | MFI reversion | reversion | 50.49 | -49.51 | 746 | 19.8 | -87.94 | -27.16 | -87.94 | 2130 |
| 78 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.53 | -24.43 | -90.53 | 2337 |
| 79 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.68 | -26.71 | -91.71 | 2341 |
| 80 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -31.95 | -97.42 | 3501 |
| 81 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -34.92 | -96.50 | 3550 |
| 82 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.43 | -24.82 | -94.46 | 2630 |
| 83 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.47 | -99.41 | 5751 |
| 84 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.07 | -25.30 | -91.07 | 2612 |
| 85 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.17 | -96.36 | 3574 |
| 86 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.41 | -99.73 | 6152 |
| 87 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.04 | -91.75 | 2340 |
| 88 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -36.98 | -97.39 | 3633 |
| 89 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -35.63 | -98.53 | 4689 |
| 90 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.48 | -32.20 | -93.48 | 2776 |
| 91 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.43 | -99.55 | 6154 |
| 92 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.25 | -22.15 | -86.25 | 2104 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.03 | -31.95 | -96.03 | 3766 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -33.75 | -89.50 | 2098 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.72 | -33.10 | -95.75 | 4073 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.60 | -99.89 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-14T21:35 | MFI reversion | buy | DOGE-USD | 10.08 | — | entry signal |
| 2026-10-14T21:35 | MFI reversion | sell | ETH-USD | 2.56 | -0.02 | rebalance down |
| 2026-10-14T21:35 | Three white soldiers | buy | SOL-USD | 21.05 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 22:55:05.000177+00:00 -> 2026-10-14 23:05:05.000177+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
