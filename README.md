# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T17:25:05.000127+00:00 · 48697 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.06 (-10.94%)

Closed trades 147, win rate 37.4%, fees £4.06, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-05 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 25575 decisions in 2793 calls, $0.3264 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T17:25 | 1 / 17 / 12 | cash |  |
| Breezy | 2026-11-05T17:25 | 0 / 21 / 9 | cash |  |
| Boozy | 2026-11-05T17:25 | 4 / 20 / 6 | COIN 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.86 | 12.86 | 0 | — | 14.32 | 4.96 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 111.72 | 11.72 | 18 | 66.7 | 15.32 | 3.27 | -4.91 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 106.04 | 6.04 | 28 | 25.0 | 14.74 | 2.66 | -8.66 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.01 | 2.01 | 28 | 42.9 | 0.50 | 0.24 | -9.64 | 29 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.32 | -0.68 | 0 | — | 3.22 | 1.00 | -6.60 | 1 |
| 8 | VWAP reversion · 1h | reversion | 98.61 | -1.39 | 106 | 46.2 | -12.16 | -3.18 | -12.83 | 142 |
| 9 | Day trade: Stocks in Play ORB | daytrade | 97.34 | -2.66 | 116 | 34.5 | 4.52 | 2.37 | -3.32 | 90 |
| 10 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 12 | Copy: Hedge-fund gurus (GURU) | copy | 95.29 | -4.71 | 0 | — | -3.49 | -1.29 | -6.35 | 1 |
| 13 | Gap and go | momentum | 95.15 | -4.85 | 161 | 29.2 | 0.34 | 0.20 | -9.18 | 220 |
| 14 | Hold SPY | benchmark | 94.60 | -5.40 | 0 | — | -3.88 | -1.58 | -5.38 | 1 |
| 15 | Agent (rotation) | meta | 94.59 | -5.41 | 174 | 27.6 | -6.46 | -3.85 | -10.38 | 171 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Trend pullback · 1h | trend | 92.42 | -7.58 | 105 | 22.9 | -15.12 | -5.35 | -17.86 | 81 |
| 18 | Daily: Connors RSI(2) · 3x ETFs ⏸ | daily | 92.31 | -7.68 | 7 | 42.9 | -9.80 | -1.16 | -17.57 | 8 |
| 19 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 20 | Copy: Congress Democrats (NANC) | copy | 90.73 | -9.27 | 0 | — | -6.26 | -1.98 | -10.27 | 1 |
| 21 | Opening range 30m | breakout | 89.51 | -10.49 | 365 | 32.9 | -15.36 | -4.99 | -17.21 | 584 |
| 22 | Hold BTC | benchmark | 89.18 | -10.82 | 0 | — | -4.82 | -0.59 | -13.31 | 1 |
| 23 | Agent | meta | 89.06 | -10.94 | 147 | 37.4 | -14.40 | -8.12 | -14.79 | 214 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.33 | -3.24 | -14.15 | 84 |
| 25 | Daily: Bullish score | daily | 88.12 | -11.88 | 14 | 21.4 | -8.28 | -1.25 | -16.58 | 14 |
| 26 | Copy: Insider buying | copy | 87.13 | -12.87 | 38 | 39.5 | -24.58 | -4.90 | -25.10 | 65 |
| 27 | Parabolic SAR · 1h | trend | 86.91 | -13.09 | 166 | 27.1 | -18.42 | -4.02 | -21.06 | 243 |
| 28 | Donchian 55/20 · 1h | breakout | 85.96 | -14.04 | 71 | 14.1 | -13.77 | -2.90 | -19.94 | 105 |
| 29 | Max aggression: 5-day momentum ⏸ | meta | 85.13 | -14.87 | 17 | 47.1 | -33.79 | -2.11 | -37.46 | 25 |
| 30 | Agent (aggressive) | meta | 84.24 | -15.76 | 72 | 30.6 | -18.09 | -5.34 | -19.03 | 98 |
| 31 | Opening range 15m | breakout | 83.31 | -16.69 | 445 | 30.6 | -19.45 | -5.82 | -21.20 | 712 |
| 32 | Volume breakout · 1h | breakout | 82.11 | -17.89 | 144 | 27.8 | -14.14 | -3.23 | -18.40 | 96 |
| 33 | Stochastic reversion · 1h ⏸ | reversion | 81.45 | -18.55 | 255 | 46.7 | -26.92 | -4.54 | -27.41 | 379 |
| 34 | Keltner breakout · 1h | breakout | 81.37 | -18.63 | 106 | 23.6 | -24.99 | -5.34 | -25.42 | 187 |
| 35 | Connors RSI(2) · 1h | reversion | 80.86 | -19.14 | 202 | 40.1 | -21.36 | -6.85 | -22.17 | 135 |
| 36 | Copy: Cathie Wood (ARKK) ⏸ | copy | 80.06 | -19.94 | 2 | 0.0 | -15.24 | -2.12 | -24.16 | 1 |
| 37 | ADX DI cross · 1h ⏸ | trend | 79.76 | -20.23 | 171 | 18.1 | -23.69 | -3.82 | -26.45 | 262 |
| 38 | MFI reversion · 1h ⏸ | reversion | 79.11 | -20.89 | 328 | 33.8 | -20.81 | -3.04 | -21.16 | 150 |
| 39 | Bollinger breakout · 1h | breakout | 78.58 | -21.42 | 165 | 23.6 | -23.45 | -4.79 | -26.52 | 252 |
| 40 | Ichimoku · 1h | trend | 78.27 | -21.73 | 93 | 15.1 | -24.39 | -4.95 | -28.61 | 130 |
| 41 | CCI reversion · 1h | reversion | 78.00 | -22.00 | 283 | 45.9 | -25.95 | -3.88 | -28.54 | 446 |
| 42 | Heikin-Ashi · 1h | trend | 76.53 | -23.47 | 385 | 23.1 | -42.63 | -8.82 | -44.06 | 676 |
| 43 | EMA 20/50 cross · 1h | trend | 76.09 | -23.91 | 102 | 10.8 | -21.29 | -3.79 | -27.81 | 134 |
| 44 | MACD zero-line · 1h | trend | 74.86 | -25.14 | 153 | 16.3 | -29.55 | -5.94 | -30.07 | 216 |
| 45 | Triple EMA stack · 1h | trend | 74.51 | -25.49 | 141 | 14.9 | -30.95 | -6.29 | -33.29 | 211 |
| 46 | Supertrend · 1h | trend | 73.73 | -26.27 | 165 | 13.3 | -30.63 | -5.66 | -33.58 | 234 |
| 47 | RSI momentum · 1h | momentum | 73.46 | -26.54 | 158 | 12.7 | -30.72 | -5.82 | -32.33 | 225 |
| 48 | MACD cross · 1h ⏸ | trend | 73.30 | -26.70 | 334 | 23.1 | -37.93 | -6.79 | -38.83 | 478 |
| 49 | Z-score reversion · 1h ⏸ | reversion | 73.13 | -26.87 | 159 | 35.8 | -26.31 | -4.28 | -26.67 | 217 |
| 50 | Bollinger reversion · 1h | reversion | 72.89 | -27.11 | 237 | 40.1 | -32.34 | -6.23 | -32.71 | 366 |
| 51 | Williams %R · 1h | reversion | 72.55 | -27.45 | 298 | 46.6 | -36.04 | -6.29 | -36.54 | 534 |
| 52 | Daily: Momentum burst ⏸ | daily | 72.30 | -27.70 | 26 | 11.5 | -34.88 | -4.89 | -36.84 | 32 |
| 53 | Donchian 20/10 · 1h | breakout | 71.84 | -28.16 | 140 | 20.0 | -32.98 | -6.04 | -34.25 | 221 |
| 54 | ROC + volume · 1h | momentum | 71.53 | -28.47 | 339 | 25.7 | -36.60 | -7.13 | -38.28 | 385 |
| 55 | OBV trend · 1h | momentum | 71.47 | -28.53 | 264 | 17.4 | -34.60 | -7.35 | -34.63 | 299 |
| 56 | VWAP momentum · 1h | momentum | 67.87 | -32.13 | 756 | 22.2 | -55.28 | -11.96 | -56.19 | 1223 |
| 57 | EMA 9/21 cross · 1h | trend | 67.66 | -32.34 | 240 | 10.0 | -41.02 | -8.09 | -41.45 | 337 |
| 58 | Three white soldiers | momentum | 67.20 | -32.80 | 446 | 16.1 | -47.28 | -21.90 | -47.28 | 635 |
| 59 | RSI(14) reversion · 1h ⏸ | reversion | 66.40 | -33.60 | 142 | 27.5 | -25.83 | -4.04 | -29.66 | 216 |
| 60 | Candlestick reversal · 1h | reversion | 66.17 | -33.83 | 378 | 29.9 | -37.84 | -7.05 | -38.12 | 559 |
| 61 | Agent (ML meta-label) | meta | 65.88 | -34.12 | 1486 | 22.3 | -10.78 | -1.53 | -17.35 | 334 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 62.20 | -37.80 | 26 | 26.9 | -42.71 | -2.69 | -54.60 | 43 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -45.52 | -98.92 | 5147 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.71 | -25.14 | -80.04 | 1408 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.38 | -46.91 | -93.38 | 2507 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.70 | -30.68 | -88.85 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.47 | -38.00 | -90.51 | 2285 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.80 | -32.60 | -90.84 | 2242 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.61 | -52.71 | -97.61 | 3417 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -58.24 | -96.16 | 3377 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.76 | -33.44 | -93.79 | 2462 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.79 | -36.34 | -81.79 | 1641 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.51 | -54.19 | -99.51 | 5909 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.50 | -42.31 | -92.64 | 2578 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.92 | -38.06 | -95.94 | 3437 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -71.14 | -99.80 | 6159 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -42.75 | -91.51 | 2236 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.31 | -25.39 | -74.72 | 1553 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -61.21 | -97.72 | 3512 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.75 | -60.06 | -98.76 | 4845 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.72 | -27.07 | -69.70 | 1184 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.51 | -54.42 | -94.51 | 2727 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.53 | -36.16 | -84.53 | 1787 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -69.39 | -99.64 | 6307 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.95 | -30.65 | -89.08 | 2263 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.25 | -19.14 | -77.36 | 1725 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -91.15 | -36.22 | -91.22 | 2231 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.55 | -50.18 | -96.59 | 3842 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.10 | -50.40 | -89.10 | 2125 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.41 | -27.58 | -65.74 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.27 | -23.90 | -73.98 | 1262 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.39 | -17.82 | -77.51 | 1645 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.21 | -49.09 | -97.23 | 4295 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -94.70 | -99.93 | 8202 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T17:20 | Agent (ML meta-label) | buy | SOXL | 5.51 | — | following Connors RSI(2) |
| 2026-11-05T17:15 | Agent (ML meta-label) | buy | SPY | 6.01 | — | entry |
| 2026-11-05T17:15 | Agent (ML meta-label) | sell | SOXL | 5.16 | 0.10 | selected signal exited |
| 2026-11-05T17:10 | Agent (ML meta-label) | sell | SPY | 5.48 | -0.02 | selected signal exited |
| 2026-11-05T17:10 | Agent (ML meta-label) | sell | GOOGL | 5.08 | 0.02 | selected signal exited |
| 2026-11-05T17:05 | Agent (ML meta-label) | buy | TECL | 4.81 | — | entry |
| 2026-11-05T17:05 | Agent (ML meta-label) | buy | SOXL | 5.06 | — | following Connors RSI(2) |
| 2026-11-05T17:05 | Agent (ML meta-label) | buy | GOOGL | 5.06 | — | entry |
| 2026-11-05T17:05 | Agent (ML meta-label) | sell | SQQQ | 5.55 | 0.06 | selected signal exited |
| 2026-11-05T17:05 | Donchian 55/20 · 1h | sell | AAPL | 21.08 | -0.52 | stop-loss |
| 2026-11-05T17:05 | Donchian 20/10 · 1h | sell | AAPL | 17.88 | -0.34 | stop-loss |
| 2026-11-05T17:05 | RSI momentum · 1h | sell | AAPL | 18.13 | -0.45 | stop-loss |
| 2026-11-05T17:05 | Parabolic SAR · 1h | sell | AAPL | 21.63 | -0.49 | stop-loss |
| 2026-11-05T17:00 | VWAP reversion · 1h | buy | SOL-USD | 24.83 | — | entry signal |
| 2026-11-05T17:00 | VWAP reversion · 1h | buy | ETH-USD | 24.83 | — | entry signal |
| 2026-11-05T17:00 | VWAP reversion · 1h | buy | DOGE-USD | 24.83 | — | entry signal |
| 2026-11-05T17:00 | VWAP reversion · 1h | buy | BTC-USD | 24.83 | — | entry signal |
| 2026-11-05T16:55 | Agent (ML meta-label) | sell | QQQ | 5.49 | -0.00 | selected signal exited |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | SQQQ | 5.50 | — | entry |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | SPY | 5.50 | — | entry |
| 2026-11-05T16:50 | Agent (ML meta-label) | buy | QQQ | 5.50 | — | entry |
| 2026-11-05T16:50 | OBV trend · 1h | sell | AAPL | 14.35 | -0.32 | stop-loss |
| 2026-11-05T16:50 | EMA 20/50 cross · 1h | sell | AAPL | 15.32 | -0.31 | stop-loss |
| 2026-11-05T16:45 | Agent (ML meta-label) | sell | SPY | 6.00 | -0.02 | selected signal exited |
| 2026-11-05T16:45 | Parabolic SAR · 1h | buy | AAPL | 4.37 | — | rebalance up |
| 2026-11-05T16:45 | Three white soldiers | sell | TSLA | 16.70 | -0.13 | exit signal |
| 2026-11-05T16:40 | Agent (ML meta-label) | sell | TECL | 5.08 | -0.03 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | buy | SPY | 6.01 | — | entry |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | SQQQ | 5.15 | -0.03 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | QQQ | 5.09 | -0.02 | selected signal exited |
| 2026-11-05T16:35 | Agent (ML meta-label) | sell | ETHU | 5.07 | -0.04 | selected signal exited |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | UPRO | 5.09 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | TSLA | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | TECL | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | QQQ | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | PLTR | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | ETHU | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | COIN | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | BITX | 5.11 | — | entry |
| 2026-11-05T16:30 | Agent (ML meta-label) | buy | AMZN | 5.11 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 17:25:05.000127+00:00 -> 2026-11-05 17:35:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 17:25:05.000127+00:00 -> 2026-11-05 17:35:05.000127+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 17:25:05.000127+00:00 -> 2026-11-05 17:35:05.000127+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
