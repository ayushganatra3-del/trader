# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T17:46:05.000169+00:00 · 32107 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.22 (-9.78%)

Closed trades 96, win rate 39.6%, fees £3.11, max drawdown -10.47%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.01 | -0.03 |
| ETHU | 36.14 | +0.21 |

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

Today: 28872 decisions in 2625 calls, $0.3610 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T17:46 | 4 / 18 / 7 | cash |  |
| Breezy | 2026-10-22T17:46 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-22T17:46 | 6 / 23 / 0 | MSTR 58% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.57 | 7.57 | 0 | — | 10.24 | 4.55 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.18 | 5.18 | 12 | 66.7 | 2.33 | 0.76 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 104.20 | 4.20 | 15 | 46.7 | 6.85 | 2.15 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.96 | 0.96 | 77 | 46.8 | -9.63 | -2.60 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.13 | 0.13 | 0 | — | 3.35 | 1.49 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.60 | 1.52 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 11 | Hold SPY | benchmark | 98.11 | -1.89 | 0 | — | -0.32 | -0.13 | -3.13 | 1 |
| 12 | Max aggression: 5-day momentum | meta | 97.87 | -2.13 | 10 | 50.0 | -17.36 | -1.38 | -34.64 | 26 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.49 | -2.00 | -5.83 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 96.99 | -3.01 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 15 | Agent (rotation) | meta | 96.11 | -3.89 | 117 | 30.8 | -8.31 | -4.52 | -9.20 | 268 |
| 16 | Hold BTC | benchmark | 95.93 | -4.07 | 0 | — | 5.63 | 1.00 | -8.68 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.80 | -4.20 | 0 | — | -0.52 | -0.14 | -5.31 | 1 |
| 18 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 2.92 | 0.69 | -7.93 | 8 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.41 | 2.00 | -7.38 | 198 |
| 21 | Copy: Insider buying | copy | 93.95 | -6.05 | 25 | 40.0 | -13.74 | -2.35 | -20.62 | 72 |
| 22 | Trend pullback · 1h | trend | 93.83 | -6.17 | 94 | 23.4 | -23.23 | -7.25 | -23.53 | 125 |
| 23 | Opening range 30m | breakout | 93.58 | -6.42 | 237 | 35.0 | -10.36 | -2.92 | -17.26 | 558 |
| 24 | Donchian 55/20 · 1h | breakout | 92.87 | -7.13 | 48 | 16.7 | -18.67 | -3.77 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.40 | -7.60 | 115 | 26.1 | -17.37 | -3.84 | -20.59 | 265 |
| 26 | Daily: Momentum burst | daily | 92.25 | -7.75 | 8 | 12.5 | -16.93 | -3.00 | -20.58 | 39 |
| 27 | ADX DI cross · 1h | trend | 92.07 | -7.93 | 103 | 19.4 | -10.11 | -1.93 | -12.72 | 251 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.13 | -0.95 | -11.76 | 96 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.23 | -2.15 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.36 | -9.64 | 8 | 0.0 | -6.67 | -0.76 | -13.10 | 13 |
| 31 | Agent | meta | 90.22 | -9.78 | 96 | 39.6 | -17.95 | -6.99 | -19.84 | 304 |
| 32 | Bollinger breakout · 1h | breakout | 89.26 | -10.74 | 104 | 27.9 | -11.71 | -2.07 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 88.95 | -11.05 | 101 | 22.8 | -11.14 | -1.97 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.83 | -11.16 | 0 | — | -4.76 | -0.58 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.84 | -12.16 | 46 | 34.8 | -23.40 | -4.69 | -27.61 | 165 |
| 36 | Stochastic reversion · 1h | reversion | 87.66 | -12.34 | 178 | 45.5 | -15.82 | -2.60 | -22.24 | 383 |
| 37 | EMA 20/50 cross · 1h | trend | 87.42 | -12.58 | 68 | 11.8 | -23.15 | -4.18 | -25.32 | 143 |
| 38 | Supertrend · 1h | trend | 86.96 | -13.04 | 104 | 15.4 | -24.26 | -4.71 | -27.31 | 219 |
| 39 | RSI momentum · 1h | momentum | 86.70 | -13.30 | 95 | 16.8 | -20.41 | -3.93 | -22.42 | 218 |
| 40 | Opening range 15m | breakout | 86.38 | -13.62 | 300 | 30.3 | -16.69 | -4.46 | -18.82 | 702 |
| 41 | Keltner breakout · 1h | breakout | 86.05 | -13.95 | 73 | 23.3 | -22.51 | -4.31 | -23.46 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.38 | -14.62 | 168 | 39.9 | -25.92 | -7.14 | -25.98 | 204 |
| 43 | MACD cross · 1h | trend | 84.80 | -15.20 | 215 | 23.3 | -26.76 | -4.94 | -28.19 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.16 | -15.84 | 96 | 15.6 | -29.26 | -5.51 | -29.69 | 221 |
| 45 | Z-score reversion · 1h | reversion | 83.89 | -16.11 | 104 | 33.7 | -13.68 | -2.09 | -21.32 | 198 |
| 46 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.02 | 116 |
| 47 | Donchian 20/10 · 1h | breakout | 83.15 | -16.85 | 92 | 20.7 | -24.44 | -4.45 | -25.27 | 226 |
| 48 | MFI reversion · 1h | reversion | 82.82 | -17.18 | 235 | 32.3 | -18.37 | -2.82 | -21.11 | 149 |
| 49 | MACD zero-line · 1h | trend | 82.38 | -17.61 | 102 | 15.7 | -24.45 | -4.66 | -25.75 | 225 |
| 50 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.88 | -17.94 | -45.15 | 596 |
| 51 | Williams %R · 1h | reversion | 81.99 | -18.02 | 204 | 44.1 | -33.57 | -5.33 | -37.94 | 524 |
| 52 | OBV trend · 1h | momentum | 81.70 | -18.30 | 198 | 17.7 | -32.61 | -6.20 | -32.84 | 306 |
| 53 | CCI reversion · 1h | reversion | 80.50 | -19.50 | 192 | 43.2 | -23.06 | -3.06 | -27.44 | 444 |
| 54 | Agent (ML meta-label) | meta | 80.44 | -19.56 | 797 | 19.3 | -13.46 | -2.62 | -15.81 | 360 |
| 55 | Bollinger reversion · 1h | reversion | 80.31 | -19.69 | 168 | 35.1 | -30.78 | -5.93 | -32.60 | 360 |
| 56 | Heikin-Ashi · 1h | trend | 79.69 | -20.31 | 260 | 23.5 | -43.50 | -9.24 | -44.13 | 670 |
| 57 | ROC + volume · 1h | momentum | 79.63 | -20.37 | 231 | 24.2 | -28.48 | -5.15 | -28.70 | 376 |
| 58 | EMA 9/21 cross · 1h | trend | 77.99 | -22.01 | 155 | 11.6 | -31.96 | -6.06 | -32.90 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 77.98 | -22.02 | 90 | 23.3 | -18.13 | -3.24 | -23.32 | 176 |
| 60 | Candlestick reversal · 1h | reversion | 77.65 | -22.35 | 239 | 29.7 | -36.71 | -6.09 | -38.38 | 562 |
| 61 | VWAP momentum · 1h | momentum | 76.47 | -23.53 | 499 | 21.4 | -50.93 | -10.37 | -51.33 | 1231 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.00 | -2.79 | -48.18 | 43 |
| 63 | ROC + volume | momentum | 59.12 | -40.88 | 689 | 23.2 | -77.86 | -21.18 | -79.37 | 1682 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.27 | -19.27 | -65.23 | 854 |
| 65 | Donchian 55/20 | breakout | 56.18 | -43.82 | 538 | 19.7 | -72.79 | -20.39 | -74.17 | 1267 |
| 66 | Squeeze breakout | breakout | 55.28 | -44.72 | 528 | 14.0 | -67.09 | -22.56 | -68.25 | 1198 |
| 67 | EMA 20/50 cross | trend | 54.16 | -45.84 | 584 | 20.2 | -79.65 | -20.73 | -79.67 | 1436 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.30 | -16.93 | -76.65 | 1669 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -72.99 | -14.39 | -73.30 | 1514 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.81 | -31.14 | -98.88 | 5285 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.18 | -34.67 | -94.40 | 2567 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.08 | -23.16 | -89.06 | 1895 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.54 | -29.31 | -91.94 | 2348 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.02 | -25.10 | -91.05 | 2216 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -33.81 | -97.93 | 3490 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.92 | -37.17 | -97.08 | 3557 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -28.15 | -94.48 | 2545 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.15 | -28.07 | -83.53 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -36.48 | -99.49 | 5854 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -29.41 | -93.00 | 2613 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.64 | -30.18 | -95.67 | 3432 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.88 | -99.78 | 6174 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.03 | -31.07 | -92.18 | 2323 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.28 | -97.76 | 3587 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.63 | -37.82 | -98.64 | 4750 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.31 | -34.35 | -94.68 | 2782 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.29 | -27.25 | -84.47 | 1785 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -39.81 | -99.59 | 6227 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.94 | -23.60 | -88.01 | 2183 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.69 | -26.92 | -88.86 | 2192 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.20 | -33.67 | -96.25 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -33.22 | -89.85 | 2105 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.20 | -34.37 | -96.22 | 4131 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.07 | -99.91 | 8250 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T17:45 | ROC + volume | sell | SQQQ | 14.69 | -0.12 | exit signal |
| 2026-10-22T17:40 | Agent (ML meta-label) | buy | ETH-USD | 4.73 | — | entry |
| 2026-10-22T17:40 | Agent (ML meta-label) | sell | MSFT | 5.02 | -0.01 | selected signal exited |
| 2026-10-22T17:35 | Agent (ML meta-label) | buy | TNA | 3.97 | — | entry |
| 2026-10-22T17:35 | Agent (ML meta-label) | buy | MSFT | 5.03 | — | entry |
| 2026-10-22T17:35 | Agent (ML meta-label) | sell | MSTR | 8.01 | -0.16 | selected signal exited |
| 2026-10-22T17:30 | Agent (ML meta-label) | buy | SQQQ | 4.85 | — | entry |
| 2026-10-22T17:30 | Agent (ML meta-label) | buy | ETHU | 4.85 | — | following VWAP reversion, Bollinger reversion |
| 2026-10-22T17:30 | Agent (ML meta-label) | sell | LABU | 5.35 | -0.09 | selected signal exited |
| 2026-10-22T17:30 | Agent (ML meta-label) | sell | ETH-USD | 5.34 | -0.02 | selected signal exited |
| 2026-10-22T17:30 | Stochastic reversion · 1h | buy | BITX | 6.63 | — | entry signal |
| 2026-10-22T17:30 | Candlestick reversal · 1h | buy | ETHU | 1.82 | — | entry signal |
| 2026-10-22T17:30 | Candlestick reversal · 1h | buy | BITX | 11.10 | — | entry signal |
| 2026-10-22T17:30 | Candlestick reversal · 1h | sell | MSFT | 12.92 | -0.17 | time stop |
| 2026-10-22T17:30 | Donchian 55/20 · 1h | buy | SQQQ | 23.23 | — | entry signal |
| 2026-10-22T17:30 | OBV trend · 1h | sell | TSLA | 16.45 | -0.12 | exit signal |
| 2026-10-22T17:30 | RSI momentum · 1h | sell | LABU | 10.55 | -0.39 | exit signal |
| 2026-10-22T17:30 | Heikin-Ashi · 1h | buy | AAPL | 19.94 | — | entry signal |
| 2026-10-22T17:30 | ADX DI cross · 1h | sell | LABU | 22.29 | -0.27 | exit signal |
| 2026-10-22T17:30 | Supertrend · 1h | buy | PLTR | 6.77 | — | rebalance up |
| 2026-10-22T17:30 | Supertrend · 1h | sell | MSTR | 10.71 | -0.14 | exit signal |
| 2026-10-22T17:30 | Supertrend · 1h | sell | LABU | 10.50 | -0.41 | exit signal |
| 2026-10-22T17:30 | MACD cross · 1h | sell | MSTR | 20.99 | -0.32 | exit signal |
| 2026-10-22T17:30 | Triple EMA stack · 1h | buy | TNA | 4.40 | — | entry signal |
| 2026-10-22T17:30 | Triple EMA stack · 1h | sell | SQQQ | 4.40 | 0.05 | rebalance down |
| 2026-10-22T17:25 | ROC + volume | sell | AAPL | 14.80 | -0.01 | exit signal |
| 2026-10-22T17:15 | Agent (ML meta-label) | buy | SPY | 2.87 | — | entry |
| 2026-10-22T17:15 | Agent (ML meta-label) | sell | MSFT | 2.87 | -0.00 | selected signal exited |
| 2026-10-22T17:10 | Day trade: Stocks in Play ORB | sell | TSLA | 24.65 | -0.16 | target is flat |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | QQQ | 3.27 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | MSFT | 2.88 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | buy | GOOGL | 4.56 | — | entry |
| 2026-10-22T17:10 | Agent (ML meta-label) | sell | TSLA | 5.34 | -0.05 | selected signal exited |
| 2026-10-22T17:10 | Agent (ML meta-label) | sell | TNA | 5.36 | -0.00 | selected signal exited |
| 2026-10-22T17:10 | ROC + volume · 1h | buy | PLTR | 4.00 | — | rebalance up |
| 2026-10-22T17:10 | ROC + volume · 1h | buy | MSTR | 4.23 | — | rebalance up |
| 2026-10-22T17:10 | ROC + volume · 1h | sell | TSLA | 15.60 | -0.42 | stop-loss |
| 2026-10-22T17:10 | Trend pullback · 1h | sell | TSLA | 22.99 | -0.62 | stop-loss |
| 2026-10-22T17:10 | EMA 20/50 cross · 1h | buy | TSLA | 4.40 | — | rebalance up |
| 2026-10-22T17:05 | Agent (ML meta-label) | buy | TQQQ | 5.36 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 17:46:05.000169+00:00 -> 2026-10-22 17:56:05.000169+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
