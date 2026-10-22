# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T11:15:05.000124+00:00 · 31796 ticks

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

Today: 8460 decisions in 1692 calls, $0.1185 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T11:15 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-22T11:15 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T11:15 | 0 / 4 / 1 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.02 | 6.02 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.37 | 2.37 | 75 | 48.0 | -8.32 | -2.26 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 101.49 | 1.49 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.22 | 0.22 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.61 | -0.39 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.39 | -0.61 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.49 | -2.52 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.05 | -2.95 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 17 | Hold BTC | benchmark | 96.74 | -3.26 | 0 | — | 6.26 | 1.10 | -8.68 | 1 |
| 18 | Copy: Insider buying | copy | 96.68 | -3.32 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.77 | -4.23 | 117 | 30.8 | -8.74 | -5.13 | -8.79 | 235 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 21 | ADX DI cross · 1h | trend | 95.45 | -4.54 | 92 | 19.6 | -10.64 | -1.94 | -16.14 | 259 |
| 22 | Daily: Momentum burst | daily | 94.91 | -5.09 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.85 | -5.15 | 92 | 23.9 | -20.36 | -6.35 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.90 | -6.10 | 46 | 17.4 | -16.33 | -3.34 | -17.38 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.91 | -7.09 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.81 | -7.19 | 113 | 25.7 | -15.82 | -3.48 | -19.79 | 270 |
| 29 | Squeeze breakout · 1h | breakout | 92.49 | -7.51 | 50 | 24.0 | -3.00 | -0.66 | -11.48 | 101 |
| 30 | Daily: Bullish score | daily | 92.18 | -7.82 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 93 | 30.1 | -8.40 | -1.50 | -14.43 | 258 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -16.03 | -6.09 | -16.97 | 256 |
| 34 | Volume breakout · 1h | breakout | 90.36 | -9.64 | 95 | 24.2 | -10.79 | -1.89 | -12.43 | 107 |
| 35 | Supertrend · 1h | trend | 89.63 | -10.37 | 93 | 15.1 | -21.15 | -4.23 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.10 | -10.90 | 89 | 18.0 | -18.47 | -3.70 | -20.65 | 220 |
| 37 | Stochastic reversion · 1h | reversion | 88.32 | -11.68 | 173 | 46.2 | -15.18 | -2.50 | -22.24 | 371 |
| 38 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 39 | EMA 20/50 cross · 1h | trend | 88.27 | -11.73 | 64 | 12.5 | -21.60 | -3.73 | -23.52 | 142 |
| 40 | Keltner breakout · 1h | breakout | 87.67 | -12.33 | 67 | 23.9 | -20.72 | -4.03 | -22.53 | 199 |
| 41 | MACD cross · 1h | trend | 87.43 | -12.57 | 202 | 22.3 | -23.79 | -4.50 | -26.95 | 467 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -17.44 | -4.42 | -19.61 | 135 |
| 43 | Z-score reversion · 1h | reversion | 86.78 | -13.22 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.50 | -13.50 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 45 | Connors RSI(2) · 1h | reversion | 85.97 | -14.03 | 166 | 40.4 | -25.39 | -7.16 | -25.48 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.40 | -14.60 | 87 | 20.7 | -20.77 | -3.89 | -23.55 | 226 |
| 47 | MFI reversion · 1h | reversion | 85.21 | -14.79 | 229 | 33.2 | -13.64 | -2.03 | -21.11 | 143 |
| 48 | Triple EMA stack · 1h | trend | 85.16 | -14.84 | 94 | 16.0 | -26.78 | -4.94 | -27.70 | 221 |
| 49 | MACD zero-line · 1h | trend | 84.51 | -15.49 | 92 | 15.2 | -23.89 | -4.60 | -26.38 | 229 |
| 50 | Agent (ML meta-label) | meta | 83.51 | -16.49 | 750 | 19.7 | -10.77 | -2.04 | -15.68 | 347 |
| 51 | OBV trend · 1h | momentum | 83.50 | -16.50 | 191 | 18.3 | -30.60 | -5.73 | -31.48 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.77 | -17.23 | 218 | 23.9 | -24.79 | -4.46 | -26.88 | 381 |
| 53 | Williams %R · 1h | reversion | 82.53 | -17.47 | 199 | 44.7 | -31.55 | -4.89 | -36.62 | 518 |
| 54 | Three white soldiers | momentum | 82.37 | -17.63 | 260 | 20.4 | -44.97 | -18.03 | -45.55 | 601 |
| 55 | CCI reversion · 1h | reversion | 82.01 | -17.99 | 188 | 43.6 | -20.37 | -2.65 | -27.44 | 439 |
| 56 | Bollinger reversion · 1h | reversion | 81.81 | -18.19 | 164 | 36.0 | -29.81 | -5.78 | -32.84 | 352 |
| 57 | Heikin-Ashi · 1h | trend | 81.40 | -18.60 | 251 | 23.9 | -44.20 | -8.98 | -46.39 | 675 |
| 58 | RSI(14) reversion · 1h | reversion | 80.80 | -19.20 | 85 | 24.7 | -17.00 | -2.90 | -24.99 | 174 |
| 59 | EMA 9/21 cross · 1h | trend | 80.74 | -19.26 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.01 | -20.99 | 231 | 30.3 | -38.87 | -7.15 | -41.79 | 542 |
| 61 | VWAP momentum · 1h | momentum | 78.98 | -21.02 | 483 | 22.2 | -49.74 | -10.09 | -51.99 | 1250 |
| 62 | Max aggression: 1-day momentum | meta | 77.13 | -22.87 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.78 | -40.22 | 679 | 23.4 | -77.77 | -21.81 | -78.97 | 1702 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.17 | -19.32 | -64.95 | 858 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -71.80 | -18.80 | -74.04 | 1274 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.18 | -23.04 | -67.93 | 1202 |
| 67 | EMA 20/50 cross | trend | 55.20 | -44.80 | 575 | 20.5 | -79.05 | -20.01 | -80.44 | 1434 |
| 68 | RSI(14) reversion | reversion | 53.57 | -46.43 | 789 | 26.2 | -75.87 | -16.95 | -76.17 | 1641 |
| 69 | VWAP reversion | reversion | 51.53 | -48.47 | 786 | 25.3 | -72.42 | -14.51 | -72.87 | 1487 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.74 | -98.85 | 5290 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.95 | -33.22 | -94.26 | 2581 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.77 | -22.85 | -88.73 | 1890 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -27.31 | -91.74 | 2353 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.24 | -25.47 | -91.24 | 2250 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -35.10 | -97.84 | 3503 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.85 | -36.73 | -96.98 | 3585 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -28.16 | -94.42 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -27.66 | -83.41 | 1726 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.97 | -99.46 | 5776 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -29.95 | -92.76 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.84 | -30.76 | -95.84 | 3458 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.89 | -99.77 | 6149 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.93 | -91.98 | 2333 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -38.15 | -97.71 | 3607 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.60 | -38.30 | -98.60 | 4720 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.23 | -34.87 | -94.51 | 2793 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.27 | -27.36 | -84.44 | 1788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.26 | -99.58 | 6203 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.73 | -23.49 | -87.79 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.37 | -26.92 | -88.49 | 2156 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.15 | -33.84 | -96.16 | 3776 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.55 | -34.44 | -89.60 | 2102 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.12 | -34.50 | -96.13 | 4103 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.00 | -99.91 | 8278 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T11:10 | EMA 20/50 cross | buy | SOL-USD | 13.81 | — | entry signal |
| 2026-10-22T11:00 | CCI reversion · 1h | buy | SOL-USD | 20.53 | — | entry signal |
| 2026-10-22T11:00 | CCI reversion · 1h | buy | DOGE-USD | 20.53 | — | entry signal |
| 2026-10-22T11:00 | Williams %R · 1h | buy | SOL-USD | 20.65 | — | entry signal |
| 2026-10-22T11:00 | RSI(14) reversion · 1h | buy | BTC-USD | 20.22 | — | entry signal |
| 2026-10-22T11:00 | EMA 20/50 cross · 1h | sell | ETH-USD | 8.55 | -0.18 | exit signal |
| 2026-10-22T10:55 | Agent (ML meta-label) | sell | XRP-USD | 10.39 | -0.06 | selected signal exited |
| 2026-10-22T10:55 | VWAP reversion | buy | ETH-USD | 2.57 | — | rebalance up |
| 2026-10-22T10:55 | VWAP reversion | sell | BTC-USD | 2.57 | -0.01 | rebalance down |
| 2026-10-22T10:50 | Agent (ML meta-label) | buy | XRP-USD | 10.45 | — | entry |
| 2026-10-22T10:50 | Three white soldiers | sell | SOL-USD | 20.55 | -0.06 | exit signal |
| 2026-10-22T10:47 | Agent (ML meta-label) | sell | XRP-USD | 2.96 | -0.02 | selected signal exited |
| 2026-10-22T10:35 | VWAP reversion | buy | ETH-USD | 2.58 | — | rebalance up |
| 2026-10-22T10:35 | VWAP reversion | sell | SOL-USD | 2.58 | 0.01 | rebalance down |
| 2026-10-22T10:10 | Agent (ML meta-label) | sell | XRP-USD | 6.26 | -0.05 | rebalance down |
| 2026-10-22T10:05 | Agent (ML meta-label) | buy | XRP-USD | 9.29 | — | entry |
| 2026-10-22T10:05 | RSI(14) reversion | sell | XRP-USD | 10.75 | -0.03 | exit signal |
| 2026-10-22T10:05 | RSI(14) reversion | sell | DOGE-USD | 10.74 | -0.03 | exit signal |
| 2026-10-22T10:05 | RSI(14) reversion | sell | BTC-USD | 10.72 | -0.04 | exit signal |
| 2026-10-22T10:05 | ROC + volume | buy | SOL-USD | 14.95 | — | entry signal |
| 2026-10-22T10:00 | MFI reversion · 1h | buy | SOL-USD | 21.31 | — | entry signal |
| 2026-10-22T10:00 | MFI reversion · 1h | buy | BTC-USD | 21.31 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | XRP-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | SOL-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | DOGE-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | VWAP reversion · 1h | buy | BTC-USD | 25.63 | — | entry signal |
| 2026-10-22T10:00 | Bollinger reversion · 1h | buy | ETH-USD | 20.33 | — | entry signal |
| 2026-10-22T10:00 | Bollinger reversion · 1h | buy | BTC-USD | 20.47 | — | entry signal |
| 2026-10-22T10:00 | RSI(14) reversion · 1h | buy | SOL-USD | 20.21 | — | entry signal |
| 2026-10-22T10:00 | Three white soldiers | buy | SOL-USD | 20.61 | — | entry signal |
| 2026-10-22T09:55 | RSI(14) reversion | buy | ETH-USD | 2.83 | — | rebalance up |
| 2026-10-22T09:55 | RSI(14) reversion | sell | SOL-USD | 10.79 | -0.05 | exit signal |
| 2026-10-22T09:50 | VWAP reversion | buy | ETH-USD | 5.15 | — | entry signal |
| 2026-10-22T09:50 | RSI(14) reversion | buy | ETH-USD | 10.60 | — | entry signal |
| 2026-10-22T09:50 | RSI(14) reversion | sell | BTC-USD | 2.67 | -0.02 | rebalance down |
| 2026-10-22T09:45 | Agent (ML meta-label) | sell | XRP-USD | 10.39 | -0.06 | selected signal exited |
| 2026-10-22T09:45 | VWAP reversion | buy | BTC-USD | 5.11 | — | rebalance up |
| 2026-10-22T09:45 | VWAP reversion | sell | ETH-USD | 10.25 | -0.10 | stop-loss |
| 2026-10-22T09:45 | RSI(14) reversion | buy | BTC-USD | 2.76 | — | rebalance up |
| 2026-10-22T09:45 | RSI(14) reversion | sell | ETH-USD | 10.69 | -0.11 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 11:15:05.000124+00:00 -> 2026-10-22 11:25:05.000124+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
