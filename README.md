# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T09:10:05.000153+00:00 · 35283 ticks

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

Today: 6789 decisions in 1362 calls, $0.0949 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T09:10 | 2 / 0 / 3 | cash |  |
| Breezy | 2026-10-25T09:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T09:10 | 1 / 4 / 0 | cash |  |

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
| 17 | Hold BTC | benchmark | 95.02 | -4.98 | 0 | — | -0.07 | 0.16 | -9.28 | 1 |
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
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.60 | -4.43 | -25.00 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.63 | -17.87 | 703 |
| 40 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 41 | RSI momentum · 1h | momentum | 85.40 | -14.60 | 101 | 15.8 | -21.59 | -4.57 | -23.32 | 216 |
| 42 | Supertrend · 1h | trend | 84.88 | -15.12 | 110 | 14.5 | -25.05 | -5.24 | -27.56 | 216 |
| 43 | MACD cross · 1h | trend | 83.94 | -16.06 | 224 | 22.8 | -23.91 | -4.76 | -27.04 | 461 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.14 | -28.32 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.43 | -16.57 | 109 | 33.9 | -16.00 | -2.70 | -21.48 | 206 |
| 47 | MFI reversion · 1h | reversion | 81.50 | -18.50 | 262 | 31.7 | -18.10 | -2.91 | -20.66 | 149 |
| 48 | MACD zero-line · 1h | trend | 81.32 | -18.68 | 105 | 15.2 | -21.94 | -4.55 | -25.39 | 219 |
| 49 | Donchian 20/10 · 1h | breakout | 81.14 | -18.86 | 97 | 19.6 | -24.31 | -4.65 | -27.21 | 217 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.22 | -6.76 | -32.92 | 304 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.21 | -6.42 | -36.69 | 531 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.82 | -6.60 | -32.15 | 372 |
| 53 | Three white soldiers | momentum | 80.13 | -19.87 | 283 | 19.4 | -44.20 | -20.63 | -44.20 | 592 |
| 54 | CCI reversion · 1h | reversion | 79.75 | -20.25 | 204 | 42.2 | -27.15 | -4.05 | -28.17 | 462 |
| 55 | Agent (ML meta-label) | meta | 79.37 | -20.62 | 872 | 18.8 | -11.30 | -2.42 | -15.85 | 357 |
| 56 | Heikin-Ashi · 1h | trend | 78.33 | -21.67 | 277 | 23.1 | -43.49 | -10.05 | -44.22 | 659 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -29.67 | -5.83 | -31.40 | 380 |
| 58 | Candlestick reversal · 1h | reversion | 76.84 | -23.16 | 263 | 28.1 | -35.22 | -6.63 | -35.80 | 552 |
| 59 | EMA 9/21 cross · 1h | trend | 76.64 | -23.36 | 164 | 11.6 | -30.86 | -6.28 | -33.99 | 323 |
| 60 | RSI(14) reversion · 1h | reversion | 76.58 | -23.42 | 99 | 23.2 | -14.48 | -2.63 | -24.41 | 191 |
| 61 | VWAP momentum · 1h | momentum | 75.32 | -24.68 | 530 | 20.9 | -51.22 | -11.74 | -51.36 | 1231 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.96 | -43.04 | 716 | 22.3 | -74.91 | -26.75 | -74.94 | 1555 |
| 64 | Volume breakout | breakout | 55.59 | -44.41 | 434 | 12.7 | -62.29 | -26.13 | -62.29 | 783 |
| 65 | Squeeze breakout | breakout | 52.63 | -47.37 | 564 | 14.0 | -67.18 | -28.65 | -67.22 | 1162 |
| 66 | Donchian 55/20 | breakout | 52.51 | -47.49 | 574 | 19.2 | -71.43 | -23.19 | -71.96 | 1255 |
| 67 | EMA 20/50 cross | trend | 51.60 | -48.41 | 631 | 20.3 | -78.96 | -23.22 | -79.37 | 1416 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.80 | -45.01 | -98.80 | 5085 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.93 | -45.04 | -93.93 | 2529 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.92 | -30.38 | -89.03 | 1899 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.31 | -37.33 | -91.42 | 2321 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.45 | -30.17 | -90.48 | 2157 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.84 | -53.29 | -97.86 | 3508 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.18 | -58.60 | -96.18 | 3353 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.03 | -35.24 | -94.07 | 2455 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.03 | -35.93 | -83.16 | 1695 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -53.95 | -99.42 | 5768 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.44 | -41.11 | -92.49 | 2597 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.55 | -39.28 | -95.56 | 3386 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -79.39 | -99.77 | 6162 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.27 | -43.99 | -92.31 | 2334 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -62.31 | -97.63 | 3545 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.63 | -60.37 | -98.65 | 4786 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.53 | -58.45 | -94.55 | 2768 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.06 | -38.71 | -84.11 | 1784 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -66.27 | -99.59 | 6249 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.32 | -29.41 | -88.34 | 2227 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -77.97 | -20.29 | -78.06 | 1706 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.72 | -38.08 | -90.75 | 2273 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -48.17 | -96.26 | 3800 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.87 | -49.35 | -89.92 | 2115 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.56 | -18.16 | -76.68 | 1590 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.41 | -49.35 | -96.44 | 4181 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -104.94 | -99.92 | 8233 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 4.73 | -0.04 | exit signal |
| 2026-10-25T09:00 | Supertrend · 1h | buy | ETH-USD | 13.66 | — | entry |
| 2026-10-25T09:00 | Supertrend · 1h | sell | DOGE-USD | 13.66 | -0.38 | exit signal |
| 2026-10-25T09:00 | MACD cross · 1h | sell | DOGE-USD | 9.19 | -0.17 | exit signal |
| 2026-10-25T08:57 | RSI(14) reversion | sell | ETH-USD | 12.47 | -0.10 | Kill switch: down 50% from peak |
| 2026-10-25T08:57 | RSI(14) reversion | sell | BTC-USD | 12.49 | -0.08 | Kill switch: down 50% from peak |
| 2026-10-25T08:55 | RSI(14) reversion | sell | SOL-USD | 12.44 | -0.12 | stop-loss |
| 2026-10-25T08:55 | RSI(14) reversion | sell | DOGE-USD | 12.45 | -0.12 | stop-loss |
| 2026-10-25T08:40 | RSI(14) reversion | buy | SOL-USD | 12.57 | — | entry signal |
| 2026-10-25T08:40 | RSI(14) reversion | buy | ETH-USD | 12.57 | — | entry signal |
| 2026-10-25T08:40 | RSI(14) reversion | buy | DOGE-USD | 12.57 | — | entry signal |
| 2026-10-25T08:35 | RSI(14) reversion | buy | BTC-USD | 12.58 | — | entry signal |
| 2026-10-25T08:30 | RSI(14) reversion | sell | SOL-USD | 12.53 | -0.14 | stop-loss |
| 2026-10-25T08:30 | RSI(14) reversion | sell | ETH-USD | 12.58 | -0.12 | stop-loss |
| 2026-10-25T08:30 | RSI(14) reversion | sell | DOGE-USD | 12.51 | -0.16 | target is flat |
| 2026-10-25T08:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.77 | — | entry signal |
| 2026-10-25T08:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.16 | — | rebalance up |
| 2026-10-25T08:00 | EMA 9/21 cross · 1h | sell | SOL-USD | 10.85 | -0.16 | exit signal |
| 2026-10-25T07:45 | RSI(14) reversion | sell | XRP-USD | 12.68 | 0.01 | take-profit |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 09:10:05.000153+00:00 -> 2026-10-25 09:20:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
