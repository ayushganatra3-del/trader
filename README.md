# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-12T16:10:05.000122+00:00 · 57114 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £86.24 (-13.76%)

Closed trades 183, win rate 35.0%, fees £5.44, max drawdown -14.98%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AMD | 17.48 | +0.34 |
| LABU | 17.81 | +0.73 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-12 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-11)

**Uptrend** since 2026-11-11 · level normal · 0 distribution days in 25 sessions · timing exposure 100% · VXN 26.74 · VIX 17.49 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 7.2, AAPL 6.8, IWM 5.7, AMZN 5.5, AMD 5.5, TSLA 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 19586 decisions in 2567 calls, $0.2553 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-12T16:10 | 14 / 13 / 3 | AMD 18%, TECL 14% |  |
| Breezy | 2026-11-12T16:10 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-12T16:10 | 10 / 19 / 1 | COIN 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | LABU | 2.12 | +7.29% | 4 |
| Gap and go | UPRO | 1.80 | +3.22% | 4 |
| Supertrend | AMZN | 1.63 | +1.60% | 3 |
| Parabolic SAR | AMD | 1.61 | +3.62% | 7 |
| VWAP reversion | META | 1.46 | +0.30% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.26 | 17.26 | 0 | — | 16.49 | 5.27 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 115.36 | 15.36 | 21 | 66.7 | 20.96 | 4.07 | -4.91 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 114.45 | 14.45 | 33 | 27.3 | 23.04 | 3.29 | -8.66 | 44 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.83 | 4.83 | 0 | — | 7.07 | 1.93 | -6.60 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.89 | 3.89 | 32 | 43.8 | 3.99 | 1.04 | -9.64 | 29 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 102.20 | 2.20 | 137 | 33.6 | 8.81 | 3.23 | -4.12 | 89 |
| 7 | Gap and go | momentum | 100.79 | 0.79 | 192 | 32.8 | 6.83 | 1.94 | -9.06 | 233 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Agent (rotation) | meta | 99.55 | -0.45 | 189 | 30.2 | -0.28 | -0.02 | -8.93 | 169 |
| 11 | Hold SPY | benchmark | 99.07 | -0.93 | 0 | — | -0.51 | -0.01 | -6.18 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -2.94 | 0.06 | -18.69 | 5 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 98.54 | -1.46 | 1 | 0.0 | -1.35 | -0.84 | -5.83 | 2 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.27 | -3.73 | 0 | — | -3.90 | -0.99 | -9.25 | 1 |
| 15 | VWAP reversion · 1h | reversion | 95.64 | -4.36 | 142 | 47.2 | -12.67 | -3.28 | -13.44 | 157 |
| 16 | Copy: Insider buying | copy | 95.33 | -4.67 | 43 | 39.5 | -6.07 | -1.17 | -15.11 | 67 |
| 17 | Timing: Nasdaq FTD · TQQQ | daily | 95.27 | -4.73 | 1 | 0.0 | -4.94 | -0.96 | -16.91 | 2 |
| 18 | Copy: Congress Democrats (NANC) | copy | 94.32 | -5.68 | 0 | — | -3.24 | -0.82 | -10.64 | 1 |
| 19 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.06 | -2.87 | -5.99 | 25 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.81 | -7.22 | -9.28 | 23 |
| 21 | Trend pullback · 1h | trend | 92.36 | -7.64 | 109 | 22.9 | -13.84 | -4.84 | -18.42 | 75 |
| 22 | Squeeze breakout · 1h | breakout | 88.02 | -11.98 | 66 | 21.2 | -8.27 | -2.89 | -14.89 | 75 |
| 23 | Opening range 30m | breakout | 87.39 | -12.62 | 417 | 32.9 | -8.93 | -2.69 | -14.11 | 603 |
| 24 | Parabolic SAR · 1h | trend | 86.69 | -13.31 | 171 | 27.5 | -13.14 | -2.77 | -21.98 | 220 |
| 25 | Agent | meta | 86.24 | -13.76 | 183 | 35.0 | -14.27 | -6.97 | -15.55 | 209 |
| 26 | Hold BTC | benchmark | 84.84 | -15.16 | 1 | 0.0 | -7.65 | -0.91 | -18.34 | 1 |
| 27 | Daily: Bullish score | daily | 84.63 | -15.37 | 16 | 18.8 | -12.03 | -1.66 | -19.56 | 15 |
| 28 | Agent (aggressive) | meta | 84.49 | -15.51 | 89 | 33.7 | -15.82 | -4.35 | -18.51 | 100 |
| 29 | Donchian 55/20 · 1h | breakout | 84.23 | -15.77 | 73 | 13.7 | -22.14 | -4.61 | -29.68 | 93 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 82.89 | -17.11 | 2 | 0.0 | -8.14 | -0.85 | -24.16 | 1 |
| 31 | ADX DI cross · 1h | trend | 82.16 | -17.84 | 191 | 19.4 | -22.18 | -3.83 | -30.15 | 282 |
| 32 | Keltner breakout · 1h | breakout | 82.00 | -18.00 | 114 | 23.7 | -17.48 | -3.59 | -25.87 | 176 |
| 33 | Max aggression: 5-day momentum ⏸ | meta | 81.45 | -18.55 | 20 | 45.0 | -23.22 | -1.10 | -45.81 | 24 |
| 34 | Connors RSI(2) · 1h | reversion | 81.17 | -18.83 | 209 | 40.2 | -19.67 | -6.62 | -20.32 | 120 |
| 35 | MFI reversion · 1h | reversion | 80.71 | -19.29 | 377 | 35.8 | -16.53 | -2.09 | -23.02 | 162 |
| 36 | Volume breakout · 1h | breakout | 80.16 | -19.84 | 155 | 27.7 | -13.78 | -3.22 | -21.11 | 91 |
| 37 | Stochastic reversion · 1h | reversion | 79.91 | -20.09 | 297 | 47.5 | -25.52 | -3.76 | -27.07 | 394 |
| 38 | Opening range 15m | breakout | 79.86 | -20.14 | 512 | 31.2 | -16.56 | -4.33 | -21.36 | 725 |
| 39 | Heikin-Ashi · 1h | trend | 78.15 | -21.86 | 430 | 24.7 | -35.96 | -6.76 | -38.20 | 656 |
| 40 | MACD cross · 1h | trend | 77.96 | -22.04 | 370 | 21.9 | -28.11 | -4.09 | -39.89 | 463 |
| 41 | Bollinger breakout · 1h | breakout | 76.59 | -23.41 | 179 | 22.3 | -21.96 | -4.57 | -29.88 | 241 |
| 42 | MACD zero-line · 1h | trend | 76.55 | -23.45 | 164 | 17.1 | -19.17 | -3.57 | -30.69 | 209 |
| 43 | Supertrend · 1h | trend | 76.33 | -23.67 | 172 | 14.0 | -28.50 | -5.06 | -36.13 | 223 |
| 44 | Max aggression: 1-day momentum ⏸ | meta | 76.00 | -24.00 | 29 | 27.6 | -18.64 | -0.50 | -57.50 | 41 |
| 45 | RSI momentum · 1h | momentum | 75.71 | -24.29 | 162 | 13.6 | -23.75 | -3.62 | -36.41 | 214 |
| 46 | Daily: Momentum burst | daily | 75.53 | -24.47 | 27 | 11.1 | -33.36 | -4.46 | -38.17 | 33 |
| 47 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -30.68 | -8.62 | -32.70 | 117 |
| 48 | EMA 20/50 cross · 1h | trend | 75.07 | -24.93 | 105 | 10.5 | -24.18 | -4.04 | -35.74 | 120 |
| 49 | ROC + volume · 1h | momentum | 73.95 | -26.05 | 385 | 27.8 | -30.36 | -5.62 | -38.34 | 377 |
| 50 | Triple EMA stack · 1h | trend | 73.79 | -26.21 | 147 | 14.3 | -24.86 | -4.09 | -36.50 | 203 |
| 51 | Bollinger reversion · 1h | reversion | 73.24 | -26.76 | 290 | 41.0 | -29.78 | -4.58 | -34.84 | 374 |
| 52 | Donchian 20/10 · 1h | breakout | 72.95 | -27.05 | 145 | 19.3 | -27.07 | -4.85 | -35.87 | 210 |
| 53 | CCI reversion · 1h ⏸ | reversion | 72.29 | -27.71 | 340 | 44.1 | -33.09 | -4.88 | -35.88 | 454 |
| 54 | OBV trend · 1h | momentum | 72.08 | -27.92 | 283 | 19.1 | -27.22 | -4.69 | -37.08 | 283 |
| 55 | Williams %R · 1h | reversion | 68.69 | -31.31 | 358 | 45.5 | -39.32 | -6.25 | -39.86 | 528 |
| 56 | Z-score reversion · 1h | reversion | 68.23 | -31.77 | 199 | 38.2 | -26.74 | -3.72 | -28.98 | 234 |
| 57 | EMA 9/21 cross · 1h | trend | 67.85 | -32.15 | 257 | 9.7 | -33.07 | -6.24 | -41.66 | 336 |
| 58 | VWAP momentum · 1h | momentum | 67.35 | -32.65 | 883 | 22.3 | -51.02 | -10.53 | -52.32 | 1219 |
| 59 | Agent (ML meta-label) | meta | 67.10 | -32.90 | 1775 | 25.0 | -11.05 | -1.28 | -22.42 | 354 |
| 60 | RSI(14) reversion · 1h ⏸ | reversion | 64.34 | -35.66 | 180 | 32.2 | -35.48 | -5.23 | -35.57 | 234 |
| 61 | Candlestick reversal · 1h | reversion | 63.31 | -36.69 | 467 | 28.5 | -42.05 | -7.65 | -42.67 | 587 |
| 62 | Three white soldiers | momentum | 59.65 | -40.35 | 526 | 14.8 | -48.74 | -22.61 | -49.08 | 661 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.98 | -43.60 | -99.01 | 5287 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.81 | -25.70 | -79.84 | 1410 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -45.04 | -93.57 | 2512 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.32 | -31.93 | -89.68 | 1937 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.94 | -39.51 | -91.05 | 2334 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -89.98 | -31.16 | -90.15 | 2189 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.86 | -54.19 | -97.88 | 3457 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.27 | -53.89 | -96.31 | 3422 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.36 | -32.44 | -93.41 | 2338 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.97 | -33.67 | -83.13 | 1658 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.57 | -55.69 | -99.58 | 6014 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.17 | -42.85 | -92.24 | 2609 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.43 | -37.03 | -95.45 | 3451 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -79.00 | -99.82 | 6154 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.14 | -43.98 | -92.16 | 2270 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.05 | -25.11 | -75.21 | 1632 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.60 | -57.24 | -97.62 | 3506 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.89 | -64.09 | -98.91 | 4918 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.36 | -26.92 | -68.53 | 1232 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.71 | -56.76 | -94.76 | 2790 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -85.00 | -38.60 | -85.16 | 1798 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.66 | -76.85 | -99.66 | 6339 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.79 | -32.68 | -90.03 | 2316 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.29 | -20.08 | -78.82 | 1786 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.67 | -36.59 | -90.94 | 2182 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.90 | -53.26 | -96.93 | 3868 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.95 | -55.58 | -89.09 | 2139 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.99 | -29.83 | -66.06 | 823 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.28 | -22.95 | -71.47 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -79.35 | -18.94 | -79.63 | 1718 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.33 | -49.81 | -97.36 | 4305 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -112.17 | -99.93 | 8354 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-12T16:10 | Agent (ML meta-label) | buy | SPY | 8.39 | — | entry |
| 2026-11-12T16:10 | Agent (ML meta-label) | sell | QQQ | 7.44 | 0.03 | selected signal exited |
| 2026-11-12T16:10 | Agent (ML meta-label) | sell | AAPL | 7.40 | -0.01 | selected signal exited |
| 2026-11-12T16:10 | Opening range 30m | buy | PLTR | 6.23 | — | entry signal |
| 2026-11-12T16:10 | Opening range 30m | buy | MSFT | 6.24 | — | entry |
| 2026-11-12T16:10 | Opening range 30m | buy | GOOGL | 6.24 | — | entry |
| 2026-11-12T16:10 | Opening range 30m | buy | ETHU | 6.24 | — | entry signal |
| 2026-11-12T16:10 | Opening range 30m | buy | COIN | 6.24 | — | entry |
| 2026-11-12T16:10 | Opening range 30m | buy | AMD | 6.24 | — | entry |
| 2026-11-12T16:10 | Opening range 30m | sell | UPRO | 4.62 | 0.04 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | TQQQ | 4.70 | 0.07 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | TECL | 4.76 | 0.17 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | SPY | 4.56 | 0.01 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | SOXL | 4.83 | 0.13 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | QQQ | 4.58 | 0.02 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | NVDA | 4.64 | 0.08 | rebalance down |
| 2026-11-12T16:10 | Opening range 30m | sell | MSTR | 4.77 | 0.15 | rebalance down |
| 2026-11-12T16:06 | Agent (ML meta-label) | buy | QQQ | 7.41 | — | entry |
| 2026-11-12T16:06 | Agent (ML meta-label) | buy | AAPL | 7.41 | — | entry |
| 2026-11-12T16:06 | Agent (ML meta-label) | sell | SPY | 7.39 | 0.00 | selected signal exited |
| 2026-11-12T16:06 | Three white soldiers | buy | SOL-USD | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | MSTR | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | GOOGL | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | ETHU | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | ETH-USD | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | DOGE-USD | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | BTC-USD | 7.42 | — | entry signal |
| 2026-11-12T16:06 | Three white soldiers | buy | BITX | 7.42 | — | entry signal |
| 2026-11-12T16:00 | Agent (ML meta-label) | sell | QQQ | 7.41 | 0.02 | selected signal exited |
| 2026-11-12T16:00 | MFI reversion · 1h | buy | SOL-USD | 11.47 | — | entry signal |
| 2026-11-12T16:00 | MFI reversion · 1h | buy | ETH-USD | 11.49 | — | entry signal |
| 2026-11-12T16:00 | MFI reversion · 1h | buy | DOGE-USD | 11.49 | — | entry signal |
| 2026-11-12T16:00 | MFI reversion · 1h | sell | TECL | 8.31 | 0.43 | rebalance down |
| 2026-11-12T16:00 | MFI reversion · 1h | sell | SPY | 8.37 | 0.06 | rebalance down |
| 2026-11-12T16:00 | MFI reversion · 1h | sell | MSFT | 8.51 | 0.02 | rebalance down |
| 2026-11-12T16:00 | MFI reversion · 1h | sell | AMZN | 8.71 | -0.03 | rebalance down |
| 2026-11-12T16:00 | VWAP reversion · 1h | buy | XRP-USD | 23.88 | — | entry signal |
| 2026-11-12T16:00 | VWAP reversion · 1h | buy | BTC-USD | 23.88 | — | entry signal |
| 2026-11-12T16:00 | Z-score reversion · 1h | buy | SOL-USD | 16.98 | — | entry signal |
| 2026-11-12T16:00 | Bollinger reversion · 1h | buy | XRP-USD | 14.61 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-14 16:10:05.000122+00:00 -> 2026-11-12 16:20:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
