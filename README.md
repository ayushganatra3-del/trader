# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T20:25:05.000167+00:00 · 23976 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.85 (-7.14%)

Closed trades 76, win rate 39.5%, fees £2.65, max drawdown -7.57%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 36957 decisions in 2958 calls, $0.4561 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T20:25 | 0 / 3 / 2 | ETH-USD 15%, MSTR 14% |  |
| Breezy | 2026-10-15T20:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T20:25 | 2 / 3 / 0 | ETH-USD 30% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| VWAP reversion | PLTR | 1.50 | +3.07% | 7 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.05 | 5.05 | 1 | 100.0 | 5.80 | 1.46 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.05 | 4.05 | 0 | — | 4.58 | 2.21 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.72 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.04 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.13 | 0.12 | 0 | — | -0.54 | -0.27 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.90 | -0.10 | 0 | — | 3.48 | 1.38 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 58 | 39.7 | -10.94 | -3.13 | -13.79 | 128 |
| 11 | Copy: Insider buying | copy | 99.41 | -0.59 | 20 | 45.0 | -16.49 | -2.63 | -21.97 | 76 |
| 12 | Copy: Congress Democrats (NANC) | copy | 98.84 | -1.16 | 0 | — | -0.59 | -0.20 | -4.45 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 14 | Hold BTC | benchmark | 98.12 | -1.88 | 0 | — | 30.59 | 3.51 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.86 | -2.14 | 0 | — | -5.22 | -2.90 | -6.38 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.03 | 0.87 | -22.11 | 113 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 97.02 | -2.98 | 0 | — | -5.50 | -2.16 | -7.50 | 1 |
| 19 | Trend pullback · 1h | trend | 96.69 | -3.31 | 86 | 24.4 | -21.45 | -6.01 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.30 | -3.70 | 11 | 0.0 | -4.10 | -3.12 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -15.89 | -5.52 | -17.79 | 295 |
| 22 | ADX DI cross · 1h | trend | 95.85 | -4.15 | 70 | 21.4 | -10.91 | -1.99 | -15.34 | 258 |
| 23 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.01 | -5.99 | 0 | — | 4.68 | 0.86 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.54 | 1.00 | -9.46 | 103 |
| 26 | Parabolic SAR · 1h | trend | 93.62 | -6.38 | 93 | 22.6 | 3.02 | 0.56 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.33 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.28 | -6.72 | 0 | — | -16.05 | -3.06 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.27 | -6.73 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.19 | -6.81 | 51 | 15.7 | 4.52 | 0.70 | -24.30 | 134 |
| 31 | MACD cross · 1h | trend | 92.95 | -7.05 | 154 | 22.1 | -13.24 | -1.78 | -26.23 | 460 |
| 32 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.81 | -6.21 | -11.32 | 244 |
| 33 | Bollinger breakout · 1h | breakout | 92.16 | -7.84 | 79 | 30.4 | 6.63 | 1.03 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 92.14 | -7.86 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.76 | -3.22 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.61 | -8.39 | 74 | 13.5 | -1.59 | 0.03 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.48 | -8.52 | 73 | 17.8 | 0.06 | 0.22 | -26.36 | 224 |
| 39 | Stochastic reversion · 1h | reversion | 91.26 | -8.74 | 128 | 44.5 | -15.86 | -2.97 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.20 | -9.80 | 77 | 16.9 | -7.13 | -0.53 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -5.96 | -2.16 | -7.37 | 120 |
| 43 | MFI reversion · 1h | reversion | 90.05 | -9.95 | 191 | 30.4 | -17.51 | -3.02 | -20.79 | 145 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.93 | -25.00 | 244 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.73 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.49 | -11.51 | 73 | 35.6 | -10.26 | -1.85 | -17.27 | 183 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.93 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.91 | -12.09 | 165 | 18.8 | -10.52 | -0.89 | -34.81 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.35 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.28 | -12.72 | 568 | 18.5 | -3.95 | -0.49 | -15.48 | 413 |
| 51 | MACD zero-line · 1h | trend | 87.16 | -12.84 | 74 | 16.2 | -22.04 | -4.28 | -22.42 | 229 |
| 52 | VWAP momentum · 1h | momentum | 86.56 | -13.44 | 354 | 21.8 | -34.44 | -4.99 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.42 | -13.58 | 170 | 26.5 | -29.90 | -4.81 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 86.23 | -13.77 | 180 | 21.7 | -8.52 | -1.03 | -25.31 | 399 |
| 55 | Donchian 20/10 · 1h | breakout | 86.08 | -13.92 | 72 | 19.4 | -0.03 | 0.20 | -20.56 | 219 |
| 56 | Three white soldiers | momentum | 85.86 | -14.14 | 200 | 19.5 | -47.54 | -19.02 | -48.85 | 607 |
| 57 | Bollinger reversion · 1h | reversion | 85.04 | -14.96 | 132 | 31.8 | -26.96 | -5.83 | -31.47 | 340 |
| 58 | EMA 9/21 cross · 1h | trend | 84.78 | -15.22 | 120 | 12.5 | -5.45 | -0.42 | -29.09 | 321 |
| 59 | Williams %R · 1h | reversion | 84.04 | -15.96 | 168 | 42.9 | -31.29 | -5.12 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.43 | -16.57 | 61 | 23.0 | -12.34 | -2.31 | -18.95 | 171 |
| 61 | CCI reversion · 1h | reversion | 83.40 | -16.60 | 143 | 42.7 | -15.30 | -1.97 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 80.34 | -19.66 | 183 | 25.7 | -32.18 | -6.04 | -33.69 | 523 |
| 63 | RSI(14) reversion | reversion | 66.62 | -33.38 | 572 | 28.7 | -73.30 | -16.22 | -74.18 | 1558 |
| 64 | ROC + volume | momentum | 66.23 | -33.77 | 526 | 22.6 | -74.76 | -16.96 | -76.52 | 1701 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.43 | -17.89 | -63.43 | 891 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.96 | -17.56 | -63.44 | 1218 |
| 67 | Donchian 55/20 | breakout | 63.56 | -36.44 | 416 | 18.3 | -68.82 | -14.10 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 62.12 | -37.88 | 431 | 19.7 | -76.93 | -14.81 | -78.49 | 1445 |
| 69 | AI bee: Boozy | ai | 58.81 | -41.19 | 278 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.49 | -14.97 | -72.55 | 1430 |
| 71 | Keltner breakout | breakout | 56.46 | -43.55 | 589 | 16.5 | -83.52 | -25.86 | -83.75 | 1852 |
| 72 | Supertrend | trend | 54.80 | -45.20 | 607 | 20.4 | -86.23 | -19.81 | -86.54 | 1914 |
| 73 | Ichimoku | trend | 53.56 | -46.44 | 528 | 11.9 | -81.91 | -22.28 | -82.04 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.44 | -48.56 | 1033 | 9.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.58 | -28.77 | -98.62 | 5294 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.36 | -28.46 | -93.47 | 2585 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -23.82 | -90.71 | 2366 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.49 | -25.99 | -91.54 | 2323 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.41 | -31.10 | -97.45 | 3517 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.55 | -34.01 | -96.57 | 3579 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -24.52 | -94.46 | 2641 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -34.48 | -99.39 | 5712 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.19 | -24.95 | -91.25 | 2641 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.19 | -30.29 | -96.19 | 3543 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.71 | -99.73 | 6152 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.70 | -28.30 | -91.79 | 2365 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.45 | -36.09 | -97.45 | 3654 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -34.90 | -98.51 | 4677 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.54 | -31.41 | -93.57 | 2797 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.39 | -99.55 | 6167 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.05 | -21.71 | -86.36 | 2103 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.43 | -26.17 | -87.79 | 2101 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -31.32 | -96.04 | 3757 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.30 | -32.29 | -89.45 | 2106 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.71 | -32.34 | -95.82 | 4069 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.32 | -99.89 | 8224 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T20:20 | AI bee: Boozy | buy | ETH-USD | 17.40 | — | Jev: buy (buy p=0.71) |
| 2026-10-15T20:20 | AI bee: Bizzy | buy | ETH-USD | 7.94 | — | Jev: buy (buy p=0.62) |
| 2026-10-15T20:15 | Squeeze breakout | sell | DOGE-USD | 16.01 | -0.13 | exit signal |
| 2026-10-15T20:15 | Ichimoku | sell | XRP-USD | 13.33 | -0.11 | exit signal |
| 2026-10-15T20:15 | Ichimoku | sell | BTC-USD | 13.36 | -0.10 | stop-loss |
| 2026-10-15T20:05 | ROC + volume | sell | XRP-USD | 16.52 | -0.10 | exit signal |
| 2026-10-15T20:05 | ROC + volume | sell | DOGE-USD | 16.53 | -0.10 | exit signal |
| 2026-10-15T20:00 | CCI reversion · 1h | sell | DOGE-USD | 4.62 | 0.11 | exit signal |
| 2026-10-15T20:00 | MACD zero-line · 1h | buy | ETH-USD | 19.21 | — | entry signal |
| 2026-10-15T20:00 | MACD zero-line · 1h | buy | BTC-USD | 21.80 | — | entry signal |
| 2026-10-15T19:59 | AI bee: Bizzy | buy | MSTR | 7.46 | — | Jev: buy (buy p=0.58) |
| 2026-10-15T19:55 | Agent (rotation) | sell | TQQQ | 32.20 | 0.24 | selected signal exited |
| 2026-10-15T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 103.54 | 0.77 | target is flat |
| 2026-10-15T19:55 | MFI reversion · 1h | buy | PLTR | 1.99 | — | entry |
| 2026-10-15T19:55 | VWAP reversion | sell | SQQQ | 14.47 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | VWAP reversion | sell | AAPL | 14.59 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | SQQQ | 16.62 | -0.06 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | AAPL | 16.66 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TQQQ | 21.53 | 0.13 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TNA | 21.54 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TECL | 21.37 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | QQQ | 21.42 | 0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Volume breakout | sell | TNA | 16.19 | -0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | TSLA | 16.18 | 0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | PLTR | 16.12 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | AMD | 13.13 | 0.21 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | buy | ETH-USD | 14.13 | — | entry |
| 2026-10-15T19:55 | Keltner breakout | sell | UPRO | 5.10 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TQQQ | 5.13 | 0.04 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TNA | 5.15 | 0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | TECL | 5.16 | 0.06 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | SPY | 5.10 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | SOXL | 5.22 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | QQQ | 5.11 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | IWM | 5.11 | 0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | COIN | 5.17 | 0.06 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | AMZN | 5.10 | -0.01 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | sell | AMD | 5.12 | 0.03 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | UPRO | 5.35 | 0.04 | end-of-day flatten |
| 2026-10-15T19:55 | Opening range 30m | sell | TSLA | 5.33 | 0.02 | end-of-day flatten |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 20:25:05.000167+00:00 -> 2026-10-15 20:35:05.000167+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
