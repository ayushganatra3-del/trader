# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T21:55:05.000172+00:00 · 26446 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 16662 decisions in 3333 calls, $0.2330 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T21:55 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-17T21:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T21:55 | 2 / 3 / 0 | COIN 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 2.27 | +3.35% | 6 |
| VWAP momentum · 1h | SQQQ | 2.13 | +12.90% | 7 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 2.01 | +0.94% | 8 |
| Opening range 30m | AMZN | 1.94 | +3.77% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.42 | -4.42 | -11.65 | 291 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.22 | -6.11 | -20.39 | 142 |
| 20 | Hold BTC | benchmark | 96.16 | -3.84 | 0 | — | 28.49 | 3.35 | -8.68 | 1 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | 1.64 | 0.41 | -14.97 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.32 | 0.96 | -9.46 | 98 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -18.01 | -3.09 | -21.23 | 125 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -4.91 | -1.66 | -8.25 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.21 | -5.28 | -12.56 | 251 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.77 | -0.10 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.29 | 0.36 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.63 | 1.04 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.07 | -0.52 | -33.23 | 229 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -13.47 | -2.14 | -28.00 | 209 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.86 | -0.94 | -27.05 | 202 |
| 42 | MACD cross · 1h | trend | 88.15 | -11.85 | 177 | 22.0 | -15.96 | -2.13 | -29.40 | 459 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.61 | -7.79 | -25.98 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.91 | -0.62 | -33.87 | 317 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.50 | -13.50 | 142 | 43.7 | -21.00 | -3.84 | -22.11 | 368 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.51 | -4.42 | -23.64 | 217 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 2.34 | 0.48 | -21.63 | 212 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.25 | -19.76 | -47.78 | 604 |
| 51 | MFI reversion · 1h | reversion | 83.85 | -16.14 | 204 | 30.4 | -21.83 | -3.62 | -22.26 | 142 |
| 52 | Z-score reversion · 1h | reversion | 83.20 | -16.80 | 86 | 31.4 | -16.04 | -2.81 | -20.30 | 182 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.72 | -1.67 | -27.12 | 396 |
| 54 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -9.74 | -1.33 | -17.92 | 399 |
| 55 | VWAP momentum · 1h | momentum | 81.71 | -18.29 | 398 | 20.6 | -36.97 | -5.62 | -45.23 | 1253 |
| 56 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -5.70 | -0.43 | -29.74 | 312 |
| 57 | Heikin-Ashi · 1h | trend | 81.55 | -18.45 | 201 | 22.9 | -32.05 | -5.25 | -41.72 | 675 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.81 | -36.60 | 531 |
| 59 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.66 | -2.61 | -21.70 | 162 |
| 60 | Bollinger reversion · 1h | reversion | 79.89 | -20.11 | 143 | 30.8 | -30.80 | -6.43 | -32.58 | 345 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.18 | -2.63 | -26.42 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.76 | -6.49 | -36.26 | 535 |
| 63 | Volume breakout | breakout | 63.34 | -36.66 | 329 | 13.1 | -63.41 | -18.28 | -63.41 | 882 |
| 64 | ROC + volume | momentum | 62.81 | -37.19 | 554 | 21.8 | -75.96 | -17.84 | -77.52 | 1727 |
| 65 | Squeeze breakout | breakout | 62.36 | -37.64 | 437 | 14.6 | -62.89 | -17.93 | -64.44 | 1216 |
| 66 | RSI(14) reversion | reversion | 60.75 | -39.25 | 662 | 25.2 | -74.32 | -16.61 | -74.32 | 1626 |
| 67 | Donchian 55/20 | breakout | 60.32 | -39.68 | 445 | 17.5 | -69.37 | -14.69 | -72.07 | 1286 |
| 68 | EMA 20/50 cross | trend | 57.83 | -42.17 | 470 | 18.7 | -77.19 | -15.29 | -79.69 | 1444 |
| 69 | VWAP reversion | reversion | 54.13 | -45.87 | 696 | 23.4 | -73.21 | -15.51 | -73.25 | 1509 |
| 70 | AI bee: Boozy | ai | 53.62 | -46.38 | 318 | 6.3 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.50 | -46.49 | 620 | 15.8 | -83.32 | -26.89 | -83.32 | 1833 |
| 72 | Ichimoku | trend | 50.69 | -49.31 | 567 | 11.5 | -82.17 | -23.41 | -82.18 | 1735 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -29.88 | -98.61 | 5314 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -30.60 | -93.63 | 2603 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.58 | -20.54 | -87.49 | 1912 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -24.93 | -90.65 | 2370 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.54 | -27.21 | -91.54 | 2326 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.84 | -97.46 | 3524 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -36.83 | -96.82 | 3634 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -26.43 | -94.29 | 2587 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.99 | -99.39 | 5820 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -25.99 | -91.38 | 2647 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -32.30 | -96.18 | 3539 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.86 | -99.74 | 6241 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.64 | -91.77 | 2367 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -39.03 | -97.52 | 3669 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -36.96 | -98.49 | 4769 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.75 | -33.43 | -93.75 | 2815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.92 | -99.53 | 6250 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.75 | -22.37 | -86.75 | 2167 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.13 | -27.22 | -88.14 | 2161 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -33.05 | -95.95 | 3821 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -34.17 | -89.32 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.86 | -34.01 | -95.87 | 4161 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.31 | -99.89 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T21:45 | VWAP reversion | buy | SOL-USD | 10.87 | — | entry signal |
| 2026-10-17T21:45 | VWAP reversion | buy | ETH-USD | 10.87 | — | entry signal |
| 2026-10-17T21:45 | VWAP reversion | buy | DOGE-USD | 10.87 | — | entry signal |
| 2026-10-17T21:45 | VWAP reversion | buy | BTC-USD | 10.87 | — | entry signal |
| 2026-10-17T21:45 | VWAP reversion | sell | XRP-USD | 2.77 | 0.01 | rebalance down |
| 2026-10-17T21:45 | RSI(14) reversion | buy | XRP-USD | 15.21 | — | entry signal |
| 2026-10-17T21:40 | Stochastic reversion · 1h | sell | DOGE-USD | 7.69 | -0.25 | stop-loss |
| 2026-10-17T21:40 | VWAP reversion | buy | XRP-USD | 13.57 | — | entry signal |
| 2026-10-17T21:35 | Stochastic reversion · 1h | sell | SOL-USD | 4.48 | -0.09 | stop-loss |
| 2026-10-17T21:35 | Bollinger reversion · 1h | sell | SOL-USD | 1.60 | -0.04 | stop-loss |
| 2026-10-17T21:35 | Bollinger reversion · 1h | sell | ETH-USD | 7.13 | -0.16 | stop-loss |
| 2026-10-17T21:35 | VWAP momentum · 1h | sell | BTC-USD | 20.44 | -0.26 | stop-loss |
| 2026-10-17T21:35 | Heikin-Ashi · 1h | sell | ETH-USD | 20.31 | -0.35 | stop-loss |
| 2026-10-17T21:35 | Heikin-Ashi · 1h | sell | BTC-USD | 20.38 | -0.22 | stop-loss |
| 2026-10-17T21:35 | MACD cross · 1h | sell | BTC-USD | 21.97 | -0.25 | stop-loss |
| 2026-10-17T21:30 | VWAP momentum · 1h | sell | XRP-USD | 19.51 | -0.39 | stop-loss |
| 2026-10-17T21:30 | VWAP momentum · 1h | sell | DOGE-USD | 20.25 | -0.45 | stop-loss |
| 2026-10-17T21:30 | Heikin-Ashi · 1h | buy | ETH-USD | 6.83 | — | rebalance up |
| 2026-10-17T21:30 | Heikin-Ashi · 1h | buy | BTC-USD | 6.76 | — | rebalance up |
| 2026-10-17T21:30 | Heikin-Ashi · 1h | sell | XRP-USD | 5.97 | -0.13 | stop-loss |
| 2026-10-17T21:30 | Heikin-Ashi · 1h | sell | SOL-USD | 13.50 | -0.30 | stop-loss |
| 2026-10-17T21:30 | Heikin-Ashi · 1h | sell | DOGE-USD | 13.52 | -0.30 | stop-loss |
| 2026-10-17T21:30 | MACD cross · 1h | buy | BTC-USD | 4.51 | — | rebalance up |
| 2026-10-17T21:30 | MACD cross · 1h | sell | XRP-USD | 7.90 | -0.16 | stop-loss |
| 2026-10-17T21:30 | VWAP reversion | sell | SOL-USD | 13.44 | -0.18 | stop-loss |
| 2026-10-17T21:30 | EMA 20/50 cross | sell | XRP-USD | 14.42 | -0.27 | stop-loss |
| 2026-10-17T21:30 | EMA 20/50 cross | sell | SOL-USD | 14.39 | -0.28 | stop-loss |
| 2026-10-17T21:30 | EMA 20/50 cross | sell | ETH-USD | 5.85 | -0.09 | stop-loss |
| 2026-10-17T21:30 | EMA 20/50 cross | sell | DOGE-USD | 11.54 | -0.22 | stop-loss |
| 2026-10-17T21:30 | EMA 20/50 cross | sell | BTC-USD | 11.63 | -0.13 | stop-loss |
| 2026-10-17T21:25 | Keltner breakout | sell | ETH-USD | 13.37 | -0.13 | stop-loss |
| 2026-10-17T21:25 | Keltner breakout | sell | BTC-USD | 13.39 | -0.08 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | XRP-USD | 15.05 | -0.15 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | ETH-USD | 15.07 | -0.15 | stop-loss |
| 2026-10-17T21:25 | Donchian 55/20 | sell | DOGE-USD | 15.09 | -0.12 | exit signal |
| 2026-10-17T21:25 | Donchian 55/20 | sell | BTC-USD | 15.10 | -0.11 | exit signal |
| 2026-10-17T21:25 | Ichimoku | sell | BTC-USD | 12.62 | -0.07 | exit signal |
| 2026-10-17T21:25 | EMA 20/50 cross | buy | ETH-USD | 2.94 | — | rebalance up |
| 2026-10-17T21:25 | EMA 20/50 cross | sell | BTC-USD | 2.94 | -0.02 | rebalance down |
| 2026-10-17T21:20 | Squeeze breakout | sell | DOGE-USD | 15.63 | 0.02 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 21:55:05.000172+00:00 -> 2026-10-17 22:05:05.000172+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
