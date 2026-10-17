# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T08:55:05.000146+00:00 · 25785 ticks

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

Today: 6747 decisions in 1350 calls, $0.0943 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T08:55 | 1 / 3 / 1 | ETH-USD 15% |  |
| Breezy | 2026-10-17T08:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T08:55 | 2 / 2 / 1 | COIN 68% |  |

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
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.49 | -3.33 | -13.80 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.42 | -4.32 | -11.67 | 289 |
| 17 | Hold BTC | benchmark | 96.87 | -3.13 | 0 | — | 29.28 | 3.43 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.23 | -6.32 | -22.13 | 145 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -9.03 | -1.61 | -13.33 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.17 | 2.34 | -6.73 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.19 | -6.81 | 96 | 21.9 | 3.10 | 0.58 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -4.13 | -0.37 | -22.92 | 129 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.79 | -2.37 | -10.02 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.94 | -5.97 | -11.33 | 245 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.41 | -0.05 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.41 | 0.38 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.72 | 0.92 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.74 | -0.60 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.52 | 0.39 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.08 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.62 | -1.05 | -27.05 | 206 |
| 42 | MACD cross · 1h | trend | 89.00 | -11.00 | 171 | 22.8 | -14.62 | -1.94 | -27.88 | 457 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.46 | -7.73 | -26.03 | 237 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.13 | -0.64 | -34.23 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.91 | -13.09 | 140 | 44.3 | -20.72 | -3.78 | -22.11 | 366 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.35 | -4.39 | -23.33 | 217 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 0.49 | 0.27 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.60 | -15.40 | 209 | 19.1 | -47.23 | -19.30 | -48.14 | 601 |
| 51 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 204 | 30.4 | -20.46 | -3.48 | -21.05 | 141 |
| 52 | Z-score reversion · 1h | reversion | 83.42 | -16.58 | 86 | 31.4 | -15.42 | -2.68 | -19.86 | 181 |
| 53 | Heikin-Ashi · 1h | trend | 83.38 | -16.62 | 192 | 24.0 | -31.37 | -5.16 | -40.65 | 674 |
| 54 | VWAP momentum · 1h | momentum | 83.32 | -16.68 | 390 | 21.0 | -35.93 | -5.46 | -43.97 | 1254 |
| 55 | Agent (ML meta-label) | meta | 83.13 | -16.87 | 611 | 19.1 | -6.92 | -0.97 | -15.76 | 392 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.81 | -1.69 | -26.96 | 403 |
| 57 | EMA 9/21 cross · 1h | trend | 82.17 | -17.83 | 127 | 11.8 | -5.76 | -0.44 | -29.38 | 314 |
| 58 | Bollinger reversion · 1h | reversion | 80.10 | -19.90 | 139 | 30.9 | -30.33 | -6.30 | -32.42 | 340 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.40 | -5.62 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.24 | -2.53 | -21.70 | 166 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.01 | -2.46 | -25.55 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.56 | -6.39 | -36.41 | 530 |
| 63 | Volume breakout | breakout | 63.62 | -36.38 | 326 | 13.2 | -63.18 | -18.19 | -63.18 | 878 |
| 64 | ROC + volume | momentum | 63.09 | -36.91 | 551 | 22.0 | -75.86 | -17.76 | -77.43 | 1719 |
| 65 | Squeeze breakout | breakout | 62.65 | -37.35 | 433 | 14.5 | -62.95 | -18.01 | -64.25 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.37 | -37.63 | 647 | 25.8 | -74.45 | -16.65 | -74.50 | 1628 |
| 67 | Donchian 55/20 | breakout | 61.07 | -38.93 | 438 | 17.8 | -69.29 | -14.70 | -71.81 | 1289 |
| 68 | EMA 20/50 cross | trend | 59.11 | -40.89 | 461 | 19.1 | -77.09 | -15.29 | -79.23 | 1451 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 682 | 23.6 | -73.18 | -15.56 | -73.22 | 1499 |
| 70 | AI bee: Boozy | ai | 54.43 | -45.56 | 310 | 6.5 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.09 | -45.91 | 613 | 16.0 | -83.46 | -27.26 | -83.46 | 1839 |
| 72 | Ichimoku | trend | 50.96 | -49.04 | 564 | 11.5 | -82.23 | -23.49 | -82.23 | 1740 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -30.20 | -98.61 | 5312 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.56 | -30.88 | -93.56 | 2606 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.46 | -20.54 | -87.18 | 1915 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.48 | -25.00 | -90.49 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.66 | -27.22 | -91.66 | 2335 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -33.04 | -97.43 | 3529 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -37.82 | -96.82 | 3632 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -26.05 | -94.19 | 2592 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -37.44 | -99.38 | 5817 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.39 | -26.23 | -91.39 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -32.29 | -96.34 | 3568 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.61 | -99.74 | 6240 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.90 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -39.85 | -97.53 | 3672 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.35 | -98.47 | 4760 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.77 | -34.06 | -93.77 | 2816 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.73 | -99.53 | 6251 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.57 | -22.37 | -86.57 | 2157 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.82 | -27.48 | -87.82 | 2153 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.90 | -33.56 | -95.90 | 3814 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -34.52 | -89.39 | 2118 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.59 | -95.80 | 4156 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.49 | -99.89 | 8310 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T08:55 | Three white soldiers | buy | SOL-USD | 21.17 | — | entry signal |
| 2026-10-17T08:45 | Squeeze breakout | sell | BTC-USD | 15.60 | -0.10 | exit signal |
| 2026-10-17T08:45 | Keltner breakout | sell | BTC-USD | 13.46 | -0.09 | exit signal |
| 2026-10-17T08:40 | Ichimoku | sell | DOGE-USD | 12.66 | -0.10 | exit signal |
| 2026-10-17T08:40 | EMA 20/50 cross | buy | BTC-USD | 9.00 | — | rebalance up |
| 2026-10-17T08:40 | EMA 20/50 cross | sell | XRP-USD | 14.70 | -0.13 | stop-loss |
| 2026-10-17T08:35 | Squeeze breakout | sell | ETH-USD | 15.62 | -0.09 | exit signal |
| 2026-10-17T08:10 | Volume breakout | sell | ETH-USD | 15.83 | -0.10 | exit signal |
| 2026-10-17T08:00 | Agent (ML meta-label) | buy | XRP-USD | 3.19 | — | entry |
| 2026-10-17T08:00 | Agent (ML meta-label) | sell | BTC-USD | 3.19 | -0.02 | selected signal exited |
| 2026-10-17T08:00 | Stochastic reversion · 1h | sell | BTC-USD | 7.94 | -0.00 | exit signal |
| 2026-10-17T08:00 | Bollinger reversion · 1h | buy | XRP-USD | 8.91 | — | entry |
| 2026-10-17T08:00 | Bollinger reversion · 1h | sell | DOGE-USD | 8.98 | -0.04 | exit signal |
| 2026-10-17T08:00 | Parabolic SAR · 1h | buy | ETH-USD | 23.31 | — | entry signal |
| 2026-10-17T08:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 20.56 | — | entry signal |
| 2026-10-17T07:48 | AI bee: Boozy | sell | ETH-USD | 17.38 | -0.12 | Jev: buy |
| 2026-10-17T07:35 | Volume breakout | buy | ETH-USD | 15.93 | — | entry signal |
| 2026-10-17T07:35 | Squeeze breakout | buy | BTC-USD | 15.70 | — | entry signal |
| 2026-10-17T07:35 | Keltner breakout | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-10-17T07:35 | Donchian 55/20 | buy | BTC-USD | 15.28 | — | entry signal |
| 2026-10-17T07:35 | Ichimoku | buy | DOGE-USD | 12.76 | — | entry signal |
| 2026-10-17T07:33 | AI bee: Boozy | buy | ETH-USD | 17.50 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T07:20 | Volume breakout | sell | ETH-USD | 15.87 | -0.08 | exit signal |
| 2026-10-17T07:20 | Ichimoku | sell | DOGE-USD | 12.72 | -0.11 | target is flat |
| 2026-10-17T07:00 | Stochastic reversion · 1h | sell | XRP-USD | 7.93 | 0.01 | exit signal |
| 2026-10-17T07:00 | Stochastic reversion · 1h | sell | ETH-USD | 7.95 | 0.02 | exit signal |
| 2026-10-17T07:00 | Heikin-Ashi · 1h | buy | XRP-USD | 20.86 | — | entry signal |
| 2026-10-17T07:00 | MACD cross · 1h | buy | BTC-USD | 11.05 | — | entry signal |
| 2026-10-17T07:00 | MACD cross · 1h | sell | SOL-USD | 11.05 | -0.07 | rebalance down |
| 2026-10-17T06:50 | Ichimoku | sell | SOL-USD | 12.74 | -0.09 | exit signal |
| 2026-10-17T06:40 | Squeeze breakout | buy | ETH-USD | 15.71 | — | entry signal |
| 2026-10-17T06:35 | Ichimoku | sell | XRP-USD | 12.77 | -0.09 | exit signal |
| 2026-10-17T06:32 | AI bee: Boozy | sell | ETH-USD | 17.50 | -0.11 | Jev: buy |
| 2026-10-17T06:15 | AI bee: Boozy | buy | ETH-USD | 17.60 | — | Jev: buy (buy p=0.68) |
| 2026-10-17T06:15 | Ichimoku | buy | SOL-USD | 12.83 | — | entry signal |
| 2026-10-17T06:15 | Ichimoku | buy | DOGE-USD | 12.83 | — | entry signal |
| 2026-10-17T06:10 | Volume breakout | buy | ETH-USD | 15.95 | — | entry signal |
| 2026-10-17T06:05 | Ichimoku | sell | ETH-USD | 12.78 | -0.08 | exit signal |
| 2026-10-17T06:01 | MFI reversion · 1h | buy | BTC-USD | 21.01 | — | entry signal |
| 2026-10-17T06:01 | Stochastic reversion · 1h | sell | SOL-USD | 7.98 | 0.04 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 08:55:05.000146+00:00 -> 2026-10-17 09:05:05.000146+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
