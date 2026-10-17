# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T17:55:05.000166+00:00 · 26240 ticks

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

Today: 13572 decisions in 2715 calls, $0.1898 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T17:55 | 3 / 2 / 0 | cash |  |
| Breezy | 2026-10-17T17:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T17:55 | 4 / 1 / 0 | COIN 69% |  |

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
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.74 | -4.40 | -12.05 | 289 |
| 17 | Hold BTC | benchmark | 96.49 | -3.51 | 0 | — | 28.46 | 3.34 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.39 | -6.34 | -22.13 | 145 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.27 | -1.46 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.37 | 2.38 | -6.56 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.66 | -0.30 | -22.92 | 127 |
| 28 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -0.53 | 0.11 | -22.55 | 273 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -4.91 | -1.66 | -8.25 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.21 | -5.28 | -12.56 | 251 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.77 | -0.10 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 0.97 | 0.33 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.68 | 1.05 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.67 | -0.59 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -8.65 | -1.24 | -20.21 | 114 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -18.43 | -3.50 | -26.17 | 208 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.46 | -1.03 | -27.05 | 205 |
| 42 | MACD cross · 1h | trend | 88.56 | -11.44 | 175 | 22.3 | -15.29 | -2.04 | -28.65 | 457 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.61 | -7.79 | -25.98 | 235 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.42 | -0.67 | -33.87 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.80 | -13.20 | 140 | 44.3 | -20.78 | -3.80 | -22.11 | 366 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 48 | MACD zero-line · 1h | trend | 85.75 | -14.25 | 81 | 16.0 | -22.67 | -4.46 | -23.64 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.56 | 0.40 | -21.63 | 215 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.25 | -19.76 | -47.78 | 604 |
| 51 | MFI reversion · 1h | reversion | 83.93 | -16.07 | 204 | 30.4 | -21.76 | -3.61 | -22.26 | 142 |
| 52 | Z-score reversion · 1h | reversion | 83.30 | -16.70 | 86 | 31.4 | -15.58 | -2.72 | -19.86 | 181 |
| 53 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.91 | -1.70 | -27.12 | 398 |
| 54 | Heikin-Ashi · 1h | trend | 82.94 | -17.05 | 196 | 23.5 | -30.73 | -5.04 | -40.59 | 670 |
| 55 | VWAP momentum · 1h | momentum | 82.81 | -17.19 | 395 | 20.8 | -36.21 | -5.51 | -44.44 | 1250 |
| 56 | Agent (ML meta-label) | meta | 82.45 | -17.55 | 644 | 18.3 | -12.60 | -2.14 | -19.55 | 384 |
| 57 | EMA 9/21 cross · 1h | trend | 81.67 | -18.33 | 129 | 11.6 | -5.88 | -0.46 | -29.74 | 313 |
| 58 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.81 | -5.71 | -36.18 | 528 |
| 59 | Bollinger reversion · 1h | reversion | 80.03 | -19.97 | 140 | 30.7 | -30.45 | -6.34 | -32.42 | 342 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.55 | -2.59 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.46 | -2.53 | -25.90 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.77 | -6.50 | -36.17 | 536 |
| 63 | Volume breakout | breakout | 63.62 | -36.38 | 326 | 13.2 | -63.20 | -18.14 | -63.20 | 878 |
| 64 | ROC + volume | momentum | 62.97 | -37.03 | 552 | 21.9 | -75.93 | -17.80 | -77.49 | 1725 |
| 65 | Squeeze breakout | breakout | 62.42 | -37.58 | 435 | 14.5 | -62.85 | -17.90 | -64.38 | 1214 |
| 66 | RSI(14) reversion | reversion | 60.89 | -39.11 | 660 | 25.3 | -75.13 | -17.04 | -75.19 | 1643 |
| 67 | Donchian 55/20 | breakout | 60.85 | -39.15 | 441 | 17.7 | -69.07 | -14.57 | -71.83 | 1283 |
| 68 | EMA 20/50 cross | trend | 58.85 | -41.15 | 465 | 18.9 | -76.93 | -15.17 | -79.32 | 1444 |
| 69 | VWAP reversion | reversion | 54.44 | -45.56 | 691 | 23.3 | -73.60 | -15.80 | -73.72 | 1516 |
| 70 | AI bee: Boozy | ai | 53.90 | -46.10 | 315 | 6.3 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.88 | -46.12 | 615 | 15.9 | -83.18 | -26.70 | -83.18 | 1828 |
| 72 | Ichimoku | trend | 50.76 | -49.24 | 566 | 11.5 | -82.21 | -23.39 | -82.23 | 1739 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.96 | -98.60 | 5312 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.50 | -30.43 | -93.51 | 2598 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.49 | -20.50 | -87.39 | 1911 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.84 | -90.58 | 2365 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.60 | -27.27 | -91.60 | 2328 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -32.80 | -97.43 | 3524 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.77 | -36.84 | -96.77 | 3628 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.12 | -26.70 | -94.33 | 2592 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -38.10 | -99.41 | 5838 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.28 | -25.90 | -91.30 | 2641 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.21 | -32.46 | -96.21 | 3545 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.04 | -99.74 | 6240 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -29.57 | -91.74 | 2364 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -38.96 | -97.50 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.86 | -98.52 | 4779 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.72 | -33.44 | -93.72 | 2811 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -41.00 | -99.54 | 6260 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.89 | -22.66 | -86.93 | 2174 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.19 | -27.50 | -88.21 | 2162 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -33.85 | -96.01 | 3828 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -34.27 | -89.29 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.90 | -34.69 | -95.91 | 4165 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.72 | -99.89 | 8300 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-17T17:00 | VWAP reversion | buy | SOL-USD | 10.88 | — | entry signal |
| 2026-10-17T17:00 | VWAP reversion | buy | ETH-USD | 10.89 | — | entry signal |
| 2026-10-17T17:00 | VWAP reversion | buy | DOGE-USD | 10.89 | — | entry signal |
| 2026-10-17T17:00 | VWAP reversion | buy | BTC-USD | 10.89 | — | entry signal |
| 2026-10-17T17:00 | VWAP reversion | sell | XRP-USD | 2.74 | -0.02 | rebalance down |
| 2026-10-17T17:00 | RSI(14) reversion | buy | ETH-USD | 15.23 | — | entry signal |
| 2026-10-17T16:57 | Agent (ML meta-label) | sell | DOGE-USD | 7.45 | -0.06 | selected signal exited |
| 2026-10-17T16:55 | VWAP reversion | buy | XRP-USD | 5.43 | — | rebalance up |
| 2026-10-17T16:55 | VWAP reversion | sell | SOL-USD | 10.86 | -0.11 | stop-loss |
| 2026-10-17T16:55 | VWAP reversion | sell | ETH-USD | 10.87 | -0.10 | stop-loss |
| 2026-10-17T16:55 | VWAP reversion | sell | DOGE-USD | 10.89 | -0.11 | stop-loss |
| 2026-10-17T16:55 | VWAP reversion | sell | BTC-USD | 10.88 | -0.08 | stop-loss |
| 2026-10-17T16:55 | RSI(14) reversion | sell | ETH-USD | 15.19 | -0.14 | stop-loss |
| 2026-10-17T16:55 | RSI(14) reversion | sell | BTC-USD | 15.22 | -0.12 | stop-loss |
| 2026-10-17T16:45 | Agent (ML meta-label) | buy | DOGE-USD | 7.51 | — | entry |
| 2026-10-17T16:26 | Agent (ML meta-label) | sell | DOGE-USD | 4.47 | -0.04 | selected signal exited |
| 2026-10-17T16:05 | Agent (ML meta-label) | sell | ETH-USD | 4.47 | -0.04 | selected signal exited |
| 2026-10-17T16:02 | VWAP reversion | sell | DOGE-USD | 2.73 | -0.02 | rebalance down |
| 2026-10-17T16:00 | Agent (ML meta-label) | sell | XRP-USD | 1.65 | -0.02 | selected signal exited |
| 2026-10-17T16:00 | Agent (ML meta-label) | sell | SOL-USD | 3.73 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 17:55:05.000166+00:00 -> 2026-10-17 18:05:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
