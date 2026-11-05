# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T03:25:05.000162+00:00 · 47954 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 2820 decisions in 564 calls, $0.0394 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T03:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-05T03:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T03:25 | 2 / 3 / 0 | SOL-USD 62% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.82 | 12.82 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.50 | 0.51 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.74 | -2.79 | -12.83 | 137 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.99 | -1.01 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 9 | Hold SPY | benchmark | 97.87 | -2.13 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.20 | -4.80 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.76 | -5.24 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Hold BTC | benchmark | 94.58 | -5.42 | 0 | — | -1.09 | -0.01 | -13.22 | 1 |
| 17 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 91.13 | -8.87 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 22 | Trend pullback · 1h | trend | 90.75 | -9.25 | 103 | 22.3 | -16.34 | -6.04 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.83 | -10.17 | 157 | 28.0 | -14.95 | -3.31 | -19.35 | 245 |
| 24 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 25 | Copy: Insider buying | copy | 89.44 | -10.56 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.47 | -14.15 | 88 |
| 28 | Daily: Bullish score | daily | 86.96 | -13.04 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Donchian 55/20 · 1h | breakout | 86.89 | -13.11 | 62 | 12.9 | -12.77 | -2.70 | -19.91 | 105 |
| 30 | Stochastic reversion · 1h | reversion | 86.71 | -13.29 | 249 | 47.8 | -20.49 | -3.87 | -24.97 | 383 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.00 | -14.00 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.05 | -14.95 | 155 | 18.1 | -17.81 | -3.17 | -22.68 | 277 |
| 34 | Volume breakout · 1h | breakout | 84.48 | -15.52 | 132 | 28.8 | -14.04 | -3.21 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.32 | -15.68 | 324 | 34.3 | -13.54 | -2.03 | -18.47 | 152 |
| 36 | Keltner breakout · 1h | breakout | 83.62 | -16.38 | 94 | 24.5 | -19.87 | -4.06 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.38 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.05 | -17.95 | 85 | 12.9 | -20.25 | -4.28 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.32 | -18.68 | 148 | 25.0 | -18.03 | -3.66 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.83 | -19.17 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.51 | -20.49 | 92 | 10.9 | -18.36 | -3.22 | -27.87 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 78.70 | -21.30 | 375 | 22.7 | -40.53 | -8.47 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.48 | -21.52 | 141 | 15.6 | -25.01 | -5.16 | -29.63 | 222 |
| 45 | MACD cross · 1h | trend | 78.07 | -21.93 | 311 | 23.2 | -30.58 | -5.96 | -33.62 | 475 |
| 46 | Z-score reversion · 1h | reversion | 77.90 | -22.10 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.86 | -22.14 | 147 | 12.9 | -28.53 | -5.20 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.80 | -23.20 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.55 | -23.45 | 290 | 47.6 | -33.00 | -5.92 | -34.59 | 523 |
| 51 | RSI momentum · 1h | momentum | 76.50 | -23.50 | 142 | 12.0 | -29.10 | -5.58 | -30.72 | 228 |
| 52 | Triple EMA stack · 1h | trend | 76.00 | -24.00 | 131 | 13.7 | -27.43 | -5.40 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.40 | -24.60 | 248 | 17.3 | -30.16 | -6.61 | -30.91 | 295 |
| 54 | Donchian 20/10 · 1h | breakout | 74.37 | -25.63 | 124 | 19.4 | -27.62 | -5.02 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.12 | -25.88 | 321 | 25.5 | -33.11 | -6.38 | -36.15 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.10 | -27.91 | 136 | 28.7 | -20.71 | -3.44 | -26.28 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 69.59 | -30.41 | 225 | 9.8 | -36.54 | -7.33 | -40.09 | 341 |
| 58 | VWAP momentum · 1h | momentum | 69.29 | -30.70 | 735 | 22.6 | -53.84 | -11.23 | -55.84 | 1228 |
| 59 | Candlestick reversal · 1h | reversion | 69.16 | -30.84 | 376 | 30.1 | -35.07 | -6.52 | -37.54 | 552 |
| 60 | Agent (ML meta-label) | meta | 69.10 | -30.90 | 1447 | 22.3 | -14.23 | -2.65 | -21.40 | 301 |
| 61 | Three white soldiers | momentum | 67.86 | -32.14 | 441 | 16.3 | -46.98 | -21.76 | -46.98 | 634 |
| 62 | Max aggression: 1-day momentum | meta | 66.51 | -33.49 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.19 | -98.92 | 5150 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.09 | -25.58 | -80.16 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -46.97 | -93.45 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.85 | -30.97 | -88.96 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.88 | -38.92 | -90.91 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.46 | -32.15 | -90.47 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -52.74 | -97.70 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.24 | -60.86 | -96.24 | 3396 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.73 | -34.04 | -93.75 | 2475 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.21 | -36.93 | -82.30 | 1657 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -53.98 | -99.48 | 5878 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.81 | -43.84 | -92.83 | 2599 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.72 | -37.08 | -95.72 | 3430 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -72.29 | -99.79 | 6164 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.76 | -43.13 | -91.76 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.87 | -26.51 | -74.87 | 1558 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -62.59 | -97.73 | 3524 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -60.59 | -98.70 | 4831 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.49 | -28.60 | -70.17 | 1197 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.64 | -54.33 | -94.65 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.52 | -35.99 | -84.52 | 1783 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.76 | -99.62 | 6306 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.26 | -30.27 | -88.44 | 2240 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.49 | -18.95 | -76.94 | 1699 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.67 | -90.62 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -49.60 | -96.45 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -52.69 | -89.35 | 2157 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.32 | -27.49 | -65.41 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.79 | -25.28 | -73.85 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.45 | -18.22 | -77.25 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.93 | -50.30 | -96.93 | 4249 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -95.30 | -99.93 | 8228 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T03:00 | VWAP momentum · 1h | buy | XRP-USD | 5.29 | — | entry |
| 2026-11-05T03:00 | VWAP momentum · 1h | sell | BTC-USD | 5.29 | -0.04 | exit signal |
| 2026-11-05T02:56 | Agent (ML meta-label) | buy | ETH-USD | 3.79 | — | rebalance up |
| 2026-11-05T02:56 | Agent (ML meta-label) | sell | BTC-USD | 4.04 | -0.03 | selected signal exited |
| 2026-11-05T02:35 | Three white soldiers | sell | ETH-USD | 16.90 | -0.12 | exit signal |
| 2026-11-05T02:30 | Three white soldiers | sell | XRP-USD | 16.92 | -0.09 | exit signal |
| 2026-11-05T02:00 | Agent (ML meta-label) | buy | ETH-USD | 1.15 | — | entry |
| 2026-11-05T02:00 | Agent (ML meta-label) | buy | BTC-USD | 4.07 | — | entry |
| 2026-11-05T02:00 | VWAP momentum · 1h | buy | SOL-USD | 2.76 | — | entry signal |
| 2026-11-05T02:00 | VWAP momentum · 1h | buy | ETH-USD | 5.33 | — | entry signal |
| 2026-11-05T02:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.33 | — | entry signal |
| 2026-11-05T02:00 | VWAP momentum · 1h | buy | BTC-USD | 5.33 | — | entry signal |
| 2026-11-05T02:00 | Trend pullback · 1h | buy | XRP-USD | 22.69 | — | entry signal |
| 2026-11-05T02:00 | Parabolic SAR · 1h | sell | ETH-USD | 9.01 | 0.44 | exit signal |
| 2026-11-05T02:00 | Parabolic SAR · 1h | sell | BTC-USD | 9.06 | 0.26 | exit signal |
| 2026-11-05T01:55 | Agent (ML meta-label) | sell | ETH-USD | 4.61 | -0.00 | selected signal exited |
| 2026-11-05T01:45 | Three white soldiers | buy | XRP-USD | 17.02 | — | entry signal |
| 2026-11-05T01:45 | Three white soldiers | buy | ETH-USD | 17.02 | — | entry signal |
| 2026-11-05T01:15 | Agent (ML meta-label) | buy | ETH-USD | 4.61 | — | entry |
| 2026-11-05T01:10 | Agent (ML meta-label) | sell | ETH-USD | 4.59 | -0.03 | selected signal exited |
| 2026-11-05T01:05 | Agent (ML meta-label) | buy | ETH-USD | 4.62 | — | entry |
| 2026-11-05T01:00 | Agent (ML meta-label) | sell | ETH-USD | 4.91 | -0.04 | selected signal exited |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | XRP-USD | 3.29 | 0.06 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | SOL-USD | 3.03 | -0.03 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | ETH-USD | 3.31 | 0.17 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.80 | 0.13 | exit signal |
| 2026-11-05T01:00 | VWAP momentum · 1h | sell | BTC-USD | 3.32 | 0.11 | exit signal |
| 2026-11-05T01:00 | MACD cross · 1h | sell | XRP-USD | 3.65 | 0.01 | exit signal |
| 2026-11-05T00:55 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:45 | Agent (ML meta-label) | sell | ETH-USD | 4.93 | -0.02 | selected signal exited |
| 2026-11-04T23:40 | Agent (ML meta-label) | buy | ETH-USD | 4.95 | — | entry |
| 2026-11-04T23:05 | Three white soldiers | sell | SOL-USD | 17.05 | -0.03 | exit signal |
| 2026-11-04T23:05 | Three white soldiers | sell | ETH-USD | 16.99 | -0.10 | exit signal |
| 2026-11-04T23:00 | VWAP momentum · 1h | buy | SOL-USD | 3.06 | — | entry signal |
| 2026-11-04T22:55 | Three white soldiers | sell | BTC-USD | 16.97 | -0.14 | stop-loss |
| 2026-11-04T22:45 | Three white soldiers | buy | BTC-USD | 17.11 | — | entry signal |
| 2026-11-04T22:20 | EMA 20/50 cross · 1h | sell | XRP-USD | 3.96 | 0.12 | rebalance down |
| 2026-11-04T22:20 | Three white soldiers | buy | SOL-USD | 17.09 | — | entry signal |
| 2026-11-04T22:20 | Three white soldiers | buy | ETH-USD | 17.09 | — | entry signal |
| 2026-11-04T21:15 | Agent (ML meta-label) | sell | ETH-USD | 5.31 | -0.02 | selected signal exited |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 03:25:05.000162+00:00 -> 2026-11-05 03:35:05.000162+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 03:25:05.000162+00:00 -> 2026-11-05 03:35:05.000162+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 03:25:05.000162+00:00 -> 2026-11-05 03:35:05.000162+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
