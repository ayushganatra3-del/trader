# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-10T15:30:05.000130+00:00 · 54724 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £87.00 (-13.00%)

Closed trades 163, win rate 35.0%, fees £5.00, max drawdown -13.61%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| SQQQ | 17.56 | +0.20 |

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

Today: 14408 decisions in 2320 calls, $0.1939 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-10T15:30 | 2 / 12 / 16 | cash |  |
| Breezy | 2026-11-10T15:30 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-10T15:30 | 1 / 26 / 3 | cash |  |

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
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 113.59 | 13.59 | 31 | 29.0 | 22.88 | 3.37 | -8.66 | 44 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 113.39 | 13.39 | 0 | — | 13.83 | 4.67 | -5.18 | 1 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.97 | 3.97 | 31 | 45.2 | 3.85 | 1.00 | -9.64 | 30 |
| 5 | Day trade: Stocks in Play ORB | daytrade | 100.62 | 0.62 | 130 | 35.4 | 8.42 | 3.15 | -2.67 | 90 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.62 | 0.62 | 0 | — | 3.78 | 1.11 | -6.60 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.81 | -1.19 | 8 | 50.0 | -3.34 | -0.06 | -18.69 | 8 |
| 10 | Agent (rotation) | meta | 98.75 | -1.25 | 178 | 28.7 | -1.81 | -0.69 | -9.49 | 151 |
| 11 | Gap and go | momentum | 98.57 | -1.43 | 183 | 30.6 | 3.52 | 1.06 | -9.06 | 238 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 13 | Hold SPY | benchmark | 96.49 | -3.51 | 0 | — | -1.71 | -0.53 | -6.18 | 1 |
| 14 | VWAP reversion · 1h | reversion | 96.05 | -3.95 | 134 | 47.0 | -13.12 | -3.36 | -13.15 | 150 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 94.48 | -5.52 | 0 | — | -3.57 | -0.89 | -9.25 | 1 |
| 16 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.80 | -3.52 | -5.99 | 28 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 93.19 | -6.81 | 22 | 18.2 | -8.20 | -6.72 | -8.67 | 22 |
| 18 | Trend pullback · 1h | trend | 92.98 | -7.02 | 108 | 23.1 | -13.61 | -5.06 | -18.02 | 79 |
| 19 | Copy: Congress Democrats (NANC) | copy | 92.85 | -7.15 | 0 | — | -4.27 | -1.13 | -10.64 | 1 |
| 20 | Copy: Insider buying | copy | 92.11 | -7.89 | 42 | 38.1 | -8.44 | -1.75 | -15.11 | 67 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Opening range 30m | breakout | 89.48 | -10.52 | 395 | 33.9 | -13.83 | -4.36 | -14.62 | 603 |
| 23 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -8.11 | -2.80 | -14.15 | 79 |
| 24 | Agent | meta | 87.00 | -13.00 | 163 | 35.0 | -13.85 | -7.16 | -14.28 | 202 |
| 25 | Daily: Bullish score | daily | 86.49 | -13.51 | 15 | 20.0 | -7.78 | -1.15 | -17.42 | 14 |
| 26 | Hold BTC | benchmark | 86.33 | -13.67 | 1 | 0.0 | -6.45 | -0.86 | -15.65 | 1 |
| 27 | Parabolic SAR · 1h | trend | 85.73 | -14.27 | 167 | 26.9 | -12.95 | -2.62 | -21.13 | 224 |
| 28 | Agent (aggressive) | meta | 84.37 | -15.63 | 76 | 31.6 | -16.47 | -4.68 | -18.51 | 95 |
| 29 | Opening range 15m | breakout | 84.02 | -15.98 | 484 | 32.2 | -16.42 | -4.63 | -19.09 | 737 |
| 30 | Donchian 55/20 · 1h | breakout | 83.85 | -16.15 | 71 | 14.1 | -17.14 | -3.71 | -22.37 | 103 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 83.37 | -16.63 | 2 | 0.0 | -7.82 | -0.87 | -24.16 | 1 |
| 32 | Max aggression: 5-day momentum | meta | 82.85 | -17.15 | 18 | 44.4 | -34.09 | -2.04 | -45.81 | 25 |
| 33 | Keltner breakout · 1h | breakout | 82.52 | -17.48 | 109 | 22.9 | -21.55 | -4.40 | -25.32 | 180 |
| 34 | Volume breakout · 1h | breakout | 81.31 | -18.69 | 146 | 27.4 | -14.86 | -3.35 | -21.11 | 96 |
| 35 | Stochastic reversion · 1h | reversion | 81.15 | -18.85 | 280 | 48.2 | -25.08 | -3.70 | -27.21 | 389 |
| 36 | Connors RSI(2) · 1h | reversion | 80.86 | -19.14 | 206 | 39.8 | -19.47 | -6.46 | -19.99 | 125 |
| 37 | Heikin-Ashi · 1h | trend | 79.72 | -20.28 | 415 | 24.3 | -39.99 | -7.45 | -42.96 | 675 |
| 38 | ADX DI cross · 1h | trend | 79.51 | -20.49 | 181 | 19.3 | -22.43 | -3.76 | -29.07 | 271 |
| 39 | MFI reversion · 1h | reversion | 78.30 | -21.70 | 355 | 34.1 | -17.58 | -2.25 | -21.69 | 158 |
| 40 | CCI reversion · 1h | reversion | 77.19 | -22.82 | 324 | 45.4 | -25.37 | -3.86 | -30.29 | 457 |
| 41 | Bollinger breakout · 1h | breakout | 77.02 | -22.98 | 170 | 22.9 | -22.47 | -4.61 | -27.92 | 241 |
| 42 | Ichimoku · 1h | trend | 76.18 | -23.82 | 98 | 15.3 | -30.77 | -8.78 | -30.96 | 120 |
| 43 | MACD cross · 1h | trend | 75.20 | -24.80 | 355 | 22.3 | -32.78 | -5.35 | -39.51 | 483 |
| 44 | MACD zero-line · 1h | trend | 74.74 | -25.26 | 157 | 16.6 | -24.91 | -4.98 | -30.11 | 215 |
| 45 | EMA 20/50 cross · 1h | trend | 74.54 | -25.46 | 102 | 10.8 | -23.38 | -4.08 | -32.57 | 124 |
| 46 | Bollinger reversion · 1h | reversion | 74.28 | -25.72 | 274 | 40.9 | -25.43 | -3.88 | -32.06 | 372 |
| 47 | Z-score reversion · 1h | reversion | 73.99 | -26.01 | 182 | 36.8 | -23.48 | -3.41 | -27.66 | 228 |
| 48 | RSI momentum · 1h | momentum | 73.60 | -26.40 | 159 | 12.6 | -23.89 | -4.02 | -33.05 | 210 |
| 49 | Supertrend · 1h | trend | 73.47 | -26.53 | 167 | 13.2 | -32.45 | -5.88 | -35.24 | 233 |
| 50 | Williams %R · 1h | reversion | 73.05 | -26.95 | 340 | 46.5 | -34.18 | -5.36 | -35.76 | 529 |
| 51 | Triple EMA stack · 1h | trend | 72.46 | -27.54 | 143 | 14.7 | -26.47 | -4.55 | -35.42 | 190 |
| 52 | OBV trend · 1h | momentum | 72.22 | -27.78 | 274 | 18.2 | -27.07 | -4.78 | -35.55 | 277 |
| 53 | Daily: Momentum burst | daily | 72.10 | -27.90 | 27 | 11.1 | -36.73 | -5.09 | -39.18 | 34 |
| 54 | ROC + volume · 1h | momentum | 71.81 | -28.19 | 358 | 26.8 | -36.70 | -6.88 | -39.38 | 384 |
| 55 | Donchian 20/10 · 1h | breakout | 71.47 | -28.54 | 142 | 19.7 | -30.73 | -5.56 | -35.64 | 210 |
| 56 | Max aggression: 1-day momentum | meta | 69.56 | -30.44 | 27 | 25.9 | -28.09 | -1.31 | -57.50 | 41 |
| 57 | RSI(14) reversion · 1h | reversion | 67.87 | -32.13 | 166 | 31.3 | -26.38 | -3.85 | -32.51 | 227 |
| 58 | Agent (ML meta-label) | meta | 67.09 | -32.91 | 1650 | 24.2 | -7.02 | -0.91 | -19.70 | 348 |
| 59 | VWAP momentum · 1h | momentum | 66.93 | -33.07 | 828 | 22.0 | -52.47 | -11.18 | -54.01 | 1238 |
| 60 | EMA 9/21 cross · 1h | trend | 65.72 | -34.28 | 249 | 9.6 | -37.55 | -7.43 | -40.79 | 336 |
| 61 | Candlestick reversal · 1h | reversion | 63.36 | -36.64 | 443 | 28.0 | -38.03 | -6.97 | -39.34 | 586 |
| 62 | Three white soldiers | momentum | 61.32 | -38.68 | 501 | 15.0 | -48.88 | -22.89 | -48.92 | 648 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -44.68 | -98.94 | 5286 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.80 | -25.89 | -79.80 | 1417 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.19 | -44.54 | -93.20 | 2500 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.15 | -31.65 | -89.18 | 1917 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -38.33 | -90.61 | 2312 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.12 | -31.19 | -90.18 | 2201 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -53.14 | -97.75 | 3450 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -53.44 | -96.21 | 3423 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.75 | -32.62 | -93.85 | 2414 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.20 | -33.71 | -82.20 | 1673 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.55 | -54.70 | -99.55 | 5982 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.20 | -42.34 | -92.20 | 2600 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.48 | -36.24 | -95.50 | 3408 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -72.49 | -99.81 | 6153 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.01 | -42.60 | -92.01 | 2254 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -75.25 | -24.15 | -75.28 | 1593 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -57.88 | -97.70 | 3517 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.87 | -62.84 | -98.88 | 4892 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.46 | -26.67 | -68.99 | 1216 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.56 | -52.70 | -94.56 | 2757 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.41 | -36.10 | -84.42 | 1774 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.65 | -71.84 | -99.65 | 6349 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -89.92 | -32.62 | -89.94 | 2296 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.32 | -20.05 | -78.38 | 1754 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.89 | -37.67 | -90.89 | 2209 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.81 | -52.37 | -96.84 | 3887 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.38 | -57.47 | -89.38 | 2156 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.26 | -27.00 | -66.01 | 814 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -70.75 | -22.33 | -71.15 | 1260 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.16 | -19.48 | -80.23 | 1691 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.25 | -48.70 | -97.27 | 4292 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -106.35 | -99.93 | 8318 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-10T15:30 | Agent (ML meta-label) | buy | TSLA | 7.46 | — | following Ichimoku |
| 2026-11-10T15:30 | Agent (ML meta-label) | buy | TECL | 7.46 | — | entry |
| 2026-11-10T15:30 | Agent (ML meta-label) | buy | SPY | 7.46 | — | entry |
| 2026-11-10T15:30 | Agent (ML meta-label) | sell | TNA | 6.48 | 0.53 | selected signal exited |
| 2026-11-10T15:30 | Agent (ML meta-label) | sell | LABU | 5.11 | -0.12 | selected signal exited |
| 2026-11-10T15:30 | CCI reversion · 1h | buy | SQQQ | 19.30 | — | entry signal |
| 2026-11-10T15:30 | VWAP reversion · 1h | sell | XRP-USD | 23.66 | -0.63 | stop-loss |
| 2026-11-10T15:30 | Bollinger reversion · 1h | buy | ETH-USD | 7.62 | — | rebalance up |
| 2026-11-10T15:30 | Bollinger reversion · 1h | sell | XRP-USD | 18.42 | -0.41 | stop-loss |
| 2026-11-10T15:30 | Connors RSI(2) · 1h | buy | AAPL | 20.22 | — | entry signal |
| 2026-11-10T15:30 | Connors RSI(2) · 1h | sell | SQQQ | 20.09 | -0.18 | exit signal |
| 2026-11-10T15:30 | Volume breakout · 1h | buy | AMD | 20.33 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | UPRO | 5.51 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | TSLA | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | TQQQ | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | TNA | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | MSFT | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | LABU | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | IWM | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | GOOGL | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | AMZN | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | buy | AMD | 5.53 | — | entry signal |
| 2026-11-10T15:30 | ROC + volume · 1h | sell | SOXL | 12.04 | 0.08 | rebalance down |
| 2026-11-10T15:30 | ROC + volume · 1h | sell | QQQ | 12.53 | -0.03 | rebalance down |
| 2026-11-10T15:30 | ROC + volume · 1h | sell | AAPL | 12.55 | -0.08 | rebalance down |
| 2026-11-10T15:30 | VWAP momentum · 1h | buy | QQQ | 3.72 | — | rebalance up |
| 2026-11-10T15:30 | VWAP momentum · 1h | buy | META | 6.09 | — | entry signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | buy | GOOGL | 6.09 | — | entry signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | buy | AMZN | 6.09 | — | entry signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | UPRO | 1.82 | 0.00 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | TNA | 3.07 | 0.19 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | SPY | 3.07 | 0.01 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | PLTR | 3.06 | -0.01 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | NVDA | 3.13 | -0.11 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | LABU | 3.14 | 0.22 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | IWM | 3.07 | 0.06 | exit signal |
| 2026-11-10T15:30 | VWAP momentum · 1h | sell | AAPL | 4.18 | -0.04 | exit signal |
| 2026-11-10T15:30 | Heikin-Ashi · 1h | buy | AMD | 15.68 | — | rebalance up |
| 2026-11-10T15:30 | Heikin-Ashi · 1h | sell | UPRO | 3.89 | -0.01 | exit signal |
| 2026-11-10T15:30 | Heikin-Ashi · 1h | sell | TSLA | 3.97 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-12 15:30:05.000130+00:00 -> 2026-11-10 15:40:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
