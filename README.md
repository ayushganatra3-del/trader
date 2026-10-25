# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T07:40:05.000107+00:00 · 35209 ticks

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

Today: 5685 decisions in 1140 calls, $0.0795 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T07:40 | 2 / 3 / 0 | cash |  |
| Breezy | 2026-10-25T07:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T07:40 | 3 / 2 / 0 | BTC-USD 58% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| VWAP momentum | PLTR | 2.11 | +6.67% | 8 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.01 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -11.85 | -3.25 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 5.84 | 2.80 | -1.76 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 17 | Hold BTC | benchmark | 95.34 | -4.66 | 0 | — | 0.27 | 0.22 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.16 | -5.84 | 25 | 40.0 | -17.31 | -3.33 | -21.47 | 61 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.85 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 90.91 | -9.09 | 109 | 18.3 | -12.09 | -2.45 | -14.69 | 257 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -12.91 | -2.65 | -16.09 | 115 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.92 | -3.92 | -22.47 | 390 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.72 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.46 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.63 | -17.87 | 703 |
| 40 | RSI momentum · 1h | momentum | 85.51 | -14.49 | 101 | 15.8 | -21.49 | -4.54 | -23.32 | 216 |
| 41 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 42 | Supertrend · 1h | trend | 85.30 | -14.70 | 109 | 14.7 | -24.62 | -5.14 | -27.35 | 216 |
| 43 | MACD cross · 1h | trend | 84.27 | -15.73 | 223 | 22.9 | -23.63 | -4.69 | -26.91 | 461 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.47 | -16.53 | 109 | 33.9 | -15.73 | -2.65 | -21.48 | 206 |
| 46 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.14 | -28.32 | 211 |
| 47 | MFI reversion · 1h | reversion | 81.50 | -18.50 | 262 | 31.7 | -18.10 | -2.91 | -20.66 | 149 |
| 48 | MACD zero-line · 1h | trend | 81.43 | -18.57 | 105 | 15.2 | -21.83 | -4.52 | -25.37 | 219 |
| 49 | Donchian 20/10 · 1h | breakout | 81.25 | -18.75 | 97 | 19.6 | -24.20 | -4.62 | -27.19 | 217 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.43 | -6.83 | -32.95 | 305 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.21 | -6.42 | -36.69 | 531 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.82 | -6.60 | -32.15 | 372 |
| 53 | Three white soldiers | momentum | 80.13 | -19.87 | 283 | 19.4 | -44.20 | -20.63 | -44.20 | 592 |
| 54 | CCI reversion · 1h | reversion | 79.78 | -20.22 | 204 | 42.2 | -27.10 | -4.04 | -28.17 | 462 |
| 55 | Agent (ML meta-label) | meta | 79.37 | -20.62 | 872 | 18.8 | -10.92 | -1.91 | -15.45 | 376 |
| 56 | Heikin-Ashi · 1h | trend | 78.33 | -21.67 | 277 | 23.1 | -43.49 | -10.05 | -44.22 | 659 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.21 | -5.96 | -31.40 | 381 |
| 58 | Candlestick reversal · 1h | reversion | 76.88 | -23.12 | 262 | 28.2 | -35.61 | -6.69 | -36.26 | 552 |
| 59 | EMA 9/21 cross · 1h | trend | 76.77 | -23.23 | 163 | 11.7 | -30.75 | -6.25 | -33.96 | 323 |
| 60 | RSI(14) reversion · 1h | reversion | 76.73 | -23.27 | 99 | 23.2 | -16.28 | -3.01 | -24.41 | 194 |
| 61 | VWAP momentum · 1h | momentum | 75.32 | -24.68 | 530 | 20.9 | -51.22 | -11.74 | -51.36 | 1231 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.96 | -43.04 | 716 | 22.3 | -75.04 | -26.75 | -75.05 | 1557 |
| 64 | Volume breakout | breakout | 55.59 | -44.41 | 434 | 12.7 | -62.29 | -26.13 | -62.29 | 783 |
| 65 | Squeeze breakout | breakout | 52.63 | -47.37 | 564 | 14.0 | -67.13 | -28.65 | -67.22 | 1162 |
| 66 | Donchian 55/20 | breakout | 52.51 | -47.49 | 574 | 19.2 | -71.83 | -23.19 | -71.96 | 1258 |
| 67 | EMA 20/50 cross | trend | 51.60 | -48.41 | 631 | 20.3 | -78.96 | -23.22 | -79.37 | 1416 |
| 68 | RSI(14) reversion | reversion | 50.68 | -49.32 | 857 | 26.0 | -77.55 | -20.06 | -77.76 | 1702 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -45.01 | -98.79 | 5079 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.93 | -45.04 | -93.97 | 2529 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.87 | -29.98 | -88.96 | 1897 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.40 | -37.33 | -91.46 | 2324 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.45 | -30.17 | -90.48 | 2157 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -52.64 | -97.84 | 3505 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -58.60 | -96.19 | 3356 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.06 | -35.36 | -94.09 | 2457 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.08 | -35.93 | -83.16 | 1696 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -53.44 | -99.42 | 5770 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.42 | -40.77 | -92.48 | 2596 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.53 | -39.25 | -95.54 | 3383 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -78.44 | -99.77 | 6166 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.29 | -43.99 | -92.32 | 2335 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.64 | -62.31 | -97.64 | 3549 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.61 | -59.14 | -98.63 | 4782 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -58.66 | -94.57 | 2769 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.07 | -38.71 | -84.11 | 1785 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -65.43 | -99.59 | 6244 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.22 | -29.14 | -88.26 | 2226 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.64 | -37.63 | -90.69 | 2272 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.22 | -47.41 | -96.23 | 3793 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.78 | -48.95 | -89.90 | 2114 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.20 | -17.92 | -76.44 | 1584 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.38 | -48.88 | -96.42 | 4177 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -103.13 | -99.92 | 8233 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T07:10 | RSI(14) reversion | buy | SOL-USD | 12.67 | — | entry |
| 2026-10-25T07:10 | RSI(14) reversion | buy | DOGE-USD | 12.67 | — | entry signal |
| 2026-10-25T07:05 | RSI(14) reversion | buy | XRP-USD | 12.67 | — | entry signal |
| 2026-10-25T07:00 | ADX DI cross · 1h | sell | XRP-USD | 22.49 | -0.32 | exit signal |
| 2026-10-25T07:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 6.11 | -0.07 | exit signal |
| 2026-10-25T06:55 | Bollinger breakout · 1h | sell | XRP-USD | 21.97 | -0.29 | stop-loss |
| 2026-10-25T06:55 | RSI(14) reversion | sell | XRP-USD | 10.14 | -0.10 | stop-loss |
| 2026-10-25T06:55 | RSI(14) reversion | sell | BTC-USD | 10.16 | -0.08 | stop-loss |
| 2026-10-25T06:50 | RSI(14) reversion | buy | ETH-USD | 12.70 | — | entry signal |
| 2026-10-25T06:45 | RSI(14) reversion | sell | SOL-USD | 10.15 | -0.10 | stop-loss |
| 2026-10-25T06:45 | RSI(14) reversion | sell | ETH-USD | 10.14 | -0.10 | stop-loss |
| 2026-10-25T06:45 | RSI(14) reversion | sell | DOGE-USD | 10.13 | -0.11 | stop-loss |
| 2026-10-25T06:12 | RSI(14) reversion | buy | XRP-USD | 2.56 | — | rebalance up |
| 2026-10-25T06:12 | RSI(14) reversion | sell | SOL-USD | 2.57 | -0.02 | rebalance down |
| 2026-10-25T06:10 | RSI(14) reversion | buy | XRP-USD | 7.68 | — | entry signal |
| 2026-10-25T06:10 | RSI(14) reversion | buy | ETH-USD | 10.24 | — | entry signal |
| 2026-10-25T06:10 | RSI(14) reversion | buy | DOGE-USD | 10.24 | — | entry signal |
| 2026-10-25T06:10 | RSI(14) reversion | buy | BTC-USD | 10.24 | — | entry signal |
| 2026-10-25T06:05 | RSI(14) reversion | sell | ETH-USD | 12.72 | -0.11 | stop-loss |
| 2026-10-25T06:00 | Agent (ML meta-label) | sell | SOL-USD | 3.97 | -0.00 | selected signal exited |
| 2026-10-25T06:00 | MFI reversion · 1h | sell | ETH-USD | 16.23 | 0.11 | exit signal |
| 2026-10-25T06:00 | MFI reversion · 1h | sell | DOGE-USD | 4.04 | -0.06 | exit signal |
| 2026-10-25T06:00 | Candlestick reversal · 1h | sell | SOL-USD | 4.77 | -0.05 | exit signal |
| 2026-10-25T06:00 | VWAP momentum · 1h | sell | DOGE-USD | 7.00 | -0.11 | exit signal |
| 2026-10-25T06:00 | Heikin-Ashi · 1h | sell | XRP-USD | 15.78 | 0.07 | exit signal |
| 2026-10-25T06:00 | Heikin-Ashi · 1h | sell | SOL-USD | 15.73 | 0.03 | exit signal |
| 2026-10-25T06:00 | Heikin-Ashi · 1h | sell | ETH-USD | 15.70 | -0.02 | exit signal |
| 2026-10-25T06:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 15.60 | -0.10 | exit signal |
| 2026-10-25T06:00 | Heikin-Ashi · 1h | sell | BTC-USD | 15.52 | -0.14 | exit signal |
| 2026-10-25T06:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.13 | -0.09 | exit signal |
| 2026-10-25T06:00 | RSI(14) reversion | buy | SOL-USD | 12.84 | — | entry signal |
| 2026-10-25T06:00 | RSI(14) reversion | buy | ETH-USD | 12.84 | — | entry signal |
| 2026-10-25T05:55 | EMA 20/50 cross | sell | XRP-USD | 10.39 | 0.12 | exit signal |
| 2026-10-25T05:50 | EMA 20/50 cross | sell | SOL-USD | 10.32 | 0.04 | exit signal |
| 2026-10-25T05:50 | EMA 20/50 cross | sell | ETH-USD | 12.88 | -0.06 | exit signal |
| 2026-10-25T05:40 | EMA 20/50 cross | sell | BTC-USD | 12.83 | -0.02 | exit signal |
| 2026-10-25T05:35 | Donchian 55/20 | sell | XRP-USD | 10.68 | 0.10 | exit signal |
| 2026-10-25T05:35 | Donchian 55/20 | sell | SOL-USD | 10.63 | 0.04 | exit signal |
| 2026-10-25T05:35 | Donchian 55/20 | sell | ETH-USD | 13.12 | -0.10 | exit signal |
| 2026-10-25T05:35 | Donchian 55/20 | sell | BTC-USD | 13.12 | -0.10 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 07:40:05.000107+00:00 -> 2026-10-25 07:50:05.000107+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
