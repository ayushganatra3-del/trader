# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-02T15:20:05.000150+00:00 · 45130 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.52 (-8.48%)

Closed trades 130, win rate 40.8%, fees £3.76, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-02 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BPRE 12%, ACN 12%, SCQCU 12%, NPB 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-30)

**Correction** since 2026-10-16 · level correction · 9 distribution days in 25 sessions · timing exposure 0% · VXN 28.50 · VIX 19.42 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.1, TSLA 6.7, LABU 4.9, AAPL 4.2, IWM 3.2, PLTR 3.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 11793 decisions in 2274 calls, $0.1636 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-02T15:20 | 6 / 14 / 10 | cash |  |
| Breezy | 2026-11-02T15:20 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-02T15:20 | 7 / 21 / 2 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD zero-line | MSFT | 2.34 | +0.86% | 5 |
| Bollinger reversion | AMZN | 2.17 | +2.35% | 10 |
| Stochastic reversion | ETHU | 2.10 | +5.34% | 11 |
| Z-score reversion | BITX | 2.10 | +6.37% | 7 |
| Williams %R | MSTR | 2.00 | +3.35% | 15 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.46 | 7.46 | 0 | — | 8.73 | 4.16 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.59 | 4.59 | 16 | 68.8 | 6.19 | 2.00 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.15 | 4.15 | 23 | 47.8 | 4.46 | 1.69 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.19 | 0.19 | 26 | 26.9 | 7.71 | 1.98 | -6.03 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.83 | -0.17 | 97 | 45.4 | -12.30 | -3.41 | -12.53 | 138 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 98.50 | -1.50 | 0 | — | 1.88 | 0.83 | -5.02 | 1 |
| 9 | Hold SPY | benchmark | 97.79 | -2.21 | 0 | — | -0.21 | -0.06 | -3.94 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 97.53 | -2.47 | 101 | 35.6 | 4.16 | 2.11 | -2.46 | 94 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.03 | -2.09 | -5.83 | 1 |
| 12 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.65 | 0.69 | -7.93 | 7 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.53 | -4.47 | 17 | 17.6 | -5.37 | -5.56 | -6.20 | 21 |
| 14 | Gap and go | momentum | 95.36 | -4.64 | 125 | 28.8 | 4.42 | 1.46 | -8.76 | 211 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.05 | -4.95 | 0 | — | -5.31 | -2.03 | -6.49 | 1 |
| 16 | Agent (rotation) | meta | 94.90 | -5.10 | 131 | 30.5 | -5.99 | -4.27 | -8.89 | 139 |
| 17 | Copy: Congress Democrats (NANC) | copy | 94.81 | -5.19 | 0 | — | -1.33 | -0.44 | -7.64 | 1 |
| 18 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.92 | -2.65 | -5.33 | 28 |
| 19 | Hold BTC | benchmark | 91.71 | -8.29 | 0 | — | 0.03 | 0.18 | -12.65 | 1 |
| 20 | Agent | meta | 91.52 | -8.48 | 130 | 40.8 | -9.17 | -5.60 | -12.48 | 205 |
| 21 | Trend pullback · 1h | trend | 91.34 | -8.66 | 101 | 21.8 | -17.68 | -6.53 | -18.61 | 82 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.73 | -2.25 | -16.91 | 1 |
| 23 | Opening range 30m | breakout | 90.36 | -9.64 | 317 | 34.7 | -12.18 | -3.72 | -17.21 | 576 |
| 24 | Copy: Insider buying | copy | 89.83 | -10.18 | 34 | 35.3 | -21.05 | -4.22 | -23.10 | 62 |
| 25 | Parabolic SAR · 1h | trend | 89.70 | -10.30 | 145 | 27.6 | -15.08 | -3.57 | -16.86 | 236 |
| 26 | Squeeze breakout · 1h | breakout | 89.49 | -10.51 | 61 | 23.0 | -4.69 | -1.28 | -13.40 | 90 |
| 27 | Daily: Bullish score | daily | 88.91 | -11.09 | 14 | 21.4 | -6.14 | -0.75 | -14.73 | 14 |
| 28 | Donchian 55/20 · 1h | breakout | 88.37 | -11.63 | 59 | 13.6 | -14.22 | -3.21 | -18.06 | 100 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.64 | -12.36 | 1 | 0.0 | -2.92 | -0.29 | -15.96 | 1 |
| 30 | Agent (aggressive) | meta | 87.19 | -12.81 | 64 | 34.4 | -11.28 | -3.73 | -15.04 | 96 |
| 31 | Stochastic reversion · 1h | reversion | 86.50 | -13.50 | 226 | 47.8 | -21.23 | -4.36 | -24.75 | 387 |
| 32 | Volume breakout · 1h | breakout | 85.35 | -14.65 | 127 | 29.1 | -13.66 | -2.90 | -18.27 | 99 |
| 33 | Keltner breakout · 1h | breakout | 84.45 | -15.55 | 88 | 23.9 | -21.49 | -4.30 | -23.96 | 179 |
| 34 | ADX DI cross · 1h | trend | 84.31 | -15.69 | 142 | 19.0 | -17.64 | -3.22 | -20.97 | 252 |
| 35 | Connors RSI(2) · 1h | reversion | 83.52 | -16.48 | 190 | 40.5 | -20.93 | -6.69 | -21.06 | 146 |
| 36 | MFI reversion · 1h | reversion | 83.26 | -16.74 | 299 | 32.8 | -16.33 | -2.62 | -18.35 | 144 |
| 37 | Opening range 15m | breakout | 82.87 | -17.13 | 392 | 31.4 | -17.49 | -5.09 | -19.57 | 710 |
| 38 | Bollinger breakout · 1h | breakout | 81.96 | -18.04 | 139 | 25.2 | -13.38 | -2.37 | -22.43 | 234 |
| 39 | Daily: Momentum burst | daily | 81.73 | -18.27 | 19 | 15.8 | -23.78 | -3.36 | -30.47 | 33 |
| 40 | Max aggression: 5-day momentum | meta | 81.53 | -18.47 | 15 | 40.0 | -35.22 | -2.58 | -37.35 | 26 |
| 41 | Ichimoku · 1h | trend | 81.23 | -18.77 | 81 | 13.6 | -21.30 | -4.28 | -25.37 | 119 |
| 42 | CCI reversion · 1h | reversion | 80.93 | -19.07 | 257 | 45.5 | -24.83 | -3.86 | -27.90 | 440 |
| 43 | Williams %R · 1h | reversion | 79.42 | -20.58 | 259 | 47.1 | -33.81 | -6.12 | -35.37 | 514 |
| 44 | Bollinger reversion · 1h | reversion | 79.18 | -20.82 | 205 | 38.0 | -27.90 | -5.62 | -30.77 | 371 |
| 45 | Supertrend · 1h | trend | 79.13 | -20.87 | 137 | 13.1 | -26.60 | -5.16 | -28.05 | 214 |
| 46 | Z-score reversion · 1h | reversion | 78.92 | -21.08 | 136 | 33.8 | -13.02 | -1.84 | -22.55 | 204 |
| 47 | EMA 20/50 cross · 1h | trend | 78.53 | -21.47 | 90 | 11.1 | -25.12 | -5.11 | -27.53 | 133 |
| 48 | MACD cross · 1h | trend | 77.90 | -22.10 | 293 | 23.9 | -32.56 | -6.46 | -34.42 | 462 |
| 49 | RSI momentum · 1h | momentum | 77.74 | -22.26 | 133 | 12.8 | -30.81 | -5.99 | -30.81 | 212 |
| 50 | MACD zero-line · 1h | trend | 77.63 | -22.38 | 136 | 15.4 | -23.19 | -4.60 | -27.57 | 213 |
| 51 | Triple EMA stack · 1h | trend | 77.02 | -22.98 | 122 | 14.8 | -31.37 | -5.91 | -31.37 | 200 |
| 52 | Heikin-Ashi · 1h | trend | 77.02 | -22.98 | 344 | 23.3 | -41.30 | -8.94 | -42.92 | 661 |
| 53 | OBV trend · 1h | momentum | 76.32 | -23.68 | 235 | 17.4 | -36.41 | -7.93 | -36.81 | 305 |
| 54 | Donchian 20/10 · 1h | breakout | 75.25 | -24.75 | 118 | 20.3 | -24.73 | -4.07 | -30.23 | 209 |
| 55 | ROC + volume · 1h | momentum | 74.34 | -25.66 | 298 | 25.5 | -29.03 | -4.93 | -33.75 | 377 |
| 56 | RSI(14) reversion · 1h | reversion | 73.48 | -26.52 | 124 | 26.6 | -19.44 | -3.30 | -26.17 | 194 |
| 57 | Candlestick reversal · 1h | reversion | 71.74 | -28.26 | 332 | 28.3 | -34.82 | -6.89 | -36.44 | 546 |
| 58 | Max aggression: 1-day momentum | meta | 71.69 | -28.31 | 22 | 31.8 | -32.56 | -1.87 | -50.32 | 42 |
| 59 | Agent (ML meta-label) | meta | 70.97 | -29.03 | 1204 | 20.9 | -15.38 | -2.66 | -19.91 | 309 |
| 60 | VWAP momentum · 1h | momentum | 70.67 | -29.33 | 671 | 22.1 | -52.45 | -11.14 | -52.53 | 1224 |
| 61 | Three white soldiers | momentum | 70.47 | -29.53 | 402 | 16.2 | -45.38 | -21.08 | -45.61 | 616 |
| 62 | EMA 9/21 cross · 1h | trend | 69.48 | -30.52 | 213 | 9.9 | -36.28 | -6.65 | -39.93 | 325 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.96 | -44.93 | -98.96 | 5196 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.68 | -24.09 | -79.78 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.58 | -43.80 | -93.61 | 2530 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.03 | -32.00 | -89.05 | 1928 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.35 | -38.00 | -91.35 | 2336 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.88 | -31.75 | -90.88 | 2245 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -53.58 | -97.77 | 3483 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.28 | -57.61 | -96.29 | 3400 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -35.13 | -93.67 | 2436 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.18 | -33.53 | -82.18 | 1690 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -56.04 | -99.47 | 5837 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -43.81 | -92.99 | 2614 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -37.46 | -95.65 | 3416 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -77.24 | -99.79 | 6172 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.97 | -45.42 | -91.97 | 2288 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.93 | -26.59 | -75.04 | 1567 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -59.68 | -97.72 | 3550 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.65 | -61.21 | -98.65 | 4810 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.98 | -28.09 | -69.07 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.66 | -53.98 | -94.68 | 2769 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.91 | -37.83 | -84.94 | 1809 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -71.09 | -99.62 | 6309 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.96 | -29.82 | -87.98 | 2208 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.79 | -19.50 | -76.81 | 1697 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.25 | -37.57 | -90.25 | 2227 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.35 | -51.66 | -96.37 | 3805 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.70 | -54.71 | -89.70 | 2131 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.18 | -25.25 | -64.66 | 811 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.82 | -25.33 | -73.89 | 1278 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.71 | -18.60 | -75.78 | 1587 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.74 | -50.23 | -96.77 | 4211 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -95.85 | -99.92 | 8244 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-02T15:20 | Agent (rotation) | buy | NVDA | 4.52 | — | entry |
| 2026-11-02T15:20 | Agent (ML meta-label) | buy | MSTR | 9.34 | — | following Williams %R |
| 2026-11-02T15:20 | Agent (ML meta-label) | sell | MSFT | 9.34 | -0.01 | selected signal exited |
| 2026-11-02T15:20 | Opening range 30m | buy | TQQQ | 1.54 | — | entry |
| 2026-11-02T15:20 | Opening range 30m | buy | QQQ | 11.30 | — | entry |
| 2026-11-02T15:20 | Opening range 30m | sell | COIN | 12.84 | -0.10 | target is flat |
| 2026-11-02T15:20 | Opening range 15m | buy | QQQ | 7.53 | — | entry |
| 2026-11-02T15:20 | Opening range 15m | sell | COIN | 8.24 | -0.06 | target is flat |
| 2026-11-02T15:18 | Agent (rotation) | buy | TQQQ | 5.27 | — | entry |
| 2026-11-02T15:18 | Agent (rotation) | buy | ETHU | 5.27 | — | following Stochastic reversion |
| 2026-11-02T15:18 | Agent (ML meta-label) | buy | MSFT | 9.35 | — | following MACD zero-line |
| 2026-11-02T15:18 | VWAP momentum · 1h | buy | SQQQ | 3.57 | — | rebalance up |
| 2026-11-02T15:18 | Opening range 30m | buy | UPRO | 12.93 | — | entry |
| 2026-11-02T15:18 | Opening range 30m | buy | SPY | 12.94 | — | entry |
| 2026-11-02T15:18 | Opening range 30m | buy | MSTR | 12.94 | — | entry |
| 2026-11-02T15:18 | Opening range 30m | buy | ETHU | 12.94 | — | entry |
| 2026-11-02T15:18 | Opening range 30m | buy | COIN | 12.94 | — | entry signal |
| 2026-11-02T15:18 | Opening range 30m | buy | AMZN | 12.94 | — | entry |
| 2026-11-02T15:18 | Opening range 30m | sell | META | 9.63 | -0.05 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | buy | MSTR | 8.28 | — | entry |
| 2026-11-02T15:18 | Opening range 15m | buy | GOOGL | 8.30 | — | entry signal |
| 2026-11-02T15:18 | Opening range 15m | buy | ETHU | 8.30 | — | entry |
| 2026-11-02T15:18 | Opening range 15m | buy | COIN | 8.30 | — | entry signal |
| 2026-11-02T15:18 | Opening range 15m | sell | UPRO | 5.57 | 0.01 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | sell | TNA | 5.56 | 0.01 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | sell | SPY | 5.54 | -0.00 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | sell | META | 5.42 | -0.03 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | sell | IWM | 5.54 | 0.00 | rebalance down |
| 2026-11-02T15:18 | Opening range 15m | sell | AMZN | 5.55 | 0.01 | rebalance down |
| 2026-11-02T15:18 | Gap and go | buy | TQQQ | 15.89 | — | entry signal |
| 2026-11-02T15:18 | Gap and go | buy | ETHU | 15.91 | — | entry |
| 2026-11-02T15:18 | Gap and go | sell | UPRO | 7.91 | 0.03 | rebalance down |
| 2026-11-02T15:18 | Gap and go | sell | TNA | 7.90 | 0.02 | rebalance down |
| 2026-11-02T15:18 | Gap and go | sell | MSTR | 8.03 | 0.10 | rebalance down |
| 2026-11-02T15:18 | Gap and go | sell | AMZN | 7.96 | 0.05 | rebalance down |
| 2026-11-02T15:16 | Agent (rotation) | buy | MSTR | 7.89 | — | following Williams %R |
| 2026-11-02T15:16 | Opening range 30m | sell | UPRO | 22.63 | -0.05 | target is flat |
| 2026-11-02T15:16 | Gap and go | buy | MSTR | 23.64 | — | entry |
| 2026-11-02T15:14 | Opening range 30m | buy | UPRO | 22.68 | — | entry signal |
| 2026-11-02T15:14 | Opening range 30m | buy | META | 22.68 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-04 15:20:05.000150+00:00 -> 2026-11-02 15:30:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
