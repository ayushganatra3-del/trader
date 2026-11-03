# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T13:50:05.000122+00:00 · 46224 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.57 (-9.43%)

Closed trades 139, win rate 39.6%, fees £3.92, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 10320 decisions in 2064 calls, $0.1440 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T13:50 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-11-03T13:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T13:50 | 3 / 2 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| MACD zero-line | MSFT | 1.87 | +0.67% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.98 | 8.98 | 0 | — | 9.68 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.30 | -1.70 | 103 | 45.6 | -13.55 | -3.72 | -13.81 | 142 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.05 | -1.95 | 0 | — | 1.42 | 0.64 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.56 | -3.44 | 0 | — | -1.84 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.84 | 1.95 | -2.33 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.02 | 0.58 | -7.93 | 9 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -5.01 | -3.07 | -8.96 | 169 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.15 | -5.85 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.66 | 1.22 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.65 | -6.35 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Hold BTC | benchmark | 91.36 | -8.64 | 0 | — | 0.15 | 0.20 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.97 | -9.03 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Squeeze breakout · 1h | breakout | 89.55 | -10.45 | 61 | 23.0 | -7.77 | -2.58 | -13.68 | 89 |
| 24 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 25 | Donchian 55/20 · 1h | breakout | 89.45 | -10.55 | 60 | 13.3 | -13.66 | -3.06 | -18.06 | 100 |
| 26 | Parabolic SAR · 1h | trend | 88.99 | -11.01 | 149 | 26.8 | -14.14 | -3.30 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.75 | -11.25 | 14 | 21.4 | -5.97 | -0.73 | -14.73 | 15 |
| 28 | Copy: Insider buying | copy | 88.61 | -11.39 | 35 | 37.1 | -22.60 | -4.63 | -23.13 | 61 |
| 29 | Max aggression: 5-day momentum | meta | 87.08 | -12.92 | 15 | 40.0 | -27.68 | -1.78 | -36.71 | 25 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.11 | -14.89 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.81 | -15.19 | 129 | 28.7 | -17.52 | -3.92 | -18.97 | 99 |
| 33 | Keltner breakout · 1h | breakout | 84.79 | -15.21 | 89 | 23.6 | -21.34 | -4.21 | -24.03 | 173 |
| 34 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.76 | -16.24 | 148 | 18.2 | -19.87 | -3.73 | -22.16 | 252 |
| 36 | Stochastic reversion · 1h | reversion | 83.02 | -16.98 | 235 | 46.4 | -25.67 | -5.39 | -25.93 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.88 | -17.12 | 299 | 32.8 | -16.65 | -2.69 | -18.26 | 149 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 81.94 | -18.06 | 83 | 13.3 | -18.16 | -3.67 | -25.58 | 120 |
| 40 | Bollinger breakout · 1h | breakout | 81.60 | -18.40 | 140 | 25.0 | -16.92 | -3.28 | -23.31 | 238 |
| 41 | EMA 20/50 cross · 1h | trend | 79.29 | -20.71 | 90 | 11.1 | -21.71 | -4.05 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 78.46 | -21.54 | 268 | 44.8 | -27.64 | -4.41 | -28.59 | 445 |
| 43 | MACD zero-line · 1h | trend | 78.12 | -21.88 | 136 | 15.4 | -25.32 | -5.44 | -27.76 | 209 |
| 44 | Supertrend · 1h | trend | 77.68 | -22.32 | 141 | 12.8 | -28.20 | -5.42 | -29.64 | 220 |
| 45 | Triple EMA stack · 1h | trend | 77.23 | -22.77 | 125 | 14.4 | -28.09 | -5.15 | -30.89 | 204 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.46 | -3.77 | -33.56 | 33 |
| 47 | Heikin-Ashi · 1h | trend | 76.96 | -23.04 | 356 | 22.5 | -40.17 | -8.54 | -43.18 | 663 |
| 48 | MACD cross · 1h | trend | 76.91 | -23.09 | 299 | 23.4 | -32.91 | -6.51 | -35.32 | 473 |
| 49 | RSI momentum · 1h | momentum | 76.85 | -23.15 | 135 | 12.6 | -29.04 | -5.56 | -30.84 | 213 |
| 50 | OBV trend · 1h | momentum | 76.46 | -23.54 | 239 | 17.6 | -30.37 | -6.41 | -33.09 | 297 |
| 51 | Bollinger reversion · 1h | reversion | 76.30 | -23.70 | 219 | 37.9 | -31.29 | -6.50 | -31.58 | 375 |
| 52 | Williams %R · 1h | reversion | 76.11 | -23.89 | 272 | 46.0 | -36.47 | -6.61 | -36.78 | 517 |
| 53 | Donchian 20/10 · 1h | breakout | 76.09 | -23.91 | 119 | 20.2 | -27.09 | -4.72 | -31.02 | 208 |
| 54 | Z-score reversion · 1h | reversion | 74.98 | -25.02 | 140 | 34.3 | -17.04 | -2.62 | -23.02 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.88 | -25.12 | 299 | 25.4 | -31.79 | -5.94 | -34.50 | 371 |
| 56 | RSI(14) reversion · 1h | reversion | 70.82 | -29.18 | 128 | 25.8 | -21.24 | -3.81 | -26.28 | 193 |
| 57 | Three white soldiers | momentum | 69.94 | -30.06 | 409 | 16.1 | -45.70 | -21.28 | -45.70 | 611 |
| 58 | EMA 9/21 cross · 1h | trend | 69.47 | -30.53 | 218 | 9.6 | -37.02 | -7.45 | -39.06 | 325 |
| 59 | Candlestick reversal · 1h | reversion | 69.27 | -30.73 | 350 | 28.6 | -38.23 | -7.87 | -38.59 | 547 |
| 60 | VWAP momentum · 1h | momentum | 69.08 | -30.92 | 697 | 21.5 | -52.41 | -10.41 | -55.45 | 1219 |
| 61 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -34.94 | -2.07 | -50.32 | 41 |
| 62 | Agent (ML meta-label) | meta | 68.36 | -31.64 | 1302 | 20.4 | -14.22 | -2.96 | -16.20 | 273 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.51 | -98.96 | 5181 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.64 | -24.03 | -80.27 | 1403 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -46.04 | -93.50 | 2511 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -31.16 | -89.04 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -38.19 | -91.32 | 2323 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.67 | -31.83 | -90.71 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -53.00 | -97.78 | 3477 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -61.16 | -96.28 | 3382 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.26 | -34.17 | -93.37 | 2396 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.63 | -34.30 | -81.76 | 1680 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -52.16 | -99.48 | 5867 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.05 | -44.73 | -93.05 | 2613 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.07 | -95.47 | 3369 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.01 | -99.80 | 6181 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.94 | -45.21 | -91.95 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.88 | -26.72 | -74.88 | 1559 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -61.83 | -97.77 | 3548 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.28 | -98.66 | 4820 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.32 | -28.36 | -70.00 | 1202 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.75 | -55.26 | -94.77 | 2774 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.65 | -36.97 | -84.71 | 1802 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.44 | -99.61 | 6303 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.83 | -88.14 | 2227 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.57 | -19.13 | -76.66 | 1689 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -35.57 | -90.33 | 2233 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -49.55 | -96.45 | 3816 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -52.89 | -89.30 | 2118 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.34 | -25.20 | -65.43 | 820 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.50 | -24.92 | -74.05 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.81 | -18.63 | -77.17 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.80 | -96.80 | 4236 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.48 | -99.92 | 8222 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T13:00 | CCI reversion · 1h | sell | SOL-USD | 19.55 | 0.03 | exit signal |
| 2026-11-03T13:00 | CCI reversion · 1h | sell | BTC-USD | 19.62 | -0.01 | exit signal |
| 2026-11-03T13:00 | Williams %R · 1h | sell | DOGE-USD | 15.25 | 0.04 | exit signal |
| 2026-11-03T13:00 | Z-score reversion · 1h | buy | BTC-USD | 8.81 | — | entry |
| 2026-11-03T13:00 | Z-score reversion · 1h | sell | DOGE-USD | 8.81 | 0.04 | exit signal |
| 2026-11-03T13:00 | Candlestick reversal · 1h | sell | SOL-USD | 6.91 | 0.01 | exit signal |
| 2026-11-03T13:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.77 | 0.09 | exit signal |
| 2026-11-03T13:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.69 | 0.02 | exit signal |
| 2026-11-03T13:00 | Volume breakout · 1h | buy | XRP-USD | 21.19 | — | entry signal |
| 2026-11-03T13:00 | Squeeze breakout · 1h | buy | XRP-USD | 22.37 | — | entry signal |
| 2026-11-03T13:00 | Squeeze breakout · 1h | buy | ETH-USD | 22.37 | — | entry signal |
| 2026-11-03T13:00 | Keltner breakout · 1h | buy | XRP-USD | 21.19 | — | entry signal |
| 2026-11-03T13:00 | Bollinger breakout · 1h | buy | XRP-USD | 16.32 | — | entry signal |
| 2026-11-03T13:00 | Bollinger breakout · 1h | buy | SOL-USD | 16.32 | — | entry signal |
| 2026-11-03T13:00 | Bollinger breakout · 1h | buy | ETH-USD | 16.32 | — | entry signal |
| 2026-11-03T13:00 | Bollinger breakout · 1h | buy | DOGE-USD | 16.32 | — | entry signal |
| 2026-11-03T13:00 | Bollinger breakout · 1h | buy | BTC-USD | 16.32 | — | entry signal |
| 2026-11-03T13:00 | Donchian 55/20 · 1h | buy | XRP-USD | 22.35 | — | entry signal |
| 2026-11-03T13:00 | Donchian 20/10 · 1h | buy | XRP-USD | 18.57 | — | entry signal |
| 2026-11-03T13:00 | Donchian 20/10 · 1h | buy | ETH-USD | 19.01 | — | entry signal |
| 2026-11-03T13:00 | RSI momentum · 1h | buy | ETH-USD | 9.71 | — | entry signal |
| 2026-11-03T13:00 | RSI momentum · 1h | buy | DOGE-USD | 12.81 | — | entry signal |
| 2026-11-03T13:00 | ROC + volume · 1h | buy | XRP-USD | 18.37 | — | entry signal |
| 2026-11-03T13:00 | ADX DI cross · 1h | buy | SOL-USD | 20.94 | — | entry signal |
| 2026-11-03T13:00 | ADX DI cross · 1h | buy | BTC-USD | 20.94 | — | entry signal |
| 2026-11-03T13:00 | Supertrend · 1h | buy | XRP-USD | 8.63 | — | entry signal |
| 2026-11-03T13:00 | Triple EMA stack · 1h | buy | XRP-USD | 19.30 | — | entry signal |
| 2026-11-03T13:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 6.71 | — | entry signal |
| 2026-11-03T13:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 3.72 | 0.06 | rebalance down |
| 2026-11-03T12:25 | Candlestick reversal · 1h | sell | XRP-USD | 7.83 | 0.15 | take-profit |
| 2026-11-03T12:25 | Parabolic SAR · 1h | buy | XRP-USD | 4.47 | — | rebalance up |
| 2026-11-03T12:25 | Parabolic SAR · 1h | sell | ETH-USD | 4.47 | 0.00 | rebalance down |
| 2026-11-03T12:00 | CCI reversion · 1h | buy | SOL-USD | 6.53 | — | rebalance up |
| 2026-11-03T12:00 | CCI reversion · 1h | buy | BTC-USD | 6.56 | — | rebalance up |
| 2026-11-03T12:00 | CCI reversion · 1h | sell | DOGE-USD | 13.09 | -0.03 | exit signal |
| 2026-11-03T12:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.66 | -0.01 | exit signal |
| 2026-11-03T12:00 | OBV trend · 1h | buy | XRP-USD | 19.01 | — | entry signal |
| 2026-11-03T12:00 | Heikin-Ashi · 1h | buy | SOL-USD | 6.00 | — | entry signal |
| 2026-11-03T12:00 | Heikin-Ashi · 1h | buy | DOGE-USD | 12.73 | — | entry signal |
| 2026-11-03T12:00 | Heikin-Ashi · 1h | buy | BTC-USD | 12.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 13:50:05.000122+00:00 -> 2026-11-03 14:00:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 13:50:05.000122+00:00 -> 2026-11-03 14:00:05.000122+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 13:50:05.000122+00:00 -> 2026-11-03 14:00:05.000122+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
