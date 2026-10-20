# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T14:26:05.000138+00:00 · 29599 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.97 (-9.03%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.54 | +0.26 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-19)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 25.56 · VIX 18.44 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.0, MSFT 6.7, AMZN 6.3, AAPL 5.7, SQQQ 5.7, BITX 4.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 14580 decisions in 2100 calls, $0.1927 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T14:26 | 6 / 19 / 6 | NANC 18%, ARKK 15% |  |
| Breezy | 2026-10-20T14:26 | 0 / 30 / 1 | cash |  |
| Boozy | 2026-10-20T14:26 | 8 / 22 / 1 | MSTR 78% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | BITX | 1.97 | +3.69% | 6 |
| VWAP reversion | ETHU | 1.90 | +4.27% | 5 |
| Opening range 15m | TSLA | 1.79 | +1.65% | 3 |
| Opening range 30m | TSLA | 1.79 | +1.65% | 3 |
| Bollinger reversion | ETHU | 1.76 | +6.38% | 11 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 105.23 | 5.23 | 0 | — | 6.29 | 3.02 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.43 | -0.03 | -8.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 102.68 | 2.68 | 9 | 44.4 | -11.65 | -0.74 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.27 | -0.73 | 0 | — | -0.11 | -0.01 | -3.13 | 1 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.26 | -0.74 | 0 | — | 0.27 | 0.20 | -5.18 | 1 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.95 | -1.05 | 3 | 33.3 | 6.24 | 1.36 | -7.93 | 8 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.70 | -1.30 | 58 | 34.5 | 2.30 | 1.32 | -1.45 | 61 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 98.07 | -1.93 | 0 | — | 21.03 | 2.77 | -8.68 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.61 | -2.39 | 37 | 16.2 | -12.39 | -2.35 | -19.72 | 97 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.49 | -1.95 | -5.83 | 1 |
| 17 | Agent (rotation) | meta | 96.77 | -3.23 | 113 | 31.9 | -6.31 | -3.15 | -7.73 | 317 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.63 | -3.37 | 0 | — | -1.05 | -0.38 | -5.31 | 1 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 95.98 | -4.02 | 0 | — | -4.81 | -1.89 | -7.04 | 1 |
| 20 | Copy: Insider buying | copy | 95.78 | -4.22 | 23 | 43.5 | -11.99 | -2.06 | -20.62 | 72 |
| 21 | Trend pullback · 1h | trend | 95.64 | -4.36 | 89 | 23.6 | -20.40 | -6.09 | -20.51 | 135 |
| 22 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 23 | ADX DI cross · 1h | trend | 94.80 | -5.21 | 88 | 18.2 | -15.14 | -2.76 | -17.19 | 258 |
| 24 | Daily: Momentum burst | daily | 94.20 | -5.79 | 6 | 16.7 | -5.01 | -0.60 | -20.58 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.51 | -0.28 | -9.46 | 95 |
| 26 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.29 | 1.37 | -6.51 | 198 |
| 27 | Opening range 30m | breakout | 92.55 | -7.45 | 207 | 29.5 | -13.02 | -3.74 | -17.26 | 565 |
| 28 | Parabolic SAR · 1h | trend | 92.11 | -7.89 | 105 | 21.9 | -17.94 | -3.89 | -23.77 | 274 |
| 29 | Volume breakout · 1h | breakout | 91.83 | -8.17 | 79 | 24.1 | -13.07 | -2.34 | -16.86 | 101 |
| 30 | Daily: Bullish score | daily | 91.61 | -8.39 | 7 | 0.0 | -6.68 | -0.72 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 91.35 | -8.65 | 84 | 28.6 | -9.38 | -1.62 | -16.84 | 254 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -11.33 | -2.11 | -16.91 | 1 |
| 33 | Agent | meta | 90.97 | -9.03 | 87 | 40.2 | -8.68 | -4.19 | -14.03 | 265 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.39 | -9.61 | 0 | — | 0.70 | 0.27 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 89.77 | -10.23 | 60 | 13.3 | -17.71 | -3.29 | -19.70 | 127 |
| 36 | Connors RSI(2) · 1h | reversion | 89.45 | -10.55 | 150 | 41.3 | -22.34 | -6.59 | -23.84 | 203 |
| 37 | RSI momentum · 1h | momentum | 89.23 | -10.77 | 82 | 15.9 | -22.48 | -4.46 | -24.84 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 88.85 | -11.15 | 155 | 45.8 | -15.32 | -2.59 | -22.24 | 364 |
| 39 | Opening range 15m | breakout | 88.64 | -11.36 | 256 | 25.8 | -17.56 | -4.65 | -20.98 | 700 |
| 40 | Supertrend · 1h | trend | 88.52 | -11.48 | 88 | 12.5 | -21.69 | -4.36 | -26.86 | 214 |
| 41 | Ichimoku · 1h | trend | 88.49 | -11.51 | 57 | 14.0 | -17.74 | -3.35 | -18.21 | 114 |
| 42 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -13.10 | -3.77 | -14.88 | 133 |
| 43 | Keltner breakout · 1h | breakout | 87.71 | -12.29 | 56 | 23.2 | -18.15 | -3.14 | -28.31 | 198 |
| 44 | Triple EMA stack · 1h | trend | 86.58 | -13.42 | 88 | 14.8 | -27.87 | -4.87 | -34.27 | 231 |
| 45 | MACD cross · 1h | trend | 86.47 | -13.53 | 192 | 20.3 | -27.55 | -5.33 | -33.50 | 474 |
| 46 | MFI reversion · 1h | reversion | 85.21 | -14.79 | 210 | 31.0 | -14.88 | -2.31 | -20.43 | 139 |
| 47 | Z-score reversion · 1h | reversion | 85.07 | -14.93 | 94 | 29.8 | -13.94 | -2.28 | -21.32 | 198 |
| 48 | OBV trend · 1h | momentum | 84.87 | -15.13 | 181 | 17.7 | -28.56 | -4.96 | -35.68 | 325 |
| 49 | MACD zero-line · 1h | trend | 84.51 | -15.49 | 87 | 14.9 | -23.97 | -4.61 | -25.37 | 219 |
| 50 | Donchian 20/10 · 1h | breakout | 84.44 | -15.56 | 81 | 17.3 | -12.24 | -1.53 | -27.92 | 214 |
| 51 | Agent (ML meta-label) | meta | 84.08 | -15.92 | 690 | 19.0 | -15.85 | -3.02 | -20.56 | 383 |
| 52 | Three white soldiers | momentum | 83.17 | -16.83 | 236 | 19.1 | -46.88 | -17.77 | -47.99 | 613 |
| 53 | Bollinger reversion · 1h | reversion | 82.30 | -17.70 | 162 | 35.8 | -28.13 | -5.39 | -33.53 | 352 |
| 54 | Williams %R · 1h | reversion | 82.11 | -17.89 | 188 | 42.6 | -32.81 | -5.17 | -36.49 | 532 |
| 55 | ROC + volume · 1h | momentum | 81.78 | -18.22 | 198 | 21.2 | -25.23 | -4.25 | -33.88 | 381 |
| 56 | CCI reversion · 1h | reversion | 81.07 | -18.93 | 169 | 39.1 | -16.68 | -2.03 | -27.44 | 443 |
| 57 | Heikin-Ashi · 1h | trend | 80.06 | -19.94 | 228 | 21.1 | -40.98 | -8.65 | -45.31 | 680 |
| 58 | RSI(14) reversion · 1h | reversion | 80.06 | -19.94 | 80 | 20.0 | -18.78 | -3.63 | -23.28 | 165 |
| 59 | EMA 9/21 cross · 1h | trend | 79.89 | -20.11 | 140 | 10.7 | -29.31 | -6.09 | -30.09 | 316 |
| 60 | VWAP momentum · 1h | momentum | 78.62 | -21.38 | 437 | 20.6 | -41.46 | -6.79 | -48.90 | 1249 |
| 61 | Candlestick reversal · 1h | reversion | 77.67 | -22.33 | 218 | 28.0 | -35.53 | -6.49 | -39.13 | 524 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.66 | -1.59 | -40.75 | 42 |
| 63 | ROC + volume | momentum | 62.89 | -37.11 | 601 | 22.3 | -76.70 | -18.99 | -78.78 | 1729 |
| 64 | Volume breakout | breakout | 62.20 | -37.80 | 365 | 13.2 | -62.84 | -18.40 | -64.23 | 870 |
| 65 | Squeeze breakout | breakout | 59.55 | -40.45 | 481 | 13.7 | -63.86 | -19.26 | -66.58 | 1211 |
| 66 | Donchian 55/20 | breakout | 58.43 | -41.57 | 488 | 18.0 | -69.64 | -16.42 | -73.50 | 1285 |
| 67 | RSI(14) reversion | reversion | 57.66 | -42.34 | 736 | 26.2 | -74.42 | -16.38 | -75.04 | 1621 |
| 68 | EMA 20/50 cross | trend | 56.46 | -43.54 | 525 | 19.4 | -77.15 | -16.22 | -80.87 | 1432 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.62 | -14.61 | -72.28 | 1502 |
| 70 | Keltner breakout | breakout | 51.41 | -48.59 | 681 | 16.0 | -82.56 | -25.18 | -83.82 | 1806 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -29.94 | -98.76 | 5326 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.37 | -30.24 | -93.86 | 2577 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.57 | -20.44 | -88.38 | 1903 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.16 | -24.15 | -91.32 | 2356 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.90 | -25.32 | -91.22 | 2252 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -31.86 | -97.64 | 3505 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.66 | -35.39 | -96.85 | 3586 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -27.81 | -94.52 | 2517 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.39 | -26.04 | -82.93 | 1692 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.92 | -99.38 | 5753 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.33 | -25.89 | -92.18 | 2627 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.18 | -95.90 | 3440 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.38 | -99.76 | 6211 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.42 | -28.41 | -91.67 | 2342 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.56 | -36.47 | -97.72 | 3618 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.23 | -98.49 | 4716 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.81 | -32.51 | -94.15 | 2800 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.59 | -99.53 | 6177 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.78 | -22.25 | -87.09 | 2162 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.77 | -25.95 | -88.24 | 2152 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.34 | -95.99 | 3769 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.81 | -31.49 | -89.26 | 2118 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.07 | -95.84 | 4112 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.72 | -99.90 | 8274 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T14:20 | Agent (aggressive) | sell | TSLA | 44.08 | 0.07 | selected signal exited |
| 2026-10-20T14:20 | RSI(14) reversion | buy | MSFT | 6.18 | — | rebalance up |
| 2026-10-20T14:20 | RSI(14) reversion | buy | META | 8.00 | — | rebalance up |
| 2026-10-20T14:20 | RSI(14) reversion | buy | GOOGL | 6.19 | — | rebalance up |
| 2026-10-20T14:20 | RSI(14) reversion | buy | AAPL | 6.20 | — | rebalance up |
| 2026-10-20T14:20 | RSI(14) reversion | sell | PLTR | 8.26 | 0.07 | exit signal |
| 2026-10-20T14:20 | RSI(14) reversion | sell | NVDA | 8.25 | 0.06 | take-profit |
| 2026-10-20T14:20 | RSI(14) reversion | sell | AMZN | 8.22 | 0.01 | exit signal |
| 2026-10-20T14:20 | Keltner breakout | buy | TSLA | 3.43 | — | entry |
| 2026-10-20T14:20 | Keltner breakout | buy | SPY | 3.43 | — | entry |
| 2026-10-20T14:20 | Keltner breakout | buy | MSTR | 3.43 | — | entry |
| 2026-10-20T14:20 | Keltner breakout | buy | ETHU | 3.43 | — | entry |
| 2026-10-20T14:20 | Keltner breakout | buy | COIN | 3.43 | — | entry |
| 2026-10-20T14:20 | Keltner breakout | sell | TNA | 2.93 | 0.05 | rebalance down |
| 2026-10-20T14:20 | Keltner breakout | sell | SOL-USD | 3.05 | 0.05 | rebalance down |
| 2026-10-20T14:20 | Keltner breakout | sell | LABU | 3.03 | 0.16 | rebalance down |
| 2026-10-20T14:20 | Keltner breakout | sell | IWM | 2.92 | 0.02 | rebalance down |
| 2026-10-20T14:20 | Keltner breakout | sell | ETH-USD | 3.02 | 0.04 | rebalance down |
| 2026-10-20T14:20 | Keltner breakout | sell | BTC-USD | 2.98 | 0.02 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | buy | UPRO | 4.94 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | buy | TNA | 5.14 | — | entry signal |
| 2026-10-20T14:20 | Opening range 30m | buy | SPY | 5.14 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | buy | PLTR | 5.14 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | buy | NVDA | 5.14 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | buy | LABU | 5.14 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | buy | IWM | 5.14 | — | entry signal |
| 2026-10-20T14:20 | Opening range 30m | buy | GOOGL | 5.14 | — | entry |
| 2026-10-20T14:20 | Opening range 30m | sell | TSLA | 5.02 | 0.03 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | TQQQ | 5.09 | 0.06 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | TECL | 5.15 | 0.09 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | SOXL | 5.20 | 0.12 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | QQQ | 5.00 | 0.02 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | MSTR | 5.23 | 0.13 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | BITX | 5.12 | 0.07 | rebalance down |
| 2026-10-20T14:20 | Opening range 30m | sell | AMD | 5.08 | 0.05 | rebalance down |
| 2026-10-20T14:20 | Donchian 55/20 | buy | UPRO | 3.90 | — | entry signal |
| 2026-10-20T14:20 | Donchian 55/20 | buy | TSLA | 3.90 | — | entry |
| 2026-10-20T14:20 | Donchian 55/20 | buy | SPY | 3.90 | — | entry |
| 2026-10-20T14:20 | Donchian 55/20 | buy | SOL-USD | 3.90 | — | entry |
| 2026-10-20T14:20 | Donchian 55/20 | buy | MSTR | 3.90 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 14:26:05.000138+00:00 -> 2026-10-20 14:36:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
