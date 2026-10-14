# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T21:27:05.000151+00:00 · 22865 ticks

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

Today: 36946 decisions in 3053 calls, $0.4583 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T21:27 | 1 / 4 / 0 | TNA 15% |  |
| Breezy | 2026-10-14T21:27 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T21:27 | 5 / 0 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.79 | +4.30% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |
| Keltner breakout | LABU | 1.69 | +7.27% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.84 | 4.84 | 0 | — | 4.15 | 2.00 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.71 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | VWAP reversion · 1h | reversion | 101.57 | 1.57 | 45 | 40.0 | -8.62 | -2.59 | -13.79 | 125 |
| 6 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.98 | -7.55 | 43 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.84 | 0.84 | 0 | — | 4.04 | 1.60 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.61 | 0.61 | 20 | 45.0 | -16.02 | -2.56 | -21.97 | 76 |
| 9 | Hold SPY | benchmark | 100.46 | 0.46 | 0 | — | -0.98 | -0.54 | -3.44 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.12 | -0.88 | 0 | — | -1.10 | -0.43 | -3.75 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 98.91 | -1.09 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.82 | -3.91 | 21 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 98.71 | -1.29 | 0 | — | -4.92 | -2.76 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.02 | -2.07 | 67 |
| 17 | Hold BTC | benchmark | 98.05 | -1.95 | 0 | — | 28.18 | 3.30 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 97.11 | -2.89 | 36 | 16.7 | 5.91 | 0.87 | -22.11 | 114 |
| 19 | Trend pullback · 1h | trend | 96.97 | -3.02 | 86 | 24.4 | -24.08 | -6.94 | -24.83 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.49 | -3.51 | 91 | 30.8 | -13.48 | -4.86 | -15.10 | 289 |
| 23 | ADX DI cross · 1h | trend | 95.93 | -4.07 | 70 | 21.4 | -10.78 | -1.98 | -14.52 | 254 |
| 24 | Daily: Bullish score | daily | 95.16 | -4.84 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 95.07 | -4.93 | 13 | 38.5 | -9.94 | -0.19 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.87 | -5.13 | 0 | — | -15.33 | -2.94 | -16.54 | 1 |
| 27 | EMA 20/50 cross · 1h | trend | 94.24 | -5.76 | 48 | 16.7 | 5.17 | 0.78 | -24.13 | 136 |
| 28 | Parabolic SAR · 1h | trend | 93.89 | -6.11 | 93 | 22.6 | 0.58 | 0.27 | -23.41 | 287 |
| 29 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.54 | 2.41 | -6.78 | 199 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.10 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.49 | -6.51 | 149 | 22.8 | -11.64 | -1.57 | -21.42 | 453 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 93.24 | -6.76 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 33 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -5.74 | -2.05 | -9.38 | 242 |
| 34 | Stochastic reversion · 1h | reversion | 92.63 | -7.37 | 114 | 49.1 | -17.18 | -3.23 | -17.93 | 362 |
| 35 | Max aggression: 5-day momentum | meta | 92.37 | -7.63 | 8 | 37.5 | -6.02 | -0.22 | -34.64 | 27 |
| 36 | Bollinger breakout · 1h | breakout | 91.91 | -8.09 | 78 | 29.5 | 7.55 | 1.13 | -14.21 | 277 |
| 37 | RSI momentum · 1h | momentum | 91.89 | -8.11 | 73 | 17.8 | 0.77 | 0.30 | -25.52 | 225 |
| 38 | Supertrend · 1h | trend | 91.84 | -8.16 | 73 | 13.7 | 1.44 | 0.38 | -23.21 | 208 |
| 39 | Z-score reversion · 1h | reversion | 91.25 | -8.75 | 60 | 38.3 | -7.27 | -1.31 | -12.17 | 162 |
| 40 | Volume breakout · 1h | breakout | 90.95 | -9.05 | 77 | 22.1 | 8.57 | 1.33 | -12.60 | 118 |
| 41 | Ichimoku · 1h | trend | 90.51 | -9.49 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 42 | Triple EMA stack · 1h | trend | 90.34 | -9.66 | 77 | 16.9 | -11.02 | -0.99 | -34.69 | 236 |
| 43 | MFI reversion · 1h | reversion | 90.33 | -9.67 | 177 | 29.9 | -16.03 | -2.82 | -17.12 | 132 |
| 44 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.75 | -2.76 | -11.10 | 123 |
| 45 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 137 | 40.1 | -23.04 | -6.92 | -24.82 | 253 |
| 46 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.02 | -17.60 | 556 |
| 47 | Agent (ML meta-label) | meta | 88.67 | -11.33 | 526 | 18.6 | 1.81 | 0.43 | -14.68 | 387 |
| 48 | OBV trend · 1h | momentum | 88.22 | -11.78 | 164 | 18.9 | -10.83 | -0.94 | -34.90 | 316 |
| 49 | Keltner breakout · 1h | breakout | 87.64 | -12.36 | 51 | 21.6 | -7.31 | -0.76 | -26.76 | 215 |
| 50 | MACD zero-line · 1h | trend | 87.35 | -12.65 | 74 | 16.2 | -23.45 | -4.57 | -23.94 | 228 |
| 51 | RSI(14) reversion · 1h | reversion | 87.02 | -12.98 | 49 | 26.5 | -2.93 | -0.35 | -13.96 | 151 |
| 52 | Donchian 20/10 · 1h | breakout | 86.73 | -13.27 | 71 | 19.7 | -1.06 | 0.07 | -20.38 | 217 |
| 53 | VWAP momentum · 1h | momentum | 85.95 | -14.05 | 347 | 21.9 | -37.10 | -5.62 | -42.74 | 1237 |
| 54 | ROC + volume · 1h | momentum | 85.73 | -14.27 | 179 | 21.2 | -11.93 | -1.64 | -25.34 | 396 |
| 55 | Heikin-Ashi · 1h | trend | 85.69 | -14.31 | 169 | 26.0 | -31.64 | -5.22 | -39.47 | 665 |
| 56 | Bollinger reversion · 1h | reversion | 85.53 | -14.47 | 105 | 34.3 | -25.56 | -5.41 | -28.60 | 329 |
| 57 | EMA 9/21 cross · 1h | trend | 85.14 | -14.86 | 120 | 12.5 | -11.03 | -1.29 | -26.93 | 329 |
| 58 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.21 | -4.95 | -21.40 | 692 |
| 59 | CCI reversion · 1h | reversion | 84.65 | -15.35 | 130 | 42.3 | -15.04 | -1.97 | -19.36 | 412 |
| 60 | Williams %R · 1h | reversion | 84.45 | -15.55 | 154 | 43.5 | -31.82 | -5.28 | -32.32 | 507 |
| 61 | Three white soldiers | momentum | 84.20 | -15.79 | 183 | 16.4 | -48.79 | -22.48 | -48.79 | 593 |
| 62 | Candlestick reversal · 1h | reversion | 82.26 | -17.74 | 158 | 27.8 | -30.77 | -5.69 | -31.06 | 508 |
| 63 | ROC + volume | momentum | 67.43 | -32.57 | 483 | 21.5 | -74.04 | -16.43 | -76.17 | 1657 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.30 | -17.79 | -63.32 | 885 |
| 65 | Squeeze breakout | breakout | 65.44 | -34.56 | 396 | 14.9 | -62.91 | -17.97 | -62.95 | 1207 |
| 66 | RSI(14) reversion | reversion | 65.26 | -34.73 | 541 | 26.2 | -74.37 | -17.27 | -74.48 | 1555 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.06 | -14.53 | -70.95 | 1271 |
| 68 | EMA 20/50 cross | trend | 63.07 | -36.93 | 408 | 19.4 | -77.18 | -15.15 | -77.77 | 1428 |
| 69 | VWAP reversion | reversion | 59.48 | -40.52 | 558 | 23.7 | -73.39 | -15.31 | -73.44 | 1456 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.42 | -43.58 | 550 | 14.2 | -83.30 | -26.77 | -83.37 | 1826 |
| 72 | Supertrend ⏸ | trend | 56.10 | -43.90 | 568 | 19.0 | -86.29 | -20.25 | -86.30 | 1891 |
| 73 | Ichimoku | trend | 54.40 | -45.60 | 485 | 9.9 | -81.72 | -22.35 | -81.85 | 1698 |
| 74 | AI bee: Bizzy | ai | 52.07 | -47.92 | 986 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 50.87 | -49.13 | 741 | 20.0 | -87.82 | -27.24 | -87.85 | 2122 |
| 76 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.53 | -29.00 | -98.53 | 5260 |
| 77 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.43 | -29.65 | -93.43 | 2568 |
| 78 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -24.56 | -90.55 | 2338 |
| 79 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.72 | -26.80 | -91.75 | 2344 |
| 80 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -32.03 | -97.42 | 3502 |
| 81 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -35.14 | -96.50 | 3531 |
| 82 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.37 | -24.76 | -94.41 | 2620 |
| 83 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.69 | -99.41 | 5750 |
| 84 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.08 | -25.28 | -91.08 | 2611 |
| 85 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.17 | -96.36 | 3574 |
| 86 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.52 | -99.73 | 6149 |
| 87 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -29.24 | -91.79 | 2344 |
| 88 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -37.05 | -97.40 | 3635 |
| 89 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -35.69 | -98.53 | 4691 |
| 90 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.45 | -32.22 | -93.46 | 2774 |
| 91 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.62 | -99.55 | 6155 |
| 92 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.21 | -22.16 | -86.23 | 2102 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -32.04 | -96.03 | 3765 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -33.83 | -89.58 | 2103 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.75 | -33.35 | -95.77 | 4077 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -44.75 | -99.89 | 8197 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T21:15 | VWAP reversion | buy | ETH-USD | 8.85 | — | entry signal |
| 2026-10-14T21:15 | VWAP reversion | sell | XRP-USD | 2.99 | -0.02 | rebalance down |
| 2026-10-14T21:10 | MFI reversion | buy | ETH-USD | 2.58 | — | rebalance up |
| 2026-10-14T21:10 | MFI reversion | sell | DOGE-USD | 10.11 | -0.13 | stop-loss |
| 2026-10-14T21:05 | AI bee: Bizzy | sell | SOL-USD | 7.59 | -0.05 | Jev: sell (sell p=0.66) after 11 min |
| 2026-10-14T21:05 | Agent (ML meta-label) | sell | ETH-USD | 7.31 | -0.17 | selected signal exited |
| 2026-10-14T21:05 | Candlestick reversal · 1h | buy | BTC-USD | 4.33 | — | entry |
| 2026-10-14T21:05 | Candlestick reversal · 1h | sell | ETH-USD | 7.43 | -0.18 | stop-loss |
| 2026-10-14T21:00 | CCI reversion · 1h | buy | BTC-USD | 20.86 | — | entry signal |
| 2026-10-14T21:00 | VWAP reversion | buy | XRP-USD | 2.98 | — | rebalance up |
| 2026-10-14T21:00 | VWAP reversion | buy | DOGE-USD | 2.98 | — | rebalance up |
| 2026-10-14T21:00 | VWAP reversion | sell | ETH-USD | 11.82 | -0.14 | stop-loss |
| 2026-10-14T20:54 | AI bee: Bizzy | buy | SOL-USD | 7.65 | — | Jev: buy (buy p=0.59) |
| 2026-10-14T20:40 | MFI reversion · 1h | buy | ETH-USD | 9.76 | — | rebalance up |
| 2026-10-14T20:40 | MFI reversion · 1h | buy | DOGE-USD | 9.74 | — | rebalance up |
| 2026-10-14T20:40 | RSI(14) reversion · 1h | sell | XRP-USD | 12.43 | -0.31 | stop-loss |
| 2026-10-14T20:40 | Squeeze breakout | sell | BTC-USD | 16.31 | -0.12 | exit signal |
| 2026-10-14T20:14 | AI bee: Bizzy | sell | SOL-USD | 7.32 | -0.05 | Jev: sell (sell p=0.81) after 10 min |
| 2026-10-14T20:04 | AI bee: Bizzy | buy | SOL-USD | 7.37 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T20:00 | MFI reversion · 1h | buy | ETH-USD | 12.94 | — | entry signal |
| 2026-10-14T20:00 | MFI reversion · 1h | buy | DOGE-USD | 12.94 | — | entry signal |
| 2026-10-14T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 103.11 | 1.70 | target is flat |
| 2026-10-14T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 102.77 | 2.24 | target is flat |
| 2026-10-14T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 98.73 | -0.08 | target is flat |
| 2026-10-14T19:55 | MFI reversion · 1h | sell | SPY | 22.67 | -0.01 | target is flat |
| 2026-10-14T19:55 | MFI reversion · 1h | sell | AMD | 22.60 | -0.04 | target is flat |
| 2026-10-14T19:55 | MFI reversion | buy | XRP-USD | 6.27 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | SOL-USD | 6.29 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | ETH-USD | 6.28 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | DOGE-USD | 8.22 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | buy | BTC-USD | 7.21 | — | rebalance up |
| 2026-10-14T19:55 | MFI reversion | sell | UPRO | 3.42 | 0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | TSLA | 3.41 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | TNA | 3.66 | 0.02 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | QQQ | 1.15 | -0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | MSFT | 3.94 | -0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | META | 1.65 | 0.00 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | ETHU | 3.67 | 0.02 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | COIN | 3.01 | -0.01 | end-of-day flatten |
| 2026-10-14T19:55 | MFI reversion | sell | AMZN | 3.01 | -0.01 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 21:27:05.000151+00:00 -> 2026-10-14 21:37:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
