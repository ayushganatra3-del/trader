# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T17:50:05.000155+00:00 · 46404 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.54 (-9.46%)

Closed trades 141, win rate 39.0%, fees £3.96, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-03 | MSM 12%, RAPP 12%, LRN 12%, SRRK 12%, BBTX 12%, BPRE 12%, ACN 12%, SCQCU 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-02)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.89 · VIX 21.15 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.9, TSLA 6.7, IWM 3.1, AAPL 2.5, MSTR 1.4, BITX 1.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 23961 decisions in 2604 calls, $0.3042 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T17:50 | 9 / 16 / 5 | cash |  |
| Breezy | 2026-11-03T17:50 | 0 / 29 / 1 | cash |  |
| Boozy | 2026-11-03T17:50 | 7 / 21 / 2 | COIN 64% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.43 | 9.43 | 0 | — | 10.39 | 4.50 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 1.35 | 0.57 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.93 | 0.94 | 26 | 26.9 | 8.66 | 2.19 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.93 | -3.58 | -13.20 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 97.01 | -2.99 | 0 | — | -1.22 | -0.60 | -3.94 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.44 | -3.56 | 5 | 40.0 | 3.00 | 0.79 | -7.93 | 8 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.37 | -3.63 | 107 | 34.6 | 4.35 | 2.08 | -3.79 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 96.17 | -3.83 | 0 | — | -0.49 | -0.11 | -6.60 | 1 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.61 | -5.33 | 29 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.33 | -5.67 | 0 | — | -2.96 | -1.12 | -7.64 | 1 |
| 16 | Agent (rotation) | meta | 94.20 | -5.80 | 156 | 28.8 | -5.00 | -2.98 | -8.64 | 185 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.11 | -5.89 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 92.64 | -7.36 | 148 | 27.0 | 2.00 | 0.70 | -8.88 | 226 |
| 19 | Hold BTC | benchmark | 91.63 | -8.37 | 0 | — | 0.15 | 0.20 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.73 | -9.27 | 102 | 21.6 | -16.46 | -6.10 | -17.40 | 78 |
| 22 | Agent | meta | 90.54 | -9.46 | 141 | 39.0 | -10.29 | -6.20 | -12.22 | 209 |
| 23 | Opening range 30m | breakout | 90.17 | -9.83 | 337 | 32.9 | -12.61 | -3.84 | -17.21 | 589 |
| 24 | Squeeze breakout · 1h | breakout | 89.59 | -10.41 | 61 | 23.0 | -7.80 | -2.62 | -13.79 | 88 |
| 25 | Parabolic SAR · 1h | trend | 88.54 | -11.46 | 150 | 26.7 | -14.09 | -3.28 | -17.40 | 242 |
| 26 | Donchian 55/20 · 1h | breakout | 88.41 | -11.59 | 60 | 13.3 | -14.60 | -3.29 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 88.33 | -11.66 | 35 | 37.1 | -22.42 | -4.58 | -23.13 | 61 |
| 28 | Daily: Bullish score | daily | 88.26 | -11.74 | 14 | 21.4 | -5.12 | -0.59 | -14.82 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.98 | -13.02 | 1 | 0.0 | -2.92 | -0.28 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Stochastic reversion · 1h | reversion | 84.85 | -15.15 | 241 | 46.9 | -23.82 | -4.78 | -26.17 | 390 |
| 32 | Volume breakout · 1h | breakout | 84.76 | -15.24 | 129 | 28.7 | -15.64 | -3.61 | -18.08 | 96 |
| 33 | Max aggression: 5-day momentum | meta | 84.71 | -15.29 | 15 | 40.0 | -29.63 | -1.96 | -36.71 | 25 |
| 34 | MFI reversion · 1h | reversion | 84.17 | -15.83 | 303 | 33.0 | -15.07 | -2.36 | -18.11 | 151 |
| 35 | Keltner breakout · 1h | breakout | 84.14 | -15.86 | 89 | 23.6 | -21.23 | -4.44 | -22.58 | 173 |
| 36 | Connors RSI(2) · 1h | reversion | 83.88 | -16.12 | 191 | 40.8 | -20.52 | -6.67 | -20.99 | 136 |
| 37 | ADX DI cross · 1h | trend | 83.29 | -16.71 | 148 | 18.2 | -18.16 | -3.56 | -21.38 | 250 |
| 38 | Opening range 15m | breakout | 82.88 | -17.12 | 411 | 30.2 | -17.99 | -5.23 | -20.73 | 721 |
| 39 | Bollinger breakout · 1h | breakout | 81.71 | -18.29 | 140 | 25.0 | -17.56 | -3.55 | -23.31 | 233 |
| 40 | Ichimoku · 1h | trend | 81.12 | -18.88 | 84 | 13.1 | -17.93 | -3.63 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 79.90 | -20.10 | 90 | 11.1 | -19.68 | -3.68 | -27.42 | 124 |
| 42 | CCI reversion · 1h | reversion | 79.27 | -20.73 | 268 | 44.8 | -25.32 | -4.00 | -27.71 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.58 | -21.42 | 224 | 38.4 | -27.39 | -5.33 | -30.13 | 376 |
| 44 | MACD zero-line · 1h | trend | 78.01 | -22.00 | 136 | 15.4 | -25.30 | -5.50 | -27.61 | 213 |
| 45 | Z-score reversion · 1h | reversion | 77.81 | -22.19 | 142 | 34.5 | -14.10 | -2.02 | -23.02 | 217 |
| 46 | Supertrend · 1h | trend | 77.81 | -22.19 | 141 | 12.8 | -27.84 | -5.32 | -29.54 | 223 |
| 47 | MACD cross · 1h | trend | 77.33 | -22.67 | 300 | 23.3 | -33.75 | -6.53 | -36.40 | 482 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.24 | -3.55 | -33.56 | 33 |
| 49 | Williams %R · 1h | reversion | 76.96 | -23.04 | 278 | 46.4 | -36.36 | -6.47 | -37.62 | 529 |
| 50 | RSI momentum · 1h | momentum | 76.46 | -23.54 | 136 | 12.5 | -28.31 | -5.47 | -30.39 | 213 |
| 51 | Heikin-Ashi · 1h | trend | 76.40 | -23.60 | 357 | 22.4 | -41.71 | -8.68 | -44.63 | 667 |
| 52 | Triple EMA stack · 1h | trend | 76.34 | -23.66 | 126 | 14.3 | -28.54 | -5.67 | -31.22 | 204 |
| 53 | OBV trend · 1h | momentum | 75.76 | -24.24 | 240 | 17.5 | -30.62 | -6.45 | -32.70 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.33 | -24.67 | 120 | 20.0 | -27.41 | -4.89 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.28 | -25.72 | 303 | 25.4 | -34.41 | -6.71 | -36.05 | 377 |
| 56 | RSI(14) reversion · 1h | reversion | 73.22 | -26.78 | 130 | 26.2 | -19.25 | -3.27 | -26.28 | 206 |
| 57 | Candlestick reversal · 1h | reversion | 71.45 | -28.55 | 356 | 28.9 | -34.59 | -6.32 | -38.30 | 551 |
| 58 | Agent (ML meta-label) | meta | 70.20 | -29.80 | 1348 | 21.6 | -13.87 | -2.72 | -16.94 | 293 |
| 59 | Three white soldiers | momentum | 69.12 | -30.88 | 415 | 16.1 | -46.29 | -21.71 | -46.29 | 617 |
| 60 | EMA 9/21 cross · 1h | trend | 69.11 | -30.89 | 219 | 9.6 | -37.08 | -7.47 | -38.82 | 328 |
| 61 | VWAP momentum · 1h | momentum | 68.69 | -31.31 | 700 | 21.6 | -53.46 | -10.50 | -56.37 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 68.25 | -31.75 | 23 | 30.4 | -32.81 | -1.86 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.17 | -98.96 | 5175 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.23 | -23.24 | -80.26 | 1405 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.31 | -44.32 | -93.37 | 2513 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.86 | -30.95 | -89.04 | 1909 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.00 | -36.68 | -91.07 | 2326 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.57 | -31.91 | -90.69 | 2221 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -52.12 | -97.73 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -58.83 | -96.23 | 3370 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.53 | -34.56 | -93.58 | 2395 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.67 | -34.40 | -82.05 | 1664 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.94 | -99.48 | 5849 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.97 | -43.82 | -93.01 | 2616 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.36 | -36.87 | -95.36 | 3355 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.46 | -99.80 | 6166 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.85 | -44.01 | -91.90 | 2261 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.38 | -26.32 | -74.81 | 1556 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -60.11 | -97.78 | 3529 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.44 | -98.66 | 4804 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.12 | -27.26 | -70.23 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.73 | -53.91 | -94.75 | 2772 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.92 | -37.74 | -84.97 | 1810 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.95 | -99.62 | 6292 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.12 | -29.83 | -88.25 | 2228 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.51 | -19.04 | -76.70 | 1694 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.05 | -36.23 | -90.08 | 2221 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.73 | -96.46 | 3803 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.27 | -52.43 | -89.29 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.63 | -25.46 | -65.64 | 818 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.36 | -24.67 | -74.12 | 1273 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.89 | -18.89 | -77.05 | 1584 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.80 | -48.83 | -96.80 | 4212 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -98.97 | -99.92 | 8219 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T17:50 | Agent (ML meta-label) | buy | GOOGL | 3.58 | — | entry |
| 2026-11-03T17:50 | Agent (ML meta-label) | sell | BITX | 3.58 | 0.01 | selected signal exited |
| 2026-11-03T17:45 | Agent (ML meta-label) | buy | BITX | 3.57 | — | following Z-score reversion |
| 2026-11-03T17:45 | Agent (ML meta-label) | sell | SQQQ | 3.53 | 0.01 | rebalance down |
| 2026-11-03T17:45 | Williams %R · 1h | buy | BITX | 6.40 | — | entry |
| 2026-11-03T17:45 | Stochastic reversion · 1h | buy | BITX | 7.06 | — | entry |
| 2026-11-03T17:40 | Agent (ML meta-label) | buy | SQQQ | 3.52 | — | rebalance up |
| 2026-11-03T17:40 | Agent (ML meta-label) | buy | MSTR | 3.51 | — | rebalance up |
| 2026-11-03T17:40 | Agent (ML meta-label) | sell | SOXL | 7.07 | -0.02 | selected signal exited |
| 2026-11-03T17:36 | Agent (ML meta-label) | buy | SOXL | 7.09 | — | following Connors RSI(2) |
| 2026-11-03T17:36 | Agent (ML meta-label) | buy | MSTR | 14.03 | — | entry |
| 2026-11-03T17:36 | Agent (ML meta-label) | sell | SQQQ | 3.59 | 0.01 | rebalance down |
| 2026-11-03T17:36 | Three white soldiers | sell | DOGE-USD | 17.20 | -0.11 | exit signal |
| 2026-11-03T17:30 | MFI reversion · 1h | buy | PLTR | 12.00 | — | entry signal |
| 2026-11-03T17:30 | MFI reversion · 1h | buy | GOOGL | 12.04 | — | entry signal |
| 2026-11-03T17:30 | MFI reversion · 1h | sell | UPRO | 4.81 | 0.01 | rebalance down |
| 2026-11-03T17:30 | MFI reversion · 1h | sell | LABU | 4.72 | 0.19 | rebalance down |
| 2026-11-03T17:30 | MFI reversion · 1h | sell | DOGE-USD | 4.83 | 0.01 | rebalance down |
| 2026-11-03T17:30 | MFI reversion · 1h | sell | BTC-USD | 4.83 | 0.00 | rebalance down |
| 2026-11-03T17:30 | MFI reversion · 1h | sell | AMZN | 4.85 | 0.11 | rebalance down |
| 2026-11-03T17:30 | Williams %R · 1h | buy | GOOGL | 7.00 | — | entry signal |
| 2026-11-03T17:30 | Williams %R · 1h | sell | META | 5.94 | 0.09 | exit signal |
| 2026-11-03T17:30 | Williams %R · 1h | sell | BITX | 5.94 | 0.05 | exit signal |
| 2026-11-03T17:30 | Stochastic reversion · 1h | sell | META | 3.30 | 0.05 | exit signal |
| 2026-11-03T17:30 | Stochastic reversion · 1h | sell | BITX | 4.59 | 0.00 | exit signal |
| 2026-11-03T17:30 | RSI(14) reversion · 1h | buy | PLTR | 6.10 | — | entry signal |
| 2026-11-03T17:30 | Candlestick reversal · 1h | buy | UPRO | 5.89 | — | entry signal |
| 2026-11-03T17:30 | Candlestick reversal · 1h | buy | SPY | 8.95 | — | entry signal |
| 2026-11-03T17:30 | Candlestick reversal · 1h | buy | ETHU | 7.36 | — | rebalance up |
| 2026-11-03T17:30 | Candlestick reversal · 1h | sell | MSTR | 5.48 | 0.13 | rebalance down |
| 2026-11-03T17:30 | Candlestick reversal · 1h | sell | GOOGL | 5.44 | 0.00 | rebalance down |
| 2026-11-03T17:30 | Candlestick reversal · 1h | sell | COIN | 5.96 | 0.36 | rebalance down |
| 2026-11-03T17:30 | Candlestick reversal · 1h | sell | AAPL | 5.32 | 0.00 | rebalance down |
| 2026-11-03T17:30 | ROC + volume · 1h | buy | AMZN | 7.36 | — | entry |
| 2026-11-03T17:30 | ROC + volume · 1h | sell | SQQQ | 7.36 | -0.04 | exit signal |
| 2026-11-03T17:30 | MACD zero-line · 1h | buy | AMZN | 6.45 | — | entry signal |
| 2026-11-03T17:30 | MACD zero-line · 1h | sell | DOGE-USD | 6.45 | -0.02 | rebalance down |
| 2026-11-03T17:30 | MACD cross · 1h | buy | TQQQ | 4.56 | — | entry signal |
| 2026-11-03T17:30 | MACD cross · 1h | buy | SOXL | 4.56 | — | entry signal |
| 2026-11-03T17:30 | MACD cross · 1h | buy | NVDA | 4.56 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 17:50:05.000155+00:00 -> 2026-11-03 18:00:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 17:50:05.000155+00:00 -> 2026-11-03 18:00:05.000155+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 17:50:05.000155+00:00 -> 2026-11-03 18:00:05.000155+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
