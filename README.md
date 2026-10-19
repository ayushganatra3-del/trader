# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T09:55:05.000143+00:00 · 28238 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, FLSC 12%, REF 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7215 decisions in 1443 calls, $0.1008 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T09:55 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-10-19T09:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T09:55 | 2 / 2 / 1 | COIN 73% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | BITX | 2.25 | +2.55% | 6 |
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.06 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.44 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.00 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.82 | 4.82 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.93 | -0.07 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.55 | -0.45 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 10 | Donchian 55/20 · 1h | breakout | 98.93 | -1.07 | 36 | 16.7 | -11.95 | -1.88 | -22.12 | 113 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 12 | Max aggression: 5-day momentum | meta | 98.74 | -1.26 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.61 | -1.39 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Hold BTC | benchmark | 98.41 | -1.58 | 0 | — | 28.85 | 3.38 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 17 | Agent (rotation) | meta | 97.13 | -2.87 | 108 | 33.3 | -4.43 | -2.26 | -5.64 | 263 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.22 | -3.78 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 21 | Three white soldiers · 1h | momentum | 96.18 | -3.82 | 12 | 0.0 | 0.74 | 0.43 | -5.48 | 33 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.56 | -4.44 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 95.05 | -4.95 | 82 | 19.5 | -11.73 | -2.25 | -13.34 | 256 |
| 24 | Parabolic SAR · 1h | trend | 93.54 | -6.46 | 97 | 21.6 | -10.69 | -1.67 | -22.75 | 273 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -3.03 | -0.67 | -9.46 | 93 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 93.00 | -7.00 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.50 | -7.50 | 55 | 14.5 | -18.40 | -3.15 | -21.23 | 130 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.02 | -8.98 | 77 | 16.9 | -16.86 | -2.91 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.66 | -9.34 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.74 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.23 | -9.77 | 52 | 15.4 | -17.99 | -3.37 | -18.38 | 116 |
| 37 | Triple EMA stack · 1h | trend | 89.98 | -10.02 | 81 | 16.0 | -21.19 | -2.76 | -33.23 | 231 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.47 | -10.53 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Keltner breakout · 1h | breakout | 89.27 | -10.73 | 52 | 23.1 | -7.60 | -0.89 | -27.05 | 204 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Supertrend · 1h | trend | 89.08 | -10.92 | 85 | 11.8 | -14.30 | -2.25 | -28.83 | 215 |
| 42 | Connors RSI(2) · 1h | reversion | 87.99 | -12.01 | 145 | 40.0 | -24.75 | -7.60 | -25.12 | 218 |
| 43 | MACD cross · 1h | trend | 87.79 | -12.21 | 181 | 21.5 | -23.49 | -4.07 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.59 | -12.41 | 170 | 18.2 | -19.40 | -2.45 | -33.85 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.68 | -13.31 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.54 | -14.46 | 82 | 15.9 | -23.48 | -4.64 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.23 | -14.77 | 207 | 30.4 | -20.87 | -3.21 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 84.86 | -15.14 | 79 | 17.7 | 1.62 | 0.40 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 82.82 | -17.18 | 223 | 18.4 | -47.66 | -19.88 | -47.68 | 610 |
| 52 | ROC + volume · 1h | momentum | 82.80 | -17.20 | 193 | 21.2 | -10.79 | -1.25 | -27.49 | 393 |
| 53 | Z-score reversion · 1h | reversion | 82.79 | -17.21 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 54 | Agent (ML meta-label) | meta | 82.21 | -17.79 | 655 | 18.0 | -17.73 | -3.06 | -19.24 | 374 |
| 55 | EMA 9/21 cross · 1h | trend | 81.24 | -18.76 | 131 | 11.5 | -18.78 | -3.10 | -29.40 | 317 |
| 56 | Heikin-Ashi · 1h | trend | 81.20 | -18.80 | 209 | 22.5 | -31.65 | -5.12 | -42.46 | 678 |
| 57 | VWAP momentum · 1h | momentum | 80.37 | -19.63 | 410 | 20.0 | -36.84 | -5.49 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.09 | -19.91 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.02 | -19.98 | 74 | 20.3 | -14.57 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.88 | -20.12 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -20.21 | -2.62 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 542 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.01 | -18.05 | -64.06 | 883 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.12 | -17.97 | -65.45 | 1214 |
| 66 | Donchian 55/20 | breakout | 59.35 | -40.65 | 462 | 18.0 | -68.72 | -14.41 | -72.80 | 1283 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.46 | -16.43 | -74.55 | 1628 |
| 68 | EMA 20/50 cross | trend | 57.78 | -42.22 | 480 | 18.3 | -75.79 | -14.57 | -80.16 | 1427 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.80 | -15.29 | -73.32 | 1514 |
| 70 | Keltner breakout | breakout | 51.66 | -48.34 | 650 | 15.8 | -82.68 | -26.42 | -83.28 | 1817 |
| 71 | AI bee: Boozy | ai | 50.99 | -49.01 | 345 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.85 | -98.64 | 5339 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -30.32 | -93.56 | 2587 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.09 | -19.91 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.00 | -23.98 | -90.90 | 2352 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.16 | -26.01 | -91.16 | 2304 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -32.14 | -97.41 | 3522 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.73 | -36.96 | -96.73 | 3620 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -26.61 | -94.82 | 2596 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.94 | -23.32 | -82.78 | 1727 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.32 | -99.38 | 5806 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.24 | -25.63 | -91.79 | 2642 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.01 | -31.21 | -96.01 | 3511 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.40 | -99.74 | 6249 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.43 | -28.80 | -91.50 | 2356 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -39.10 | -97.56 | 3670 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.50 | -98.47 | 4756 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.68 | -33.23 | -93.74 | 2813 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -38.97 | -99.53 | 6237 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.74 | -22.16 | -86.78 | 2168 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.18 | -26.99 | -88.23 | 2168 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.11 | -95.87 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.00 | -32.45 | -89.30 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.66 | -95.77 | 4150 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.41 | -99.90 | 8345 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T09:53 | AI bee: Boozy | sell | BTC-USD | 13.94 | -0.10 | Jev: buy |
| 2026-10-19T09:45 | Three white soldiers | sell | SOL-USD | 20.59 | -0.18 | exit signal |
| 2026-10-19T09:40 | Keltner breakout | buy | ETH-USD | 12.93 | — | entry signal |
| 2026-10-19T09:40 | Donchian 55/20 | buy | ETH-USD | 14.85 | — | entry signal |
| 2026-10-19T09:37 | AI bee: Boozy | buy | BTC-USD | 14.04 | — | Jev: buy (buy p=0.73) |
| 2026-10-19T09:35 | Three white soldiers | buy | BTC-USD | 20.75 | — | entry signal |
| 2026-10-19T09:33 | AI bee: Boozy | sell | ETH-USD | 14.04 | -0.09 | Jev: add (buy p=0.52) |
| 2026-10-19T09:25 | Three white soldiers | buy | SOL-USD | 20.77 | — | entry signal |
| 2026-10-19T09:18 | AI bee: Boozy | buy | ETH-USD | 14.13 | — | Jev: buy (buy p=0.74) |
| 2026-10-19T09:00 | OBV trend · 1h | buy | ETH-USD | 7.25 | — | entry signal |
| 2026-10-19T09:00 | OBV trend · 1h | sell | SOL-USD | 7.25 | -0.03 | rebalance down |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | buy | SOL-USD | 6.66 | — | rebalance up |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | buy | ETH-USD | 6.73 | — | rebalance up |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | sell | XRP-USD | 16.22 | -0.02 | exit signal |
| 2026-10-19T09:00 | Heikin-Ashi · 1h | sell | BTC-USD | 13.55 | 0.06 | exit signal |
| 2026-10-19T09:00 | EMA 20/50 cross · 1h | buy | ETH-USD | 7.78 | — | entry signal |
| 2026-10-19T09:00 | EMA 20/50 cross · 1h | sell | BTC-USD | 4.67 | 0.00 | rebalance down |
| 2026-10-19T08:10 | Donchian 55/20 | sell | SOL-USD | 12.02 | 0.20 | exit signal |
| 2026-10-19T08:10 | Donchian 55/20 | sell | BTC-USD | 11.89 | 0.05 | exit signal |
| 2026-10-19T08:05 | Donchian 55/20 | sell | XRP-USD | 14.82 | -0.14 | stop-loss |
| 2026-10-19T08:05 | Donchian 55/20 | sell | ETH-USD | 11.89 | 0.07 | exit signal |
| 2026-10-19T08:00 | OBV trend · 1h | buy | XRP-USD | 6.60 | — | entry signal |
| 2026-10-19T08:00 | OBV trend · 1h | sell | BTC-USD | 4.39 | -0.01 | rebalance down |
| 2026-10-19T08:00 | VWAP momentum · 1h | buy | DOGE-USD | 2.34 | — | entry signal |
| 2026-10-19T08:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 23.11 | — | entry signal |
| 2026-10-19T07:40 | Three white soldiers | sell | SOL-USD | 20.67 | -0.20 | stop-loss |
| 2026-10-19T07:40 | Three white soldiers | sell | DOGE-USD | 20.68 | -0.19 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | XRP-USD | 12.37 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | SOL-USD | 12.37 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | ETH-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | DOGE-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Volume breakout | sell | BTC-USD | 12.38 | -0.11 | stop-loss |
| 2026-10-19T07:40 | Squeeze breakout | sell | ETH-USD | 15.06 | -0.14 | stop-loss |
| 2026-10-19T07:40 | Squeeze breakout | sell | BTC-USD | 15.10 | -0.10 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | XRP-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | ETH-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | DOGE-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Keltner breakout | sell | BTC-USD | 12.93 | -0.12 | stop-loss |
| 2026-10-19T07:40 | Donchian 55/20 | sell | DOGE-USD | 8.79 | -0.08 | stop-loss |
| 2026-10-19T07:36 | Three white soldiers | buy | SOL-USD | 20.87 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 09:55:05.000143+00:00 -> 2026-10-19 10:05:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
