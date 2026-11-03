# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T06:20:05.000184+00:00 · 45845 ticks

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

Today: 4635 decisions in 927 calls, $0.0648 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T06:20 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-03T06:20 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-03T06:20 | 1 / 3 / 1 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.12 | 9.12 | 0 | — | 9.79 | 4.21 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 8.19 | 2.53 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.14 | 3.14 | 25 | 48.0 | 2.88 | 1.12 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 98.31 | -1.69 | 103 | 45.6 | -13.20 | -3.64 | -13.45 | 143 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.08 | -1.92 | 0 | — | 1.41 | 0.63 | -5.02 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 10 | Hold SPY | benchmark | 96.60 | -3.40 | 0 | — | -1.85 | -0.95 | -3.94 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.47 | -3.52 | 104 | 34.6 | 3.49 | 1.76 | -2.66 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.07 | 0.60 | -7.93 | 7 |
| 14 | Agent (rotation) | meta | 94.94 | -5.05 | 144 | 30.6 | -4.95 | -3.04 | -8.93 | 159 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 94.19 | -5.82 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 17 | Gap and go | momentum | 94.01 | -5.99 | 137 | 28.5 | 3.75 | 1.25 | -8.76 | 214 |
| 18 | Copy: Congress Democrats (NANC) | copy | 93.68 | -6.32 | 0 | — | -2.94 | -1.09 | -7.64 | 1 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 20 | Trend pullback · 1h | trend | 90.97 | -9.03 | 101 | 21.8 | -16.63 | -6.16 | -17.67 | 80 |
| 21 | Agent | meta | 90.57 | -9.43 | 139 | 39.6 | -10.50 | -6.35 | -12.20 | 209 |
| 22 | Hold BTC | benchmark | 90.17 | -9.83 | 0 | — | -1.88 | -0.13 | -12.65 | 1 |
| 23 | Opening range 30m | breakout | 89.54 | -10.46 | 334 | 33.2 | -13.07 | -4.01 | -17.21 | 578 |
| 24 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -7.27 | -2.37 | -13.40 | 87 |
| 25 | Donchian 55/20 · 1h | breakout | 89.42 | -10.58 | 60 | 13.3 | -13.71 | -3.07 | -18.06 | 99 |
| 26 | Parabolic SAR · 1h | trend | 88.77 | -11.23 | 149 | 26.8 | -16.02 | -3.77 | -17.40 | 241 |
| 27 | Daily: Bullish score | daily | 88.76 | -11.24 | 14 | 21.4 | -5.96 | -0.72 | -14.73 | 14 |
| 28 | Copy: Insider buying | copy | 88.64 | -11.36 | 35 | 37.1 | -22.54 | -4.61 | -23.08 | 59 |
| 29 | Max aggression: 5-day momentum | meta | 87.11 | -12.89 | 15 | 40.0 | -30.82 | -2.05 | -37.35 | 26 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.14 | -14.86 | 1 | 0.0 | -5.53 | -0.72 | -16.59 | 1 |
| 32 | Volume breakout · 1h | breakout | 84.77 | -15.22 | 129 | 28.7 | -17.56 | -3.93 | -18.81 | 98 |
| 33 | Keltner breakout · 1h | breakout | 84.76 | -15.24 | 89 | 23.6 | -20.10 | -3.83 | -24.07 | 172 |
| 34 | Connors RSI(2) · 1h | reversion | 84.21 | -15.79 | 191 | 40.8 | -20.81 | -6.65 | -21.57 | 139 |
| 35 | ADX DI cross · 1h | trend | 83.65 | -16.35 | 148 | 18.2 | -20.00 | -3.76 | -22.16 | 249 |
| 36 | Stochastic reversion · 1h | reversion | 82.97 | -17.03 | 232 | 46.6 | -25.75 | -5.41 | -25.93 | 390 |
| 37 | Opening range 15m | breakout | 82.17 | -17.83 | 408 | 30.4 | -18.70 | -5.47 | -20.73 | 708 |
| 38 | MFI reversion · 1h | reversion | 82.15 | -17.85 | 299 | 32.8 | -17.37 | -2.83 | -18.26 | 148 |
| 39 | Ichimoku · 1h | trend | 82.00 | -18.00 | 82 | 13.4 | -18.13 | -3.66 | -25.58 | 120 |
| 40 | Bollinger breakout · 1h | breakout | 81.61 | -18.39 | 140 | 25.0 | -16.36 | -3.11 | -22.79 | 233 |
| 41 | EMA 20/50 cross · 1h | trend | 78.88 | -21.12 | 90 | 11.1 | -22.00 | -4.09 | -27.42 | 126 |
| 42 | CCI reversion · 1h | reversion | 78.13 | -21.87 | 264 | 44.7 | -28.11 | -4.51 | -28.59 | 445 |
| 43 | Supertrend · 1h | trend | 77.68 | -22.32 | 141 | 12.8 | -28.21 | -5.42 | -29.57 | 219 |
| 44 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -25.79 | -5.58 | -27.67 | 208 |
| 45 | Triple EMA stack · 1h | trend | 77.21 | -22.79 | 125 | 14.4 | -28.58 | -5.27 | -30.89 | 208 |
| 46 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -28.44 | -3.77 | -33.54 | 33 |
| 47 | MACD cross · 1h | trend | 76.94 | -23.06 | 299 | 23.4 | -33.39 | -6.65 | -35.23 | 469 |
| 48 | RSI momentum · 1h | momentum | 76.88 | -23.12 | 135 | 12.6 | -30.34 | -5.82 | -30.84 | 213 |
| 49 | Heikin-Ashi · 1h | trend | 76.50 | -23.50 | 356 | 22.5 | -40.63 | -8.71 | -43.18 | 659 |
| 50 | Bollinger reversion · 1h | reversion | 76.17 | -23.83 | 215 | 38.1 | -31.41 | -6.54 | -31.58 | 375 |
| 51 | OBV trend · 1h | momentum | 76.07 | -23.93 | 239 | 17.6 | -33.21 | -7.06 | -33.53 | 300 |
| 52 | Donchian 20/10 · 1h | breakout | 76.05 | -23.95 | 119 | 20.2 | -26.18 | -4.43 | -30.95 | 206 |
| 53 | Williams %R · 1h | reversion | 75.91 | -24.09 | 267 | 46.1 | -36.78 | -6.69 | -36.79 | 517 |
| 54 | ROC + volume · 1h | momentum | 74.87 | -25.13 | 299 | 25.4 | -31.09 | -5.68 | -34.50 | 370 |
| 55 | Z-score reversion · 1h | reversion | 74.86 | -25.14 | 139 | 33.8 | -17.52 | -2.71 | -23.02 | 211 |
| 56 | RSI(14) reversion · 1h | reversion | 70.84 | -29.16 | 128 | 25.8 | -21.56 | -3.88 | -26.28 | 194 |
| 57 | Three white soldiers | momentum | 70.00 | -30.00 | 408 | 16.2 | -45.66 | -21.26 | -45.66 | 610 |
| 58 | EMA 9/21 cross · 1h | trend | 68.95 | -31.05 | 218 | 9.6 | -37.36 | -7.53 | -39.06 | 325 |
| 59 | Candlestick reversal · 1h | reversion | 68.93 | -31.07 | 345 | 27.8 | -38.38 | -7.91 | -38.45 | 544 |
| 60 | Max aggression: 1-day momentum | meta | 68.78 | -31.22 | 23 | 30.4 | -35.26 | -2.08 | -50.32 | 42 |
| 61 | VWAP momentum · 1h | momentum | 68.47 | -31.53 | 697 | 21.5 | -53.06 | -10.62 | -55.35 | 1219 |
| 62 | Agent (ML meta-label) | meta | 68.38 | -31.62 | 1302 | 20.4 | -11.92 | -2.16 | -15.18 | 278 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.78 | -98.96 | 5169 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.93 | -24.32 | -80.07 | 1402 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.65 | -47.56 | -93.65 | 2514 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.05 | -31.56 | -89.05 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.43 | -38.63 | -91.43 | 2322 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.78 | -31.85 | -90.79 | 2232 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.52 | -97.77 | 3473 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.33 | -62.35 | -96.33 | 3379 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.28 | -34.03 | -93.41 | 2404 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.11 | -34.85 | -82.11 | 1681 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.27 | -99.48 | 5876 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -93.09 | -44.54 | -93.09 | 2608 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -36.47 | -95.55 | 3378 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -73.53 | -99.79 | 6172 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.92 | -44.82 | -91.92 | 2275 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.75 | -26.38 | -74.75 | 1556 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -61.73 | -97.77 | 3542 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.71 | -62.47 | -98.71 | 4838 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.33 | -28.28 | -69.68 | 1201 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -55.08 | -94.74 | 2764 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.73 | -37.23 | -84.73 | 1796 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -71.63 | -99.63 | 6317 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.13 | -29.85 | -88.13 | 2226 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.14 | -19.61 | -77.20 | 1700 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.38 | -36.46 | -90.38 | 2237 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.52 | -51.42 | -96.52 | 3827 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -53.60 | -89.45 | 2127 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.08 | -25.19 | -64.90 | 812 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -74.18 | -25.90 | -74.18 | 1274 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.10 | -19.13 | -77.10 | 1607 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.88 | -50.81 | -96.88 | 4245 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -100.09 | -99.92 | 8216 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T06:00 | Candlestick reversal · 1h | buy | XRP-USD | 3.83 | — | rebalance up |
| 2026-11-03T06:00 | Candlestick reversal · 1h | buy | DOGE-USD | 3.79 | — | rebalance up |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | SOL-USD | 7.68 | -0.05 | exit signal |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | ETH-USD | 7.66 | -0.07 | exit signal |
| 2026-11-03T06:00 | Candlestick reversal · 1h | sell | BTC-USD | 7.64 | -0.09 | exit signal |
| 2026-11-03T06:00 | VWAP momentum · 1h | sell | XRP-USD | 17.03 | -0.12 | exit signal |
| 2026-11-03T05:00 | CCI reversion · 1h | buy | BTC-USD | 13.07 | — | entry |
| 2026-11-03T05:00 | CCI reversion · 1h | sell | XRP-USD | 13.08 | -0.05 | exit signal |
| 2026-11-03T05:00 | Ichimoku · 1h | buy | XRP-USD | 20.54 | — | entry signal |
| 2026-11-03T05:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 17.27 | — | entry signal |
| 2026-11-03T04:00 | VWAP momentum · 1h | buy | XRP-USD | 17.15 | — | entry signal |
| 2026-11-03T03:30 | Three white soldiers | sell | BTC-USD | 17.40 | -0.14 | exit signal |
| 2026-11-03T03:20 | MFI reversion · 1h | sell | SOL-USD | 4.12 | -0.02 | rebalance down |
| 2026-11-03T03:20 | Three white soldiers | buy | BTC-USD | 17.53 | — | entry signal |
| 2026-11-03T03:00 | VWAP momentum · 1h | sell | ETH-USD | 17.13 | -0.15 | exit signal |
| 2026-11-03T03:00 | VWAP momentum · 1h | sell | BTC-USD | 17.08 | -0.19 | exit signal |
| 2026-11-03T02:00 | VWAP momentum · 1h | buy | ETH-USD | 3.45 | — | rebalance up |
| 2026-11-03T02:00 | VWAP momentum · 1h | buy | BTC-USD | 3.45 | — | rebalance up |
| 2026-11-03T02:00 | VWAP momentum · 1h | sell | SOL-USD | 9.94 | -0.07 | exit signal |
| 2026-11-03T02:00 | VWAP momentum · 1h | sell | DOGE-USD | 13.72 | -0.10 | exit signal |
| 2026-11-03T01:45 | MFI reversion · 1h | buy | SOL-USD | 4.16 | — | rebalance up |
| 2026-11-03T01:20 | MFI reversion · 1h | sell | SOL-USD | 4.14 | -0.01 | rebalance down |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | SOL-USD | 24.61 | -0.07 | exit signal |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | DOGE-USD | 24.56 | 0.04 | exit signal |
| 2026-11-03T01:00 | VWAP reversion · 1h | sell | BTC-USD | 24.53 | -0.13 | exit signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | SOL-USD | 10.01 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | ETH-USD | 13.82 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | DOGE-USD | 13.82 | — | entry signal |
| 2026-11-03T01:00 | VWAP momentum · 1h | buy | BTC-USD | 13.82 | — | entry signal |
| 2026-11-03T00:00 | CCI reversion · 1h | buy | ETH-USD | 12.97 | — | entry signal |
| 2026-11-03T00:00 | CCI reversion · 1h | sell | XRP-USD | 6.58 | -0.04 | rebalance down |
| 2026-11-03T00:00 | CCI reversion · 1h | sell | DOGE-USD | 6.39 | -0.04 | rebalance down |
| 2026-11-02T23:00 | CCI reversion · 1h | buy | DOGE-USD | 19.54 | — | entry signal |
| 2026-11-02T23:00 | VWAP momentum · 1h | sell | XRP-USD | 17.17 | -0.13 | exit signal |
| 2026-11-02T22:00 | MFI reversion · 1h | buy | SOL-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | MFI reversion · 1h | buy | DOGE-USD | 20.67 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | buy | DOGE-USD | 8.77 | — | entry signal |
| 2026-11-02T22:00 | Z-score reversion · 1h | sell | XRP-USD | 8.77 | -0.05 | exit signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | SOL-USD | 5.46 | — | entry signal |
| 2026-11-02T22:00 | Bollinger reversion · 1h | buy | ETH-USD | 5.46 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 06:20:05.000184+00:00 -> 2026-11-03 06:30:05.000184+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
