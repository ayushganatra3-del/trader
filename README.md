# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T18:56:05.000129+00:00 · 54886 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.49 (-12.51%)

Closed trades 169, win rate 35.5%, fees £5.11, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 17.49 | -0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-10 | BBTX 12%, MGM 12%, KNOP 12%, MDGL 12%, ASPE 12%, LRN 12%, KOD 12%, KMI 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-09)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.97 · VIX 19.92 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.2, MSFT 6.4, AMZN 5.9, AAPL 5.2, IWM 4.5, LABU 3.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 29054 decisions in 2806 calls, $0.3651 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T18:56 | 4 / 22 / 4 | TECL 15% |  |
| Breezy | 2026-11-10T18:56 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-11-10T18:56 | 6 / 23 / 1 | COIN 66% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion | SQQQ | 1.79 | +7.91% | 12 |
| Donchian 20/10 | COIN | 1.62 | +6.48% | 6 |
| MFI reversion | LABU | 1.60 | +6.02% | 3 |
| Ichimoku | TSLA | 1.50 | +0.60% | 4 |
| Gap and go | UPRO | 1.39 | +2.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 117.56 | 17.56 | 20 | 70.0 | 19.49 | 3.91 | -4.91 | 26 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 115.04 | 15.04 | 0 | — | 15.16 | 4.99 | -5.18 | 1 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 110.59 | 10.59 | 32 | 28.1 | 19.15 | 2.87 | -8.66 | 44 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 101.26 | 1.26 | 0 | — | 4.12 | 1.20 | -6.60 | 1 |
| 6 | Day trade: Stocks in Play ORB | daytrade | 100.36 | 0.36 | 131 | 35.1 | 8.15 | 3.05 | -2.67 | 90 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 11 | Agent (rotation) | meta | 97.87 | -2.13 | 179 | 28.5 | -3.36 | -1.33 | -10.00 | 148 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.58 | -3.42 | 0 | — | -1.95 | -0.61 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 96.08 | -3.92 | 137 | 46.0 | -12.86 | -3.30 | -13.73 | 153 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.43 | -5.57 | 0 | — | -4.95 | -1.29 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Copy: Insider buying | copy | 92.92 | -7.08 | 43 | 39.5 | -8.03 | -1.65 | -15.11 | 67 |
| 19 | Trend pullback · 1h | trend | 92.83 | -7.17 | 108 | 23.1 | -13.32 | -4.95 | -17.51 | 78 |
| 20 | Copy: Congress Democrats (NANC) | copy | 92.24 | -7.76 | 0 | — | -4.65 | -1.23 | -10.64 | 1 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.28 | -2.87 | -14.15 | 76 |
| 23 | Opening range 30m | breakout | 88.48 | -11.52 | 403 | 33.3 | -14.91 | -4.59 | -14.91 | 605 |
| 24 | Agent | meta | 87.49 | -12.51 | 169 | 35.5 | -13.70 | -6.94 | -14.55 | 201 |
| 25 | Daily: Bullish score | daily | 86.77 | -13.23 | 15 | 20.0 | -7.57 | -1.11 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 86.01 | -13.99 | 1 | 0.0 | -6.33 | -0.83 | -16.64 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.25 | -14.76 | 168 | 26.8 | -13.93 | -2.83 | -21.70 | 225 |
| 28 | Agent (aggressive) | meta | 84.98 | -15.02 | 79 | 32.9 | -16.09 | -4.52 | -18.49 | 93 |
| 29 | Donchian 55/20 · 1h | breakout | 84.28 | -15.72 | 71 | 14.1 | -16.68 | -3.46 | -22.28 | 101 |
| 30 | Keltner breakout · 1h | breakout | 81.58 | -18.42 | 110 | 23.6 | -20.96 | -4.35 | -25.10 | 174 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 81.57 | -18.43 | 2 | 0.0 | -9.91 | -1.15 | -24.16 | 1 |
| 32 | Stochastic reversion · 1h | reversion | 81.09 | -18.91 | 284 | 47.5 | -25.76 | -3.80 | -27.72 | 395 |
| 33 | Opening range 15m | breakout | 80.97 | -19.03 | 499 | 31.5 | -19.83 | -5.40 | -20.46 | 740 |
| 34 | Connors RSI(2) · 1h | reversion | 80.96 | -19.04 | 206 | 39.8 | -19.40 | -6.43 | -19.97 | 126 |
| 35 | Volume breakout · 1h | breakout | 80.20 | -19.80 | 147 | 27.2 | -15.42 | -3.59 | -22.08 | 93 |
| 36 | Max aggression: 5-day momentum | meta | 80.17 | -19.83 | 18 | 44.4 | -36.42 | -2.31 | -45.81 | 25 |
| 37 | Heikin-Ashi · 1h | trend | 78.90 | -21.10 | 416 | 24.5 | -40.18 | -7.47 | -42.50 | 664 |
| 38 | ADX DI cross · 1h | trend | 78.83 | -21.17 | 185 | 18.9 | -24.86 | -4.29 | -29.95 | 272 |
| 39 | CCI reversion · 1h | reversion | 77.26 | -22.74 | 326 | 45.1 | -25.41 | -3.84 | -30.69 | 453 |
| 40 | MFI reversion · 1h | reversion | 77.06 | -22.95 | 360 | 33.9 | -19.38 | -2.46 | -22.46 | 159 |
| 41 | Bollinger breakout · 1h | breakout | 76.87 | -23.13 | 171 | 22.8 | -21.33 | -4.40 | -27.99 | 236 |
| 42 | Ichimoku · 1h | trend | 75.37 | -24.63 | 100 | 15.0 | -31.53 | -8.91 | -31.64 | 121 |
| 43 | EMA 20/50 cross · 1h | trend | 75.07 | -24.93 | 102 | 10.8 | -26.12 | -4.59 | -36.42 | 118 |
| 44 | MACD cross · 1h | trend | 74.44 | -25.56 | 360 | 21.9 | -31.96 | -5.17 | -39.64 | 469 |
| 45 | Bollinger reversion · 1h | reversion | 74.13 | -25.87 | 278 | 40.3 | -26.92 | -4.14 | -32.54 | 370 |
| 46 | MACD zero-line · 1h | trend | 73.69 | -26.31 | 159 | 16.4 | -25.55 | -5.21 | -30.85 | 215 |
| 47 | Supertrend · 1h | trend | 73.22 | -26.78 | 168 | 13.1 | -32.76 | -5.96 | -36.07 | 232 |
| 48 | RSI momentum · 1h | momentum | 73.20 | -26.80 | 159 | 12.6 | -25.00 | -4.09 | -34.10 | 212 |
| 49 | Triple EMA stack · 1h | trend | 72.09 | -27.91 | 144 | 14.6 | -26.80 | -4.67 | -35.22 | 203 |
| 50 | Williams %R · 1h | reversion | 72.01 | -27.99 | 346 | 45.7 | -35.39 | -5.50 | -36.06 | 531 |
| 51 | OBV trend · 1h | momentum | 71.71 | -28.29 | 275 | 18.2 | -27.22 | -4.74 | -35.86 | 278 |
| 52 | ROC + volume · 1h | momentum | 70.92 | -29.08 | 362 | 26.5 | -35.88 | -6.82 | -38.44 | 378 |
| 53 | Donchian 20/10 · 1h | breakout | 70.80 | -29.20 | 142 | 19.7 | -30.03 | -5.56 | -35.64 | 205 |
| 54 | Daily: Momentum burst | daily | 70.63 | -29.37 | 27 | 11.1 | -38.39 | -5.46 | -39.29 | 34 |
| 55 | Z-score reversion · 1h ⏸ | reversion | 70.59 | -29.41 | 190 | 36.3 | -26.25 | -3.78 | -28.98 | 230 |
| 56 | Max aggression: 1-day momentum | meta | 67.05 | -32.95 | 27 | 25.9 | -30.90 | -1.53 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 66.65 | -33.35 | 170 | 30.6 | -25.56 | -3.46 | -32.54 | 242 |
| 58 | VWAP momentum · 1h | momentum | 66.22 | -33.78 | 838 | 22.0 | -53.84 | -11.47 | -54.89 | 1215 |
| 59 | Agent (ML meta-label) | meta | 65.42 | -34.58 | 1689 | 24.4 | -8.83 | -1.26 | -17.95 | 347 |
| 60 | EMA 9/21 cross · 1h | trend | 65.23 | -34.77 | 252 | 9.9 | -37.38 | -7.38 | -41.69 | 333 |
| 61 | Candlestick reversal · 1h | reversion | 63.76 | -36.24 | 445 | 27.9 | -38.50 | -6.98 | -40.05 | 593 |
| 62 | Three white soldiers | momentum | 61.00 | -39.00 | 506 | 14.8 | -48.85 | -22.59 | -48.99 | 653 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.60 | -98.96 | 5250 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -25.90 | -79.86 | 1414 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.23 | -44.67 | -93.24 | 2503 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.34 | -31.51 | -89.37 | 1922 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.68 | -38.46 | -90.70 | 2317 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -31.54 | -90.31 | 2196 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -51.74 | -97.78 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.20 | -54.15 | -96.21 | 3408 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.46 | -32.50 | -93.58 | 2362 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.37 | -33.85 | -82.42 | 1673 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -53.34 | -99.56 | 6022 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.19 | -41.89 | -92.21 | 2606 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.49 | -36.55 | -95.54 | 3433 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -69.60 | -99.81 | 6162 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.98 | -42.11 | -92.00 | 2256 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.11 | -24.15 | -75.34 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -58.39 | -97.73 | 3518 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.86 | -61.29 | -98.87 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.40 | -26.56 | -68.99 | 1222 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -51.72 | -94.57 | 2768 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -35.99 | -84.52 | 1774 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.64 | -69.97 | -99.65 | 6350 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.74 | -31.64 | -89.87 | 2293 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.51 | -20.18 | -78.77 | 1773 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.74 | -36.35 | -90.90 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.80 | -51.27 | -96.82 | 3858 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.44 | -54.76 | -89.51 | 2172 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.31 | -27.05 | -65.98 | 819 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.09 | -22.58 | -71.09 | 1258 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.11 | -19.43 | -80.31 | 1696 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.19 | -46.98 | -97.23 | 4294 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.07 | -99.93 | 8310 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T18:50 | Three white soldiers | buy | SOL-USD | 3.08 | — | rebalance up |
| 2026-11-10T18:50 | Three white soldiers | buy | ETH-USD | 3.06 | — | rebalance up |
| 2026-11-10T18:50 | Three white soldiers | buy | DOGE-USD | 3.05 | — | rebalance up |
| 2026-11-10T18:50 | Three white soldiers | sell | TNA | 12.20 | -0.02 | exit signal |
| 2026-11-10T18:45 | Agent (ML meta-label) | buy | AAPL | 10.88 | — | entry |
| 2026-11-10T18:45 | Agent (ML meta-label) | sell | TSLA | 10.85 | -0.02 | selected signal exited |
| 2026-11-10T18:45 | Agent (ML meta-label) | sell | SOXL | 2.26 | 0.00 | selected signal exited |
| 2026-11-10T18:41 | Three white soldiers | buy | SOL-USD | 3.05 | — | rebalance up |
| 2026-11-10T18:41 | Three white soldiers | sell | DOGE-USD | 3.05 | -0.01 | rebalance down |
| 2026-11-10T18:40 | Agent (ML meta-label) | buy | SOXL | 2.25 | — | entry |
| 2026-11-10T18:40 | Three white soldiers | buy | SOL-USD | 9.17 | — | entry signal |
| 2026-11-10T18:40 | Three white soldiers | buy | ETH-USD | 12.23 | — | entry signal |
| 2026-11-10T18:40 | Three white soldiers | sell | TNA | 3.07 | 0.00 | rebalance down |
| 2026-11-10T18:40 | Three white soldiers | sell | BTC-USD | 3.07 | -0.00 | rebalance down |
| 2026-11-10T18:35 | Agent (ML meta-label) | buy | TSLA | 10.87 | — | following Ichimoku |
| 2026-11-10T18:35 | Agent (ML meta-label) | buy | SPY | 10.87 | — | entry |
| 2026-11-10T18:35 | Agent (ML meta-label) | sell | GOOGL | 8.11 | -0.04 | selected signal exited |
| 2026-11-10T18:35 | Agent (ML meta-label) | sell | AAPL | 8.12 | -0.03 | selected signal exited |
| 2026-11-10T18:35 | Agent | buy | TSLA | 17.50 | — | following Ichimoku |
| 2026-11-10T18:35 | MFI reversion · 1h | buy | SPY | 3.87 | — | rebalance up |
| 2026-11-10T18:35 | MFI reversion · 1h | buy | ETHU | 7.04 | — | rebalance up |
| 2026-11-10T18:35 | MFI reversion · 1h | buy | AAPL | 3.90 | — | rebalance up |
| 2026-11-10T18:35 | MFI reversion · 1h | sell | AMZN | 15.30 | 0.15 | target is flat |
| 2026-11-10T18:35 | ADX DI cross · 1h | buy | TNA | 3.94 | — | rebalance up |
| 2026-11-10T18:35 | ADX DI cross · 1h | sell | AMD | 3.94 | 0.06 | rebalance down |
| 2026-11-10T18:34 | Copy: Insider buying | buy | KMI | 9.19 | — | entry |
| 2026-11-10T18:34 | Copy: Insider buying | sell | RAPP | 9.19 | 0.22 | target is flat |
| 2026-11-10T18:30 | Agent (ML meta-label) | buy | TECL | 5.49 | — | rebalance up |
| 2026-11-10T18:30 | Agent (ML meta-label) | sell | TSLA | 8.14 | 0.03 | selected signal exited |
| 2026-11-10T18:30 | Agent (ML meta-label) | sell | SOXL | 3.97 | 0.01 | selected signal exited |
| 2026-11-10T18:30 | Agent (ML meta-label) | sell | META | 6.89 | -0.04 | selected signal exited |
| 2026-11-10T18:30 | MFI reversion · 1h | buy | ETHU | 12.05 | — | entry signal |
| 2026-11-10T18:30 | MFI reversion · 1h | sell | SPY | 4.05 | 0.00 | rebalance down |
| 2026-11-10T18:30 | MFI reversion · 1h | sell | AMZN | 3.92 | 0.04 | rebalance down |
| 2026-11-10T18:30 | MFI reversion · 1h | sell | AAPL | 4.08 | -0.01 | rebalance down |
| 2026-11-10T18:30 | CCI reversion · 1h | buy | NVDA | 19.31 | — | entry signal |
| 2026-11-10T18:30 | Stochastic reversion · 1h | buy | NVDA | 8.93 | — | entry signal |
| 2026-11-10T18:30 | Stochastic reversion · 1h | buy | MSTR | 8.97 | — | entry signal |
| 2026-11-10T18:30 | Stochastic reversion · 1h | buy | BITX | 8.97 | — | entry signal |
| 2026-11-10T18:30 | Stochastic reversion · 1h | sell | SQQQ | 4.49 | 0.17 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 18:56:05.000129+00:00 -> 2026-11-10 19:06:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
