# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-18T20:55:05.000147+00:00 · 27606 ticks

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
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 15813 decisions in 3165 calls, $0.2212 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-18T20:55 | 0 / 4 / 1 | cash |  |
| Breezy | 2026-10-18T20:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-18T20:55 | 1 / 4 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 2.34 | +2.45% | 9 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| VWAP reversion | ETHU | 1.80 | +2.34% | 5 |
| VWAP momentum · 1h | SQQQ | 1.77 | +10.81% | 7 |

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
| 8 | VWAP reversion · 1h | reversion | 99.31 | -0.69 | 62 | 37.1 | -11.78 | -3.42 | -13.80 | 137 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.92 | -1.73 | 65 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | -2.87 | -0.22 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.17 | -2.37 | -20.62 | 67 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -5.37 | -2.79 | -6.62 | 279 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 19 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -19.51 | -5.88 | -19.70 | 140 |
| 20 | Hold BTC | benchmark | 95.99 | -4.01 | 0 | — | 25.29 | 3.05 | -8.68 | 1 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.12 | -0.02 | -5.23 | 30 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 82 | 19.5 | -12.24 | -2.39 | -13.31 | 251 |
| 24 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 3.26 | 0.78 | -9.46 | 97 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.40 | -6.51 | 197 |
| 26 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 27 | Parabolic SAR · 1h | trend | 92.87 | -7.13 | 97 | 21.6 | -9.89 | -1.53 | -22.55 | 270 |
| 28 | EMA 20/50 cross · 1h | trend | 92.56 | -7.44 | 55 | 14.5 | -18.32 | -3.16 | -21.23 | 126 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.79 | -2.00 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.43 | -5.97 | -12.60 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.89 | -9.11 | 77 | 16.9 | -17.00 | -2.97 | -27.38 | 216 |
| 34 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.33 | 1.12 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -17.94 | -3.38 | -17.98 | 112 |
| 37 | Triple EMA stack · 1h | trend | 90.05 | -9.95 | 81 | 16.0 | -16.11 | -1.85 | -33.23 | 229 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 40 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -7.81 | -0.93 | -27.05 | 201 |
| 41 | Supertrend · 1h | trend | 88.87 | -11.13 | 85 | 11.8 | -22.71 | -4.71 | -26.17 | 208 |
| 42 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -24.24 | -7.43 | -25.57 | 226 |
| 43 | OBV trend · 1h | momentum | 87.64 | -12.36 | 170 | 18.2 | -24.92 | -3.79 | -33.59 | 320 |
| 44 | MACD cross · 1h | trend | 87.56 | -12.44 | 181 | 21.5 | -16.45 | -2.13 | -30.43 | 459 |
| 45 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 46 | Stochastic reversion · 1h | reversion | 86.22 | -13.78 | 145 | 43.4 | -21.40 | -3.93 | -22.24 | 371 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.46 | -14.54 | 82 | 15.9 | -19.29 | -3.34 | -24.35 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 84.68 | -15.32 | 79 | 17.7 | 1.42 | 0.38 | -21.63 | 212 |
| 50 | Three white soldiers | momentum | 83.56 | -16.44 | 216 | 18.5 | -47.34 | -19.37 | -47.62 | 602 |
| 51 | MFI reversion · 1h | reversion | 83.24 | -16.76 | 206 | 30.1 | -22.68 | -3.58 | -23.01 | 146 |
| 52 | Z-score reversion · 1h | reversion | 82.74 | -17.26 | 89 | 30.3 | -17.11 | -3.01 | -21.26 | 186 |
| 53 | ROC + volume · 1h | momentum | 82.71 | -17.29 | 193 | 21.2 | -13.20 | -1.71 | -27.31 | 394 |
| 54 | Agent (ML meta-label) | meta | 82.20 | -17.80 | 655 | 18.0 | -10.94 | -1.48 | -22.81 | 379 |
| 55 | EMA 9/21 cross · 1h | trend | 80.97 | -19.03 | 131 | 11.5 | -11.09 | -1.32 | -30.34 | 312 |
| 56 | Heikin-Ashi · 1h | trend | 80.95 | -19.05 | 206 | 22.3 | -32.42 | -5.33 | -42.19 | 678 |
| 57 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -35.75 | -5.91 | -36.83 | 528 |
| 58 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -15.30 | -2.74 | -22.21 | 165 |
| 59 | Bollinger reversion · 1h | reversion | 79.78 | -20.21 | 148 | 31.1 | -31.14 | -6.52 | -33.04 | 353 |
| 60 | VWAP momentum · 1h | momentum | 79.78 | -20.22 | 408 | 20.1 | -37.58 | -5.72 | -46.73 | 1251 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -21.07 | -2.77 | -27.30 | 425 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -36.48 | -6.61 | -37.18 | 542 |
| 63 | Volume breakout | breakout | 62.76 | -37.24 | 335 | 12.8 | -62.98 | -18.17 | -63.54 | 877 |
| 64 | ROC + volume | momentum | 62.11 | -37.89 | 560 | 21.6 | -75.92 | -17.88 | -77.82 | 1726 |
| 65 | Squeeze breakout | breakout | 61.75 | -38.25 | 444 | 14.4 | -62.87 | -17.97 | -64.76 | 1214 |
| 66 | Donchian 55/20 | breakout | 59.13 | -40.87 | 455 | 17.1 | -69.05 | -14.66 | -72.67 | 1279 |
| 67 | RSI(14) reversion | reversion | 58.60 | -41.40 | 685 | 25.1 | -74.82 | -16.84 | -74.89 | 1637 |
| 68 | EMA 20/50 cross | trend | 56.85 | -43.15 | 480 | 18.3 | -76.75 | -15.17 | -80.07 | 1434 |
| 69 | VWAP reversion | reversion | 52.66 | -47.34 | 715 | 23.4 | -73.95 | -15.81 | -74.03 | 1530 |
| 70 | Keltner breakout | breakout | 52.35 | -47.65 | 633 | 15.5 | -83.01 | -27.13 | -83.06 | 1818 |
| 71 | AI bee: Boozy | ai | 52.17 | -47.83 | 333 | 6.0 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.13 | -98.63 | 5319 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -30.64 | -93.47 | 2583 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.56 | -20.57 | -87.74 | 1909 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.32 | -24.80 | -90.87 | 2354 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.16 | -26.60 | -91.16 | 2298 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.48 | -33.06 | -97.48 | 3526 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.94 | -96.73 | 3607 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.21 | -27.16 | -94.52 | 2569 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.83 | -23.39 | -82.50 | 1722 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.63 | -99.41 | 5834 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.34 | -26.09 | -91.63 | 2636 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.11 | -32.37 | -96.11 | 3521 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.20 | -99.74 | 6236 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -29.64 | -91.70 | 2362 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -39.07 | -97.47 | 3647 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.52 | -98.53 | 4777 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.71 | -33.89 | -93.72 | 2805 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -40.61 | -99.55 | 6257 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.95 | -22.64 | -86.98 | 2179 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.35 | -27.64 | -88.40 | 2182 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -33.15 | -95.95 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -34.00 | -89.32 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.92 | -34.41 | -95.93 | 4166 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.04 | -99.90 | 8314 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-18T20:45 | RSI(14) reversion | sell | DOGE-USD | 14.59 | -0.18 | stop-loss |
| 2026-10-18T20:20 | VWAP reversion | buy | SOL-USD | 5.27 | — | entry signal |
| 2026-10-18T20:20 | VWAP reversion | sell | ETH-USD | 2.67 | -0.02 | rebalance down |
| 2026-10-18T20:20 | RSI(14) reversion | sell | BTC-USD | 11.72 | -0.10 | stop-loss |
| 2026-10-18T20:15 | VWAP reversion | buy | BTC-USD | 10.49 | — | rebalance up |
| 2026-10-18T20:15 | VWAP reversion | sell | SOL-USD | 13.09 | -0.17 | stop-loss |
| 2026-10-18T20:15 | RSI(14) reversion | buy | DOGE-USD | 2.95 | — | rebalance up |
| 2026-10-18T20:15 | RSI(14) reversion | sell | SOL-USD | 11.67 | -0.15 | stop-loss |
| 2026-10-18T20:05 | VWAP reversion | buy | BTC-USD | 2.68 | — | entry signal |
| 2026-10-18T20:05 | VWAP reversion | sell | DOGE-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-18T19:50 | VWAP reversion | buy | XRP-USD | 13.21 | — | entry signal |
| 2026-10-18T19:50 | VWAP reversion | buy | SOL-USD | 13.26 | — | entry signal |
| 2026-10-18T19:50 | VWAP reversion | buy | ETH-USD | 13.26 | — | entry signal |
| 2026-10-18T19:50 | RSI(14) reversion | buy | XRP-USD | 11.82 | — | entry signal |
| 2026-10-18T19:50 | RSI(14) reversion | buy | SOL-USD | 11.82 | — | entry signal |
| 2026-10-18T19:50 | RSI(14) reversion | buy | ETH-USD | 11.82 | — | entry signal |
| 2026-10-18T19:50 | RSI(14) reversion | buy | DOGE-USD | 11.82 | — | entry signal |
| 2026-10-18T19:50 | RSI(14) reversion | buy | BTC-USD | 11.82 | — | entry signal |
| 2026-10-18T19:45 | VWAP reversion | buy | DOGE-USD | 13.25 | — | entry signal |
| 2026-10-18T19:45 | VWAP reversion | sell | BTC-USD | 10.66 | -0.10 | stop-loss |
| 2026-10-18T19:40 | MFI reversion · 1h | sell | DOGE-USD | 20.48 | -0.52 | stop-loss |
| 2026-10-18T19:40 | Stochastic reversion · 1h | sell | ETH-USD | 4.04 | -0.08 | stop-loss |
| 2026-10-18T19:40 | Stochastic reversion · 1h | sell | DOGE-USD | 4.68 | -0.13 | stop-loss |
| 2026-10-18T19:40 | VWAP reversion · 1h | buy | SOL-USD | 6.00 | — | rebalance up |
| 2026-10-18T19:40 | VWAP reversion · 1h | sell | DOGE-USD | 7.41 | -0.10 | stop-loss |
| 2026-10-18T19:40 | Bollinger reversion · 1h | buy | SOL-USD | 1.41 | — | entry |
| 2026-10-18T19:40 | Bollinger reversion · 1h | sell | DOGE-USD | 1.41 | -0.02 | stop-loss |
| 2026-10-18T19:35 | VWAP reversion · 1h | buy | DOGE-USD | 7.51 | — | entry |
| 2026-10-18T19:35 | VWAP reversion · 1h | sell | ETH-USD | 7.51 | -0.15 | stop-loss |
| 2026-10-18T19:35 | Bollinger reversion · 1h | buy | DOGE-USD | 1.43 | — | entry |
| 2026-10-18T19:35 | Bollinger reversion · 1h | sell | ETH-USD | 1.43 | -0.03 | stop-loss |
| 2026-10-18T19:35 | VWAP reversion | sell | XRP-USD | 10.63 | -0.13 | stop-loss |
| 2026-10-18T19:35 | VWAP reversion | sell | SOL-USD | 10.63 | -0.13 | stop-loss |
| 2026-10-18T19:35 | VWAP reversion | sell | ETH-USD | 10.47 | -0.15 | stop-loss |
| 2026-10-18T19:35 | VWAP reversion | sell | DOGE-USD | 10.58 | -0.18 | stop-loss |
| 2026-10-18T19:25 | Z-score reversion · 1h | buy | BTC-USD | 11.72 | — | entry |
| 2026-10-18T19:25 | Z-score reversion · 1h | sell | ETH-USD | 11.72 | -0.14 | stop-loss |
| 2026-10-18T19:00 | MFI reversion · 1h | buy | XRP-USD | 20.98 | — | entry signal |
| 2026-10-18T19:00 | Stochastic reversion · 1h | buy | ETH-USD | 4.12 | — | entry signal |
| 2026-10-18T18:10 | RSI(14) reversion | sell | BTC-USD | 14.74 | -0.08 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-20 20:55:05.000147+00:00 -> 2026-10-18 21:05:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
