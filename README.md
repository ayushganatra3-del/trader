# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T19:45:05.000156+00:00 · 32200 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.14 (-9.86%)

Closed trades 97, win rate 39.2%, fees £3.13, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.07 | +0.11 |

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

Today: 37218 decisions in 2904 calls, $0.4588 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T19:45 | 6 / 10 / 14 | cash |  |
| Breezy | 2026-10-22T19:45 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-22T19:45 | 4 / 23 / 3 | BITX 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.39 | 7.39 | 0 | — | 8.82 | 4.28 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.81 | 6.81 | 12 | 66.7 | 3.90 | 1.18 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.80 | 5.80 | 15 | 46.7 | 8.50 | 2.52 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.82 | -5.96 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.61 | 0.61 | 0 | — | 4.00 | 1.75 | -5.02 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.87 | -0.13 | 78 | 46.2 | -9.60 | -2.61 | -13.79 | 141 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.06 | -0.94 | 12 | 25.0 | -2.87 | -2.92 | -4.04 | 22 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.23 | -2.29 | 68 |
| 11 | Max aggression: 5-day momentum | meta | 98.08 | -1.92 | 10 | 50.0 | -17.19 | -1.37 | -34.64 | 26 |
| 12 | Hold SPY | benchmark | 97.92 | -2.08 | 0 | — | -0.16 | -0.04 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.52 | -2.04 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.76 | -3.24 | 117 | 30.8 | -3.56 | -1.55 | -7.58 | 243 |
| 15 | Hold BTC | benchmark | 96.01 | -3.99 | 0 | — | 4.70 | 0.88 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.84 | -4.16 | 0 | — | -0.44 | -0.12 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.83 | 0.68 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.08 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.91 | -5.09 | 0 | — | -5.22 | -1.91 | -7.17 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.24 | 1.97 | -7.38 | 196 |
| 21 | Copy: Insider buying | copy | 94.21 | -5.79 | 25 | 40.0 | -13.49 | -2.33 | -20.62 | 72 |
| 22 | Opening range 30m | breakout | 93.95 | -6.05 | 237 | 35.0 | -10.13 | -2.86 | -17.26 | 558 |
| 23 | Trend pullback · 1h | trend | 93.71 | -6.29 | 95 | 23.2 | -23.34 | -7.34 | -23.60 | 125 |
| 24 | Donchian 55/20 · 1h | breakout | 93.22 | -6.78 | 48 | 16.7 | -18.35 | -3.76 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.86 | -7.14 | 115 | 26.1 | -16.97 | -3.77 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.43 | -7.57 | 103 | 19.4 | -9.71 | -1.87 | -12.98 | 251 |
| 27 | Daily: Momentum burst | daily | 91.93 | -8.07 | 8 | 12.5 | -16.96 | -3.01 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.26 | -0.70 | -11.76 | 98 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.30 | -2.18 | -16.91 | 1 |
| 30 | Agent | meta | 90.14 | -9.86 | 97 | 39.2 | -13.08 | -6.27 | -14.70 | 263 |
| 31 | Bollinger breakout · 1h | breakout | 89.61 | -10.39 | 104 | 27.9 | -11.36 | -2.03 | -15.91 | 257 |
| 32 | Daily: Bullish score | daily | 89.55 | -10.45 | 8 | 0.0 | -7.29 | -0.85 | -13.53 | 13 |
| 33 | Volume breakout · 1h | breakout | 89.30 | -10.70 | 101 | 22.8 | -10.80 | -1.91 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.95 | -11.05 | 0 | — | -2.79 | -0.28 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.85 | -12.15 | 46 | 34.8 | -18.12 | -4.61 | -19.65 | 133 |
| 36 | EMA 20/50 cross · 1h | trend | 87.61 | -12.39 | 68 | 11.8 | -23.14 | -4.22 | -25.20 | 142 |
| 37 | Supertrend · 1h | trend | 86.90 | -13.10 | 104 | 15.4 | -24.25 | -4.74 | -27.31 | 219 |
| 38 | Stochastic reversion · 1h | reversion | 86.70 | -13.29 | 178 | 45.5 | -16.81 | -2.77 | -22.24 | 388 |
| 39 | RSI momentum · 1h | momentum | 86.64 | -13.36 | 96 | 16.7 | -22.03 | -4.24 | -22.88 | 216 |
| 40 | Opening range 15m | breakout | 86.60 | -13.40 | 301 | 30.2 | -16.45 | -4.45 | -18.54 | 701 |
| 41 | Keltner breakout · 1h | breakout | 86.38 | -13.62 | 73 | 23.3 | -22.29 | -4.33 | -23.59 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.17 | -14.83 | 168 | 39.9 | -26.11 | -7.17 | -26.17 | 204 |
| 43 | MACD cross · 1h | trend | 84.92 | -15.08 | 216 | 23.1 | -28.23 | -5.16 | -29.72 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.43 | -15.57 | 96 | 15.6 | -27.49 | -5.16 | -29.70 | 221 |
| 45 | Ichimoku · 1h | trend | 83.98 | -16.02 | 65 | 12.3 | -20.22 | -3.73 | -23.03 | 117 |
| 46 | Donchian 20/10 · 1h | breakout | 82.87 | -17.12 | 93 | 20.4 | -24.59 | -4.49 | -25.39 | 226 |
| 47 | Z-score reversion · 1h | reversion | 82.50 | -17.50 | 104 | 33.7 | -14.62 | -2.13 | -21.32 | 200 |
| 48 | OBV trend · 1h | momentum | 82.19 | -17.81 | 198 | 17.7 | -32.79 | -6.22 | -33.44 | 307 |
| 49 | MACD zero-line · 1h | trend | 82.18 | -17.82 | 103 | 15.5 | -24.37 | -4.66 | -25.56 | 224 |
| 50 | Three white soldiers | momentum | 81.84 | -18.16 | 266 | 19.9 | -45.10 | -18.27 | -45.28 | 599 |
| 51 | MFI reversion · 1h | reversion | 81.63 | -18.37 | 241 | 32.0 | -19.21 | -2.93 | -21.11 | 152 |
| 52 | Williams %R · 1h | reversion | 81.60 | -18.40 | 204 | 44.1 | -33.89 | -5.43 | -37.93 | 529 |
| 53 | CCI reversion · 1h | reversion | 80.38 | -19.62 | 193 | 43.0 | -24.11 | -3.27 | -28.13 | 444 |
| 54 | Heikin-Ashi · 1h | trend | 80.09 | -19.91 | 260 | 23.5 | -43.27 | -9.32 | -44.18 | 669 |
| 55 | ROC + volume · 1h | momentum | 79.80 | -20.20 | 233 | 24.0 | -28.64 | -5.22 | -29.22 | 378 |
| 56 | Agent (ML meta-label) | meta | 79.77 | -20.23 | 826 | 19.0 | -19.14 | -3.81 | -19.75 | 376 |
| 57 | Bollinger reversion · 1h | reversion | 79.54 | -20.46 | 168 | 35.1 | -31.62 | -6.06 | -32.69 | 363 |
| 58 | EMA 9/21 cross · 1h | trend | 77.99 | -22.01 | 155 | 11.6 | -32.12 | -6.07 | -33.28 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 77.31 | -22.69 | 90 | 23.3 | -23.35 | -4.20 | -24.53 | 187 |
| 60 | Candlestick reversal · 1h | reversion | 77.16 | -22.84 | 240 | 29.6 | -39.10 | -6.93 | -40.98 | 563 |
| 61 | VWAP momentum · 1h | momentum | 76.89 | -23.11 | 499 | 21.4 | -50.12 | -10.27 | -51.01 | 1231 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.93 | -2.86 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 59.10 | -40.90 | 690 | 23.2 | -78.54 | -22.48 | -79.63 | 1675 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.95 | -20.72 | -65.23 | 850 |
| 65 | Donchian 55/20 | breakout | 56.44 | -43.56 | 538 | 19.7 | -72.53 | -20.34 | -74.14 | 1265 |
| 66 | Squeeze breakout | breakout | 55.02 | -44.98 | 530 | 14.0 | -67.71 | -24.16 | -68.41 | 1198 |
| 67 | EMA 20/50 cross | trend | 54.14 | -45.86 | 584 | 20.2 | -79.69 | -21.10 | -79.71 | 1437 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.57 | -17.00 | -76.76 | 1663 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.33 | -14.52 | -73.45 | 1522 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -32.42 | -98.88 | 5246 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.08 | -35.36 | -94.39 | 2559 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.50 | -25.06 | -89.20 | 1886 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.50 | -29.83 | -91.99 | 2343 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.97 | -25.38 | -91.06 | 2212 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.87 | -36.95 | -97.92 | 3495 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -38.76 | -97.07 | 3526 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -28.48 | -94.40 | 2548 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.19 | -28.77 | -83.57 | 1719 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -37.30 | -99.49 | 5866 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.61 | -31.17 | -93.10 | 2619 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -31.01 | -95.68 | 3420 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -44.40 | -99.79 | 6194 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.23 | -32.91 | -92.23 | 2330 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.69 | -40.27 | -97.75 | 3575 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -38.98 | -98.65 | 4765 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.46 | -37.09 | -94.72 | 2787 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.86 | -29.28 | -84.66 | 1781 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -41.26 | -99.59 | 6233 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.05 | -23.99 | -88.09 | 2196 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.74 | -26.95 | -88.86 | 2182 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.25 | -34.71 | -96.29 | 3801 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.67 | -34.83 | -89.91 | 2109 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -35.19 | -96.22 | 4131 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -47.17 | -99.91 | 8249 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T19:45 | MFI reversion · 1h | buy | UPRO | 6.48 | — | entry |
| 2026-10-22T19:45 | MFI reversion · 1h | buy | LABU | 7.07 | — | rebalance up |
| 2026-10-22T19:45 | MFI reversion · 1h | sell | SOXL | 4.33 | -0.10 | rebalance down |
| 2026-10-22T19:45 | MFI reversion · 1h | sell | AMZN | 4.67 | -0.06 | rebalance down |
| 2026-10-22T19:45 | MFI reversion · 1h | sell | AMD | 4.56 | -0.02 | rebalance down |
| 2026-10-22T19:45 | Three white soldiers | sell | MSTR | 20.43 | -0.09 | exit signal |
| 2026-10-22T19:45 | Squeeze breakout | buy | ETH-USD | 2.78 | — | rebalance up |
| 2026-10-22T19:45 | Squeeze breakout | sell | ETHU | 10.96 | -0.08 | stop-loss |
| 2026-10-22T19:40 | CCI reversion · 1h | buy | COIN | 4.01 | — | rebalance up |
| 2026-10-22T19:40 | CCI reversion · 1h | sell | BTC-USD | 4.01 | -0.03 | rebalance down |
| 2026-10-22T19:40 | Three white soldiers | sell | SOL-USD | 20.36 | -0.16 | exit signal |
| 2026-10-22T19:36 | Agent (ML meta-label) | buy | META | 1.02 | — | entry |
| 2026-10-22T19:36 | Agent (ML meta-label) | buy | ETH-USD | 4.00 | — | entry |
| 2026-10-22T19:36 | Agent (ML meta-label) | sell | GOOGL | 4.51 | -0.01 | selected signal exited |
| 2026-10-22T19:36 | Squeeze breakout | buy | TNA | 2.76 | — | rebalance up |
| 2026-10-22T19:30 | Day trade: Last half hour · TQQQ/SQQQ | buy | SQQQ | 98.30 | — | entry |
| 2026-10-22T19:30 | Agent (ML meta-label) | buy | COIN | 3.65 | — | entry |
| 2026-10-22T19:30 | Agent (ML meta-label) | sell | AMZN | 4.02 | 0.01 | rebalance down |
| 2026-10-22T19:30 | MFI reversion · 1h | buy | LABU | 2.00 | — | entry signal |
| 2026-10-22T19:30 | MFI reversion · 1h | buy | COIN | 10.32 | — | entry signal |
| 2026-10-22T19:30 | MFI reversion · 1h | sell | SOL-USD | 6.17 | -0.04 | rebalance down |
| 2026-10-22T19:30 | MFI reversion · 1h | sell | QQQ | 6.15 | -0.03 | rebalance down |
| 2026-10-22T19:30 | CCI reversion · 1h | buy | COIN | 8.22 | — | entry signal |
| 2026-10-22T19:30 | CCI reversion · 1h | sell | DOGE-USD | 4.09 | -0.02 | rebalance down |
| 2026-10-22T19:30 | CCI reversion · 1h | sell | BITX | 4.13 | -0.00 | rebalance down |
| 2026-10-22T19:30 | VWAP reversion · 1h | buy | TQQQ | 14.29 | — | entry signal |
| 2026-10-22T19:30 | VWAP reversion · 1h | buy | SOXL | 14.41 | — | entry signal |
| 2026-10-22T19:30 | VWAP reversion · 1h | buy | NVDA | 14.41 | — | entry signal |
| 2026-10-22T19:30 | VWAP reversion · 1h | sell | SOL-USD | 5.88 | -0.06 | rebalance down |
| 2026-10-22T19:30 | VWAP reversion · 1h | sell | ETH-USD | 10.74 | -0.03 | rebalance down |
| 2026-10-22T19:30 | VWAP reversion · 1h | sell | DOGE-USD | 11.02 | -0.08 | rebalance down |
| 2026-10-22T19:30 | VWAP reversion · 1h | sell | BTC-USD | 10.70 | -0.04 | rebalance down |
| 2026-10-22T19:30 | Z-score reversion · 1h | buy | TQQQ | 10.77 | — | entry signal |
| 2026-10-22T19:30 | Z-score reversion · 1h | buy | QQQ | 11.90 | — | entry signal |
| 2026-10-22T19:30 | Z-score reversion · 1h | sell | SOXL | 8.55 | -0.27 | rebalance down |
| 2026-10-22T19:30 | Z-score reversion · 1h | sell | MSFT | 4.69 | -0.05 | rebalance down |
| 2026-10-22T19:30 | Z-score reversion · 1h | sell | DOGE-USD | 4.72 | -0.00 | rebalance down |
| 2026-10-22T19:30 | Z-score reversion · 1h | sell | AMD | 4.71 | -0.07 | rebalance down |
| 2026-10-22T19:30 | RSI(14) reversion · 1h | buy | TQQQ | 19.45 | — | entry signal |
| 2026-10-22T19:30 | RSI(14) reversion · 1h | buy | QQQ | 19.45 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 19:45:05.000156+00:00 -> 2026-10-22 19:55:05.000156+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
