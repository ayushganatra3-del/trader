# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T17:55:05.000141+00:00 · 25036 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.94 (-8.06%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.23 | -0.14 |
| SQQQ | 19.04 | +0.67 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 29579 decisions in 2659 calls, $0.3698 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T17:55 | 1 / 7 / 23 | cash |  |
| Breezy | 2026-10-16T17:55 | 0 / 24 / 7 | cash |  |
| Boozy | 2026-10-16T17:55 | 1 / 25 / 5 | BITX 61% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | AMZN | 2.38 | +4.65% | 4 |
| VWAP momentum · 1h | SQQQ | 1.75 | +9.18% | 7 |
| Donchian 55/20 | AMD | 1.73 | +2.62% | 3 |
| Candlestick reversal · 1h | LABU | 1.71 | +14.60% | 3 |
| Connors RSI(2) · 1h | GOOGL | 1.70 | +1.58% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 106.84 | 6.84 | 9 | 66.7 | 8.21 | 2.99 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.13 | 6.13 | 10 | 70.0 | 0.29 | 0.17 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.94 | 4.94 | 14 | 35.7 | 7.15 | 1.88 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.33 | 4.33 | 0 | — | 5.34 | 2.58 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.74 | -0.26 | 59 | 39.0 | -11.43 | -3.30 | -13.79 | 126 |
| 8 | Daily: SMA 20/50 cross · AAPL | daily | 99.66 | -0.34 | 0 | — | 3.64 | 1.45 | -5.18 | 1 |
| 9 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.49 | -0.51 | 1 | 100.0 | 0.54 | 0.24 | -7.93 | 9 |
| 10 | Copy: Insider buying | copy | 99.01 | -0.99 | 20 | 45.0 | -11.67 | -1.98 | -20.62 | 75 |
| 11 | Hold SPY | benchmark | 98.76 | -1.24 | 0 | — | -1.51 | -0.82 | -3.23 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.76 | -3.91 | 20 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 98.67 | -1.33 | 51 | 31.4 | 1.86 | 1.04 | -2.96 | 69 |
| 14 | Donchian 55/20 · 1h | breakout | 98.64 | -1.36 | 36 | 16.7 | 8.81 | 1.18 | -22.12 | 109 |
| 15 | Max aggression: 5-day momentum | meta | 98.05 | -1.95 | 8 | 37.5 | -17.82 | -1.48 | -34.64 | 26 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.35 | -2.65 | 0 | — | -4.87 | -1.95 | -7.50 | 1 |
| 17 | Copy: Congress Democrats (NANC) | copy | 96.75 | -3.25 | 0 | — | -2.37 | -0.94 | -5.15 | 1 |
| 18 | Agent (rotation) | meta | 96.75 | -3.25 | 107 | 32.7 | -9.97 | -3.42 | -13.23 | 298 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.62 | -3.38 | 0 | — | -6.44 | -3.52 | -6.67 | 1 |
| 20 | Hold BTC | benchmark | 96.49 | -3.51 | 0 | — | 28.50 | 3.32 | -8.68 | 1 |
| 21 | Trend pullback · 1h | trend | 96.15 | -3.85 | 87 | 24.1 | -21.70 | -6.45 | -22.38 | 152 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.57 | -5.43 | 81 | 19.8 | -9.20 | -1.64 | -13.33 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Daily: Momentum burst | daily | 93.30 | -6.70 | 5 | 20.0 | -6.96 | -0.92 | -19.89 | 42 |
| 26 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.31 | -6.78 | 197 |
| 27 | Parabolic SAR · 1h | trend | 93.12 | -6.88 | 95 | 22.1 | 3.13 | 0.58 | -22.55 | 278 |
| 28 | EMA 20/50 cross · 1h | trend | 92.77 | -7.23 | 54 | 14.8 | -4.35 | -0.40 | -22.92 | 129 |
| 29 | Agent | meta | 91.94 | -8.06 | 77 | 39.0 | -9.80 | -5.21 | -10.73 | 244 |
| 30 | Agent (aggressive) | meta | 91.82 | -8.18 | 38 | 31.6 | -6.42 | -2.26 | -9.30 | 122 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.79 | -0.11 | -14.55 | 118 |
| 32 | Opening range 30m | breakout | 91.02 | -8.98 | 193 | 29.5 | -12.42 | -3.43 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 90.99 | -9.01 | 76 | 17.1 | 0.58 | 0.28 | -26.55 | 219 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.48 | 0.89 | -14.21 | 274 |
| 35 | Daily: Bullish score | daily | 90.56 | -9.44 | 7 | 0.0 | -6.15 | -0.60 | -12.93 | 13 |
| 36 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 37 | Triple EMA stack · 1h | trend | 90.21 | -9.79 | 80 | 16.2 | -8.76 | -0.71 | -33.23 | 235 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.95 | -10.05 | 0 | — | -19.33 | -3.68 | -20.01 | 1 |
| 39 | Copy: Cathie Wood (ARKK) | copy | 89.80 | -10.20 | 0 | — | 0.38 | 0.23 | -13.89 | 1 |
| 40 | MACD cross · 1h | trend | 89.46 | -10.54 | 169 | 23.1 | -14.40 | -1.90 | -27.71 | 454 |
| 41 | Supertrend · 1h | trend | 89.35 | -10.65 | 81 | 12.3 | -3.72 | -0.22 | -30.09 | 213 |
| 42 | Keltner breakout · 1h | breakout | 88.93 | -11.07 | 52 | 23.1 | -9.42 | -1.17 | -27.05 | 210 |
| 43 | Connors RSI(2) · 1h | reversion | 88.23 | -11.77 | 144 | 40.3 | -24.79 | -7.40 | -25.74 | 243 |
| 44 | OBV trend · 1h | momentum | 87.90 | -12.10 | 168 | 18.5 | -9.02 | -0.74 | -33.94 | 320 |
| 45 | Stochastic reversion · 1h | reversion | 87.39 | -12.61 | 135 | 43.7 | -20.26 | -3.70 | -21.55 | 352 |
| 46 | Opening range 15m | breakout | 86.44 | -13.55 | 242 | 25.2 | -17.40 | -4.52 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -23.24 | -4.56 | -23.33 | 224 |
| 48 | Max aggression: 1-day momentum | meta | 86.00 | -14.00 | 14 | 35.7 | -10.73 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.85 | -15.15 | 78 | 17.9 | 0.71 | 0.30 | -21.63 | 219 |
| 50 | Three white soldiers | momentum | 84.72 | -15.28 | 207 | 18.8 | -47.86 | -19.97 | -48.52 | 609 |
| 51 | Z-score reversion · 1h | reversion | 84.66 | -15.34 | 83 | 32.5 | -14.32 | -2.54 | -18.68 | 180 |
| 52 | MFI reversion · 1h ⏸ | reversion | 84.04 | -15.96 | 204 | 30.4 | -21.43 | -3.61 | -21.71 | 140 |
| 53 | Agent (ML meta-label) | meta | 83.82 | -16.18 | 599 | 18.9 | -8.69 | -1.20 | -18.40 | 391 |
| 54 | Heikin-Ashi · 1h | trend | 83.76 | -16.24 | 189 | 24.3 | -31.26 | -5.11 | -40.33 | 673 |
| 55 | VWAP momentum · 1h | momentum | 83.74 | -16.26 | 387 | 21.2 | -36.34 | -5.50 | -43.85 | 1253 |
| 56 | ROC + volume · 1h | momentum | 82.86 | -17.14 | 191 | 21.5 | -12.55 | -1.66 | -26.42 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.28 | -17.72 | 126 | 11.9 | -7.22 | -0.65 | -29.65 | 320 |
| 58 | Williams %R · 1h | reversion | 80.89 | -19.11 | 180 | 42.2 | -34.06 | -5.58 | -35.16 | 524 |
| 59 | Bollinger reversion · 1h | reversion | 80.79 | -19.20 | 138 | 31.2 | -29.81 | -6.21 | -31.83 | 337 |
| 60 | RSI(14) reversion · 1h | reversion | 80.36 | -19.64 | 71 | 21.1 | -14.69 | -2.62 | -21.29 | 165 |
| 61 | CCI reversion · 1h | reversion | 80.01 | -19.99 | 159 | 39.0 | -18.50 | -2.41 | -24.55 | 427 |
| 62 | Candlestick reversal · 1h | reversion | 76.44 | -23.56 | 203 | 25.1 | -34.93 | -6.29 | -35.50 | 519 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -62.95 | -17.79 | -62.95 | 891 |
| 64 | ROC + volume | momentum | 63.32 | -36.68 | 546 | 21.8 | -75.78 | -17.48 | -77.39 | 1709 |
| 65 | Squeeze breakout | breakout | 63.25 | -36.76 | 428 | 14.7 | -62.94 | -17.80 | -63.91 | 1217 |
| 66 | RSI(14) reversion | reversion | 63.16 | -36.84 | 619 | 27.0 | -74.57 | -16.69 | -74.60 | 1620 |
| 67 | Donchian 55/20 | breakout | 61.39 | -38.61 | 434 | 17.7 | -69.24 | -14.49 | -71.81 | 1285 |
| 68 | EMA 20/50 cross | trend | 59.82 | -40.18 | 454 | 19.2 | -77.25 | -15.12 | -79.04 | 1451 |
| 69 | VWAP reversion | reversion | 55.91 | -44.09 | 631 | 22.8 | -73.46 | -15.45 | -73.52 | 1489 |
| 70 | AI bee: Boozy | ai | 55.88 | -44.12 | 293 | 5.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.66 | -45.34 | 606 | 16.0 | -83.69 | -26.97 | -83.80 | 1848 |
| 72 | Ichimoku | trend | 51.90 | -48.10 | 552 | 11.6 | -82.01 | -22.77 | -82.11 | 1733 |
| 73 | Supertrend | trend | 51.37 | -48.63 | 632 | 19.8 | -86.55 | -20.33 | -86.95 | 1916 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -29.33 | -98.63 | 5311 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -29.86 | -93.53 | 2601 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -24.50 | -90.57 | 2368 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.82 | -27.13 | -91.83 | 2345 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.44 | -31.97 | -97.45 | 3527 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.71 | -35.83 | -96.72 | 3597 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.41 | -26.18 | -94.46 | 2621 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.90 | -99.41 | 5803 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.40 | -25.70 | -91.45 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.37 | -31.69 | -96.38 | 3572 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.66 | -99.73 | 6208 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.10 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -37.52 | -97.47 | 3653 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.08 | -98.50 | 4750 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.66 | -32.65 | -93.71 | 2807 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.16 | -99.55 | 6247 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.63 | -22.20 | -86.65 | 2160 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.04 | -27.08 | -88.04 | 2162 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -32.24 | -96.01 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.36 | -33.71 | -89.36 | 2108 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.85 | -33.53 | -95.87 | 4148 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.02 | -99.89 | 8276 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T17:55 | CCI reversion · 1h | sell | AMZN | 13.28 | -0.12 | stop-loss |
| 2026-10-16T17:55 | Z-score reversion · 1h | sell | AMZN | 12.06 | -0.16 | stop-loss |
| 2026-10-16T17:55 | RSI(14) reversion · 1h | buy | NVDA | 5.98 | — | rebalance up |
| 2026-10-16T17:55 | RSI(14) reversion · 1h | buy | IWM | 4.54 | — | rebalance up |
| 2026-10-16T17:55 | RSI(14) reversion · 1h | buy | ETHU | 4.66 | — | rebalance up |
| 2026-10-16T17:55 | RSI(14) reversion · 1h | buy | AMD | 6.07 | — | rebalance up |
| 2026-10-16T17:55 | RSI(14) reversion · 1h | sell | AMZN | 11.49 | -0.18 | stop-loss |
| 2026-10-16T17:45 | Supertrend | buy | XRP-USD | 8.61 | — | entry signal |
| 2026-10-16T17:45 | Supertrend | buy | SOL-USD | 8.63 | — | entry signal |
| 2026-10-16T17:45 | Supertrend | buy | ETHU | 8.63 | — | entry signal |
| 2026-10-16T17:45 | Supertrend | buy | ETH-USD | 8.63 | — | entry signal |
| 2026-10-16T17:45 | Supertrend | sell | BTC-USD | 4.28 | -0.02 | rebalance down |
| 2026-10-16T17:45 | Supertrend | sell | BITX | 4.33 | 0.00 | rebalance down |
| 2026-10-16T17:37 | AI bee: Boozy | buy | BITX | 34.15 | — | Jev: buy (buy p=0.61) |
| 2026-10-16T17:37 | AI bee: Boozy | sell | COIN | 31.20 | -0.31 | Jev: buy |
| 2026-10-16T17:35 | Supertrend | buy | BTC-USD | 12.94 | — | entry signal |
| 2026-10-16T17:35 | Supertrend | buy | BITX | 12.94 | — | entry signal |
| 2026-10-16T17:30 | Agent (ML meta-label) | buy | MSFT | 6.45 | — | entry |
| 2026-10-16T17:30 | Agent (ML meta-label) | buy | LABU | 6.45 | — | following Candlestick reversal · 1h |
| 2026-10-16T17:30 | Stochastic reversion · 1h | buy | PLTR | 14.58 | — | entry signal |
| 2026-10-16T17:30 | Stochastic reversion · 1h | buy | MSFT | 14.59 | — | entry signal |
| 2026-10-16T17:30 | Stochastic reversion · 1h | buy | LABU | 14.59 | — | entry signal |
| 2026-10-16T17:30 | Stochastic reversion · 1h | sell | TECL | 7.36 | -0.23 | rebalance down |
| 2026-10-16T17:30 | Stochastic reversion · 1h | sell | SOXL | 7.26 | -0.18 | rebalance down |
| 2026-10-16T17:30 | Stochastic reversion · 1h | sell | AMD | 7.23 | -0.06 | rebalance down |
| 2026-10-16T17:30 | Candlestick reversal · 1h | sell | BITX | 19.13 | -0.30 | exit signal |
| 2026-10-16T17:30 | Candlestick reversal · 1h | sell | AMD | 15.43 | -0.18 | exit signal |
| 2026-10-16T17:30 | VWAP momentum · 1h | sell | AAPL | 20.80 | -0.09 | exit signal |
| 2026-10-16T17:30 | Supertrend · 1h | buy | SQQQ | 6.75 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | buy | ETHU | 7.60 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | buy | ETH-USD | 7.42 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | buy | COIN | 7.56 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | buy | BTC-USD | 7.40 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | buy | AAPL | 7.24 | — | rebalance up |
| 2026-10-16T17:30 | Supertrend · 1h | sell | TNA | 7.29 | -0.35 | exit signal |
| 2026-10-16T17:30 | Supertrend · 1h | sell | IWM | 7.50 | -0.14 | exit signal |
| 2026-10-16T17:30 | RSI(14) reversion | buy | XRP-USD | 4.50 | — | entry signal |
| 2026-10-16T17:30 | RSI(14) reversion | buy | UPRO | 4.52 | — | entry signal |
| 2026-10-16T17:30 | RSI(14) reversion | buy | TSLA | 4.52 | — | entry signal |
| 2026-10-16T17:30 | RSI(14) reversion | buy | TQQQ | 4.52 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 17:55:05.000141+00:00 -> 2026-10-16 18:05:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
