# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T13:20:05.000140+00:00 · 46204 ticks

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

Today: 10020 decisions in 2004 calls, $0.1398 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T13:20 | 2 / 1 / 2 | cash |  |
| Breezy | 2026-11-03T13:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T13:20 | 2 / 3 / 0 | ETH-USD 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| VWAP reversion | COIN | 1.90 | +3.41% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.09 | 9.09 | 0 | — | 9.79 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.30 | -1.70 | 103 | 45.6 | -13.20 | -3.64 | -13.45 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.06 | -1.94 | 0 | — | 1.41 | 0.63 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.57 | -3.43 | 0 | — | -1.85 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.49 | 1.76 | -2.66 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -5.42 | -3.60 | -8.93 | 168 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.16 | -5.84 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.75 | 1.25 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.66 | -6.34 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Hold BTC | benchmark | 91.19 | -8.81 | 0 | — | -0.24 | 0.13 | -12.65 | 1 |
| 21 | Trend pullback · 1h | trend | 90.97 | -9.03 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 22 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.30 | -10.70 | 61 | 23.0 | -9.04 | -3.10 | -13.62 | 90 |
| 25 | Donchian 55/20 · 1h | breakout | 89.30 | -10.70 | 60 | 13.3 | -13.81 | -3.10 | -18.06 | 100 |
| 26 | Parabolic SAR · 1h | trend | 88.86 | -11.14 | 149 | 26.8 | -14.34 | -3.36 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.75 | -11.25 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 28 | Copy: Insider buying | copy | 88.62 | -11.38 | 35 | 37.1 | -22.54 | -4.61 | -23.08 | 59 |
| 29 | Max aggression: 5-day momentum | meta | 87.09 | -12.91 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.12 | -14.88 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.67 | -15.33 | 129 | 28.7 | -17.66 | -3.96 | -18.94 | 99 |
| 33 | Keltner breakout · 1h | breakout | 84.65 | -15.35 | 89 | 23.6 | -23.24 | -4.67 | -24.47 | 173 |
| 34 | Connors RSI(2) · 1h | reversion | 84.20 | -15.80 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.55 | -16.45 | 148 | 18.2 | -20.08 | -3.77 | -22.16 | 252 |
| 36 | Stochastic reversion · 1h | reversion | 83.03 | -16.97 | 235 | 46.4 | -25.69 | -5.39 | -25.95 | 390 |
| 37 | MFI reversion · 1h | reversion | 82.73 | -17.27 | 299 | 32.8 | -16.80 | -2.72 | -18.26 | 149 |
| 38 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 39 | Ichimoku · 1h | trend | 81.94 | -18.06 | 83 | 13.3 | -18.16 | -3.67 | -25.58 | 120 |
| 40 | Bollinger breakout · 1h | breakout | 81.25 | -18.75 | 140 | 25.0 | -17.35 | -3.36 | -23.19 | 238 |
| 41 | EMA 20/50 cross · 1h | trend | 79.16 | -20.84 | 90 | 11.1 | -21.84 | -4.09 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 78.47 | -21.53 | 268 | 44.8 | -27.64 | -4.41 | -28.59 | 445 |
| 43 | MACD zero-line · 1h | trend | 77.98 | -22.02 | 136 | 15.4 | -25.45 | -5.48 | -27.76 | 209 |
| 44 | Supertrend · 1h | trend | 77.63 | -22.37 | 141 | 12.8 | -28.25 | -5.43 | -29.62 | 220 |
| 45 | Triple EMA stack · 1h | trend | 77.11 | -22.89 | 125 | 14.4 | -28.21 | -5.18 | -30.89 | 204 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.92 | -23.08 | 299 | 23.4 | -33.08 | -6.56 | -35.32 | 473 |
| 48 | RSI momentum · 1h | momentum | 76.77 | -23.23 | 135 | 12.6 | -29.23 | -5.61 | -30.86 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 76.72 | -23.28 | 356 | 22.5 | -40.38 | -8.62 | -43.18 | 663 |
| 50 | OBV trend · 1h | momentum | 76.33 | -23.67 | 239 | 17.6 | -30.71 | -6.51 | -33.25 | 297 |
| 51 | Bollinger reversion · 1h | reversion | 76.30 | -23.70 | 219 | 37.9 | -31.29 | -6.50 | -31.58 | 375 |
| 52 | Williams %R · 1h | reversion | 76.11 | -23.89 | 272 | 46.0 | -36.47 | -6.61 | -36.79 | 517 |
| 53 | Donchian 20/10 · 1h | breakout | 75.88 | -24.12 | 119 | 20.2 | -27.30 | -4.77 | -31.02 | 208 |
| 54 | Z-score reversion · 1h | reversion | 74.97 | -25.03 | 140 | 34.3 | -17.12 | -2.64 | -23.02 | 211 |
| 55 | ROC + volume · 1h | momentum | 74.76 | -25.24 | 299 | 25.4 | -31.75 | -5.94 | -34.35 | 371 |
| 56 | RSI(14) reversion · 1h | reversion | 70.83 | -29.17 | 128 | 25.8 | -21.31 | -3.83 | -26.28 | 193 |
| 57 | Three white soldiers | momentum | 69.94 | -30.06 | 409 | 16.1 | -45.70 | -21.31 | -45.70 | 611 |
| 58 | EMA 9/21 cross · 1h | trend | 69.35 | -30.65 | 218 | 9.6 | -37.16 | -7.49 | -39.06 | 325 |
| 59 | Candlestick reversal · 1h | reversion | 69.27 | -30.73 | 350 | 28.6 | -38.21 | -7.86 | -38.57 | 548 |
| 60 | VWAP momentum · 1h | momentum | 68.87 | -31.13 | 697 | 21.5 | -52.62 | -10.48 | -55.49 | 1220 |
| 61 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 62 | Agent (ML meta-label) | meta | 68.36 | -31.64 | 1302 | 20.4 | -9.76 | -1.69 | -15.14 | 289 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.78 | -98.97 | 5184 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.64 | -24.00 | -80.27 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -46.85 | -93.56 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.92 | -31.28 | -89.06 | 1902 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -38.18 | -91.30 | 2321 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.64 | -31.73 | -90.72 | 2223 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -53.25 | -97.78 | 3476 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.25 | -61.52 | -96.28 | 3380 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.28 | -34.19 | -93.39 | 2400 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.67 | -34.43 | -81.76 | 1680 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.99 | -99.48 | 5866 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.02 | -44.58 | -93.04 | 2611 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.46 | -37.08 | -95.46 | 3369 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -73.21 | -99.80 | 6180 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.95 | -45.27 | -91.95 | 2276 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.74 | -26.64 | -74.75 | 1558 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -61.83 | -97.76 | 3548 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -59.49 | -98.66 | 4822 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.41 | -28.47 | -70.00 | 1203 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -55.11 | -94.75 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.68 | -37.14 | -84.71 | 1801 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.48 | -99.61 | 6303 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.83 | -88.14 | 2227 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.55 | -19.10 | -76.65 | 1688 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.24 | -35.59 | -90.32 | 2231 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.44 | -49.62 | -96.45 | 3817 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -53.65 | -89.35 | 2121 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.14 | -25.09 | -65.24 | 816 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.62 | -25.11 | -74.05 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.63 | -18.57 | -77.03 | 1597 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.79 | -48.80 | -96.80 | 4236 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.17 | -99.92 | 8222 |
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

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 13:20:05.000140+00:00 -> 2026-11-03 13:30:05.000140+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 13:20:05.000140+00:00 -> 2026-11-03 13:30:05.000140+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 13:20:05.000140+00:00 -> 2026-11-03 13:30:05.000140+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
