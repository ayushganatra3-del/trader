# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T14:45:05.000144+00:00 · 31950 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.76 (-9.24%)

Closed trades 94, win rate 40.4%, fees £3.06, max drawdown -10.18%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| ETHU | 18.25 | +0.11 |

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

Today: 14769 decisions in 2154 calls, $0.1959 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T14:45 | 4 / 17 / 9 | COIN 15% |  |
| Breezy | 2026-10-22T14:45 | 0 / 25 / 5 | cash |  |
| Boozy | 2026-10-22T14:45 | 5 / 21 / 4 | COIN 79% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.84 | 6.84 | 0 | — | 9.23 | 4.27 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.69 | 4.69 | 12 | 66.7 | 1.63 | 0.56 | -7.48 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.72 | 3.72 | 19 | 31.6 | 7.16 | 1.81 | -5.96 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.71 | 3.71 | 15 | 46.7 | 6.13 | 1.95 | -4.90 | 24 |
| 5 | VWAP reversion · 1h | reversion | 102.60 | 2.60 | 75 | 48.0 | -8.28 | -2.24 | -13.79 | 135 |
| 6 | Max aggression: 5-day momentum | meta | 101.28 | 1.28 | 10 | 50.0 | -14.66 | -1.11 | -34.64 | 26 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 99.48 | -0.52 | 68 | 35.3 | 3.22 | 1.87 | -2.29 | 68 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.30 | -0.70 | 0 | — | 2.76 | 1.24 | -5.02 | 1 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 12 | Hold SPY | benchmark | 98.19 | -1.81 | 0 | — | -0.63 | -0.30 | -3.13 | 1 |
| 13 | Copy: Hedge-fund gurus (GURU) | copy | 97.20 | -2.80 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.14 | -1.79 | -5.83 | 1 |
| 15 | Hold BTC | benchmark | 96.82 | -3.18 | 0 | — | 5.46 | 0.99 | -8.68 | 1 |
| 16 | Copy: Congress Democrats (NANC) | copy | 96.65 | -3.35 | 0 | — | -0.21 | -0.02 | -5.31 | 1 |
| 17 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.03 | 0.89 | -7.93 | 8 |
| 18 | Agent (rotation) | meta | 95.69 | -4.31 | 117 | 30.8 | -5.00 | -2.12 | -7.58 | 253 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 20 | Gap and go | momentum | 94.64 | -5.36 | 89 | 21.3 | 6.58 | 2.05 | -7.38 | 198 |
| 21 | Trend pullback · 1h | trend | 94.35 | -5.65 | 93 | 23.7 | -21.68 | -6.69 | -21.81 | 126 |
| 22 | Copy: Insider buying | copy | 94.26 | -5.74 | 25 | 40.0 | -13.64 | -2.33 | -20.62 | 72 |
| 23 | Opening range 30m | breakout | 93.89 | -6.11 | 236 | 35.2 | -10.10 | -2.84 | -17.26 | 558 |
| 24 | Daily: Momentum burst | daily | 93.61 | -6.39 | 8 | 12.5 | -15.28 | -2.70 | -20.58 | 39 |
| 25 | ADX DI cross · 1h | trend | 93.41 | -6.59 | 101 | 18.8 | -12.37 | -2.34 | -14.92 | 255 |
| 26 | Donchian 55/20 · 1h | breakout | 92.92 | -7.08 | 48 | 16.7 | -18.02 | -3.61 | -19.05 | 103 |
| 27 | Parabolic SAR · 1h | trend | 91.94 | -8.06 | 115 | 26.1 | -16.63 | -3.62 | -19.31 | 267 |
| 28 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -5.08 | -1.20 | -11.76 | 102 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.27 | -1.93 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 91.05 | -8.96 | 8 | 0.0 | -5.99 | -0.66 | -13.10 | 13 |
| 31 | Agent | meta | 90.76 | -9.24 | 94 | 40.4 | -19.78 | -5.86 | -21.73 | 277 |
| 32 | Copy: Cathie Wood (ARKK) | copy | 90.35 | -9.65 | 0 | — | -3.78 | -0.44 | -14.37 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 89.45 | -10.55 | 103 | 28.2 | -11.95 | -2.13 | -15.89 | 259 |
| 34 | Stochastic reversion · 1h | reversion | 89.24 | -10.76 | 176 | 46.0 | -14.48 | -2.38 | -22.24 | 371 |
| 35 | Volume breakout · 1h | breakout | 88.85 | -11.15 | 101 | 22.8 | -13.21 | -2.32 | -15.17 | 107 |
| 36 | EMA 20/50 cross · 1h | trend | 88.30 | -11.70 | 67 | 11.9 | -23.01 | -4.27 | -25.78 | 142 |
| 37 | Opening range 15m | breakout | 87.90 | -12.10 | 296 | 30.7 | -15.35 | -4.15 | -18.82 | 701 |
| 38 | Supertrend · 1h | trend | 87.88 | -12.12 | 102 | 15.7 | -23.60 | -4.65 | -26.75 | 219 |
| 39 | RSI momentum · 1h | momentum | 87.77 | -12.23 | 94 | 17.0 | -19.52 | -3.85 | -21.69 | 218 |
| 40 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.81 | -4.39 | -19.25 | 143 |
| 41 | Keltner breakout · 1h | breakout | 85.95 | -14.05 | 73 | 23.3 | -23.20 | -4.45 | -23.83 | 198 |
| 42 | Connors RSI(2) · 1h | reversion | 85.82 | -14.18 | 167 | 40.1 | -25.63 | -7.17 | -25.71 | 203 |
| 43 | MACD cross · 1h | trend | 85.48 | -14.52 | 209 | 22.0 | -26.98 | -5.10 | -27.59 | 471 |
| 44 | Ichimoku · 1h | trend | 84.99 | -15.01 | 64 | 12.5 | -19.70 | -3.68 | -22.29 | 117 |
| 45 | Z-score reversion · 1h | reversion | 84.50 | -15.50 | 103 | 34.0 | -9.48 | -1.30 | -21.32 | 195 |
| 46 | MFI reversion · 1h | reversion | 84.34 | -15.66 | 230 | 33.0 | -16.84 | -2.62 | -21.11 | 144 |
| 47 | Triple EMA stack · 1h | trend | 84.34 | -15.66 | 96 | 15.6 | -30.39 | -5.32 | -31.58 | 217 |
| 48 | Donchian 20/10 · 1h | breakout | 84.23 | -15.77 | 92 | 20.7 | -23.04 | -4.28 | -23.93 | 227 |
| 49 | Williams %R · 1h | reversion | 83.47 | -16.53 | 201 | 44.8 | -32.41 | -5.07 | -38.05 | 514 |
| 50 | OBV trend · 1h | momentum | 82.61 | -17.39 | 196 | 17.9 | -31.68 | -6.08 | -32.26 | 308 |
| 51 | MACD zero-line · 1h | trend | 82.58 | -17.43 | 99 | 15.2 | -24.81 | -4.77 | -25.83 | 227 |
| 52 | Three white soldiers | momentum | 82.17 | -17.83 | 262 | 20.2 | -44.77 | -17.94 | -45.22 | 598 |
| 53 | Agent (ML meta-label) | meta | 82.13 | -17.87 | 759 | 19.5 | -11.46 | -2.09 | -17.21 | 347 |
| 54 | Bollinger reversion · 1h | reversion | 81.66 | -18.34 | 165 | 35.8 | -29.95 | -5.80 | -32.75 | 352 |
| 55 | CCI reversion · 1h | reversion | 81.62 | -18.38 | 190 | 43.2 | -21.00 | -2.74 | -27.44 | 443 |
| 56 | ROC + volume · 1h | momentum | 80.34 | -19.66 | 230 | 24.3 | -27.54 | -4.95 | -27.84 | 380 |
| 57 | Heikin-Ashi · 1h | trend | 79.66 | -20.34 | 260 | 23.5 | -45.34 | -9.43 | -45.37 | 675 |
| 58 | RSI(14) reversion · 1h | reversion | 79.28 | -20.72 | 87 | 24.1 | -17.85 | -3.36 | -23.28 | 173 |
| 59 | Candlestick reversal · 1h | reversion | 78.98 | -21.02 | 234 | 30.3 | -36.11 | -6.15 | -38.86 | 554 |
| 60 | EMA 9/21 cross · 1h | trend | 78.70 | -21.30 | 154 | 11.7 | -30.58 | -5.81 | -31.84 | 338 |
| 61 | VWAP momentum · 1h | momentum | 76.84 | -23.16 | 497 | 21.5 | -51.14 | -10.47 | -51.81 | 1250 |
| 62 | Max aggression: 1-day momentum ⏸ | meta | 67.94 | -32.06 | 18 | 27.8 | -42.90 | -2.79 | -47.70 | 43 |
| 63 | ROC + volume | momentum | 59.86 | -40.14 | 681 | 23.3 | -77.55 | -21.25 | -79.03 | 1699 |
| 64 | Volume breakout | breakout | 58.55 | -41.45 | 406 | 13.5 | -64.52 | -19.57 | -65.31 | 867 |
| 65 | Donchian 55/20 | breakout | 56.12 | -43.88 | 538 | 19.7 | -71.93 | -18.64 | -74.22 | 1276 |
| 66 | Squeeze breakout | breakout | 55.60 | -44.40 | 527 | 14.0 | -67.22 | -22.86 | -68.25 | 1202 |
| 67 | EMA 20/50 cross | trend | 54.77 | -45.23 | 579 | 20.4 | -78.98 | -20.02 | -80.33 | 1441 |
| 68 | RSI(14) reversion | reversion | 54.05 | -45.95 | 792 | 26.5 | -75.91 | -17.17 | -76.18 | 1645 |
| 69 | VWAP reversion | reversion | 51.30 | -48.70 | 790 | 25.2 | -72.78 | -14.51 | -73.03 | 1501 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.80 | -31.30 | -98.86 | 5309 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.77 | -31.66 | -94.25 | 2572 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.90 | -23.10 | -88.88 | 1899 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.27 | -27.52 | -91.91 | 2357 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.11 | -25.28 | -91.11 | 2246 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.75 | -34.78 | -97.89 | 3503 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.79 | -35.52 | -97.02 | 3573 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -28.16 | -94.47 | 2558 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.85 | -27.04 | -83.46 | 1719 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -37.38 | -99.47 | 5810 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.37 | -30.11 | -92.92 | 2616 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.79 | -30.80 | -95.82 | 3456 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -41.68 | -99.78 | 6161 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.36 | -92.08 | 2332 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.67 | -37.77 | -97.75 | 3596 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.62 | -38.40 | -98.63 | 4743 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.26 | -34.53 | -94.62 | 2786 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.39 | -27.47 | -84.50 | 1784 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.59 | -40.28 | -99.59 | 6217 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.67 | -23.50 | -87.81 | 2184 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.55 | -27.14 | -88.70 | 2172 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.18 | -33.89 | -96.22 | 3802 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.55 | -34.04 | -89.78 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.19 | -34.48 | -96.21 | 4133 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.74 | -99.91 | 8248 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T14:45 | Agent (ML meta-label) | buy | LABU | 1.93 | — | following Connors RSI(2) |
| 2026-10-22T14:45 | Agent | sell | LABU | 18.11 | -0.02 | selected signal exited |
| 2026-10-22T14:45 | RSI(14) reversion | buy | PLTR | 8.16 | — | entry signal |
| 2026-10-22T14:45 | RSI(14) reversion | buy | ETHU | 10.81 | — | entry signal |
| 2026-10-22T14:45 | RSI(14) reversion | buy | BITX | 10.81 | — | entry signal |
| 2026-10-22T14:45 | RSI(14) reversion | sell | MSTR | 2.80 | 0.02 | rebalance down |
| 2026-10-22T14:45 | Opening range 30m | buy | MSTR | 23.48 | — | entry signal |
| 2026-10-22T14:40 | Agent (ML meta-label) | buy | AAPL | 9.58 | — | rebalance up |
| 2026-10-22T14:40 | Agent (ML meta-label) | sell | LABU | 11.52 | -0.28 | selected signal exited |
| 2026-10-22T14:40 | VWAP reversion | buy | SPY | 3.60 | — | entry signal |
| 2026-10-22T14:40 | VWAP reversion | buy | PLTR | 4.66 | — | entry |
| 2026-10-22T14:40 | VWAP reversion | buy | MSFT | 3.23 | — | rebalance up |
| 2026-10-22T14:40 | VWAP reversion | buy | AAPL | 4.66 | — | entry signal |
| 2026-10-22T14:40 | VWAP reversion | sell | XRP-USD | 2.66 | -0.01 | rebalance down |
| 2026-10-22T14:40 | VWAP reversion | sell | SOL-USD | 2.65 | 0.01 | rebalance down |
| 2026-10-22T14:40 | VWAP reversion | sell | GOOGL | 2.67 | -0.01 | rebalance down |
| 2026-10-22T14:40 | VWAP reversion | sell | ETH-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-22T14:40 | VWAP reversion | sell | DOGE-USD | 2.65 | 0.00 | rebalance down |
| 2026-10-22T14:40 | VWAP reversion | sell | BTC-USD | 2.84 | -0.02 | rebalance down |
| 2026-10-22T14:35 | Agent (rotation) | buy | SQQQ | 31.90 | — | entry |
| 2026-10-22T14:35 | Day trade: Open breakout · TQQQ/SQQQ | buy | SQQQ | 104.64 | — | entry |
| 2026-10-22T14:35 | Agent (ML meta-label) | buy | AAPL | 4.07 | — | entry |
| 2026-10-22T14:35 | Bollinger breakout · 1h | sell | IWM | 22.41 | -0.09 | stop-loss |
| 2026-10-22T14:35 | OBV trend · 1h | buy | LABU | 4.18 | — | rebalance up |
| 2026-10-22T14:35 | VWAP reversion | buy | MSFT | 1.43 | — | entry signal |
| 2026-10-22T14:35 | VWAP reversion | buy | AMZN | 5.69 | — | entry signal |
| 2026-10-22T14:30 | Day trade: Noise-area momentum · TQQQ/SQQQ | buy | SQQQ | 103.17 | — | entry |
| 2026-10-22T14:30 | Agent (ML meta-label) | buy | MSTR | 13.67 | — | entry |
| 2026-10-22T14:30 | Agent (ML meta-label) | sell | QQQ | 10.40 | -0.16 | selected signal exited |
| 2026-10-22T14:30 | CCI reversion · 1h | buy | SQQQ | 13.56 | — | entry signal |
| 2026-10-22T14:30 | Williams %R · 1h | sell | SQQQ | 21.52 | 0.85 | exit signal |
| 2026-10-22T14:30 | Stochastic reversion · 1h | sell | SQQQ | 18.16 | 1.15 | exit signal |
| 2026-10-22T14:30 | Connors RSI(2) · 1h | buy | MSFT | 21.44 | — | entry signal |
| 2026-10-22T14:30 | Volume breakout · 1h | buy | SQQQ | 22.18 | — | entry signal |
| 2026-10-22T14:30 | Keltner breakout · 1h | buy | SQQQ | 21.46 | — | entry signal |
| 2026-10-22T14:30 | Keltner breakout · 1h | sell | TNA | 21.33 | -0.20 | stop-loss |
| 2026-10-22T14:30 | Keltner breakout · 1h | sell | IWM | 21.45 | -0.07 | exit signal |
| 2026-10-22T14:30 | Bollinger breakout · 1h | buy | SQQQ | 22.33 | — | entry signal |
| 2026-10-22T14:30 | Bollinger breakout · 1h | sell | TNA | 22.28 | -0.21 | stop-loss |
| 2026-10-22T14:30 | Donchian 20/10 · 1h | buy | TSLA | 6.65 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 14:45:05.000144+00:00 -> 2026-10-22 14:55:05.000144+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
