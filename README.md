# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T05:55:05.000123+00:00 · 48088 ticks

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

Today: 4830 decisions in 966 calls, $0.0675 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T05:55 | 3 / 0 / 2 | cash |  |
| Breezy | 2026-11-05T05:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T05:55 | 1 / 4 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 112.80 | 12.80 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.49 | 0.49 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -10.74 | -2.79 | -12.83 | 137 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.97 | -1.03 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 9 | Hold SPY | benchmark | 97.86 | -2.14 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.18 | -4.82 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.74 | -5.25 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 17 | Hold BTC | benchmark | 94.25 | -5.75 | 0 | — | -0.85 | 0.03 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Max aggression: 5-day momentum | meta | 91.12 | -8.88 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 22 | Trend pullback · 1h | trend | 90.67 | -9.33 | 103 | 22.3 | -16.41 | -6.07 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.82 | -10.18 | 157 | 28.0 | -14.95 | -3.31 | -19.35 | 245 |
| 24 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 25 | Copy: Insider buying | copy | 89.42 | -10.58 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.91 | -3.44 | -14.15 | 88 |
| 28 | Daily: Bullish score | daily | 86.96 | -13.04 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.70 | -13.30 | 249 | 47.8 | -20.49 | -3.87 | -24.97 | 383 |
| 30 | Donchian 55/20 · 1h | breakout | 86.59 | -13.41 | 62 | 12.9 | -13.05 | -2.77 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 85.99 | -14.01 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 84.98 | -15.02 | 155 | 18.1 | -18.24 | -3.27 | -22.68 | 278 |
| 34 | Volume breakout · 1h | breakout | 84.33 | -15.67 | 133 | 29.3 | -14.19 | -3.25 | -18.08 | 103 |
| 35 | MFI reversion · 1h | reversion | 84.31 | -15.69 | 324 | 34.3 | -13.54 | -2.03 | -18.47 | 152 |
| 36 | Keltner breakout · 1h | breakout | 83.56 | -16.44 | 94 | 24.5 | -19.93 | -4.07 | -22.57 | 178 |
| 37 | Connors RSI(2) · 1h | reversion | 83.11 | -16.89 | 194 | 41.2 | -19.32 | -6.38 | -20.21 | 125 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.93 | -18.07 | 85 | 12.9 | -20.35 | -4.30 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.27 | -18.73 | 148 | 25.0 | -18.07 | -3.67 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.82 | -19.18 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.29 | -20.71 | 92 | 10.9 | -18.54 | -3.26 | -27.87 | 131 |
| 43 | Heikin-Ashi · 1h | trend | 78.69 | -21.31 | 375 | 22.7 | -40.66 | -8.51 | -43.89 | 679 |
| 44 | MACD zero-line · 1h | trend | 78.25 | -21.75 | 143 | 16.8 | -26.06 | -5.44 | -29.33 | 220 |
| 45 | MACD cross · 1h | trend | 77.93 | -22.07 | 314 | 23.9 | -30.69 | -5.98 | -33.62 | 475 |
| 46 | Z-score reversion · 1h | reversion | 77.89 | -22.11 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 47 | Supertrend · 1h | trend | 77.69 | -22.31 | 147 | 12.9 | -28.64 | -5.23 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.79 | -23.21 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.54 | -23.46 | 290 | 47.6 | -33.02 | -5.93 | -34.59 | 523 |
| 51 | RSI momentum · 1h | momentum | 76.32 | -23.68 | 142 | 12.0 | -28.02 | -5.36 | -30.33 | 225 |
| 52 | Triple EMA stack · 1h | trend | 75.77 | -24.23 | 131 | 13.7 | -27.55 | -5.43 | -31.75 | 212 |
| 53 | OBV trend · 1h | momentum | 75.20 | -24.80 | 248 | 17.3 | -30.30 | -6.65 | -30.84 | 295 |
| 54 | Donchian 20/10 · 1h | breakout | 74.21 | -25.79 | 124 | 19.4 | -27.77 | -5.05 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.03 | -25.97 | 324 | 26.2 | -33.23 | -6.42 | -36.17 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.08 | -27.92 | 136 | 28.7 | -20.46 | -3.39 | -26.28 | 217 |
| 57 | EMA 9/21 cross · 1h | trend | 69.42 | -30.58 | 225 | 9.8 | -36.65 | -7.36 | -40.09 | 341 |
| 58 | Candlestick reversal · 1h | reversion | 69.16 | -30.84 | 376 | 30.1 | -35.28 | -6.58 | -37.80 | 555 |
| 59 | VWAP momentum · 1h | momentum | 69.13 | -30.87 | 738 | 22.5 | -53.96 | -11.29 | -55.84 | 1228 |
| 60 | Agent (ML meta-label) | meta | 68.99 | -31.01 | 1449 | 22.2 | -6.55 | -1.11 | -18.58 | 309 |
| 61 | Three white soldiers | momentum | 67.72 | -32.28 | 442 | 16.3 | -46.99 | -21.76 | -47.04 | 634 |
| 62 | Max aggression: 1-day momentum | meta | 66.50 | -33.50 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -46.10 | -98.92 | 5149 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.57 | -25.11 | -79.76 | 1416 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -48.11 | -93.44 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.87 | -31.42 | -88.89 | 1903 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.86 | -39.56 | -90.86 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.57 | -32.51 | -90.58 | 2231 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.69 | -54.50 | -97.70 | 3454 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.26 | -61.72 | -96.26 | 3395 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.86 | -34.52 | -93.87 | 2483 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.15 | -37.38 | -82.15 | 1652 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -53.92 | -99.47 | 5862 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.85 | -44.46 | -92.86 | 2598 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.79 | -37.69 | -95.79 | 3439 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -74.74 | -99.79 | 6160 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.57 | -43.33 | -91.57 | 2252 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.91 | -26.60 | -74.91 | 1558 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.76 | -64.65 | -97.76 | 3525 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -60.90 | -98.69 | 4828 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.49 | -28.72 | -70.05 | 1196 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.65 | -55.10 | -94.65 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.58 | -36.32 | -84.58 | 1784 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -69.71 | -99.62 | 6306 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.28 | -30.35 | -88.44 | 2241 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.44 | -18.90 | -76.92 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.63 | -36.84 | -90.64 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.42 | -49.63 | -96.43 | 3828 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.29 | -52.40 | -89.29 | 2150 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.43 | -27.69 | -65.43 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.56 | -25.19 | -73.56 | 1266 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.48 | -18.24 | -77.24 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.94 | -50.72 | -96.94 | 4250 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -99.17 | -99.93 | 8232 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T05:45 | Three white soldiers | sell | XRP-USD | 16.82 | -0.14 | exit signal |
| 2026-11-05T05:40 | Three white soldiers | buy | XRP-USD | 16.97 | — | entry signal |
| 2026-11-05T05:00 | Agent (ML meta-label) | buy | XRP-USD | 5.10 | — | entry |
| 2026-11-05T05:00 | Agent (ML meta-label) | sell | SOL-USD | 5.10 | -0.05 | selected signal exited |
| 2026-11-05T05:00 | ROC + volume · 1h | sell | BTC-USD | 3.92 | 0.03 | exit signal |
| 2026-11-05T05:00 | VWAP momentum · 1h | sell | SOL-USD | 6.87 | -0.06 | exit signal |
| 2026-11-05T05:00 | MACD zero-line · 1h | sell | DOGE-USD | 8.65 | 0.10 | exit signal |
| 2026-11-05T05:00 | MACD zero-line · 1h | sell | BTC-USD | 8.71 | 0.20 | exit signal |
| 2026-11-05T05:00 | MACD cross · 1h | sell | DOGE-USD | 3.87 | 0.06 | exit signal |
| 2026-11-05T05:00 | MACD cross · 1h | sell | BTC-USD | 4.34 | 0.10 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 05:55:05.000123+00:00 -> 2026-11-05 06:05:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 05:55:05.000123+00:00 -> 2026-11-05 06:05:05.000123+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 05:55:05.000123+00:00 -> 2026-11-05 06:05:05.000123+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
