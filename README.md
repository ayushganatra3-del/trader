# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T01:25:05.000150+00:00 · 25400 ticks

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

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 22.89 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 975 decisions in 195 calls, $0.0137 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T01:25 | 1 / 4 / 0 | SOL-USD 18% |  |
| Breezy | 2026-10-17T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T01:25 | 2 / 3 / 0 | COIN 67% |  |

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
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.59 | -3.36 | -13.80 | 136 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.33 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -9.85 | -4.05 | -11.12 | 287 |
| 17 | Hold BTC | benchmark | 96.70 | -3.30 | 0 | — | 28.79 | 3.38 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.02 | -6.26 | -22.15 | 150 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.50 | -1.51 | -13.33 | 253 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 3.78 | 0.87 | -9.46 | 100 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.17 | 2.34 | -6.73 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.87 | -0.33 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.79 | -2.37 | -10.02 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.84 | -5.99 | -12.21 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.39 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.25 | 0.36 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.16 | 0.98 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.35 | -0.56 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.08 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | MACD cross · 1h | trend | 89.13 | -10.87 | 171 | 22.8 | -14.63 | -1.94 | -27.78 | 454 |
| 42 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.82 | -1.08 | -27.05 | 207 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.14 | -7.57 | -26.03 | 239 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.12 | -0.64 | -34.23 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.86 | -13.14 | 136 | 43.4 | -20.59 | -3.75 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.73 | -4.48 | -23.33 | 219 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.33 | 0.37 | -21.63 | 217 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.38 | -19.35 | -48.41 | 602 |
| 51 | MFI reversion · 1h | reversion | 84.04 | -15.96 | 204 | 30.4 | -20.43 | -3.48 | -21.05 | 140 |
| 52 | VWAP momentum · 1h | momentum | 83.61 | -16.39 | 388 | 21.1 | -35.87 | -5.45 | -43.85 | 1251 |
| 53 | Heikin-Ashi · 1h | trend | 83.46 | -16.54 | 191 | 24.1 | -31.93 | -5.28 | -40.65 | 677 |
| 54 | Z-score reversion · 1h | reversion | 83.40 | -16.60 | 86 | 31.4 | -15.44 | -2.69 | -19.86 | 182 |
| 55 | Agent (ML meta-label) | meta | 83.12 | -16.88 | 610 | 19.2 | -9.60 | -1.46 | -18.69 | 397 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -13.61 | -1.80 | -27.23 | 405 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.42 | -0.55 | -29.70 | 317 |
| 58 | Bollinger reversion · 1h | reversion | 80.11 | -19.89 | 138 | 31.2 | -30.26 | -6.28 | -32.42 | 345 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.39 | -5.61 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.44 | -2.57 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.11 | -2.47 | -25.51 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.41 | -6.35 | -36.41 | 529 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.13 | -18.14 | -63.13 | 877 |
| 64 | ROC + volume | momentum | 63.23 | -36.77 | 550 | 22.0 | -75.82 | -17.71 | -77.39 | 1719 |
| 65 | Squeeze breakout | breakout | 62.99 | -37.01 | 430 | 14.7 | -62.92 | -17.97 | -64.11 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.39 | -37.62 | 646 | 25.9 | -74.61 | -16.69 | -74.67 | 1633 |
| 67 | Donchian 55/20 | breakout | 61.30 | -38.70 | 437 | 17.8 | -69.17 | -14.63 | -71.81 | 1285 |
| 68 | EMA 20/50 cross | trend | 59.47 | -40.53 | 458 | 19.2 | -77.20 | -15.33 | -79.10 | 1452 |
| 69 | VWAP reversion | reversion | 55.61 | -44.39 | 679 | 23.7 | -73.38 | -15.61 | -73.49 | 1501 |
| 70 | AI bee: Boozy | ai | 55.30 | -44.70 | 303 | 6.6 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.59 | -45.41 | 608 | 16.1 | -83.41 | -27.00 | -83.50 | 1838 |
| 72 | Ichimoku | trend | 51.92 | -48.08 | 554 | 11.7 | -81.95 | -23.12 | -82.05 | 1732 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -29.87 | -98.58 | 5299 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -30.51 | -93.48 | 2600 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.50 | -20.53 | -87.10 | 1915 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.45 | -24.90 | -90.45 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.68 | -27.33 | -91.70 | 2336 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -32.87 | -97.43 | 3528 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.70 | -37.00 | -96.70 | 3614 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.29 | -26.50 | -94.36 | 2615 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.24 | -99.41 | 5844 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.34 | -26.02 | -91.34 | 2646 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -32.16 | -96.33 | 3564 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.58 | -99.73 | 6225 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -29.64 | -91.75 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.47 | -38.90 | -97.47 | 3659 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.38 | -98.50 | 4773 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.66 | -33.26 | -93.66 | 2807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.48 | -99.54 | 6257 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.64 | -22.40 | -86.64 | 2162 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.89 | -27.39 | -87.89 | 2160 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -33.58 | -96.02 | 3830 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -34.04 | -89.27 | 2112 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.86 | -34.58 | -95.86 | 4161 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.22 | -99.89 | 8305 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T01:15 | RSI(14) reversion | buy | DOGE-USD | 15.61 | — | entry signal |
| 2026-10-17T01:05 | EMA 20/50 cross | sell | DOGE-USD | 14.77 | -0.20 | stop-loss |
| 2026-10-17T01:00 | VWAP momentum · 1h | buy | SOL-USD | 20.93 | — | entry signal |
| 2026-10-17T01:00 | VWAP momentum · 1h | buy | ETH-USD | 20.93 | — | entry signal |
| 2026-10-17T01:00 | Heikin-Ashi · 1h | sell | XRP-USD | 12.00 | -0.11 | exit signal |
| 2026-10-17T01:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 16.55 | -0.22 | exit signal |
| 2026-10-17T00:55 | EMA 20/50 cross | sell | XRP-USD | 14.85 | -0.11 | exit signal |
| 2026-10-17T00:50 | Supertrend | sell | SOL-USD | 12.61 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-17T00:50 | Supertrend | sell | ETH-USD | 12.61 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-17T00:45 | Ichimoku | sell | SOL-USD | 12.90 | -0.11 | exit signal |
| 2026-10-17T00:35 | VWAP reversion | sell | ETH-USD | 13.93 | -0.02 | exit signal |
| 2026-10-17T00:35 | VWAP reversion | sell | DOGE-USD | 13.85 | -0.11 | exit signal |
| 2026-10-17T00:35 | Ichimoku | buy | SOL-USD | 13.01 | — | entry signal |
| 2026-10-17T00:25 | Supertrend | sell | XRP-USD | 12.60 | -0.12 | exit signal |
| 2026-10-17T00:20 | Supertrend | sell | DOGE-USD | 12.60 | -0.12 | exit signal |
| 2026-10-17T00:20 | EMA 20/50 cross | buy | ETH-USD | 8.93 | — | rebalance up |
| 2026-10-17T00:20 | EMA 20/50 cross | buy | DOGE-USD | 3.00 | — | rebalance up |
| 2026-10-17T00:20 | EMA 20/50 cross | sell | BTC-USD | 14.88 | -0.11 | exit signal |
| 2026-10-17T00:15 | Heikin-Ashi · 1h | buy | XRP-USD | 4.17 | — | rebalance up |
| 2026-10-17T00:15 | Heikin-Ashi · 1h | sell | SOL-USD | 4.17 | -0.02 | rebalance down |
| 2026-10-17T00:15 | VWAP reversion | sell | SOL-USD | 11.17 | 0.03 | exit signal |
| 2026-10-17T00:15 | Donchian 55/20 | sell | XRP-USD | 15.26 | -0.13 | exit signal |
| 2026-10-17T00:15 | Donchian 55/20 | sell | DOGE-USD | 15.28 | -0.10 | exit signal |
| 2026-10-17T00:15 | EMA 20/50 cross | buy | ETH-USD | 2.98 | — | rebalance up |
| 2026-10-17T00:15 | EMA 20/50 cross | sell | SOL-USD | 2.98 | -0.01 | rebalance down |
| 2026-10-17T00:00 | VWAP momentum · 1h | sell | BTC-USD | 20.80 | -0.17 | exit signal |
| 2026-10-17T00:00 | Heikin-Ashi · 1h | buy | XRP-USD | 7.94 | — | entry signal |
| 2026-10-17T00:00 | Heikin-Ashi · 1h | buy | ETH-USD | 16.77 | — | entry signal |
| 2026-10-17T00:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 16.77 | — | entry signal |
| 2026-10-17T00:00 | Supertrend | buy | XRP-USD | 12.72 | — | entry |
| 2026-10-17T00:00 | Supertrend | buy | SOL-USD | 12.72 | — | entry |
| 2026-10-17T00:00 | Supertrend | buy | ETH-USD | 12.72 | — | entry |
| 2026-10-17T00:00 | Supertrend | buy | DOGE-USD | 12.72 | — | entry |
| 2026-10-16T23:30 | Squeeze breakout | sell | ETH-USD | 15.67 | -0.11 | exit signal |
| 2026-10-16T23:25 | Keltner breakout | sell | DOGE-USD | 13.55 | -0.13 | stop-loss |
| 2026-10-16T23:25 | ROC + volume | sell | DOGE-USD | 15.73 | -0.12 | exit signal |
| 2026-10-16T23:10 | VWAP reversion | buy | DOGE-USD | 13.96 | — | entry |
| 2026-10-16T23:10 | ROC + volume | sell | SOL-USD | 15.85 | 0.01 | exit signal |
| 2026-10-16T23:05 | VWAP reversion | sell | DOGE-USD | 11.20 | 0.06 | exit signal |
| 2026-10-16T23:05 | Keltner breakout | buy | DOGE-USD | 13.68 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 01:25:05.000150+00:00 -> 2026-10-17 01:35:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
