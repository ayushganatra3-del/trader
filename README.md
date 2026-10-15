# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T14:56:05.000142+00:00 · 23729 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: timed out |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 16392 decisions in 2217 calls, $0.2151 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T14:56 | 2 / 23 / 5 | SOXL 14%, MSTR 15%, TNA 15%, COIN 14% |  |
| Breezy | 2026-10-15T14:56 | 0 / 27 / 3 | cash |  |
| Boozy | 2026-10-15T14:56 | 4 / 25 / 1 | MSTR 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.86 | +4.13% | 5 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 4.73 | 2.25 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 103.35 | 3.35 | 1 | 100.0 | 4.01 | 1.10 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.19 | 2.62 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.42 | -0.73 | -9.61 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.91 | 0.91 | 0 | — | 4.76 | 1.84 | -5.18 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Hold SPY | benchmark | 99.87 | -0.13 | 0 | — | -0.96 | -0.52 | -3.35 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.85 | -0.15 | 57 | 38.6 | -10.58 | -3.06 | -13.79 | 123 |
| 11 | Copy: Insider buying | copy | 99.46 | -0.54 | 20 | 45.0 | -16.53 | -2.64 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.00 | -2.00 | 0 | — | -1.71 | -0.69 | -4.45 | 1 |
| 14 | Donchian 55/20 · 1h | breakout | 97.64 | -2.36 | 36 | 16.7 | 7.12 | 0.99 | -22.11 | 112 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Hold BTC | benchmark | 97.60 | -2.40 | 0 | — | 29.61 | 3.42 | -8.68 | 1 |
| 17 | Timing: Nasdaq FTD · QQQ | daily | 97.53 | -2.47 | 0 | — | -5.58 | -3.07 | -6.38 | 1 |
| 18 | Trend pullback · 1h | trend | 96.99 | -3.01 | 86 | 24.4 | -24.16 | -7.06 | -25.21 | 165 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.67 | -3.33 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | ADX DI cross · 1h | trend | 96.53 | -3.47 | 70 | 21.4 | -9.47 | -1.68 | -14.76 | 253 |
| 21 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.18 | -3.16 | -5.30 | 30 |
| 22 | Daily: Momentum burst | daily | 96.19 | -3.81 | 5 | 20.0 | -4.44 | -0.52 | -17.67 | 39 |
| 23 | Agent (rotation) | meta | 95.86 | -4.14 | 104 | 30.8 | -12.06 | -4.04 | -13.23 | 287 |
| 24 | Max aggression: 5-day momentum | meta | 94.33 | -5.67 | 8 | 37.5 | -5.30 | -0.17 | -34.64 | 26 |
| 25 | Parabolic SAR · 1h | trend | 93.91 | -6.09 | 93 | 22.6 | 1.80 | 0.42 | -22.50 | 286 |
| 26 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.38 | 1.16 | -9.46 | 101 |
| 27 | EMA 20/50 cross · 1h | trend | 93.63 | -6.37 | 51 | 15.7 | 1.15 | 0.34 | -23.70 | 130 |
| 28 | Gap and go | momentum | 93.45 | -6.55 | 65 | 12.3 | 9.04 | 2.27 | -6.78 | 202 |
| 29 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -7.56 | -3.59 | -8.95 | 243 |
| 30 | Daily: Bullish score | daily | 92.98 | -7.02 | 7 | 0.0 | -4.61 | -0.40 | -12.76 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 92.41 | -7.59 | 79 | 30.4 | 8.39 | 1.22 | -14.21 | 276 |
| 32 | RSI momentum · 1h | momentum | 92.30 | -7.70 | 73 | 17.8 | 1.38 | 0.37 | -25.36 | 226 |
| 33 | Supertrend · 1h | trend | 92.29 | -7.71 | 73 | 13.7 | 4.06 | 0.68 | -23.22 | 206 |
| 34 | Timing: Nasdaq FTD · TQQQ | daily | 92.22 | -7.78 | 0 | — | -17.07 | -3.24 | -19.22 | 1 |
| 35 | MACD cross · 1h | trend | 92.18 | -7.82 | 154 | 22.1 | -12.73 | -1.74 | -22.49 | 460 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | 6.93 | 1.11 | -12.60 | 120 |
| 37 | Copy: Cathie Wood (ARKK) | copy | 91.37 | -8.63 | 0 | — | 2.65 | 0.56 | -13.89 | 1 |
| 38 | Triple EMA stack · 1h | trend | 90.83 | -9.17 | 77 | 16.9 | -6.72 | -0.51 | -31.79 | 228 |
| 39 | Ichimoku · 1h | trend | 90.52 | -9.47 | 51 | 15.7 | 1.04 | 0.33 | -22.64 | 123 |
| 40 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -9.96 | -3.55 | -11.21 | 130 |
| 41 | Stochastic reversion · 1h | reversion | 90.18 | -9.82 | 127 | 44.1 | -17.99 | -3.34 | -20.43 | 352 |
| 42 | Opening range 30m | breakout | 90.14 | -9.86 | 169 | 23.1 | -13.19 | -3.87 | -17.60 | 564 |
| 43 | Connors RSI(2) · 1h | reversion | 89.33 | -10.67 | 141 | 39.7 | -22.91 | -6.81 | -24.89 | 250 |
| 44 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -16.78 | -0.62 | -37.31 | 43 |
| 45 | MFI reversion · 1h | reversion | 88.95 | -11.05 | 183 | 29.0 | -18.12 | -3.14 | -20.11 | 138 |
| 46 | OBV trend · 1h | momentum | 88.62 | -11.38 | 164 | 18.9 | -10.94 | -0.94 | -35.24 | 320 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -6.87 | -0.70 | -26.75 | 215 |
| 48 | MACD zero-line · 1h | trend | 87.87 | -12.13 | 74 | 16.2 | -21.48 | -4.09 | -22.51 | 224 |
| 49 | Z-score reversion · 1h | reversion | 87.22 | -12.78 | 70 | 32.9 | -11.61 | -2.05 | -17.27 | 170 |
| 50 | Donchian 20/10 · 1h | breakout | 86.66 | -13.34 | 72 | 19.4 | -0.53 | 0.13 | -20.38 | 215 |
| 51 | Agent (ML meta-label) | meta | 86.50 | -13.50 | 562 | 18.0 | -5.25 | -0.74 | -14.72 | 412 |
| 52 | Heikin-Ashi · 1h | trend | 86.15 | -13.85 | 169 | 26.0 | -30.13 | -4.86 | -39.17 | 659 |
| 53 | ROC + volume · 1h | momentum | 86.10 | -13.90 | 179 | 21.2 | -10.44 | -1.38 | -25.30 | 396 |
| 54 | VWAP momentum · 1h | momentum | 85.79 | -14.21 | 353 | 21.8 | -36.13 | -5.41 | -43.07 | 1240 |
| 55 | Opening range 15m | breakout | 85.75 | -14.25 | 216 | 20.4 | -18.43 | -5.00 | -21.40 | 704 |
| 56 | EMA 9/21 cross · 1h | trend | 85.16 | -14.84 | 120 | 12.5 | -10.19 | -1.18 | -27.74 | 319 |
| 57 | Three white soldiers | momentum | 85.06 | -14.95 | 187 | 16.0 | -47.71 | -19.72 | -48.93 | 599 |
| 58 | Bollinger reversion · 1h | reversion | 83.57 | -16.43 | 126 | 28.6 | -27.33 | -5.82 | -31.44 | 330 |
| 59 | RSI(14) reversion · 1h | reversion | 82.50 | -17.50 | 60 | 21.7 | -13.16 | -2.22 | -18.95 | 156 |
| 60 | Williams %R · 1h | reversion | 82.44 | -17.56 | 162 | 41.4 | -32.76 | -5.39 | -34.81 | 515 |
| 61 | CCI reversion · 1h | reversion | 82.41 | -17.59 | 137 | 40.1 | -18.33 | -2.41 | -23.38 | 422 |
| 62 | Candlestick reversal · 1h | reversion | 79.76 | -20.24 | 179 | 24.6 | -32.36 | -5.96 | -33.65 | 506 |
| 63 | ROC + volume | momentum | 66.96 | -33.04 | 492 | 21.5 | -74.15 | -16.48 | -76.49 | 1681 |
| 64 | RSI(14) reversion | reversion | 66.01 | -33.99 | 561 | 27.6 | -73.53 | -16.53 | -74.12 | 1571 |
| 65 | Volume breakout | breakout | 65.31 | -34.69 | 310 | 13.5 | -63.24 | -17.79 | -63.29 | 886 |
| 66 | Squeeze breakout | breakout | 64.57 | -35.43 | 404 | 14.6 | -62.88 | -17.47 | -63.39 | 1208 |
| 67 | Donchian 55/20 | breakout | 63.02 | -36.98 | 400 | 16.8 | -68.77 | -14.23 | -71.15 | 1272 |
| 68 | EMA 20/50 cross | trend | 61.38 | -38.62 | 421 | 18.8 | -77.41 | -15.05 | -78.49 | 1438 |
| 69 | VWAP reversion | reversion | 58.42 | -41.58 | 581 | 24.6 | -72.36 | -14.93 | -72.64 | 1426 |
| 70 | AI bee: Boozy | ai | 56.73 | -43.27 | 277 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.07 | -43.93 | 559 | 14.1 | -83.40 | -26.11 | -83.58 | 1839 |
| 72 | Supertrend | trend | 54.27 | -45.73 | 581 | 18.6 | -86.49 | -20.05 | -86.62 | 1900 |
| 73 | Ichimoku | trend | 53.26 | -46.74 | 493 | 9.7 | -82.04 | -22.38 | -82.12 | 1703 |
| 74 | AI bee: Bizzy | ai | 50.96 | -49.04 | 1011 | 8.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -28.96 | -98.65 | 5364 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.46 | -28.77 | -93.56 | 2566 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -23.93 | -90.72 | 2352 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.46 | -25.86 | -91.49 | 2322 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -31.40 | -97.48 | 3506 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -34.14 | -96.58 | 3561 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.40 | -24.49 | -94.41 | 2604 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -35.41 | -99.42 | 5767 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.18 | -25.08 | -91.25 | 2621 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.17 | -29.87 | -96.19 | 3542 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.40 | -99.73 | 6169 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.87 | -28.62 | -91.95 | 2355 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -36.08 | -97.45 | 3637 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.53 | -35.64 | -98.55 | 4694 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.43 | -31.09 | -93.54 | 2775 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.87 | -99.56 | 6167 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.28 | -21.85 | -86.54 | 2124 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.90 | -26.73 | -88.11 | 2129 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -31.91 | -96.13 | 3784 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.40 | -32.96 | -89.47 | 2110 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -32.87 | -95.91 | 4072 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.75 | -99.89 | 8209 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T14:55 | Agent (ML meta-label) | buy | TECL | 6.65 | — | entry |
| 2026-10-15T14:55 | Agent (ML meta-label) | buy | NVDA | 6.65 | — | following Ichimoku |
| 2026-10-15T14:55 | RSI(14) reversion | sell | ETHU | 5.20 | 0.18 | take-profit |
| 2026-10-15T14:55 | ROC + volume | buy | COIN | 9.53 | — | entry |
| 2026-10-15T14:55 | ROC + volume | buy | AMZN | 9.57 | — | entry signal |
| 2026-10-15T14:55 | ROC + volume | sell | XRP-USD | 3.79 | 0.01 | rebalance down |
| 2026-10-15T14:55 | ROC + volume | sell | TNA | 3.83 | 0.05 | rebalance down |
| 2026-10-15T14:55 | ROC + volume | sell | SOL-USD | 3.88 | 0.03 | rebalance down |
| 2026-10-15T14:55 | ROC + volume | sell | ETH-USD | 3.81 | 0.01 | rebalance down |
| 2026-10-15T14:55 | ROC + volume | sell | BTC-USD | 3.80 | 0.01 | rebalance down |
| 2026-10-15T14:55 | EMA 20/50 cross | buy | XRP-USD | 8.77 | — | entry |
| 2026-10-15T14:55 | EMA 20/50 cross | sell | GOOGL | 9.29 | -0.05 | exit signal |
| 2026-10-15T14:50 | Agent (ML meta-label) | sell | TECL | 3.51 | -0.00 | selected signal exited |
| 2026-10-15T14:50 | Agent (ML meta-label) | sell | NVDA | 6.89 | -0.01 | selected signal exited |
| 2026-10-15T14:50 | VWAP reversion | buy | SQQQ | 14.61 | — | entry signal |
| 2026-10-15T14:50 | VWAP reversion | sell | DOGE-USD | 14.63 | 0.13 | exit signal |
| 2026-10-15T14:50 | RSI(14) reversion | sell | DOGE-USD | 4.70 | 0.02 | exit signal |
| 2026-10-15T14:50 | Keltner breakout | buy | LABU | 1.73 | — | entry |
| 2026-10-15T14:50 | Keltner breakout | buy | COIN | 6.22 | — | entry |
| 2026-10-15T14:50 | Keltner breakout | sell | GOOGL | 7.95 | -0.06 | exit signal |
| 2026-10-15T14:46 | AI bee: Bizzy | buy | SOXL | 7.18 | — | Jev: buy (buy p=0.56) |
| 2026-10-15T14:45 | Agent (ML meta-label) | buy | TQQQ | 6.91 | — | entry |
| 2026-10-15T14:45 | Agent (ML meta-label) | buy | TECL | 3.52 | — | entry |
| 2026-10-15T14:45 | Agent (ML meta-label) | buy | NVDA | 6.91 | — | following Ichimoku |
| 2026-10-15T14:45 | Keltner breakout · 1h | sell | SQQQ | 23.54 | 1.78 | stop-loss |
| 2026-10-15T14:45 | Bollinger breakout · 1h | sell | SQQQ | 24.01 | 1.62 | stop-loss |
| 2026-10-15T14:45 | ROC + volume · 1h | buy | LABU | 21.53 | — | entry |
| 2026-10-15T14:45 | Ichimoku | buy | XRP-USD | 13.29 | — | entry signal |
| 2026-10-15T14:45 | Ichimoku | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-15T14:45 | Ichimoku | buy | BTC-USD | 13.29 | — | entry signal |
| 2026-10-15T14:42 | AI bee: Bizzy | buy | TNA | 7.45 | — | Jev: buy (buy p=0.59) |
| 2026-10-15T14:42 | AI bee: Bizzy | buy | MSTR | 7.73 | — | Jev: buy (buy p=0.61) |
| 2026-10-15T14:42 | AI bee: Bizzy | buy | COIN | 7.15 | — | Jev: buy (buy p=0.56) |
| 2026-10-15T14:40 | Agent (ML meta-label) | sell | TQQQ | 7.19 | 0.01 | selected signal exited |
| 2026-10-15T14:40 | Agent (ML meta-label) | sell | NVDA | 7.17 | -0.00 | selected signal exited |
| 2026-10-15T14:40 | Keltner breakout | buy | XRP-USD | 7.88 | — | entry signal |
| 2026-10-15T14:40 | Donchian 55/20 | buy | SOL-USD | 10.46 | — | entry signal |
| 2026-10-15T14:40 | Donchian 55/20 | buy | ETH-USD | 10.47 | — | entry signal |
| 2026-10-15T14:40 | Donchian 55/20 | buy | BTC-USD | 10.47 | — | entry signal |
| 2026-10-15T14:40 | Donchian 55/20 | sell | TNA | 5.29 | -0.00 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 14:56:05.000142+00:00 -> 2026-10-15 15:06:05.000142+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
