# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T11:55:05.000144+00:00 · 29474 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.63 (-9.38%)

Closed trades 86, win rate 39.5%, fees £2.89, max drawdown -9.99%.

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

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 8625 decisions in 1725 calls, $0.1208 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T11:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-20T11:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-20T11:55 | 1 / 4 / 0 | cash |  |

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
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.80 | 4.80 | 0 | — | 5.36 | 2.58 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.71 | -0.29 | 0 | — | 2.38 | 1.00 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 98.95 | -1.05 | 0 | — | -0.52 | -0.26 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.26 | -1.74 | 55 | 32.7 | 3.06 | 1.69 | -2.17 | 63 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.09 | -1.91 | 3 | 33.3 | 2.37 | 0.61 | -7.93 | 9 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -1.75 | -0.68 | -5.85 | 309 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.15 | -2.85 | 0 | — | -0.71 | -0.23 | -5.31 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.13 | -2.87 | 37 | 16.2 | -11.51 | -2.15 | -19.38 | 97 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.03 | -2.28 | -5.83 | 1 |
| 17 | Hold BTC | benchmark | 96.57 | -3.43 | 0 | — | 25.18 | 3.05 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 96.34 | -3.66 | 88 | 23.9 | -20.10 | -5.95 | -20.55 | 136 |
| 19 | Copy: Insider buying | copy | 96.26 | -3.75 | 23 | 43.5 | -11.54 | -1.97 | -20.62 | 70 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 96.19 | -3.81 | 0 | — | -5.86 | -2.32 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.08 | -3.11 | -6.31 | 33 |
| 22 | Max aggression: 5-day momentum | meta | 95.23 | -4.77 | 8 | 37.5 | -20.05 | -1.69 | -34.64 | 26 |
| 23 | Gap and go | momentum | 93.55 | -6.45 | 76 | 18.4 | 7.55 | 2.17 | -6.51 | 199 |
| 24 | ADX DI cross · 1h | trend | 93.45 | -6.55 | 88 | 18.2 | -14.55 | -2.65 | -16.51 | 259 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 92.79 | -7.21 | 6 | 16.7 | -5.98 | -0.76 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 91.85 | -8.15 | 7 | 0.0 | -3.02 | -0.19 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.85 | -8.15 | 78 | 23.1 | -12.57 | -2.25 | -16.37 | 102 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.85 | -2.44 | -16.91 | 1 |
| 30 | Opening range 30m | breakout | 90.95 | -9.05 | 207 | 29.5 | -13.06 | -3.76 | -17.26 | 557 |
| 31 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 84 | 28.6 | -9.05 | -1.53 | -16.89 | 253 |
| 32 | Parabolic SAR · 1h | trend | 90.67 | -9.33 | 105 | 21.9 | -20.47 | -4.57 | -22.26 | 270 |
| 33 | Agent | meta | 90.63 | -9.38 | 86 | 39.5 | -14.98 | -5.34 | -20.47 | 280 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 89.90 | -10.10 | 0 | — | 0.78 | 0.28 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 89.90 | -10.10 | 60 | 13.3 | -19.38 | -3.47 | -21.31 | 127 |
| 36 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.30 | -6.57 | -23.86 | 205 |
| 37 | RSI momentum · 1h | momentum | 89.22 | -10.78 | 82 | 15.9 | -22.77 | -4.30 | -28.12 | 211 |
| 38 | Ichimoku · 1h | trend | 88.56 | -11.44 | 56 | 14.3 | -17.68 | -3.34 | -18.16 | 114 |
| 39 | Stochastic reversion · 1h | reversion | 88.11 | -11.89 | 152 | 46.1 | -17.12 | -2.96 | -22.24 | 365 |
| 40 | Agent (aggressive) | meta | 88.03 | -11.97 | 43 | 34.9 | -14.91 | -3.38 | -22.27 | 136 |
| 41 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 56 | 23.2 | -16.89 | -2.80 | -26.96 | 199 |
| 42 | Supertrend · 1h | trend | 86.96 | -13.04 | 88 | 12.5 | -23.06 | -4.73 | -26.61 | 214 |
| 43 | Triple EMA stack · 1h | trend | 86.74 | -13.26 | 88 | 14.8 | -26.11 | -4.47 | -33.14 | 233 |
| 44 | Opening range 15m | breakout | 86.44 | -13.56 | 256 | 25.8 | -17.62 | -4.68 | -20.98 | 693 |
| 45 | MACD cross · 1h | trend | 85.83 | -14.17 | 189 | 20.6 | -28.48 | -5.57 | -32.90 | 470 |
| 46 | OBV trend · 1h | momentum | 85.09 | -14.91 | 181 | 17.7 | -29.28 | -4.94 | -36.50 | 316 |
| 47 | Z-score reversion · 1h | reversion | 85.03 | -14.97 | 91 | 30.8 | -14.19 | -2.33 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.24 | -15.76 | 209 | 31.1 | -17.40 | -2.72 | -21.34 | 138 |
| 49 | MACD zero-line · 1h | trend | 84.19 | -15.81 | 87 | 14.9 | -24.79 | -4.90 | -25.19 | 217 |
| 50 | Agent (ML meta-label) | meta | 83.67 | -16.33 | 681 | 18.8 | -8.94 | -1.57 | -14.79 | 350 |
| 51 | Donchian 20/10 · 1h | breakout | 83.58 | -16.42 | 81 | 17.3 | -11.50 | -1.38 | -27.92 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.72 | -17.28 | 158 | 34.8 | -27.91 | -5.34 | -33.53 | 352 |
| 53 | Max aggression: 1-day momentum | meta | 82.39 | -17.61 | 15 | 33.3 | -15.83 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 81.85 | -18.15 | 235 | 18.7 | -47.67 | -19.24 | -48.14 | 606 |
| 55 | Williams %R · 1h | reversion | 81.83 | -18.17 | 182 | 42.9 | -33.31 | -5.30 | -36.49 | 532 |
| 56 | ROC + volume · 1h | momentum | 81.38 | -18.62 | 197 | 20.8 | -25.43 | -4.28 | -33.98 | 384 |
| 57 | CCI reversion · 1h | reversion | 80.48 | -19.52 | 163 | 39.3 | -18.00 | -2.25 | -27.44 | 443 |
| 58 | RSI(14) reversion · 1h | reversion | 79.98 | -20.02 | 75 | 21.3 | -20.45 | -3.64 | -25.21 | 170 |
| 59 | EMA 9/21 cross · 1h | trend | 79.36 | -20.64 | 139 | 10.8 | -29.93 | -6.23 | -30.06 | 316 |
| 60 | Heikin-Ashi · 1h | trend | 78.66 | -21.34 | 227 | 21.1 | -42.12 | -9.06 | -45.31 | 681 |
| 61 | VWAP momentum · 1h | momentum | 77.77 | -22.23 | 433 | 20.8 | -43.60 | -7.68 | -48.64 | 1248 |
| 62 | Candlestick reversal · 1h | reversion | 76.96 | -23.04 | 214 | 27.6 | -36.51 | -6.55 | -37.48 | 530 |
| 63 | ROC + volume | momentum | 61.35 | -38.65 | 598 | 22.2 | -75.81 | -17.07 | -78.25 | 1723 |
| 64 | Volume breakout | breakout | 61.21 | -38.80 | 362 | 13.0 | -62.18 | -16.61 | -64.30 | 862 |
| 65 | Squeeze breakout | breakout | 59.45 | -40.55 | 476 | 13.9 | -63.96 | -19.35 | -66.16 | 1203 |
| 66 | Donchian 55/20 | breakout | 58.03 | -41.97 | 484 | 18.2 | -69.99 | -16.66 | -73.25 | 1266 |
| 67 | RSI(14) reversion | reversion | 56.76 | -43.23 | 722 | 24.9 | -74.97 | -16.71 | -75.01 | 1606 |
| 68 | EMA 20/50 cross | trend | 55.64 | -44.36 | 522 | 19.5 | -77.45 | -16.42 | -80.68 | 1421 |
| 69 | VWAP reversion | reversion | 53.62 | -46.38 | 751 | 25.2 | -71.65 | -14.60 | -72.48 | 1494 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -28.78 | -98.72 | 5266 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -32.05 | -93.78 | 2562 |
| 72 | Keltner breakout | breakout | 50.46 | -49.54 | 678 | 16.1 | -82.21 | -22.95 | -83.72 | 1795 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.82 | -20.81 | -88.33 | 1887 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.35 | -24.60 | -91.28 | 2345 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.04 | -25.75 | -91.17 | 2254 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.52 | -32.54 | -97.62 | 3489 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.69 | -36.20 | -96.79 | 3576 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.53 | -28.36 | -94.55 | 2502 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.98 | -24.47 | -82.95 | 1684 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.12 | -99.38 | 5739 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.03 | -23.59 | -92.14 | 2621 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.93 | -31.18 | -95.93 | 3448 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -38.97 | -99.75 | 6183 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -29.27 | -91.63 | 2329 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.59 | -37.08 | -97.68 | 3615 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -36.39 | -98.49 | 4694 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.61 | -29.95 | -94.05 | 2787 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.97 | -99.52 | 6157 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.00 | -22.54 | -87.02 | 2142 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.00 | -26.60 | -88.06 | 2130 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -32.52 | -95.96 | 3750 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.97 | -32.16 | -89.26 | 2097 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.38 | -95.78 | 4103 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -42.65 | -99.90 | 8266 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T11:40 | Keltner breakout | buy | XRP-USD | 12.63 | — | entry signal |
| 2026-10-20T11:40 | ROC + volume | buy | XRP-USD | 15.36 | — | entry signal |
| 2026-10-20T11:30 | Squeeze breakout | buy | XRP-USD | 14.87 | — | entry signal |
| 2026-10-20T11:25 | Squeeze breakout | sell | DOGE-USD | 14.83 | -0.10 | target is flat |
| 2026-10-20T11:20 | Squeeze breakout | sell | SOL-USD | 14.80 | -0.13 | exit signal |
| 2026-10-20T11:10 | Volume breakout | sell | DOGE-USD | 15.24 | -0.08 | target is flat |
| 2026-10-20T11:05 | RSI(14) reversion | sell | DOGE-USD | 14.17 | -0.05 | exit signal |
| 2026-10-20T11:05 | Volume breakout | buy | DOGE-USD | 15.32 | — | entry signal |
| 2026-10-20T11:05 | Squeeze breakout | buy | SOL-USD | 14.93 | — | entry signal |
| 2026-10-20T11:05 | Squeeze breakout | buy | DOGE-USD | 14.93 | — | entry signal |
| 2026-10-20T11:00 | Bollinger reversion · 1h | buy | XRP-USD | 20.69 | — | entry signal |
| 2026-10-20T11:00 | Bollinger reversion · 1h | buy | ETH-USD | 20.69 | — | entry signal |
| 2026-10-20T11:00 | Ichimoku · 1h | buy | DOGE-USD | 22.15 | — | entry signal |
| 2026-10-20T10:20 | RSI(14) reversion | sell | ETH-USD | 14.21 | -0.07 | target is flat |
| 2026-10-20T10:15 | RSI(14) reversion | sell | BTC-USD | 14.19 | -0.06 | exit signal |
| 2026-10-20T10:00 | Bollinger reversion · 1h | buy | BTC-USD | 20.70 | — | entry signal |
| 2026-10-20T09:05 | RSI(14) reversion | sell | XRP-USD | 14.20 | -0.13 | stop-loss |
| 2026-10-20T09:00 | OBV trend · 1h | sell | SOL-USD | 12.64 | -0.17 | exit signal |
| 2026-10-20T09:00 | RSI momentum · 1h | sell | SOL-USD | 22.27 | -0.23 | exit signal |
| 2026-10-20T09:00 | Parabolic SAR · 1h | buy | XRP-USD | 17.80 | — | rebalance up |
| 2026-10-20T09:00 | Parabolic SAR · 1h | buy | ETH-USD | 4.70 | — | rebalance up |
| 2026-10-20T09:00 | Parabolic SAR · 1h | sell | BTC-USD | 22.50 | -0.34 | exit signal |
| 2026-10-20T09:00 | Triple EMA stack · 1h | sell | SOL-USD | 21.60 | -0.33 | exit signal |
| 2026-10-20T09:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 19.66 | -0.27 | exit signal |
| 2026-10-20T09:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 19.76 | -0.26 | exit signal |
| 2026-10-20T09:00 | RSI(14) reversion | buy | DOGE-USD | 14.22 | — | entry signal |
| 2026-10-20T08:55 | RSI momentum · 1h | buy | SOL-USD | 4.47 | — | rebalance up |
| 2026-10-20T08:55 | RSI(14) reversion | sell | SOL-USD | 14.22 | -0.17 | stop-loss |
| 2026-10-20T08:25 | RSI(14) reversion | buy | BTC-USD | 14.25 | — | entry signal |
| 2026-10-20T08:20 | RSI(14) reversion | buy | ETH-USD | 14.28 | — | entry signal |
| 2026-10-20T08:05 | RSI(14) reversion | sell | ETH-USD | 14.21 | -0.16 | stop-loss |
| 2026-10-20T08:05 | RSI(14) reversion | sell | BTC-USD | 14.24 | -0.16 | stop-loss |
| 2026-10-20T08:00 | RSI momentum · 1h | sell | XRP-USD | 17.89 | -0.20 | exit signal |
| 2026-10-20T08:00 | Supertrend · 1h | sell | ETH-USD | 10.82 | -0.21 | exit signal |
| 2026-10-20T08:00 | Triple EMA stack · 1h | sell | XRP-USD | 21.11 | -0.31 | exit signal |
| 2026-10-20T08:00 | EMA 20/50 cross · 1h | sell | DOGE-USD | 22.23 | -0.34 | exit signal |
| 2026-10-20T08:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 3.92 | — | rebalance up |
| 2026-10-20T08:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 4.02 | — | rebalance up |
| 2026-10-20T08:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 7.95 | -0.12 | exit signal |
| 2026-10-20T07:55 | RSI(14) reversion | buy | XRP-USD | 14.33 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 11:55:05.000144+00:00 -> 2026-10-20 12:05:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
