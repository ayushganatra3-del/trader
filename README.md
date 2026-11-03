# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-03T18:21:05.000150+00:00 · 46424 ticks

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

Today: 25755 decisions in 2664 calls, $0.3251 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-03T18:21 | 2 / 18 / 10 | cash |  |
| Breezy | 2026-11-03T18:21 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-11-03T18:21 | 4 / 25 / 1 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| Candlestick reversal | LABU | 2.07 | +6.93% | 12 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| VWAP reversion | COIN | 1.90 | +3.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 109.39 | 9.38 | 0 | — | 10.54 | 4.55 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 9.33 | 2.80 | -4.91 | 25 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 1.23 | 0.53 | -5.37 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.82 | 0.82 | 26 | 26.9 | 8.53 | 2.17 | -6.54 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -12.85 | -3.55 | -13.12 | 142 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.75 | -1.89 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 97.06 | -2.94 | 0 | — | -1.22 | -0.60 | -3.94 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 96.55 | -3.45 | 5 | 40.0 | 2.82 | 0.75 | -7.93 | 8 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.45 | -3.55 | 107 | 34.6 | 4.44 | 2.13 | -3.79 | 94 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 95.94 | -4.05 | 0 | — | -0.73 | -0.20 | -6.60 | 1 |
| 14 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -2.11 | -1.61 | -5.33 | 29 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.44 | -5.56 | 0 | — | -2.72 | -1.02 | -7.64 | 1 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -5.15 | -3.05 | -8.68 | 185 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 94.11 | -5.89 | 0 | — | -5.27 | -2.05 | -6.35 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | 1.50 | 0.54 | -9.15 | 226 |
| 19 | Hold BTC | benchmark | 91.51 | -8.49 | 0 | — | 0.18 | 0.20 | -12.65 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.90 | -2.04 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.73 | -9.27 | 102 | 21.6 | -16.46 | -6.10 | -17.40 | 78 |
| 22 | Agent | meta | 90.54 | -9.46 | 141 | 39.0 | -10.30 | -6.21 | -12.22 | 208 |
| 23 | Opening range 30m | breakout | 90.18 | -9.82 | 337 | 32.9 | -12.65 | -3.86 | -17.21 | 591 |
| 24 | Squeeze breakout · 1h | breakout | 89.51 | -10.49 | 61 | 23.0 | -7.90 | -2.64 | -13.79 | 87 |
| 25 | Parabolic SAR · 1h | trend | 88.69 | -11.30 | 150 | 26.7 | -13.77 | -3.18 | -17.40 | 241 |
| 26 | Copy: Insider buying | copy | 88.47 | -11.53 | 35 | 37.1 | -22.29 | -4.55 | -23.13 | 61 |
| 27 | Donchian 55/20 · 1h | breakout | 88.41 | -11.59 | 60 | 13.3 | -14.61 | -3.29 | -18.06 | 100 |
| 28 | Daily: Bullish score | daily | 88.30 | -11.70 | 14 | 21.4 | -5.24 | -0.61 | -14.82 | 15 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 87.01 | -12.99 | 1 | 0.0 | -2.91 | -0.28 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 86.63 | -13.37 | 66 | 33.3 | -11.85 | -3.93 | -14.77 | 94 |
| 31 | Stochastic reversion · 1h | reversion | 84.89 | -15.11 | 241 | 46.9 | -23.77 | -4.76 | -26.18 | 390 |
| 32 | Max aggression: 5-day momentum | meta | 84.80 | -15.20 | 15 | 40.0 | -29.55 | -1.96 | -36.71 | 25 |
| 33 | Volume breakout · 1h | breakout | 84.71 | -15.29 | 129 | 28.7 | -15.49 | -3.57 | -18.08 | 96 |
| 34 | MFI reversion · 1h | reversion | 84.36 | -15.64 | 305 | 33.1 | -14.82 | -2.30 | -18.14 | 149 |
| 35 | Keltner breakout · 1h | breakout | 84.12 | -15.88 | 89 | 23.6 | -21.41 | -4.46 | -22.26 | 173 |
| 36 | Connors RSI(2) · 1h | reversion | 83.90 | -16.10 | 191 | 40.8 | -20.50 | -6.67 | -20.99 | 136 |
| 37 | ADX DI cross · 1h | trend | 83.36 | -16.64 | 148 | 18.2 | -18.08 | -3.52 | -21.39 | 251 |
| 38 | Opening range 15m | breakout | 82.96 | -17.04 | 411 | 30.2 | -17.98 | -5.23 | -20.73 | 724 |
| 39 | Bollinger breakout · 1h | breakout | 81.62 | -18.38 | 140 | 25.0 | -17.68 | -3.58 | -23.31 | 233 |
| 40 | Ichimoku · 1h | trend | 81.14 | -18.86 | 84 | 13.1 | -17.91 | -3.62 | -25.58 | 119 |
| 41 | EMA 20/50 cross · 1h | trend | 80.00 | -20.00 | 90 | 11.1 | -19.33 | -3.59 | -27.42 | 125 |
| 42 | CCI reversion · 1h | reversion | 79.40 | -20.60 | 268 | 44.8 | -25.17 | -3.96 | -27.71 | 451 |
| 43 | Bollinger reversion · 1h | reversion | 78.47 | -21.53 | 224 | 38.4 | -27.58 | -5.40 | -30.25 | 376 |
| 44 | MACD zero-line · 1h | trend | 77.96 | -22.04 | 136 | 15.4 | -25.29 | -5.50 | -27.61 | 213 |
| 45 | Supertrend · 1h | trend | 77.84 | -22.16 | 141 | 12.8 | -27.83 | -5.32 | -29.54 | 223 |
| 46 | Z-score reversion · 1h | reversion | 77.73 | -22.27 | 142 | 34.5 | -14.20 | -2.04 | -23.02 | 217 |
| 47 | MACD cross · 1h | trend | 77.28 | -22.72 | 300 | 23.3 | -33.80 | -6.55 | -36.40 | 482 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -27.27 | -3.56 | -33.57 | 33 |
| 49 | Williams %R · 1h | reversion | 77.01 | -22.99 | 278 | 46.4 | -36.34 | -6.46 | -37.65 | 530 |
| 50 | RSI momentum · 1h | momentum | 76.48 | -23.52 | 136 | 12.5 | -28.55 | -5.54 | -30.39 | 213 |
| 51 | Triple EMA stack · 1h | trend | 76.32 | -23.68 | 126 | 14.3 | -28.57 | -5.68 | -31.22 | 204 |
| 52 | Heikin-Ashi · 1h | trend | 76.24 | -23.76 | 357 | 22.4 | -41.78 | -8.70 | -44.63 | 667 |
| 53 | OBV trend · 1h | momentum | 75.92 | -24.08 | 240 | 17.5 | -30.49 | -6.41 | -32.71 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 75.29 | -24.71 | 120 | 20.0 | -28.91 | -5.30 | -30.44 | 208 |
| 55 | ROC + volume · 1h | momentum | 74.17 | -25.83 | 304 | 25.7 | -35.08 | -6.90 | -35.98 | 376 |
| 56 | RSI(14) reversion · 1h | reversion | 73.17 | -26.83 | 130 | 26.2 | -19.57 | -3.36 | -26.28 | 207 |
| 57 | Candlestick reversal · 1h | reversion | 71.27 | -28.73 | 357 | 28.9 | -34.73 | -6.40 | -38.29 | 551 |
| 58 | Agent (ML meta-label) | meta | 70.10 | -29.90 | 1354 | 21.7 | -12.24 | -2.42 | -16.61 | 280 |
| 59 | EMA 9/21 cross · 1h | trend | 69.15 | -30.86 | 219 | 9.6 | -37.06 | -7.47 | -38.82 | 328 |
| 60 | Three white soldiers | momentum | 69.10 | -30.90 | 415 | 16.1 | -46.35 | -21.69 | -46.35 | 618 |
| 61 | VWAP momentum · 1h | momentum | 68.63 | -31.37 | 700 | 21.6 | -53.46 | -10.50 | -56.37 | 1236 |
| 62 | Max aggression: 1-day momentum | meta | 68.32 | -31.68 | 23 | 30.4 | -32.74 | -1.86 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.95 | -44.19 | -98.96 | 5165 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.26 | -23.36 | -80.27 | 1412 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.32 | -44.33 | -93.42 | 2522 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.79 | -30.69 | -89.04 | 1905 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.95 | -36.27 | -91.06 | 2328 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.58 | -31.93 | -90.70 | 2221 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.72 | -52.00 | -97.73 | 3460 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.17 | -57.40 | -96.17 | 3381 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.67 | -34.72 | -93.67 | 2405 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.63 | -34.13 | -82.06 | 1663 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -51.74 | -99.48 | 5845 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.98 | -43.86 | -93.01 | 2623 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.34 | -36.76 | -95.36 | 3354 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.80 | -71.21 | -99.80 | 6175 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -43.85 | -91.88 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.60 | -26.28 | -74.95 | 1559 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.77 | -60.06 | -97.78 | 3532 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -59.59 | -98.66 | 4805 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.08 | -27.08 | -70.23 | 1200 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.74 | -53.92 | -94.75 | 2776 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.66 | -36.70 | -84.75 | 1808 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -68.69 | -99.61 | 6280 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.11 | -29.78 | -88.24 | 2227 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.50 | -19.04 | -76.68 | 1689 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.06 | -36.00 | -90.13 | 2222 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.45 | -49.58 | -96.45 | 3800 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -54.02 | -89.42 | 2134 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -64.78 | -25.45 | -65.73 | 821 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.33 | -24.59 | -74.13 | 1272 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.89 | -18.89 | -77.06 | 1583 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.78 | -48.46 | -96.80 | 4212 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -97.51 | -99.92 | 8220 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | TSLA | 3.96 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | SQQQ | 4.04 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | MSTR | 4.01 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | ETHU | 4.01 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | buy | BITX | 9.71 | — | rebalance up |
| 2026-11-03T18:15 | Agent (ML meta-label) | sell | UPRO | 5.08 | -0.00 | selected signal exited |
| 2026-11-03T18:15 | Agent (ML meta-label) | sell | SOXL | 10.08 | -0.06 | selected signal exited |
| 2026-11-03T18:15 | Agent (ML meta-label) | sell | GOOGL | 10.05 | 0.02 | selected signal exited |
| 2026-11-03T18:15 | Opening range 15m | buy | AMZN | 4.34 | — | entry |
| 2026-11-03T18:15 | Opening range 15m | sell | MSFT | 4.34 | 0.07 | rebalance down |
| 2026-11-03T18:10 | Agent (ML meta-label) | buy | UPRO | 5.08 | — | entry |
| 2026-11-03T18:10 | Agent (ML meta-label) | buy | SOXL | 10.14 | — | following Connors RSI(2) |
| 2026-11-03T18:10 | Agent (ML meta-label) | sell | TQQQ | 10.04 | 0.03 | selected signal exited |
| 2026-11-03T18:10 | Agent (ML meta-label) | sell | BITX | 5.71 | 0.01 | rebalance down |
| 2026-11-03T18:10 | Donchian 20/10 · 1h | buy | SQQQ | 3.78 | — | rebalance up |
| 2026-11-03T18:10 | Three white soldiers | buy | IWM | 17.28 | — | entry signal |
| 2026-11-03T18:05 | Agent (ML meta-label) | buy | TQQQ | 10.01 | — | entry |
| 2026-11-03T18:05 | Agent (ML meta-label) | buy | MSTR | 10.02 | — | entry |
| 2026-11-03T18:05 | Agent (ML meta-label) | buy | GOOGL | 10.02 | — | entry |
| 2026-11-03T18:05 | Agent (ML meta-label) | buy | BITX | 10.02 | — | following Z-score reversion |
| 2026-11-03T18:05 | Agent (ML meta-label) | sell | TSLA | 7.53 | -0.02 | rebalance down |
| 2026-11-03T18:05 | Agent (ML meta-label) | sell | SQQQ | 7.52 | -0.02 | rebalance down |
| 2026-11-03T18:05 | Agent (ML meta-label) | sell | ETHU | 7.52 | 0.01 | rebalance down |
| 2026-11-03T18:05 | MFI reversion · 1h | buy | PLTR | 4.83 | — | rebalance up |
| 2026-11-03T18:05 | MFI reversion · 1h | buy | LABU | 4.86 | — | rebalance up |
| 2026-11-03T18:05 | MFI reversion · 1h | buy | DOGE-USD | 4.82 | — | rebalance up |
| 2026-11-03T18:05 | MFI reversion · 1h | buy | BTC-USD | 4.81 | — | rebalance up |
| 2026-11-03T18:05 | MFI reversion · 1h | buy | AMZN | 4.75 | — | rebalance up |
| 2026-11-03T18:05 | MFI reversion · 1h | sell | UPRO | 12.04 | 0.04 | target is flat |
| 2026-11-03T17:55 | Agent (rotation) | sell | BITX | 7.84 | -0.01 | selected signal exited |
| 2026-11-03T17:55 | Agent (ML meta-label) | sell | GOOGL | 17.51 | -0.04 | selected signal exited |
| 2026-11-03T17:55 | MFI reversion · 1h | sell | GOOGL | 12.03 | -0.01 | target is flat |
| 2026-11-03T17:55 | Candlestick reversal · 1h | buy | ETHU | 4.61 | — | entry |
| 2026-11-03T17:55 | ROC + volume · 1h | sell | AMZN | 7.36 | 0.01 | target is flat |
| 2026-11-03T17:55 | Gap and go | sell | BITX | 23.13 | -0.02 | target is flat |
| 2026-11-03T17:52 | Agent (ML meta-label) | buy | SQQQ | 3.59 | — | rebalance up |
| 2026-11-03T17:52 | Agent (ML meta-label) | buy | GOOGL | 13.97 | — | rebalance up |
| 2026-11-03T17:52 | Agent (ML meta-label) | sell | MSTR | 17.57 | 0.02 | selected signal exited |
| 2026-11-03T17:52 | Candlestick reversal · 1h | buy | UPRO | 4.33 | — | rebalance up |
| 2026-11-03T17:52 | Candlestick reversal · 1h | sell | ETHU | 8.94 | -0.01 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-05 18:21:05.000150+00:00 -> 2026-11-03 18:31:05.000150+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-05 18:21:05.000150+00:00 -> 2026-11-03 18:31:05.000150+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-05 18:21:05.000150+00:00 -> 2026-11-03 18:31:05.000150+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
