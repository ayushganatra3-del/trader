# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T18:15:05.000148+00:00 · 32128 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.94 (-10.06%)

Closed trades 96, win rate 39.6%, fees £3.12, max drawdown -10.53%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 17.91 | -0.13 |
| ETHU | 17.96 | -0.00 |

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

Today: 30756 decisions in 2688 calls, $0.3832 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T18:15 | 1 / 7 / 21 | AAPL 15% |  |
| Breezy | 2026-10-22T18:15 | 0 / 22 / 7 | cash |  |
| Boozy | 2026-10-22T18:15 | 2 / 19 / 8 | cash |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.67 | 7.67 | 0 | — | 10.43 | 4.61 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.01 | 6.01 | 12 | 66.7 | 3.13 | 0.98 | -7.48 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.01 | 5.01 | 15 | 46.7 | 7.69 | 2.34 | -4.92 | 24 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 5 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 78 | 46.2 | -10.06 | -2.69 | -13.79 | 135 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.30 | 0.30 | 0 | — | 3.81 | 1.67 | -5.02 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.86 | -1.14 | 69 | 34.8 | 2.02 | 1.22 | -2.29 | 68 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 11 | Hold SPY | benchmark | 97.99 | -2.01 | 0 | — | -0.49 | -0.22 | -3.13 | 1 |
| 12 | Max aggression: 5-day momentum | meta | 97.52 | -2.48 | 10 | 50.0 | -17.65 | -1.41 | -34.64 | 26 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.40 | -1.95 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.42 | -3.58 | 117 | 30.8 | -9.05 | -4.89 | -10.21 | 268 |
| 15 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.21 | 0.74 | -7.93 | 8 |
| 16 | Hold BTC | benchmark | 95.63 | -4.37 | 0 | — | 4.73 | 0.87 | -8.68 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 95.61 | -4.39 | 0 | — | -0.87 | -0.28 | -5.45 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.66 | -2.93 | -5.48 | 30 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 94.91 | -5.09 | 0 | — | -5.22 | -1.90 | -7.17 | 1 |
| 20 | Gap and go | momentum | 94.48 | -5.52 | 90 | 22.2 | 6.41 | 2.00 | -7.38 | 198 |
| 21 | Copy: Insider buying | copy | 93.91 | -6.09 | 25 | 40.0 | -13.77 | -2.36 | -20.62 | 72 |
| 22 | Opening range 30m | breakout | 93.77 | -6.24 | 237 | 35.0 | -10.18 | -2.87 | -17.26 | 558 |
| 23 | Trend pullback · 1h | trend | 93.69 | -6.31 | 94 | 23.4 | -23.35 | -7.28 | -23.60 | 125 |
| 24 | Donchian 55/20 · 1h | breakout | 93.05 | -6.95 | 48 | 16.7 | -18.51 | -3.75 | -19.70 | 104 |
| 25 | Parabolic SAR · 1h | trend | 92.51 | -7.49 | 115 | 26.1 | -17.28 | -3.82 | -20.59 | 265 |
| 26 | ADX DI cross · 1h | trend | 92.14 | -7.86 | 103 | 19.4 | -9.71 | -1.85 | -12.72 | 250 |
| 27 | Daily: Momentum burst | daily | 91.73 | -8.28 | 8 | 12.5 | -17.44 | -3.08 | -20.58 | 39 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -4.56 | -1.06 | -11.76 | 97 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.98 | -2.09 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 90.05 | -9.95 | 8 | 0.0 | -6.63 | -0.75 | -13.10 | 13 |
| 31 | Agent | meta | 89.94 | -10.06 | 96 | 39.6 | -18.59 | -6.42 | -21.78 | 307 |
| 32 | Bollinger breakout · 1h | breakout | 89.44 | -10.56 | 104 | 27.9 | -11.49 | -2.04 | -15.91 | 257 |
| 33 | Volume breakout · 1h | breakout | 89.13 | -10.87 | 101 | 22.8 | -10.97 | -1.93 | -12.44 | 105 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 88.40 | -11.60 | 0 | — | -5.44 | -0.68 | -14.37 | 1 |
| 35 | Agent (aggressive) | meta | 87.57 | -12.43 | 46 | 34.8 | -18.58 | -4.60 | -22.79 | 135 |
| 36 | EMA 20/50 cross · 1h | trend | 87.42 | -12.58 | 68 | 11.8 | -23.41 | -4.24 | -25.32 | 143 |
| 37 | Stochastic reversion · 1h | reversion | 87.11 | -12.89 | 178 | 45.5 | -16.02 | -2.60 | -22.21 | 383 |
| 38 | Supertrend · 1h | trend | 86.88 | -13.12 | 104 | 15.4 | -24.30 | -4.71 | -27.31 | 219 |
| 39 | RSI momentum · 1h | momentum | 86.54 | -13.46 | 95 | 16.8 | -20.57 | -3.95 | -22.44 | 218 |
| 40 | Opening range 15m | breakout | 86.46 | -13.54 | 301 | 30.2 | -16.59 | -4.44 | -18.82 | 702 |
| 41 | Keltner breakout · 1h | breakout | 86.22 | -13.78 | 73 | 23.3 | -23.44 | -4.53 | -24.35 | 201 |
| 42 | Connors RSI(2) · 1h | reversion | 85.34 | -14.66 | 168 | 39.9 | -25.96 | -7.13 | -26.02 | 204 |
| 43 | MACD cross · 1h | trend | 84.83 | -15.17 | 215 | 23.3 | -26.73 | -4.93 | -28.19 | 467 |
| 44 | Triple EMA stack · 1h | trend | 84.24 | -15.76 | 96 | 15.6 | -29.01 | -5.45 | -29.73 | 221 |
| 45 | Ichimoku · 1h | trend | 83.82 | -16.18 | 65 | 12.3 | -20.38 | -3.72 | -23.02 | 116 |
| 46 | Z-score reversion · 1h | reversion | 83.34 | -16.66 | 104 | 33.7 | -14.25 | -2.16 | -21.32 | 198 |
| 47 | Donchian 20/10 · 1h | breakout | 82.89 | -17.11 | 92 | 20.7 | -24.61 | -4.46 | -25.29 | 226 |
| 48 | MFI reversion · 1h | reversion | 82.33 | -17.67 | 237 | 32.1 | -18.69 | -2.86 | -21.11 | 149 |
| 49 | MACD zero-line · 1h | trend | 82.25 | -17.75 | 102 | 15.7 | -24.57 | -4.68 | -25.75 | 225 |
| 50 | Three white soldiers | momentum | 82.17 | -17.83 | 263 | 20.2 | -44.88 | -17.94 | -45.15 | 596 |
| 51 | OBV trend · 1h | momentum | 81.90 | -18.10 | 198 | 17.7 | -32.79 | -6.23 | -33.21 | 306 |
| 52 | Williams %R · 1h | reversion | 81.77 | -18.23 | 204 | 44.1 | -33.62 | -5.33 | -37.92 | 523 |
| 53 | Agent (ML meta-label) | meta | 80.14 | -19.86 | 800 | 19.2 | -12.70 | -2.28 | -17.57 | 378 |
| 54 | Bollinger reversion · 1h | reversion | 80.09 | -19.91 | 168 | 35.1 | -31.04 | -5.96 | -32.60 | 360 |
| 55 | CCI reversion · 1h | reversion | 80.06 | -19.94 | 193 | 43.0 | -23.52 | -3.13 | -27.44 | 444 |
| 56 | Heikin-Ashi · 1h | trend | 79.88 | -20.12 | 260 | 23.5 | -43.33 | -9.22 | -44.09 | 670 |
| 57 | ROC + volume · 1h | momentum | 79.41 | -20.59 | 231 | 24.2 | -28.97 | -5.20 | -29.11 | 378 |
| 58 | EMA 9/21 cross · 1h | trend | 77.81 | -22.19 | 155 | 11.6 | -32.12 | -6.07 | -32.90 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 77.79 | -22.21 | 90 | 23.3 | -17.63 | -3.13 | -23.32 | 176 |
| 60 | Candlestick reversal · 1h | reversion | 77.29 | -22.71 | 240 | 29.6 | -36.59 | -6.06 | -38.23 | 561 |
| 61 | VWAP momentum · 1h | momentum | 76.65 | -23.34 | 499 | 21.4 | -50.34 | -10.22 | -51.09 | 1230 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -43.45 | -2.81 | -48.26 | 43 |
| 63 | ROC + volume | momentum | 59.12 | -40.88 | 689 | 23.2 | -77.73 | -21.06 | -79.29 | 1678 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.25 | -19.26 | -65.21 | 853 |
| 65 | Donchian 55/20 | breakout | 56.29 | -43.71 | 538 | 19.7 | -72.88 | -20.29 | -74.13 | 1267 |
| 66 | Squeeze breakout | breakout | 55.28 | -44.72 | 528 | 14.0 | -67.24 | -22.91 | -68.25 | 1197 |
| 67 | EMA 20/50 cross | trend | 54.18 | -45.82 | 584 | 20.2 | -79.58 | -20.73 | -79.61 | 1434 |
| 68 | RSI(14) reversion ⏸ | reversion | 53.15 | -46.85 | 807 | 26.0 | -76.42 | -16.84 | -76.65 | 1668 |
| 69 | VWAP reversion ⏸ | reversion | 51.01 | -48.99 | 804 | 25.1 | -73.27 | -14.39 | -73.41 | 1518 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.82 | -31.23 | -98.88 | 5270 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -94.19 | -34.80 | -94.39 | 2565 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.36 | -24.54 | -89.08 | 1890 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.58 | -29.24 | -92.00 | 2346 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.00 | -25.01 | -91.06 | 2218 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -34.42 | -97.93 | 3488 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.93 | -37.64 | -97.07 | 3546 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.45 | -27.99 | -94.48 | 2545 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.13 | -28.01 | -83.53 | 1718 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.48 | -36.32 | -99.49 | 5856 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.35 | -29.34 | -93.00 | 2612 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.65 | -30.21 | -95.68 | 3431 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -42.56 | -99.78 | 6175 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.06 | -31.29 | -92.18 | 2322 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -39.21 | -97.76 | 3584 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.64 | -37.72 | -98.65 | 4755 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.29 | -34.32 | -94.68 | 2782 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.16 | -27.02 | -84.44 | 1783 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -39.69 | -99.59 | 6220 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.01 | -23.58 | -88.07 | 2186 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.73 | -26.73 | -88.84 | 2199 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.23 | -33.70 | -96.26 | 3807 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.56 | -33.62 | -89.85 | 2103 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.22 | -34.29 | -96.22 | 4132 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.09 | -99.91 | 8237 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T18:15 | Agent (ML meta-label) | buy | MSTR | 5.34 | — | entry |
| 2026-10-22T18:15 | Agent (ML meta-label) | sell | QQQ | 3.25 | -0.01 | selected signal exited |
| 2026-10-22T18:15 | Agent (ML meta-label) | sell | MSFT | 4.01 | -0.00 | selected signal exited |
| 2026-10-22T18:15 | Agent (ML meta-label) | sell | GOOGL | 4.52 | -0.04 | selected signal exited |
| 2026-10-22T18:15 | Donchian 55/20 | buy | AAPL | 14.07 | — | entry signal |
| 2026-10-22T18:10 | Agent (ML meta-label) | buy | MSFT | 4.01 | — | entry |
| 2026-10-22T18:10 | Agent (ML meta-label) | sell | PLTR | 4.03 | -0.04 | rebalance down |
| 2026-10-22T18:10 | Agent | sell | ETHU | 18.00 | 0.03 | rebalance down |
| 2026-10-22T18:05 | MFI reversion · 1h | buy | TECL | 8.46 | — | rebalance up |
| 2026-10-22T18:05 | MFI reversion · 1h | sell | XRP-USD | 13.65 | -0.30 | stop-loss |
| 2026-10-22T18:05 | CCI reversion · 1h | buy | SOL-USD | 6.62 | — | rebalance up |
| 2026-10-22T18:05 | CCI reversion · 1h | buy | DOGE-USD | 6.73 | — | rebalance up |
| 2026-10-22T18:05 | CCI reversion · 1h | buy | BTC-USD | 6.60 | — | rebalance up |
| 2026-10-22T18:05 | CCI reversion · 1h | buy | BITX | 6.72 | — | rebalance up |
| 2026-10-22T18:05 | CCI reversion · 1h | sell | XRP-USD | 13.24 | -0.35 | stop-loss |
| 2026-10-22T18:05 | VWAP reversion · 1h | sell | XRP-USD | 24.99 | -0.57 | stop-loss |
| 2026-10-22T18:05 | Candlestick reversal · 1h | buy | ETHU | 11.05 | — | rebalance up |
| 2026-10-22T18:05 | Candlestick reversal · 1h | sell | XRP-USD | 12.73 | -0.26 | stop-loss |
| 2026-10-22T18:05 | Opening range 15m | sell | IWM | 17.26 | -0.13 | stop-loss |
| 2026-10-22T17:50 | MFI reversion · 1h | buy | TECL | 5.30 | — | entry |
| 2026-10-22T17:50 | MFI reversion · 1h | buy | SOXL | 11.82 | — | entry |
| 2026-10-22T17:50 | MFI reversion · 1h | sell | GOOGL | 11.78 | -0.06 | target is flat |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 18:15:05.000148+00:00 -> 2026-10-22 18:25:05.000148+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
