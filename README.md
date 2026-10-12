# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T10:55:05.000141+00:00 · 20130 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 8082 decisions in 1617 calls, $0.1132 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T10:55 | 0 / 1 / 4 | NANC 18%, COIN 15% |  |
| Breezy | 2026-10-12T10:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T10:55 | 1 / 4 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MFI reversion | AAPL | 2.49 | +0.83% | 6 |
| Z-score reversion | TNA | 2.35 | +2.62% | 5 |
| CCI reversion | AAPL | 2.19 | +1.68% | 6 |
| VWAP momentum · 1h | PLTR | 2.12 | +8.28% | 5 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.27 | 3.27 | 37 | 43.2 | -7.53 | -2.28 | -13.79 | 116 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.58 | 2.58 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.25 | 2.25 | 0 | — | -3.56 | -1.44 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.06 | 2.06 | 14 | 57.1 | -12.40 | -2.03 | -20.64 | 68 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.38 | 1.38 | 0 | — | 1.88 | 0.90 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.29 | 1.29 | 0 | — | 0.49 | 0.33 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.14 | 1.14 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.96 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.80 | -0.20 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Hold BTC | benchmark | 99.74 | -0.26 | 0 | — | 29.28 | 3.45 | -8.68 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.74 | -0.26 | 0 | — | -3.82 | -1.75 | -5.36 | 1 |
| 16 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.19 | -1.56 | 85 |
| 18 | Donchian 55/20 · 1h | breakout | 99.23 | -0.77 | 28 | 14.3 | 12.79 | 1.59 | -16.96 | 114 |
| 19 | Stochastic reversion · 1h | reversion | 99.16 | -0.84 | 89 | 55.1 | -9.72 | -1.86 | -14.61 | 336 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.94 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.64 | -1.36 | 0 | — | 1.66 | 0.70 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.60 | -1.40 | 0 | — | 11.52 | 1.86 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.84 | -2.16 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.32 | -2.68 | 7 | 0.0 | -3.26 | -2.50 | -4.32 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.19 | -2.81 | 42 | 42.9 | 1.26 | 0.37 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.09 | -2.91 | 78 | 23.1 | -23.23 | -6.54 | -25.39 | 166 |
| 27 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -6.87 | -2.29 | -10.19 | 268 |
| 28 | EMA 20/50 cross · 1h | trend | 96.67 | -3.33 | 40 | 12.5 | 6.22 | 0.89 | -19.85 | 136 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.46 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.35 | -3.65 | 58 | 20.7 | -0.25 | 0.12 | -13.84 | 252 |
| 31 | Parabolic SAR · 1h | trend | 96.30 | -3.70 | 82 | 22.0 | -2.13 | -0.11 | -20.87 | 296 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -9.07 | -5.05 | -9.83 | 230 |
| 33 | MACD cross · 1h | trend | 95.71 | -4.29 | 118 | 23.7 | -14.84 | -2.36 | -17.27 | 469 |
| 34 | Supertrend · 1h | trend | 95.45 | -4.55 | 53 | 13.2 | 2.22 | 0.48 | -18.22 | 207 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -1.99 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.04 | 2.06 | -6.30 | 201 |
| 37 | MFI reversion · 1h | reversion | 93.52 | -6.48 | 119 | 34.5 | -10.24 | -1.62 | -17.79 | 124 |
| 38 | Squeeze breakout · 1h | breakout | 93.42 | -6.58 | 39 | 23.1 | 23.27 | 3.16 | -9.37 | 108 |
| 39 | RSI(14) reversion · 1h | reversion | 93.12 | -6.88 | 26 | 26.9 | -1.97 | -0.32 | -9.03 | 145 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.10 | -5.95 | -20.97 | 249 |
| 41 | Agent (ML meta-label) | meta | 92.86 | -7.14 | 392 | 18.4 | -2.75 | -0.34 | -13.71 | 409 |
| 42 | Bollinger reversion · 1h | reversion | 92.77 | -7.23 | 78 | 37.2 | -20.80 | -4.93 | -23.20 | 313 |
| 43 | RSI momentum · 1h | momentum | 92.69 | -7.31 | 64 | 15.6 | 4.72 | 0.77 | -17.17 | 225 |
| 44 | Volume breakout · 1h | breakout | 92.11 | -7.89 | 59 | 20.3 | 7.61 | 1.19 | -12.60 | 122 |
| 45 | Ichimoku · 1h | trend | 91.82 | -8.18 | 45 | 17.8 | -1.24 | 0.05 | -21.18 | 125 |
| 46 | Williams %R · 1h | reversion | 91.55 | -8.45 | 126 | 47.6 | -23.72 | -4.04 | -26.91 | 509 |
| 47 | Bollinger breakout · 1h | breakout | 91.24 | -8.76 | 72 | 27.8 | 6.18 | 0.95 | -13.62 | 287 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.05 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.72 | -9.29 | 69 | 15.9 | -7.92 | -0.76 | -26.49 | 238 |
| 50 | Candlestick reversal · 1h | reversion | 90.40 | -9.60 | 118 | 33.1 | -25.63 | -4.94 | -27.68 | 502 |
| 51 | CCI reversion · 1h | reversion | 89.96 | -10.04 | 105 | 46.7 | -7.04 | -0.87 | -14.35 | 411 |
| 52 | VWAP momentum · 1h | momentum | 89.43 | -10.57 | 285 | 21.8 | -32.56 | -4.83 | -39.21 | 1281 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.38 | -5.18 | -19.78 | 700 |
| 54 | OBV trend · 1h | momentum | 88.76 | -11.24 | 149 | 18.8 | -12.23 | -1.38 | -28.50 | 323 |
| 55 | Donchian 20/10 · 1h | breakout | 88.70 | -11.30 | 60 | 18.3 | -0.74 | 0.12 | -18.18 | 228 |
| 56 | Heikin-Ashi · 1h | trend | 88.65 | -11.35 | 138 | 25.4 | -29.75 | -4.94 | -36.59 | 700 |
| 57 | MACD zero-line · 1h | trend | 88.25 | -11.75 | 66 | 18.2 | -6.97 | -0.75 | -20.89 | 240 |
| 58 | Max aggression: 5-day momentum | meta | 87.96 | -12.04 | 7 | 28.6 | -14.32 | -1.04 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.87 | -12.13 | 104 | 13.5 | -8.61 | -0.96 | -21.96 | 339 |
| 60 | Keltner breakout · 1h | breakout | 87.09 | -12.91 | 43 | 18.6 | -12.54 | -1.46 | -26.07 | 221 |
| 61 | Three white soldiers | momentum | 86.74 | -13.26 | 147 | 17.0 | -48.22 | -23.11 | -48.31 | 593 |
| 62 | ROC + volume · 1h | momentum | 86.26 | -13.74 | 132 | 21.2 | -10.50 | -1.26 | -23.80 | 416 |
| 63 | ROC + volume | momentum | 73.90 | -26.10 | 401 | 22.9 | -73.09 | -16.62 | -74.19 | 1685 |
| 64 | RSI(14) reversion | reversion | 73.69 | -26.31 | 375 | 27.5 | -72.18 | -17.86 | -72.20 | 1487 |
| 65 | Squeeze breakout | breakout | 70.38 | -29.62 | 340 | 15.3 | -62.17 | -18.00 | -62.18 | 1234 |
| 66 | Volume breakout | breakout | 69.81 | -30.19 | 271 | 14.0 | -62.42 | -17.79 | -62.43 | 904 |
| 67 | EMA 20/50 cross | trend | 68.46 | -31.54 | 348 | 19.8 | -76.73 | -15.22 | -76.75 | 1453 |
| 68 | Donchian 55/20 | breakout | 68.19 | -31.81 | 350 | 18.0 | -68.04 | -14.50 | -68.35 | 1299 |
| 69 | VWAP reversion | reversion | 67.72 | -32.28 | 405 | 25.9 | -71.25 | -15.77 | -71.30 | 1429 |
| 70 | Supertrend | trend | 61.75 | -38.25 | 484 | 19.6 | -86.09 | -21.07 | -86.14 | 1916 |
| 71 | Keltner breakout | breakout | 61.17 | -38.83 | 470 | 14.5 | -83.77 | -27.78 | -83.77 | 1854 |
| 72 | AI bee: Boozy | ai | 59.96 | -40.04 | 261 | 5.0 | — | — | — | — |
| 73 | Z-score reversion | reversion | 58.58 | -41.42 | 519 | 22.0 | -85.11 | -22.81 | -85.16 | 2077 |
| 74 | Ichimoku | trend | 58.46 | -41.55 | 425 | 10.1 | -82.00 | -23.21 | -82.00 | 1756 |
| 75 | MFI reversion | reversion | 57.70 | -42.30 | 528 | 20.6 | -87.58 | -28.04 | -87.62 | 2125 |
| 76 | AI bee: Bizzy | ai | 55.94 | -44.05 | 871 | 8.5 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.58 | -45.42 | 565 | 10.1 | -89.44 | -35.37 | -89.44 | 2128 |
| 78 | Donchian 20/10 | breakout | 53.40 | -46.60 | 658 | 17.9 | -90.88 | -26.16 | -90.88 | 2670 |
| 79 | MACD zero-line | trend | 52.03 | -47.97 | 611 | 14.6 | -91.50 | -29.78 | -91.50 | 2366 |
| 80 | RSI momentum | momentum | 51.60 | -48.40 | 636 | 16.7 | -90.56 | -25.90 | -90.56 | 2395 |
| 81 | Trend pullback | trend | 51.55 | -48.45 | 625 | 14.4 | -91.32 | -27.17 | -91.32 | 2355 |
| 82 | Triple EMA stack | trend | 50.68 | -49.32 | 660 | 15.2 | -93.34 | -30.45 | -93.34 | 2631 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.66 | -31.24 | -98.66 | 5398 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.38 | -33.49 | -97.38 | 3554 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -36.27 | -96.50 | 3627 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.26 | -25.51 | -94.26 | 2695 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.89 | -99.35 | 5697 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.53 | -31.98 | -96.53 | 3650 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.66 | -99.73 | 6202 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.35 | -38.10 | -97.35 | 3692 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -36.80 | -98.45 | 4708 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.52 | -33.15 | -93.52 | 2822 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -40.14 | -99.52 | 6152 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.77 | -33.14 | -95.78 | 3738 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.65 | -34.32 | -95.65 | 4091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.05 | -99.89 | 8303 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T10:55 | ADX DI cross | sell | SOL-USD | 13.56 | -0.11 | exit signal |
| 2026-10-12T10:50 | AI bee: Bizzy | sell | DOGE-USD | 7.81 | -0.04 | Jev: sell (sell p=0.51) after 10 min |
| 2026-10-12T10:50 | RSI momentum | buy | DOGE-USD | 12.91 | — | entry |
| 2026-10-12T10:50 | ROC + volume | buy | DOGE-USD | 18.50 | — | entry signal |
| 2026-10-12T10:50 | ADX DI cross | buy | SOL-USD | 13.67 | — | entry signal |
| 2026-10-12T10:45 | Z-score reversion | sell | DOGE-USD | 14.67 | -0.02 | exit signal |
| 2026-10-12T10:45 | Volume breakout | buy | DOGE-USD | 17.47 | — | entry signal |
| 2026-10-12T10:45 | Donchian 20/10 | buy | DOGE-USD | 13.36 | — | entry signal |
| 2026-10-12T10:40 | AI bee: Bizzy | buy | DOGE-USD | 7.85 | — | Jev: buy (buy p=0.56) |
| 2026-10-12T10:40 | Three white soldiers | buy | DOGE-USD | 21.70 | — | entry signal |
| 2026-10-12T10:40 | Supertrend | buy | DOGE-USD | 15.45 | — | entry signal |
| 2026-10-12T10:35 | MFI reversion | buy | SOL-USD | 2.88 | — | rebalance up |
| 2026-10-12T10:35 | MFI reversion | sell | DOGE-USD | 2.88 | -0.02 | rebalance down |
| 2026-10-12T10:30 | MFI reversion | buy | SOL-USD | 5.82 | — | entry signal |
| 2026-10-12T10:30 | MFI reversion | sell | ETH-USD | 2.93 | -0.01 | rebalance down |
| 2026-10-12T10:30 | MFI reversion | sell | BTC-USD | 2.89 | -0.01 | rebalance down |
| 2026-10-12T10:12 | AI bee: Bizzy | sell | ETH-USD | 7.91 | -0.06 | Jev: sell (sell p=0.82) after 10 min |
| 2026-10-12T10:02 | AI bee: Bizzy | buy | ETH-USD | 7.98 | — | Jev: buy (buy p=0.57) |
| 2026-10-12T10:00 | MACD cross · 1h | sell | SOL-USD | 5.10 | 0.06 | exit signal |
| 2026-10-12T10:00 | MFI reversion | buy | XRP-USD | 14.46 | — | entry signal |
| 2026-10-12T10:00 | MFI reversion | buy | DOGE-USD | 14.47 | — | entry signal |
| 2026-10-12T09:55 | MFI reversion | buy | BTC-USD | 14.47 | — | entry signal |
| 2026-10-12T09:55 | Z-score reversion | buy | XRP-USD | 14.65 | — | entry signal |
| 2026-10-12T09:55 | RSI(14) reversion | buy | SOL-USD | 18.43 | — | entry signal |
| 2026-10-12T09:50 | MFI reversion | sell | DOGE-USD | 14.36 | -0.13 | stop-loss |
| 2026-10-12T09:50 | VWAP reversion | buy | BTC-USD | 16.94 | — | entry signal |
| 2026-10-12T09:50 | Z-score reversion | buy | SOL-USD | 14.64 | — | entry signal |
| 2026-10-12T09:50 | RSI(14) reversion | buy | BTC-USD | 18.44 | — | entry signal |
| 2026-10-12T09:45 | Z-score reversion | sell | SOL-USD | 14.57 | -0.15 | stop-loss |
| 2026-10-12T09:40 | Z-score reversion | buy | DOGE-USD | 14.69 | — | entry signal |
| 2026-10-12T09:40 | Z-score reversion | sell | BTC-USD | 14.61 | -0.12 | stop-loss |
| 2026-10-12T09:25 | MFI reversion | buy | DOGE-USD | 14.49 | — | entry signal |
| 2026-10-12T09:15 | MFI reversion | buy | ETH-USD | 14.51 | — | entry signal |
| 2026-10-12T09:00 | Volume breakout · 1h | sell | ETH-USD | 23.17 | 0.03 | exit signal |
| 2026-10-12T09:00 | VWAP momentum · 1h | sell | SOL-USD | 6.84 | -0.03 | exit signal |
| 2026-10-12T09:00 | Ichimoku · 1h | sell | XRP-USD | 22.75 | -0.35 | exit signal |
| 2026-10-12T09:00 | MACD cross · 1h | sell | XRP-USD | 4.50 | -0.07 | exit signal |
| 2026-10-12T09:00 | MACD cross · 1h | sell | BTC-USD | 4.51 | -0.06 | stop-loss |
| 2026-10-12T09:00 | MFI reversion | sell | BTC-USD | 14.41 | -0.13 | stop-loss |
| 2026-10-12T08:55 | EMA 20/50 cross | sell | ETH-USD | 13.88 | -0.01 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 10:55:05.000141+00:00 -> 2026-10-12 11:05:05.000141+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
