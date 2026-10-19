# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T11:56:05.000155+00:00 · 28339 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.98 (-8.02%)

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
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 8730 decisions in 1746 calls, $0.1220 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T11:56 | 2 / 2 / 1 | SOL-USD 16% |  |
| Breezy | 2026-10-19T11:56 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T11:56 | 3 / 2 / 0 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.21 | +2.15% | 7 |
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.06 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.44 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.00 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.80 | 4.80 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.54 | -0.46 | 64 | 39.1 | -11.34 | -3.26 | -13.80 | 139 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 11 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 13 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 14 | Donchian 55/20 · 1h | breakout | 98.57 | -1.43 | 36 | 16.7 | -10.61 | -1.69 | -22.12 | 111 |
| 15 | Copy: Insider buying | copy | 98.14 | -1.86 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 16 | Hold BTC | benchmark | 97.71 | -2.29 | 0 | — | 27.88 | 3.29 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -4.46 | -2.28 | -5.67 | 262 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.42 | -3.58 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.46 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -0.02 | 0.04 | -5.48 | 33 |
| 23 | ADX DI cross · 1h | trend | 94.57 | -5.43 | 83 | 19.3 | -12.30 | -2.38 | -13.37 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 0.54 | 0.23 | -9.46 | 94 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.98 | -7.02 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.89 | -7.11 | 98 | 22.4 | -11.89 | -1.96 | -22.78 | 272 |
| 28 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.82 | -1.99 | -8.61 | 114 |
| 29 | Agent | meta | 91.98 | -8.02 | 77 | 39.0 | -9.45 | -5.81 | -13.80 | 231 |
| 30 | EMA 20/50 cross · 1h | trend | 91.94 | -8.06 | 55 | 14.5 | -18.90 | -3.25 | -21.74 | 130 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 34 | RSI momentum · 1h | momentum | 90.63 | -9.37 | 77 | 16.9 | -16.43 | -2.71 | -27.72 | 221 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.74 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 89.53 | -10.47 | 52 | 15.4 | -18.61 | -3.50 | -18.98 | 116 |
| 37 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 38 | Triple EMA stack · 1h | trend | 89.43 | -10.57 | 81 | 16.0 | -26.40 | -4.15 | -30.85 | 233 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.24 | -10.76 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Supertrend · 1h | trend | 88.89 | -11.11 | 85 | 11.8 | -19.60 | -3.75 | -27.02 | 214 |
| 41 | Keltner breakout · 1h | breakout | 88.40 | -11.60 | 55 | 21.8 | -8.53 | -1.03 | -27.05 | 204 |
| 42 | Connors RSI(2) · 1h | reversion | 87.89 | -12.11 | 145 | 40.0 | -24.81 | -7.63 | -25.12 | 219 |
| 43 | MACD cross · 1h | trend | 87.57 | -12.43 | 181 | 21.5 | -23.66 | -4.09 | -30.63 | 458 |
| 44 | OBV trend · 1h | momentum | 87.24 | -12.76 | 170 | 18.2 | -20.25 | -2.60 | -33.91 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.32 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.94 | -14.06 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MFI reversion · 1h | reversion | 85.03 | -14.97 | 209 | 31.1 | -21.06 | -3.24 | -23.01 | 148 |
| 49 | MACD zero-line · 1h | trend | 84.86 | -15.14 | 82 | 15.9 | -24.08 | -4.79 | -24.76 | 220 |
| 50 | Donchian 20/10 · 1h | breakout | 84.32 | -15.68 | 79 | 17.7 | 0.98 | 0.33 | -22.10 | 216 |
| 51 | Z-score reversion · 1h | reversion | 82.78 | -17.22 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 52 | Three white soldiers | momentum | 82.70 | -17.30 | 224 | 18.3 | -47.38 | -19.13 | -47.40 | 605 |
| 53 | ROC + volume · 1h | momentum | 82.47 | -17.53 | 193 | 21.2 | -11.03 | -1.29 | -27.70 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -20.66 | -3.72 | -22.11 | 378 |
| 55 | Heikin-Ashi · 1h | trend | 80.91 | -19.09 | 211 | 22.7 | -31.89 | -5.18 | -42.46 | 678 |
| 56 | EMA 9/21 cross · 1h | trend | 80.75 | -19.25 | 131 | 11.5 | -19.15 | -3.16 | -29.68 | 316 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.45 | -2.55 | -22.27 | 169 |
| 59 | Bollinger reversion · 1h | reversion | 79.87 | -20.13 | 150 | 32.0 | -30.68 | -6.34 | -33.04 | 355 |
| 60 | VWAP momentum · 1h | momentum | 79.79 | -20.21 | 415 | 20.5 | -37.10 | -5.51 | -46.96 | 1250 |
| 61 | CCI reversion · 1h | reversion | 79.02 | -20.98 | 161 | 38.5 | -20.34 | -2.64 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.10 | -23.90 | 205 | 25.4 | -36.29 | -6.52 | -37.22 | 545 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.67 | -17.46 | -77.84 | 1731 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.01 | -18.05 | -64.06 | 883 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.07 | -17.95 | -65.45 | 1213 |
| 66 | Donchian 55/20 | breakout | 59.27 | -40.73 | 463 | 17.9 | -68.68 | -14.41 | -72.80 | 1279 |
| 67 | RSI(14) reversion | reversion | 58.24 | -41.76 | 689 | 25.0 | -74.63 | -16.56 | -74.75 | 1635 |
| 68 | EMA 20/50 cross | trend | 57.14 | -42.86 | 485 | 19.0 | -75.89 | -14.69 | -80.16 | 1423 |
| 69 | VWAP reversion | reversion | 53.30 | -46.70 | 721 | 23.9 | -73.00 | -15.39 | -73.44 | 1519 |
| 70 | Keltner breakout | breakout | 51.60 | -48.40 | 651 | 15.8 | -82.68 | -26.39 | -83.30 | 1816 |
| 71 | AI bee: Boozy | ai | 50.99 | -49.01 | 345 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -30.04 | -98.67 | 5350 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -30.47 | -93.60 | 2587 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.15 | -19.98 | -87.78 | 1906 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.07 | -24.10 | -90.90 | 2351 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.18 | -25.97 | -91.18 | 2302 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -32.28 | -97.41 | 3521 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.74 | -36.98 | -96.74 | 3615 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.45 | -26.78 | -94.78 | 2590 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.94 | -23.33 | -82.82 | 1722 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -36.81 | -99.39 | 5813 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.28 | -25.66 | -91.83 | 2642 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -31.54 | -96.11 | 3522 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.36 | -99.74 | 6245 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.41 | -28.78 | -91.47 | 2350 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -39.07 | -97.56 | 3664 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.85 | -98.49 | 4764 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.67 | -33.21 | -93.73 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.20 | -99.53 | 6242 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.94 | -22.50 | -86.98 | 2179 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -27.34 | -88.24 | 2172 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.87 | -32.40 | -95.88 | 3804 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.89 | -32.17 | -89.17 | 2103 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.79 | -33.95 | -95.81 | 4156 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.41 | -99.90 | 8347 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T11:40 | VWAP reversion | buy | XRP-USD | 13.31 | — | entry signal |
| 2026-10-19T11:40 | RSI(14) reversion | buy | ETH-USD | 14.54 | — | entry signal |
| 2026-10-19T11:35 | VWAP reversion | sell | XRP-USD | 13.22 | -0.15 | stop-loss |
| 2026-10-19T11:35 | RSI(14) reversion | sell | XRP-USD | 11.59 | -0.13 | stop-loss |
| 2026-10-19T11:35 | RSI(14) reversion | sell | ETH-USD | 11.59 | -0.14 | stop-loss |
| 2026-10-19T11:00 | Connors RSI(2) · 1h | buy | BTC-USD | 21.93 | — | entry signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | XRP-USD | 23.69 | -0.17 | exit signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | SOL-USD | 23.96 | 0.12 | exit signal |
| 2026-10-19T11:00 | Three white soldiers · 1h | sell | ETH-USD | 24.01 | 0.17 | exit signal |
| 2026-10-19T11:00 | ROC + volume · 1h | buy | SOL-USD | 20.06 | — | entry signal |
| 2026-10-19T11:00 | ROC + volume · 1h | buy | BTC-USD | 20.67 | — | entry signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | XRP-USD | 15.89 | -0.08 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | SOL-USD | 13.36 | 0.07 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | ETH-USD | 13.39 | 0.09 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | DOGE-USD | 2.31 | -0.03 | exit signal |
| 2026-10-19T11:00 | VWAP momentum · 1h | sell | BTC-USD | 13.33 | 0.03 | exit signal |
| 2026-10-19T11:00 | Heikin-Ashi · 1h | sell | ETH-USD | 20.16 | -0.06 | exit signal |
| 2026-10-19T11:00 | ADX DI cross · 1h | buy | ETH-USD | 10.75 | — | entry |
| 2026-10-19T11:00 | ADX DI cross · 1h | sell | DOGE-USD | 10.75 | -0.08 | exit signal |
| 2026-10-19T11:00 | Parabolic SAR · 1h | buy | DOGE-USD | 14.02 | — | rebalance up |
| 2026-10-19T11:00 | Parabolic SAR · 1h | sell | BTC-USD | 18.60 | 0.04 | exit signal |
| 2026-10-19T10:40 | VWAP reversion | buy | XRP-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | VWAP reversion | buy | DOGE-USD | 13.37 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | XRP-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | SOL-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | ETH-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | DOGE-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | RSI(14) reversion | buy | BTC-USD | 11.73 | — | entry signal |
| 2026-10-19T10:40 | EMA 20/50 cross | sell | ETH-USD | 11.47 | 0.10 | exit signal |
| 2026-10-19T10:35 | Keltner breakout · 1h | sell | XRP-USD | 22.02 | -0.25 | stop-loss |
| 2026-10-19T10:35 | Keltner breakout · 1h | sell | SOL-USD | 21.24 | -0.34 | stop-loss |
| 2026-10-19T10:30 | Keltner breakout · 1h | sell | BTC-USD | 22.15 | -0.10 | stop-loss |
| 2026-10-19T10:30 | EMA 20/50 cross | sell | DOGE-USD | 14.24 | -0.05 | exit signal |
| 2026-10-19T10:30 | EMA 20/50 cross | sell | BTC-USD | 14.29 | 0.01 | exit signal |
| 2026-10-19T10:25 | EMA 20/50 cross | sell | XRP-USD | 14.31 | 0.06 | exit signal |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | XRP-USD | 2.88 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | DOGE-USD | 2.93 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | buy | BTC-USD | 2.91 | — | rebalance up |
| 2026-10-19T10:20 | EMA 20/50 cross | sell | SOL-USD | 11.54 | 0.17 | exit signal |
| 2026-10-19T10:02 | Triple EMA stack · 1h | buy | XRP-USD | 4.48 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 11:56:05.000155+00:00 -> 2026-10-19 12:06:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
