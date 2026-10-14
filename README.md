# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T03:56:05.000127+00:00 · 22040 ticks

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

Today: 2890 decisions in 578 calls, $0.0404 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T03:56 | 0 / 1 / 4 | AMD 14% |  |
| Breezy | 2026-10-14T03:56 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-14T03:56 | 1 / 3 / 1 | COIN 77% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.02 | 3.02 | 0 | — | 2.51 | 1.26 | -5.18 | 1 |
| 2 | VWAP reversion · 1h | reversion | 101.89 | 1.89 | 43 | 41.9 | -9.01 | -2.66 | -13.79 | 119 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | Copy: Insider buying | copy | 101.72 | 1.72 | 18 | 50.0 | -15.68 | -2.48 | -21.97 | 75 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.41 | 1.42 | 12 | 41.7 | 5.68 | 1.72 | -7.55 | 43 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.31 | 1.31 | 7 | 57.1 | 4.71 | 2.08 | -3.27 | 17 |
| 7 | Hold SPY | benchmark | 100.95 | 0.95 | 0 | — | -0.20 | -0.08 | -3.71 | 1 |
| 8 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.53 | 0.53 | 8 | 62.5 | -3.51 | -1.14 | -9.74 | 25 |
| 9 | Copy: Congress Democrats (NANC) | copy | 100.32 | 0.32 | 0 | — | 0.23 | 0.16 | -3.55 | 1 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Hold BTC | benchmark | 99.83 | -0.17 | 0 | — | 31.17 | 3.58 | -8.68 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.75 | -0.25 | 0 | — | -2.37 | -1.30 | -5.09 | 1 |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.74 | -0.26 | 0 | — | 4.58 | 1.76 | -5.18 | 1 |
| 15 | Timing: Nasdaq FTD · TQQQ | daily | 98.87 | -1.13 | 0 | — | -8.34 | -1.50 | -15.27 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -2.56 | -2.76 | -3.51 | 21 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.31 | -1.69 | 0 | — | -5.15 | -2.35 | -5.50 | 1 |
| 18 | Day trade: Stocks in Play ORB | daytrade | 98.24 | -1.76 | 46 | 32.6 | 2.98 | 1.70 | -1.32 | 74 |
| 19 | Trend pullback · 1h | trend | 97.69 | -2.31 | 82 | 25.6 | -22.65 | -6.36 | -25.36 | 171 |
| 20 | Donchian 55/20 · 1h | breakout | 97.38 | -2.62 | 32 | 12.5 | 7.03 | 0.98 | -22.08 | 113 |
| 21 | Daily: Bullish score | daily | 97.28 | -2.72 | 5 | 0.0 | 0.45 | 0.25 | -12.76 | 12 |
| 22 | Agent (rotation) | meta | 96.71 | -3.29 | 88 | 31.8 | -7.02 | -2.86 | -8.69 | 309 |
| 23 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.84 | -0.42 | -17.67 | 39 |
| 24 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 25 | ADX DI cross · 1h | trend | 96.39 | -3.61 | 64 | 18.8 | -11.52 | -2.12 | -14.81 | 253 |
| 26 | Stochastic reversion · 1h | reversion | 96.16 | -3.84 | 107 | 51.4 | -14.16 | -2.74 | -16.23 | 343 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.69 | -4.31 | 0 | — | 5.91 | 1.05 | -8.36 | 1 |
| 28 | MACD cross · 1h | trend | 95.57 | -4.43 | 132 | 23.5 | -8.90 | -1.15 | -19.25 | 460 |
| 29 | Z-score reversion · 1h | reversion | 95.48 | -4.52 | 50 | 44.0 | 2.96 | 0.71 | -8.60 | 158 |
| 30 | EMA 20/50 cross · 1h | trend | 95.28 | -4.72 | 45 | 15.6 | 10.39 | 1.31 | -20.35 | 136 |
| 31 | Max aggression: 1-day momentum | meta | 95.27 | -4.73 | 12 | 33.3 | -11.24 | -0.27 | -37.31 | 42 |
| 32 | Agent | meta | 95.12 | -4.88 | 64 | 46.9 | -8.87 | -5.08 | -8.87 | 233 |
| 33 | Supertrend · 1h | trend | 94.01 | -5.99 | 60 | 13.3 | 2.36 | 0.49 | -20.32 | 213 |
| 34 | Squeeze breakout · 1h | breakout | 93.92 | -6.08 | 40 | 22.5 | 5.69 | 1.22 | -9.46 | 101 |
| 35 | Parabolic SAR · 1h | trend | 93.70 | -6.30 | 90 | 22.2 | 1.89 | 0.43 | -22.66 | 287 |
| 36 | Agent (aggressive) | meta | 93.22 | -6.78 | 32 | 37.5 | -1.97 | -0.62 | -5.61 | 111 |
| 37 | Gap and go | momentum | 93.18 | -6.82 | 62 | 11.3 | 8.62 | 2.18 | -6.70 | 199 |
| 38 | RSI momentum · 1h | momentum | 92.53 | -7.47 | 66 | 15.2 | 1.24 | 0.35 | -25.56 | 227 |
| 39 | MFI reversion · 1h | reversion | 92.45 | -7.55 | 165 | 31.5 | -8.80 | -1.38 | -17.02 | 129 |
| 40 | Connors RSI(2) · 1h | reversion | 91.93 | -8.07 | 127 | 42.5 | -19.97 | -5.86 | -22.90 | 254 |
| 41 | RSI(14) reversion · 1h | reversion | 91.48 | -8.52 | 37 | 32.4 | 6.10 | 1.39 | -9.40 | 127 |
| 42 | Ichimoku · 1h | trend | 91.21 | -8.79 | 48 | 16.7 | 2.06 | 0.44 | -22.34 | 124 |
| 43 | Agent (ML meta-label) | meta | 90.98 | -9.02 | 485 | 18.1 | -0.42 | 0.06 | -11.49 | 382 |
| 44 | Triple EMA stack · 1h | trend | 90.69 | -9.31 | 71 | 15.5 | -7.87 | -0.62 | -32.27 | 242 |
| 45 | Volume breakout · 1h | breakout | 90.64 | -9.36 | 75 | 22.7 | 8.60 | 1.31 | -12.60 | 120 |
| 46 | Bollinger breakout · 1h | breakout | 90.63 | -9.37 | 77 | 28.6 | 7.26 | 1.07 | -14.21 | 278 |
| 47 | Bollinger reversion · 1h | reversion | 89.94 | -10.06 | 97 | 37.1 | -23.78 | -5.71 | -24.98 | 321 |
| 48 | Williams %R · 1h | reversion | 89.34 | -10.66 | 143 | 45.5 | -27.96 | -4.74 | -29.58 | 510 |
| 49 | CCI reversion · 1h | reversion | 89.04 | -10.96 | 117 | 45.3 | -9.49 | -1.23 | -14.42 | 416 |
| 50 | Opening range 30m | breakout | 88.65 | -11.35 | 167 | 22.8 | -15.04 | -4.51 | -17.60 | 571 |
| 51 | OBV trend · 1h | momentum | 88.04 | -11.96 | 158 | 18.4 | -9.97 | -0.84 | -33.87 | 323 |
| 52 | MACD zero-line · 1h | trend | 87.51 | -12.49 | 69 | 17.4 | -22.00 | -4.27 | -22.71 | 228 |
| 53 | VWAP momentum · 1h | momentum | 87.48 | -12.52 | 328 | 22.9 | -33.57 | -4.98 | -40.76 | 1257 |
| 54 | Donchian 20/10 · 1h | breakout | 86.91 | -13.09 | 67 | 17.9 | 0.61 | 0.28 | -19.52 | 217 |
| 55 | Heikin-Ashi · 1h | trend | 86.74 | -13.26 | 165 | 26.7 | -29.87 | -4.89 | -38.65 | 677 |
| 56 | Max aggression: 5-day momentum | meta | 86.68 | -13.32 | 8 | 37.5 | -11.31 | -0.74 | -34.64 | 28 |
| 57 | EMA 9/21 cross · 1h | trend | 86.64 | -13.36 | 110 | 12.7 | -10.63 | -1.35 | -24.13 | 330 |
| 58 | Keltner breakout · 1h | breakout | 86.64 | -13.36 | 49 | 20.4 | -8.31 | -0.89 | -26.76 | 215 |
| 59 | Candlestick reversal · 1h | reversion | 86.52 | -13.48 | 141 | 31.2 | -29.69 | -5.74 | -30.32 | 475 |
| 60 | Three white soldiers | momentum | 86.16 | -13.84 | 165 | 18.2 | -47.70 | -22.13 | -47.72 | 584 |
| 61 | Opening range 15m | breakout | 85.93 | -14.07 | 204 | 21.1 | -18.29 | -4.99 | -20.83 | 698 |
| 62 | ROC + volume · 1h | momentum | 85.24 | -14.76 | 173 | 20.2 | -8.75 | -1.00 | -24.84 | 399 |
| 63 | ROC + volume | momentum | 70.97 | -29.03 | 455 | 22.4 | -73.04 | -16.30 | -75.13 | 1668 |
| 64 | Squeeze breakout | breakout | 67.66 | -32.34 | 377 | 15.4 | -62.24 | -17.73 | -62.46 | 1220 |
| 65 | Volume breakout | breakout | 67.48 | -32.52 | 295 | 14.2 | -61.92 | -17.38 | -62.06 | 889 |
| 66 | RSI(14) reversion | reversion | 67.30 | -32.70 | 461 | 27.5 | -73.70 | -16.90 | -74.07 | 1482 |
| 67 | EMA 20/50 cross | trend | 65.72 | -34.28 | 392 | 20.2 | -76.48 | -14.93 | -76.82 | 1440 |
| 68 | Donchian 55/20 | breakout | 64.18 | -35.83 | 387 | 17.1 | -68.85 | -14.37 | -70.28 | 1282 |
| 69 | VWAP reversion | reversion | 62.55 | -37.45 | 487 | 25.5 | -72.36 | -15.16 | -72.36 | 1400 |
| 70 | AI bee: Boozy | ai | 59.84 | -40.16 | 270 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 59.12 | -40.88 | 545 | 19.8 | -85.70 | -20.23 | -85.70 | 1913 |
| 72 | Keltner breakout | breakout | 58.49 | -41.51 | 529 | 14.6 | -83.17 | -26.64 | -83.17 | 1848 |
| 73 | Ichimoku | trend | 54.55 | -45.45 | 476 | 9.7 | -82.16 | -22.58 | -82.19 | 1720 |
| 74 | AI bee: Bizzy | ai | 53.36 | -46.64 | 953 | 8.5 | — | — | — | — |
| 75 | MFI reversion | reversion | 53.10 | -46.90 | 671 | 20.3 | -87.80 | -26.74 | -87.82 | 2111 |
| 76 | Z-score reversion | reversion | 52.35 | -47.65 | 622 | 23.2 | -86.20 | -21.79 | -86.21 | 2089 |
| 77 | ADX DI cross | trend | 51.42 | -48.58 | 650 | 10.5 | -89.27 | -33.12 | -89.27 | 2116 |
| 78 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.46 | -28.53 | -98.46 | 5300 |
| 79 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.29 | -29.19 | -93.31 | 2609 |
| 80 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.25 | -24.32 | -90.25 | 2368 |
| 81 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.71 | -26.49 | -91.72 | 2361 |
| 82 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.32 | -31.48 | -97.33 | 3530 |
| 83 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -34.68 | -96.48 | 3600 |
| 84 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.44 | -25.01 | -94.44 | 2639 |
| 85 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -34.82 | -99.36 | 5639 |
| 86 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -90.85 | -25.23 | -90.87 | 2633 |
| 87 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.35 | -30.33 | -96.35 | 3595 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -39.51 | -99.72 | 6168 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.46 | -28.92 | -91.47 | 2359 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -35.76 | -97.36 | 3671 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -34.57 | -98.51 | 4672 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.35 | -31.47 | -93.36 | 2797 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.34 | -99.54 | 6123 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -31.22 | -96.00 | 3742 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.67 | -32.53 | -95.67 | 4044 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.36 | -99.89 | 8214 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T03:55 | Volume breakout | sell | XRP-USD | 16.78 | -0.14 | exit signal |
| 2026-10-14T03:48 | AI bee: Boozy | sell | ETH-USD | 13.53 | -0.09 | Jev: buy |
| 2026-10-14T03:45 | AI bee: Bizzy | sell | SOL-USD | 7.78 | -0.05 | Jev: sell (sell p=0.77) after 10 min |
| 2026-10-14T03:40 | Supertrend | buy | XRP-USD | 2.95 | — | rebalance up |
| 2026-10-14T03:40 | Supertrend | sell | ETH-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-14T03:36 | Keltner breakout | buy | XRP-USD | 2.93 | — | rebalance up |
| 2026-10-14T03:36 | Keltner breakout | sell | BTC-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-14T03:35 | AI bee: Bizzy | buy | SOL-USD | 7.84 | — | Jev: buy (buy p=0.59) |
| 2026-10-14T03:35 | Volume breakout | buy | XRP-USD | 16.92 | — | entry signal |
| 2026-10-14T03:35 | Volume breakout | buy | ETH-USD | 16.92 | — | entry signal |
| 2026-10-14T03:35 | Keltner breakout | buy | XRP-USD | 8.81 | — | entry signal |
| 2026-10-14T03:35 | Keltner breakout | buy | SOL-USD | 11.75 | — | entry signal |
| 2026-10-14T03:35 | Keltner breakout | buy | ETH-USD | 11.75 | — | entry signal |
| 2026-10-14T03:35 | Keltner breakout | buy | DOGE-USD | 11.75 | — | entry signal |
| 2026-10-14T03:35 | Donchian 55/20 | buy | SOL-USD | 16.08 | — | entry signal |
| 2026-10-14T03:35 | Donchian 55/20 | buy | BTC-USD | 16.08 | — | entry signal |
| 2026-10-14T03:35 | ROC + volume | buy | XRP-USD | 17.81 | — | entry signal |
| 2026-10-14T03:35 | ROC + volume | buy | ETH-USD | 17.81 | — | entry signal |
| 2026-10-14T03:35 | ROC + volume | buy | BTC-USD | 17.81 | — | entry signal |
| 2026-10-14T03:35 | Supertrend | buy | XRP-USD | 5.97 | — | entry signal |
| 2026-10-14T03:35 | Supertrend | buy | SOL-USD | 11.86 | — | entry signal |
| 2026-10-14T03:35 | Supertrend | sell | BTC-USD | 2.96 | -0.01 | rebalance down |
| 2026-10-14T03:33 | AI bee: Boozy | buy | ETH-USD | 13.61 | — | Jev: buy (buy p=0.78) |
| 2026-10-14T03:13 | AI bee: Boozy | sell | ETH-USD | 13.61 | -0.09 | Jev: buy |
| 2026-10-14T03:12 | AI bee: Bizzy | sell | BTC-USD | 8.49 | -0.06 | Jev: sell (sell p=0.59) after 10 min |
| 2026-10-14T03:05 | AI bee: Bizzy | sell | SOL-USD | 7.58 | -0.05 | Jev: sell (sell p=0.57) after 11 min |
| 2026-10-14T03:05 | Supertrend | buy | DOGE-USD | 14.81 | — | entry |
| 2026-10-14T03:02 | AI bee: Bizzy | buy | BTC-USD | 8.55 | — | Jev: buy (buy p=0.64) |
| 2026-10-14T03:02 | AI bee: Bizzy | sell | DOGE-USD | 7.90 | -0.03 | Jev: sell (sell p=0.53) after 17 min |
| 2026-10-14T03:00 | VWAP momentum · 1h | buy | XRP-USD | 2.33 | — | entry signal |
| 2026-10-14T03:00 | VWAP momentum · 1h | buy | ETH-USD | 5.47 | — | entry signal |
| 2026-10-14T03:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.47 | — | entry signal |
| 2026-10-14T03:00 | VWAP momentum · 1h | buy | BTC-USD | 5.47 | — | entry signal |
| 2026-10-14T03:00 | ADX DI cross · 1h | buy | DOGE-USD | 7.75 | — | entry signal |
| 2026-10-14T03:00 | MACD zero-line · 1h | buy | DOGE-USD | 21.06 | — | entry signal |
| 2026-10-14T03:00 | MACD cross · 1h | buy | BTC-USD | 3.63 | — | entry signal |
| 2026-10-14T03:00 | Squeeze breakout | buy | ETH-USD | 16.92 | — | entry signal |
| 2026-10-14T03:00 | Squeeze breakout | buy | DOGE-USD | 16.92 | — | entry signal |
| 2026-10-14T03:00 | Ichimoku | buy | ETH-USD | 13.64 | — | entry signal |
| 2026-10-14T03:00 | Ichimoku | buy | DOGE-USD | 13.64 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 03:56:05.000127+00:00 -> 2026-10-14 04:06:05.000127+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
