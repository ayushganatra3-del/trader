# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T15:25:05.000128+00:00 · 26118 ticks

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

Today: 11742 decisions in 2349 calls, $0.1642 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T15:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-17T15:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T15:25 | 1 / 2 / 2 | COIN 69% |  |

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
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.55 | -4.32 | -11.87 | 285 |
| 17 | Hold BTC | benchmark | 96.64 | -3.36 | 0 | — | 28.29 | 3.33 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.30 | -6.34 | -22.13 | 145 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.27 | -1.46 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.01 | -6.99 | 96 | 21.9 | -0.38 | 0.13 | -22.55 | 273 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -4.41 | -0.41 | -22.92 | 129 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.45 | -1.86 | -8.77 | 122 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.13 | -5.38 | -12.68 | 248 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.77 | -0.10 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.39 | 0.38 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.68 | 1.05 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.70 | -0.60 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -18.43 | -3.50 | -26.17 | 208 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.91 | -0.95 | -27.05 | 203 |
| 42 | MACD cross · 1h | trend | 88.70 | -11.30 | 173 | 22.5 | -15.05 | -2.00 | -28.45 | 457 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.62 | -7.79 | -25.98 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.85 | -0.72 | -34.23 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.82 | -13.18 | 140 | 44.3 | -20.77 | -3.79 | -22.11 | 366 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.84 | -14.15 | 80 | 16.2 | -22.70 | -4.48 | -23.56 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.56 | 0.40 | -21.63 | 215 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.11 | -19.18 | -47.98 | 599 |
| 51 | MFI reversion · 1h | reversion | 83.96 | -16.04 | 204 | 30.4 | -19.40 | -3.29 | -19.95 | 141 |
| 52 | Z-score reversion · 1h | reversion | 83.31 | -16.69 | 86 | 31.4 | -15.56 | -2.71 | -19.86 | 181 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.61 | -1.66 | -27.07 | 397 |
| 54 | Heikin-Ashi · 1h | trend | 82.94 | -17.05 | 196 | 23.5 | -31.09 | -5.11 | -40.90 | 670 |
| 55 | VWAP momentum · 1h | momentum | 82.81 | -17.19 | 395 | 20.8 | -36.21 | -5.51 | -44.44 | 1250 |
| 56 | Agent (ML meta-label) | meta | 82.75 | -17.25 | 633 | 18.6 | -13.17 | -2.27 | -19.61 | 391 |
| 57 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -6.20 | -0.50 | -29.74 | 314 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.71 | -5.69 | -36.00 | 528 |
| 59 | Bollinger reversion · 1h | reversion | 80.04 | -19.96 | 140 | 30.7 | -30.43 | -6.33 | -32.42 | 342 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.54 | -2.59 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.37 | -2.51 | -25.67 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.93 | -6.48 | -36.48 | 534 |
| 63 | Volume breakout | breakout | 63.62 | -36.38 | 326 | 13.2 | -63.18 | -18.13 | -63.18 | 877 |
| 64 | ROC + volume | momentum | 62.97 | -37.03 | 552 | 21.9 | -75.91 | -17.80 | -77.48 | 1722 |
| 65 | Squeeze breakout | breakout | 62.42 | -37.58 | 435 | 14.5 | -62.92 | -17.96 | -64.38 | 1215 |
| 66 | RSI(14) reversion | reversion | 61.46 | -38.53 | 656 | 25.5 | -74.61 | -16.83 | -74.65 | 1631 |
| 67 | Donchian 55/20 | breakout | 60.85 | -39.15 | 441 | 17.7 | -69.07 | -14.57 | -71.83 | 1283 |
| 68 | EMA 20/50 cross | trend | 58.85 | -41.15 | 465 | 18.9 | -77.01 | -15.22 | -79.32 | 1446 |
| 69 | VWAP reversion | reversion | 55.08 | -44.92 | 685 | 23.5 | -73.70 | -15.80 | -73.71 | 1514 |
| 70 | AI bee: Boozy | ai | 53.98 | -46.02 | 314 | 6.4 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.88 | -46.12 | 615 | 15.9 | -83.21 | -26.79 | -83.21 | 1829 |
| 72 | Ichimoku | trend | 50.76 | -49.24 | 566 | 11.5 | -82.21 | -23.39 | -82.24 | 1739 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -30.16 | -98.62 | 5315 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -30.50 | -93.51 | 2599 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.56 | -20.62 | -87.38 | 1914 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.49 | -24.94 | -90.58 | 2367 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.60 | -27.27 | -91.60 | 2328 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -33.05 | -97.45 | 3528 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.81 | -37.25 | -96.81 | 3631 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -26.74 | -94.29 | 2589 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -38.04 | -99.40 | 5832 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.34 | -26.05 | -91.34 | 2644 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -32.64 | -96.29 | 3559 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.32 | -99.74 | 6239 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -29.85 | -91.78 | 2368 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -38.96 | -97.50 | 3663 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -37.98 | -98.51 | 4775 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.73 | -33.62 | -93.73 | 2810 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -41.10 | -99.54 | 6255 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.82 | -22.74 | -86.84 | 2169 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.02 | -27.64 | -88.02 | 2163 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.98 | -33.97 | -95.98 | 3825 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.28 | -34.26 | -89.28 | 2112 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -34.99 | -95.90 | 4166 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.66 | -99.89 | 8296 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T15:20 | Squeeze breakout | sell | BTC-USD | 15.52 | -0.11 | stop-loss |
| 2026-10-17T15:12 | AI bee: Boozy | sell | ETH-USD | 16.93 | -0.13 | Jev: sell |
| 2026-10-17T15:10 | ROC + volume | sell | DOGE-USD | 15.65 | -0.13 | stop-loss |
| 2026-10-17T15:05 | Agent (ML meta-label) | sell | XRP-USD | 3.69 | -0.02 | selected signal exited |
| 2026-10-17T15:05 | Agent (ML meta-label) | sell | SOL-USD | 3.75 | -0.01 | selected signal exited |
| 2026-10-17T15:05 | Agent (ML meta-label) | sell | ETH-USD | 3.74 | -0.02 | selected signal exited |
| 2026-10-17T15:05 | Agent (ML meta-label) | sell | DOGE-USD | 3.75 | -0.02 | selected signal exited |
| 2026-10-17T15:05 | Keltner breakout | sell | XRP-USD | 13.39 | -0.11 | exit signal |
| 2026-10-17T14:57 | AI bee: Boozy | buy | ETH-USD | 17.06 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T14:35 | Squeeze breakout | buy | BTC-USD | 15.63 | — | entry signal |
| 2026-10-17T14:35 | Keltner breakout | buy | XRP-USD | 13.50 | — | entry signal |
| 2026-10-17T14:30 | VWAP reversion | sell | XRP-USD | 13.78 | -0.01 | target is flat |
| 2026-10-17T14:30 | RSI(14) reversion | sell | SOL-USD | 15.37 | -0.05 | exit signal |
| 2026-10-17T14:25 | ROC + volume | buy | DOGE-USD | 15.77 | — | entry |
| 2026-10-17T14:20 | RSI(14) reversion | sell | DOGE-USD | 15.37 | -0.01 | exit signal |
| 2026-10-17T14:10 | RSI(14) reversion | sell | XRP-USD | 15.34 | -0.03 | exit signal |
| 2026-10-17T14:05 | Agent (ML meta-label) | buy | XRP-USD | 3.71 | — | entry |
| 2026-10-17T14:05 | Agent (ML meta-label) | buy | SOL-USD | 3.76 | — | entry |
| 2026-10-17T14:05 | Agent (ML meta-label) | buy | ETH-USD | 3.76 | — | entry |
| 2026-10-17T14:05 | Agent (ML meta-label) | buy | DOGE-USD | 3.76 | — | entry |
| 2026-10-17T14:00 | Bollinger reversion · 1h | buy | DOGE-USD | 8.01 | — | entry signal |
| 2026-10-17T14:00 | MACD cross · 1h | buy | BTC-USD | 4.01 | — | rebalance up |
| 2026-10-17T14:00 | MACD cross · 1h | sell | XRP-USD | 4.01 | -0.06 | exit signal |
| 2026-10-17T14:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 20.30 | -0.23 | exit signal |
| 2026-10-17T13:25 | RSI(14) reversion | buy | XRP-USD | 15.37 | — | entry signal |
| 2026-10-17T13:20 | RSI(14) reversion | buy | DOGE-USD | 15.37 | — | entry |
| 2026-10-17T13:15 | RSI(14) reversion | sell | DOGE-USD | 15.28 | -0.14 | stop-loss |
| 2026-10-17T13:06 | Agent (ML meta-label) | sell | XRP-USD | 2.78 | -0.01 | selected signal exited |
| 2026-10-17T13:06 | Agent (ML meta-label) | sell | ETH-USD | 3.05 | -0.02 | selected signal exited |
| 2026-10-17T13:06 | Agent (ML meta-label) | sell | DOGE-USD | 3.06 | -0.01 | selected signal exited |
| 2026-10-17T13:06 | RSI(14) reversion | buy | SOL-USD | 15.42 | — | entry signal |
| 2026-10-17T13:06 | RSI(14) reversion | buy | DOGE-USD | 15.42 | — | entry signal |
| 2026-10-17T13:00 | Agent (ML meta-label) | sell | SOL-USD | 3.05 | -0.02 | selected signal exited |
| 2026-10-17T13:00 | Agent (ML meta-label) | sell | BTC-USD | 3.05 | -0.02 | selected signal exited |
| 2026-10-17T13:00 | VWAP momentum · 1h | sell | ETH-USD | 20.64 | -0.16 | exit signal |
| 2026-10-17T13:00 | Heikin-Ashi · 1h | sell | ETH-USD | 20.73 | -0.14 | exit signal |
| 2026-10-17T13:00 | MACD cross · 1h | buy | ETH-USD | 10.99 | — | entry |
| 2026-10-17T13:00 | MACD cross · 1h | sell | SOL-USD | 10.99 | -0.17 | exit signal |
| 2026-10-17T13:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 20.21 | -0.35 | exit signal |
| 2026-10-17T13:00 | VWAP reversion | buy | XRP-USD | 13.80 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 15:25:05.000128+00:00 -> 2026-10-17 15:35:05.000128+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
