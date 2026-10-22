# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T11:45:05.000158+00:00 · 31819 ticks

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

Today: 8805 decisions in 1761 calls, $0.1234 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T11:45 | 1 / 2 / 2 | cash |  |
| Breezy | 2026-10-22T11:45 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T11:45 | 0 / 5 / 0 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.15 | 6.15 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.51 | 2.51 | 75 | 48.0 | -8.31 | -2.25 | -13.79 | 134 |
| 6 | Max aggression: 5-day momentum | meta | 101.61 | 1.61 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.34 | 0.34 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.73 | -0.27 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.51 | -0.49 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.60 | -2.40 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 97.16 | -2.84 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 17 | Copy: Insider buying | copy | 96.79 | -3.21 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 18 | Hold BTC | benchmark | 96.76 | -3.24 | 0 | — | 5.42 | 0.98 | -8.68 | 1 |
| 19 | Agent (rotation) | meta | 95.81 | -4.19 | 117 | 30.8 | -8.40 | -4.90 | -8.45 | 236 |
| 20 | ADX DI cross · 1h | trend | 95.56 | -4.44 | 92 | 19.6 | -10.64 | -1.94 | -16.14 | 259 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 22 | Daily: Momentum burst | daily | 95.03 | -4.97 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.91 | -5.09 | 92 | 23.9 | -20.36 | -6.35 | -20.58 | 129 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.93 | -6.07 | 46 | 17.4 | -16.33 | -3.34 | -17.38 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 93.02 | -6.98 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.86 | -7.14 | 113 | 25.7 | -15.82 | -3.48 | -19.79 | 270 |
| 29 | Squeeze breakout · 1h | breakout | 92.51 | -7.49 | 50 | 24.0 | -2.55 | -0.55 | -11.48 | 100 |
| 30 | Daily: Bullish score | daily | 92.27 | -7.73 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.08 | -7.92 | 93 | 30.1 | -8.39 | -1.50 | -14.43 | 258 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -17.85 | -5.46 | -19.69 | 258 |
| 34 | Volume breakout · 1h | breakout | 90.43 | -9.57 | 95 | 24.2 | -10.79 | -1.89 | -12.43 | 107 |
| 35 | Supertrend · 1h | trend | 89.71 | -10.29 | 93 | 15.1 | -21.06 | -4.21 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.17 | -10.83 | 89 | 18.0 | -18.47 | -3.70 | -20.65 | 220 |
| 37 | Stochastic reversion · 1h | reversion | 88.44 | -11.56 | 173 | 46.2 | -15.17 | -2.50 | -22.24 | 371 |
| 38 | EMA 20/50 cross · 1h | trend | 88.35 | -11.65 | 64 | 12.5 | -21.60 | -3.73 | -23.52 | 142 |
| 39 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 40 | Keltner breakout · 1h | breakout | 87.73 | -12.27 | 67 | 23.9 | -20.71 | -4.02 | -22.53 | 199 |
| 41 | MACD cross · 1h | trend | 87.52 | -12.48 | 202 | 22.3 | -23.79 | -4.50 | -26.95 | 467 |
| 42 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.07 | -4.38 | -19.63 | 132 |
| 43 | Z-score reversion · 1h | reversion | 86.84 | -13.16 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.59 | -13.41 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 45 | Connors RSI(2) · 1h | reversion | 85.99 | -14.01 | 166 | 40.4 | -25.42 | -7.16 | -25.48 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.47 | -14.53 | 87 | 20.7 | -20.77 | -3.89 | -23.55 | 226 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.65 | -2.03 | -21.11 | 143 |
| 48 | Triple EMA stack · 1h | trend | 85.24 | -14.76 | 94 | 16.0 | -26.78 | -4.94 | -27.70 | 221 |
| 49 | MACD zero-line · 1h | trend | 84.61 | -15.39 | 92 | 15.2 | -23.89 | -4.60 | -26.38 | 229 |
| 50 | Agent (ML meta-label) | meta | 83.59 | -16.41 | 750 | 19.7 | -9.59 | -1.76 | -16.43 | 356 |
| 51 | OBV trend · 1h | momentum | 83.57 | -16.43 | 191 | 18.3 | -30.60 | -5.73 | -31.48 | 307 |
| 52 | ROC + volume · 1h | momentum | 82.85 | -17.15 | 218 | 23.9 | -24.79 | -4.46 | -26.88 | 381 |
| 53 | Williams %R · 1h | reversion | 82.61 | -17.39 | 199 | 44.7 | -31.54 | -4.89 | -36.62 | 518 |
| 54 | Three white soldiers | momentum | 82.37 | -17.63 | 260 | 20.4 | -44.95 | -18.02 | -45.53 | 601 |
| 55 | CCI reversion · 1h | reversion | 82.15 | -17.85 | 188 | 43.6 | -20.33 | -2.64 | -27.44 | 439 |
| 56 | Bollinger reversion · 1h | reversion | 81.93 | -18.07 | 164 | 36.0 | -29.80 | -5.78 | -32.84 | 352 |
| 57 | Heikin-Ashi · 1h | trend | 81.45 | -18.55 | 251 | 23.9 | -43.87 | -9.02 | -46.07 | 675 |
| 58 | RSI(14) reversion · 1h | reversion | 80.89 | -19.11 | 85 | 24.7 | -17.01 | -2.91 | -24.99 | 174 |
| 59 | EMA 9/21 cross · 1h | trend | 80.83 | -19.17 | 145 | 11.7 | -26.79 | -5.19 | -29.94 | 331 |
| 60 | Candlestick reversal · 1h | reversion | 79.10 | -20.90 | 231 | 30.3 | -38.88 | -7.16 | -41.79 | 542 |
| 61 | VWAP momentum · 1h | momentum | 79.05 | -20.95 | 483 | 22.2 | -49.92 | -10.09 | -52.17 | 1250 |
| 62 | Max aggression: 1-day momentum | meta | 77.22 | -22.77 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.75 | -40.25 | 680 | 23.4 | -77.73 | -21.69 | -78.97 | 1701 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.17 | -19.32 | -64.95 | 858 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -71.80 | -18.80 | -74.04 | 1274 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.04 | -22.78 | -67.93 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.22 | -44.78 | 575 | 20.5 | -78.97 | -19.87 | -80.44 | 1433 |
| 68 | RSI(14) reversion | reversion | 53.58 | -46.42 | 789 | 26.2 | -75.85 | -16.92 | -76.17 | 1639 |
| 69 | VWAP reversion | reversion | 51.60 | -48.41 | 786 | 25.3 | -72.41 | -14.51 | -72.87 | 1487 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -31.56 | -98.85 | 5288 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.88 | -32.44 | -94.26 | 2577 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.86 | -23.17 | -88.74 | 1892 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.12 | -27.30 | -91.74 | 2353 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.24 | -25.47 | -91.24 | 2250 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.74 | -34.92 | -97.84 | 3501 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -36.35 | -96.98 | 3583 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.42 | -28.15 | -94.42 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.01 | -27.66 | -83.41 | 1726 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.95 | -99.46 | 5778 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.26 | -29.98 | -92.77 | 2622 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.83 | -30.76 | -95.83 | 3457 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.91 | -99.77 | 6150 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -29.43 | -92.00 | 2329 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.68 | -38.19 | -97.71 | 3608 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.60 | -38.31 | -98.60 | 4721 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.21 | -34.81 | -94.49 | 2792 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.34 | -27.64 | -84.44 | 1790 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.28 | -99.58 | 6207 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.73 | -23.49 | -87.79 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.37 | -26.92 | -88.50 | 2156 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.15 | -33.84 | -96.16 | 3776 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.51 | -34.32 | -89.61 | 2099 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.12 | -34.50 | -96.13 | 4105 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.88 | -99.91 | 8276 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T11:25 | ROC + volume | sell | SOL-USD | 14.90 | -0.05 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 11:45:05.000158+00:00 -> 2026-10-22 11:55:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
