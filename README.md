# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T14:10:05.000118+00:00 · 35541 ticks

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

Today: 10653 decisions in 2136 calls, $0.1490 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T14:10 | 0 / 0 / 5 | cash |  |
| Breezy | 2026-10-25T14:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T14:10 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| VWAP momentum | PLTR | 2.24 | +6.98% | 8 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
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
| 6 | VWAP reversion · 1h | reversion | 100.38 | 0.38 | 89 | 44.9 | -11.96 | -3.28 | -13.74 | 157 |
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
| 17 | Hold BTC | benchmark | 94.95 | -5.05 | 0 | — | -0.13 | 0.15 | -9.28 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
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
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.85 | -2.85 | -17.00 | 114 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.74 | -11.26 | 106 | 27.4 | -12.35 | -2.41 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.96 | -3.93 | -22.47 | 393 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -23.06 | -4.84 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -23.18 | -4.60 | -24.92 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.63 | -17.87 | 703 |
| 40 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 41 | RSI momentum · 1h | momentum | 85.39 | -14.61 | 101 | 15.8 | -21.32 | -4.49 | -23.32 | 216 |
| 42 | Supertrend · 1h | trend | 84.73 | -15.27 | 112 | 14.3 | -25.21 | -5.28 | -27.77 | 216 |
| 43 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 44 | MACD cross · 1h | trend | 83.77 | -16.23 | 228 | 22.8 | -24.24 | -4.84 | -27.22 | 461 |
| 45 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.44 | -5.22 | -28.26 | 211 |
| 46 | Z-score reversion · 1h | reversion | 83.43 | -16.57 | 109 | 33.9 | -15.09 | -2.52 | -21.48 | 205 |
| 47 | MFI reversion · 1h | reversion | 81.50 | -18.50 | 262 | 31.7 | -18.15 | -2.92 | -20.66 | 149 |
| 48 | MACD zero-line · 1h | trend | 81.16 | -18.84 | 106 | 15.1 | -22.09 | -4.59 | -25.51 | 219 |
| 49 | Donchian 20/10 · 1h | breakout | 81.13 | -18.87 | 97 | 19.6 | -24.31 | -4.65 | -27.27 | 217 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.66 | -6.92 | -32.83 | 303 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.40 | -6.45 | -36.80 | 536 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.95 | -6.62 | -32.28 | 372 |
| 53 | CCI reversion · 1h | reversion | 79.76 | -20.24 | 204 | 42.2 | -27.13 | -4.05 | -28.17 | 462 |
| 54 | Three white soldiers | momentum | 79.70 | -20.30 | 286 | 19.2 | -44.12 | -20.92 | -44.12 | 593 |
| 55 | Agent (ML meta-label) | meta | 79.37 | -20.62 | 872 | 18.8 | -17.78 | -3.84 | -18.17 | 361 |
| 56 | Heikin-Ashi · 1h | trend | 78.33 | -21.67 | 277 | 23.1 | -43.44 | -9.96 | -43.91 | 656 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -29.65 | -5.82 | -31.38 | 378 |
| 58 | Candlestick reversal · 1h | reversion | 76.82 | -23.18 | 263 | 28.1 | -36.02 | -6.77 | -36.52 | 556 |
| 59 | EMA 9/21 cross · 1h | trend | 76.64 | -23.36 | 164 | 11.6 | -30.87 | -6.28 | -34.03 | 323 |
| 60 | RSI(14) reversion · 1h | reversion | 76.61 | -23.39 | 99 | 23.2 | -17.65 | -3.27 | -24.41 | 195 |
| 61 | VWAP momentum · 1h | momentum | 75.32 | -24.68 | 530 | 20.9 | -50.84 | -11.62 | -50.93 | 1229 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.58 | -43.42 | 719 | 22.3 | -74.90 | -27.36 | -74.95 | 1554 |
| 64 | Volume breakout | breakout | 55.17 | -44.83 | 438 | 12.6 | -62.31 | -26.49 | -62.49 | 787 |
| 65 | Donchian 55/20 | breakout | 52.44 | -47.56 | 574 | 19.2 | -71.31 | -23.24 | -72.00 | 1255 |
| 66 | Squeeze breakout | breakout | 52.12 | -47.88 | 569 | 13.9 | -67.33 | -29.16 | -67.35 | 1165 |
| 67 | EMA 20/50 cross | trend | 51.38 | -48.62 | 632 | 20.3 | -78.82 | -23.29 | -79.38 | 1416 |
| 68 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.79 | -44.99 | -98.79 | 5088 |
| 69 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.79 | -45.33 | -93.91 | 2523 |
| 70 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.87 | -30.68 | -89.14 | 1902 |
| 71 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.32 | -38.13 | -91.49 | 2324 |
| 72 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.34 | -29.79 | -90.34 | 2152 |
| 73 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -55.26 | -97.88 | 3516 |
| 74 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.07 | -58.86 | -96.15 | 3346 |
| 75 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -35.32 | -94.15 | 2462 |
| 76 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.91 | -36.03 | -83.20 | 1693 |
| 77 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -55.05 | -99.43 | 5773 |
| 78 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.41 | -41.89 | -92.53 | 2598 |
| 79 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.51 | -38.86 | -95.51 | 3378 |
| 80 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -81.73 | -99.77 | 6167 |
| 81 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.32 | -45.16 | -92.32 | 2337 |
| 82 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.62 | -63.33 | -97.64 | 3548 |
| 83 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -61.23 | -98.66 | 4788 |
| 84 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 85 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -59.73 | -94.59 | 2773 |
| 86 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.89 | -39.28 | -83.97 | 1781 |
| 87 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.60 | -68.03 | -99.60 | 6257 |
| 88 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.41 | -29.57 | -88.42 | 2230 |
| 89 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -78.19 | -20.37 | -78.28 | 1710 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.81 | -38.72 | -90.85 | 2279 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.31 | -48.90 | -96.31 | 3801 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.91 | -51.42 | -89.91 | 2117 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.71 | -18.25 | -76.96 | 1594 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.46 | -49.79 | -96.47 | 4183 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -111.84 | -99.92 | 8244 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T14:05 | Squeeze breakout | sell | XRP-USD | 12.94 | -0.12 | stop-loss |
| 2026-10-25T13:55 | Squeeze breakout | buy | XRP-USD | 13.06 | — | entry signal |
| 2026-10-25T13:45 | EMA 20/50 cross | buy | XRP-USD | 12.87 | — | entry signal |
| 2026-10-25T13:40 | Donchian 55/20 | buy | DOGE-USD | 13.13 | — | entry signal |
| 2026-10-25T13:20 | EMA 20/50 cross | buy | DOGE-USD | 12.87 | — | entry signal |
| 2026-10-25T12:30 | EMA 20/50 cross | sell | BTC-USD | 12.79 | -0.11 | stop-loss |
| 2026-10-25T12:20 | ROC + volume | sell | SOL-USD | 14.08 | -0.14 | stop-loss |
| 2026-10-25T12:20 | ROC + volume | sell | ETH-USD | 14.08 | -0.13 | exit signal |
| 2026-10-25T12:15 | Squeeze breakout | sell | XRP-USD | 13.06 | -0.10 | stop-loss |
| 2026-10-25T12:15 | Squeeze breakout | sell | SOL-USD | 13.06 | -0.10 | stop-loss |
| 2026-10-25T12:15 | Squeeze breakout | sell | ETH-USD | 13.09 | -0.07 | stop-loss |
| 2026-10-25T12:15 | Squeeze breakout | sell | DOGE-USD | 13.03 | -0.12 | stop-loss |
| 2026-10-25T12:10 | Three white soldiers | sell | SOL-USD | 19.83 | -0.17 | exit signal |
| 2026-10-25T12:10 | Three white soldiers | sell | BTC-USD | 19.87 | -0.14 | exit signal |
| 2026-10-25T12:10 | Volume breakout | sell | SOL-USD | 13.77 | -0.12 | exit signal |
| 2026-10-25T12:10 | Volume breakout | sell | ETH-USD | 13.80 | -0.10 | exit signal |
| 2026-10-25T12:10 | Volume breakout | sell | DOGE-USD | 13.78 | -0.11 | exit signal |
| 2026-10-25T12:10 | Volume breakout | sell | BTC-USD | 13.80 | -0.09 | exit signal |
| 2026-10-25T12:05 | EMA 20/50 cross | buy | BTC-USD | 12.90 | — | entry signal |
| 2026-10-25T11:50 | Three white soldiers | buy | SOL-USD | 20.00 | — | entry signal |
| 2026-10-25T11:50 | Three white soldiers | buy | BTC-USD | 20.00 | — | entry signal |
| 2026-10-25T11:50 | Volume breakout | buy | SOL-USD | 13.89 | — | entry signal |
| 2026-10-25T11:50 | Volume breakout | buy | DOGE-USD | 13.89 | — | entry signal |
| 2026-10-25T11:50 | Volume breakout | buy | BTC-USD | 13.89 | — | entry signal |
| 2026-10-25T11:50 | Squeeze breakout | buy | DOGE-USD | 13.15 | — | entry signal |
| 2026-10-25T11:50 | ROC + volume | buy | SOL-USD | 14.21 | — | entry signal |
| 2026-10-25T11:50 | ROC + volume | buy | ETH-USD | 14.21 | — | entry signal |
| 2026-10-25T11:45 | Volume breakout | buy | ETH-USD | 13.90 | — | entry signal |
| 2026-10-25T11:45 | Squeeze breakout | buy | XRP-USD | 13.16 | — | entry signal |
| 2026-10-25T11:45 | Squeeze breakout | buy | SOL-USD | 13.16 | — | entry signal |
| 2026-10-25T11:05 | Squeeze breakout | buy | ETH-USD | 13.16 | — | entry signal |
| 2026-10-25T11:00 | Supertrend · 1h | buy | XRP-USD | 7.13 | — | rebalance up |
| 2026-10-25T11:00 | Supertrend · 1h | sell | SOL-USD | 14.00 | -0.31 | exit signal |
| 2026-10-25T11:00 | Supertrend · 1h | sell | ETH-USD | 13.53 | -0.13 | exit signal |
| 2026-10-25T11:00 | MACD cross · 1h | sell | XRP-USD | 13.91 | 0.03 | exit signal |
| 2026-10-25T10:50 | ROC + volume | sell | DOGE-USD | 14.13 | -0.11 | exit signal |
| 2026-10-25T10:25 | Three white soldiers | sell | DOGE-USD | 19.91 | -0.13 | exit signal |
| 2026-10-25T10:20 | ROC + volume | buy | DOGE-USD | 14.24 | — | entry signal |
| 2026-10-25T10:00 | VWAP reversion · 1h | buy | SOL-USD | 25.12 | — | entry signal |
| 2026-10-25T10:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 14:10:05.000118+00:00 -> 2026-10-25 14:20:05.000118+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
