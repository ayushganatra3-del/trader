# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T14:55:05.000157+00:00 · 48561 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.06 (-10.94%)

Closed trades 147, win rate 37.4%, fees £4.06, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 13140 decisions in 2385 calls, $0.1804 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T14:55 | 0 / 1 / 29 | cash |  |
| Breezy | 2026-11-05T14:55 | 0 / 17 / 13 | cash |  |
| Boozy | 2026-11-05T14:55 | 4 / 20 / 6 | COIN 56% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.60 | 13.60 | 0 | — | 14.93 | 5.15 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.76 | 6.76 | 18 | 66.7 | 8.40 | 2.54 | -4.91 | 26 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.41 | 1.41 | 0 | — | 5.28 | 1.57 | -6.60 | 1 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.34 | 1.33 | 28 | 25.0 | 9.54 | 2.19 | -8.66 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.34 | -0.66 | 106 | 46.2 | -13.46 | -3.41 | -13.56 | 139 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.53 | -3.48 | 0 | — | -2.04 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.19 | -3.81 | 116 | 34.5 | 3.31 | 1.83 | -3.32 | 90 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 95.39 | -4.61 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 14 | Gap and go | momentum | 94.25 | -5.75 | 160 | 28.8 | -0.58 | -0.12 | -9.18 | 220 |
| 15 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 16 | Agent (rotation) | meta | 93.76 | -6.24 | 174 | 27.6 | -6.84 | -4.74 | -9.46 | 169 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.48 | -6.52 | 0 | — | -3.98 | -1.47 | -7.64 | 1 |
| 18 | Trend pullback · 1h | trend | 92.44 | -7.56 | 105 | 22.9 | -14.91 | -5.25 | -17.67 | 79 |
| 19 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -4.16 | -0.55 | -10.25 | 8 |
| 20 | Hold BTC | benchmark | 92.30 | -7.70 | 0 | — | -1.45 | -0.07 | -13.22 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Copy: Insider buying | copy | 89.51 | -10.49 | 38 | 39.5 | -21.89 | -4.43 | -23.32 | 65 |
| 23 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -13.43 | -7.49 | -13.83 | 205 |
| 24 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -16.03 | -5.28 | -17.21 | 583 |
| 25 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.47 | -3.29 | -14.15 | 86 |
| 26 | Parabolic SAR · 1h | trend | 87.41 | -12.59 | 164 | 26.8 | -17.33 | -3.71 | -20.25 | 244 |
| 27 | Daily: Bullish score | daily | 87.31 | -12.69 | 14 | 21.4 | -8.04 | -1.20 | -16.58 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 86.26 | -13.74 | 66 | 15.2 | -13.42 | -2.86 | -19.86 | 105 |
| 29 | Max aggression: 5-day momentum | meta | 85.86 | -14.14 | 16 | 43.8 | -27.61 | -1.70 | -36.71 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -16.79 | -4.84 | -18.47 | 98 |
| 31 | Stochastic reversion · 1h | reversion | 84.17 | -15.83 | 250 | 47.6 | -22.71 | -4.28 | -24.83 | 380 |
| 32 | Opening range 15m | breakout | 82.35 | -17.65 | 445 | 30.6 | -20.39 | -6.25 | -21.20 | 712 |
| 33 | Volume breakout · 1h | breakout | 82.20 | -17.80 | 142 | 28.2 | -16.71 | -3.76 | -20.42 | 100 |
| 34 | ADX DI cross · 1h | trend | 82.00 | -18.00 | 164 | 18.3 | -21.32 | -3.86 | -23.81 | 271 |
| 35 | Keltner breakout · 1h | breakout | 81.68 | -18.32 | 103 | 24.3 | -24.72 | -5.16 | -26.37 | 187 |
| 36 | Connors RSI(2) · 1h | reversion | 81.67 | -18.33 | 200 | 40.5 | -20.59 | -6.75 | -20.59 | 130 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 81.50 | -18.50 | 1 | 0.0 | -12.12 | -1.81 | -19.75 | 1 |
| 38 | MFI reversion · 1h | reversion | 80.90 | -19.10 | 326 | 34.0 | -17.75 | -2.71 | -18.73 | 149 |
| 39 | Ichimoku · 1h | trend | 79.68 | -20.32 | 88 | 13.6 | -23.04 | -4.82 | -27.33 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 78.87 | -21.13 | 162 | 24.1 | -22.09 | -4.49 | -25.86 | 252 |
| 41 | EMA 20/50 cross · 1h | trend | 77.70 | -22.30 | 96 | 10.4 | -20.07 | -3.64 | -26.30 | 135 |
| 42 | CCI reversion · 1h | reversion | 77.42 | -22.58 | 282 | 45.7 | -25.11 | -3.60 | -28.54 | 446 |
| 43 | Heikin-Ashi · 1h | trend | 76.24 | -23.76 | 384 | 22.9 | -43.00 | -8.87 | -44.12 | 678 |
| 44 | MACD zero-line · 1h | trend | 76.11 | -23.89 | 151 | 16.6 | -28.27 | -5.84 | -28.51 | 217 |
| 45 | Daily: Momentum burst | daily | 75.71 | -24.30 | 23 | 13.0 | -30.86 | -4.34 | -33.76 | 32 |
| 46 | Supertrend · 1h | trend | 75.57 | -24.43 | 148 | 12.8 | -30.10 | -5.64 | -31.73 | 231 |
| 47 | Triple EMA stack · 1h | trend | 75.09 | -24.91 | 134 | 13.4 | -27.99 | -4.78 | -32.91 | 207 |
| 48 | MACD cross · 1h | trend | 74.84 | -25.16 | 321 | 23.7 | -35.47 | -6.69 | -36.12 | 478 |
| 49 | RSI momentum · 1h | momentum | 74.31 | -25.68 | 152 | 11.2 | -30.25 | -5.80 | -31.23 | 225 |
| 50 | Williams %R · 1h | reversion | 74.12 | -25.88 | 296 | 46.6 | -34.86 | -6.23 | -35.57 | 523 |
| 51 | Z-score reversion · 1h | reversion | 73.61 | -26.39 | 158 | 36.1 | -20.65 | -2.97 | -24.30 | 218 |
| 52 | Bollinger reversion · 1h | reversion | 72.97 | -27.03 | 237 | 40.1 | -31.97 | -6.07 | -32.40 | 368 |
| 53 | OBV trend · 1h | momentum | 72.70 | -27.30 | 258 | 17.8 | -34.38 | -7.44 | -34.44 | 302 |
| 54 | Donchian 20/10 · 1h | breakout | 72.63 | -27.37 | 135 | 20.0 | -29.90 | -5.46 | -33.23 | 218 |
| 55 | ROC + volume · 1h | momentum | 71.95 | -28.05 | 336 | 25.9 | -35.60 | -6.83 | -37.00 | 386 |
| 56 | EMA 9/21 cross · 1h | trend | 68.29 | -31.71 | 230 | 9.6 | -38.86 | -7.99 | -39.28 | 338 |
| 57 | Agent (ML meta-label) | meta | 68.04 | -31.96 | 1464 | 22.1 | -5.22 | -0.80 | -17.53 | 316 |
| 58 | Candlestick reversal · 1h | reversion | 67.60 | -32.40 | 378 | 29.9 | -36.90 | -7.02 | -37.84 | 544 |
| 59 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.21 | -21.89 | -47.21 | 635 |
| 60 | VWAP momentum · 1h | momentum | 67.21 | -32.79 | 755 | 22.3 | -55.35 | -11.56 | -56.73 | 1231 |
| 61 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -27.27 | -4.35 | -29.66 | 204 |
| 62 | Max aggression: 1-day momentum | meta | 65.16 | -34.84 | 25 | 28.0 | -37.37 | -2.27 | -50.32 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -45.92 | -98.93 | 5205 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.87 | -25.30 | -80.10 | 1415 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -47.84 | -93.40 | 2522 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.71 | -30.91 | -88.72 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -39.19 | -90.61 | 2302 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -32.95 | -90.97 | 2255 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -54.08 | -97.64 | 3438 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -60.47 | -96.22 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.83 | -33.46 | -93.88 | 2472 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.90 | -36.89 | -81.90 | 1647 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -54.36 | -99.48 | 5853 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.66 | -43.91 | -92.72 | 2592 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.91 | -38.20 | -95.91 | 3444 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -72.64 | -99.80 | 6161 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.55 | -43.26 | -91.55 | 2246 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.52 | -26.20 | -74.73 | 1550 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -63.03 | -97.75 | 3528 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.02 | -98.70 | 4819 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.18 | -28.15 | -69.89 | 1193 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -55.70 | -94.58 | 2745 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.61 | -36.57 | -84.61 | 1790 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.24 | -99.62 | 6295 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.42 | -30.56 | -88.45 | 2247 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.66 | -19.05 | -76.67 | 1692 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.75 | -37.03 | -90.76 | 2216 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.85 | -96.43 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.17 | -51.52 | -89.19 | 2143 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.61 | -28.01 | -65.68 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.26 | -24.69 | -73.65 | 1265 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.38 | -18.12 | -76.65 | 1596 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.08 | -52.14 | -97.08 | 4267 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.92 | -99.93 | 8212 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T14:55 | Agent (ML meta-label) | buy | MSFT | 7.26 | — | rebalance up |
| 2026-11-05T14:55 | Agent (ML meta-label) | buy | AAPL | 7.26 | — | rebalance up |
| 2026-11-05T14:55 | Agent (ML meta-label) | sell | XRP-USD | 9.73 | -0.20 | selected signal exited |
| 2026-11-05T14:55 | Agent (ML meta-label) | sell | MSTR | 9.66 | -0.13 | selected signal exited |
| 2026-11-05T14:55 | Agent (ML meta-label) | sell | GOOGL | 8.92 | -0.04 | selected signal exited |
| 2026-11-05T14:55 | Agent (ML meta-label) | sell | ETHU | 9.69 | -0.10 | selected signal exited |
| 2026-11-05T14:55 | Agent (ML meta-label) | sell | BITX | 9.70 | -0.09 | selected signal exited |
| 2026-11-05T14:55 | VWAP reversion · 1h | sell | DOGE-USD | 24.38 | -0.61 | stop-loss |
| 2026-11-05T14:55 | Connors RSI(2) · 1h | sell | XRP-USD | 20.27 | -0.50 | stop-loss |
| 2026-11-05T14:55 | Connors RSI(2) · 1h | sell | ETH-USD | 20.27 | -0.50 | stop-loss |
| 2026-11-05T14:55 | Connors RSI(2) · 1h | sell | BTC-USD | 20.36 | -0.42 | stop-loss |
| 2026-11-05T14:55 | Volume breakout · 1h | buy | MSFT | 4.12 | — | rebalance up |
| 2026-11-05T14:55 | Volume breakout · 1h | sell | GOOGL | 20.54 | -0.38 | target is flat |
| 2026-11-05T14:55 | Trend pullback · 1h | sell | XRP-USD | 22.14 | -0.55 | stop-loss |
| 2026-11-05T14:55 | EMA 9/21 cross · 1h | sell | SPY | 3.37 | -0.04 | stop-loss |
| 2026-11-05T14:51 | Agent (ML meta-label) | buy | MSTR | 9.79 | — | entry |
| 2026-11-05T14:51 | Agent (ML meta-label) | buy | ETHU | 9.79 | — | entry |
| 2026-11-05T14:51 | Agent (ML meta-label) | buy | BITX | 9.79 | — | entry |
| 2026-11-05T14:51 | Agent (ML meta-label) | sell | XRP-USD | 7.25 | -0.12 | rebalance down |
| 2026-11-05T14:51 | Agent (ML meta-label) | sell | MSFT | 7.30 | -0.09 | rebalance down |
| 2026-11-05T14:51 | Agent (ML meta-label) | sell | AAPL | 7.42 | 0.01 | rebalance down |
| 2026-11-05T14:51 | Volume breakout · 1h | buy | GOOGL | 4.13 | — | rebalance up |
| 2026-11-05T14:51 | Volume breakout · 1h | sell | AAPL | 16.64 | -0.03 | target is flat |
| 2026-11-05T14:51 | Keltner breakout · 1h | sell | MSFT | 20.42 | -0.25 | stop-loss |
| 2026-11-05T14:51 | Bollinger breakout · 1h | buy | GOOGL | 8.45 | — | rebalance up |
| 2026-11-05T14:51 | Bollinger breakout · 1h | buy | AMZN | 8.50 | — | rebalance up |
| 2026-11-05T14:51 | Bollinger breakout · 1h | buy | AAPL | 8.34 | — | rebalance up |
| 2026-11-05T14:51 | Bollinger breakout · 1h | sell | TNA | 11.18 | -0.34 | stop-loss |
| 2026-11-05T14:51 | Bollinger breakout · 1h | sell | MSFT | 11.32 | -0.13 | stop-loss |
| 2026-11-05T14:51 | Bollinger breakout · 1h | sell | IWM | 11.36 | -0.12 | stop-loss |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | XRP-USD | 5.31 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | MSFT | 5.21 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | ETH-USD | 5.33 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | BTC-USD | 5.28 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | AMZN | 5.23 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | buy | AAPL | 5.17 | — | rebalance up |
| 2026-11-05T14:51 | RSI momentum · 1h | sell | TNA | 5.66 | -0.16 | stop-loss |
| 2026-11-05T14:51 | RSI momentum · 1h | sell | IWM | 4.98 | -0.07 | stop-loss |
| 2026-11-05T14:51 | ROC + volume · 1h | buy | AMZN | 3.64 | — | rebalance up |
| 2026-11-05T14:51 | ROC + volume · 1h | sell | TNA | 14.32 | -0.13 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 14:55:05.000157+00:00 -> 2026-11-05 15:05:05.000157+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 14:55:05.000157+00:00 -> 2026-11-05 15:05:05.000157+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 14:55:05.000157+00:00 -> 2026-11-05 15:05:05.000157+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
