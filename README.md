# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-16T10:55:05.000136+00:00 · 24697 ticks

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
| Copy: Insider buying | 2026-10-15 | GGR 12%, BORR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.89 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 8212 decisions in 1643 calls, $0.1150 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-16T10:55 | 2 / 2 / 1 | MSTR 15% |  |
| Breezy | 2026-10-16T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-16T10:55 | 2 / 3 / 0 | ETH-USD 29% |  |

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
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 104.57 | 4.57 | 1 | 100.0 | 5.79 | 1.45 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 103.58 | 3.58 | 0 | — | 4.58 | 2.20 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.71 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.02 | -3.27 | 18 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.73 | -7.55 | 43 |
| 8 | VWAP reversion · 1h | reversion | 99.71 | -0.29 | 58 | 39.7 | -11.10 | -3.14 | -13.79 | 127 |
| 9 | Hold SPY | benchmark | 99.67 | -0.33 | 0 | — | -0.55 | -0.27 | -3.26 | 1 |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.45 | -0.55 | 0 | — | 3.48 | 1.37 | -5.18 | 1 |
| 11 | Copy: Insider buying | copy | 99.02 | -0.98 | 20 | 45.0 | -11.57 | -1.93 | -20.62 | 75 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.71 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.29 | -1.71 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.64 | -2.36 | 0 | — | -5.22 | -2.88 | -6.38 | 1 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 16 | Hold BTC | benchmark | 97.46 | -2.54 | 0 | — | 30.04 | 3.43 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 97.23 | -2.77 | 0 | — | -4.87 | -1.92 | -7.50 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 96.94 | -3.06 | 36 | 16.7 | 7.64 | 1.04 | -22.11 | 108 |
| 19 | Trend pullback · 1h | trend | 96.48 | -3.52 | 86 | 24.4 | -22.58 | -6.44 | -23.29 | 154 |
| 20 | Three white soldiers · 1h | momentum | 96.19 | -3.81 | 11 | 0.0 | -4.10 | -3.09 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.05 | -3.95 | 106 | 32.1 | -13.59 | -4.48 | -14.77 | 291 |
| 22 | Daily: Momentum burst | daily | 95.54 | -4.46 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.07 | -4.93 | 75 | 20.0 | -11.04 | -2.01 | -15.34 | 259 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.40 | 1.16 | -9.46 | 99 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 93.59 | -6.41 | 0 | — | 4.68 | 0.85 | -13.89 | 1 |
| 26 | Parabolic SAR · 1h | trend | 93.41 | -6.59 | 93 | 22.6 | 3.19 | 0.58 | -22.05 | 277 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.31 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.06 | -6.94 | 0 | — | -16.05 | -3.04 | -19.22 | 1 |
| 29 | EMA 20/50 cross · 1h | trend | 92.97 | -7.03 | 51 | 15.7 | -6.36 | -0.68 | -23.77 | 132 |
| 30 | Daily: Bullish score | daily | 92.93 | -7.07 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.99 | -6.20 | -11.52 | 247 |
| 32 | MACD cross · 1h | trend | 92.60 | -7.40 | 155 | 21.9 | -12.10 | -1.59 | -26.23 | 455 |
| 33 | Bollinger breakout · 1h | breakout | 91.95 | -8.05 | 80 | 30.0 | 6.63 | 1.02 | -14.21 | 273 |
| 34 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.20 | -17.60 | 567 |
| 35 | Max aggression: 5-day momentum | meta | 91.73 | -8.27 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.80 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.26 | -8.74 | 74 | 13.5 | -1.58 | 0.03 | -28.77 | 214 |
| 38 | RSI momentum · 1h | momentum | 91.22 | -8.78 | 73 | 17.8 | 0.39 | 0.26 | -26.67 | 222 |
| 39 | Stochastic reversion · 1h | reversion | 90.85 | -9.15 | 128 | 44.5 | -15.85 | -2.95 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.39 | -22.64 | 118 |
| 41 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -8.18 | -3.01 | -9.08 | 123 |
| 42 | Triple EMA stack · 1h | trend | 90.01 | -9.99 | 77 | 16.9 | -7.55 | -0.58 | -32.08 | 235 |
| 43 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.88 | -25.00 | 239 |
| 44 | MFI reversion · 1h | reversion | 89.58 | -10.42 | 195 | 31.3 | -16.46 | -2.82 | -19.82 | 140 |
| 45 | Max aggression: 1-day momentum | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.72 | -37.31 | 43 |
| 46 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -13.89 | -1.90 | -29.15 | 211 |
| 47 | Z-score reversion · 1h | reversion | 88.11 | -11.89 | 74 | 36.5 | -10.17 | -1.82 | -17.27 | 178 |
| 48 | OBV trend · 1h | momentum | 87.70 | -12.30 | 165 | 18.8 | -10.71 | -0.90 | -34.78 | 317 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.32 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 86.94 | -13.06 | 568 | 18.5 | -2.08 | -0.19 | -15.13 | 399 |
| 51 | MACD zero-line · 1h | trend | 86.69 | -13.31 | 75 | 16.0 | -21.30 | -4.08 | -22.72 | 226 |
| 52 | VWAP momentum · 1h | momentum | 86.02 | -13.98 | 361 | 21.9 | -34.10 | -4.89 | -43.06 | 1257 |
| 53 | Heikin-Ashi · 1h | trend | 85.84 | -14.16 | 175 | 25.7 | -29.82 | -4.77 | -39.15 | 672 |
| 54 | Donchian 20/10 · 1h | breakout | 85.65 | -14.35 | 72 | 19.4 | -0.03 | 0.20 | -20.97 | 220 |
| 55 | ROC + volume · 1h | momentum | 85.52 | -14.48 | 184 | 22.3 | -9.10 | -1.11 | -25.32 | 398 |
| 56 | Three white soldiers | momentum | 85.20 | -14.80 | 204 | 19.1 | -47.78 | -19.37 | -48.69 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 84.66 | -15.34 | 132 | 31.8 | -26.66 | -5.70 | -31.47 | 338 |
| 58 | EMA 9/21 cross · 1h | trend | 84.49 | -15.51 | 120 | 12.5 | -5.30 | -0.40 | -29.27 | 322 |
| 59 | Williams %R · 1h | reversion | 83.67 | -16.33 | 168 | 42.9 | -31.21 | -5.06 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.08 | -16.92 | 62 | 24.2 | -12.64 | -2.35 | -18.95 | 175 |
| 61 | CCI reversion · 1h | reversion | 83.05 | -16.95 | 143 | 42.7 | -15.10 | -1.93 | -23.38 | 428 |
| 62 | Candlestick reversal · 1h | reversion | 79.93 | -20.07 | 186 | 26.3 | -32.52 | -6.06 | -33.95 | 524 |
| 63 | RSI(14) reversion | reversion | 66.20 | -33.80 | 580 | 28.4 | -73.20 | -16.00 | -73.93 | 1558 |
| 64 | ROC + volume | momentum | 65.30 | -34.70 | 532 | 22.4 | -75.08 | -16.79 | -76.71 | 1705 |
| 65 | Volume breakout | breakout | 64.41 | -35.59 | 319 | 13.5 | -63.46 | -17.70 | -63.46 | 884 |
| 66 | Squeeze breakout | breakout | 63.76 | -36.24 | 425 | 14.8 | -62.97 | -17.40 | -63.66 | 1216 |
| 67 | Donchian 55/20 | breakout | 61.61 | -38.39 | 428 | 18.0 | -69.31 | -14.26 | -71.45 | 1283 |
| 68 | EMA 20/50 cross | trend | 60.54 | -39.46 | 442 | 19.7 | -77.29 | -14.87 | -78.71 | 1448 |
| 69 | AI bee: Boozy | ai | 58.00 | -42.01 | 285 | 5.3 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.71 | -42.29 | 592 | 24.3 | -72.57 | -14.81 | -72.60 | 1429 |
| 71 | Keltner breakout | breakout | 55.31 | -44.69 | 598 | 16.2 | -83.69 | -25.83 | -83.69 | 1853 |
| 72 | Supertrend | trend | 53.06 | -46.94 | 622 | 20.1 | -86.37 | -19.83 | -86.56 | 1915 |
| 73 | Ichimoku | trend | 52.44 | -47.56 | 541 | 11.8 | -82.02 | -22.14 | -82.02 | 1728 |
| 74 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -28.49 | -98.63 | 5296 |
| 75 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -28.61 | -93.51 | 2594 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.61 | -23.85 | -90.62 | 2367 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.74 | -26.05 | -91.75 | 2337 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.47 | -30.78 | -97.47 | 3526 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.71 | -34.16 | -96.71 | 3607 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -24.72 | -94.45 | 2634 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -33.33 | -99.37 | 5703 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.38 | -24.90 | -91.38 | 2647 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.27 | -29.93 | -96.27 | 3559 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -38.19 | -99.73 | 6162 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.75 | -28.03 | -91.75 | 2366 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -35.66 | -97.47 | 3655 |
| 87 | AI bee: Bizzy | ai | 50.02 | -49.98 | 1065 | 8.9 | — | — | — | — |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.44 | -33.89 | -98.45 | 4682 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.70 | -31.32 | -93.70 | 2804 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -36.30 | -99.53 | 6165 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -85.93 | -21.24 | -86.09 | 2102 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.50 | -25.55 | -87.62 | 2110 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -30.45 | -95.92 | 3758 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -31.66 | -89.27 | 2101 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.69 | -31.57 | -95.70 | 4071 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -41.78 | -99.89 | 8232 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-16T10:55 | EMA 20/50 cross | buy | XRP-USD | 15.15 | — | entry signal |
| 2026-10-16T10:53 | AI bee: Bizzy | sell | XRP-USD | 7.38 | -0.04 | Jev: sell (sell p=0.56) after 12 min |
| 2026-10-16T10:53 | AI bee: Bizzy | sell | ETH-USD | 6.93 | -0.04 | Jev: sell (sell p=0.55) after 11 min |
| 2026-10-16T10:50 | AI bee: Bizzy | sell | SOL-USD | 7.46 | -0.02 | Jev: sell (sell p=0.58) after 17 min |
| 2026-10-16T10:45 | VWAP reversion | sell | BTC-USD | 14.40 | -0.04 | exit signal |
| 2026-10-16T10:45 | RSI(14) reversion | sell | SOL-USD | 16.56 | 0.01 | take-profit |
| 2026-10-16T10:45 | RSI(14) reversion | sell | BTC-USD | 16.52 | -0.04 | take-profit |
| 2026-10-16T10:45 | Keltner breakout | buy | ETH-USD | 13.84 | — | entry signal |
| 2026-10-16T10:45 | Donchian 55/20 | buy | ETH-USD | 15.41 | — | entry signal |
| 2026-10-16T10:45 | Supertrend | buy | SOL-USD | 2.70 | — | entry signal |
| 2026-10-16T10:45 | Supertrend | sell | ETH-USD | 2.65 | -0.01 | rebalance down |
| 2026-10-16T10:45 | EMA 20/50 cross | buy | SOL-USD | 15.16 | — | entry signal |
| 2026-10-16T10:42 | AI bee: Bizzy | buy | ETH-USD | 6.98 | — | Jev: buy (buy p=0.56) |
| 2026-10-16T10:41 | AI bee: Boozy | buy | ETH-USD | 16.56 | — | Jev: buy (buy p=0.74) |
| 2026-10-16T10:41 | AI bee: Bizzy | buy | XRP-USD | 7.43 | — | Jev: buy (buy p=0.59) |
| 2026-10-16T10:40 | RSI(14) reversion | sell | XRP-USD | 16.54 | -0.03 | exit signal |
| 2026-10-16T10:40 | Supertrend | buy | XRP-USD | 13.27 | — | entry signal |
| 2026-10-16T10:40 | Supertrend | buy | DOGE-USD | 13.27 | — | entry |
| 2026-10-16T10:35 | Supertrend | buy | ETH-USD | 13.29 | — | entry signal |
| 2026-10-16T10:35 | Supertrend | buy | BTC-USD | 13.29 | — | entry signal |
| 2026-10-16T10:33 | AI bee: Bizzy | buy | SOL-USD | 7.48 | — | Jev: buy (buy p=0.60) |
| 2026-10-16T10:20 | RSI(14) reversion | buy | SOL-USD | 16.55 | — | entry signal |
| 2026-10-16T10:15 | VWAP reversion | buy | BTC-USD | 14.44 | — | entry signal |
| 2026-10-16T10:15 | RSI(14) reversion | buy | XRP-USD | 16.57 | — | entry signal |
| 2026-10-16T10:15 | RSI(14) reversion | buy | BTC-USD | 16.57 | — | entry signal |
| 2026-10-16T10:10 | Supertrend | sell | DOGE-USD | 10.63 | -0.08 | exit signal |
| 2026-10-16T10:10 | EMA 20/50 cross | sell | XRP-USD | 15.10 | -0.20 | stop-loss |
| 2026-10-16T10:05 | Donchian 55/20 | sell | SOL-USD | 15.28 | -0.23 | stop-loss |
| 2026-10-16T10:05 | Donchian 55/20 | sell | ETH-USD | 15.38 | -0.20 | stop-loss |
| 2026-10-16T10:05 | Ichimoku | sell | DOGE-USD | 13.03 | -0.14 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | XRP-USD | 13.29 | -0.14 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | SOL-USD | 10.65 | -0.06 | exit signal |
| 2026-10-16T10:05 | Supertrend | sell | ETH-USD | 13.31 | -0.09 | exit signal |
| 2026-10-16T10:00 | Candlestick reversal · 1h | sell | ETH-USD | 2.79 | 0.03 | exit signal |
| 2026-10-16T10:00 | Bollinger breakout · 1h | sell | BTC-USD | 22.72 | -0.38 | exit signal |
| 2026-10-16T10:00 | VWAP momentum · 1h | sell | BTC-USD | 3.28 | -0.03 | exit signal |
| 2026-10-16T10:00 | MACD zero-line · 1h | buy | XRP-USD | 4.15 | — | entry |
| 2026-10-16T10:00 | MACD zero-line · 1h | buy | DOGE-USD | 17.33 | — | rebalance up |
| 2026-10-16T10:00 | MACD zero-line · 1h | sell | BTC-USD | 21.48 | -0.32 | exit signal |
| 2026-10-16T10:00 | MACD cross · 1h | sell | BTC-USD | 7.62 | -0.07 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-18 10:55:05.000136+00:00 -> 2026-10-16 11:05:05.000136+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
