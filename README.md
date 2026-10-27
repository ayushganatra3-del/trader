# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T18:05:05.000133+00:00 · 38124 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.04 (-9.96%)

Closed trades 114, win rate 39.5%, fees £3.46, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 28957 decisions in 2645 calls, $0.3610 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T18:05 | 5 / 10 / 14 | cash |  |
| Breezy | 2026-10-27T18:05 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-27T18:05 | 5 / 21 / 3 | COIN 63% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.68 | 7.68 | 0 | — | 8.16 | 4.07 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.34 | 6.34 | 14 | 71.4 | 3.65 | 1.20 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.09 | 5.09 | 19 | 47.4 | 7.79 | 2.52 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.75 | 0.75 | 0 | — | 2.31 | 1.10 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.92 | -3.86 | -14.07 | 150 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.52 | -0.48 | 0 | — | 0.28 | 0.21 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.89 | -1.11 | 82 | 35.4 | 8.06 | 3.73 | -2.29 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.86 | -2.14 | 0 | — | -0.48 | -0.15 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.18 | -2.01 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.22 | -3.78 | 122 | 31.1 | -2.40 | -1.36 | -6.39 | 180 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.01 | -3.99 | 0 | — | -5.80 | -2.36 | -7.83 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.41 | 1.05 | -7.93 | 8 |
| 17 | Hold BTC | benchmark | 95.57 | -4.43 | 0 | — | 2.25 | 0.54 | -9.28 | 1 |
| 18 | Gap and go | momentum | 95.56 | -4.45 | 115 | 27.8 | 5.19 | 1.69 | -8.76 | 210 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 20 | Opening range 30m | breakout | 93.59 | -6.41 | 272 | 34.2 | -9.71 | -2.88 | -17.21 | 593 |
| 21 | Donchian 55/20 · 1h | breakout | 93.52 | -6.48 | 49 | 16.3 | -13.07 | -2.94 | -15.45 | 97 |
| 22 | Trend pullback · 1h | trend | 93.46 | -6.54 | 96 | 22.9 | -21.96 | -7.01 | -22.19 | 116 |
| 23 | Copy: Cathie Wood (ARKK) | copy | 92.54 | -7.46 | 0 | — | -1.58 | -0.09 | -14.57 | 1 |
| 24 | Copy: Insider buying | copy | 92.11 | -7.89 | 27 | 37.0 | -19.92 | -3.92 | -22.94 | 63 |
| 25 | Parabolic SAR · 1h | trend | 91.93 | -8.07 | 121 | 25.6 | -20.55 | -5.09 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.87 | -8.13 | 13 | 15.4 | -18.20 | -3.52 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.64 | -8.36 | 120 | 18.3 | -14.24 | -3.10 | -15.79 | 270 |
| 28 | Daily: Bullish score | daily | 91.27 | -8.73 | 11 | 18.2 | -6.53 | -0.78 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.28 | -2.17 | -16.91 | 1 |
| 30 | Max aggression: 5-day momentum | meta | 90.99 | -9.01 | 12 | 41.7 | -14.52 | -1.30 | -27.23 | 25 |
| 31 | Squeeze breakout · 1h | breakout | 90.82 | -9.18 | 52 | 23.1 | -4.69 | -1.22 | -12.18 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.10 | -9.90 | 108 | 25.9 | -11.93 | -2.45 | -16.00 | 115 |
| 33 | Agent | meta | 90.04 | -9.96 | 114 | 39.5 | -11.42 | -7.17 | -12.47 | 223 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 109 | 26.6 | -12.93 | -2.55 | -18.15 | 249 |
| 35 | Agent (aggressive) | meta | 88.18 | -11.82 | 57 | 36.8 | -10.87 | -3.56 | -14.77 | 98 |
| 36 | Stochastic reversion · 1h | reversion | 87.81 | -12.19 | 205 | 47.3 | -21.10 | -3.93 | -22.35 | 389 |
| 37 | Opening range 15m | breakout | 87.06 | -12.94 | 338 | 30.8 | -13.48 | -3.74 | -17.87 | 719 |
| 38 | Keltner breakout · 1h | breakout | 87.05 | -12.95 | 74 | 23.0 | -20.04 | -3.88 | -23.13 | 188 |
| 39 | Z-score reversion · 1h | reversion | 86.62 | -13.38 | 125 | 36.0 | -12.88 | -2.05 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.60 | -14.40 | 114 | 14.0 | -25.58 | -5.20 | -28.20 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.19 | -14.81 | 176 | 40.9 | -24.26 | -7.38 | -24.88 | 195 |
| 42 | RSI momentum · 1h | momentum | 84.88 | -15.12 | 104 | 15.4 | -21.45 | -4.35 | -24.15 | 212 |
| 43 | MACD cross · 1h | trend | 84.26 | -15.74 | 244 | 22.1 | -26.77 | -5.04 | -28.72 | 473 |
| 44 | EMA 20/50 cross · 1h | trend | 84.06 | -15.94 | 73 | 11.0 | -23.15 | -4.71 | -24.49 | 133 |
| 45 | Ichimoku · 1h | trend | 83.76 | -16.24 | 68 | 11.8 | -20.13 | -4.12 | -24.73 | 111 |
| 46 | MFI reversion · 1h | reversion | 83.49 | -16.52 | 273 | 32.2 | -16.19 | -2.50 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.27 | -16.73 | 101 | 14.9 | -28.31 | -5.42 | -31.09 | 202 |
| 48 | CCI reversion · 1h | reversion | 82.28 | -17.73 | 230 | 45.2 | -23.56 | -3.35 | -28.06 | 465 |
| 49 | Williams %R · 1h | reversion | 81.80 | -18.20 | 232 | 47.0 | -35.27 | -5.95 | -36.08 | 537 |
| 50 | Donchian 20/10 · 1h | breakout | 81.78 | -18.22 | 99 | 20.2 | -24.48 | -4.70 | -26.91 | 222 |
| 51 | MACD zero-line · 1h | trend | 81.22 | -18.78 | 111 | 15.3 | -23.27 | -4.89 | -24.78 | 228 |
| 52 | Bollinger reversion · 1h | reversion | 80.78 | -19.22 | 182 | 37.4 | -29.11 | -5.95 | -30.19 | 364 |
| 53 | Agent (ML meta-label) | meta | 80.63 | -19.37 | 977 | 20.5 | -5.18 | -0.81 | -17.41 | 337 |
| 54 | RSI(14) reversion · 1h | reversion | 80.18 | -19.82 | 107 | 27.1 | -19.88 | -3.82 | -24.95 | 185 |
| 55 | OBV trend · 1h | momentum | 80.16 | -19.84 | 209 | 17.7 | -30.99 | -6.60 | -32.76 | 296 |
| 56 | ROC + volume · 1h | momentum | 79.01 | -20.99 | 259 | 25.9 | -31.69 | -6.21 | -33.27 | 386 |
| 57 | Heikin-Ashi · 1h | trend | 78.23 | -21.77 | 295 | 22.7 | -43.34 | -9.56 | -44.60 | 671 |
| 58 | Three white soldiers | momentum | 77.35 | -22.65 | 321 | 19.0 | -44.55 | -20.14 | -45.08 | 607 |
| 59 | Candlestick reversal · 1h | reversion | 77.14 | -22.86 | 285 | 29.5 | -34.69 | -6.69 | -35.35 | 554 |
| 60 | VWAP momentum · 1h | momentum | 76.76 | -23.24 | 571 | 22.2 | -49.23 | -10.69 | -51.08 | 1237 |
| 61 | EMA 9/21 cross · 1h | trend | 76.49 | -23.51 | 176 | 10.8 | -30.90 | -6.66 | -32.65 | 338 |
| 62 | Max aggression: 1-day momentum | meta | 71.88 | -28.12 | 20 | 30.0 | -38.18 | -2.49 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 53.98 | -46.02 | 805 | 22.4 | -74.43 | -26.07 | -75.09 | 1579 |
| 64 | Volume breakout | breakout | 52.60 | -47.40 | 482 | 12.9 | -62.91 | -25.44 | -63.54 | 808 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -42.33 | -98.87 | 5131 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.27 | -23.26 | -80.03 | 1413 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.68 | -43.41 | -93.79 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.21 | -30.25 | -89.36 | 1922 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.41 | -37.12 | -91.56 | 2342 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.25 | -31.73 | -90.30 | 2180 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -48.65 | -97.89 | 3503 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -53.23 | -96.19 | 3372 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.13 | -36.22 | -94.13 | 2455 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.35 | -32.93 | -82.64 | 1686 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -51.63 | -99.42 | 5765 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -40.34 | -92.92 | 2626 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.41 | -38.47 | -95.41 | 3386 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -69.40 | -99.78 | 6167 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.21 | -43.23 | -92.34 | 2322 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.78 | -60.59 | -97.78 | 3596 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.64 | -98.66 | 4793 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.84 | -27.94 | -68.70 | 1180 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.60 | -53.36 | -94.67 | 2769 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.29 | -37.56 | -84.58 | 1818 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -63.93 | -99.61 | 6299 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.23 | -28.62 | -88.27 | 2225 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.78 | -19.05 | -77.00 | 1680 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.57 | -36.37 | -90.69 | 2280 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.89 | -96.28 | 3821 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.05 | -47.29 | -90.10 | 2132 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.98 | -24.57 | -73.50 | 1285 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.17 | -17.90 | -76.40 | 1582 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.38 | -96.55 | 4194 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -92.22 | -99.92 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T18:01 | Candlestick reversal · 1h | buy | GOOGL | 4.35 | — | rebalance up |
| 2026-10-27T18:01 | Candlestick reversal · 1h | buy | BITX | 5.74 | — | rebalance up |
| 2026-10-27T18:01 | Candlestick reversal · 1h | sell | SOL-USD | 12.82 | -0.04 | exit signal |
| 2026-10-27T18:01 | ROC + volume | sell | ETHU | 13.45 | -0.07 | exit signal |
| 2026-10-27T17:55 | Agent (ML meta-label) | buy | SOXL | 4.04 | — | rebalance up |
| 2026-10-27T17:55 | Agent (ML meta-label) | sell | MSFT | 20.16 | -0.02 | selected signal exited |
| 2026-10-27T17:55 | Agent (ML meta-label) | sell | META | 5.39 | -0.01 | selected signal exited |
| 2026-10-27T17:50 | Agent (ML meta-label) | buy | MSFT | 20.18 | — | following MACD zero-line |
| 2026-10-27T17:50 | Agent (ML meta-label) | buy | META | 5.40 | — | following VWAP reversion |
| 2026-10-27T17:40 | Day trade: Stocks in Play ORB | buy | SOXL | 24.75 | — | entry |
| 2026-10-27T17:40 | Agent (aggressive) | sell | PLTR | 44.20 | 0.21 | selected signal exited |
| 2026-10-27T17:40 | Agent | sell | PLTR | 18.07 | 0.09 | selected signal exited |
| 2026-10-27T17:40 | MFI reversion · 1h | sell | GOOGL | 20.88 | -0.02 | target is flat |
| 2026-10-27T17:40 | VWAP momentum · 1h | buy | SPY | 3.34 | — | entry |
| 2026-10-27T17:40 | VWAP momentum · 1h | sell | PLTR | 3.34 | -0.00 | target is flat |
| 2026-10-27T17:40 | Gap and go | sell | SOXL | 24.07 | 0.20 | target is flat |
| 2026-10-27T17:36 | Agent (ML meta-label) | sell | UPRO | 16.03 | -0.02 | selected signal exited |
| 2026-10-27T17:36 | Agent (ML meta-label) | sell | PLTR | 16.14 | -0.02 | selected signal exited |
| 2026-10-27T17:36 | Agent (ML meta-label) | sell | NVDA | 16.14 | -0.02 | selected signal exited |
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | UPRO | 16.05 | — | entry |
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | PLTR | 16.16 | — | following VWAP momentum |
| 2026-10-27T17:35 | Agent (ML meta-label) | buy | NVDA | 16.16 | — | entry |
| 2026-10-27T17:35 | Agent (ML meta-label) | sell | SOXL | 4.08 | 0.08 | rebalance down |
| 2026-10-27T17:35 | Agent (ML meta-label) | sell | IWM | 20.18 | -0.01 | selected signal exited |
| 2026-10-27T17:35 | Volume breakout | sell | DOGE-USD | 13.06 | -0.12 | exit signal |
| 2026-10-27T17:30 | Agent (ML meta-label) | buy | SOXL | 4.05 | — | rebalance up |
| 2026-10-27T17:30 | Agent (ML meta-label) | buy | IWM | 8.08 | — | rebalance up |
| 2026-10-27T17:30 | Agent (ML meta-label) | sell | NVDA | 20.11 | -0.07 | selected signal exited |
| 2026-10-27T17:30 | Agent (ML meta-label) | sell | AMD | 16.13 | -0.03 | selected signal exited |
| 2026-10-27T17:30 | Stochastic reversion · 1h | buy | SQQQ | 21.98 | — | entry signal |
| 2026-10-27T17:30 | Bollinger reversion · 1h | buy | SQQQ | 20.22 | — | entry signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | buy | COIN | 12.91 | — | entry signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | sell | NVDA | 6.83 | -0.02 | exit signal |
| 2026-10-27T17:30 | Candlestick reversal · 1h | sell | MSFT | 11.01 | 0.00 | exit signal |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | SOL-USD | 3.20 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | PLTR | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | MSTR | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | buy | MSFT | 3.35 | — | entry |
| 2026-10-27T17:30 | VWAP momentum · 1h | sell | NVDA | 4.75 | 0.04 | exit signal |
| 2026-10-27T17:30 | VWAP momentum · 1h | sell | AMZN | 4.26 | 0.04 | target is flat |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 18:05:05.000133+00:00 -> 2026-10-27 18:15:05.000133+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
