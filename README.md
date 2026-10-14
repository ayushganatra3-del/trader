# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T12:25:05.000138+00:00 · 22449 ticks

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

Today: 9022 decisions in 1805 calls, $0.1262 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T12:25 | 0 / 3 / 2 | AMD 14% |  |
| Breezy | 2026-10-14T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T12:25 | 1 / 3 / 1 | ETH-USD 22% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.07 | 3.07 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.12 | -2.70 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.76 | 1.76 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.00 | 1.00 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.37 | 0.37 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.79 | -0.21 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.79 | -0.21 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.72 | -0.28 | 0 | — | 31.17 | 3.58 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.91 | -1.09 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.36 | -1.64 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.74 | -2.26 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.43 | -2.57 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.32 | -2.68 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.86 | -8.69 | 309 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.30 | -3.70 | 65 | 18.5 | -11.39 | -2.09 | -14.81 | 251 |
| 26 | Stochastic reversion · 1h | reversion | 96.21 | -3.79 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.73 | -4.27 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | Z-score reversion · 1h | reversion | 95.43 | -4.57 | 52 | 44.2 | 2.86 | 0.69 | -8.60 | 158 |
| 29 | MACD cross · 1h | trend | 95.36 | -4.64 | 136 | 22.8 | -8.66 | -1.11 | -19.25 | 458 |
| 30 | EMA 20/50 cross · 1h | trend | 95.33 | -4.67 | 45 | 15.6 | 10.38 | 1.31 | -20.35 | 136 |
| 31 | Max aggression: 1-day momentum | meta | 95.31 | -4.69 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.08 | -8.87 | 233 |
| 33 | Supertrend · 1h | trend | 93.99 | -6.01 | 60 | 13.3 | 2.29 | 0.48 | -20.34 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.93 | -6.07 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.53 | -6.47 | 91 | 22.0 | 1.43 | 0.37 | -22.84 | 289 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.58 | -7.42 | 66 | 15.2 | 1.22 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.49 | -7.51 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.98 | -8.02 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.49 | -8.51 | 38 | 34.2 | 5.77 | 1.33 | -9.40 | 128 |
| 42 | Ichimoku · 1h | trend | 91.26 | -8.74 | 48 | 16.7 | 1.84 | 0.42 | -22.34 | 125 |
| 43 | Agent (ML meta-label) | meta | 91.02 | -8.98 | 485 | 18.1 | -0.04 | 0.13 | -12.61 | 374 |
| 44 | Triple EMA stack · 1h | trend | 90.71 | -9.29 | 71 | 15.5 | -7.46 | -0.57 | -32.27 | 240 |
| 45 | Volume breakout · 1h | breakout | 90.66 | -9.34 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.65 | -9.35 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 89.96 | -10.04 | 97 | 37.1 | -23.71 | -5.69 | -24.90 | 322 |
| 48 | Williams %R · 1h | reversion | 89.38 | -10.62 | 143 | 45.5 | -28.06 | -4.76 | -29.59 | 513 |
| 49 | CCI reversion · 1h | reversion | 88.91 | -11.09 | 120 | 45.0 | -9.72 | -1.27 | -14.42 | 418 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.06 | -11.94 | 159 | 18.2 | -9.88 | -0.83 | -33.87 | 322 |
| 52 | MACD zero-line · 1h | trend | 87.40 | -12.60 | 71 | 16.9 | -22.34 | -4.34 | -22.71 | 230 |
| 53 | VWAP momentum · 1h | momentum | 87.29 | -12.71 | 333 | 22.8 | -33.09 | -4.90 | -40.79 | 1252 |
| 54 | Donchian 20/10 · 1h | breakout | 86.95 | -13.05 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Max aggression: 5-day momentum | meta | 86.72 | -13.28 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 56 | Keltner breakout · 1h | breakout | 86.66 | -13.34 | 49 | 20.4 | -8.10 | -0.87 | -26.76 | 214 |
| 57 | EMA 9/21 cross · 1h | trend | 86.62 | -13.38 | 111 | 12.6 | -10.36 | -1.31 | -24.29 | 330 |
| 58 | Heikin-Ashi · 1h | trend | 86.55 | -13.45 | 166 | 26.5 | -29.46 | -4.81 | -38.65 | 673 |
| 59 | Candlestick reversal · 1h | reversion | 86.39 | -13.61 | 143 | 30.8 | -29.58 | -5.73 | -30.06 | 475 |
| 60 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 61 | Three white soldiers | momentum | 85.72 | -14.28 | 168 | 17.9 | -47.66 | -21.89 | -47.90 | 584 |
| 62 | ROC + volume · 1h | momentum | 85.29 | -14.71 | 173 | 20.2 | -8.96 | -1.02 | -24.87 | 399 |
| 63 | ROC + volume | momentum | 69.68 | -30.32 | 464 | 22.0 | -73.57 | -16.54 | -75.61 | 1676 |
| 64 | RSI(14) reversion | reversion | 67.30 | -32.70 | 462 | 27.5 | -73.25 | -16.67 | -73.65 | 1472 |
| 65 | Volume breakout | breakout | 66.82 | -33.18 | 301 | 14.0 | -62.19 | -17.42 | -62.50 | 894 |
| 66 | Squeeze breakout | breakout | 66.75 | -33.25 | 384 | 15.1 | -62.67 | -18.00 | -62.89 | 1224 |
| 67 | EMA 20/50 cross | trend | 64.29 | -35.71 | 400 | 19.8 | -76.73 | -14.96 | -77.31 | 1445 |
| 68 | Donchian 55/20 | breakout | 63.13 | -36.87 | 395 | 16.7 | -69.18 | -14.42 | -70.80 | 1285 |
| 69 | VWAP reversion | reversion | 62.38 | -37.62 | 493 | 25.6 | -72.10 | -15.05 | -72.28 | 1398 |
| 70 | AI bee: Boozy | ai | 59.72 | -40.28 | 271 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 57.88 | -42.12 | 556 | 19.4 | -85.84 | -20.34 | -85.87 | 1916 |
| 72 | Keltner breakout | breakout | 57.13 | -42.87 | 541 | 14.2 | -83.32 | -26.77 | -83.32 | 1851 |
| 73 | Ichimoku | trend | 54.01 | -45.99 | 482 | 9.5 | -82.30 | -22.74 | -82.30 | 1721 |
| 74 | AI bee: Bizzy | ai | 52.72 | -47.28 | 967 | 8.4 | — | — | — | — |
| 75 | MFI reversion | reversion | 52.70 | -47.30 | 680 | 20.1 | -87.64 | -26.68 | -87.66 | 2108 |
| 76 | Z-score reversion | reversion | 52.21 | -47.79 | 628 | 22.9 | -85.83 | -21.59 | -85.86 | 2080 |
| 77 | ADX DI cross | trend | 50.67 | -49.33 | 658 | 10.3 | -89.25 | -33.41 | -89.25 | 2113 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.50 | -28.93 | -98.50 | 5312 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -29.46 | -93.46 | 2618 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.41 | -24.48 | -90.44 | 2375 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.61 | -26.17 | -91.61 | 2352 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -31.67 | -97.35 | 3534 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.54 | -34.87 | -96.54 | 3607 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.52 | -25.21 | -94.52 | 2643 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.37 | -35.10 | -99.37 | 5640 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.93 | -25.44 | -90.94 | 2635 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -30.42 | -96.38 | 3597 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.71 | -39.15 | -99.71 | 6153 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.48 | -28.93 | -91.51 | 2361 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -36.11 | -97.40 | 3673 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -34.88 | -98.50 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.39 | -31.75 | -93.40 | 2802 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.77 | -99.54 | 6121 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -31.32 | -95.93 | 3731 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.66 | -33.07 | -95.67 | 4042 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.96 | -99.89 | 8214 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T12:24 | AI bee: Bizzy | sell | SOL-USD | 7.48 | -0.07 | Jev: sell (sell p=0.74) after 11 min |
| 2026-10-14T12:22 | AI bee: Bizzy | sell | BTC-USD | 7.23 | -0.05 | Jev: sell (sell p=0.57) after 10 min |
| 2026-10-14T12:18 | EMA 20/50 cross | buy | ETH-USD | 3.21 | — | rebalance up |
| 2026-10-14T12:18 | EMA 20/50 cross | sell | BTC-USD | 3.21 | -0.02 | rebalance down |
| 2026-10-14T12:17 | EMA 20/50 cross | buy | ETH-USD | 3.23 | — | rebalance up |
| 2026-10-14T12:17 | EMA 20/50 cross | sell | SOL-USD | 3.23 | -0.01 | rebalance down |
| 2026-10-14T12:15 | MFI reversion | sell | DOGE-USD | 13.23 | 0.02 | exit signal |
| 2026-10-14T12:15 | MFI reversion | sell | BTC-USD | 10.57 | 0.01 | exit signal |
| 2026-10-14T12:15 | Squeeze breakout | buy | ETH-USD | 16.72 | — | entry signal |
| 2026-10-14T12:15 | EMA 20/50 cross | buy | ETH-USD | 6.47 | — | entry signal |
| 2026-10-14T12:15 | EMA 20/50 cross | buy | DOGE-USD | 12.91 | — | entry signal |
| 2026-10-14T12:15 | EMA 20/50 cross | sell | XRP-USD | 3.25 | -0.00 | rebalance down |
| 2026-10-14T12:13 | AI bee: Bizzy | buy | SOL-USD | 7.55 | — | Jev: buy (buy p=0.57) |
| 2026-10-14T12:13 | Keltner breakout | sell | XRP-USD | 2.86 | -0.02 | rebalance down |
| 2026-10-14T12:12 | AI bee: Bizzy | buy | BTC-USD | 7.28 | — | Jev: buy (buy p=0.55) |
| 2026-10-14T12:12 | Keltner breakout | buy | SOL-USD | 2.86 | — | rebalance up |
| 2026-10-14T12:12 | Keltner breakout | sell | DOGE-USD | 2.86 | -0.01 | rebalance down |
| 2026-10-14T12:10 | AI bee: Boozy | buy | ETH-USD | 13.45 | — | Jev: buy (buy p=0.79) |
| 2026-10-14T12:10 | Three white soldiers | buy | ETH-USD | 21.45 | — | entry signal |
| 2026-10-14T12:10 | Volume breakout | buy | DOGE-USD | 16.73 | — | entry signal |
| 2026-10-14T12:10 | Squeeze breakout | buy | BTC-USD | 16.73 | — | entry signal |
| 2026-10-14T12:10 | Keltner breakout | buy | SOL-USD | 5.76 | — | entry signal |
| 2026-10-14T12:10 | Keltner breakout | buy | ETH-USD | 11.46 | — | entry signal |
| 2026-10-14T12:10 | Keltner breakout | buy | BTC-USD | 11.46 | — | entry signal |
| 2026-10-14T12:10 | ROC + volume | buy | SOL-USD | 17.46 | — | entry signal |
| 2026-10-14T12:10 | ROC + volume | buy | DOGE-USD | 17.46 | — | entry signal |
| 2026-10-14T12:10 | EMA 20/50 cross | buy | SOL-USD | 16.15 | — | entry signal |
| 2026-10-14T12:10 | EMA 20/50 cross | buy | BTC-USD | 16.15 | — | entry signal |
| 2026-10-14T12:05 | VWAP reversion | sell | SOL-USD | 15.65 | 0.02 | exit signal |
| 2026-10-14T12:05 | VWAP reversion | sell | ETH-USD | 15.56 | 0.02 | exit signal |
| 2026-10-14T12:05 | VWAP reversion | sell | DOGE-USD | 15.63 | -0.00 | exit signal |
| 2026-10-14T12:05 | VWAP reversion | sell | BTC-USD | 15.54 | -0.02 | exit signal |
| 2026-10-14T12:05 | Volume breakout | buy | XRP-USD | 16.75 | — | entry signal |
| 2026-10-14T12:05 | Volume breakout | buy | BTC-USD | 16.75 | — | entry signal |
| 2026-10-14T12:05 | Keltner breakout | buy | XRP-USD | 14.34 | — | entry signal |
| 2026-10-14T12:05 | Keltner breakout | buy | DOGE-USD | 14.34 | — | entry signal |
| 2026-10-14T12:05 | Supertrend | buy | DOGE-USD | 8.72 | — | entry signal |
| 2026-10-14T12:05 | Supertrend | buy | BTC-USD | 11.59 | — | entry signal |
| 2026-10-14T12:05 | Supertrend | sell | XRP-USD | 2.90 | -0.00 | rebalance down |
| 2026-10-14T12:05 | Supertrend | sell | SOL-USD | 2.90 | -0.01 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 12:25:05.000138+00:00 -> 2026-10-14 12:35:05.000138+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
