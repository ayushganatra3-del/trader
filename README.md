# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T14:55:05.000126+00:00 · 47301 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.15 (-9.85%)

Closed trades 143, win rate 38.5%, fees £4.00, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 18.00 | -0.04 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 10506 decisions in 1869 calls, $0.1436 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T14:55 | 0 / 15 / 16 | cash |  |
| Breezy | 2026-11-04T14:55 | 0 / 28 / 3 | cash |  |
| Boozy | 2026-11-04T14:55 | 5 / 22 / 4 | MSTR 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.69 | 9.69 | 0 | — | 10.72 | 4.56 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.50 | 7.50 | 17 | 70.6 | 8.22 | 2.54 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 100.90 | 0.90 | 0 | — | 4.94 | 1.45 | -6.60 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.81 | -3.10 | -13.53 | 140 |
| 8 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.83 | -0.17 | 5 | 40.0 | 6.12 | 1.37 | -7.93 | 8 |
| 9 | Hold SPY | benchmark | 97.87 | -2.13 | 0 | — | -0.93 | -0.43 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 96.02 | -3.98 | 109 | 34.9 | 5.69 | 2.63 | -3.27 | 90 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.35 | -4.65 | 0 | — | -3.76 | -1.39 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.02 | -4.99 | 0 | — | -2.07 | -0.74 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Agent (rotation) | meta | 94.44 | -5.56 | 157 | 28.7 | -6.75 | -5.16 | -8.13 | 171 |
| 18 | Hold BTC | benchmark | 92.85 | -7.15 | 0 | — | -3.04 | -0.36 | -13.22 | 1 |
| 19 | Gap and go | momentum | 92.65 | -7.35 | 151 | 26.5 | -1.33 | -0.39 | -8.76 | 222 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Parabolic SAR · 1h | trend | 91.17 | -8.83 | 153 | 26.8 | -12.56 | -2.63 | -18.39 | 238 |
| 22 | Trend pullback · 1h | trend | 90.94 | -9.06 | 103 | 22.3 | -16.46 | -6.10 | -17.40 | 78 |
| 23 | Agent | meta | 90.15 | -9.85 | 143 | 38.5 | -10.73 | -6.50 | -12.20 | 206 |
| 24 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -15.06 | -4.98 | -17.21 | 573 |
| 25 | Copy: Insider buying | copy | 88.80 | -11.20 | 37 | 37.8 | -21.80 | -4.41 | -23.13 | 63 |
| 26 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.29 | -3.18 | -14.15 | 88 |
| 27 | Max aggression: 5-day momentum | meta | 87.63 | -12.37 | 16 | 43.8 | -26.74 | -1.69 | -36.71 | 25 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 86.93 | -13.07 | 1 | 0.0 | -6.41 | -0.91 | -16.59 | 1 |
| 29 | Daily: Bullish score | daily | 86.51 | -13.48 | 14 | 21.4 | -11.05 | -1.68 | -16.58 | 14 |
| 30 | Donchian 55/20 · 1h | breakout | 86.24 | -13.76 | 62 | 12.9 | -15.72 | -3.52 | -19.86 | 101 |
| 31 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 32 | Stochastic reversion · 1h | reversion | 85.50 | -14.50 | 243 | 46.9 | -22.40 | -4.39 | -26.10 | 388 |
| 33 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -14.75 | -3.38 | -17.85 | 91 |
| 34 | ADX DI cross · 1h | trend | 84.49 | -15.51 | 154 | 17.5 | -17.99 | -3.30 | -22.31 | 262 |
| 35 | MFI reversion · 1h | reversion | 84.44 | -15.56 | 314 | 33.8 | -13.49 | -2.03 | -18.26 | 151 |
| 36 | Keltner breakout · 1h | breakout | 83.48 | -16.52 | 91 | 23.1 | -23.24 | -4.81 | -24.96 | 168 |
| 37 | Connors RSI(2) · 1h | reversion | 82.65 | -17.35 | 192 | 40.6 | -19.67 | -6.53 | -20.15 | 130 |
| 38 | Opening range 15m | breakout | 81.77 | -18.23 | 427 | 30.7 | -20.82 | -6.41 | -21.19 | 717 |
| 39 | CCI reversion · 1h | reversion | 81.39 | -18.61 | 269 | 45.0 | -22.58 | -3.30 | -27.71 | 456 |
| 40 | Ichimoku · 1h | trend | 81.25 | -18.75 | 84 | 13.1 | -18.09 | -3.68 | -25.73 | 121 |
| 41 | Bollinger breakout · 1h | breakout | 81.00 | -19.00 | 145 | 24.1 | -17.96 | -3.65 | -23.94 | 232 |
| 42 | EMA 20/50 cross · 1h | trend | 79.44 | -20.56 | 92 | 10.9 | -19.98 | -3.77 | -27.62 | 129 |
| 43 | Z-score reversion · 1h | reversion | 79.12 | -20.88 | 144 | 34.7 | -11.97 | -1.64 | -23.02 | 221 |
| 44 | Bollinger reversion · 1h | reversion | 79.07 | -20.93 | 229 | 39.7 | -25.83 | -4.90 | -30.18 | 379 |
| 45 | Heikin-Ashi · 1h | trend | 78.28 | -21.72 | 372 | 22.6 | -40.20 | -8.46 | -43.53 | 666 |
| 46 | MACD cross · 1h | trend | 78.22 | -21.78 | 307 | 23.1 | -30.66 | -5.88 | -33.65 | 483 |
| 47 | Williams %R · 1h | reversion | 77.84 | -22.16 | 283 | 46.6 | -34.86 | -6.08 | -37.51 | 532 |
| 48 | Supertrend · 1h | trend | 77.77 | -22.23 | 145 | 12.4 | -27.69 | -5.24 | -30.27 | 226 |
| 49 | MACD zero-line · 1h | trend | 77.76 | -22.24 | 141 | 15.6 | -26.20 | -5.68 | -30.11 | 215 |
| 50 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -31.26 | -4.45 | -33.57 | 33 |
| 51 | RSI momentum · 1h | momentum | 76.34 | -23.66 | 141 | 12.1 | -29.43 | -5.78 | -31.33 | 217 |
| 52 | Triple EMA stack · 1h | trend | 76.34 | -23.66 | 130 | 13.8 | -26.27 | -4.72 | -32.22 | 198 |
| 53 | OBV trend · 1h | momentum | 75.94 | -24.06 | 245 | 17.1 | -29.50 | -6.36 | -30.87 | 287 |
| 54 | RSI(14) reversion · 1h | reversion | 74.44 | -25.56 | 133 | 27.8 | -18.57 | -2.98 | -26.28 | 215 |
| 55 | Donchian 20/10 · 1h | breakout | 74.12 | -25.88 | 123 | 19.5 | -26.83 | -4.87 | -31.68 | 205 |
| 56 | ROC + volume · 1h | momentum | 73.65 | -26.35 | 314 | 25.5 | -35.81 | -7.10 | -37.47 | 373 |
| 57 | Candlestick reversal · 1h | reversion | 72.02 | -27.98 | 368 | 29.3 | -32.80 | -5.86 | -37.89 | 556 |
| 58 | VWAP momentum · 1h | momentum | 69.48 | -30.52 | 720 | 22.1 | -55.25 | -11.52 | -56.40 | 1227 |
| 59 | Agent (ML meta-label) | meta | 69.20 | -30.80 | 1380 | 21.8 | -12.31 | -2.50 | -20.56 | 251 |
| 60 | EMA 9/21 cross · 1h | trend | 68.92 | -31.08 | 225 | 9.8 | -37.13 | -7.62 | -39.97 | 334 |
| 61 | Three white soldiers | momentum | 67.64 | -32.36 | 426 | 15.7 | -47.22 | -21.82 | -47.26 | 628 |
| 62 | Max aggression: 1-day momentum | meta | 66.74 | -33.26 | 24 | 29.2 | -35.72 | -2.12 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.55 | -98.99 | 5169 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.02 | -24.44 | -80.22 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -44.96 | -93.53 | 2517 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -30.08 | -89.11 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.17 | -36.92 | -91.32 | 2317 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.53 | -31.91 | -90.55 | 2193 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.71 | -50.16 | -97.75 | 3450 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -55.07 | -96.29 | 3365 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -33.00 | -93.68 | 2447 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -35.10 | -82.06 | 1638 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.61 | -99.49 | 5883 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.08 | -43.27 | -93.12 | 2623 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.38 | -36.64 | -95.38 | 3357 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -70.21 | -99.80 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -41.65 | -91.86 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.92 | -26.81 | -75.01 | 1558 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -58.53 | -97.78 | 3496 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.71 | -62.19 | -98.71 | 4827 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -70.44 | -30.84 | -70.89 | 1206 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.84 | -53.61 | -94.90 | 2779 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.87 | -37.04 | -84.99 | 1793 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.39 | -99.63 | 6316 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.24 | -30.23 | -88.43 | 2254 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.87 | -19.23 | -77.02 | 1712 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.51 | -36.83 | -90.53 | 2228 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.49 | -50.55 | -96.54 | 3835 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.11 | -49.62 | -89.35 | 2141 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.58 | -27.80 | -65.78 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.87 | -25.16 | -74.10 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.14 | -19.02 | -77.37 | 1615 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.96 | -51.99 | -96.97 | 4246 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -100.52 | -99.93 | 8192 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T14:55 | Day trade: Stocks in Play ORB | buy | AMZN | 24.01 | — | entry |
| 2026-11-04T14:55 | Agent (ML meta-label) | buy | MSTR | 17.33 | — | entry |
| 2026-11-04T14:55 | Agent (ML meta-label) | buy | ETHU | 14.53 | — | rebalance up |
| 2026-11-04T14:55 | Agent (ML meta-label) | sell | SOL-USD | 17.21 | -0.21 | selected signal exited |
| 2026-11-04T14:55 | Agent (ML meta-label) | sell | ETH-USD | 17.23 | -0.19 | selected signal exited |
| 2026-11-04T14:55 | MFI reversion · 1h | buy | LABU | 4.36 | — | rebalance up |
| 2026-11-04T14:55 | MFI reversion · 1h | buy | ETH-USD | 6.74 | — | rebalance up |
| 2026-11-04T14:55 | MFI reversion · 1h | buy | DOGE-USD | 6.90 | — | rebalance up |
| 2026-11-04T14:55 | MFI reversion · 1h | buy | AMZN | 4.26 | — | rebalance up |
| 2026-11-04T14:55 | MFI reversion · 1h | sell | PLTR | 20.60 | -0.38 | target is flat |
| 2026-11-04T14:55 | Candlestick reversal · 1h | buy | TECL | 3.62 | — | rebalance up |
| 2026-11-04T14:55 | VWAP momentum · 1h | buy | AMZN | 3.62 | — | rebalance up |
| 2026-11-04T14:55 | VWAP momentum · 1h | sell | META | 4.96 | 0.08 | target is flat |
| 2026-11-04T14:55 | Opening range 15m | buy | GOOGL | 1.89 | — | entry signal |
| 2026-11-04T14:55 | Opening range 15m | buy | AAPL | 8.18 | — | entry signal |
| 2026-11-04T14:55 | Opening range 15m | sell | AMD | 10.06 | -0.25 | stop-loss |
| 2026-11-04T14:51 | Day trade: Stocks in Play ORB | sell | TNA | 23.86 | -0.20 | target is flat |
| 2026-11-04T14:51 | Agent (ML meta-label) | buy | SOL-USD | 17.42 | — | entry |
| 2026-11-04T14:51 | Agent (ML meta-label) | buy | ETH-USD | 17.42 | — | entry |
| 2026-11-04T14:51 | Agent (ML meta-label) | sell | SQQQ | 17.28 | -0.04 | selected signal exited |
| 2026-11-04T14:51 | Agent (ML meta-label) | sell | MSTR | 17.31 | -0.00 | selected signal exited |
| 2026-11-04T14:51 | Agent (ML meta-label) | sell | ETHU | 15.93 | 1.14 | rebalance down |
| 2026-11-04T14:51 | Three white soldiers | buy | SOL-USD | 17.01 | — | entry signal |
| 2026-11-04T14:51 | Three white soldiers | buy | ETHU | 17.01 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | TQQQ | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | QQQ | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | PLTR | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | MSTR | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | ETHU | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | COIN | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | BITX | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Opening range 15m | buy | AMD | 10.31 | — | entry signal |
| 2026-11-04T14:51 | Gap and go | buy | GOOGL | 11.38 | — | entry |
| 2026-11-04T14:51 | Gap and go | buy | ETHU | 11.62 | — | entry |
| 2026-11-04T14:51 | Gap and go | sell | TNA | 11.48 | -0.10 | exit signal |
| 2026-11-04T14:51 | Gap and go | sell | IWM | 11.53 | -0.04 | exit signal |
| 2026-11-04T14:45 | Day trade: Stocks in Play ORB | buy | GOOGL | 24.05 | — | entry |
| 2026-11-04T14:45 | Agent (ML meta-label) | buy | SQQQ | 17.32 | — | entry |
| 2026-11-04T14:45 | Agent (ML meta-label) | buy | MSTR | 17.32 | — | entry |
| 2026-11-04T14:45 | Agent (ML meta-label) | sell | SOL-USD | 17.28 | 0.11 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 14:55:05.000126+00:00 -> 2026-11-04 15:05:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 14:55:05.000126+00:00 -> 2026-11-04 15:05:05.000126+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 14:55:05.000126+00:00 -> 2026-11-04 15:05:05.000126+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
