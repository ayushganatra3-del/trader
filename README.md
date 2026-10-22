# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T15:16:05.000138+00:00 · 31979 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.40 (-9.60%)

Closed trades 94, win rate 40.4%, fees £3.06, max drawdown -10.18%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 17.88 | -0.25 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 17364 decisions in 2241 calls, $0.2263 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T15:16 | 2 / 20 / 8 | cash |  |
| Breezy | 2026-10-22T15:16 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-22T15:16 | 4 / 24 / 2 | COIN 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.23 | 7.23 | 0 | — | 9.44 | 4.30 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.25 | 5.25 | 12 | 66.7 | 2.18 | 0.72 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.27 | 4.27 | 15 | 46.7 | 6.70 | 2.11 | -4.90 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 101.81 | 1.81 | 75 | 48.0 | -8.97 | -2.44 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.09 | 0.09 | 0 | — | 3.20 | 1.43 | -5.02 | 1 |
| 7 | Max aggression: 5-day momentum | meta | 100.01 | 0.01 | 10 | 50.0 | -15.73 | -1.22 | -34.64 | 26 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.19 | -0.81 | 68 | 35.3 | 2.92 | 1.71 | -2.29 | 68 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 12 | Hold SPY | benchmark | 98.21 | -1.79 | 0 | — | -0.48 | -0.22 | -3.13 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.20 | -2.80 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.33 | -1.91 | -5.83 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 96.65 | -3.35 | 0 | — | -0.21 | -0.02 | -5.31 | 1 |
| 16 | Hold BTC | benchmark | 96.30 | -3.70 | 0 | — | 5.21 | 0.95 | -8.68 | 1 |
| 17 | Agent (rotation) | meta | 96.12 | -3.88 | 117 | 30.8 | -4.90 | -2.14 | -7.58 | 273 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.42 | 0.78 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.77 | -5.23 | 89 | 21.3 | 6.72 | 2.09 | -7.38 | 198 |
| 21 | Trend pullback · 1h | trend | 94.27 | -5.73 | 93 | 23.7 | -21.74 | -6.71 | -21.88 | 126 |
| 22 | Copy: Insider buying | copy | 94.01 | -5.99 | 25 | 40.0 | -13.88 | -2.37 | -20.62 | 72 |
| 23 | Opening range 30m | breakout | 93.60 | -6.40 | 237 | 35.0 | -10.39 | -2.93 | -17.26 | 558 |
| 24 | ADX DI cross · 1h | trend | 93.18 | -6.82 | 101 | 18.8 | -13.25 | -2.53 | -14.82 | 255 |
| 25 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.02 | -3.61 | -19.05 | 103 |
| 26 | Daily: Momentum burst | daily | 92.82 | -7.17 | 8 | 12.5 | -16.80 | -2.99 | -20.58 | 39 |
| 27 | Parabolic SAR · 1h | trend | 92.14 | -7.86 | 115 | 26.1 | -16.33 | -3.51 | -19.19 | 266 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.88 | -0.87 | -11.76 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.80 | -2.05 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.88 | -9.12 | 8 | 0.0 | -6.26 | -0.70 | -13.10 | 13 |
| 31 | Agent | meta | 90.40 | -9.60 | 94 | 40.4 | -19.91 | -6.00 | -21.33 | 266 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.19 | -9.81 | 0 | — | -3.65 | -0.42 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 89.51 | -10.49 | 103 | 28.2 | -11.67 | -2.08 | -15.89 | 259 |
| 34 | Volume breakout · 1h | breakout | 88.97 | -11.03 | 101 | 22.8 | -11.84 | -2.09 | -13.70 | 106 |
| 35 | Stochastic reversion · 1h | reversion | 88.69 | -11.31 | 176 | 46.0 | -15.05 | -2.48 | -22.24 | 371 |
| 36 | EMA 20/50 cross · 1h | trend | 87.89 | -12.11 | 67 | 11.9 | -23.65 | -4.40 | -25.78 | 142 |
| 37 | Supertrend · 1h | trend | 87.50 | -12.51 | 102 | 15.7 | -23.94 | -4.68 | -26.78 | 219 |
| 38 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.68 | -4.60 | -18.68 | 138 |
| 39 | RSI momentum · 1h | momentum | 87.30 | -12.70 | 94 | 17.0 | -20.41 | -4.02 | -21.81 | 219 |
| 40 | Opening range 15m | breakout | 87.01 | -12.99 | 297 | 30.6 | -16.22 | -4.37 | -18.82 | 701 |
| 41 | Keltner breakout · 1h | breakout | 86.06 | -13.94 | 73 | 23.3 | -23.00 | -4.42 | -23.74 | 199 |
| 42 | Connors RSI(2) · 1h | reversion | 85.87 | -14.13 | 168 | 39.9 | -25.59 | -7.17 | -25.71 | 203 |
| 43 | MACD cross · 1h | trend | 84.94 | -15.05 | 209 | 22.0 | -26.42 | -4.89 | -27.69 | 468 |
| 44 | Ichimoku · 1h | trend | 84.72 | -15.28 | 64 | 12.5 | -19.95 | -3.71 | -22.29 | 117 |
| 45 | Z-score reversion · 1h | reversion | 84.39 | -15.61 | 104 | 33.7 | -9.61 | -1.31 | -21.32 | 195 |
| 46 | Triple EMA stack · 1h | trend | 84.35 | -15.65 | 96 | 15.6 | -30.86 | -5.43 | -31.19 | 217 |
| 47 | MFI reversion · 1h | reversion | 83.73 | -16.27 | 231 | 32.9 | -17.54 | -2.72 | -21.11 | 144 |
| 48 | Donchian 20/10 · 1h | breakout | 83.68 | -16.32 | 92 | 20.7 | -24.61 | -4.55 | -25.17 | 228 |
| 49 | Williams %R · 1h | reversion | 82.91 | -17.09 | 201 | 44.8 | -32.98 | -5.20 | -38.16 | 516 |
| 50 | OBV trend · 1h | momentum | 82.43 | -17.57 | 196 | 17.9 | -32.27 | -6.18 | -32.67 | 309 |
| 51 | MACD zero-line · 1h | trend | 82.40 | -17.60 | 99 | 15.2 | -24.98 | -4.79 | -25.87 | 227 |
| 52 | Three white soldiers | momentum | 82.23 | -17.77 | 262 | 20.2 | -44.73 | -17.91 | -45.28 | 600 |
| 53 | Agent (ML meta-label) | meta | 81.56 | -18.44 | 762 | 19.4 | -9.87 | -1.87 | -15.00 | 348 |
| 54 | CCI reversion · 1h | reversion | 81.18 | -18.82 | 190 | 43.2 | -21.39 | -2.80 | -27.44 | 443 |
| 55 | Bollinger reversion · 1h | reversion | 81.15 | -18.85 | 165 | 35.8 | -30.43 | -5.90 | -32.80 | 352 |
| 56 | ROC + volume · 1h | momentum | 80.05 | -19.95 | 230 | 24.3 | -28.05 | -5.01 | -28.18 | 382 |
| 57 | Heikin-Ashi · 1h | trend | 79.66 | -20.34 | 260 | 23.5 | -45.76 | -9.46 | -45.79 | 675 |
| 58 | Candlestick reversal · 1h | reversion | 78.70 | -21.30 | 235 | 30.2 | -36.05 | -6.16 | -38.96 | 550 |
| 59 | RSI(14) reversion · 1h | reversion | 78.68 | -21.32 | 87 | 24.1 | -19.45 | -3.69 | -23.28 | 173 |
| 60 | EMA 9/21 cross · 1h | trend | 78.39 | -21.61 | 154 | 11.7 | -30.89 | -5.80 | -32.03 | 338 |
| 61 | VWAP momentum · 1h | momentum | 76.38 | -23.62 | 497 | 21.5 | -50.66 | -10.34 | -50.89 | 1248 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.05 | -2.79 | -47.70 | 43 |
| 63 | ROC + volume | momentum | 59.95 | -40.05 | 681 | 23.3 | -77.62 | -21.24 | -79.13 | 1700 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.62 | -19.55 | -65.41 | 878 |
| 65 | Donchian 55/20 | breakout | 56.19 | -43.81 | 538 | 19.7 | -71.89 | -18.62 | -74.22 | 1276 |
| 66 | Squeeze breakout | breakout | 55.60 | -44.40 | 527 | 14.0 | -67.37 | -22.86 | -68.37 | 1201 |
| 67 | EMA 20/50 cross | trend | 54.44 | -45.56 | 581 | 20.3 | -78.75 | -19.33 | -80.90 | 1446 |
| 68 | RSI(14) reversion | reversion | 53.32 | -46.68 | 794 | 26.4 | -76.35 | -17.27 | -76.35 | 1656 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.70 | -14.32 | -73.06 | 1504 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -31.42 | -98.87 | 5294 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.80 | -31.78 | -94.29 | 2566 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.26 | -88.98 | 1897 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -27.47 | -91.88 | 2350 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.11 | -25.28 | -91.11 | 2234 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -34.90 | -97.90 | 3504 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -35.78 | -97.04 | 3569 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -28.04 | -94.47 | 2559 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.71 | -26.27 | -83.46 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -37.27 | -99.47 | 5834 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.37 | -30.11 | -92.92 | 2616 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.81 | -30.93 | -95.82 | 3454 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.35 | -99.78 | 6165 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.80 | -29.43 | -92.12 | 2333 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -37.70 | -97.76 | 3591 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.63 | -38.30 | -98.63 | 4747 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.27 | -34.42 | -94.63 | 2785 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.34 | -27.18 | -84.51 | 1784 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -40.32 | -99.59 | 6220 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.75 | -23.44 | -87.81 | 2187 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.53 | -26.85 | -88.61 | 2179 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.21 | -33.92 | -96.23 | 3801 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -34.29 | -89.79 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -34.48 | -96.23 | 4136 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.58 | -99.91 | 8247 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T15:15 | VWAP reversion · 1h | buy | ETH-USD | 5.08 | — | rebalance up |
| 2026-10-22T15:15 | VWAP reversion · 1h | sell | BTC-USD | 5.08 | -0.05 | rebalance down |
| 2026-10-22T15:15 | VWAP reversion | sell | XRP-USD | 4.62 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | TQQQ | 1.47 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | TECL | 3.92 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | SPY | 3.59 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | SOL-USD | 4.63 | 0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | PLTR | 4.66 | -0.00 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | GOOGL | 4.66 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | ETH-USD | 4.62 | -0.04 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | DOGE-USD | 4.61 | -0.03 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | BTC-USD | 4.63 | -0.05 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | AMZN | 5.68 | -0.01 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | VWAP reversion | sell | AMD | 3.92 | -0.02 | Daily loss limit (6%) hit; paused until tomorrow (UTC) |
| 2026-10-22T15:15 | RSI(14) reversion | buy | MSFT | 6.26 | — | rebalance up |
| 2026-10-22T15:15 | RSI(14) reversion | sell | ETHU | 10.59 | -0.23 | stop-loss |
| 2026-10-22T15:15 | Opening range 30m | sell | MSTR | 23.04 | -0.44 | stop-loss |
| 2026-10-22T15:15 | EMA 20/50 cross | sell | TSLA | 13.52 | -0.19 | stop-loss |
| 2026-10-22T15:15 | EMA 20/50 cross | sell | ETH-USD | 13.50 | -0.19 | stop-loss |
| 2026-10-22T15:10 | Agent (ML meta-label) | sell | LABU | 10.84 | -0.04 | selected signal exited |
| 2026-10-22T15:10 | VWAP reversion | buy | TQQQ | 1.47 | — | entry |
| 2026-10-22T15:10 | VWAP reversion | buy | AMD | 3.94 | — | entry signal |
| 2026-10-22T15:10 | VWAP reversion | sell | AAPL | 4.68 | 0.02 | exit signal |
| 2026-10-22T15:10 | RSI(14) reversion | buy | META | 8.89 | — | entry signal |
| 2026-10-22T15:10 | RSI(14) reversion | sell | COIN | 8.89 | -0.17 | stop-loss |
| 2026-10-22T15:10 | Opening range 15m | sell | COIN | 21.64 | -0.35 | stop-loss |
| 2026-10-22T15:00 | Agent (ML meta-label) | buy | LABU | 10.88 | — | following Connors RSI(2) |
| 2026-10-22T15:00 | Williams %R · 1h | buy | ETH-USD | 20.85 | — | entry signal |
| 2026-10-22T15:00 | Connors RSI(2) · 1h | sell | BTC-USD | 21.52 | -0.17 | exit signal |
| 2026-10-22T15:00 | Candlestick reversal · 1h | sell | XRP-USD | 19.64 | -0.17 | exit signal |
| 2026-10-22T15:00 | EMA 20/50 cross | buy | AAPL | 13.68 | — | entry signal |
| 2026-10-22T14:55 | VWAP reversion | buy | TECL | 3.95 | — | entry signal |
| 2026-10-22T14:55 | VWAP reversion | sell | MSFT | 4.67 | 0.01 | exit signal |
| 2026-10-22T14:55 | Three white soldiers | buy | MSFT | 20.54 | — | entry signal |
| 2026-10-22T14:50 | MFI reversion · 1h | sell | TECL | 13.55 | -0.66 | stop-loss |
| 2026-10-22T14:50 | Z-score reversion · 1h | sell | TECL | 19.78 | -1.35 | stop-loss |
| 2026-10-22T14:50 | RSI(14) reversion | buy | MSFT | 4.39 | — | entry signal |
| 2026-10-22T14:50 | RSI(14) reversion | sell | COIN | 4.39 | -0.04 | rebalance down |
| 2026-10-22T14:50 | EMA 20/50 cross | buy | ETH-USD | 13.69 | — | entry signal |
| 2026-10-22T14:47 | Agent (ML meta-label) | buy | TNA | 4.68 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 15:16:05.000138+00:00 -> 2026-10-22 15:26:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
