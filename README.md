# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T04:25:05.000151+00:00 · 48007 ticks

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

Today: 3615 decisions in 723 calls, $0.0505 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T04:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-05T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T04:25 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.84 | 12.84 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.52 | 0.52 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.74 | -2.79 | -12.83 | 137 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.01 | -0.99 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 9 | Hold SPY | benchmark | 97.89 | -2.11 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.22 | -4.78 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.78 | -5.22 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Hold BTC | benchmark | 94.26 | -5.74 | 0 | — | -1.15 | -0.02 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 91.15 | -8.85 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 22 | Trend pullback · 1h | trend | 90.65 | -9.35 | 103 | 22.3 | -16.44 | -6.09 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.84 | -10.15 | 157 | 28.0 | -14.95 | -3.31 | -19.35 | 245 |
| 24 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 25 | Copy: Insider buying | copy | 89.45 | -10.55 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -10.00 | -3.47 | -14.15 | 88 |
| 28 | Daily: Bullish score | daily | 86.97 | -13.03 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.73 | -13.27 | 249 | 47.8 | -20.49 | -3.87 | -24.97 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.64 | -13.36 | 62 | 12.9 | -13.03 | -2.77 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.02 | -13.98 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 84.99 | -15.01 | 155 | 18.1 | -18.12 | -3.24 | -22.68 | 277 |
| 34 | Volume breakout · 1h | breakout | 84.35 | -15.65 | 133 | 29.3 | -14.19 | -3.25 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.33 | -15.67 | 324 | 34.3 | -13.54 | -2.03 | -18.47 | 152 |
| 36 | Keltner breakout · 1h | breakout | 83.58 | -16.42 | 94 | 24.5 | -20.13 | -4.12 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.38 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.94 | -18.06 | 85 | 12.9 | -20.37 | -4.31 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.29 | -18.71 | 148 | 25.0 | -18.07 | -3.67 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.85 | -19.15 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.34 | -20.66 | 92 | 10.9 | -18.53 | -3.26 | -27.87 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 78.72 | -21.28 | 375 | 22.7 | -40.63 | -8.50 | -43.89 | 679 |
| 44 | MACD zero-line · 1h | trend | 78.32 | -21.68 | 141 | 15.6 | -25.55 | -5.31 | -29.50 | 221 |
| 45 | MACD cross · 1h | trend | 77.97 | -22.03 | 312 | 23.4 | -30.53 | -5.94 | -33.62 | 474 |
| 46 | Z-score reversion · 1h | reversion | 77.92 | -22.08 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.74 | -22.26 | 147 | 12.9 | -28.64 | -5.22 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.82 | -23.18 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.56 | -23.44 | 290 | 47.6 | -33.00 | -5.92 | -34.59 | 523 |
| 51 | RSI momentum · 1h | momentum | 76.35 | -23.65 | 142 | 12.0 | -28.90 | -5.56 | -30.42 | 227 |
| 52 | Triple EMA stack · 1h | trend | 75.80 | -24.20 | 131 | 13.7 | -27.58 | -5.44 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.23 | -24.77 | 248 | 17.3 | -30.70 | -6.76 | -31.09 | 296 |
| 54 | Donchian 20/10 · 1h | breakout | 74.24 | -25.76 | 124 | 19.4 | -27.76 | -5.05 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.06 | -25.94 | 323 | 26.0 | -33.28 | -6.43 | -36.24 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.11 | -27.89 | 136 | 28.7 | -19.98 | -3.29 | -26.28 | 218 |
| 57 | EMA 9/21 cross · 1h | trend | 69.46 | -30.54 | 225 | 9.8 | -36.64 | -7.36 | -40.09 | 341 |
| 58 | Candlestick reversal · 1h | reversion | 69.17 | -30.83 | 376 | 30.1 | -35.43 | -6.60 | -37.95 | 554 |
| 59 | VWAP momentum · 1h | momentum | 69.15 | -30.85 | 737 | 22.5 | -53.96 | -11.28 | -55.84 | 1228 |
| 60 | Agent (ML meta-label) | meta | 69.05 | -30.95 | 1448 | 22.2 | -9.10 | -1.47 | -20.08 | 305 |
| 61 | Three white soldiers | momentum | 67.86 | -32.14 | 441 | 16.3 | -46.98 | -21.76 | -46.98 | 634 |
| 62 | Max aggression: 1-day momentum | meta | 66.52 | -33.48 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.91 | -45.41 | -98.91 | 5141 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.22 | -25.79 | -80.23 | 1422 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.49 | -47.72 | -93.49 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.88 | -31.35 | -88.89 | 1900 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.95 | -39.38 | -90.97 | 2310 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.51 | -32.33 | -90.52 | 2227 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.70 | -53.72 | -97.70 | 3456 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -61.48 | -96.26 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.81 | -34.35 | -93.82 | 2480 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.31 | -37.33 | -82.32 | 1656 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -53.65 | -99.47 | 5861 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.86 | -44.44 | -92.86 | 2599 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.76 | -37.48 | -95.76 | 3435 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -72.77 | -99.79 | 6156 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.71 | -43.24 | -91.71 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.91 | -26.60 | -74.91 | 1558 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -63.57 | -97.74 | 3523 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -59.98 | -98.68 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.61 | -28.86 | -70.17 | 1198 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.67 | -55.06 | -94.67 | 2756 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.60 | -36.37 | -84.60 | 1784 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -68.56 | -99.62 | 6304 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.27 | -30.31 | -88.44 | 2240 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.44 | -18.90 | -76.92 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.61 | -36.67 | -90.62 | 2220 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.43 | -49.85 | -96.44 | 3831 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.22 | -51.88 | -89.23 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.43 | -27.69 | -65.43 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.69 | -25.34 | -73.69 | 1268 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.55 | -18.27 | -77.34 | 1606 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.94 | -50.83 | -96.94 | 4254 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -96.61 | -99.93 | 8228 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T04:05 | Volume breakout · 1h | sell | DOGE-USD | 7.04 | -0.03 | target is flat |
| 2026-11-05T04:00 | Agent (ML meta-label) | buy | SOL-USD | 5.15 | — | entry |
| 2026-11-05T04:00 | Agent (ML meta-label) | sell | ETH-USD | 4.90 | -0.04 | selected signal exited |
| 2026-11-05T04:00 | ROC + volume · 1h | sell | ETH-USD | 3.90 | 0.14 | exit signal |
| 2026-11-05T04:00 | ROC + volume · 1h | sell | DOGE-USD | 3.90 | -0.01 | exit signal |
| 2026-11-05T04:00 | VWAP momentum · 1h | buy | SOL-USD | 4.17 | — | rebalance up |
| 2026-11-05T04:00 | VWAP momentum · 1h | sell | ETH-USD | 5.29 | -0.04 | exit signal |
| 2026-11-05T04:00 | VWAP momentum · 1h | sell | DOGE-USD | 5.29 | -0.04 | exit signal |
| 2026-11-05T04:00 | MACD cross · 1h | sell | ETH-USD | 4.44 | 0.20 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 04:25:05.000151+00:00 -> 2026-11-05 04:35:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 04:25:05.000151+00:00 -> 2026-11-05 04:35:05.000151+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 04:25:05.000151+00:00 -> 2026-11-05 04:35:05.000151+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
