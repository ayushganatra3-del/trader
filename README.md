# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-20T14:54:05.000175+00:00 · 29627 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.12 (-8.88%)

Closed trades 87, win rate 40.2%, fees £2.92, max drawdown -9.99%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| TSLA | 36.69 | +0.41 |

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

Today: 17121 decisions in 2184 calls, $0.2223 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-20T14:54 | 8 / 17 / 5 | cash |  |
| Breezy | 2026-10-20T14:54 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-20T14:54 | 8 / 21 / 1 | MSTR 71% |  |

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
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.29 | 6.29 | 11 | 63.6 | 8.70 | 2.89 | -3.27 | 20 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 105.34 | 5.34 | 0 | — | 6.87 | 3.29 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | -0.91 | -0.17 | -9.24 | 27 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.32 | 4.32 | 17 | 35.3 | 5.95 | 1.52 | -7.11 | 43 |
| 5 | Max aggression: 5-day momentum | meta | 102.51 | 2.51 | 9 | 44.4 | -11.65 | -0.74 | -34.64 | 26 |
| 6 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.17 | -2.22 | -13.79 | 133 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.18 | -0.82 | 0 | — | 0.10 | 0.10 | -3.13 | 1 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.13 | -0.87 | 3 | 33.3 | 5.37 | 1.20 | -7.93 | 8 |
| 11 | Daily: SMA 20/50 cross · AAPL | daily | 99.01 | -0.99 | 0 | — | -0.01 | 0.08 | -5.18 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.74 | -1.26 | 58 | 34.5 | 2.45 | 1.40 | -1.45 | 61 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.40 | -1.60 | 11 | 27.3 | -3.69 | -4.02 | -3.91 | 21 |
| 14 | Hold BTC | benchmark | 98.01 | -1.99 | 0 | — | 21.16 | 2.78 | -8.68 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.31 | -2.69 | 37 | 16.2 | -12.58 | -2.39 | -19.72 | 98 |
| 16 | Copy: Congress Democrats (NANC) | copy | 97.17 | -2.83 | 0 | — | 0.29 | 0.18 | -5.31 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.86 | -2.18 | -5.83 | 1 |
| 18 | Agent (rotation) | meta | 96.53 | -3.47 | 113 | 31.9 | -6.59 | -3.27 | -8.05 | 324 |
| 19 | Copy: Insider buying | copy | 95.97 | -4.03 | 23 | 43.5 | -11.11 | -1.89 | -20.62 | 72 |
| 20 | Copy: Hedge-fund gurus (GURU) | copy | 95.82 | -4.18 | 0 | — | -4.81 | -1.89 | -7.04 | 1 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Trend pullback · 1h | trend | 95.44 | -4.56 | 89 | 23.6 | -20.50 | -6.13 | -20.69 | 135 |
| 23 | ADX DI cross · 1h | trend | 94.88 | -5.12 | 89 | 18.0 | -12.63 | -2.23 | -16.43 | 261 |
| 24 | Daily: Momentum burst | daily | 94.71 | -5.29 | 6 | 16.7 | -4.13 | -0.46 | -20.58 | 40 |
| 25 | Squeeze breakout · 1h | breakout | 93.46 | -6.54 | 42 | 23.8 | -1.98 | -0.41 | -9.46 | 97 |
| 26 | Gap and go | momentum | 93.43 | -6.57 | 78 | 17.9 | 4.32 | 1.38 | -6.51 | 198 |
| 27 | Opening range 30m | breakout | 92.96 | -7.04 | 208 | 29.3 | -12.49 | -3.51 | -17.26 | 565 |
| 28 | Parabolic SAR · 1h | trend | 92.09 | -7.92 | 105 | 21.9 | -16.61 | -3.53 | -22.67 | 276 |
| 29 | Volume breakout · 1h | breakout | 91.86 | -8.13 | 79 | 24.1 | -13.49 | -2.39 | -17.83 | 104 |
| 30 | Daily: Bullish score | daily | 91.56 | -8.44 | 7 | 0.0 | -6.98 | -0.76 | -13.10 | 13 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 91.47 | -8.53 | 0 | — | 1.73 | 0.43 | -14.37 | 1 |
| 32 | Bollinger breakout · 1h | breakout | 91.39 | -8.61 | 84 | 28.6 | -8.88 | -1.51 | -16.92 | 258 |
| 33 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.36 | -2.34 | -16.91 | 1 |
| 34 | Agent | meta | 91.12 | -8.88 | 87 | 40.2 | -9.53 | -4.85 | -14.03 | 255 |
| 35 | EMA 20/50 cross · 1h | trend | 89.65 | -10.35 | 60 | 13.3 | -19.65 | -3.58 | -21.64 | 128 |
| 36 | Connors RSI(2) · 1h | reversion | 89.41 | -10.59 | 150 | 41.3 | -22.56 | -6.68 | -24.01 | 203 |
| 37 | RSI momentum · 1h | momentum | 89.28 | -10.72 | 82 | 15.9 | -24.35 | -4.70 | -26.83 | 216 |
| 38 | Opening range 15m | breakout | 89.14 | -10.86 | 256 | 25.8 | -17.06 | -4.40 | -20.98 | 700 |
| 39 | Stochastic reversion · 1h | reversion | 88.89 | -11.11 | 163 | 46.6 | -13.37 | -2.19 | -22.24 | 362 |
| 40 | Supertrend · 1h | trend | 88.63 | -11.37 | 88 | 12.5 | -21.46 | -4.29 | -26.86 | 220 |
| 41 | Ichimoku · 1h | trend | 88.43 | -11.57 | 57 | 14.0 | -17.80 | -3.36 | -18.27 | 115 |
| 42 | Keltner breakout · 1h | breakout | 88.27 | -11.73 | 56 | 23.2 | -15.74 | -2.54 | -26.01 | 203 |
| 43 | Agent (aggressive) | meta | 88.09 | -11.90 | 44 | 36.4 | -12.44 | -3.57 | -14.88 | 117 |
| 44 | MACD cross · 1h | trend | 86.69 | -13.31 | 192 | 20.3 | -27.18 | -5.18 | -33.45 | 472 |
| 45 | Triple EMA stack · 1h | trend | 86.44 | -13.56 | 88 | 14.8 | -28.41 | -4.92 | -34.80 | 217 |
| 46 | Z-score reversion · 1h | reversion | 85.29 | -14.71 | 95 | 30.5 | -13.57 | -2.20 | -21.32 | 198 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 210 | 31.0 | -15.01 | -2.31 | -20.56 | 142 |
| 48 | OBV trend · 1h | momentum | 84.59 | -15.41 | 183 | 17.5 | -30.21 | -5.19 | -37.09 | 326 |
| 49 | Donchian 20/10 · 1h | breakout | 84.56 | -15.44 | 81 | 17.3 | -11.88 | -1.47 | -27.86 | 217 |
| 50 | MACD zero-line · 1h | trend | 84.50 | -15.50 | 87 | 14.9 | -24.78 | -4.92 | -25.56 | 218 |
| 51 | Agent (ML meta-label) | meta | 84.29 | -15.71 | 693 | 19.2 | -8.36 | -1.42 | -14.92 | 375 |
| 52 | Three white soldiers | momentum | 83.41 | -16.59 | 236 | 19.1 | -46.70 | -17.45 | -47.95 | 617 |
| 53 | Williams %R · 1h | reversion | 82.35 | -17.65 | 193 | 43.5 | -32.11 | -4.99 | -36.22 | 529 |
| 54 | Bollinger reversion · 1h | reversion | 82.30 | -17.70 | 162 | 35.8 | -28.03 | -5.36 | -33.44 | 352 |
| 55 | ROC + volume · 1h | momentum | 81.96 | -18.04 | 198 | 21.2 | -24.71 | -4.11 | -33.82 | 392 |
| 56 | CCI reversion · 1h | reversion | 81.18 | -18.82 | 171 | 39.8 | -16.52 | -2.01 | -27.44 | 444 |
| 57 | Heikin-Ashi · 1h | trend | 80.66 | -19.34 | 228 | 21.1 | -40.04 | -8.39 | -44.90 | 680 |
| 58 | EMA 9/21 cross · 1h | trend | 80.22 | -19.78 | 140 | 10.7 | -28.90 | -5.99 | -30.18 | 317 |
| 59 | RSI(14) reversion · 1h | reversion | 80.16 | -19.84 | 83 | 22.9 | -16.70 | -3.05 | -23.28 | 177 |
| 60 | VWAP momentum · 1h | momentum | 78.52 | -21.48 | 438 | 20.5 | -41.42 | -6.78 | -48.89 | 1263 |
| 61 | Candlestick reversal · 1h | reversion | 77.93 | -22.07 | 218 | 28.0 | -33.04 | -5.77 | -37.30 | 543 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 77.11 | -22.89 | 17 | 29.4 | -28.96 | -1.61 | -41.28 | 42 |
| 63 | ROC + volume | momentum | 63.21 | -36.79 | 601 | 22.3 | -76.65 | -18.76 | -78.84 | 1735 |
| 64 | Volume breakout | breakout | 62.44 | -37.56 | 365 | 13.2 | -62.78 | -18.19 | -64.31 | 879 |
| 65 | Squeeze breakout | breakout | 59.57 | -40.43 | 481 | 13.7 | -63.79 | -19.19 | -66.58 | 1211 |
| 66 | Donchian 55/20 | breakout | 58.67 | -41.33 | 488 | 18.0 | -69.61 | -16.48 | -73.50 | 1287 |
| 67 | RSI(14) reversion | reversion | 57.51 | -42.49 | 736 | 26.2 | -74.54 | -16.47 | -75.08 | 1622 |
| 68 | EMA 20/50 cross | trend | 56.59 | -43.41 | 525 | 19.4 | -76.98 | -16.12 | -80.87 | 1438 |
| 69 | VWAP reversion | reversion | 53.69 | -46.31 | 752 | 25.3 | -71.59 | -14.59 | -72.28 | 1503 |
| 70 | Keltner breakout | breakout | 51.59 | -48.41 | 681 | 16.0 | -82.37 | -24.53 | -83.82 | 1809 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -29.78 | -98.76 | 5309 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -30.45 | -93.87 | 2579 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.52 | -20.35 | -88.38 | 1905 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.31 | -24.74 | -91.32 | 2362 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.85 | -25.20 | -91.18 | 2245 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -31.97 | -97.64 | 3512 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.65 | -35.18 | -96.86 | 3587 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.39 | -27.53 | -94.53 | 2530 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.46 | -26.23 | -82.73 | 1692 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.74 | -99.38 | 5742 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.25 | -25.54 | -92.18 | 2624 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.90 | -31.25 | -95.90 | 3435 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -39.21 | -99.76 | 6212 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.43 | -28.43 | -91.67 | 2348 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -36.30 | -97.71 | 3611 |
| 86 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.17 | -98.49 | 4715 |
| 87 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.75 | -32.00 | -94.15 | 2797 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -38.55 | -99.53 | 6178 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.79 | -22.27 | -87.09 | 2162 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.77 | -25.85 | -88.28 | 2142 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.36 | -95.99 | 3769 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.93 | -31.98 | -89.26 | 2116 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.09 | -95.83 | 4108 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -43.25 | -99.90 | 8266 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-20T14:50 | Volume breakout · 1h | buy | LABU | 22.97 | — | entry |
| 2026-10-20T14:50 | Opening range 30m | sell | GOOGL | 5.11 | -0.03 | exit signal |
| 2026-10-20T14:45 | MFI reversion · 1h | buy | MSTR | 8.93 | — | entry |
| 2026-10-20T14:45 | MFI reversion · 1h | sell | ETH-USD | 4.43 | 0.06 | rebalance down |
| 2026-10-20T14:45 | MFI reversion · 1h | sell | DOGE-USD | 4.51 | 0.09 | rebalance down |
| 2026-10-20T14:45 | EMA 20/50 cross | buy | AMD | 3.51 | — | entry signal |
| 2026-10-20T14:45 | EMA 20/50 cross | sell | ETHU | 3.51 | 0.11 | rebalance down |
| 2026-10-20T14:40 | Agent (ML meta-label) | sell | COIN | 5.40 | 0.14 | selected signal exited |
| 2026-10-20T14:40 | Three white soldiers | buy | TQQQ | 6.93 | — | entry |
| 2026-10-20T14:40 | Three white soldiers | buy | SPY | 6.96 | — | entry |
| 2026-10-20T14:40 | Three white soldiers | buy | META | 6.96 | — | entry |
| 2026-10-20T14:40 | Three white soldiers | buy | IWM | 6.96 | — | entry |
| 2026-10-20T14:40 | Three white soldiers | buy | ETHU | 6.96 | — | entry |
| 2026-10-20T14:40 | Three white soldiers | sell | UPRO | 4.95 | 0.05 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | TECL | 5.00 | 0.10 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | SOXL | 5.10 | 0.10 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | QQQ | 4.90 | 0.01 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | NVDA | 4.90 | 0.01 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | MSTR | 5.08 | 0.24 | rebalance down |
| 2026-10-20T14:40 | Three white soldiers | sell | DOGE-USD | 4.84 | -0.03 | rebalance down |
| 2026-10-20T14:40 | EMA 20/50 cross | buy | COIN | 2.91 | — | entry |
| 2026-10-20T14:40 | EMA 20/50 cross | sell | XRP-USD | 2.91 | 0.06 | rebalance down |
| 2026-10-20T14:35 | Agent (ML meta-label) | buy | UPRO | 7.20 | — | entry |
| 2026-10-20T14:35 | Agent (ML meta-label) | buy | GOOGL | 7.20 | — | entry |
| 2026-10-20T14:30 | Agent (rotation) | buy | TQQQ | 32.24 | — | entry |
| 2026-10-20T14:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | TQQQ | 106.82 | — | entry |
| 2026-10-20T14:30 | Agent (ML meta-label) | sell | UPRO | 5.28 | -0.00 | selected signal exited |
| 2026-10-20T14:30 | Agent (ML meta-label) | sell | IWM | 6.46 | 0.03 | selected signal exited |
| 2026-10-20T14:30 | MFI reversion · 1h | buy | COIN | 20.81 | — | entry signal |
| 2026-10-20T14:30 | MFI reversion · 1h | buy | AMD | 21.29 | — | entry signal |
| 2026-10-20T14:30 | CCI reversion · 1h | buy | COIN | 4.77 | — | entry signal |
| 2026-10-20T14:30 | CCI reversion · 1h | sell | LABU | 4.40 | 0.34 | exit signal |
| 2026-10-20T14:30 | CCI reversion · 1h | sell | BITX | 4.13 | 0.12 | exit signal |
| 2026-10-20T14:30 | Williams %R · 1h | buy | MSTR | 7.21 | — | rebalance up |
| 2026-10-20T14:30 | Williams %R · 1h | buy | GOOGL | 7.39 | — | rebalance up |
| 2026-10-20T14:30 | Williams %R · 1h | buy | ETHU | 13.70 | — | entry signal |
| 2026-10-20T14:30 | Williams %R · 1h | buy | COIN | 6.75 | — | rebalance up |
| 2026-10-20T14:30 | Williams %R · 1h | buy | AMD | 7.39 | — | rebalance up |
| 2026-10-20T14:30 | Williams %R · 1h | buy | AAPL | 7.43 | — | rebalance up |
| 2026-10-20T14:30 | Williams %R · 1h | sell | TNA | 6.62 | 0.26 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-22 14:54:05.000175+00:00 -> 2026-10-20 15:04:05.000175+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
