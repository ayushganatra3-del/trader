# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T18:50:05.000110+00:00 · 56082 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.77 (-14.23%)

Closed trades 178, win rate 35.4%, fees £5.35, max drawdown -14.66%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.57 | +0.23 |
| SQQQ | 34.26 | -0.22 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-11 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-10)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.57 · VIX 19.46 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.4, AMZN 6.1, AAPL 5.3, IWM 4.7, MSFT 3.9, TSLA 2.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 30096 decisions in 2832 calls, $0.3762 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T18:50 | 2 / 15 / 12 | cash |  |
| Breezy | 2026-11-11T18:50 | 0 / 27 / 2 | cash |  |
| Boozy | 2026-11-11T18:50 | 4 / 23 / 2 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| MFI reversion | LABU | 1.66 | +5.37% | 3 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.89 | 17.89 | 20 | 70.0 | 19.40 | 3.88 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.17 | 15.17 | 0 | — | 14.83 | 4.90 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.11 | 5.11 | 31 | 45.2 | 5.21 | 1.30 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.75 | 3.75 | 0 | — | 6.21 | 1.71 | -6.60 | 1 |
| 6 | Gap and go | momentum | 101.16 | 1.17 | 184 | 30.4 | 8.20 | 2.21 | -9.06 | 247 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.92 | -0.09 | 133 | 34.6 | 10.54 | 3.64 | -3.22 | 85 |
| 10 | Agent (rotation) | meta | 99.15 | -0.85 | 181 | 28.2 | -1.20 | -0.38 | -8.81 | 164 |
| 11 | Hold SPY | benchmark | 98.87 | -1.13 | 0 | — | 0.53 | 0.26 | -6.18 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.16 | -3.84 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.66 | -5.34 | 0 | — | -3.31 | -0.83 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.14 | -5.86 | 43 | 39.5 | -7.11 | -1.43 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.59 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.74 | -8.26 | 109 | 22.9 | -16.15 | -5.67 | -18.84 | 80 |
| 21 | Max aggression: 5-day momentum | meta | 91.63 | -8.37 | 19 | 47.4 | -24.10 | -1.10 | -45.81 | 25 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.20 | -9.80 | 404 | 33.2 | -12.53 | -3.68 | -14.11 | 601 |
| 24 | Squeeze breakout · 1h | breakout | 88.74 | -11.26 | 64 | 21.9 | -7.44 | -2.57 | -14.28 | 74 |
| 25 | Hold BTC | benchmark | 87.51 | -12.49 | 1 | 0.0 | -3.69 | -0.41 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.92 | -13.08 | 168 | 26.8 | -13.73 | -2.86 | -21.98 | 225 |
| 27 | Agent | meta | 85.77 | -14.23 | 178 | 35.4 | -15.56 | -7.73 | -15.70 | 203 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.28 | -14.72 | 2 | 0.0 | -4.46 | -0.37 | -24.16 | 1 |
| 29 | Max aggression: 1-day momentum | meta | 84.94 | -15.06 | 27 | 25.9 | -13.72 | -0.15 | -57.50 | 40 |
| 30 | Daily: Bullish score | daily | 83.98 | -16.02 | 16 | 18.8 | -9.04 | -1.35 | -19.56 | 15 |
| 31 | Donchian 55/20 · 1h | breakout | 83.80 | -16.20 | 72 | 13.9 | -23.01 | -4.76 | -29.15 | 97 |
| 32 | ADX DI cross · 1h | trend | 83.78 | -16.22 | 185 | 18.9 | -19.02 | -2.83 | -30.93 | 267 |
| 33 | Agent (aggressive) | meta | 83.77 | -16.23 | 86 | 33.7 | -18.17 | -5.13 | -18.67 | 98 |
| 34 | Keltner breakout · 1h | breakout | 83.73 | -16.27 | 110 | 23.6 | -16.81 | -3.32 | -25.32 | 177 |
| 35 | Stochastic reversion · 1h | reversion | 82.51 | -17.49 | 292 | 48.3 | -23.72 | -3.36 | -27.17 | 394 |
| 36 | Volume breakout · 1h | breakout | 82.17 | -17.83 | 148 | 27.7 | -11.54 | -2.54 | -21.11 | 95 |
| 37 | Opening range 15m | breakout | 82.12 | -17.88 | 501 | 31.3 | -18.17 | -4.81 | -21.11 | 735 |
| 38 | Heikin-Ashi · 1h | trend | 81.35 | -18.65 | 417 | 24.5 | -36.52 | -6.64 | -40.59 | 670 |
| 39 | MFI reversion · 1h | reversion | 80.18 | -19.82 | 373 | 35.4 | -15.92 | -1.94 | -23.02 | 158 |
| 40 | Connors RSI(2) · 1h | reversion | 79.86 | -20.14 | 208 | 39.9 | -21.11 | -7.01 | -21.17 | 123 |
| 41 | MACD cross · 1h | trend | 79.23 | -20.77 | 362 | 22.1 | -27.62 | -4.18 | -38.69 | 471 |
| 42 | CCI reversion · 1h | reversion | 78.53 | -21.47 | 332 | 45.2 | -26.67 | -4.02 | -31.08 | 450 |
| 43 | Bollinger breakout · 1h | breakout | 78.39 | -21.61 | 171 | 22.8 | -19.54 | -3.91 | -28.24 | 242 |
| 44 | MACD zero-line · 1h | trend | 76.89 | -23.11 | 160 | 16.9 | -20.09 | -3.77 | -31.12 | 210 |
| 45 | Bollinger reversion · 1h | reversion | 76.18 | -23.82 | 286 | 41.6 | -25.53 | -3.78 | -33.10 | 368 |
| 46 | Daily: Momentum burst | daily | 75.99 | -24.01 | 27 | 11.1 | -31.06 | -3.94 | -38.23 | 33 |
| 47 | Supertrend · 1h | trend | 75.93 | -24.07 | 168 | 13.1 | -28.23 | -4.76 | -36.25 | 223 |
| 48 | RSI momentum · 1h | momentum | 75.90 | -24.10 | 159 | 12.6 | -24.81 | -3.68 | -37.22 | 215 |
| 49 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 50 | EMA 20/50 cross · 1h | trend | 75.28 | -24.72 | 103 | 10.7 | -25.80 | -4.27 | -36.88 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.77 | -25.23 | 144 | 14.6 | -24.74 | -3.95 | -35.76 | 211 |
| 52 | ROC + volume · 1h | momentum | 74.20 | -25.80 | 376 | 27.7 | -33.32 | -5.77 | -38.60 | 385 |
| 53 | Donchian 20/10 · 1h | breakout | 73.32 | -26.68 | 142 | 19.7 | -27.43 | -4.84 | -35.62 | 211 |
| 54 | Williams %R · 1h | reversion | 72.99 | -27.01 | 353 | 46.2 | -35.38 | -5.43 | -37.07 | 528 |
| 55 | OBV trend · 1h | momentum | 72.33 | -27.67 | 279 | 18.6 | -25.66 | -4.49 | -35.28 | 286 |
| 56 | Z-score reversion · 1h | reversion | 71.87 | -28.13 | 197 | 38.6 | -22.25 | -2.98 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.46 | -30.54 | 175 | 32.6 | -23.90 | -3.26 | -32.54 | 231 |
| 58 | VWAP momentum · 1h | momentum | 68.89 | -31.11 | 857 | 22.6 | -52.33 | -10.78 | -54.64 | 1235 |
| 59 | EMA 9/21 cross · 1h | trend | 67.97 | -32.03 | 253 | 9.9 | -33.39 | -6.06 | -41.69 | 337 |
| 60 | Agent (ML meta-label) | meta | 67.37 | -32.63 | 1738 | 24.9 | -6.94 | -0.83 | -19.59 | 345 |
| 61 | Candlestick reversal · 1h | reversion | 65.41 | -34.59 | 460 | 28.9 | -37.73 | -6.84 | -40.36 | 579 |
| 62 | Three white soldiers | momentum | 60.17 | -39.83 | 518 | 14.7 | -49.23 | -22.56 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.53 | -99.04 | 5307 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.92 | -25.82 | -80.51 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.45 | -44.02 | -93.60 | 2530 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -31.34 | -89.47 | 1929 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.01 | -39.20 | -91.30 | 2338 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.31 | -31.91 | -90.43 | 2214 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.79 | -51.78 | -97.81 | 3454 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -55.48 | -96.46 | 3447 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.38 | -31.96 | -93.42 | 2343 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.10 | -33.86 | -83.48 | 1672 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -52.24 | -99.53 | 5935 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.10 | -41.60 | -92.36 | 2624 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.15 | -95.49 | 3436 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.84 | -99.80 | 6134 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.93 | -41.54 | -91.97 | 2266 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.10 | -23.72 | -75.56 | 1634 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -57.76 | -97.73 | 3538 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -60.43 | -98.84 | 4874 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.15 | -25.90 | -68.78 | 1230 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -51.87 | -94.75 | 2787 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.74 | -36.73 | -85.33 | 1799 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.32 | -99.63 | 6313 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.39 | -31.44 | -89.41 | 2282 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.37 | -19.43 | -77.53 | 1735 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.70 | -35.31 | -90.71 | 2160 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.68 | -50.30 | -96.69 | 3818 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.04 | -52.79 | -89.04 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.09 | -29.17 | -66.91 | 829 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.00 | -22.23 | -72.14 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.36 | -18.43 | -78.56 | 1684 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.17 | -47.53 | -97.17 | 4262 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.12 | -99.93 | 8379 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T18:50 | Bollinger breakout · 1h | buy | TQQQ | 3.92 | — | rebalance up |
| 2026-11-11T18:50 | Bollinger breakout · 1h | sell | XRP-USD | 3.92 | -0.04 | rebalance down |
| 2026-11-11T18:45 | Agent (ML meta-label) | buy | TSLA | 10.08 | — | entry |
| 2026-11-11T18:45 | Agent (ML meta-label) | sell | AMZN | 3.38 | 0.00 | rebalance down |
| 2026-11-11T18:45 | Agent (ML meta-label) | sell | AMD | 3.39 | 0.01 | rebalance down |
| 2026-11-11T18:45 | Agent (aggressive) | buy | COIN | 41.87 | — | following Donchian 20/10 |
| 2026-11-11T18:40 | Agent (ML meta-label) | buy | AMD | 16.83 | — | entry |
| 2026-11-11T18:40 | Agent | buy | SQQQ | 17.15 | — | rebalance up |
| 2026-11-11T18:35 | Agent (ML meta-label) | buy | AAPL | 16.83 | — | entry |
| 2026-11-11T18:35 | Agent (ML meta-label) | sell | AMD | 13.55 | 0.16 | selected signal exited |
| 2026-11-11T18:35 | Agent (aggressive) | sell | COIN | 42.42 | 0.45 | selected signal exited |
| 2026-11-11T18:35 | Agent | sell | UPRO | 17.13 | -0.02 | selected signal exited |
| 2026-11-11T18:30 | Agent (ML meta-label) | buy | AMZN | 5.16 | — | rebalance up |
| 2026-11-11T18:30 | Agent (ML meta-label) | sell | TSLA | 8.01 | -0.01 | selected signal exited |
| 2026-11-11T18:30 | Agent (ML meta-label) | sell | COIN | 8.89 | -0.01 | selected signal exited |
| 2026-11-11T18:30 | Agent (ML meta-label) | sell | AAPL | 11.68 | -0.01 | selected signal exited |
| 2026-11-11T18:30 | Agent | buy | UPRO | 17.15 | — | following Gap and go |
| 2026-11-11T18:30 | CCI reversion · 1h | sell | COIN | 19.60 | 0.44 | exit signal |
| 2026-11-11T18:30 | Stochastic reversion · 1h | sell | NVDA | 11.86 | 0.42 | exit signal |
| 2026-11-11T18:30 | Bollinger breakout · 1h | buy | TQQQ | 3.21 | — | entry |
| 2026-11-11T18:30 | Bollinger breakout · 1h | buy | QQQ | 7.13 | — | entry |
| 2026-11-11T18:30 | Bollinger breakout · 1h | buy | GOOGL | 7.13 | — | entry signal |
| 2026-11-11T18:30 | Bollinger breakout · 1h | buy | BTC-USD | 7.13 | — | entry |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | TSLA | 3.99 | -0.01 | rebalance down |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | TECL | 4.20 | 0.15 | rebalance down |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | SOXL | 4.33 | 0.26 | rebalance down |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | SOL-USD | 4.06 | 0.01 | rebalance down |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | ETH-USD | 4.05 | -0.00 | rebalance down |
| 2026-11-11T18:30 | Bollinger breakout · 1h | sell | DOGE-USD | 3.97 | -0.03 | rebalance down |
| 2026-11-11T18:30 | OBV trend · 1h | buy | TSLA | 9.58 | — | entry signal |
| 2026-11-11T18:30 | OBV trend · 1h | sell | AMD | 3.70 | 0.33 | rebalance down |
| 2026-11-11T18:30 | OBV trend · 1h | sell | AAPL | 5.88 | 0.02 | rebalance down |
| 2026-11-11T18:30 | VWAP momentum · 1h | buy | SOXL | 3.28 | — | entry |
| 2026-11-11T18:30 | VWAP momentum · 1h | sell | META | 3.42 | -0.01 | exit signal |
| 2026-11-11T18:30 | Triple EMA stack · 1h | buy | TSLA | 7.36 | — | entry signal |
| 2026-11-11T18:30 | Triple EMA stack · 1h | buy | LABU | 3.96 | — | rebalance up |
| 2026-11-11T18:30 | Triple EMA stack · 1h | sell | TNA | 5.60 | 0.08 | rebalance down |
| 2026-11-11T18:30 | Triple EMA stack · 1h | sell | META | 5.72 | 0.00 | rebalance down |
| 2026-11-11T18:30 | EMA 20/50 cross · 1h | buy | TSLA | 5.46 | — | rebalance up |
| 2026-11-11T18:30 | EMA 20/50 cross · 1h | buy | META | 3.86 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 18:50:05.000110+00:00 -> 2026-11-11 19:00:05.000110+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
