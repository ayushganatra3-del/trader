# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-09T18:36:05.000161+00:00 · 53686 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.47 (-12.53%)

Closed trades 159, win rate 35.8%, fees £4.91, max drawdown -13.02%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.50 | -0.11 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-09 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, KOD 12%, RAPP 12%, LRN 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-06)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 34.02 · VIX 25.64 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 8.4, AMZN 5.2, AAPL 3.5, MSFT 3.2, MSTR 1.4, BITX 1.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 27960 decisions in 2922 calls, $0.3536 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-09T18:36 | 6 / 20 / 4 | AMD 18%, SOXL 15% |  |
| Breezy | 2026-11-09T18:36 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-09T18:36 | 8 / 21 / 1 | COIN 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Donchian 20/10 | COIN | 2.14 | +8.48% | 5 |
| MFI reversion | LABU | 2.01 | +7.77% | 4 |
| RSI(14) reversion | SQQQ | 1.94 | +6.29% | 3 |
| Keltner breakout | COIN | 1.82 | +1.65% | 3 |
| VWAP momentum | TSLA | 1.69 | +2.40% | 13 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 116.74 | 16.74 | 19 | 68.4 | 16.81 | 3.49 | -4.91 | 27 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 112.19 | 12.19 | 0 | — | 13.12 | 4.58 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 111.15 | 11.15 | 30 | 26.7 | 19.10 | 2.95 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.24 | 3.24 | 30 | 43.3 | 2.97 | 0.82 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 101.17 | 1.17 | 123 | 35.0 | 9.52 | 3.83 | -2.27 | 89 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.89 | 0.89 | 0 | — | 4.41 | 1.30 | -6.60 | 1 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.40 | 0.40 | 7 | 42.9 | -1.58 | 0.12 | -18.69 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Gap and go | momentum | 98.49 | -1.51 | 179 | 29.1 | 3.45 | 1.05 | -9.06 | 241 |
| 11 | Agent (rotation) | meta | 97.56 | -2.44 | 176 | 27.8 | -3.58 | -1.54 | -10.11 | 161 |
| 12 | VWAP reversion · 1h | reversion | 97.15 | -2.85 | 132 | 47.0 | -12.05 | -3.08 | -12.05 | 152 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.88 | -5.83 | 1 |
| 14 | Hold SPY | benchmark | 96.54 | -3.46 | 0 | — | -1.95 | -0.56 | -6.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.26 | -5.74 | 0 | — | -3.86 | -1.03 | -9.25 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 94.10 | -5.90 | 21 | 19.0 | -7.10 | -6.03 | -7.78 | 22 |
| 17 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.55 | -5.99 | 28 |
| 18 | Trend pullback · 1h | trend | 92.59 | -7.41 | 108 | 23.1 | -13.53 | -5.08 | -17.75 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.53 | -7.47 | 0 | — | -4.29 | -1.16 | -10.64 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.04 | -16.91 | 1 |
| 21 | Opening range 30m | breakout | 90.08 | -9.92 | 378 | 32.3 | -14.54 | -4.66 | -15.99 | 598 |
| 22 | Copy: Insider buying | copy | 89.51 | -10.49 | 40 | 37.5 | -11.16 | -2.55 | -16.06 | 63 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.08 | -2.81 | -14.15 | 79 |
| 24 | Agent | meta | 87.47 | -12.53 | 159 | 35.8 | -13.14 | -6.82 | -13.69 | 202 |
| 25 | Hold BTC | benchmark | 86.60 | -13.40 | 1 | 0.0 | -5.36 | -0.64 | -15.58 | 1 |
| 26 | Daily: Bullish score | daily | 86.31 | -13.69 | 15 | 20.0 | -9.98 | -1.41 | -17.10 | 14 |
| 27 | Parabolic SAR · 1h | trend | 85.67 | -14.33 | 167 | 26.9 | -11.27 | -2.04 | -21.29 | 226 |
| 28 | Agent (aggressive) | meta | 84.33 | -15.68 | 75 | 32.0 | -15.74 | -4.46 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 83.74 | -16.26 | 71 | 14.1 | -16.42 | -3.48 | -21.91 | 103 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 83.29 | -16.71 | 2 | 0.0 | -9.06 | -1.04 | -24.16 | 1 |
| 31 | Opening range 15m | breakout | 83.18 | -16.82 | 466 | 30.5 | -19.21 | -5.53 | -20.97 | 736 |
| 32 | Stochastic reversion · 1h | reversion | 82.72 | -17.28 | 279 | 48.4 | -23.83 | -3.55 | -27.72 | 385 |
| 33 | Keltner breakout · 1h | breakout | 81.83 | -18.17 | 107 | 23.4 | -22.30 | -4.73 | -25.05 | 178 |
| 34 | Volume breakout · 1h | breakout | 81.47 | -18.53 | 145 | 27.6 | -14.85 | -3.37 | -21.11 | 95 |
| 35 | Connors RSI(2) · 1h | reversion | 80.77 | -19.23 | 205 | 40.0 | -19.06 | -6.35 | -19.40 | 125 |
| 36 | Heikin-Ashi · 1h | trend | 79.64 | -20.36 | 398 | 22.9 | -38.32 | -7.22 | -41.75 | 681 |
| 37 | Max aggression: 5-day momentum ⏸ | meta | 79.24 | -20.76 | 18 | 44.4 | -38.97 | -2.62 | -44.97 | 25 |
| 38 | ADX DI cross · 1h | trend | 79.18 | -20.82 | 179 | 18.4 | -22.68 | -3.87 | -28.65 | 269 |
| 39 | MFI reversion · 1h | reversion | 79.05 | -20.95 | 347 | 34.0 | -16.43 | -2.13 | -21.23 | 163 |
| 40 | CCI reversion · 1h | reversion | 78.72 | -21.28 | 310 | 44.2 | -24.98 | -3.86 | -30.29 | 461 |
| 41 | Ichimoku · 1h | trend | 77.70 | -22.30 | 96 | 15.6 | -23.66 | -4.85 | -30.03 | 124 |
| 42 | Bollinger breakout · 1h | breakout | 76.93 | -23.07 | 170 | 22.9 | -22.31 | -4.64 | -27.85 | 241 |
| 43 | Bollinger reversion · 1h | reversion | 75.61 | -24.39 | 272 | 41.2 | -26.25 | -4.05 | -32.97 | 372 |
| 44 | MACD cross · 1h | trend | 75.06 | -24.94 | 349 | 22.6 | -33.03 | -5.42 | -39.64 | 487 |
| 45 | Z-score reversion · 1h | reversion | 74.86 | -25.14 | 176 | 36.4 | -20.61 | -2.98 | -27.66 | 228 |
| 46 | Williams %R · 1h | reversion | 74.79 | -25.21 | 335 | 46.9 | -34.62 | -5.51 | -37.58 | 541 |
| 47 | MACD zero-line · 1h | trend | 74.39 | -25.61 | 157 | 16.6 | -24.90 | -5.14 | -29.19 | 211 |
| 48 | EMA 20/50 cross · 1h | trend | 74.33 | -25.66 | 102 | 10.8 | -21.76 | -3.63 | -31.10 | 128 |
| 49 | Supertrend · 1h | trend | 73.22 | -26.78 | 167 | 13.2 | -31.37 | -5.67 | -34.87 | 229 |
| 50 | RSI momentum · 1h | momentum | 73.00 | -27.00 | 159 | 12.6 | -23.79 | -3.79 | -33.27 | 214 |
| 51 | Triple EMA stack · 1h | trend | 72.47 | -27.53 | 143 | 14.7 | -26.34 | -4.65 | -34.72 | 202 |
| 52 | OBV trend · 1h | momentum | 71.74 | -28.26 | 274 | 18.2 | -28.33 | -5.64 | -34.25 | 275 |
| 53 | ROC + volume · 1h | momentum | 71.56 | -28.44 | 349 | 25.5 | -36.79 | -6.97 | -39.35 | 386 |
| 54 | Daily: Momentum burst | daily | 70.52 | -29.48 | 26 | 11.5 | -38.45 | -5.41 | -39.42 | 31 |
| 55 | Donchian 20/10 · 1h | breakout | 70.45 | -29.55 | 142 | 19.7 | -31.56 | -5.90 | -35.64 | 209 |
| 56 | RSI(14) reversion · 1h | reversion | 67.96 | -32.04 | 160 | 30.6 | -32.07 | -4.93 | -35.23 | 246 |
| 57 | Agent (ML meta-label) | meta | 67.78 | -32.22 | 1601 | 23.8 | -10.04 | -1.26 | -22.36 | 352 |
| 58 | VWAP momentum · 1h | momentum | 67.56 | -32.44 | 809 | 21.6 | -51.90 | -11.14 | -53.77 | 1234 |
| 59 | Max aggression: 1-day momentum | meta | 67.43 | -32.58 | 27 | 25.9 | -32.40 | -1.70 | -57.50 | 42 |
| 60 | EMA 9/21 cross · 1h | trend | 65.52 | -34.48 | 247 | 9.7 | -39.18 | -7.54 | -40.80 | 332 |
| 61 | Candlestick reversal · 1h | reversion | 65.04 | -34.96 | 434 | 28.6 | -38.14 | -6.89 | -38.91 | 593 |
| 62 | Three white soldiers | momentum | 62.46 | -37.54 | 493 | 15.2 | -48.64 | -22.61 | -48.65 | 647 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -45.75 | -98.99 | 5266 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.96 | -26.45 | -80.00 | 1421 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.19 | -46.50 | -93.29 | 2501 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.25 | -32.41 | -89.30 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.70 | -40.12 | -90.76 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.06 | -31.83 | -90.07 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -54.78 | -97.71 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -57.91 | -96.29 | 3406 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.55 | -32.37 | -93.61 | 2413 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -34.63 | -82.28 | 1671 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.54 | -56.06 | -99.54 | 5991 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.35 | -42.96 | -92.54 | 2593 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -37.32 | -95.55 | 3409 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -76.04 | -99.79 | 6149 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -44.12 | -91.76 | 2257 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.46 | -24.83 | -75.90 | 1589 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.66 | -62.07 | -97.67 | 3498 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.84 | -63.71 | -98.84 | 4881 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.65 | -27.06 | -69.44 | 1208 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.13 | -94.59 | 2735 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.91 | -37.04 | -85.01 | 1773 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -75.45 | -99.65 | 6377 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.66 | -32.75 | -89.67 | 2270 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.85 | -20.15 | -78.85 | 1757 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.73 | -90.70 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.77 | -52.70 | -96.80 | 3889 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -58.06 | -89.38 | 2153 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.01 | -29.05 | -66.26 | 808 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.36 | -23.21 | -72.00 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.65 | -19.13 | -79.73 | 1688 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.28 | -50.30 | -97.31 | 4324 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -109.48 | -99.93 | 8281 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | QQQ | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | LABU | 4.76 | — | following MFI reversion |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | GOOGL | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | buy | AAPL | 4.76 | — | entry |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | SOXL | 4.28 | 0.01 | rebalance down |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | META | 5.47 | -0.01 | selected signal exited |
| 2026-11-09T18:35 | Agent (ML meta-label) | sell | BITX | 4.81 | -0.04 | selected signal exited |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | TECL | 1.98 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | SOXL | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | META | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | buy | AMD | 5.48 | — | entry |
| 2026-11-09T18:30 | Agent (ML meta-label) | sell | PLTR | 5.49 | 0.38 | selected signal exited |
| 2026-11-09T18:30 | CCI reversion · 1h | sell | IWM | 1.82 | 0.03 | exit signal |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | SQQQ | 5.14 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | ETH-USD | 5.84 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | DOGE-USD | 3.76 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | COIN | 3.75 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | buy | BTC-USD | 6.59 | — | rebalance up |
| 2026-11-09T18:30 | Candlestick reversal · 1h | sell | TSLA | 9.33 | 0.20 | exit signal |
| 2026-11-09T18:30 | Candlestick reversal · 1h | sell | PLTR | 9.33 | 0.30 | exit signal |
| 2026-11-09T18:30 | VWAP momentum · 1h | sell | TSLA | 3.04 | -0.02 | exit signal |
| 2026-11-09T18:30 | VWAP momentum · 1h | sell | AAPL | 3.05 | -0.02 | exit signal |
| 2026-11-09T18:30 | Heikin-Ashi · 1h | sell | GOOGL | 3.95 | -0.02 | exit signal |
| 2026-11-09T18:30 | MACD zero-line · 1h | buy | IWM | 18.59 | — | entry signal |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | buy | TNA | 4.95 | — | entry |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | buy | PLTR | 5.46 | — | entry signal |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | buy | LABU | 5.46 | — | entry |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | sell | GOOGL | 3.86 | -0.06 | rebalance down |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | sell | AMZN | 3.90 | 0.17 | rebalance down |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | sell | AMD | 4.02 | 0.05 | rebalance down |
| 2026-11-09T18:30 | EMA 9/21 cross · 1h | sell | AAPL | 3.88 | -0.02 | rebalance down |
| 2026-11-09T18:20 | Agent (ML meta-label) | sell | TSLA | 3.91 | -0.01 | selected signal exited |
| 2026-11-09T18:20 | Agent (ML meta-label) | sell | META | 4.84 | -0.01 | selected signal exited |
| 2026-11-09T18:20 | Agent (ML meta-label) | sell | LABU | 5.25 | 0.03 | selected signal exited |
| 2026-11-09T18:20 | Agent (ML meta-label) | sell | AMD | 4.91 | -0.01 | selected signal exited |
| 2026-11-09T18:20 | Opening range 30m | buy | PLTR | 2.36 | — | entry |
| 2026-11-09T18:20 | Opening range 30m | buy | LABU | 6.42 | — | entry |
| 2026-11-09T18:20 | Opening range 30m | sell | MSTR | 8.77 | -0.17 | exit signal |
| 2026-11-09T18:15 | Agent (ML meta-label) | buy | TSLA | 3.92 | — | following VWAP momentum |
| 2026-11-09T18:15 | Agent (ML meta-label) | buy | META | 4.85 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-11 18:36:05.000161+00:00 -> 2026-11-09 18:46:05.000161+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-11 18:36:05.000161+00:00 -> 2026-11-09 18:46:05.000161+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-11 18:36:05.000161+00:00 -> 2026-11-09 18:46:05.000161+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
