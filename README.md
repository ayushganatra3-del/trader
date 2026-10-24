# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-24T18:10:05.000123+00:00 · 34531 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 13776 decisions in 2757 calls, $0.1928 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-24T18:10 | 4 / 1 / 0 | cash |  |
| Breezy | 2026-10-24T18:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-24T18:10 | 4 / 1 / 0 | ETH-USD 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |
| RSI(14) reversion | TSLA | 1.70 | +3.98% | 7 |
| Opening range 30m | PLTR | 1.69 | +3.38% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.17 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.19 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.97 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.03 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.61 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -12.07 | -3.37 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 3.01 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.37 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.20 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.34 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.86 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.03 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 94.90 | -5.10 | 0 | — | -0.19 | 0.14 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.74 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -16.22 | -3.12 | -21.83 | 67 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.58 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -7.01 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.53 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.45 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.37 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.89 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.38 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.83 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.37 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.23 | -8.77 | 108 | 18.5 | -11.79 | -2.40 | -14.69 | 256 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.04 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.75 | -2.80 | -16.90 | 115 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.77 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.77 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 89.03 | -10.97 | 105 | 27.6 | -12.06 | -2.37 | -16.40 | 240 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.26 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.93 | -3.96 | -22.47 | 390 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.76 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.50 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.67 | -17.87 | 703 |
| 40 | Supertrend · 1h | trend | 85.63 | -14.37 | 109 | 14.7 | -24.13 | -5.06 | -26.68 | 212 |
| 41 | RSI momentum · 1h | momentum | 85.62 | -14.38 | 101 | 15.8 | -21.39 | -4.55 | -23.32 | 215 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.99 | -26.96 | 196 |
| 43 | MACD cross · 1h | trend | 84.10 | -15.90 | 223 | 22.9 | -23.74 | -4.76 | -26.88 | 457 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.78 | -25.24 | 110 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.18 | -28.32 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.37 | -16.63 | 108 | 33.3 | -15.91 | -2.71 | -21.48 | 204 |
| 47 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.70 | -4.53 | -25.14 | 218 |
| 48 | MFI reversion · 1h | reversion | 81.36 | -18.64 | 260 | 31.5 | -18.09 | -2.93 | -20.54 | 147 |
| 49 | Donchian 20/10 · 1h | breakout | 81.26 | -18.73 | 97 | 19.6 | -24.19 | -4.66 | -27.15 | 216 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.39 | -6.88 | -32.91 | 305 |
| 51 | Three white soldiers | momentum | 80.95 | -19.05 | 277 | 19.9 | -43.71 | -20.51 | -43.82 | 589 |
| 52 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.21 | -6.48 | -36.69 | 531 |
| 53 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.98 | -6.70 | -32.19 | 372 |
| 54 | CCI reversion · 1h | reversion | 79.79 | -20.21 | 202 | 42.1 | -27.11 | -4.08 | -28.17 | 458 |
| 55 | Agent (ML meta-label) | meta | 79.44 | -20.56 | 860 | 18.6 | -13.51 | -2.42 | -17.32 | 386 |
| 56 | Heikin-Ashi · 1h | trend | 78.64 | -21.36 | 271 | 22.9 | -43.24 | -10.07 | -43.93 | 653 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.38 | -6.05 | -31.55 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 77.02 | -22.98 | 161 | 11.8 | -30.34 | -6.19 | -33.63 | 318 |
| 59 | Candlestick reversal · 1h | reversion | 76.89 | -23.11 | 259 | 28.2 | -35.66 | -6.77 | -36.26 | 550 |
| 60 | RSI(14) reversion · 1h | reversion | 76.46 | -23.54 | 97 | 21.6 | -16.72 | -3.11 | -24.41 | 194 |
| 61 | VWAP momentum · 1h | momentum | 75.45 | -24.55 | 528 | 21.0 | -50.90 | -11.74 | -51.04 | 1224 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.95 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 57.30 | -42.70 | 709 | 22.6 | -74.69 | -26.85 | -74.70 | 1548 |
| 64 | Volume breakout | breakout | 56.85 | -43.16 | 420 | 13.1 | -61.38 | -25.84 | -61.38 | 771 |
| 65 | Squeeze breakout | breakout | 53.28 | -46.72 | 553 | 14.1 | -66.70 | -28.67 | -66.76 | 1151 |
| 66 | Donchian 55/20 | breakout | 52.98 | -47.02 | 566 | 19.1 | -71.55 | -23.25 | -71.69 | 1250 |
| 67 | EMA 20/50 cross | trend | 51.38 | -48.62 | 626 | 20.0 | -79.07 | -23.79 | -79.35 | 1414 |
| 68 | RSI(14) reversion | reversion | 51.34 | -48.66 | 851 | 26.2 | -77.30 | -20.08 | -77.58 | 1692 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.71 | -45.04 | -98.73 | 5048 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -46.57 | -93.92 | 2518 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.83 | -30.78 | -88.96 | 1892 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.38 | -38.83 | -91.44 | 2320 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.32 | -30.51 | -90.37 | 2147 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -55.40 | -97.84 | 3498 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -60.47 | -96.10 | 3344 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.74 | -34.49 | -93.77 | 2427 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.91 | -36.10 | -82.96 | 1687 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -56.01 | -99.41 | 5760 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.42 | -42.59 | -92.48 | 2591 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.28 | -38.80 | -95.29 | 3350 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -81.35 | -99.76 | 6130 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -46.20 | -92.32 | 2333 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -62.66 | -97.56 | 3526 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.57 | -61.48 | -98.60 | 4763 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.37 | -59.05 | -94.41 | 2749 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.73 | -38.68 | -83.80 | 1770 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.57 | -68.80 | -99.58 | 6221 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.06 | -29.40 | -88.18 | 2216 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.51 | -38.53 | -90.61 | 2260 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.18 | -49.22 | -96.20 | 3785 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.74 | -51.71 | -89.86 | 2107 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.94 | -18.02 | -76.42 | 1576 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.29 | -49.72 | -96.35 | 4158 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -108.83 | -99.91 | 8181 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-24T18:05 | EMA 20/50 cross | buy | BTC-USD | 12.85 | — | entry signal |
| 2026-10-24T18:00 | MFI reversion · 1h | buy | ETH-USD | 20.18 | — | entry signal |
| 2026-10-24T18:00 | CCI reversion · 1h | buy | XRP-USD | 3.99 | — | entry signal |
| 2026-10-24T18:00 | MACD cross · 1h | buy | XRP-USD | 14.02 | — | entry signal |
| 2026-10-24T18:00 | ROC + volume | sell | XRP-USD | 14.26 | -0.09 | exit signal |
| 2026-10-24T17:55 | EMA 20/50 cross | buy | XRP-USD | 12.86 | — | entry signal |
| 2026-10-24T17:20 | RSI(14) reversion | sell | ETH-USD | 12.86 | 0.00 | exit signal |
| 2026-10-24T17:05 | ROC + volume | buy | XRP-USD | 14.34 | — | entry signal |
| 2026-10-24T17:00 | Agent (ML meta-label) | buy | DOGE-USD | 4.18 | — | entry |
| 2026-10-24T17:00 | Z-score reversion · 1h | buy | XRP-USD | 8.13 | — | entry signal |
| 2026-10-24T17:00 | RSI(14) reversion · 1h | buy | XRP-USD | 8.22 | — | entry signal |
| 2026-10-24T17:00 | RSI(14) reversion · 1h | buy | SOL-USD | 8.50 | — | entry signal |
| 2026-10-24T17:00 | RSI(14) reversion · 1h | buy | DOGE-USD | 8.50 | — | entry signal |
| 2026-10-24T17:00 | RSI(14) reversion · 1h | buy | BTC-USD | 8.50 | — | entry signal |
| 2026-10-24T16:55 | ROC + volume | buy | BTC-USD | 14.35 | — | entry signal |
| 2026-10-24T16:50 | RSI(14) reversion | sell | SOL-USD | 10.28 | 0.04 | exit signal |
| 2026-10-24T16:50 | RSI(14) reversion | sell | DOGE-USD | 12.85 | 0.05 | exit signal |
| 2026-10-24T16:50 | RSI(14) reversion | sell | BTC-USD | 12.83 | 0.00 | exit signal |
| 2026-10-24T16:25 | RSI(14) reversion | buy | DOGE-USD | 2.56 | — | rebalance up |
| 2026-10-24T16:15 | RSI(14) reversion | buy | ETH-USD | 2.60 | — | rebalance up |
| 2026-10-24T16:15 | RSI(14) reversion | buy | BTC-USD | 2.59 | — | rebalance up |
| 2026-10-24T16:15 | RSI(14) reversion | sell | XRP-USD | 10.27 | 0.04 | exit signal |
| 2026-10-24T16:10 | RSI(14) reversion | buy | ETH-USD | 2.56 | — | rebalance up |
| 2026-10-24T16:10 | RSI(14) reversion | sell | DOGE-USD | 2.56 | -0.01 | rebalance down |
| 2026-10-24T16:02 | RSI(14) reversion | buy | ETH-USD | 2.56 | — | rebalance up |
| 2026-10-24T16:02 | RSI(14) reversion | sell | BTC-USD | 2.56 | -0.01 | rebalance down |
| 2026-10-24T16:00 | Agent (ML meta-label) | buy | XRP-USD | 4.52 | — | entry |
| 2026-10-24T16:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.76 | — | entry signal |
| 2026-10-24T16:00 | RSI(14) reversion | buy | ETH-USD | 2.56 | — | rebalance up |
| 2026-10-24T16:00 | RSI(14) reversion | sell | SOL-USD | 2.56 | -0.00 | rebalance down |
| 2026-10-24T15:55 | RSI(14) reversion | buy | ETH-USD | 2.57 | — | entry signal |
| 2026-10-24T15:55 | RSI(14) reversion | sell | XRP-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-24T15:35 | RSI(14) reversion | buy | XRP-USD | 12.81 | — | entry signal |
| 2026-10-24T15:35 | RSI(14) reversion | buy | SOL-USD | 12.81 | — | entry signal |
| 2026-10-24T15:35 | RSI(14) reversion | buy | DOGE-USD | 12.81 | — | entry signal |
| 2026-10-24T15:35 | RSI(14) reversion | buy | BTC-USD | 12.81 | — | entry signal |
| 2026-10-24T15:10 | RSI(14) reversion | sell | XRP-USD | 12.80 | -0.19 | stop-loss |
| 2026-10-24T15:10 | RSI(14) reversion | sell | SOL-USD | 12.77 | -0.22 | stop-loss |
| 2026-10-24T15:05 | MFI reversion · 1h | sell | SOL-USD | 20.18 | -0.17 | stop-loss |
| 2026-10-24T15:05 | Z-score reversion · 1h | sell | BTC-USD | 7.52 | -0.07 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-26 18:10:05.000123+00:00 -> 2026-10-24 18:20:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
