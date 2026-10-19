# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-19T18:25:05.000145+00:00 · 28648 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.72 (-9.28%)

Closed trades 82, win rate 40.2%, fees £2.81, max drawdown -9.80%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 18.12 | -0.03 |

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

Today: 29499 decisions in 2673 calls, $0.3675 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-19T18:25 | 2 / 7 / 19 | cash |  |
| Breezy | 2026-10-19T18:25 | 0 / 22 / 6 | cash |  |
| Boozy | 2026-10-19T18:25 | 0 / 24 / 4 | COIN 72% |  |

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
| 4 | Copy: Warren Buffett (BRK-B) | copy | 105.09 | 5.09 | 0 | — | 5.69 | 2.78 | -5.18 | 1 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -7.64 | -2.06 | -13.79 | 136 |
| 6 | Daily: SMA 20/50 cross · AAPL | daily | 100.12 | 0.12 | 0 | — | 2.43 | 1.02 | -5.18 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.32 | -0.68 | 0 | — | -0.13 | -0.03 | -3.13 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -3.01 | -3.44 | -3.91 | 20 |
| 11 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.56 | -1.44 | 3 | 33.3 | 2.59 | 0.65 | -7.93 | 9 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 98.19 | -1.81 | 54 | 31.5 | 3.06 | 1.69 | -2.17 | 63 |
| 13 | Agent (rotation) | meta | 97.54 | -2.46 | 112 | 32.1 | -3.43 | -1.60 | -6.06 | 278 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.45 | -2.55 | 0 | — | -0.94 | -0.33 | -5.31 | 1 |
| 15 | Donchian 55/20 · 1h | breakout | 97.33 | -2.67 | 36 | 16.7 | -9.49 | -1.59 | -19.34 | 100 |
| 16 | Hold BTC | benchmark | 97.26 | -2.74 | 0 | — | 25.91 | 3.09 | -8.68 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -4.08 | -2.31 | -5.83 | 1 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 96.60 | -3.40 | 0 | — | -5.71 | -2.25 | -7.04 | 1 |
| 19 | Trend pullback · 1h | trend | 96.55 | -3.45 | 88 | 23.9 | -19.58 | -5.78 | -20.58 | 136 |
| 20 | Copy: Insider buying | copy | 96.41 | -3.58 | 23 | 43.5 | -15.00 | -2.71 | -20.62 | 73 |
| 21 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.78 | -2.89 | -6.31 | 32 |
| 22 | Max aggression: 5-day momentum | meta | 95.35 | -4.64 | 8 | 37.5 | -20.15 | -1.70 | -34.64 | 26 |
| 23 | ADX DI cross · 1h | trend | 93.59 | -6.41 | 87 | 18.4 | -13.98 | -2.51 | -16.51 | 255 |
| 24 | Gap and go | momentum | 93.58 | -6.42 | 75 | 18.7 | 9.73 | 2.45 | -6.54 | 203 |
| 25 | Squeeze breakout · 1h | breakout | 93.44 | -6.56 | 42 | 23.8 | -1.76 | -0.35 | -9.46 | 93 |
| 26 | Daily: Momentum burst | daily | 93.13 | -6.87 | 6 | 16.7 | -5.87 | -0.74 | -20.58 | 40 |
| 27 | Daily: Bullish score | daily | 92.12 | -7.88 | 7 | 0.0 | -2.69 | -0.14 | -13.10 | 12 |
| 28 | Volume breakout · 1h | breakout | 91.85 | -8.15 | 78 | 23.1 | -5.58 | -0.75 | -16.37 | 107 |
| 29 | Parabolic SAR · 1h | trend | 91.79 | -8.21 | 102 | 22.5 | -14.09 | -2.67 | -24.44 | 267 |
| 30 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -12.98 | -2.47 | -16.91 | 1 |
| 31 | Opening range 30m | breakout | 90.94 | -9.06 | 201 | 28.9 | -12.15 | -3.35 | -17.61 | 564 |
| 32 | Bollinger breakout · 1h | breakout | 90.74 | -9.26 | 84 | 28.6 | -8.23 | -1.37 | -16.85 | 257 |
| 33 | Agent | meta | 90.72 | -9.28 | 82 | 40.2 | -8.82 | -3.40 | -15.99 | 261 |
| 34 | EMA 20/50 cross · 1h | trend | 90.38 | -9.62 | 58 | 13.8 | -18.83 | -3.44 | -21.09 | 125 |
| 35 | Copy: Cathie Wood (ARKK) | copy | 90.16 | -9.84 | 0 | — | 4.06 | 0.76 | -14.37 | 1 |
| 36 | RSI momentum · 1h | momentum | 89.62 | -10.38 | 78 | 16.7 | -17.34 | -2.87 | -28.43 | 213 |
| 37 | Connors RSI(2) · 1h | reversion | 89.46 | -10.54 | 149 | 40.9 | -22.96 | -6.81 | -24.51 | 206 |
| 38 | Ichimoku · 1h | trend | 88.67 | -11.33 | 55 | 14.5 | -17.57 | -3.31 | -18.08 | 113 |
| 39 | Stochastic reversion · 1h | reversion | 88.40 | -11.60 | 152 | 46.1 | -17.02 | -2.94 | -22.24 | 362 |
| 40 | Agent (aggressive) | meta | 87.92 | -12.08 | 41 | 34.1 | -3.78 | -0.92 | -13.96 | 116 |
| 41 | Keltner breakout · 1h | breakout | 87.68 | -12.32 | 56 | 23.2 | -11.54 | -1.60 | -26.92 | 202 |
| 42 | Triple EMA stack · 1h | trend | 87.64 | -12.36 | 85 | 15.3 | -21.60 | -3.01 | -32.93 | 230 |
| 43 | Supertrend · 1h | trend | 87.18 | -12.82 | 86 | 12.8 | -23.99 | -4.96 | -27.53 | 219 |
| 44 | Opening range 15m | breakout | 86.43 | -13.57 | 250 | 24.8 | -17.15 | -4.45 | -21.40 | 702 |
| 45 | MACD cross · 1h | trend | 86.09 | -13.91 | 189 | 20.6 | -26.14 | -4.88 | -32.54 | 469 |
| 46 | OBV trend · 1h | momentum | 85.54 | -14.46 | 179 | 17.9 | -23.53 | -3.23 | -35.43 | 319 |
| 47 | Z-score reversion · 1h | reversion | 85.39 | -14.61 | 91 | 30.8 | -13.68 | -2.22 | -21.32 | 198 |
| 48 | MFI reversion · 1h | reversion | 84.53 | -15.47 | 209 | 31.1 | -17.87 | -2.79 | -21.34 | 139 |
| 49 | MACD zero-line · 1h | trend | 84.20 | -15.80 | 87 | 14.9 | -24.96 | -4.99 | -25.20 | 219 |
| 50 | Agent (ML meta-label) | meta | 83.90 | -16.10 | 672 | 18.8 | -8.59 | -1.48 | -16.21 | 392 |
| 51 | Donchian 20/10 · 1h | breakout | 83.63 | -16.37 | 81 | 17.3 | -1.13 | 0.08 | -25.20 | 214 |
| 52 | Bollinger reversion · 1h | reversion | 82.72 | -17.28 | 157 | 34.4 | -27.92 | -5.36 | -33.53 | 349 |
| 53 | Max aggression: 1-day momentum | meta | 82.67 | -17.33 | 15 | 33.3 | -15.77 | -0.59 | -37.31 | 42 |
| 54 | Three white soldiers | momentum | 82.64 | -17.36 | 230 | 19.1 | -47.33 | -18.83 | -47.47 | 602 |
| 55 | Williams %R · 1h | reversion | 82.15 | -17.85 | 182 | 42.9 | -33.65 | -5.36 | -36.50 | 535 |
| 56 | ROC + volume · 1h | momentum | 81.38 | -18.62 | 197 | 20.8 | -18.45 | -2.49 | -33.74 | 389 |
| 57 | CCI reversion · 1h | reversion | 80.76 | -19.24 | 163 | 39.3 | -19.91 | -2.52 | -27.44 | 438 |
| 58 | RSI(14) reversion · 1h | reversion | 80.28 | -19.72 | 75 | 21.3 | -14.41 | -2.59 | -22.27 | 174 |
| 59 | EMA 9/21 cross · 1h | trend | 80.12 | -19.88 | 134 | 11.2 | -29.18 | -6.05 | -29.45 | 312 |
| 60 | Heikin-Ashi · 1h | trend | 78.96 | -21.04 | 221 | 21.7 | -36.60 | -6.08 | -44.70 | 681 |
| 61 | VWAP momentum · 1h | momentum | 78.07 | -21.93 | 431 | 20.9 | -39.66 | -6.21 | -48.22 | 1244 |
| 62 | Candlestick reversal · 1h | reversion | 77.22 | -22.78 | 213 | 27.2 | -35.65 | -6.50 | -37.45 | 535 |
| 63 | ROC + volume | momentum | 62.50 | -37.50 | 590 | 22.5 | -75.65 | -17.43 | -78.19 | 1733 |
| 64 | Volume breakout | breakout | 61.60 | -38.40 | 358 | 13.1 | -62.51 | -17.62 | -64.19 | 877 |
| 65 | Squeeze breakout | breakout | 60.83 | -39.17 | 457 | 14.4 | -63.91 | -20.64 | -65.58 | 1200 |
| 66 | Donchian 55/20 | breakout | 59.20 | -40.80 | 474 | 18.6 | -68.13 | -13.93 | -72.80 | 1264 |
| 67 | RSI(14) reversion | reversion | 57.81 | -42.19 | 702 | 25.1 | -74.01 | -15.98 | -74.42 | 1603 |
| 68 | EMA 20/50 cross | trend | 57.08 | -42.92 | 494 | 19.0 | -75.34 | -13.88 | -80.26 | 1418 |
| 69 | VWAP reversion | reversion | 53.74 | -46.26 | 741 | 25.1 | -72.44 | -15.03 | -73.01 | 1514 |
| 70 | Keltner breakout | breakout | 51.59 | -48.41 | 666 | 16.4 | -82.44 | -25.88 | -83.37 | 1812 |
| 71 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.64 | -29.66 | -98.65 | 5287 |
| 72 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.12 | -28.23 | -93.67 | 2564 |
| 73 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.25 | -19.91 | -88.02 | 1894 |
| 74 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -89.81 | -22.82 | -91.01 | 2342 |
| 75 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.89 | -25.41 | -91.00 | 2264 |
| 76 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -31.73 | -97.51 | 3484 |
| 77 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -34.44 | -96.71 | 3576 |
| 78 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -27.64 | -94.49 | 2533 |
| 79 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.02 | -24.69 | -82.93 | 1696 |
| 80 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.97 | -99.37 | 5741 |
| 81 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.03 | -24.91 | -91.90 | 2614 |
| 82 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.13 | -31.57 | -96.13 | 3487 |
| 83 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.67 | -99.74 | 6169 |
| 84 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.66 | -29.46 | -91.70 | 2332 |
| 85 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.50 | -36.64 | -97.59 | 3627 |
| 86 | AI bee: Boozy | ai | 50.07 | -49.93 | 346 | 5.8 | — | — | — | — |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -36.38 | -98.46 | 4705 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.60 | -31.96 | -93.87 | 2792 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -38.95 | -99.53 | 6163 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.90 | -22.43 | -86.90 | 2134 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.92 | -26.74 | -87.92 | 2138 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.58 | -95.89 | 3749 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -88.90 | -32.29 | -88.97 | 2095 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.73 | -33.36 | -95.73 | 4109 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -44.74 | -99.90 | 8264 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-19T18:25 | Donchian 20/10 · 1h | buy | DOGE-USD | 4.20 | — | rebalance up |
| 2026-10-19T18:25 | VWAP reversion | buy | ETH-USD | 2.70 | — | rebalance up |
| 2026-10-19T18:25 | VWAP reversion | buy | COIN | 5.37 | — | rebalance up |
| 2026-10-19T18:25 | VWAP reversion | buy | AMD | 2.70 | — | rebalance up |
| 2026-10-19T18:25 | VWAP reversion | sell | MSTR | 10.73 | -0.09 | stop-loss |
| 2026-10-19T18:25 | Donchian 55/20 | sell | TSLA | 14.77 | -0.01 | exit signal |
| 2026-10-19T18:25 | Gap and go | sell | AMZN | 18.86 | 0.27 | exit signal |
| 2026-10-19T18:15 | Keltner breakout | buy | AAPL | 12.90 | — | entry signal |
| 2026-10-19T18:10 | Donchian 55/20 | sell | PLTR | 14.79 | 0.01 | exit signal |
| 2026-10-19T18:10 | ROC + volume | sell | SQQQ | 15.61 | -0.02 | exit signal |
| 2026-10-19T18:10 | EMA 20/50 cross | buy | UPRO | 3.55 | — | entry |
| 2026-10-19T18:10 | EMA 20/50 cross | buy | GOOGL | 2.96 | — | rebalance up |
| 2026-10-19T18:10 | EMA 20/50 cross | sell | TECL | 5.69 | 0.03 | exit signal |
| 2026-10-19T18:05 | Agent (ML meta-label) | buy | GOOGL | 4.71 | — | entry |
| 2026-10-19T18:05 | VWAP reversion | sell | ETH-USD | 2.71 | -0.00 | rebalance down |
| 2026-10-19T18:02 | VWAP reversion | buy | COIN | 2.70 | — | rebalance up |
| 2026-10-19T18:02 | VWAP reversion | sell | AMD | 2.70 | -0.00 | rebalance down |
| 2026-10-19T18:00 | Agent (ML meta-label) | buy | TSLA | 5.25 | — | entry |
| 2026-10-19T18:00 | Agent (ML meta-label) | sell | GOOGL | 4.94 | -0.01 | selected signal exited |
| 2026-10-19T18:00 | Agent (ML meta-label) | sell | AMZN | 4.95 | -0.01 | selected signal exited |
| 2026-10-19T18:00 | Agent | buy | BITX | 18.15 | — | following VWAP reversion |
| 2026-10-19T18:00 | MFI reversion · 1h | buy | ETH-USD | 21.18 | — | entry signal |
| 2026-10-19T18:00 | Candlestick reversal · 1h | sell | MSTR | 6.66 | -0.01 | target is flat |
| 2026-10-19T18:00 | OBV trend · 1h | buy | SQQQ | 7.13 | — | rebalance up |
| 2026-10-19T18:00 | OBV trend · 1h | buy | MSFT | 7.12 | — | rebalance up |
| 2026-10-19T18:00 | OBV trend · 1h | buy | AMZN | 7.19 | — | rebalance up |
| 2026-10-19T18:00 | OBV trend · 1h | sell | XRP-USD | 14.22 | -0.08 | exit signal |
| 2026-10-19T18:00 | OBV trend · 1h | sell | SOL-USD | 14.24 | -0.12 | exit signal |
| 2026-10-19T18:00 | OBV trend · 1h | sell | AAPL | 14.29 | 0.01 | target is flat |
| 2026-10-19T18:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 6.65 | — | rebalance up |
| 2026-10-19T18:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 6.68 | — | rebalance up |
| 2026-10-19T18:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 6.73 | — | rebalance up |
| 2026-10-19T18:00 | EMA 9/21 cross · 1h | buy | AMZN | 6.79 | — | rebalance up |
| 2026-10-19T18:00 | EMA 9/21 cross · 1h | sell | BTC-USD | 13.41 | -0.11 | exit signal |
| 2026-10-19T18:00 | VWAP reversion | buy | COIN | 5.40 | — | entry signal |
| 2026-10-19T18:00 | VWAP reversion | buy | BITX | 10.79 | — | entry |
| 2026-10-19T18:00 | VWAP reversion | sell | MSTR | 2.70 | -0.01 | rebalance down |
| 2026-10-19T18:00 | RSI(14) reversion | buy | SOXL | 14.53 | — | entry signal |
| 2026-10-19T18:00 | RSI(14) reversion | buy | COIN | 14.53 | — | entry signal |
| 2026-10-19T17:50 | Keltner breakout | sell | LABU | 12.92 | 0.14 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-21 18:25:05.000145+00:00 -> 2026-10-19 18:35:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
