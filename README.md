# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T20:57:05.000117+00:00 · 20567 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.28 (-4.72%)

Closed trades 59, win rate 49.2%, fees £2.28, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-12)

**Uptrend** since 2026-09-21 · level caution · 3 distribution days in 25 sessions · timing exposure 75% · VXN 20.55 · VIX 15.24 · last follow-through day 2026-08-04

Best bullish scores: MSFT 9.0, PLTR 8.0, AMZN 6.2, META 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 33132 decisions in 2928 calls, $0.4127 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T20:57 | 0 / 0 / 5 | PLTR 15%, AMD 15% |  |
| Breezy | 2026-10-12T20:57 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-12T20:57 | 1 / 4 / 0 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.95 | 2.95 | 0 | — | 1.61 | 0.84 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.12 | 2.12 | 40 | 42.5 | -8.66 | -2.64 | -13.79 | 118 |
| 3 | Copy: Insider buying | copy | 102.09 | 2.08 | 16 | 50.0 | -12.87 | -2.14 | -20.64 | 71 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Hold SPY | benchmark | 101.46 | 1.46 | 0 | — | 0.73 | 0.48 | -3.66 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.11 | -3.27 | 17 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.25 | 1.25 | 0 | — | 1.71 | 0.84 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.68 | 0.68 | 0 | — | -5.03 | -0.83 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.65 | 0.66 | 0 | — | -1.20 | -0.63 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.52 | 0.52 | 7 | 57.1 | -3.92 | -1.31 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.31 | 0.31 | 11 | 36.4 | 4.54 | 1.44 | -7.55 | 43 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 100.15 | 0.15 | 0 | — | 3.58 | 1.41 | -5.18 | 1 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.58 | -0.42 | 0 | — | -4.71 | -2.19 | -5.36 | 1 |
| 16 | Hold BTC | benchmark | 99.51 | -0.49 | 0 | — | 30.13 | 3.57 | -8.68 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.66 | -1.80 | 78 |
| 18 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.80 | -3.51 | 21 |
| 19 | Donchian 55/20 · 1h | breakout | 98.26 | -1.74 | 31 | 12.9 | 12.04 | 1.46 | -18.79 | 113 |
| 20 | Daily: Bullish score | daily | 98.17 | -1.83 | 4 | 0.0 | 1.29 | 0.36 | -12.76 | 11 |
| 21 | Max aggression: 1-day momentum | meta | 98.04 | -1.96 | 11 | 36.4 | -16.71 | -0.63 | -37.31 | 42 |
| 22 | Trend pullback · 1h | trend | 97.90 | -2.10 | 78 | 23.1 | -23.01 | -6.47 | -25.60 | 168 |
| 23 | Stochastic reversion · 1h | reversion | 97.60 | -2.40 | 96 | 53.1 | -11.78 | -2.31 | -14.02 | 342 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.63 | -4.53 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.07 | -2.93 | 44 | 43.2 | 3.79 | 0.89 | -8.60 | 160 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 97.06 | -2.94 | 0 | — | 9.02 | 1.51 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.17 | -0.32 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.50 | -3.50 | 62 | 19.4 | -6.17 | -0.99 | -13.79 | 254 |
| 29 | Agent (rotation) | meta | 96.43 | -3.57 | 84 | 31.0 | -5.85 | -2.49 | -7.50 | 309 |
| 30 | MACD cross · 1h | trend | 95.87 | -4.13 | 125 | 24.0 | -11.44 | -1.80 | -17.79 | 461 |
| 31 | Parabolic SAR · 1h | trend | 95.38 | -4.62 | 86 | 22.1 | 1.20 | 0.35 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.37 | -4.63 | 45 | 15.6 | 4.61 | 0.72 | -23.71 | 137 |
| 33 | Agent | meta | 95.28 | -4.72 | 59 | 49.2 | -7.96 | -3.86 | -8.72 | 232 |
| 34 | Supertrend · 1h | trend | 94.59 | -5.41 | 58 | 13.8 | 1.32 | 0.36 | -18.92 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.46 | 2.17 | -6.21 | 200 |
| 36 | Squeeze breakout · 1h | breakout | 93.52 | -6.48 | 39 | 23.1 | 15.62 | 2.48 | -9.46 | 105 |
| 37 | MFI reversion · 1h | reversion | 93.48 | -6.52 | 151 | 32.5 | -7.75 | -1.18 | -16.91 | 128 |
| 38 | Agent (aggressive) | meta | 93.15 | -6.85 | 30 | 36.7 | -6.25 | -2.77 | -6.47 | 114 |
| 39 | RSI momentum · 1h | momentum | 92.64 | -7.36 | 66 | 15.2 | -0.63 | 0.13 | -23.02 | 229 |
| 40 | Connors RSI(2) · 1h | reversion | 92.55 | -7.45 | 115 | 43.5 | -18.87 | -6.28 | -21.22 | 256 |
| 41 | Agent (ML meta-label) | meta | 92.53 | -7.47 | 439 | 17.8 | 2.91 | 0.63 | -12.47 | 398 |
| 42 | RSI(14) reversion · 1h | reversion | 92.14 | -7.86 | 31 | 29.0 | 2.33 | 0.64 | -9.03 | 127 |
| 43 | Volume breakout · 1h | breakout | 91.74 | -8.26 | 70 | 20.0 | 9.08 | 1.39 | -12.60 | 117 |
| 44 | Bollinger reversion · 1h | reversion | 91.67 | -8.33 | 83 | 37.3 | -23.05 | -5.76 | -24.24 | 316 |
| 45 | Ichimoku · 1h | trend | 91.04 | -8.96 | 48 | 16.7 | 0.43 | 0.26 | -22.34 | 128 |
| 46 | Bollinger breakout · 1h | breakout | 90.89 | -9.11 | 74 | 28.4 | 8.33 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.74 | -9.26 | 71 | 15.5 | -7.55 | -0.67 | -27.17 | 239 |
| 48 | Williams %R · 1h | reversion | 89.67 | -10.33 | 132 | 46.2 | -25.68 | -4.32 | -27.71 | 506 |
| 49 | Opening range 30m | breakout | 89.46 | -10.54 | 154 | 22.1 | -15.64 | -4.74 | -16.08 | 569 |
| 50 | CCI reversion · 1h | reversion | 89.13 | -10.87 | 111 | 45.9 | -10.06 | -1.35 | -14.35 | 407 |
| 51 | OBV trend · 1h | momentum | 88.74 | -11.26 | 150 | 18.7 | -13.03 | -1.26 | -34.14 | 319 |
| 52 | Candlestick reversal · 1h | reversion | 88.51 | -11.49 | 127 | 31.5 | -27.61 | -5.32 | -28.12 | 491 |
| 53 | VWAP momentum · 1h | momentum | 88.28 | -11.72 | 311 | 23.2 | -33.38 | -5.01 | -40.22 | 1255 |
| 54 | Max aggression: 5-day momentum | meta | 88.13 | -11.87 | 7 | 28.6 | -14.35 | -1.05 | -34.64 | 28 |
| 55 | Donchian 20/10 · 1h | breakout | 87.74 | -12.26 | 63 | 17.5 | -0.60 | 0.13 | -19.51 | 214 |
| 56 | Heikin-Ashi · 1h | trend | 87.73 | -12.27 | 153 | 28.1 | -30.61 | -5.11 | -37.65 | 678 |
| 57 | MACD zero-line · 1h | trend | 87.62 | -12.38 | 67 | 17.9 | -22.05 | -4.12 | -22.12 | 236 |
| 58 | EMA 9/21 cross · 1h | trend | 87.13 | -12.87 | 108 | 13.0 | -8.23 | -0.86 | -23.06 | 332 |
| 59 | Opening range 15m | breakout | 86.73 | -13.27 | 182 | 20.3 | -18.28 | -5.07 | -19.42 | 691 |
| 60 | Keltner breakout · 1h | breakout | 86.68 | -13.32 | 45 | 20.0 | -11.09 | -1.21 | -26.77 | 215 |
| 61 | Three white soldiers | momentum | 86.57 | -13.43 | 152 | 17.1 | -48.55 | -23.61 | -48.61 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.55 | -14.45 | 164 | 20.1 | -9.06 | -1.05 | -25.01 | 401 |
| 63 | ROC + volume | momentum | 72.75 | -27.25 | 417 | 22.5 | -72.79 | -16.58 | -74.48 | 1658 |
| 64 | RSI(14) reversion | reversion | 70.74 | -29.26 | 416 | 26.7 | -72.64 | -17.95 | -72.67 | 1467 |
| 65 | Squeeze breakout | breakout | 69.90 | -30.10 | 349 | 15.8 | -62.09 | -18.14 | -62.20 | 1223 |
| 66 | Volume breakout | breakout | 69.62 | -30.39 | 277 | 14.8 | -61.64 | -17.57 | -61.69 | 894 |
| 67 | EMA 20/50 cross | trend | 67.95 | -32.05 | 353 | 20.1 | -76.26 | -15.13 | -76.27 | 1431 |
| 68 | Donchian 55/20 | breakout | 66.89 | -33.11 | 358 | 17.6 | -68.12 | -14.43 | -69.01 | 1291 |
| 69 | VWAP reversion | reversion | 65.57 | -34.43 | 455 | 25.7 | -71.32 | -15.83 | -71.42 | 1400 |
| 70 | Keltner breakout | breakout | 60.63 | -39.37 | 480 | 14.8 | -83.16 | -27.39 | -83.17 | 1836 |
| 71 | Supertrend | trend | 60.44 | -39.56 | 498 | 19.5 | -86.00 | -21.09 | -86.04 | 1894 |
| 72 | AI bee: Boozy | ai | 60.33 | -39.66 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.28 | -42.72 | 434 | 9.9 | -82.15 | -23.20 | -82.17 | 1733 |
| 74 | Z-score reversion | reversion | 55.80 | -44.20 | 563 | 22.2 | -85.66 | -23.22 | -85.69 | 2065 |
| 75 | AI bee: Bizzy | ai | 55.48 | -44.52 | 889 | 8.3 | — | — | — | — |
| 76 | MFI reversion | reversion | 55.47 | -44.53 | 618 | 19.6 | -87.88 | -28.41 | -87.94 | 2113 |
| 77 | ADX DI cross | trend | 53.81 | -46.19 | 594 | 10.1 | -89.09 | -34.70 | -89.13 | 2104 |
| 78 | Donchian 20/10 | breakout | 52.15 | -47.85 | 679 | 17.7 | -90.85 | -26.10 | -90.88 | 2644 |
| 79 | MACD zero-line | trend | 51.22 | -48.78 | 630 | 14.6 | -91.46 | -30.08 | -91.48 | 2347 |
| 80 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.62 | -31.15 | -98.62 | 5333 |
| 81 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.22 | -26.67 | -91.22 | 2324 |
| 82 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.21 | -30.33 | -93.21 | 2601 |
| 83 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -25.75 | -90.52 | 2363 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.37 | -33.45 | -97.37 | 3522 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -36.31 | -96.39 | 3588 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.23 | -25.61 | -94.23 | 2621 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.21 | -99.36 | 5627 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -31.67 | -96.31 | 3593 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -42.48 | -99.73 | 6151 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.32 | -38.47 | -97.32 | 3659 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.52 | -98.49 | 4660 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.35 | -33.02 | -93.37 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.60 | -99.53 | 6101 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -33.60 | -95.90 | 3724 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -34.82 | -95.70 | 4048 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.34 | -99.89 | 8206 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T20:40 | EMA 20/50 cross | buy | SOL-USD | 17.00 | — | entry signal |
| 2026-10-12T20:30 | EMA 20/50 cross | buy | ETH-USD | 17.01 | — | entry signal |
| 2026-10-12T20:18 | AI bee: Bizzy | sell | SOL-USD | 7.96 | -0.03 | Jev: sell (sell p=0.53) after 13 min |
| 2026-10-12T20:15 | EMA 20/50 cross | buy | DOGE-USD | 17.01 | — | entry signal |
| 2026-10-12T20:10 | MFI reversion | sell | SOL-USD | 13.87 | 0.02 | exit signal |
| 2026-10-12T20:10 | Keltner breakout | buy | XRP-USD | 9.13 | — | entry signal |
| 2026-10-12T20:10 | Keltner breakout | buy | ETH-USD | 12.15 | — | entry signal |
| 2026-10-12T20:10 | Keltner breakout | sell | SOL-USD | 3.04 | -0.01 | rebalance down |
| 2026-10-12T20:10 | Keltner breakout | sell | BTC-USD | 3.04 | -0.01 | rebalance down |
| 2026-10-12T20:10 | Donchian 55/20 | buy | DOGE-USD | 16.75 | — | entry signal |
| 2026-10-12T20:10 | Donchian 55/20 | buy | BTC-USD | 16.75 | — | entry signal |
| 2026-10-12T20:10 | ROC + volume | buy | DOGE-USD | 18.20 | — | entry signal |
| 2026-10-12T20:10 | ROC + volume | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-10-12T20:05 | AI bee: Bizzy | buy | SOL-USD | 7.99 | — | Jev: buy (buy p=0.58) |
| 2026-10-12T20:05 | Keltner breakout | buy | DOGE-USD | 15.18 | — | entry signal |
| 2026-10-12T20:05 | Ichimoku | buy | DOGE-USD | 14.32 | — | entry signal |
| 2026-10-12T20:05 | EMA 20/50 cross | buy | BTC-USD | 17.02 | — | entry signal |
| 2026-10-12T20:00 | Williams %R · 1h | buy | ETH-USD | 13.23 | — | entry signal |
| 2026-10-12T20:00 | Williams %R · 1h | buy | DOGE-USD | 17.93 | — | entry signal |
| 2026-10-12T20:00 | Stochastic reversion · 1h | buy | BTC-USD | 10.76 | — | entry |
| 2026-10-12T20:00 | Stochastic reversion · 1h | sell | SOL-USD | 5.38 | -0.00 | rebalance down |
| 2026-10-12T20:00 | Stochastic reversion · 1h | sell | DOGE-USD | 5.38 | -0.01 | rebalance down |
| 2026-10-12T20:00 | Volume breakout | buy | DOGE-USD | 17.39 | — | entry signal |
| 2026-10-12T19:56 | Agent (rotation) | sell | SQQQ | 64.37 | 0.24 | selected signal exited |
| 2026-10-12T19:56 | Day trade: Noise-area momentum · TQQQ/SQQQ | sell | SQQQ | 101.31 | 0.28 | target is flat |
| 2026-10-12T19:56 | Day trade: Open breakout · TQQQ/SQQQ | sell | SQQQ | 100.52 | 0.05 | target is flat |
| 2026-10-12T19:56 | Day trade: Last half hour · TQQQ/SQQQ | sell | SQQQ | 98.81 | -0.25 | target is flat |
| 2026-10-12T19:56 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 100.31 | 0.74 | target is flat |
| 2026-10-12T19:56 | Agent (aggressive) | sell | TNA | 46.50 | -0.25 | selected signal exited |
| 2026-10-12T19:56 | Agent | sell | TNA | 18.99 | -0.10 | selected signal exited |
| 2026-10-12T19:56 | MFI reversion · 1h | buy | NVDA | 18.55 | — | entry |
| 2026-10-12T19:56 | MFI reversion · 1h | buy | BITX | 18.63 | — | entry |
| 2026-10-12T19:56 | MFI reversion · 1h | sell | SOXL | 23.30 | -0.04 | target is flat |
| 2026-10-12T19:56 | MFI reversion · 1h | sell | QQQ | 4.68 | -0.00 | rebalance down |
| 2026-10-12T19:56 | Volume breakout · 1h | buy | MSFT | 22.92 | — | entry |
| 2026-10-12T19:56 | ROC + volume · 1h | buy | PLTR | 12.21 | — | entry |
| 2026-10-12T19:56 | ROC + volume · 1h | sell | AMZN | 12.21 | -0.01 | target is flat |
| 2026-10-12T19:56 | VWAP momentum · 1h | buy | BITX | 17.65 | — | entry |
| 2026-10-12T19:56 | VWAP momentum · 1h | sell | SQQQ | 4.43 | -0.00 | rebalance down |
| 2026-10-12T19:56 | VWAP momentum · 1h | sell | AMD | 4.41 | 0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 20:57:05.000117+00:00 -> 2026-10-12 21:07:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
