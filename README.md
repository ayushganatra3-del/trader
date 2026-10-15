# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T23:55:05.000183+00:00 · 24146 ticks

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

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.46 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 39507 decisions in 3468 calls, $0.4918 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T23:55 | 0 / 4 / 1 | DOGE-USD 15%, MSTR 15% |  |
| Breezy | 2026-10-15T23:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T23:55 | 2 / 3 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.01 | 5.01 | 1 | 100.0 | 5.79 | 1.46 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.02 | 4.02 | 0 | — | 4.58 | 2.21 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.72 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.04 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.10 | 0.10 | 0 | — | -0.55 | -0.28 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.87 | -0.13 | 0 | — | 3.48 | 1.38 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.81 | -0.19 | 58 | 39.7 | -11.10 | -3.16 | -13.79 | 127 |
| 11 | Copy: Insider buying | copy | 99.39 | -0.61 | 20 | 45.0 | -16.49 | -2.63 | -21.97 | 76 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.71 | -1.29 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 97.94 | -2.06 | 0 | — | 30.11 | 3.46 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.85 | -2.15 | 0 | — | -5.22 | -2.90 | -6.38 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.65 | -2.35 | 0 | — | -4.87 | -1.94 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.04 | -2.96 | 36 | 16.7 | 5.58 | 0.83 | -22.11 | 114 |
| 19 | Trend pullback · 1h | trend | 96.68 | -3.32 | 86 | 24.4 | -21.45 | -6.01 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.29 | -3.71 | 11 | 0.0 | -4.10 | -3.12 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -15.13 | -5.50 | -16.86 | 299 |
| 22 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 23 | ADX DI cross · 1h | trend | 95.54 | -4.46 | 71 | 21.1 | -10.90 | -1.99 | -15.34 | 257 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 93.99 | -6.01 | 0 | — | 4.68 | 0.86 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.95 | 1.08 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.61 | -6.39 | 93 | 22.6 | 3.02 | 0.56 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.33 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.27 | -6.74 | 0 | — | -16.05 | -3.06 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.25 | -6.75 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.18 | -6.82 | 51 | 15.7 | 3.61 | 0.61 | -25.21 | 135 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.90 | -6.20 | -11.44 | 247 |
| 32 | MACD cross · 1h | trend | 92.73 | -7.27 | 154 | 22.1 | -13.01 | -1.75 | -26.23 | 458 |
| 33 | Max aggression: 5-day momentum | meta | 92.12 | -7.88 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 79 | 30.4 | 6.46 | 1.01 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.22 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.81 | -0.11 | -14.55 | 118 |
| 37 | Supertrend · 1h | trend | 91.44 | -8.56 | 74 | 13.5 | -1.75 | 0.01 | -28.77 | 213 |
| 38 | Stochastic reversion · 1h | reversion | 91.24 | -8.76 | 128 | 44.5 | -15.85 | -2.97 | -19.84 | 349 |
| 39 | RSI momentum · 1h | momentum | 91.23 | -8.77 | 73 | 17.8 | -0.49 | 0.16 | -26.54 | 225 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.19 | -9.81 | 77 | 16.9 | -7.15 | -0.54 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -6.19 | -2.19 | -7.66 | 122 |
| 43 | MFI reversion · 1h | reversion | 89.81 | -10.19 | 191 | 30.4 | -16.79 | -2.91 | -19.95 | 143 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.08 | -6.86 | -25.00 | 242 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.73 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.43 | -11.57 | 73 | 35.6 | -10.31 | -1.86 | -17.27 | 181 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.93 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.90 | -12.10 | 165 | 18.8 | -10.45 | -0.88 | -34.70 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.35 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.16 | -12.84 | 568 | 18.5 | -1.87 | -0.14 | -14.86 | 397 |
| 51 | MACD zero-line · 1h | trend | 86.86 | -13.13 | 74 | 16.2 | -22.27 | -4.33 | -22.40 | 228 |
| 52 | VWAP momentum · 1h | momentum | 86.38 | -13.62 | 354 | 21.8 | -34.50 | -5.01 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.23 | -13.77 | 172 | 26.2 | -30.05 | -4.85 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 85.92 | -14.08 | 180 | 21.7 | -8.78 | -1.07 | -25.32 | 399 |
| 55 | Donchian 20/10 · 1h | breakout | 85.73 | -14.27 | 72 | 19.4 | -0.35 | 0.16 | -20.75 | 219 |
| 56 | Three white soldiers | momentum | 85.57 | -14.43 | 202 | 19.3 | -47.72 | -19.52 | -48.85 | 609 |
| 57 | Bollinger reversion · 1h | reversion | 85.02 | -14.98 | 132 | 31.8 | -26.90 | -5.81 | -31.47 | 340 |
| 58 | EMA 9/21 cross · 1h | trend | 84.52 | -15.48 | 120 | 12.5 | -5.95 | -0.48 | -29.15 | 323 |
| 59 | Williams %R · 1h | reversion | 84.03 | -15.97 | 168 | 42.9 | -31.27 | -5.11 | -34.85 | 526 |
| 60 | CCI reversion · 1h | reversion | 83.38 | -16.62 | 143 | 42.7 | -15.27 | -1.97 | -23.38 | 429 |
| 61 | RSI(14) reversion · 1h | reversion | 83.37 | -16.63 | 61 | 23.0 | -12.31 | -2.30 | -18.95 | 169 |
| 62 | Candlestick reversal · 1h | reversion | 80.23 | -19.77 | 185 | 25.9 | -32.43 | -6.09 | -33.86 | 524 |
| 63 | RSI(14) reversion | reversion | 66.48 | -33.52 | 572 | 28.7 | -73.26 | -16.21 | -74.09 | 1559 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.94 | -16.88 | -76.65 | 1704 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.32 | -17.78 | -63.32 | 885 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.85 | -17.51 | -63.44 | 1216 |
| 67 | Donchian 55/20 | breakout | 63.12 | -36.88 | 420 | 18.3 | -68.76 | -14.15 | -71.15 | 1277 |
| 68 | EMA 20/50 cross | trend | 61.54 | -38.46 | 436 | 20.0 | -77.22 | -14.94 | -78.49 | 1446 |
| 69 | AI bee: Boozy | ai | 58.63 | -41.37 | 280 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.50 | -14.93 | -72.55 | 1425 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.55 | -25.88 | -83.75 | 1851 |
| 72 | Supertrend | trend | 54.28 | -45.72 | 613 | 20.4 | -86.35 | -19.91 | -86.49 | 1912 |
| 73 | Ichimoku | trend | 53.14 | -46.86 | 533 | 11.8 | -81.99 | -22.38 | -81.99 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.15 | -48.85 | 1039 | 9.1 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.55 | -28.28 | -98.58 | 5276 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.48 | -28.89 | -93.48 | 2589 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.58 | -24.00 | -90.68 | 2365 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.59 | -26.32 | -91.59 | 2324 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -31.08 | -97.45 | 3519 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.60 | -34.19 | -96.60 | 3586 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.53 | -24.50 | -94.53 | 2645 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -34.31 | -99.39 | 5712 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.26 | -24.93 | -91.26 | 2642 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.25 | -30.54 | -96.25 | 3550 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.77 | -99.72 | 6153 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.73 | -28.33 | -91.78 | 2366 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -36.15 | -97.46 | 3652 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -34.67 | -98.49 | 4680 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.53 | -31.33 | -93.53 | 2794 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -37.09 | -99.54 | 6167 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.09 | -21.71 | -86.36 | 2108 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.65 | -26.19 | -87.87 | 2119 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -31.16 | -96.03 | 3761 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.33 | -32.36 | -89.45 | 2105 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -32.20 | -95.82 | 4076 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.24 | -99.89 | 8222 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T23:53 | AI bee: Bizzy | buy | DOGE-USD | 7.49 | — | Jev: buy (buy p=0.59) |
| 2026-10-15T23:50 | RSI(14) reversion | buy | ETH-USD | 16.62 | — | entry signal |
| 2026-10-15T23:35 | EMA 20/50 cross | sell | BTC-USD | 12.35 | -0.06 | exit signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | XRP-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | SOL-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | RSI(14) reversion | buy | DOGE-USD | 16.65 | — | entry signal |
| 2026-10-15T23:30 | EMA 20/50 cross | sell | ETH-USD | 12.31 | -0.00 | exit signal |
| 2026-10-15T23:20 | EMA 20/50 cross | sell | SOL-USD | 12.32 | -0.01 | exit signal |
| 2026-10-15T23:20 | EMA 20/50 cross | sell | DOGE-USD | 15.37 | -0.20 | exit signal |
| 2026-10-15T23:15 | Supertrend | sell | BTC-USD | 13.55 | -0.11 | exit signal |
| 2026-10-15T23:10 | EMA 20/50 cross | buy | DOGE-USD | 3.11 | — | rebalance up |
| 2026-10-15T23:10 | EMA 20/50 cross | sell | XRP-USD | 12.30 | -0.07 | exit signal |
| 2026-10-15T23:05 | Candlestick reversal · 1h | sell | DOGE-USD | 6.19 | 0.05 | target is flat |
| 2026-10-15T23:05 | Donchian 55/20 | sell | ETH-USD | 15.81 | -0.04 | exit signal |
| 2026-10-15T23:05 | Donchian 55/20 | sell | DOGE-USD | 15.76 | -0.15 | exit signal |
| 2026-10-15T23:05 | Supertrend | sell | SOL-USD | 13.60 | -0.14 | exit signal |
| 2026-10-15T23:05 | Supertrend | sell | ETH-USD | 10.91 | 0.02 | exit signal |
| 2026-10-15T23:05 | Supertrend | sell | DOGE-USD | 10.87 | -0.06 | exit signal |
| 2026-10-15T23:00 | ADX DI cross · 1h | buy | BTC-USD | 9.52 | — | entry signal |
| 2026-10-15T23:00 | Ichimoku | sell | SOL-USD | 13.26 | -0.09 | exit signal |
| 2026-10-15T22:50 | Ichimoku | sell | ETH-USD | 13.26 | -0.08 | exit signal |
| 2026-10-15T22:36 | AI bee: Bizzy | sell | BTC-USD | 7.73 | -0.06 | Jev: sell (sell p=0.73) after 11 min |
| 2026-10-15T22:25 | AI bee: Bizzy | buy | BTC-USD | 7.79 | — | Jev: buy (buy p=0.61) |
| 2026-10-15T22:20 | Three white soldiers | sell | BTC-USD | 21.29 | -0.14 | exit signal |
| 2026-10-15T22:18 | AI bee: Boozy | sell | ETH-USD | 17.17 | -0.13 | Jev: sell |
| 2026-10-15T22:07 | AI bee: Bizzy | sell | SOL-USD | 7.25 | -0.04 | Jev: sell (sell p=0.59) after 10 min |
| 2026-10-15T22:02 | AI bee: Boozy | buy | ETH-USD | 17.30 | — | Jev: buy (buy p=0.71) |
| 2026-10-15T22:00 | Heikin-Ashi · 1h | sell | XRP-USD | 6.11 | -0.03 | exit signal |
| 2026-10-15T22:00 | Three white soldiers | buy | BTC-USD | 21.43 | — | entry signal |
| 2026-10-15T22:00 | Ichimoku | sell | DOGE-USD | 13.25 | -0.07 | exit signal |
| 2026-10-15T22:00 | Supertrend | buy | BTC-USD | 13.66 | — | entry signal |
| 2026-10-15T21:57 | AI bee: Bizzy | buy | SOL-USD | 7.29 | — | Jev: buy (buy p=0.57) |
| 2026-10-15T21:55 | Ichimoku | buy | DOGE-USD | 13.33 | — | entry signal |
| 2026-10-15T21:50 | Ichimoku | buy | ETH-USD | 13.34 | — | entry signal |
| 2026-10-15T21:45 | Three white soldiers | sell | XRP-USD | 21.31 | -0.15 | exit signal |
| 2026-10-15T21:45 | Ichimoku | buy | SOL-USD | 13.35 | — | entry signal |
| 2026-10-15T21:42 | AI bee: Bizzy | sell | DOGE-USD | 7.24 | -0.05 | Jev: sell (sell p=0.69) after 12 min |
| 2026-10-15T21:34 | AI bee: Bizzy | sell | SOL-USD | 7.09 | -0.04 | Jev: sell (sell p=0.58) after 16 min |
| 2026-10-15T21:30 | AI bee: Bizzy | buy | DOGE-USD | 7.29 | — | Jev: buy (buy p=0.57) |
| 2026-10-15T21:30 | Three white soldiers | buy | XRP-USD | 21.46 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 23:55:05.000183+00:00 -> 2026-10-16 00:05:05.000183+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
