# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T15:25:05.000168+00:00 · 23750 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.02 (-6.98%)

Closed trades 72, win rate 41.7%, fees £2.57, max drawdown -7.41%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 18.54 | -0.08 |

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

Today: 18288 decisions in 2280 calls, $0.2372 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T15:25 | 1 / 23 / 6 | MSTR 16%, ETHU 14% |  |
| Breezy | 2026-10-15T15:25 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-15T15:25 | 4 / 25 / 1 | MSTR 68% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.51 | 4.51 | 0 | — | 4.27 | 2.04 | -5.18 | 1 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.21 | 4.21 | 1 | 100.0 | 4.88 | 1.29 | -7.93 | 9 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.37 | 1.95 | -3.27 | 19 |
| 4 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.42 | -0.73 | -9.61 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.45 | 0.45 | 0 | — | 4.04 | 1.59 | -5.18 | 1 |
| 6 | Hold SPY | benchmark | 100.06 | 0.06 | 0 | — | -0.83 | -0.44 | -3.40 | 1 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Copy: Insider buying | copy | 99.97 | -0.03 | 20 | 45.0 | -16.10 | -2.56 | -21.97 | 76 |
| 10 | VWAP reversion · 1h | reversion | 99.95 | -0.05 | 57 | 38.6 | -9.89 | -2.92 | -13.79 | 119 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.17 | -1.83 | 0 | — | -1.48 | -0.59 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 98.15 | -1.85 | 0 | — | 30.06 | 3.46 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.70 | -2.30 | 0 | — | -5.11 | -2.80 | -6.38 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Donchian 55/20 · 1h | breakout | 97.37 | -2.63 | 36 | 16.7 | 6.83 | 0.96 | -22.11 | 112 |
| 18 | Trend pullback · 1h | trend | 96.88 | -3.12 | 86 | 24.4 | -24.25 | -7.10 | -25.21 | 165 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 96.67 | -3.33 | 0 | — | -6.15 | -2.39 | -7.50 | 1 |
| 20 | Three white soldiers · 1h | momentum | 96.28 | -3.72 | 11 | 0.0 | -4.12 | -3.13 | -5.30 | 30 |
| 21 | ADX DI cross · 1h | trend | 96.26 | -3.74 | 70 | 21.4 | -9.81 | -1.76 | -14.76 | 253 |
| 22 | Daily: Momentum burst | daily | 95.94 | -4.06 | 5 | 20.0 | -4.75 | -0.57 | -17.67 | 39 |
| 23 | Agent (rotation) | meta | 95.89 | -4.11 | 104 | 30.8 | -13.40 | -4.60 | -14.67 | 278 |
| 24 | Parabolic SAR · 1h | trend | 93.80 | -6.20 | 93 | 22.6 | 2.53 | 0.50 | -22.50 | 283 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.91 | 1.06 | -9.46 | 102 |
| 26 | Gap and go | momentum | 93.54 | -6.46 | 65 | 12.3 | 9.14 | 2.30 | -6.78 | 202 |
| 27 | EMA 20/50 cross · 1h | trend | 93.50 | -6.50 | 51 | 15.7 | 5.73 | 0.82 | -23.13 | 134 |
| 28 | Max aggression: 5-day momentum | meta | 93.34 | -6.66 | 8 | 37.5 | -6.29 | -0.26 | -34.64 | 26 |
| 29 | Daily: Bullish score | daily | 93.11 | -6.89 | 7 | 0.0 | -4.34 | -0.36 | -12.76 | 13 |
| 30 | Agent | meta | 93.02 | -6.98 | 72 | 41.7 | -6.67 | -2.97 | -8.22 | 230 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 92.74 | -7.25 | 0 | — | 3.87 | 0.74 | -13.89 | 1 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 92.74 | -7.26 | 0 | — | -15.76 | -2.97 | -19.22 | 1 |
| 33 | Bollinger breakout · 1h | breakout | 92.41 | -7.59 | 79 | 30.4 | 8.54 | 1.24 | -14.21 | 276 |
| 34 | MACD cross · 1h | trend | 92.38 | -7.62 | 154 | 22.1 | -12.70 | -1.73 | -22.49 | 466 |
| 35 | Supertrend · 1h | trend | 92.00 | -8.00 | 73 | 13.7 | 1.83 | 0.42 | -22.72 | 208 |
| 36 | RSI momentum · 1h | momentum | 92.00 | -8.00 | 73 | 17.8 | 1.98 | 0.43 | -25.29 | 223 |
| 37 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | 6.91 | 1.11 | -12.60 | 120 |
| 38 | Opening range 30m | breakout | 90.77 | -9.23 | 169 | 23.1 | -12.54 | -3.59 | -17.60 | 567 |
| 39 | Triple EMA stack · 1h | trend | 90.58 | -9.42 | 77 | 16.9 | -6.23 | -0.45 | -31.79 | 225 |
| 40 | Stochastic reversion · 1h | reversion | 90.49 | -9.52 | 127 | 44.1 | -17.80 | -3.31 | -20.56 | 353 |
| 41 | Ichimoku · 1h | trend | 90.42 | -9.58 | 51 | 15.7 | 0.92 | 0.31 | -22.64 | 123 |
| 42 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -12.34 | -3.96 | -13.56 | 128 |
| 43 | Connors RSI(2) · 1h | reversion | 89.54 | -10.46 | 141 | 39.7 | -23.33 | -6.98 | -24.89 | 248 |
| 44 | MFI reversion · 1h | reversion | 89.46 | -10.54 | 183 | 29.0 | -17.69 | -3.06 | -20.14 | 140 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -17.66 | -0.67 | -37.31 | 43 |
| 46 | OBV trend · 1h | momentum | 88.33 | -11.67 | 164 | 18.9 | -11.11 | -0.96 | -35.24 | 319 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -5.02 | -0.42 | -26.68 | 211 |
| 48 | Z-score reversion · 1h | reversion | 87.68 | -12.32 | 70 | 32.9 | -11.14 | -1.98 | -17.27 | 172 |
| 49 | MACD zero-line · 1h | trend | 87.61 | -12.39 | 74 | 16.2 | -21.97 | -4.20 | -22.79 | 225 |
| 50 | Agent (ML meta-label) | meta | 86.95 | -13.05 | 568 | 18.5 | -6.04 | -0.90 | -15.41 | 411 |
| 51 | Opening range 15m | breakout | 86.49 | -13.51 | 216 | 20.4 | -17.85 | -4.76 | -21.40 | 707 |
| 52 | Donchian 20/10 · 1h | breakout | 86.47 | -13.53 | 72 | 19.4 | -0.72 | 0.11 | -20.38 | 216 |
| 53 | ROC + volume · 1h | momentum | 86.31 | -13.69 | 180 | 21.7 | -10.18 | -1.34 | -25.31 | 398 |
| 54 | VWAP momentum · 1h | momentum | 86.07 | -13.93 | 353 | 21.8 | -35.97 | -5.36 | -43.13 | 1244 |
| 55 | Heikin-Ashi · 1h | trend | 85.92 | -14.08 | 169 | 26.0 | -30.38 | -4.93 | -39.15 | 659 |
| 56 | Three white soldiers | momentum | 85.85 | -14.15 | 189 | 16.4 | -47.40 | -18.61 | -48.93 | 599 |
| 57 | EMA 9/21 cross · 1h | trend | 85.06 | -14.94 | 120 | 12.5 | -10.17 | -1.16 | -28.05 | 321 |
| 58 | Bollinger reversion · 1h | reversion | 83.77 | -16.23 | 130 | 30.8 | -27.19 | -5.80 | -31.47 | 332 |
| 59 | Williams %R · 1h | reversion | 83.13 | -16.87 | 163 | 41.7 | -32.32 | -5.33 | -34.92 | 518 |
| 60 | CCI reversion · 1h | reversion | 82.78 | -17.22 | 137 | 40.1 | -18.02 | -2.37 | -23.38 | 424 |
| 61 | RSI(14) reversion · 1h | reversion | 82.77 | -17.23 | 60 | 21.7 | -13.72 | -2.37 | -18.95 | 162 |
| 62 | Candlestick reversal · 1h | reversion | 80.02 | -19.98 | 180 | 25.0 | -33.07 | -6.15 | -34.27 | 521 |
| 63 | ROC + volume | momentum | 67.50 | -32.50 | 492 | 21.5 | -74.02 | -16.31 | -76.54 | 1684 |
| 64 | RSI(14) reversion | reversion | 66.45 | -33.55 | 567 | 28.4 | -73.29 | -16.27 | -74.13 | 1562 |
| 65 | Volume breakout | breakout | 65.24 | -34.76 | 310 | 13.5 | -63.28 | -17.82 | -63.32 | 888 |
| 66 | Squeeze breakout | breakout | 64.69 | -35.31 | 404 | 14.6 | -62.61 | -17.31 | -63.39 | 1211 |
| 67 | Donchian 55/20 | breakout | 63.45 | -36.55 | 400 | 16.8 | -68.55 | -14.10 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.73 | -38.27 | 421 | 18.8 | -77.24 | -14.98 | -78.49 | 1443 |
| 69 | VWAP reversion | reversion | 58.20 | -41.80 | 581 | 24.6 | -72.55 | -15.04 | -72.72 | 1423 |
| 70 | AI bee: Boozy | ai | 57.66 | -42.34 | 277 | 5.1 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.49 | -43.51 | 559 | 14.1 | -83.19 | -25.77 | -83.50 | 1841 |
| 72 | Supertrend | trend | 54.65 | -45.35 | 581 | 18.6 | -86.31 | -19.87 | -86.64 | 1908 |
| 73 | Ichimoku | trend | 53.69 | -46.30 | 493 | 9.7 | -81.89 | -22.20 | -82.11 | 1702 |
| 74 | AI bee: Bizzy | ai | 51.17 | -48.83 | 1015 | 8.3 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -28.92 | -98.64 | 5358 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -28.61 | -93.51 | 2567 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -23.97 | -90.72 | 2355 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.48 | -25.90 | -91.51 | 2319 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -31.45 | -97.49 | 3509 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -33.85 | -96.56 | 3571 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.30 | -24.55 | -94.33 | 2602 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -35.20 | -99.41 | 5746 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.07 | -24.86 | -91.21 | 2628 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.18 | -29.94 | -96.18 | 3542 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.42 | -99.73 | 6166 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.78 | -28.46 | -91.94 | 2360 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.41 | -36.00 | -97.46 | 3636 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -35.59 | -98.55 | 4693 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.40 | -30.96 | -93.54 | 2777 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.83 | -99.56 | 6164 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.18 | -21.88 | -86.50 | 2120 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.78 | -26.48 | -88.08 | 2131 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.05 | -31.89 | -96.13 | 3783 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -32.58 | -89.48 | 2110 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -32.91 | -95.92 | 4071 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.48 | -99.89 | 8200 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T15:25 | RSI(14) reversion | sell | META | 16.66 | 0.04 | exit signal |
| 2026-10-15T15:25 | Three white soldiers | buy | DOGE-USD | 4.81 | — | rebalance up |
| 2026-10-15T15:25 | Three white soldiers | sell | TNA | 12.04 | 0.05 | exit signal |
| 2026-10-15T15:24 | AI bee: Bizzy | sell | LABU | 7.02 | -0.02 | Jev: sell (sell p=0.62) after 21 min |
| 2026-10-15T15:22 | AI bee: Bizzy | sell | TNA | 7.46 | 0.01 | Jev: sell (sell p=0.51) after 40 min |
| 2026-10-15T15:20 | Agent (ML meta-label) | buy | TECL | 4.07 | — | entry |
| 2026-10-15T15:20 | Agent (ML meta-label) | buy | SPY | 4.58 | — | entry |
| 2026-10-15T15:20 | Agent (ML meta-label) | buy | NVDA | 4.58 | — | following Ichimoku |
| 2026-10-15T15:20 | Agent (ML meta-label) | sell | ETHU | 1.67 | -0.00 | selected signal exited |
| 2026-10-15T15:20 | Agent (ML meta-label) | sell | COIN | 3.56 | 0.02 | selected signal exited |
| 2026-10-15T15:20 | Agent (ML meta-label) | sell | AMZN | 3.64 | 0.01 | selected signal exited |
| 2026-10-15T15:20 | Agent (ML meta-label) | sell | AMD | 3.65 | 0.02 | selected signal exited |
| 2026-10-15T15:20 | RSI(14) reversion | buy | TECL | 5.53 | — | rebalance up |
| 2026-10-15T15:20 | RSI(14) reversion | buy | NVDA | 5.57 | — | rebalance up |
| 2026-10-15T15:20 | RSI(14) reversion | buy | META | 5.58 | — | rebalance up |
| 2026-10-15T15:20 | RSI(14) reversion | buy | AMD | 5.52 | — | rebalance up |
| 2026-10-15T15:20 | RSI(14) reversion | sell | SOXL | 11.14 | 0.36 | exit signal |
| 2026-10-15T15:20 | Opening range 15m | buy | NVDA | 4.15 | — | entry |
| 2026-10-15T15:20 | Opening range 15m | buy | AMD | 4.56 | — | entry signal |
| 2026-10-15T15:20 | Opening range 15m | sell | MSTR | 4.34 | 0.20 | rebalance down |
| 2026-10-15T15:20 | Opening range 15m | sell | ETHU | 4.37 | 0.21 | rebalance down |
| 2026-10-15T15:16 | Three white soldiers | sell | ETHU | 2.43 | -0.00 | target is flat |
| 2026-10-15T15:16 | Volume breakout | buy | QQQ | 16.31 | — | entry signal |
| 2026-10-15T15:16 | EMA 20/50 cross | buy | MSTR | 5.10 | — | entry signal |
| 2026-10-15T15:16 | EMA 20/50 cross | buy | MSFT | 5.15 | — | entry |
| 2026-10-15T15:16 | EMA 20/50 cross | buy | GOOGL | 5.15 | — | entry |
| 2026-10-15T15:16 | EMA 20/50 cross | buy | COIN | 5.15 | — | entry |
| 2026-10-15T15:16 | EMA 20/50 cross | buy | BITX | 5.15 | — | entry signal |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | XRP-USD | 3.68 | 0.02 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | TNA | 3.67 | 0.03 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | SOL-USD | 3.75 | 0.07 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | LABU | 3.70 | 0.11 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | IWM | 3.62 | 0.01 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | ETH-USD | 3.12 | 0.03 | rebalance down |
| 2026-10-15T15:16 | EMA 20/50 cross | sell | BTC-USD | 3.65 | 0.01 | rebalance down |
| 2026-10-15T15:10 | Agent (ML meta-label) | buy | META | 3.62 | — | following ROC + volume, Squeeze breakout |
| 2026-10-15T15:10 | Agent (ML meta-label) | sell | DOGE-USD | 4.33 | 0.05 | rebalance down |
| 2026-10-15T15:10 | RSI(14) reversion | sell | TSLA | 11.06 | 0.07 | take-profit |
| 2026-10-15T15:10 | Squeeze breakout | buy | MSFT | 16.18 | — | entry signal |
| 2026-10-15T15:10 | Ichimoku | buy | MSFT | 5.36 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 15:25:05.000168+00:00 -> 2026-10-15 15:35:05.000168+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
