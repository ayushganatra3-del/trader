# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T19:15:05.000119+00:00 · 32178 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.13 (-9.87%)

Closed trades 97, win rate 39.2%, fees £3.13, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.06 | +0.10 |

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

Today: 35247 decisions in 2838 calls, $0.4358 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T19:15 | 2 / 21 / 8 | cash |  |
| Breezy | 2026-10-22T19:15 | 0 / 29 / 2 | cash |  |
| Boozy | 2026-10-22T19:15 | 5 / 24 / 2 | COIN 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.51 | 7.51 | 0 | — | 10.00 | 4.69 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.40 | 6.40 | 12 | 66.7 | 3.55 | 1.10 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.40 | 5.40 | 15 | 46.7 | 8.13 | 2.45 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.82 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.49 | 0.49 | 78 | 46.2 | -9.01 | -2.46 | -13.79 | 138 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.31 | 0.31 | 0 | — | 4.02 | 1.77 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.23 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.97 | -4.04 | 21 |
| 11 | Max aggression: 5-day momentum | meta | 97.97 | -2.03 | 10 | 50.0 | -17.25 | -1.38 | -34.64 | 26 |
| 12 | Hold SPY | benchmark | 97.89 | -2.11 | 0 | — | -0.18 | -0.05 | -3.13 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.45 | -1.99 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.54 | -3.46 | 117 | 30.8 | -6.51 | -3.93 | -8.19 | 240 |
| 15 | Hold BTC | benchmark | 95.88 | -4.12 | 0 | — | 4.62 | 0.87 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 95.76 | -4.24 | 0 | — | -0.64 | -0.19 | -5.45 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.06 | 0.72 | -7.93 | 8 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.08 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.88 | -5.12 | 0 | — | -5.22 | -1.91 | -7.17 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.43 | 2.02 | -7.38 | 197 |
| 21 | Copy: Insider buying | copy | 94.17 | -5.83 | 25 | 40.0 | -13.50 | -2.33 | -20.62 | 72 |
| 22 | Opening range 30m | breakout | 93.85 | -6.14 | 237 | 35.0 | -10.06 | -2.85 | -17.26 | 558 |
| 23 | Trend pullback · 1h | trend | 93.64 | -6.37 | 95 | 23.2 | -23.39 | -7.35 | -23.60 | 125 |
| 24 | Donchian 55/20 · 1h | breakout | 93.13 | -6.87 | 48 | 16.7 | -18.42 | -3.77 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.71 | -7.29 | 115 | 26.1 | -17.06 | -3.80 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.35 | -7.65 | 103 | 19.4 | -9.85 | -1.89 | -13.07 | 251 |
| 27 | Daily: Momentum burst | daily | 91.83 | -8.17 | 8 | 12.5 | -17.05 | -3.02 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.42 | -0.76 | -11.76 | 95 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.11 | -2.14 | -16.91 | 1 |
| 30 | Agent | meta | 90.13 | -9.87 | 97 | 39.2 | -14.53 | -6.84 | -16.03 | 261 |
| 31 | Daily: Bullish score | daily | 89.56 | -10.44 | 8 | 0.0 | -7.21 | -0.84 | -13.53 | 13 |
| 32 | Bollinger breakout · 1h | breakout | 89.52 | -10.47 | 104 | 27.9 | -11.40 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.21 | -10.79 | 101 | 22.8 | -10.88 | -1.93 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.30 | -11.70 | 0 | — | -4.12 | -0.48 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.82 | -12.18 | 46 | 34.8 | -15.84 | -3.65 | -18.01 | 128 |
| 36 | EMA 20/50 cross · 1h | trend | 87.54 | -12.46 | 68 | 11.8 | -23.25 | -4.25 | -25.26 | 142 |
| 37 | Stochastic reversion · 1h | reversion | 86.96 | -13.04 | 178 | 45.5 | -16.11 | -2.63 | -22.21 | 385 |
| 38 | Supertrend · 1h | trend | 86.85 | -13.15 | 104 | 15.4 | -24.11 | -4.72 | -27.15 | 219 |
| 39 | RSI momentum · 1h | momentum | 86.57 | -13.43 | 96 | 16.7 | -21.70 | -4.27 | -22.52 | 220 |
| 40 | Opening range 15m | breakout | 86.53 | -13.47 | 301 | 30.2 | -16.50 | -4.46 | -18.81 | 702 |
| 41 | Keltner breakout · 1h | breakout | 86.30 | -13.70 | 73 | 23.3 | -23.00 | -4.47 | -24.17 | 200 |
| 42 | Connors RSI(2) · 1h | reversion | 85.17 | -14.83 | 168 | 39.9 | -26.09 | -7.17 | -26.17 | 204 |
| 43 | MACD cross · 1h | trend | 84.77 | -15.23 | 215 | 23.3 | -28.14 | -5.11 | -29.52 | 466 |
| 44 | Triple EMA stack · 1h | trend | 84.29 | -15.71 | 96 | 15.6 | -27.71 | -5.21 | -29.84 | 222 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.74 | -23.02 | 116 |
| 46 | Z-score reversion · 1h | reversion | 82.84 | -17.16 | 104 | 33.7 | -14.19 | -2.08 | -21.32 | 198 |
| 47 | Donchian 20/10 · 1h | breakout | 82.83 | -17.17 | 93 | 20.4 | -24.63 | -4.49 | -25.41 | 226 |
| 48 | MFI reversion · 1h | reversion | 82.14 | -17.86 | 240 | 32.1 | -18.83 | -2.90 | -21.11 | 148 |
| 49 | MACD zero-line · 1h | trend | 82.12 | -17.88 | 102 | 15.7 | -25.53 | -4.86 | -26.64 | 226 |
| 50 | Three white soldiers | momentum | 82.09 | -17.91 | 264 | 20.1 | -44.93 | -18.21 | -45.15 | 597 |
| 51 | OBV trend · 1h | momentum | 82.06 | -17.95 | 198 | 17.7 | -32.51 | -6.22 | -33.09 | 308 |
| 52 | Williams %R · 1h | reversion | 81.59 | -18.41 | 204 | 44.1 | -33.76 | -5.41 | -37.91 | 526 |
| 53 | CCI reversion · 1h | reversion | 80.39 | -19.61 | 193 | 43.0 | -23.18 | -3.10 | -27.44 | 444 |
| 54 | Agent (ML meta-label) | meta | 80.03 | -19.97 | 823 | 19.1 | -14.25 | -2.57 | -16.50 | 354 |
| 55 | Heikin-Ashi · 1h | trend | 79.96 | -20.04 | 260 | 23.5 | -43.39 | -9.35 | -44.22 | 669 |
| 56 | Bollinger reversion · 1h | reversion | 79.82 | -20.18 | 168 | 35.1 | -31.27 | -6.02 | -32.58 | 362 |
| 57 | ROC + volume · 1h | momentum | 79.44 | -20.56 | 231 | 24.2 | -28.95 | -5.24 | -29.22 | 378 |
| 58 | EMA 9/21 cross · 1h | trend | 77.90 | -22.10 | 155 | 11.6 | -32.01 | -6.11 | -32.90 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 77.66 | -22.34 | 90 | 23.3 | -20.38 | -3.80 | -23.46 | 177 |
| 60 | Candlestick reversal · 1h | reversion | 77.23 | -22.77 | 240 | 29.6 | -37.60 | -6.50 | -39.63 | 564 |
| 61 | VWAP momentum · 1h | momentum | 76.77 | -23.23 | 499 | 21.4 | -50.32 | -10.31 | -51.15 | 1232 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.79 | -2.85 | -48.56 | 43 |
| 63 | ROC + volume | momentum | 59.10 | -40.90 | 690 | 23.2 | -78.35 | -22.05 | -79.61 | 1674 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.88 | -20.60 | -65.25 | 853 |
| 65 | Donchian 55/20 | breakout | 56.34 | -43.66 | 538 | 19.7 | -72.57 | -20.38 | -74.14 | 1265 |
| 66 | Squeeze breakout | breakout | 55.20 | -44.80 | 529 | 14.0 | -67.29 | -23.35 | -68.30 | 1195 |
| 67 | EMA 20/50 cross | trend | 54.18 | -45.82 | 584 | 20.2 | -79.71 | -21.09 | -79.74 | 1438 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.63 | -17.17 | -76.88 | 1673 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.38 | -14.60 | -73.53 | 1523 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -32.14 | -98.88 | 5261 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.32 | -35.45 | -94.35 | 2563 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.39 | -25.01 | -89.12 | 1891 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.53 | -29.93 | -91.98 | 2338 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.94 | -25.32 | -91.02 | 2212 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.81 | -36.27 | -97.94 | 3490 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.98 | -39.44 | -97.09 | 3536 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -28.51 | -94.35 | 2537 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.13 | -28.62 | -83.55 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -37.44 | -99.49 | 5874 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.54 | -30.51 | -93.10 | 2611 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -30.99 | -95.68 | 3425 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -44.55 | -99.79 | 6189 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.17 | -32.88 | -92.17 | 2325 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.70 | -40.32 | -97.75 | 3581 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -39.05 | -98.65 | 4762 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.38 | -35.97 | -94.72 | 2779 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.53 | -28.52 | -84.55 | 1781 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -41.31 | -99.60 | 6231 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.02 | -24.00 | -88.08 | 2194 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.76 | -27.03 | -88.88 | 2190 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.24 | -34.72 | -96.28 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.60 | -35.08 | -89.85 | 2101 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.21 | -35.27 | -96.22 | 4140 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -46.88 | -99.91 | 8236 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T19:15 | Agent (ML meta-label) | buy | AMZN | 5.64 | — | rebalance up |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | TQQQ | 5.00 | -0.01 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | TECL | 4.72 | 0.01 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | SQQQ | 4.70 | -0.01 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | META | 3.36 | -0.01 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | LABU | 4.75 | 0.04 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | GOOGL | 1.38 | -0.00 | selected signal exited |
| 2026-10-22T19:15 | Agent (ML meta-label) | sell | ETH-USD | 4.18 | -0.02 | selected signal exited |
| 2026-10-22T19:15 | ROC + volume | sell | ETHU | 14.76 | -0.02 | target is flat |
| 2026-10-22T19:10 | Agent (ML meta-label) | buy | META | 3.37 | — | entry |
| 2026-10-22T19:10 | Agent (ML meta-label) | buy | ETH-USD | 4.20 | — | entry |
| 2026-10-22T19:10 | Agent (ML meta-label) | sell | UPRO | 4.71 | -0.00 | selected signal exited |
| 2026-10-22T19:10 | Agent (ML meta-label) | sell | SPY | 2.86 | -0.01 | selected signal exited |
| 2026-10-22T19:10 | MFI reversion · 1h | buy | AMD | 8.27 | — | entry |
| 2026-10-22T19:10 | MFI reversion · 1h | sell | SOL-USD | 4.14 | -0.05 | rebalance down |
| 2026-10-22T19:10 | MFI reversion · 1h | sell | QQQ | 4.13 | -0.03 | rebalance down |
| 2026-10-22T19:10 | Three white soldiers | sell | COIN | 20.46 | -0.08 | exit signal |
| 2026-10-22T19:05 | OBV trend · 1h | buy | TNA | 19.68 | — | entry |
| 2026-10-22T19:05 | Squeeze breakout | buy | AAPL | 13.81 | — | entry signal |
| 2026-10-22T19:05 | ROC + volume | buy | ETHU | 14.78 | — | entry signal |
| 2026-10-22T19:00 | Agent (ML meta-label) | buy | GOOGL | 1.39 | — | entry |
| 2026-10-22T19:00 | Williams %R · 1h | buy | XRP-USD | 8.14 | — | entry |
| 2026-10-22T19:00 | Williams %R · 1h | buy | ETH-USD | 8.17 | — | entry |
| 2026-10-22T19:00 | Williams %R · 1h | buy | DOGE-USD | 8.17 | — | entry signal |
| 2026-10-22T19:00 | Williams %R · 1h | buy | BTC-USD | 8.17 | — | entry signal |
| 2026-10-22T19:00 | Williams %R · 1h | sell | UPRO | 5.36 | -0.07 | rebalance down |
| 2026-10-22T19:00 | Williams %R · 1h | sell | TNA | 5.51 | -0.00 | rebalance down |
| 2026-10-22T19:00 | Williams %R · 1h | sell | SPY | 5.45 | -0.03 | rebalance down |
| 2026-10-22T19:00 | Williams %R · 1h | sell | SOL-USD | 5.46 | -0.07 | rebalance down |
| 2026-10-22T19:00 | Williams %R · 1h | sell | MSFT | 5.39 | -0.05 | rebalance down |
| 2026-10-22T19:00 | Williams %R · 1h | sell | IWM | 5.48 | -0.02 | rebalance down |
| 2026-10-22T19:00 | VWAP reversion · 1h | buy | ETH-USD | 25.17 | — | entry signal |
| 2026-10-22T19:00 | VWAP reversion · 1h | buy | BTC-USD | 25.17 | — | entry signal |
| 2026-10-22T19:00 | Z-score reversion · 1h | buy | ETH-USD | 13.00 | — | entry signal |
| 2026-10-22T19:00 | Z-score reversion · 1h | buy | DOGE-USD | 16.59 | — | entry signal |
| 2026-10-22T19:00 | Z-score reversion · 1h | sell | MSFT | 4.29 | -0.05 | rebalance down |
| 2026-10-22T19:00 | Z-score reversion · 1h | sell | AMD | 4.20 | -0.07 | rebalance down |
| 2026-10-22T19:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.37 | — | entry signal |
| 2026-10-22T19:00 | Candlestick reversal · 1h | buy | ETH-USD | 7.73 | — | entry signal |
| 2026-10-22T19:00 | Candlestick reversal · 1h | buy | DOGE-USD | 7.73 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 19:15:05.000119+00:00 -> 2026-10-22 19:25:05.000119+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
