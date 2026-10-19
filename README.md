# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T09:25:05.000167+00:00 · 28216 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.05 (-7.95%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.18 | -0.20 |
| SQQQ | 19.21 | +0.83 |

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

Today: 6885 decisions in 1377 calls, $0.0961 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T09:25 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-19T09:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-19T09:25 | 3 / 2 / 0 | ETH-USD 28% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.99 | 4.99 | 0 | — | 5.93 | 2.79 | -5.18 | 1 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.09 | 0.09 | 0 | — | 4.02 | 1.58 | -5.18 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | VWAP reversion · 1h | reversion | 99.70 | -0.30 | 64 | 39.1 | -11.25 | -3.24 | -13.79 | 140 |
| 9 | Donchian 55/20 · 1h | breakout | 99.10 | -0.90 | 36 | 16.7 | -11.90 | -1.87 | -22.12 | 113 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.27 | -3.91 | 21 |
| 11 | Max aggression: 5-day momentum | meta | 98.90 | -1.10 | 8 | 37.5 | -17.17 | -1.39 | -34.64 | 26 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 3.39 | 1.91 | -1.73 | 65 |
| 13 | Hold SPY | benchmark | 98.77 | -1.23 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 15 | Hold BTC | benchmark | 98.55 | -1.45 | 0 | — | 28.89 | 3.39 | -8.68 | 1 |
| 16 | Copy: Insider buying | copy | 98.29 | -1.71 | 20 | 45.0 | -13.89 | -2.50 | -20.62 | 69 |
| 17 | Agent (rotation) | meta | 97.18 | -2.83 | 108 | 33.3 | -4.43 | -2.26 | -5.64 | 263 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.59 | -3.41 | 0 | — | -2.60 | -1.02 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.51 | -3.49 | 0 | — | -6.58 | -3.57 | -6.88 | 1 |
| 20 | Three white soldiers · 1h | momentum | 96.35 | -3.65 | 12 | 0.0 | 0.79 | 0.46 | -5.48 | 33 |
| 21 | Trend pullback · 1h | trend | 96.26 | -3.75 | 87 | 24.1 | -18.89 | -5.63 | -19.70 | 137 |
| 22 | Copy: Hedge-fund gurus (GURU) | copy | 95.71 | -4.29 | 0 | — | -6.53 | -2.54 | -7.59 | 1 |
| 23 | ADX DI cross · 1h | trend | 95.24 | -4.76 | 82 | 19.5 | -11.70 | -2.25 | -13.34 | 256 |
| 24 | Parabolic SAR · 1h | trend | 93.73 | -6.26 | 97 | 21.6 | -10.64 | -1.66 | -22.75 | 273 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | 0.54 | 0.23 | -9.46 | 94 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.43 | 2.38 | -6.51 | 197 |
| 27 | Daily: Momentum burst | daily | 93.15 | -6.85 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.70 | -7.30 | 55 | 14.5 | -18.37 | -3.15 | -21.23 | 130 |
| 29 | Agent (aggressive) | meta | 92.23 | -7.77 | 38 | 31.6 | -5.81 | -1.99 | -8.61 | 114 |
| 30 | Agent | meta | 92.05 | -7.95 | 77 | 39.0 | -8.96 | -5.32 | -13.12 | 232 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.24 | -0.02 | -14.55 | 112 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.38 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.20 | -8.80 | 77 | 16.9 | -16.84 | -2.91 | -27.42 | 221 |
| 34 | Daily: Bullish score | daily | 90.77 | -9.22 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 35 | Bollinger breakout · 1h | breakout | 90.54 | -9.46 | 84 | 28.6 | 7.74 | 1.15 | -14.21 | 265 |
| 36 | Ichimoku · 1h | trend | 90.41 | -9.59 | 52 | 15.4 | -17.95 | -3.36 | -18.38 | 116 |
| 37 | Triple EMA stack · 1h | trend | 90.14 | -9.86 | 81 | 16.0 | -21.15 | -2.76 | -33.23 | 231 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.54 | -10.46 | 0 | — | -19.73 | -3.73 | -20.60 | 1 |
| 39 | Keltner breakout · 1h | breakout | 89.47 | -10.53 | 52 | 23.1 | -7.55 | -0.89 | -27.05 | 204 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.40 | -10.60 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Supertrend · 1h | trend | 89.22 | -10.78 | 85 | 11.8 | -19.18 | -3.65 | -27.02 | 214 |
| 42 | Connors RSI(2) · 1h | reversion | 88.09 | -11.91 | 145 | 40.0 | -24.75 | -7.60 | -25.12 | 218 |
| 43 | MACD cross · 1h | trend | 87.96 | -12.04 | 181 | 21.5 | -23.47 | -4.06 | -30.63 | 459 |
| 44 | OBV trend · 1h | momentum | 87.76 | -12.24 | 170 | 18.2 | -19.38 | -2.45 | -33.85 | 321 |
| 45 | Stochastic reversion · 1h | reversion | 86.76 | -13.24 | 150 | 45.3 | -21.02 | -3.82 | -22.24 | 373 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.47 | -21.40 | 709 |
| 47 | Max aggression: 1-day momentum | meta | 86.09 | -13.91 | 14 | 35.7 | -10.67 | -0.23 | -37.31 | 42 |
| 48 | MACD zero-line · 1h | trend | 85.72 | -14.28 | 82 | 15.9 | -23.45 | -4.64 | -24.31 | 220 |
| 49 | MFI reversion · 1h | reversion | 85.31 | -14.69 | 207 | 30.4 | -20.86 | -3.20 | -23.01 | 148 |
| 50 | Donchian 20/10 · 1h | breakout | 85.03 | -14.96 | 79 | 17.7 | 1.67 | 0.40 | -21.74 | 216 |
| 51 | Three white soldiers | momentum | 83.02 | -16.98 | 222 | 18.5 | -47.55 | -19.83 | -47.57 | 609 |
| 52 | Z-score reversion · 1h | reversion | 82.90 | -17.10 | 91 | 30.8 | -16.62 | -2.90 | -21.32 | 190 |
| 53 | ROC + volume · 1h | momentum | 82.86 | -17.14 | 193 | 21.2 | -10.78 | -1.25 | -27.49 | 393 |
| 54 | Agent (ML meta-label) | meta | 82.32 | -17.68 | 655 | 18.0 | -18.62 | -3.19 | -20.11 | 378 |
| 55 | EMA 9/21 cross · 1h | trend | 81.40 | -18.60 | 131 | 11.5 | -18.75 | -3.10 | -29.40 | 317 |
| 56 | Heikin-Ashi · 1h | trend | 81.34 | -18.66 | 209 | 22.5 | -31.62 | -5.11 | -42.46 | 678 |
| 57 | VWAP momentum · 1h | momentum | 80.52 | -19.48 | 410 | 20.0 | -36.82 | -5.48 | -46.96 | 1252 |
| 58 | Williams %R · 1h | reversion | 80.22 | -19.78 | 180 | 42.2 | -35.33 | -5.77 | -36.90 | 533 |
| 59 | RSI(14) reversion · 1h | reversion | 80.15 | -19.85 | 74 | 20.3 | -14.57 | -2.58 | -22.27 | 167 |
| 60 | Bollinger reversion · 1h | reversion | 79.99 | -20.01 | 150 | 32.0 | -30.68 | -6.34 | -33.03 | 355 |
| 61 | CCI reversion · 1h | reversion | 79.16 | -20.84 | 161 | 38.5 | -20.22 | -2.62 | -27.44 | 430 |
| 62 | Candlestick reversal · 1h | reversion | 76.24 | -23.76 | 205 | 25.4 | -35.84 | -6.46 | -36.73 | 542 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 567 | 22.0 | -75.72 | -17.50 | -77.85 | 1733 |
| 64 | Volume breakout | breakout | 61.88 | -38.12 | 349 | 12.9 | -63.19 | -18.13 | -64.06 | 886 |
| 65 | Squeeze breakout | breakout | 60.56 | -39.44 | 453 | 14.1 | -63.30 | -18.06 | -65.45 | 1218 |
| 66 | Donchian 55/20 | breakout | 59.41 | -40.59 | 462 | 18.0 | -68.57 | -14.35 | -72.80 | 1280 |
| 67 | RSI(14) reversion | reversion | 58.63 | -41.37 | 687 | 25.0 | -74.46 | -16.43 | -74.55 | 1629 |
| 68 | EMA 20/50 cross | trend | 57.90 | -42.10 | 480 | 18.3 | -75.74 | -14.54 | -80.16 | 1427 |
| 69 | VWAP reversion | reversion | 53.49 | -46.51 | 720 | 23.9 | -72.80 | -15.29 | -73.32 | 1514 |
| 70 | Keltner breakout | breakout | 51.71 | -48.29 | 650 | 15.8 | -82.76 | -26.52 | -83.26 | 1820 |
| 71 | AI bee: Boozy | ai | 51.16 | -48.84 | 343 | 5.8 | — | — | — | — |
| 72 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.88 | -98.65 | 5340 |
| 73 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.35 | -30.28 | -93.56 | 2587 |
| 74 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.10 | -19.91 | -87.78 | 1907 |
| 75 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.01 | -23.99 | -90.90 | 2352 |
| 76 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.15 | -25.99 | -91.15 | 2304 |
| 77 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -32.15 | -97.41 | 3523 |
| 78 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.71 | -36.88 | -96.71 | 3618 |
| 79 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.56 | -26.96 | -94.90 | 2596 |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.91 | -23.28 | -82.75 | 1725 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.28 | -99.38 | 5806 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.30 | -25.70 | -91.78 | 2645 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.02 | -31.19 | -96.02 | 3510 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -41.37 | -99.74 | 6249 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.42 | -28.76 | -91.50 | 2356 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.55 | -39.08 | -97.56 | 3670 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -36.50 | -98.47 | 4756 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.69 | -33.30 | -93.71 | 2815 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.97 | -99.53 | 6238 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.77 | -22.18 | -86.81 | 2170 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.19 | -27.00 | -88.24 | 2169 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.86 | -32.11 | -95.87 | 3803 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.99 | -32.45 | -89.29 | 2106 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.77 | -33.64 | -95.77 | 4150 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -46.36 | -99.90 | 8344 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
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
| 2026-10-19T07:36 | Three white soldiers | buy | DOGE-USD | 20.87 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | XRP-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | SOL-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | ETH-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | DOGE-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Volume breakout | buy | BTC-USD | 12.49 | — | entry signal |
| 2026-10-19T07:36 | Squeeze breakout | buy | ETH-USD | 15.20 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 09:25:05.000167+00:00 -> 2026-10-19 09:35:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
