# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T01:25:05.000152+00:00 · 21916 ticks

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

**Uptrend** since 2026-09-21 · level caution · 4 distribution days in 25 sessions · timing exposure 75% · VXN 20.84 · VIX 15.21 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.0, MSFT 7.9, BITX 6.5, META 6.1, MSTR 6.0, UPRO 5.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 1035 decisions in 207 calls, $0.0145 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T01:25 | 2 / 3 / 0 | SOL-USD 15%, AMD 14% |  |
| Breezy | 2026-10-14T01:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T01:25 | 5 / 0 / 0 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.13 | 3.13 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.12 | -2.70 | -13.79 | 117 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.43 | 1.44 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 101.06 | 1.05 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.42 | 0.42 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.84 | -0.16 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.83 | -0.17 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Hold BTC | benchmark | 99.46 | -0.54 | 0 | — | 31.01 | 3.57 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.95 | -1.05 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.41 | -1.58 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.80 | -2.20 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.48 | -2.52 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.38 | -2.62 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.12 | -2.89 | -8.90 | 308 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.45 | -3.55 | 64 | 18.8 | -10.99 | -2.01 | -14.81 | 249 |
| 26 | Stochastic reversion · 1h | reversion | 96.26 | -3.74 | 107 | 51.4 | -14.39 | -2.78 | -16.43 | 344 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.79 | -4.21 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.58 | -4.42 | 132 | 23.5 | -8.96 | -1.16 | -19.25 | 459 |
| 29 | Z-score reversion · 1h | reversion | 95.49 | -4.51 | 50 | 44.0 | 2.87 | 0.70 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.38 | -4.62 | 45 | 15.6 | 9.62 | 1.22 | -19.71 | 139 |
| 31 | Max aggression: 1-day momentum | meta | 95.37 | -4.63 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.95 | -5.12 | -8.95 | 234 |
| 33 | Supertrend · 1h | trend | 94.01 | -5.99 | 60 | 13.3 | 2.24 | 0.47 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.94 | -6.06 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.77 | -6.23 | 90 | 22.2 | 1.66 | 0.40 | -22.66 | 288 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.62 | -0.50 | -5.61 | 112 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.63 | -7.37 | 66 | 15.2 | 0.87 | 0.31 | -25.56 | 228 |
| 39 | MFI reversion · 1h | reversion | 92.54 | -7.46 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 130 |
| 40 | Connors RSI(2) · 1h | reversion | 92.03 | -7.97 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.49 | -8.51 | 37 | 32.4 | 6.10 | 1.39 | -9.40 | 125 |
| 42 | Ichimoku · 1h | trend | 91.31 | -8.69 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 91.07 | -8.93 | 485 | 18.1 | -2.45 | -0.33 | -12.37 | 368 |
| 44 | Triple EMA stack · 1h | trend | 90.71 | -9.29 | 71 | 15.5 | -7.63 | -0.59 | -32.27 | 242 |
| 45 | Volume breakout · 1h | breakout | 90.68 | -9.32 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.68 | -9.32 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 90.02 | -9.98 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.43 | -10.57 | 143 | 45.5 | -28.13 | -4.76 | -30.00 | 511 |
| 49 | CCI reversion · 1h | reversion | 89.01 | -10.99 | 117 | 45.3 | -9.57 | -1.24 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.11 | -11.89 | 158 | 18.4 | -9.96 | -0.84 | -33.87 | 324 |
| 52 | MACD zero-line · 1h | trend | 87.63 | -12.37 | 69 | 17.4 | -21.93 | -4.25 | -22.68 | 227 |
| 53 | VWAP momentum · 1h | momentum | 87.60 | -12.40 | 327 | 22.9 | -34.03 | -5.07 | -40.73 | 1255 |
| 54 | Donchian 20/10 · 1h | breakout | 87.00 | -13.00 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Heikin-Ashi · 1h | trend | 86.78 | -13.22 | 165 | 26.7 | -30.38 | -4.99 | -38.65 | 679 |
| 56 | Max aggression: 5-day momentum | meta | 86.77 | -13.23 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | Keltner breakout · 1h | breakout | 86.69 | -13.31 | 49 | 20.4 | -8.10 | -0.87 | -26.76 | 214 |
| 58 | EMA 9/21 cross · 1h | trend | 86.68 | -13.32 | 110 | 12.7 | -10.07 | -1.27 | -24.13 | 327 |
| 59 | Candlestick reversal · 1h | reversion | 86.54 | -13.46 | 141 | 31.2 | -28.55 | -5.53 | -29.14 | 468 |
| 60 | Three white soldiers | momentum | 86.19 | -13.81 | 165 | 18.2 | -47.71 | -22.15 | -47.74 | 584 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.33 | -14.67 | 173 | 20.2 | -8.86 | -1.01 | -24.84 | 400 |
| 63 | ROC + volume | momentum | 71.23 | -28.77 | 455 | 22.4 | -73.06 | -16.32 | -75.01 | 1669 |
| 64 | Squeeze breakout | breakout | 67.81 | -32.19 | 377 | 15.4 | -62.23 | -17.69 | -62.30 | 1218 |
| 65 | Volume breakout | breakout | 67.70 | -32.30 | 294 | 14.3 | -61.97 | -17.43 | -61.97 | 891 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.69 | -16.90 | -74.06 | 1482 |
| 67 | EMA 20/50 cross | trend | 65.79 | -34.21 | 392 | 20.2 | -76.47 | -14.92 | -76.76 | 1437 |
| 68 | Donchian 55/20 | breakout | 64.32 | -35.68 | 387 | 17.1 | -68.85 | -14.37 | -70.21 | 1281 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -71.94 | -14.95 | -72.01 | 1388 |
| 70 | AI bee: Boozy | ai | 60.01 | -39.98 | 268 | 4.9 | — | — | — | — |
| 71 | Supertrend | trend | 59.34 | -40.66 | 545 | 19.8 | -85.67 | -20.17 | -85.67 | 1909 |
| 72 | Keltner breakout | breakout | 58.75 | -41.25 | 529 | 14.6 | -83.16 | -26.52 | -83.16 | 1846 |
| 73 | Ichimoku | trend | 54.67 | -45.33 | 476 | 9.7 | -82.31 | -22.68 | -82.31 | 1722 |
| 74 | AI bee: Bizzy | ai | 53.63 | -46.37 | 947 | 8.6 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.10 | -46.90 | 671 | 20.3 | -87.81 | -26.74 | -87.83 | 2112 |
| 76 | Z-score reversion | reversion | 52.35 | -47.65 | 622 | 23.2 | -86.20 | -21.79 | -86.21 | 2089 |
| 77 | ADX DI cross | trend | 51.60 | -48.40 | 648 | 10.5 | -89.25 | -32.96 | -89.25 | 2117 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.42 | -28.22 | -98.43 | 5290 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.34 | -29.31 | -93.34 | 2609 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.28 | -24.33 | -90.29 | 2368 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.71 | -26.43 | -91.71 | 2360 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.29 | -31.25 | -97.30 | 3522 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -34.68 | -96.48 | 3592 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -25.02 | -94.44 | 2638 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -34.60 | -99.36 | 5631 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.84 | -25.13 | -90.85 | 2632 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -30.29 | -96.34 | 3594 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.22 | -99.72 | 6162 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.42 | -28.79 | -91.42 | 2353 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.37 | -35.67 | -97.37 | 3668 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -34.46 | -98.51 | 4670 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.36 | -31.46 | -93.36 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.22 | -99.54 | 6123 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -31.17 | -96.00 | 3741 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.50 | -95.67 | 4044 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.90 | -99.89 | 8216 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T01:25 | AI bee: Bizzy | buy | SOL-USD | 7.80 | — | Jev: buy (buy p=0.58) |
| 2026-10-14T01:25 | ADX DI cross | buy | XRP-USD | 12.91 | — | entry signal |
| 2026-10-14T01:10 | ADX DI cross | sell | XRP-USD | 12.88 | -0.08 | exit signal |
| 2026-10-14T01:10 | ADX DI cross | sell | BTC-USD | 12.87 | -0.09 | exit signal |
| 2026-10-14T01:10 | EMA 20/50 cross | sell | DOGE-USD | 13.15 | -0.13 | stop-loss |
| 2026-10-14T01:05 | Donchian 55/20 | sell | SOL-USD | 12.84 | -0.14 | stop-loss |
| 2026-10-14T01:05 | Ichimoku | sell | XRP-USD | 13.67 | -0.10 | exit signal |
| 2026-10-14T01:05 | ADX DI cross | sell | ETH-USD | 12.87 | -0.09 | exit signal |
| 2026-10-14T01:05 | Supertrend | sell | XRP-USD | 14.81 | -0.12 | exit signal |
| 2026-10-14T01:05 | Supertrend | sell | SOL-USD | 11.87 | -0.09 | exit signal |
| 2026-10-14T01:05 | Supertrend | sell | BTC-USD | 14.84 | -0.10 | exit signal |
| 2026-10-14T01:05 | EMA 20/50 cross | sell | XRP-USD | 13.17 | -0.12 | stop-loss |
| 2026-10-14T01:05 | EMA 20/50 cross | sell | SOL-USD | 13.15 | -0.14 | stop-loss |
| 2026-10-14T01:05 | EMA 20/50 cross | sell | BTC-USD | 13.18 | -0.11 | stop-loss |
| 2026-10-14T01:00 | Candlestick reversal · 1h | buy | SOL-USD | 7.87 | — | entry signal |
| 2026-10-14T01:00 | VWAP momentum · 1h | sell | ETH-USD | 6.24 | -0.04 | exit signal |
| 2026-10-14T01:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.27 | -0.00 | exit signal |
| 2026-10-14T01:00 | ADX DI cross · 1h | buy | SOL-USD | 13.78 | — | entry signal |
| 2026-10-14T01:00 | Three white soldiers | sell | XRP-USD | 21.58 | -0.06 | exit signal |
| 2026-10-14T01:00 | Three white soldiers | sell | BTC-USD | 21.53 | -0.11 | exit signal |
| 2026-10-14T01:00 | Volume breakout | sell | SOL-USD | 16.96 | -0.05 | exit signal |
| 2026-10-14T01:00 | Donchian 55/20 | sell | DOGE-USD | 12.88 | -0.12 | stop-loss |
| 2026-10-14T01:00 | ROC + volume | sell | SOL-USD | 17.80 | -0.09 | stop-loss |
| 2026-10-14T01:00 | Ichimoku | sell | DOGE-USD | 13.69 | -0.08 | exit signal |
| 2026-10-14T01:00 | Supertrend | buy | XRP-USD | 5.93 | — | rebalance up |
| 2026-10-14T01:00 | Supertrend | buy | BTC-USD | 2.99 | — | rebalance up |
| 2026-10-14T01:00 | Supertrend | sell | ETH-USD | 11.88 | -0.08 | exit signal |
| 2026-10-14T01:00 | Supertrend | sell | DOGE-USD | 11.87 | -0.09 | exit signal |
| 2026-10-14T00:55 | Keltner breakout | sell | ETH-USD | 14.66 | -0.10 | stop-loss |
| 2026-10-14T00:55 | Donchian 55/20 | sell | ETH-USD | 16.08 | -0.15 | stop-loss |
| 2026-10-14T00:55 | Ichimoku | sell | ETH-USD | 13.63 | -0.13 | stop-loss |
| 2026-10-14T00:55 | EMA 20/50 cross | sell | ETH-USD | 13.14 | -0.10 | stop-loss |
| 2026-10-14T00:53 | EMA 20/50 cross | buy | ETH-USD | 3.30 | — | rebalance up |
| 2026-10-14T00:53 | EMA 20/50 cross | sell | SOL-USD | 3.30 | -0.02 | rebalance down |
| 2026-10-14T00:52 | EMA 20/50 cross | buy | ETH-USD | 3.30 | — | rebalance up |
| 2026-10-14T00:52 | EMA 20/50 cross | sell | XRP-USD | 3.30 | -0.02 | rebalance down |
| 2026-10-14T00:50 | AI bee: Boozy | sell | ETH-USD | 13.70 | -0.08 | Jev: buy |
| 2026-10-14T00:50 | Three white soldiers | sell | SOL-USD | 21.46 | -0.21 | stop-loss |
| 2026-10-14T00:50 | Volume breakout | sell | XRP-USD | 16.86 | -0.17 | stop-loss |
| 2026-10-14T00:50 | Volume breakout | sell | DOGE-USD | 16.89 | -0.14 | exit signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 01:25:05.000152+00:00 -> 2026-10-14 01:35:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
