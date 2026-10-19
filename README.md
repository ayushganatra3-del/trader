# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T17:25:05.000160+00:00 · 28609 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.73 (-9.27%)

Closed trades 81, win rate 39.5%, fees £2.79, max drawdown -9.80%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.15 | +0.02 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-19 | PAM 12%, BBD 12%, BORR 12%, PEP 12%, GME 12%, BPRE 12%, APLD 12%, FLSC 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 26034 decisions in 2556 calls, $0.3269 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T17:25 | 4 / 16 / 10 | cash |  |
| Breezy | 2026-10-19T17:25 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-19T17:25 | 2 / 25 / 3 | COIN 72% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Williams %R | SQQQ | 1.94 | +2.05% | 8 |
| Bollinger reversion | SQQQ | 1.87 | +0.89% | 6 |
| EMA 20/50 cross | COIN | 1.70 | +8.82% | 3 |
| Heikin-Ashi · 1h | SQQQ | 1.60 | +7.36% | 3 |
| VWAP reversion | BITX | 1.52 | +2.60% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 2.61 | 0.85 | -9.61 | 26 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.82 | 6.82 | 11 | 63.6 | 9.24 | 3.07 | -3.27 | 19 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.42 | 5.42 | 16 | 37.5 | 8.75 | 2.15 | -7.55 | 43 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.87 | 4.87 | 0 | — | 5.55 | 2.72 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.63 | -0.37 | 0 | — | 1.88 | 0.81 | -5.18 | 1 |
| 9 | Hold SPY | benchmark | 99.30 | -0.70 | 0 | — | -0.18 | -0.06 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.69 | -1.31 | 3 | 33.3 | 2.74 | 0.68 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.25 | -1.75 | 54 | 31.5 | 3.13 | 1.73 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -5.69 | -2.97 | -6.43 | 257 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.42 | -2.58 | 0 | — | -0.61 | -0.19 | -5.31 | 1 |
| 15 | Hold BTC | benchmark | 97.40 | -2.60 | 0 | — | 26.07 | 3.11 | -8.68 | 1 |
| 16 | Donchian 55/20 · 1h | breakout | 97.34 | -2.66 | 36 | 16.7 | -8.87 | -1.43 | -19.37 | 100 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.08 | -2.31 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.61 | -3.39 | 0 | — | -5.68 | -2.23 | -7.04 | 1 |
| 19 | Copy: Insider buying | copy | 96.35 | -3.65 | 23 | 43.5 | -15.06 | -2.73 | -20.62 | 73 |
| 20 | Trend pullback · 1h | trend | 96.33 | -3.67 | 88 | 23.9 | -19.76 | -5.85 | -20.58 | 136 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 94.95 | -5.05 | 8 | 37.5 | -20.48 | -1.73 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.68 | -6.32 | 87 | 18.4 | -12.78 | -2.42 | -15.20 | 256 |
| 24 | Gap and go | momentum | 93.64 | -6.36 | 74 | 17.6 | 9.81 | 2.47 | -6.54 | 203 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 93.30 | -6.70 | 6 | 16.7 | -5.64 | -0.70 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.11 | -7.89 | 7 | 0.0 | -2.83 | -0.16 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.91 | -8.09 | 78 | 23.1 | -6.09 | -0.80 | -17.45 | 108 |
| 29 | Parabolic SAR · 1h | trend | 91.87 | -8.13 | 102 | 22.5 | -13.38 | -2.54 | -23.89 | 268 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -13.00 | -2.48 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 91.19 | -8.81 | 198 | 29.3 | -11.90 | -3.28 | -17.61 | 564 |
| 32 | Bollinger breakout · 1h | breakout | 90.80 | -9.20 | 84 | 28.6 | -8.16 | -1.35 | -16.85 | 257 |
| 33 | Agent | meta | 90.73 | -9.27 | 81 | 39.5 | -7.93 | -3.07 | -14.44 | 242 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 90.44 | -9.56 | 0 | — | 4.23 | 0.78 | -14.37 | 1 |
| 35 | EMA 20/50 cross · 1h | trend | 90.41 | -9.59 | 58 | 13.8 | -19.53 | -3.57 | -21.79 | 125 |
| 36 | RSI momentum · 1h | momentum | 89.73 | -10.27 | 78 | 16.7 | -16.73 | -2.95 | -27.20 | 215 |
| 37 | Connors RSI(2) · 1h | reversion | 89.37 | -10.63 | 149 | 40.9 | -23.04 | -6.86 | -24.51 | 206 |
| 38 | Ichimoku · 1h | trend | 88.75 | -11.25 | 55 | 14.5 | -17.50 | -3.30 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.66 | -11.34 | 152 | 46.1 | -18.00 | -3.09 | -22.24 | 366 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -3.96 | -0.94 | -14.01 | 115 |
| 41 | Keltner breakout · 1h | breakout | 87.74 | -12.26 | 56 | 23.2 | -8.70 | -1.10 | -26.99 | 203 |
| 42 | Triple EMA stack · 1h | trend | 87.63 | -12.37 | 85 | 15.3 | -23.92 | -3.18 | -35.30 | 232 |
| 43 | Supertrend · 1h | trend | 87.45 | -12.55 | 86 | 12.8 | -23.77 | -4.91 | -27.41 | 219 |
| 44 | Opening range 15m | breakout | 86.65 | -13.35 | 248 | 25.0 | -16.92 | -4.39 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.28 | -13.72 | 189 | 20.6 | -25.98 | -4.85 | -32.45 | 468 |
| 46 | OBV trend · 1h | momentum | 85.69 | -14.31 | 176 | 17.6 | -22.80 | -3.12 | -35.01 | 320 |
| 47 | Z-score reversion · 1h | reversion | 85.68 | -14.32 | 91 | 30.8 | -13.42 | -2.16 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.80 | -15.21 | 209 | 31.1 | -17.09 | -2.65 | -21.34 | 139 |
| 49 | MACD zero-line · 1h | trend | 84.25 | -15.75 | 87 | 14.9 | -24.85 | -4.97 | -25.13 | 219 |
| 50 | Agent (ML meta-label) | meta | 84.16 | -15.84 | 668 | 18.9 | -11.29 | -2.08 | -15.50 | 386 |
| 51 | Max aggression: 1-day momentum | meta | 83.90 | -16.10 | 15 | 33.3 | -14.51 | -0.51 | -37.31 | 42 |
| 52 | Donchian 20/10 · 1h | breakout | 83.77 | -16.23 | 81 | 17.3 | -1.37 | 0.05 | -25.02 | 215 |
| 53 | Bollinger reversion · 1h | reversion | 82.68 | -17.32 | 157 | 34.4 | -27.96 | -5.38 | -33.53 | 349 |
| 54 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.22 | -18.83 | -47.41 | 602 |
| 55 | Williams %R · 1h | reversion | 82.39 | -17.61 | 182 | 42.9 | -33.47 | -5.30 | -36.50 | 535 |
| 56 | ROC + volume · 1h | momentum | 81.46 | -18.54 | 197 | 20.8 | -17.58 | -2.22 | -32.98 | 391 |
| 57 | CCI reversion · 1h | reversion | 81.01 | -18.99 | 163 | 39.3 | -19.69 | -2.51 | -27.44 | 440 |
| 58 | RSI(14) reversion · 1h | reversion | 80.63 | -19.37 | 75 | 21.3 | -15.95 | -2.82 | -22.27 | 178 |
| 59 | EMA 9/21 cross · 1h | trend | 80.50 | -19.50 | 132 | 11.4 | -29.02 | -6.02 | -29.19 | 312 |
| 60 | Heikin-Ashi · 1h | trend | 79.18 | -20.82 | 212 | 22.6 | -36.41 | -6.05 | -44.56 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.39 | -21.61 | 427 | 21.1 | -37.18 | -5.17 | -48.05 | 1246 |
| 62 | Candlestick reversal · 1h | reversion | 77.63 | -22.37 | 212 | 27.4 | -35.64 | -6.31 | -37.17 | 536 |
| 63 | ROC + volume | momentum | 62.53 | -37.47 | 588 | 22.4 | -75.63 | -17.42 | -78.19 | 1733 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.51 | -17.62 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.79 | -39.21 | 457 | 14.4 | -64.06 | -20.85 | -65.58 | 1201 |
| 66 | Donchian 55/20 | breakout | 59.34 | -40.66 | 471 | 18.3 | -67.82 | -13.47 | -72.80 | 1269 |
| 67 | RSI(14) reversion | reversion | 58.10 | -41.90 | 701 | 25.0 | -74.44 | -16.42 | -74.56 | 1601 |
| 68 | EMA 20/50 cross | trend | 57.24 | -42.76 | 491 | 18.9 | -75.32 | -13.92 | -80.26 | 1421 |
| 69 | VWAP reversion | reversion | 54.03 | -45.97 | 738 | 25.1 | -72.14 | -14.83 | -72.95 | 1514 |
| 70 | Keltner breakout | breakout | 51.67 | -48.33 | 665 | 16.2 | -82.50 | -26.18 | -83.37 | 1817 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -29.74 | -98.65 | 5310 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.11 | -28.50 | -93.67 | 2567 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.22 | -19.90 | -88.01 | 1894 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.88 | -23.42 | -90.97 | 2339 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.95 | -25.56 | -91.03 | 2267 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -32.08 | -97.50 | 3479 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.56 | -35.30 | -96.71 | 3578 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -27.07 | -94.51 | 2543 |
| 79 | AI bee: Boozy | ai | 50.33 | -49.67 | 346 | 5.8 | — | — | — | — |
| 80 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.01 | -24.79 | -82.93 | 1697 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.21 | -99.38 | 5740 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.00 | -25.02 | -91.86 | 2616 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.13 | -31.57 | -96.13 | 3486 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -40.45 | -99.74 | 6169 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.39 | -28.69 | -91.44 | 2336 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -37.35 | -97.56 | 3622 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.38 | -98.46 | 4701 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.58 | -32.09 | -93.85 | 2790 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.01 | -99.53 | 6157 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.88 | -22.43 | -86.91 | 2132 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.94 | -26.83 | -87.94 | 2136 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.88 | -32.59 | -95.88 | 3747 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.84 | -32.08 | -88.97 | 2090 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.41 | -95.73 | 4108 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.77 | -99.90 | 8256 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T17:20 | RSI(14) reversion | buy | MSTR | 14.52 | — | entry signal |
| 2026-10-19T17:10 | Keltner breakout | sell | TSLA | 12.90 | -0.01 | exit signal |
| 2026-10-19T17:10 | Opening range 30m | buy | UPRO | 8.27 | — | rebalance up |
| 2026-10-19T17:10 | Opening range 30m | sell | SPY | 10.09 | -0.01 | exit signal |
| 2026-10-19T17:10 | Opening range 15m | sell | SPY | 8.66 | -0.01 | exit signal |
| 2026-10-19T17:10 | Donchian 55/20 | sell | AMZN | 14.81 | 0.04 | exit signal |
| 2026-10-19T17:05 | VWAP reversion | buy | MSTR | 13.53 | — | entry signal |
| 2026-10-19T17:00 | EMA 9/21 cross · 1h | buy | AMZN | 13.33 | — | entry |
| 2026-10-19T17:00 | EMA 9/21 cross · 1h | sell | ETH-USD | 13.33 | -0.16 | exit signal |
| 2026-10-19T16:55 | VWAP reversion | sell | SQQQ | 13.70 | 0.24 | exit signal |
| 2026-10-19T16:55 | RSI(14) reversion | sell | SQQQ | 14.61 | 0.12 | exit signal |
| 2026-10-19T16:55 | Donchian 55/20 | buy | TSLA | 4.94 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | PLTR | 4.96 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | NVDA | 4.95 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | buy | AMZN | 4.95 | — | rebalance up |
| 2026-10-19T16:55 | Donchian 55/20 | sell | UPRO | 9.89 | -0.05 | exit signal |
| 2026-10-19T16:55 | Donchian 55/20 | sell | SPY | 9.91 | -0.01 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | buy | UPRO | 4.52 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | TSLA | 4.46 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | SPY | 4.49 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | PLTR | 4.48 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | NVDA | 4.49 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | buy | AMZN | 4.46 | — | rebalance up |
| 2026-10-19T16:50 | Donchian 55/20 | sell | TQQQ | 5.38 | 0.01 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | sell | TECL | 5.36 | -0.07 | exit signal |
| 2026-10-19T16:50 | Donchian 55/20 | sell | QQQ | 5.42 | 0.01 | exit signal |
| 2026-10-19T16:45 | VWAP reversion | buy | COIN | 13.44 | — | entry signal |
| 2026-10-19T16:41 | Donchian 55/20 | sell | SOXL | 5.30 | -0.14 | stop-loss |
| 2026-10-19T16:35 | Agent (ML meta-label) | buy | TQQQ | 4.70 | — | entry |
| 2026-10-19T16:35 | Agent (ML meta-label) | buy | TECL | 4.70 | — | entry |
| 2026-10-19T16:35 | Agent (ML meta-label) | sell | GOOGL | 4.23 | 0.00 | selected signal exited |
| 2026-10-19T16:35 | Agent (ML meta-label) | sell | BITX | 5.27 | -0.05 | selected signal exited |
| 2026-10-19T16:31 | Agent (rotation) | sell | TQQQ | 32.32 | -0.29 | selected signal exited |
| 2026-10-19T16:31 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | TQQQ | 106.82 | -0.97 | target is flat |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | TQQQ | 4.51 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | SOXL | 4.41 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | MSFT | 4.71 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | ETHU | 4.87 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | buy | AMD | 4.65 | — | rebalance up |
| 2026-10-19T16:31 | Candlestick reversal · 1h | sell | MSTR | 6.48 | 0.11 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 17:25:05.000160+00:00 -> 2026-10-19 17:35:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
