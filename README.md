# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T18:25:05.000144+00:00 · 26268 ticks

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

Today: 13992 decisions in 2799 calls, $0.1957 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T18:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-17T18:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T18:25 | 2 / 3 / 0 | ETH-USD 31% |  |

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
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.39 | -3.30 | -13.80 | 134 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.94 | 1.65 | -2.15 | 66 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.45 | -4.42 | -11.67 | 290 |
| 17 | Hold BTC | benchmark | 96.68 | -3.32 | 0 | — | 28.55 | 3.35 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -20.60 | -6.21 | -20.94 | 143 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.27 | -1.46 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -12.58 | -1.93 | -21.23 | 126 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.42 | -1.85 | -8.74 | 122 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.94 | -5.30 | -12.50 | 249 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.77 | -0.10 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.30 | 0.36 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.68 | 1.05 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.33 | -0.55 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -18.43 | -3.50 | -26.17 | 208 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.17 | -0.99 | -27.05 | 204 |
| 42 | MACD cross · 1h | trend | 88.56 | -11.44 | 175 | 22.3 | -15.27 | -2.04 | -28.65 | 457 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.62 | -7.79 | -25.98 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.42 | -0.67 | -34.04 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.84 | -13.16 | 140 | 44.3 | -20.77 | -3.79 | -22.11 | 368 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.67 | -4.46 | -23.64 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.56 | 0.40 | -21.63 | 215 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.03 | -19.09 | -47.90 | 598 |
| 51 | MFI reversion · 1h | reversion | 83.97 | -16.03 | 204 | 30.4 | -20.96 | -3.46 | -21.51 | 142 |
| 52 | Z-score reversion · 1h | reversion | 83.32 | -16.68 | 86 | 31.4 | -15.55 | -2.71 | -19.86 | 182 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.84 | -1.69 | -27.07 | 397 |
| 54 | Heikin-Ashi · 1h | trend | 82.94 | -17.05 | 196 | 23.5 | -30.73 | -5.04 | -40.59 | 670 |
| 55 | VWAP momentum · 1h | momentum | 82.81 | -17.19 | 395 | 20.8 | -36.21 | -5.51 | -44.44 | 1250 |
| 56 | Agent (ML meta-label) | meta | 82.43 | -17.57 | 649 | 18.2 | -12.72 | -2.05 | -21.35 | 375 |
| 57 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -5.88 | -0.46 | -29.74 | 313 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.81 | -5.71 | -36.19 | 531 |
| 59 | Bollinger reversion · 1h | reversion | 80.06 | -19.94 | 140 | 30.7 | -30.44 | -6.33 | -32.42 | 345 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.53 | -2.59 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.35 | -2.51 | -25.90 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.10 | -6.52 | -36.66 | 537 |
| 63 | Volume breakout | breakout | 63.54 | -36.46 | 326 | 13.2 | -63.25 | -18.18 | -63.27 | 880 |
| 64 | ROC + volume | momentum | 62.90 | -37.10 | 552 | 21.9 | -75.96 | -17.83 | -77.54 | 1725 |
| 65 | Squeeze breakout | breakout | 62.36 | -37.64 | 435 | 14.5 | -62.88 | -17.92 | -64.44 | 1216 |
| 66 | Donchian 55/20 | breakout | 60.85 | -39.15 | 441 | 17.7 | -69.07 | -14.57 | -71.83 | 1283 |
| 67 | RSI(14) reversion | reversion | 60.85 | -39.15 | 662 | 25.2 | -74.69 | -16.87 | -74.73 | 1634 |
| 68 | EMA 20/50 cross | trend | 58.85 | -41.15 | 465 | 18.9 | -76.93 | -15.17 | -79.32 | 1444 |
| 69 | VWAP reversion | reversion | 54.55 | -45.45 | 692 | 23.3 | -73.54 | -15.76 | -73.71 | 1515 |
| 70 | AI bee: Boozy | ai | 53.87 | -46.13 | 315 | 6.3 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.84 | -46.16 | 615 | 15.9 | -83.19 | -26.72 | -83.19 | 1829 |
| 72 | Ichimoku | trend | 50.73 | -49.27 | 566 | 11.5 | -82.22 | -23.40 | -82.25 | 1740 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.89 | -98.60 | 5308 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -30.43 | -93.51 | 2598 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.53 | -20.53 | -87.43 | 1915 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.48 | -24.87 | -90.61 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.60 | -27.27 | -91.60 | 2329 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -32.78 | -97.43 | 3528 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -36.83 | -96.78 | 3625 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.09 | -26.67 | -94.31 | 2586 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.94 | -99.41 | 5837 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.30 | -25.92 | -91.34 | 2646 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.21 | -32.46 | -96.21 | 3546 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.04 | -99.74 | 6240 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.63 | -91.76 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -38.96 | -97.51 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.86 | -98.52 | 4779 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -33.39 | -93.71 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.99 | -99.54 | 6260 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.79 | -22.46 | -86.82 | 2170 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.04 | -27.53 | -88.05 | 2167 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -33.84 | -96.02 | 3828 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -33.79 | -89.24 | 2111 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -34.69 | -95.91 | 4165 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.42 | -99.89 | 8297 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T18:20 | VWAP reversion | buy | SOL-USD | 2.74 | — | rebalance up |
| 2026-10-17T18:20 | VWAP reversion | sell | BTC-USD | 10.86 | -0.03 | exit signal |
| 2026-10-17T18:13 | AI bee: Boozy | buy | ETH-USD | 16.85 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T18:05 | Agent (ML meta-label) | sell | XRP-USD | 2.31 | -0.01 | selected signal exited |
| 2026-10-17T18:05 | Agent (ML meta-label) | sell | SOL-USD | 3.05 | -0.01 | selected signal exited |
| 2026-10-17T18:05 | Agent (ML meta-label) | sell | ETH-USD | 3.17 | -0.01 | selected signal exited |
| 2026-10-17T18:05 | Agent (ML meta-label) | sell | DOGE-USD | 3.05 | -0.01 | selected signal exited |
| 2026-10-17T18:05 | Agent (ML meta-label) | sell | BTC-USD | 3.04 | -0.01 | selected signal exited |
| 2026-10-17T18:05 | RSI(14) reversion | sell | XRP-USD | 15.28 | -0.05 | exit signal |
| 2026-10-17T18:05 | RSI(14) reversion | sell | ETH-USD | 15.22 | -0.01 | take-profit |
| 2026-10-17T18:05 | Volume breakout | buy | XRP-USD | 15.91 | — | entry signal |
| 2026-10-17T18:05 | Volume breakout | buy | BTC-USD | 15.91 | — | entry signal |
| 2026-10-17T18:05 | Squeeze breakout | buy | XRP-USD | 15.61 | — | entry signal |
| 2026-10-17T18:05 | Squeeze breakout | buy | DOGE-USD | 15.61 | — | entry signal |
| 2026-10-17T18:05 | Keltner breakout | buy | BTC-USD | 13.47 | — | entry signal |
| 2026-10-17T18:05 | ROC + volume | buy | XRP-USD | 15.74 | — | entry signal |
| 2026-10-17T18:05 | ROC + volume | buy | SOL-USD | 15.74 | — | entry signal |
| 2026-10-17T18:05 | Ichimoku | buy | BTC-USD | 12.69 | — | entry signal |
| 2026-10-17T18:00 | Stochastic reversion · 1h | buy | XRP-USD | 4.57 | — | entry signal |
| 2026-10-17T18:00 | Stochastic reversion · 1h | buy | SOL-USD | 4.57 | — | entry signal |
| 2026-10-17T17:55 | AI bee: Boozy | sell | ETH-USD | 16.85 | -0.08 | Jev: add (buy p=0.58) |
| 2026-10-17T17:50 | Agent (ML meta-label) | buy | XRP-USD | 2.32 | — | entry |
| 2026-10-17T17:50 | Agent (ML meta-label) | buy | SOL-USD | 3.05 | — | entry |
| 2026-10-17T17:50 | Agent (ML meta-label) | buy | DOGE-USD | 3.05 | — | entry |
| 2026-10-17T17:50 | Agent (ML meta-label) | buy | BTC-USD | 3.05 | — | entry |
| 2026-10-17T17:45 | Agent (ML meta-label) | sell | XRP-USD | 2.02 | -0.01 | selected signal exited |
| 2026-10-17T17:45 | Agent (ML meta-label) | sell | SOL-USD | 3.16 | -0.02 | selected signal exited |
| 2026-10-17T17:45 | Agent (ML meta-label) | sell | DOGE-USD | 3.16 | -0.02 | selected signal exited |
| 2026-10-17T17:45 | Agent (ML meta-label) | sell | BTC-USD | 3.16 | -0.02 | selected signal exited |
| 2026-10-17T17:40 | AI bee: Boozy | buy | ETH-USD | 16.93 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T17:26 | Agent (ML meta-label) | buy | XRP-USD | 2.03 | — | entry |
| 2026-10-17T17:26 | Agent (ML meta-label) | buy | SOL-USD | 3.17 | — | entry |
| 2026-10-17T17:26 | Agent (ML meta-label) | buy | ETH-USD | 3.17 | — | entry |
| 2026-10-17T17:26 | Agent (ML meta-label) | buy | DOGE-USD | 3.17 | — | entry |
| 2026-10-17T17:26 | Agent (ML meta-label) | buy | BTC-USD | 3.17 | — | entry |
| 2026-10-17T17:20 | Agent (ML meta-label) | sell | ETH-USD | 3.57 | -0.02 | selected signal exited |
| 2026-10-17T17:20 | Agent (ML meta-label) | sell | DOGE-USD | 3.58 | -0.01 | selected signal exited |
| 2026-10-17T17:05 | Agent (ML meta-label) | buy | ETH-USD | 3.59 | — | entry |
| 2026-10-17T17:05 | Agent (ML meta-label) | buy | DOGE-USD | 3.59 | — | entry |
| 2026-10-17T17:05 | RSI(14) reversion | sell | DOGE-USD | 15.17 | -0.16 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 18:25:05.000144+00:00 -> 2026-10-17 18:35:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
