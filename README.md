# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T11:25:05.000145+00:00 · 22403 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.12 (-4.88%)

Closed trades 64, win rate 46.9%, fees £2.37, max drawdown -5.38%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-13)

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 21.14 · VIX 15.27 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 8335 decisions in 1667 calls, $0.1166 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T11:25 | 1 / 1 / 3 | AMD 14% |  |
| Breezy | 2026-10-14T11:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T11:25 | 5 / 0 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.05 | 3.05 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.06 | -2.68 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.75 | 1.75 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.98 | 0.98 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.35 | 0.35 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 99.77 | -0.23 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 13 | Daily: SMA 20/50 cross · AAPL | daily | 99.77 | -0.23 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 14 | Hold BTC | benchmark | 99.43 | -0.57 | 0 | — | 30.87 | 3.55 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.89 | -1.11 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.34 | -1.66 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.73 | -2.27 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.41 | -2.59 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.31 | -2.69 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -6.98 | -2.85 | -8.76 | 307 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.24 | -3.76 | 65 | 18.5 | -11.46 | -2.11 | -14.81 | 251 |
| 26 | Stochastic reversion · 1h | reversion | 96.19 | -3.81 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.72 | -4.28 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | Z-score reversion · 1h | reversion | 95.39 | -4.61 | 52 | 44.2 | 2.82 | 0.69 | -8.60 | 158 |
| 29 | MACD cross · 1h | trend | 95.32 | -4.68 | 136 | 22.8 | -8.86 | -1.14 | -19.25 | 458 |
| 30 | EMA 20/50 cross · 1h | trend | 95.31 | -4.69 | 45 | 15.6 | 10.68 | 1.33 | -19.71 | 135 |
| 31 | Max aggression: 1-day momentum | meta | 95.30 | -4.70 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.95 | -5.12 | -8.95 | 234 |
| 33 | Squeeze breakout · 1h | breakout | 93.93 | -6.07 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 34 | Supertrend · 1h | trend | 93.91 | -6.09 | 60 | 13.3 | 2.19 | 0.47 | -20.34 | 213 |
| 35 | Parabolic SAR · 1h | trend | 93.52 | -6.48 | 91 | 22.0 | 1.66 | 0.40 | -22.84 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.62 | -0.50 | -5.61 | 112 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.56 | -7.44 | 66 | 15.2 | 0.88 | 0.31 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.48 | -7.52 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.96 | -8.04 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.43 | -8.57 | 38 | 34.2 | 6.07 | 1.39 | -9.40 | 125 |
| 42 | Ichimoku · 1h | trend | 91.24 | -8.76 | 48 | 16.7 | 1.84 | 0.42 | -22.34 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.01 | -8.99 | 485 | 18.1 | -2.42 | -0.30 | -13.98 | 383 |
| 44 | Triple EMA stack · 1h | trend | 90.65 | -9.35 | 71 | 15.5 | -7.45 | -0.57 | -32.27 | 241 |
| 45 | Volume breakout · 1h | breakout | 90.65 | -9.35 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 89.91 | -10.09 | 97 | 37.1 | -23.86 | -5.74 | -24.98 | 323 |
| 48 | Williams %R · 1h | reversion | 89.37 | -10.63 | 143 | 45.5 | -28.08 | -4.77 | -29.53 | 513 |
| 49 | CCI reversion · 1h | reversion | 88.88 | -11.12 | 120 | 45.0 | -9.64 | -1.26 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.04 | -11.96 | 159 | 18.2 | -9.75 | -0.82 | -33.87 | 322 |
| 52 | MACD zero-line · 1h | trend | 87.30 | -12.70 | 71 | 16.9 | -22.24 | -4.32 | -22.54 | 229 |
| 53 | VWAP momentum · 1h | momentum | 87.24 | -12.76 | 333 | 22.8 | -33.47 | -4.97 | -40.79 | 1255 |
| 54 | Donchian 20/10 · 1h | breakout | 86.94 | -13.06 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.71 | -13.29 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 86.57 | -13.43 | 111 | 12.6 | -10.29 | -1.30 | -24.29 | 329 |
| 58 | Heikin-Ashi · 1h | trend | 86.54 | -13.46 | 166 | 26.5 | -29.46 | -4.81 | -38.65 | 673 |
| 59 | Candlestick reversal · 1h | reversion | 86.33 | -13.67 | 143 | 30.8 | -28.17 | -5.45 | -28.62 | 464 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.80 | -14.20 | 168 | 17.9 | -47.61 | -21.85 | -47.85 | 583 |
| 62 | ROC + volume · 1h | momentum | 85.27 | -14.73 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 69.87 | -30.13 | 463 | 22.0 | -73.49 | -16.52 | -75.55 | 1674 |
| 64 | RSI(14) reversion | reversion | 67.30 | -32.70 | 462 | 27.5 | -73.38 | -16.75 | -73.76 | 1474 |
| 65 | Volume breakout | breakout | 67.00 | -33.00 | 301 | 14.0 | -62.09 | -17.39 | -62.40 | 891 |
| 66 | Squeeze breakout | breakout | 66.91 | -33.09 | 384 | 15.1 | -62.57 | -17.95 | -62.79 | 1222 |
| 67 | EMA 20/50 cross | trend | 64.52 | -35.48 | 400 | 19.8 | -76.60 | -14.92 | -77.23 | 1440 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.18 | -14.42 | -70.80 | 1285 |
| 69 | VWAP reversion | reversion | 62.37 | -37.63 | 489 | 25.4 | -72.05 | -15.02 | -72.23 | 1395 |
| 70 | AI bee: Boozy | ai | 59.77 | -40.23 | 271 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.82 | -42.18 | 556 | 19.4 | -85.78 | -20.27 | -85.80 | 1912 |
| 72 | Keltner breakout | breakout | 57.43 | -42.57 | 540 | 14.3 | -83.22 | -26.72 | -83.22 | 1846 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.30 | -22.74 | -82.30 | 1721 |
| 74 | AI bee: Bizzy | ai | 52.92 | -47.08 | 963 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.67 | -47.34 | 677 | 20.1 | -87.65 | -26.70 | -87.66 | 2108 |
| 76 | Z-score reversion | reversion | 52.24 | -47.77 | 627 | 23.0 | -85.95 | -21.71 | -85.98 | 2083 |
| 77 | ADX DI cross | trend | 50.67 | -49.33 | 658 | 10.3 | -89.22 | -33.32 | -89.22 | 2111 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.48 | -28.87 | -98.48 | 5305 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.41 | -29.40 | -93.43 | 2614 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.39 | -24.46 | -90.42 | 2371 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.63 | -26.25 | -91.63 | 2353 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.36 | -31.82 | -97.36 | 3536 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.51 | -34.81 | -96.51 | 3601 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.51 | -25.25 | -94.51 | 2642 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.22 | -99.37 | 5644 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.98 | -25.51 | -90.98 | 2635 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -30.42 | -96.38 | 3597 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.49 | -99.72 | 6159 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.51 | -29.02 | -91.51 | 2361 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -36.16 | -97.40 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -34.91 | -98.50 | 4671 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.42 | -31.84 | -93.42 | 2801 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.76 | -99.54 | 6120 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -31.32 | -95.93 | 3731 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -33.07 | -95.67 | 4042 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.86 | -99.89 | 8212 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T11:22 | MFI reversion | sell | XRP-USD | 10.53 | -0.01 | exit signal |
| 2026-10-14T11:22 | EMA 20/50 cross | buy | XRP-USD | 16.14 | — | entry signal |
| 2026-10-14T11:15 | MFI reversion | buy | SOL-USD | 2.64 | — | rebalance up |
| 2026-10-14T11:15 | MFI reversion | buy | DOGE-USD | 5.27 | — | rebalance up |
| 2026-10-14T11:15 | MFI reversion | sell | ETH-USD | 13.12 | -0.07 | exit signal |
| 2026-10-14T11:05 | Three white soldiers | sell | ETH-USD | 21.35 | -0.13 | exit signal |
| 2026-10-14T11:05 | ADX DI cross | sell | SOL-USD | 12.61 | -0.11 | exit signal |
| 2026-10-14T11:05 | ADX DI cross | sell | ETH-USD | 12.61 | -0.10 | exit signal |
| 2026-10-14T11:00 | Bollinger reversion · 1h | buy | SOL-USD | 1.58 | — | entry signal |
| 2026-10-14T11:00 | Bollinger reversion · 1h | buy | ETH-USD | 11.25 | — | entry signal |
| 2026-10-14T11:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.85 | — | entry signal |
| 2026-10-14T11:00 | Candlestick reversal · 1h | buy | ETH-USD | 7.85 | — | entry signal |
| 2026-10-14T11:00 | VWAP momentum · 1h | buy | XRP-USD | 7.27 | — | entry signal |
| 2026-10-14T11:00 | Parabolic SAR · 1h | sell | BTC-USD | 23.23 | -0.20 | exit signal |
| 2026-10-14T11:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 5.06 | — | entry |
| 2026-10-14T11:00 | EMA 9/21 cross · 1h | sell | DOGE-USD | 5.06 | -0.05 | exit signal |
| 2026-10-14T11:00 | Z-score reversion | sell | SOL-USD | 13.05 | -0.02 | exit signal |
| 2026-10-14T11:00 | Z-score reversion | sell | ETH-USD | 13.02 | -0.02 | exit signal |
| 2026-10-14T11:00 | RSI(14) reversion | sell | ETH-USD | 16.82 | -0.00 | exit signal |
| 2026-10-14T11:00 | Keltner breakout | buy | XRP-USD | 14.38 | — | entry signal |
| 2026-10-14T11:00 | ROC + volume | buy | XRP-USD | 17.49 | — | entry signal |
| 2026-10-14T11:00 | ADX DI cross | buy | ETH-USD | 12.71 | — | entry signal |
| 2026-10-14T11:00 | Supertrend | buy | ETH-USD | 14.48 | — | entry signal |
| 2026-10-14T10:55 | Supertrend | buy | XRP-USD | 14.48 | — | entry signal |
| 2026-10-14T10:50 | MFI reversion | buy | DOGE-USD | 5.27 | — | rebalance up |
| 2026-10-14T10:50 | MFI reversion | sell | XRP-USD | 2.63 | -0.01 | rebalance down |
| 2026-10-14T10:50 | MFI reversion | sell | SOL-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-14T10:50 | ADX DI cross | buy | SOL-USD | 12.72 | — | entry signal |
| 2026-10-14T10:50 | Supertrend | buy | SOL-USD | 14.49 | — | entry signal |
| 2026-10-14T10:49 | AI bee: Bizzy | sell | XRP-USD | 8.02 | -0.04 | Jev: sell (sell p=0.67) after 11 min |
| 2026-10-14T10:45 | MFI reversion | buy | DOGE-USD | 2.67 | — | entry signal |
| 2026-10-14T10:45 | MFI reversion | sell | BTC-USD | 2.63 | -0.01 | rebalance down |
| 2026-10-14T10:38 | AI bee: Bizzy | buy | XRP-USD | 8.06 | — | Jev: buy (buy p=0.61) |
| 2026-10-14T10:35 | MFI reversion | buy | ETH-USD | 13.19 | — | entry signal |
| 2026-10-14T10:20 | Three white soldiers | buy | ETH-USD | 21.48 | — | entry signal |
| 2026-10-14T10:15 | Z-score reversion | buy | ETH-USD | 13.05 | — | entry signal |
| 2026-10-14T10:10 | VWAP reversion | buy | ETH-USD | 15.54 | — | entry signal |
| 2026-10-14T10:10 | VWAP reversion | buy | BTC-USD | 15.55 | — | entry signal |
| 2026-10-14T10:10 | RSI(14) reversion | buy | ETH-USD | 16.83 | — | entry signal |
| 2026-10-14T10:05 | VWAP reversion | sell | ETH-USD | 15.44 | -0.17 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 11:25:05.000145+00:00 -> 2026-10-14 11:35:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
