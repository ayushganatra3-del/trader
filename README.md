# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T22:25:05.000182+00:00 · 29999 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.86 (-9.14%)

Closed trades 90, win rate 41.1%, fees £2.98, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-20)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 17.46 · last follow-through day 2026-08-04

Best bullish scores: MSFT 6.8, AMZN 6.4, PLTR 6.0, SQQQ 5.7, BITX 5.0, TSLA 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 41244 decisions in 3297 calls, $0.5082 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T22:25 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-20T22:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T22:25 | 2 / 3 / 0 | ETH-USD 68% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| VWAP reversion | BITX | 1.77 | +3.00% | 6 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.05 | 6.05 | 0 | — | 8.23 | 3.87 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.38 | 5.38 | 12 | 58.3 | 7.74 | 2.56 | -3.27 | 20 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -1.37 | -0.30 | -9.26 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.53 | -7.11 | 43 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.24 | -13.79 | 133 |
| 6 | Max aggression: 5-day momentum | meta | 100.68 | 0.68 | 9 | 44.4 | -13.29 | -0.94 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 98.96 | -1.03 | 0 | — | 0.33 | 0.24 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 62 | 35.5 | 4.20 | 2.22 | -1.45 | 61 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 98.46 | -1.54 | 0 | — | -0.73 | -0.22 | -5.15 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.05 | -3.91 | 21 |
| 13 | Hold BTC | benchmark | 98.19 | -1.81 | 0 | — | 19.36 | 2.60 | -8.68 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.04 | -1.96 | 3 | 33.3 | 4.26 | 0.99 | -7.93 | 8 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.83 | -2.18 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.93 | -3.07 | 0 | — | -4.22 | -1.62 | -7.04 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.79 | -3.21 | 0 | — | 0.02 | 0.07 | -5.31 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.56 | -3.44 | 40 | 15.0 | -14.20 | -2.86 | -15.92 | 99 |
| 19 | Copy: Insider buying | copy | 96.12 | -3.88 | 25 | 40.0 | -11.99 | -2.08 | -20.62 | 72 |
| 20 | Agent (rotation) | meta | 96.07 | -3.93 | 114 | 31.6 | -6.32 | -3.13 | -8.16 | 302 |
| 21 | Trend pullback · 1h | trend | 95.70 | -4.30 | 90 | 23.3 | -21.57 | -6.37 | -21.96 | 134 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.91 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.58 | -5.42 | 89 | 18.0 | -13.78 | -2.62 | -16.12 | 253 |
| 24 | Daily: Momentum burst | daily | 94.10 | -5.90 | 6 | 16.7 | -6.94 | -0.93 | -20.58 | 40 |
| 25 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.71 | 1.51 | -6.51 | 196 |
| 26 | Parabolic SAR · 1h | trend | 92.19 | -7.81 | 105 | 21.9 | -17.59 | -3.78 | -20.69 | 271 |
| 27 | Opening range 30m | breakout | 92.11 | -7.89 | 225 | 32.4 | -13.40 | -3.94 | -17.26 | 565 |
| 28 | Squeeze breakout · 1h | breakout | 91.86 | -8.14 | 46 | 21.7 | -3.16 | -0.70 | -11.48 | 98 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.25 | -2.34 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.12 | -8.88 | 7 | 0.0 | -7.95 | -0.90 | -13.10 | 13 |
| 31 | Agent | meta | 90.86 | -9.14 | 90 | 41.1 | -9.26 | -4.71 | -14.24 | 243 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.78 | -9.22 | 0 | — | 0.92 | 0.31 | -14.37 | 1 |
| 33 | Volume breakout · 1h | breakout | 90.75 | -9.25 | 84 | 22.6 | -12.40 | -2.23 | -13.92 | 105 |
| 34 | Bollinger breakout · 1h | breakout | 90.61 | -9.39 | 87 | 29.9 | -12.96 | -2.45 | -16.36 | 258 |
| 35 | RSI momentum · 1h | momentum | 89.44 | -10.55 | 83 | 15.7 | -24.30 | -4.76 | -25.28 | 217 |
| 36 | Connors RSI(2) · 1h | reversion | 89.42 | -10.58 | 151 | 41.7 | -22.29 | -6.70 | -23.77 | 197 |
| 37 | EMA 20/50 cross · 1h | trend | 88.79 | -11.21 | 62 | 12.9 | -19.01 | -3.52 | -21.41 | 132 |
| 38 | Supertrend · 1h | trend | 88.30 | -11.70 | 88 | 12.5 | -21.31 | -4.19 | -26.62 | 222 |
| 39 | Opening range 15m | breakout | 88.26 | -11.74 | 270 | 29.3 | -17.73 | -4.82 | -20.79 | 699 |
| 40 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -12.63 | -3.67 | -16.49 | 127 |
| 41 | Stochastic reversion · 1h | reversion | 87.75 | -12.24 | 164 | 47.0 | -14.70 | -2.47 | -22.24 | 362 |
| 42 | Keltner breakout · 1h | breakout | 87.36 | -12.64 | 60 | 21.7 | -19.81 | -3.70 | -26.64 | 207 |
| 43 | Ichimoku · 1h | trend | 86.94 | -13.06 | 60 | 13.3 | -18.96 | -3.60 | -20.25 | 119 |
| 44 | MACD cross · 1h | trend | 86.35 | -13.65 | 193 | 20.2 | -25.96 | -4.92 | -33.71 | 467 |
| 45 | Triple EMA stack · 1h | trend | 85.55 | -14.45 | 91 | 14.3 | -33.22 | -5.96 | -33.52 | 229 |
| 46 | Donchian 20/10 · 1h | breakout | 84.71 | -15.29 | 81 | 17.3 | -18.07 | -3.00 | -28.55 | 220 |
| 47 | Z-score reversion · 1h | reversion | 84.50 | -15.50 | 96 | 30.2 | -14.30 | -2.36 | -21.32 | 195 |
| 48 | OBV trend · 1h | momentum | 84.15 | -15.85 | 186 | 17.2 | -32.03 | -6.05 | -36.32 | 314 |
| 49 | MFI reversion · 1h | reversion | 83.97 | -16.04 | 220 | 30.5 | -14.87 | -2.35 | -20.43 | 140 |
| 50 | MACD zero-line · 1h | trend | 83.73 | -16.27 | 89 | 14.6 | -25.38 | -5.03 | -26.48 | 226 |
| 51 | Agent (ML meta-label) | meta | 83.65 | -16.35 | 711 | 19.1 | -4.63 | -0.73 | -15.60 | 379 |
| 52 | Three white soldiers | momentum | 82.36 | -17.64 | 252 | 19.4 | -47.00 | -18.61 | -47.63 | 616 |
| 53 | Bollinger reversion · 1h | reversion | 82.22 | -17.78 | 162 | 35.8 | -29.42 | -5.75 | -32.84 | 347 |
| 54 | ROC + volume · 1h | momentum | 81.56 | -18.44 | 203 | 21.2 | -27.10 | -4.84 | -34.11 | 394 |
| 55 | Williams %R · 1h | reversion | 81.37 | -18.63 | 195 | 43.6 | -30.71 | -4.78 | -36.49 | 524 |
| 56 | CCI reversion · 1h | reversion | 80.74 | -19.26 | 178 | 41.6 | -18.25 | -2.30 | -27.44 | 442 |
| 57 | Heikin-Ashi · 1h | trend | 80.16 | -19.84 | 232 | 20.7 | -43.78 | -9.39 | -47.30 | 671 |
| 58 | EMA 9/21 cross · 1h | trend | 79.63 | -20.37 | 143 | 10.5 | -29.28 | -6.15 | -30.12 | 326 |
| 59 | RSI(14) reversion · 1h | reversion | 79.57 | -20.43 | 83 | 22.9 | -15.38 | -2.73 | -23.28 | 184 |
| 60 | VWAP momentum · 1h | momentum | 77.86 | -22.14 | 463 | 19.9 | -45.20 | -8.18 | -50.19 | 1258 |
| 61 | Candlestick reversal · 1h | reversion | 77.38 | -22.62 | 226 | 28.8 | -37.05 | -6.90 | -38.89 | 543 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -27.91 | -1.55 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 61.61 | -38.39 | 629 | 23.1 | -77.68 | -21.91 | -78.40 | 1729 |
| 64 | Volume breakout | breakout | 61.38 | -38.62 | 379 | 14.0 | -63.52 | -19.65 | -64.06 | 868 |
| 65 | Squeeze breakout | breakout | 58.55 | -41.45 | 491 | 14.1 | -65.94 | -22.47 | -66.59 | 1202 |
| 66 | Donchian 55/20 | breakout | 57.81 | -42.19 | 503 | 19.3 | -70.52 | -17.69 | -73.50 | 1280 |
| 67 | RSI(14) reversion | reversion | 57.37 | -42.63 | 745 | 26.6 | -74.52 | -16.67 | -74.99 | 1629 |
| 68 | EMA 20/50 cross | trend | 55.95 | -44.05 | 551 | 19.4 | -76.90 | -15.98 | -80.87 | 1447 |
| 69 | VWAP reversion | reversion | 53.63 | -46.37 | 754 | 25.2 | -71.29 | -14.55 | -72.28 | 1492 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.74 | -31.35 | -98.76 | 5290 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -31.18 | -93.91 | 2590 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.52 | -20.43 | -88.38 | 1896 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.14 | -24.47 | -91.32 | 2351 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.93 | -25.97 | -91.19 | 2244 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.52 | -33.69 | -97.65 | 3520 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.64 | -37.32 | -96.74 | 3581 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.29 | -28.63 | -94.44 | 2522 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.37 | -27.67 | -82.67 | 1702 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -37.15 | -99.38 | 5744 |
| 80 | Keltner breakout | breakout | 50.27 | -49.73 | 704 | 16.8 | -83.19 | -27.94 | -83.82 | 1804 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.68 | -27.85 | -92.27 | 2624 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.96 | -32.44 | -95.96 | 3460 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.75 | -42.48 | -99.75 | 6189 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.55 | -29.66 | -91.63 | 2354 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -39.13 | -97.67 | 3609 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -37.07 | -98.47 | 4704 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.04 | -35.78 | -94.07 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -39.59 | -99.52 | 6186 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.61 | -22.37 | -87.01 | 2144 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.79 | -26.57 | -88.13 | 2146 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -33.33 | -95.97 | 3766 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.06 | -33.24 | -89.37 | 2111 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.64 | -33.64 | -95.77 | 4104 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.36 | -99.91 | 8291 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T22:05 | Donchian 55/20 | buy | BTC-USD | 5.81 | — | entry signal |
| 2026-10-20T22:05 | Donchian 55/20 | sell | XRP-USD | 2.88 | -0.01 | rebalance down |
| 2026-10-20T22:05 | Donchian 55/20 | sell | DOGE-USD | 2.90 | -0.01 | rebalance down |
| 2026-10-20T22:01 | Heikin-Ashi · 1h | buy | DOGE-USD | 7.94 | — | entry signal |
| 2026-10-20T22:01 | Donchian 55/20 | buy | ETH-USD | 14.44 | — | entry signal |
| 2026-10-20T21:35 | Volume breakout | sell | BTC-USD | 15.28 | -0.11 | exit signal |
| 2026-10-20T21:35 | Squeeze breakout | sell | DOGE-USD | 14.58 | -0.08 | exit signal |
| 2026-10-20T21:35 | Keltner breakout | sell | DOGE-USD | 12.52 | -0.07 | exit signal |
| 2026-10-20T21:35 | ROC + volume | sell | DOGE-USD | 15.33 | -0.08 | exit signal |
| 2026-10-20T21:25 | Three white soldiers | sell | XRP-USD | 20.53 | -0.12 | exit signal |
| 2026-10-20T21:25 | Three white soldiers | sell | SOL-USD | 20.55 | -0.10 | exit signal |
| 2026-10-20T21:25 | Volume breakout | sell | SOL-USD | 15.29 | -0.10 | exit signal |
| 2026-10-20T21:20 | Volume breakout | buy | BTC-USD | 15.39 | — | entry signal |
| 2026-10-20T21:15 | Donchian 55/20 | buy | SOL-USD | 14.47 | — | entry signal |
| 2026-10-20T21:10 | Keltner breakout | buy | ETH-USD | 12.58 | — | entry signal |
| 2026-10-20T21:10 | Keltner breakout | buy | BTC-USD | 12.58 | — | entry signal |
| 2026-10-20T21:01 | Volume breakout | buy | SOL-USD | 15.40 | — | entry signal |
| 2026-10-20T20:35 | RSI(14) reversion | sell | ETH-USD | 14.27 | 0.01 | take-profit |
| 2026-10-20T20:35 | Three white soldiers | buy | XRP-USD | 20.64 | — | entry signal |
| 2026-10-20T20:35 | Three white soldiers | buy | SOL-USD | 20.64 | — | entry signal |
| 2026-10-20T20:35 | Donchian 55/20 | buy | XRP-USD | 14.46 | — | entry signal |
| 2026-10-20T20:35 | ROC + volume | buy | SOL-USD | 15.41 | — | entry signal |
| 2026-10-20T20:35 | EMA 20/50 cross | buy | ETH-USD | 13.93 | — | entry signal |
| 2026-10-20T20:30 | EMA 20/50 cross | buy | SOL-USD | 13.92 | — | entry signal |
| 2026-10-20T20:20 | Three white soldiers | sell | XRP-USD | 20.58 | -0.09 | exit signal |
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | LABU | 24.57 | -0.15 | target is flat |
| 2026-10-20T19:55 | Day trade: Stocks in Play ORB | sell | IWM | 24.80 | 0.24 | target is flat |
| 2026-10-20T19:55 | Agent | sell | TSLA | 36.52 | 0.24 | selected signal exited |
| 2026-10-20T19:55 | MFI reversion · 1h | buy | IWM | 5.57 | — | entry |
| 2026-10-20T19:55 | VWAP reversion | sell | AAPL | 13.40 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | META | 14.43 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | COIN | 14.36 | 0.02 | end-of-day flatten |
| 2026-10-20T19:55 | RSI(14) reversion | sell | AAPL | 14.31 | -0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Squeeze breakout | sell | SQQQ | 14.63 | -0.04 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | UPRO | 4.90 | -0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TSLA | 5.14 | 0.03 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TQQQ | 5.09 | 0.01 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TNA | 5.20 | 0.06 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | TECL | 5.09 | 0.05 | end-of-day flatten |
| 2026-10-20T19:55 | Opening range 30m | sell | SPY | 5.12 | -0.02 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 22:25:05.000182+00:00 -> 2026-10-20 22:35:05.000182+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
