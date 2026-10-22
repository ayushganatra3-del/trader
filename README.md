# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T06:50:05.000181+00:00 · 31566 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 5010 decisions in 1002 calls, $0.0702 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T06:50 | 4 / 1 / 0 | cash |  |
| Breezy | 2026-10-22T06:50 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T06:50 | 3 / 2 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.94 | 5.94 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.42 | 1.42 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.14 | 0.14 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.54 | -0.46 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.32 | -0.68 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.41 | -2.58 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Hold BTC | benchmark | 97.32 | -2.68 | 0 | — | 7.70 | 1.31 | -8.68 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 96.98 | -3.02 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 18 | Copy: Insider buying | copy | 96.61 | -3.39 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.75 | -4.25 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -4.12 | -3.16 | -6.31 | 31 |
| 21 | ADX DI cross · 1h | trend | 95.39 | -4.61 | 92 | 19.6 | -9.25 | -1.66 | -16.14 | 256 |
| 22 | Daily: Momentum burst | daily | 94.85 | -5.15 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.81 | -5.18 | 92 | 23.9 | -20.41 | -6.36 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 94.27 | -5.73 | 44 | 18.2 | -15.98 | -3.27 | -17.04 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.84 | -7.16 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.78 | -7.22 | 113 | 25.7 | -16.62 | -3.68 | -19.79 | 272 |
| 29 | Squeeze breakout · 1h | breakout | 92.48 | -7.52 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.12 | -7.88 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 91.96 | -8.04 | 93 | 30.1 | -9.96 | -1.80 | -14.57 | 261 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -16.10 | -6.15 | -16.63 | 249 |
| 34 | Volume breakout · 1h | breakout | 90.32 | -9.68 | 95 | 24.2 | -13.56 | -2.38 | -13.60 | 109 |
| 35 | Supertrend · 1h | trend | 89.59 | -10.41 | 93 | 15.1 | -21.06 | -4.21 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.06 | -10.94 | 89 | 18.0 | -18.62 | -3.74 | -20.65 | 219 |
| 37 | Stochastic reversion · 1h | reversion | 88.98 | -11.02 | 169 | 47.3 | -14.24 | -2.34 | -22.24 | 368 |
| 38 | EMA 20/50 cross · 1h | trend | 88.37 | -11.63 | 62 | 12.9 | -21.44 | -3.70 | -23.57 | 142 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.63 | -12.37 | 67 | 23.9 | -20.11 | -3.87 | -22.65 | 200 |
| 41 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -20.01 | -4.59 | -20.01 | 130 |
| 42 | MACD cross · 1h | trend | 87.38 | -12.62 | 202 | 22.3 | -23.77 | -4.50 | -26.95 | 467 |
| 43 | Connors RSI(2) · 1h | reversion | 86.89 | -13.11 | 163 | 41.1 | -24.57 | -7.17 | -24.58 | 202 |
| 44 | Z-score reversion · 1h | reversion | 86.75 | -13.25 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 45 | Ichimoku · 1h | trend | 86.45 | -13.55 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 46 | Donchian 20/10 · 1h | breakout | 85.36 | -14.64 | 87 | 20.7 | -23.70 | -4.39 | -28.87 | 229 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.57 | -2.02 | -21.11 | 141 |
| 48 | Triple EMA stack · 1h | trend | 85.12 | -14.88 | 94 | 16.0 | -26.51 | -4.87 | -27.70 | 221 |
| 49 | MACD zero-line · 1h | trend | 84.45 | -15.55 | 92 | 15.2 | -23.42 | -4.56 | -26.06 | 228 |
| 50 | Agent (ML meta-label) | meta | 84.23 | -15.77 | 739 | 20.0 | -15.37 | -2.90 | -18.15 | 351 |
| 51 | OBV trend · 1h | momentum | 83.48 | -16.52 | 190 | 18.4 | -30.57 | -5.73 | -31.52 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.72 | -17.28 | 218 | 23.9 | -28.46 | -5.00 | -32.98 | 387 |
| 53 | Williams %R · 1h | reversion | 82.56 | -17.44 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -45.32 | -18.08 | -46.47 | 603 |
| 55 | Bollinger reversion · 1h | reversion | 82.32 | -17.68 | 163 | 36.2 | -29.31 | -5.67 | -32.84 | 349 |
| 56 | CCI reversion · 1h | reversion | 82.09 | -17.91 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 57 | Heikin-Ashi · 1h | trend | 81.38 | -18.62 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.85 | -19.15 | 85 | 24.7 | -16.91 | -2.89 | -24.99 | 172 |
| 59 | EMA 9/21 cross · 1h | trend | 80.69 | -19.31 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 78.95 | -21.05 | 231 | 30.3 | -38.84 | -7.15 | -41.79 | 542 |
| 61 | VWAP momentum · 1h | momentum | 78.93 | -21.07 | 483 | 22.2 | -48.57 | -9.74 | -52.95 | 1253 |
| 62 | Max aggression: 1-day momentum | meta | 77.08 | -22.93 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.94 | -22.18 | -78.97 | 1707 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.24 | -19.44 | -64.95 | 859 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.03 | -19.18 | -74.04 | 1276 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.16 | -23.01 | -67.93 | 1203 |
| 67 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.87 | -19.22 | -80.87 | 1437 |
| 68 | RSI(14) reversion | reversion | 54.70 | -45.30 | 778 | 26.6 | -75.40 | -17.00 | -75.63 | 1628 |
| 69 | VWAP reversion | reversion | 52.89 | -47.11 | 774 | 25.7 | -71.60 | -14.44 | -72.15 | 1475 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -32.18 | -98.87 | 5305 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.00 | -33.64 | -94.26 | 2584 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.04 | -23.78 | -88.71 | 1894 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -28.28 | -91.74 | 2358 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.16 | -25.41 | -91.26 | 2260 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.78 | -35.68 | -97.83 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.91 | -37.47 | -96.98 | 3590 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.63 | -28.63 | -94.68 | 2562 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.10 | -27.92 | -83.41 | 1727 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.43 | -37.74 | -99.44 | 5757 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.33 | -30.55 | -92.73 | 2623 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.88 | -30.99 | -95.88 | 3469 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.48 | -99.77 | 6152 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.84 | -30.56 | -91.92 | 2336 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.74 | -39.11 | -97.74 | 3619 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.58 | -38.06 | -98.58 | 4718 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.29 | -35.65 | -94.46 | 2794 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.49 | -28.11 | -84.44 | 1792 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.57 | -40.52 | -99.57 | 6205 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.48 | -23.29 | -87.54 | 2161 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.23 | -27.13 | -88.27 | 2147 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.13 | -33.92 | -96.13 | 3778 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.55 | -34.28 | -89.55 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.06 | -34.71 | -96.08 | 4104 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.25 | -99.91 | 8288 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T06:50 | Agent (ML meta-label) | sell | XRP-USD | 9.31 | -0.05 | selected signal exited |
| 2026-10-22T06:45 | VWAP reversion | buy | ETH-USD | 2.58 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | SOL-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | DOGE-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | VWAP reversion | buy | BTC-USD | 13.26 | — | entry signal |
| 2026-10-22T06:40 | RSI(14) reversion | buy | SOL-USD | 13.69 | — | entry signal |
| 2026-10-22T06:35 | Agent (ML meta-label) | buy | XRP-USD | 9.36 | — | entry |
| 2026-10-22T06:35 | VWAP reversion | sell | SOL-USD | 13.24 | -0.14 | stop-loss |
| 2026-10-22T06:35 | RSI(14) reversion | sell | ETH-USD | 10.96 | -0.13 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | buy | SOL-USD | 2.74 | — | rebalance up |
| 2026-10-22T06:30 | VWAP reversion | sell | ETH-USD | 10.65 | -0.13 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | sell | DOGE-USD | 10.60 | -0.09 | stop-loss |
| 2026-10-22T06:30 | VWAP reversion | sell | BTC-USD | 10.62 | -0.13 | stop-loss |
| 2026-10-22T06:30 | RSI(14) reversion | sell | SOL-USD | 13.64 | -0.17 | stop-loss |
| 2026-10-22T06:30 | RSI(14) reversion | sell | BTC-USD | 13.70 | -0.15 | stop-loss |
| 2026-10-22T06:25 | Agent (ML meta-label) | sell | XRP-USD | 9.30 | -0.08 | selected signal exited |
| 2026-10-22T06:05 | Agent (ML meta-label) | buy | XRP-USD | 9.38 | — | entry |
| 2026-10-22T06:00 | Agent (ML meta-label) | sell | XRP-USD | 9.57 | -0.07 | selected signal exited |
| 2026-10-22T06:00 | VWAP reversion | buy | SOL-USD | 10.63 | — | entry signal |
| 2026-10-22T06:00 | VWAP reversion | buy | DOGE-USD | 10.69 | — | entry |
| 2026-10-22T06:00 | VWAP reversion | sell | BTC-USD | 2.68 | -0.02 | rebalance down |
| 2026-10-22T05:55 | VWAP reversion | sell | SOL-USD | 13.28 | -0.17 | stop-loss |
| 2026-10-22T05:55 | VWAP reversion | sell | DOGE-USD | 5.36 | -0.06 | stop-loss |
| 2026-10-22T05:45 | RSI(14) reversion | sell | DOGE-USD | 13.72 | -0.18 | stop-loss |
| 2026-10-22T05:05 | RSI(14) reversion | buy | DOGE-USD | 2.78 | — | rebalance up |
| 2026-10-22T05:05 | RSI(14) reversion | buy | BTC-USD | 8.23 | — | rebalance up |
| 2026-10-22T05:05 | RSI(14) reversion | sell | XRP-USD | 13.74 | -0.00 | exit signal |
| 2026-10-22T04:55 | VWAP reversion | buy | DOGE-USD | 2.68 | — | rebalance up |
| 2026-10-22T04:55 | VWAP reversion | sell | XRP-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-22T04:50 | VWAP reversion | buy | DOGE-USD | 2.73 | — | entry |
| 2026-10-22T04:50 | VWAP reversion | sell | ETH-USD | 2.73 | -0.02 | rebalance down |
| 2026-10-22T04:05 | Agent (ML meta-label) | buy | XRP-USD | 6.85 | — | rebalance up |
| 2026-10-22T04:05 | Agent (ML meta-label) | sell | SOL-USD | 6.85 | -0.04 | selected signal exited |
| 2026-10-22T04:00 | Agent (ML meta-label) | buy | XRP-USD | 2.79 | — | entry |
| 2026-10-22T04:00 | Agent (ML meta-label) | buy | SOL-USD | 6.89 | — | entry |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | SOL-USD | 6.26 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | ETH-USD | 12.78 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | buy | BTC-USD | 12.78 | — | entry signal |
| 2026-10-22T04:00 | Stochastic reversion · 1h | sell | DOGE-USD | 9.48 | -0.07 | rebalance down |
| 2026-10-22T04:00 | Bollinger reversion · 1h | buy | SOL-USD | 20.65 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 06:50:05.000181+00:00 -> 2026-10-22 07:00:05.000181+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
