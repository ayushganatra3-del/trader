# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-11T18:20:05.000142+00:00 · 56054 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.84 (-14.16%)

Closed trades 176, win rate 35.2%, fees £5.30, max drawdown -14.55%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| COIN | 17.49 | +0.15 |
| SQQQ | 34.36 | -0.25 |
| UPRO | 17.16 | -0.01 |

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

Today: 27564 decisions in 2748 calls, $0.3467 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-11T18:20 | 7 / 12 / 12 | cash |  |
| Breezy | 2026-11-11T18:20 | 0 / 30 / 1 | cash |  |
| Boozy | 2026-11-11T18:20 | 8 / 21 / 2 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 2.20 | +9.77% | 14 |
| Donchian 20/10 | COIN | 1.81 | +7.11% | 7 |
| Williams %R | SQQQ | 1.66 | +4.12% | 18 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.52 | 17.52 | 20 | 70.0 | 19.07 | 3.82 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 114.98 | 14.98 | 0 | — | 14.93 | 4.92 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 109.59 | 9.59 | 33 | 27.3 | 17.65 | 2.67 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.79 | 4.79 | 31 | 45.2 | 4.91 | 1.24 | -9.64 | 29 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 103.63 | 3.63 | 0 | — | 6.12 | 1.69 | -6.60 | 1 |
| 6 | Gap and go | momentum | 100.84 | 0.84 | 184 | 30.4 | 7.91 | 2.15 | -9.06 | 247 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.87 | -0.13 | 133 | 34.6 | 10.50 | 3.62 | -3.22 | 85 |
| 10 | Agent (rotation) | meta | 98.87 | -1.13 | 181 | 28.2 | -1.54 | -0.51 | -8.95 | 167 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 12 | Hold SPY | benchmark | 98.76 | -1.24 | 0 | — | 0.47 | 0.25 | -6.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.13 | -3.87 | 0 | — | -3.14 | -0.78 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.99 | -4.01 | 140 | 47.1 | -12.37 | -3.17 | -13.44 | 153 |
| 16 | Copy: Congress Democrats (NANC) | copy | 94.69 | -5.30 | 0 | — | -3.24 | -0.81 | -10.64 | 1 |
| 17 | Copy: Insider buying | copy | 94.18 | -5.82 | 43 | 39.5 | -7.02 | -1.41 | -15.11 | 67 |
| 18 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.60 | -3.30 | -5.99 | 26 |
| 19 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 20 | Trend pullback · 1h | trend | 91.67 | -8.33 | 109 | 22.9 | -16.20 | -5.68 | -18.84 | 80 |
| 21 | Max aggression: 5-day momentum | meta | 91.40 | -8.60 | 19 | 47.4 | -24.26 | -1.11 | -45.81 | 25 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 89.99 | -10.01 | 404 | 33.2 | -12.52 | -3.71 | -14.11 | 601 |
| 24 | Squeeze breakout · 1h | breakout | 88.76 | -11.24 | 64 | 21.9 | -6.23 | -1.91 | -14.28 | 73 |
| 25 | Hold BTC | benchmark | 87.45 | -12.55 | 1 | 0.0 | -3.85 | -0.43 | -16.64 | 1 |
| 26 | Parabolic SAR · 1h | trend | 86.86 | -13.14 | 168 | 26.8 | -13.80 | -2.88 | -21.98 | 225 |
| 27 | Agent | meta | 85.84 | -14.16 | 176 | 35.2 | -15.58 | -7.97 | -15.69 | 205 |
| 28 | Copy: Cathie Wood (ARKK) | copy | 85.31 | -14.69 | 2 | 0.0 | -4.55 | -0.39 | -24.16 | 1 |
| 29 | Max aggression: 1-day momentum | meta | 84.73 | -15.27 | 27 | 25.9 | -13.91 | -0.16 | -57.50 | 40 |
| 30 | Daily: Bullish score | daily | 84.02 | -15.98 | 16 | 18.8 | -8.76 | -1.30 | -19.52 | 15 |
| 31 | Agent (aggressive) | meta | 83.81 | -16.19 | 85 | 32.9 | -18.98 | -5.44 | -19.35 | 99 |
| 32 | Donchian 55/20 · 1h | breakout | 83.66 | -16.34 | 72 | 13.9 | -22.93 | -4.75 | -29.08 | 97 |
| 33 | ADX DI cross · 1h | trend | 83.56 | -16.44 | 185 | 18.9 | -19.61 | -3.03 | -30.84 | 274 |
| 34 | Keltner breakout · 1h | breakout | 83.49 | -16.51 | 110 | 23.6 | -17.11 | -3.41 | -25.32 | 177 |
| 35 | Stochastic reversion · 1h | reversion | 82.51 | -17.49 | 291 | 48.1 | -23.69 | -3.35 | -27.17 | 394 |
| 36 | Volume breakout · 1h | breakout | 81.98 | -18.02 | 148 | 27.7 | -11.69 | -2.59 | -21.11 | 95 |
| 37 | Opening range 15m | breakout | 81.92 | -18.08 | 501 | 31.3 | -18.29 | -4.86 | -21.11 | 735 |
| 38 | Heikin-Ashi · 1h | trend | 81.18 | -18.82 | 417 | 24.5 | -37.04 | -6.75 | -41.01 | 673 |
| 39 | MFI reversion · 1h | reversion | 80.00 | -20.00 | 373 | 35.4 | -15.80 | -1.93 | -23.02 | 158 |
| 40 | Connors RSI(2) · 1h | reversion | 79.93 | -20.07 | 208 | 39.9 | -20.90 | -6.95 | -20.95 | 124 |
| 41 | MACD cross · 1h | trend | 79.10 | -20.90 | 362 | 22.1 | -27.77 | -4.25 | -38.68 | 473 |
| 42 | CCI reversion · 1h | reversion | 78.54 | -21.46 | 331 | 45.0 | -26.50 | -3.97 | -31.08 | 450 |
| 43 | Bollinger breakout · 1h | breakout | 78.40 | -21.60 | 171 | 22.8 | -19.57 | -3.92 | -28.24 | 241 |
| 44 | MACD zero-line · 1h | trend | 76.72 | -23.28 | 160 | 16.9 | -18.94 | -3.31 | -31.28 | 211 |
| 45 | Bollinger reversion · 1h | reversion | 76.23 | -23.77 | 286 | 41.6 | -25.31 | -3.76 | -32.97 | 369 |
| 46 | Supertrend · 1h | trend | 75.81 | -24.19 | 168 | 13.1 | -28.13 | -4.73 | -36.07 | 230 |
| 47 | Daily: Momentum burst | daily | 75.74 | -24.26 | 27 | 11.1 | -31.29 | -4.00 | -38.23 | 33 |
| 48 | RSI momentum · 1h | momentum | 75.73 | -24.27 | 159 | 12.6 | -24.98 | -3.72 | -37.27 | 215 |
| 49 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.99 | -8.69 | -31.64 | 117 |
| 50 | EMA 20/50 cross · 1h | trend | 75.21 | -24.79 | 102 | 10.8 | -25.86 | -4.28 | -36.88 | 115 |
| 51 | Triple EMA stack · 1h | trend | 74.66 | -25.34 | 144 | 14.6 | -25.96 | -4.25 | -36.71 | 209 |
| 52 | ROC + volume · 1h | momentum | 73.99 | -26.01 | 376 | 27.7 | -34.19 | -6.04 | -38.60 | 386 |
| 53 | Donchian 20/10 · 1h | breakout | 73.13 | -26.87 | 142 | 19.7 | -27.96 | -4.95 | -35.62 | 212 |
| 54 | Williams %R · 1h | reversion | 73.02 | -26.98 | 353 | 46.2 | -35.29 | -5.40 | -37.03 | 528 |
| 55 | OBV trend · 1h | momentum | 72.21 | -27.79 | 279 | 18.6 | -25.33 | -4.40 | -35.07 | 284 |
| 56 | Z-score reversion · 1h | reversion | 71.84 | -28.16 | 197 | 38.6 | -22.25 | -2.98 | -28.98 | 234 |
| 57 | RSI(14) reversion · 1h | reversion | 69.48 | -30.52 | 175 | 32.6 | -24.99 | -3.48 | -32.54 | 232 |
| 58 | VWAP momentum · 1h | momentum | 68.81 | -31.19 | 854 | 22.5 | -51.42 | -10.28 | -54.64 | 1237 |
| 59 | EMA 9/21 cross · 1h | trend | 67.87 | -32.13 | 253 | 9.9 | -33.51 | -6.10 | -41.69 | 337 |
| 60 | Agent (ML meta-label) | meta | 67.25 | -32.75 | 1734 | 24.9 | -12.08 | -1.61 | -21.47 | 335 |
| 61 | Candlestick reversal · 1h | reversion | 65.44 | -34.56 | 460 | 28.9 | -37.19 | -6.70 | -39.89 | 579 |
| 62 | Three white soldiers | momentum | 60.13 | -39.87 | 518 | 14.7 | -49.26 | -22.59 | -49.27 | 658 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.02 | -44.80 | -99.05 | 5315 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.93 | -25.85 | -80.53 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.47 | -44.29 | -93.62 | 2537 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.26 | -31.36 | -89.40 | 1930 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.03 | -39.29 | -91.32 | 2341 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -31.96 | -90.44 | 2212 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -51.51 | -97.81 | 3452 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -55.89 | -96.46 | 3452 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.33 | -32.11 | -93.39 | 2340 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.11 | -33.88 | -83.49 | 1674 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.53 | -52.37 | -99.54 | 5938 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.16 | -41.93 | -92.31 | 2627 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -37.14 | -95.49 | 3438 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -68.50 | -99.80 | 6132 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -41.62 | -91.96 | 2267 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.53 | -24.37 | -75.44 | 1648 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -57.81 | -97.73 | 3536 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.83 | -60.39 | -98.84 | 4873 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.09 | -25.80 | -69.13 | 1241 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.61 | -52.25 | -94.75 | 2791 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.92 | -37.62 | -85.30 | 1805 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.06 | -99.63 | 6307 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.45 | -31.67 | -89.46 | 2284 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.49 | -19.55 | -77.64 | 1736 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.73 | -35.15 | -90.74 | 2159 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.67 | -50.25 | -96.69 | 3819 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.03 | -53.10 | -89.03 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.24 | -27.07 | -66.69 | 828 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.03 | -22.27 | -72.14 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -78.28 | -18.34 | -78.49 | 1683 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.16 | -47.38 | -97.16 | 4259 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.36 | -99.93 | 8371 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-11T18:20 | Agent (ML meta-label) | sell | AAPL | 16.56 | -0.02 | selected signal exited |
| 2026-11-11T18:20 | Agent | buy | UPRO | 17.17 | — | following Gap and go |
| 2026-11-11T18:15 | Agent (ML meta-label) | sell | COIN | 0.87 | -0.00 | selected signal exited |
| 2026-11-11T18:10 | Agent (ML meta-label) | buy | AAPL | 16.58 | — | entry |
| 2026-11-11T18:10 | Agent (ML meta-label) | sell | TSLA | 10.16 | -0.00 | selected signal exited |
| 2026-11-11T18:10 | Agent (ML meta-label) | sell | COIN | 12.53 | -0.03 | rebalance down |
| 2026-11-11T18:10 | Three white soldiers | buy | GOOGL | 15.03 | — | entry signal |
| 2026-11-11T18:05 | Agent (ML meta-label) | buy | TSLA | 10.16 | — | entry |
| 2026-11-11T18:05 | Agent (ML meta-label) | buy | TECL | 13.44 | — | entry |
| 2026-11-11T18:05 | Agent (ML meta-label) | buy | COIN | 13.44 | — | following Donchian 20/10 |
| 2026-11-11T18:05 | Agent (ML meta-label) | sell | AMD | 3.42 | 0.01 | rebalance down |
| 2026-11-11T18:05 | Williams %R · 1h | buy | DOGE-USD | 2.41 | — | entry |
| 2026-11-11T18:05 | Stochastic reversion · 1h | buy | DOGE-USD | 11.75 | — | entry |
| 2026-11-11T18:05 | VWAP momentum · 1h | buy | BITX | 2.19 | — | entry |
| 2026-11-11T18:05 | VWAP momentum · 1h | buy | AMD | 3.12 | — | entry |
| 2026-11-11T18:05 | VWAP momentum · 1h | sell | TQQQ | 5.31 | 0.13 | target is flat |
| 2026-11-11T18:05 | Three white soldiers | sell | UPRO | 15.02 | -0.03 | exit signal |
| 2026-11-11T18:05 | Three white soldiers | sell | TNA | 15.03 | -0.03 | exit signal |
| 2026-11-11T18:00 | Agent (ML meta-label) | sell | TECL | 7.84 | -0.00 | selected signal exited |
| 2026-11-11T18:00 | Williams %R · 1h | buy | XRP-USD | 4.26 | — | rebalance up |
| 2026-11-11T18:00 | Williams %R · 1h | buy | MSTR | 4.27 | — | rebalance up |
| 2026-11-11T18:00 | Williams %R · 1h | buy | ETHU | 3.93 | — | rebalance up |
| 2026-11-11T18:00 | Williams %R · 1h | buy | BITX | 4.08 | — | rebalance up |
| 2026-11-11T18:00 | Williams %R · 1h | sell | DOGE-USD | 10.37 | 0.19 | exit signal |
| 2026-11-11T18:00 | Stochastic reversion · 1h | sell | DOGE-USD | 11.75 | 0.04 | exit signal |
| 2026-11-11T18:00 | Z-score reversion · 1h | sell | ETH-USD | 17.98 | 0.13 | exit signal |
| 2026-11-11T18:00 | Three white soldiers | sell | TQQQ | 15.02 | -0.04 | exit signal |
| 2026-11-11T17:55 | Agent (ML meta-label) | buy | TECL | 7.84 | — | entry |
| 2026-11-11T17:55 | Agent | sell | UPRO | 17.18 | -0.01 | selected signal exited |
| 2026-11-11T17:55 | EMA 20/50 cross · 1h | buy | TSLA | 3.76 | — | rebalance up |
| 2026-11-11T17:55 | EMA 20/50 cross · 1h | sell | LABU | 3.76 | 0.00 | rebalance down |
| 2026-11-11T17:45 | Agent (ML meta-label) | sell | AAPL | 16.78 | -0.02 | selected signal exited |
| 2026-11-11T17:45 | Agent | buy | UPRO | 17.20 | — | following Gap and go |
| 2026-11-11T17:40 | Agent (aggressive) | buy | SQQQ | 41.53 | — | following Stochastic reversion, Williams %R |
| 2026-11-11T17:40 | Agent | buy | SQQQ | 17.18 | — | rebalance up |
| 2026-11-11T17:40 | Agent | sell | UPRO | 17.20 | 0.01 | selected signal exited |
| 2026-11-11T17:40 | Three white soldiers | buy | UPRO | 15.05 | — | entry |
| 2026-11-11T17:35 | Agent (ML meta-label) | buy | AMD | 16.80 | — | entry |
| 2026-11-11T17:35 | Agent (ML meta-label) | buy | AAPL | 16.80 | — | entry |
| 2026-11-11T17:35 | Agent (aggressive) | sell | SQQQ | 41.41 | -0.70 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-13 18:20:05.000142+00:00 -> 2026-11-11 18:30:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
