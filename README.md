# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T19:55:05.000153+00:00 · 25136 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.03 (-7.97%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.14 | -0.23 |
| SQQQ | 19.22 | +0.85 |

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

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 38627 decisions in 2959 calls, $0.4760 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T19:55 | 9 / 14 / 7 | COIN 15% |  |
| Breezy | 2026-10-16T19:55 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-16T19:55 | 5 / 22 / 3 | COIN 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.80 | 4.79 | 0 | — | 5.84 | 2.78 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.97 | -0.03 | 0 | — | 3.99 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.57 | -0.43 | 59 | 39.0 | -11.58 | -3.38 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Max aggression: 5-day momentum | meta | 98.98 | -1.02 | 8 | 37.5 | -17.02 | -1.38 | -34.64 | 26 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 12 | Donchian 55/20 · 1h | breakout | 98.89 | -1.11 | 36 | 16.7 | 9.07 | 1.22 | -22.12 | 109 |
| 13 | Hold SPY | benchmark | 98.65 | -1.35 | 0 | — | -1.59 | -0.87 | -3.23 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 98.63 | -1.37 | 3 | 33.3 | -0.17 | 0.10 | -7.93 | 9 |
| 15 | Copy: Insider buying | copy | 98.30 | -1.70 | 20 | 45.0 | -12.25 | -2.11 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.11 | -2.89 | 108 | 33.3 | -9.42 | -3.22 | -13.23 | 293 |
| 17 | Hold BTC | benchmark | 96.78 | -3.22 | 0 | — | 28.83 | 3.38 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.59 | -3.41 | 0 | — | -2.51 | -1.00 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.44 | -3.56 | 0 | — | -6.61 | -3.60 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.23 | -3.77 | 87 | 24.1 | -21.13 | -6.30 | -22.47 | 151 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.46 | -4.54 | 0 | — | -6.69 | -2.61 | -7.75 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.84 | -5.16 | 81 | 19.8 | -8.72 | -1.56 | -13.33 | 257 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Parabolic SAR · 1h | trend | 93.31 | -6.69 | 96 | 21.9 | 3.34 | 0.61 | -22.55 | 278 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 27 | Daily: Momentum burst | daily | 93.01 | -6.99 | 5 | 20.0 | -7.23 | -0.96 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.96 | -7.04 | 54 | 14.8 | -4.18 | -0.38 | -22.92 | 129 |
| 29 | Agent (aggressive) | meta | 92.27 | -7.73 | 38 | 31.6 | -5.96 | -2.05 | -9.30 | 121 |
| 30 | Agent | meta | 92.03 | -7.97 | 77 | 39.0 | -10.09 | -5.26 | -11.11 | 242 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 32 | RSI momentum · 1h | momentum | 91.24 | -8.76 | 76 | 17.1 | 0.92 | 0.32 | -26.55 | 219 |
| 33 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.72 | 0.92 | -14.21 | 273 |
| 35 | Daily: Bullish score | daily | 90.67 | -9.33 | 7 | 0.0 | -6.02 | -0.59 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.45 | -9.55 | 80 | 16.2 | -7.84 | -0.61 | -33.23 | 234 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.43 | -10.57 | 0 | — | -19.79 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.35 | -10.65 | 84 | 11.9 | -3.92 | -0.25 | -30.09 | 214 |
| 40 | MACD cross · 1h | trend | 89.22 | -10.78 | 171 | 22.8 | -14.49 | -1.92 | -27.78 | 453 |
| 41 | Keltner breakout · 1h | breakout | 89.15 | -10.85 | 52 | 23.1 | -9.20 | -1.14 | -27.05 | 210 |
| 42 | Copy: Cathie Wood (ARKK) | copy | 88.92 | -11.08 | 0 | — | -0.58 | 0.09 | -14.37 | 1 |
| 43 | OBV trend · 1h | momentum | 88.04 | -11.96 | 169 | 18.3 | -8.64 | -0.70 | -33.94 | 320 |
| 44 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.17 | -7.57 | -26.03 | 239 |
| 45 | Stochastic reversion · 1h | reversion | 86.76 | -13.24 | 136 | 43.4 | -20.75 | -3.77 | -22.11 | 368 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.09 | -4.55 | -23.33 | 220 |
| 48 | Max aggression: 1-day momentum | meta | 85.92 | -14.08 | 14 | 35.7 | -10.79 | -0.25 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 85.02 | -14.98 | 78 | 17.9 | 0.95 | 0.33 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.74 | -20.16 | -48.45 | 609 |
| 51 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -22.05 | -3.68 | -22.52 | 144 |
| 52 | Heikin-Ashi · 1h | trend | 83.96 | -16.04 | 189 | 24.3 | -31.09 | -5.13 | -40.33 | 673 |
| 53 | VWAP momentum · 1h | momentum | 83.94 | -16.06 | 387 | 21.2 | -36.06 | -5.50 | -43.85 | 1252 |
| 54 | Z-score reversion · 1h | reversion | 83.51 | -16.49 | 86 | 31.4 | -15.38 | -2.67 | -19.86 | 181 |
| 55 | Agent (ML meta-label) | meta | 83.29 | -16.70 | 608 | 19.2 | -5.47 | -0.67 | -15.19 | 378 |
| 56 | ROC + volume · 1h | momentum | 83.03 | -16.97 | 192 | 21.4 | -12.38 | -1.65 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.26 | -17.75 | 127 | 11.8 | -7.32 | -0.66 | -29.70 | 320 |
| 58 | Bollinger reversion · 1h | reversion | 80.18 | -19.82 | 138 | 31.2 | -30.24 | -6.25 | -32.42 | 341 |
| 59 | Williams %R · 1h | reversion | 80.17 | -19.83 | 180 | 42.2 | -34.48 | -5.63 | -35.92 | 525 |
| 60 | RSI(14) reversion · 1h | reversion | 80.04 | -19.95 | 74 | 20.3 | -15.01 | -2.67 | -21.70 | 168 |
| 61 | CCI reversion · 1h | reversion | 79.13 | -20.87 | 161 | 38.5 | -19.34 | -2.52 | -25.42 | 426 |
| 62 | Candlestick reversal · 1h | reversion | 76.13 | -23.87 | 205 | 25.4 | -35.15 | -6.31 | -36.06 | 530 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.09 | -18.16 | -63.11 | 879 |
| 64 | ROC + volume | momentum | 63.34 | -36.66 | 548 | 21.9 | -75.94 | -17.80 | -77.53 | 1695 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.88 | -17.98 | -63.96 | 1216 |
| 66 | RSI(14) reversion ⏸ | reversion | 62.42 | -37.58 | 646 | 25.9 | -74.82 | -16.82 | -74.90 | 1638 |
| 67 | Donchian 55/20 | breakout | 61.53 | -38.47 | 435 | 17.9 | -69.06 | -14.57 | -71.81 | 1283 |
| 68 | EMA 20/50 cross | trend | 59.96 | -40.04 | 455 | 19.3 | -77.14 | -15.25 | -79.04 | 1450 |
| 69 | AI bee: Boozy | ai | 55.70 | -44.30 | 299 | 6.7 | — | — | — | — |
| 70 | VWAP reversion | reversion | 55.58 | -44.42 | 674 | 23.6 | -73.67 | -15.64 | -73.73 | 1505 |
| 71 | Keltner breakout | breakout | 54.72 | -45.28 | 607 | 16.1 | -83.62 | -27.44 | -83.74 | 1846 |
| 72 | Ichimoku | trend | 52.02 | -47.98 | 553 | 11.8 | -81.97 | -23.14 | -82.11 | 1733 |
| 73 | Supertrend ⏸ | trend | 50.88 | -49.12 | 638 | 19.6 | -86.56 | -20.53 | -87.07 | 1916 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -29.94 | -98.62 | 5309 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -30.32 | -93.49 | 2597 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.85 | -90.54 | 2366 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.73 | -91.83 | 2346 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -32.79 | -97.45 | 3530 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.68 | -36.63 | -96.69 | 3569 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.34 | -26.65 | -94.40 | 2611 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.09 | -99.42 | 5844 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.41 | -26.18 | -91.44 | 2650 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -32.56 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.90 | -99.74 | 6232 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -29.70 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -38.70 | -97.46 | 3654 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.11 | -98.52 | 4778 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -33.60 | -93.72 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.38 | -99.55 | 6263 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.73 | -22.43 | -86.76 | 2166 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.52 | -88.23 | 2162 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.02 | -33.10 | -96.06 | 3830 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.46 | -34.54 | -89.46 | 2118 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -34.41 | -95.88 | 4160 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.82 | -99.89 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T19:55 | Agent (rotation) | sell | SQQQ | 66.05 | 2.53 | selected signal exited |
| 2026-10-16T19:55 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.67 | 1.26 | target is flat |
| 2026-10-16T19:55 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 107.79 | 4.69 | target is flat |
| 2026-10-16T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 107.08 | 3.54 | target is flat |
| 2026-10-16T19:55 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 99.09 | 0.36 | target is flat |
| 2026-10-16T19:55 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 105.88 | 5.95 | target is flat |
| 2026-10-16T19:55 | Agent (ML meta-label) | buy | ETHU | 9.26 | — | entry |
| 2026-10-16T19:55 | Agent (ML meta-label) | sell | SQQQ | 9.33 | 0.03 | selected signal exited |
| 2026-10-16T19:55 | VWAP reversion | buy | XRP-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | SOL-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | ETH-USD | 8.91 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | DOGE-USD | 8.82 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | buy | BTC-USD | 8.90 | — | rebalance up |
| 2026-10-16T19:55 | VWAP reversion | sell | UPRO | 2.42 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TSLA | 2.33 | 0.02 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TQQQ | 2.41 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TNA | 2.22 | -0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | TECL | 2.42 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | SPY | 2.32 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | QQQ | 2.41 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | PLTR | 2.24 | -0.02 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | NVDA | 2.42 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | MSTR | 2.44 | 0.03 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | MSFT | 2.24 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | META | 2.32 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | LABU | 2.24 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | IWM | 2.23 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | GOOGL | 2.33 | -0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | ETHU | 2.26 | 0.03 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | COIN | 2.34 | 0.04 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | AMZN | 2.24 | 0.00 | end-of-day flatten |
| 2026-10-16T19:55 | VWAP reversion | sell | AAPL | 2.18 | 0.01 | end-of-day flatten |
| 2026-10-16T19:55 | Opening range 30m | sell | SQQQ | 23.58 | 0.98 | end-of-day flatten |
| 2026-10-16T19:55 | Opening range 15m | sell | SQQQ | 18.28 | 0.83 | end-of-day flatten |
| 2026-10-16T19:55 | Donchian 55/20 | sell | SQQQ | 16.03 | 0.79 | end-of-day flatten |
| 2026-10-16T19:55 | ROC + volume | sell | SQQQ | 16.04 | 0.24 | end-of-day flatten |
| 2026-10-16T19:55 | Ichimoku | sell | SQQQ | 13.53 | 0.62 | end-of-day flatten |
| 2026-10-16T19:55 | EMA 20/50 cross | sell | SQQQ | 15.56 | 0.71 | end-of-day flatten |
| 2026-10-16T19:53 | AI bee: Boozy | buy | COIN | 36.89 | — | Jev: buy (buy p=0.66) |
| 2026-10-16T19:53 | AI bee: Boozy | sell | BITX | 34.28 | -0.20 | Jev: buy |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 19:55:05.000153+00:00 -> 2026-10-16 20:05:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
