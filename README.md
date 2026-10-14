# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-14T15:25:05.000126+00:00 · 22592 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £94.26 (-5.74%)

Closed trades 65, win rate 46.2%, fees £2.41, max drawdown -6.17%.

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

Today: 17830 decisions in 2234 calls, $0.2315 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-14T15:25 | 5 / 15 / 10 | cash |  |
| Breezy | 2026-10-14T15:25 | 0 / 28 / 2 | cash |  |
| Boozy | 2026-10-14T15:25 | 3 / 25 / 2 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | PLTR | 2.37 | +3.06% | 4 |
| Donchian 20/10 | LABU | 2.03 | +5.76% | 5 |
| MACD zero-line | LABU | 1.82 | +5.51% | 3 |
| Z-score reversion | GOOGL | 1.73 | +0.66% | 5 |
| Keltner breakout | LABU | 1.69 | +7.27% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 103.87 | 3.87 | 0 | — | 2.81 | 1.41 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.42 | 2.42 | 18 | 50.0 | -15.67 | -2.50 | -21.97 | 76 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 101.81 | 1.81 | 0 | — | 5.27 | 2.01 | -5.18 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | VWAP reversion · 1h | reversion | 101.65 | 1.65 | 44 | 40.9 | -8.24 | -2.47 | -13.79 | 113 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.40 | 1.40 | 8 | 62.5 | 4.25 | 1.89 | -3.27 | 19 |
| 7 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.98 | -7.55 | 43 |
| 8 | Hold SPY | benchmark | 100.91 | 0.91 | 0 | — | -0.64 | -0.34 | -3.58 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.73 | 0.73 | 8 | 62.5 | -4.78 | -1.65 | -9.84 | 26 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Copy: Congress Democrats (NANC) | copy | 99.99 | -0.01 | 0 | — | -0.85 | -0.33 | -3.47 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 99.40 | -0.60 | 0 | — | -4.48 | -2.61 | -5.09 | 1 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.06 | -0.94 | 0 | — | -5.15 | -2.37 | -5.50 | 1 |
| 15 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.81 | -1.19 | 8 | 25.0 | -3.21 | -3.73 | -3.51 | 20 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.02 | -2.07 | 67 |
| 17 | Hold BTC | benchmark | 98.29 | -1.71 | 0 | — | 28.85 | 3.37 | -8.68 | 1 |
| 18 | Trend pullback · 1h | trend | 97.03 | -2.97 | 86 | 24.4 | -24.78 | -7.05 | -25.54 | 169 |
| 19 | Max aggression: 1-day momentum | meta | 97.02 | -2.98 | 13 | 38.5 | -8.23 | -0.07 | -37.31 | 42 |
| 20 | Donchian 55/20 · 1h | breakout | 96.93 | -3.07 | 34 | 14.7 | 5.76 | 0.85 | -22.08 | 114 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 96.67 | -3.33 | 0 | — | -14.14 | -2.81 | -15.27 | 1 |
| 22 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -3.71 | -0.41 | -17.67 | 39 |
| 23 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.94 | -4.98 | 29 |
| 24 | Agent (rotation) | meta | 96.52 | -3.48 | 90 | 31.1 | -12.16 | -4.16 | -13.99 | 256 |
| 25 | ADX DI cross · 1h | trend | 96.27 | -3.73 | 68 | 19.1 | -11.19 | -2.07 | -14.77 | 252 |
| 26 | Daily: Bullish score | daily | 96.24 | -3.76 | 5 | 0.0 | -2.00 | -0.06 | -12.76 | 12 |
| 27 | EMA 20/50 cross · 1h | trend | 94.99 | -5.01 | 45 | 15.6 | 9.19 | 1.18 | -20.36 | 137 |
| 28 | Parabolic SAR · 1h | trend | 94.31 | -5.69 | 92 | 22.8 | 1.00 | 0.32 | -23.46 | 285 |
| 29 | Agent | meta | 94.26 | -5.74 | 65 | 46.2 | -8.95 | -4.79 | -8.99 | 231 |
| 30 | Copy: Cathie Wood (ARKK) | copy | 94.17 | -5.83 | 0 | — | 4.37 | 0.82 | -10.34 | 1 |
| 31 | Stochastic reversion · 1h | reversion | 93.79 | -6.21 | 112 | 50.0 | -15.85 | -3.06 | -16.31 | 348 |
| 32 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.69 | 1.03 | -9.46 | 103 |
| 33 | Gap and go | momentum | 93.36 | -6.64 | 62 | 11.3 | 8.94 | 2.27 | -6.78 | 199 |
| 34 | MACD cross · 1h | trend | 93.18 | -6.82 | 146 | 22.6 | -13.08 | -1.74 | -21.07 | 459 |
| 35 | Supertrend · 1h | trend | 92.69 | -7.31 | 69 | 11.6 | 0.80 | 0.29 | -21.92 | 211 |
| 36 | Z-score reversion · 1h | reversion | 92.69 | -7.31 | 58 | 39.7 | -4.37 | -0.76 | -10.66 | 157 |
| 37 | RSI momentum · 1h | momentum | 92.56 | -7.44 | 69 | 14.5 | 2.14 | 0.46 | -24.21 | 225 |
| 38 | Agent (aggressive) | meta | 92.13 | -7.87 | 33 | 36.4 | -3.98 | -1.26 | -6.73 | 115 |
| 39 | Bollinger breakout · 1h | breakout | 91.44 | -8.56 | 78 | 29.5 | 7.83 | 1.15 | -14.21 | 278 |
| 40 | Connors RSI(2) · 1h | reversion | 91.11 | -8.88 | 131 | 42.0 | -20.76 | -6.10 | -22.51 | 256 |
| 41 | MFI reversion · 1h | reversion | 91.05 | -8.95 | 173 | 30.6 | -15.40 | -2.71 | -17.17 | 129 |
| 42 | Ichimoku · 1h | trend | 90.92 | -9.08 | 50 | 16.0 | -0.09 | 0.20 | -23.06 | 126 |
| 43 | Triple EMA stack · 1h | trend | 90.62 | -9.38 | 74 | 14.9 | -7.24 | -0.57 | -31.73 | 232 |
| 44 | Max aggression: 5-day momentum | meta | 90.55 | -9.45 | 8 | 37.5 | -8.02 | -0.41 | -34.64 | 27 |
| 45 | Volume breakout · 1h | breakout | 90.49 | -9.51 | 77 | 22.1 | 9.03 | 1.37 | -12.60 | 118 |
| 46 | Agent (ML meta-label) | meta | 89.73 | -10.27 | 494 | 18.4 | -4.02 | -0.58 | -12.82 | 378 |
| 47 | Opening range 30m | breakout | 88.74 | -11.26 | 167 | 22.8 | -14.16 | -4.27 | -17.60 | 558 |
| 48 | OBV trend · 1h | momentum | 88.34 | -11.66 | 162 | 18.5 | -11.11 | -0.96 | -34.91 | 324 |
| 49 | RSI(14) reversion · 1h | reversion | 88.34 | -11.66 | 47 | 27.7 | -8.39 | -1.63 | -12.79 | 151 |
| 50 | Keltner breakout · 1h | breakout | 87.42 | -12.58 | 50 | 22.0 | -7.03 | -0.73 | -26.75 | 213 |
| 51 | MACD zero-line · 1h | trend | 86.87 | -13.13 | 73 | 16.4 | -22.58 | -4.41 | -22.68 | 227 |
| 52 | Donchian 20/10 · 1h | breakout | 86.87 | -13.13 | 68 | 17.6 | -0.08 | 0.19 | -20.09 | 217 |
| 53 | Bollinger reversion · 1h | reversion | 86.80 | -13.20 | 104 | 34.6 | -27.30 | -6.26 | -27.47 | 320 |
| 54 | Williams %R · 1h | reversion | 86.65 | -13.35 | 153 | 43.8 | -30.54 | -5.22 | -30.76 | 512 |
| 55 | CCI reversion · 1h | reversion | 86.07 | -13.93 | 128 | 43.0 | -13.53 | -1.80 | -18.08 | 416 |
| 56 | EMA 9/21 cross · 1h | trend | 85.64 | -14.36 | 118 | 12.7 | -11.03 | -1.33 | -26.21 | 329 |
| 57 | ROC + volume · 1h | momentum | 85.64 | -14.36 | 177 | 21.5 | -9.30 | -1.08 | -25.32 | 398 |
| 58 | VWAP momentum · 1h | momentum | 85.58 | -14.42 | 345 | 22.0 | -36.31 | -5.47 | -42.61 | 1250 |
| 59 | Heikin-Ashi · 1h | trend | 85.56 | -14.44 | 168 | 26.2 | -31.25 | -5.20 | -39.47 | 671 |
| 60 | Three white soldiers | momentum | 85.17 | -14.83 | 171 | 17.5 | -48.03 | -22.40 | -48.24 | 587 |
| 61 | Opening range 15m | breakout | 84.50 | -15.50 | 213 | 20.2 | -19.05 | -5.20 | -21.41 | 697 |
| 62 | Candlestick reversal · 1h | reversion | 83.54 | -16.46 | 154 | 28.6 | -32.84 | -6.36 | -32.93 | 500 |
| 63 | ROC + volume | momentum | 68.26 | -31.74 | 474 | 21.7 | -73.70 | -16.54 | -75.80 | 1681 |
| 64 | Squeeze breakout | breakout | 66.32 | -33.68 | 386 | 15.0 | -63.01 | -18.35 | -63.18 | 1224 |
| 65 | RSI(14) reversion | reversion | 66.27 | -33.73 | 481 | 27.0 | -73.89 | -17.25 | -73.97 | 1542 |
| 66 | Volume breakout | breakout | 66.07 | -33.92 | 305 | 13.8 | -62.85 | -17.77 | -63.15 | 897 |
| 67 | EMA 20/50 cross | trend | 63.29 | -36.71 | 406 | 19.5 | -77.10 | -15.16 | -77.70 | 1436 |
| 68 | Donchian 55/20 | breakout | 63.00 | -37.00 | 397 | 16.6 | -69.47 | -14.71 | -70.95 | 1282 |
| 69 | VWAP reversion | reversion | 60.72 | -39.28 | 505 | 25.1 | -72.81 | -15.41 | -72.91 | 1411 |
| 70 | AI bee: Boozy | ai | 58.17 | -41.83 | 272 | 4.8 | — | — | — | — |
| 71 | Supertrend | trend | 56.75 | -43.25 | 561 | 19.3 | -85.97 | -20.48 | -86.00 | 1899 |
| 72 | Keltner breakout | breakout | 56.23 | -43.77 | 548 | 14.1 | -83.49 | -27.05 | -83.52 | 1854 |
| 73 | Ichimoku | trend | 54.11 | -45.89 | 483 | 9.5 | -82.17 | -22.96 | -82.21 | 1716 |
| 74 | AI bee: Bizzy | ai | 52.41 | -47.59 | 972 | 8.3 | — | — | — | — |
| 75 | MFI reversion | reversion | 51.85 | -48.15 | 692 | 19.9 | -87.71 | -27.34 | -87.71 | 2130 |
| 76 | Z-score reversion | reversion | 50.71 | -49.29 | 651 | 22.4 | -86.08 | -22.12 | -86.12 | 2115 |
| 77 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.53 | -29.16 | -98.54 | 5333 |
| 78 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.57 | -30.19 | -93.57 | 2596 |
| 79 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -25.06 | -90.57 | 2358 |
| 80 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.69 | -26.80 | -91.69 | 2351 |
| 81 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.40 | -32.73 | -97.40 | 3522 |
| 82 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.58 | -35.85 | -96.58 | 3591 |
| 83 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.64 | -26.21 | -94.65 | 2639 |
| 84 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -36.08 | -99.38 | 5707 |
| 85 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.04 | -25.81 | -91.06 | 2634 |
| 86 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.36 | -31.12 | -96.37 | 3584 |
| 87 | ADX DI cross | trend | 50.17 | -49.83 | 662 | 10.3 | -89.26 | -34.25 | -89.26 | 2100 |
| 88 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -41.11 | -99.73 | 6154 |
| 89 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.72 | -29.86 | -91.72 | 2362 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -37.43 | -97.42 | 3655 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.51 | -35.98 | -98.52 | 4672 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.44 | -32.63 | -93.46 | 2799 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -39.27 | -99.55 | 6139 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.00 | -32.50 | -96.01 | 3744 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.74 | -33.89 | -95.76 | 4057 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.67 | -99.89 | 8210 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-14T15:25 | MFI reversion | buy | MSTR | 1.48 | — | entry |
| 2026-10-14T15:25 | MFI reversion | buy | META | 3.24 | — | entry |
| 2026-10-14T15:25 | MFI reversion | sell | DOGE-USD | 4.72 | 0.01 | exit signal |
| 2026-10-14T15:21 | MFI reversion | buy | ETHU | 1.13 | — | entry signal |
| 2026-10-14T15:21 | MFI reversion | buy | BTC-USD | 3.05 | — | entry signal |
| 2026-10-14T15:21 | MFI reversion | buy | AMZN | 3.05 | — | entry signal |
| 2026-10-14T15:21 | MFI reversion | sell | NVDA | 3.42 | -0.01 | rebalance down |
| 2026-10-14T15:21 | MFI reversion | sell | MSFT | 3.81 | -0.01 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | buy | UPRO | 4.29 | — | entry |
| 2026-10-14T15:21 | VWAP reversion | buy | TNA | 4.35 | — | entry signal |
| 2026-10-14T15:21 | VWAP reversion | buy | TECL | 4.35 | — | entry signal |
| 2026-10-14T15:21 | VWAP reversion | buy | SOXL | 4.35 | — | entry signal |
| 2026-10-14T15:21 | VWAP reversion | buy | MSFT | 4.35 | — | entry |
| 2026-10-14T15:21 | VWAP reversion | buy | IWM | 4.35 | — | entry signal |
| 2026-10-14T15:21 | VWAP reversion | buy | BTC-USD | 4.35 | — | entry |
| 2026-10-14T15:21 | VWAP reversion | sell | XRP-USD | 4.34 | -0.01 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | SOL-USD | 4.27 | 0.01 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | META | 4.27 | -0.01 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | ETHU | 4.45 | 0.07 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | ETH-USD | 4.37 | 0.00 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | DOGE-USD | 4.35 | 0.01 | rebalance down |
| 2026-10-14T15:21 | VWAP reversion | sell | BITX | 4.31 | 0.00 | rebalance down |
| 2026-10-14T15:21 | RSI(14) reversion | buy | SPY | 2.70 | — | entry signal |
| 2026-10-14T15:21 | RSI(14) reversion | buy | IWM | 3.32 | — | entry signal |
| 2026-10-14T15:21 | ADX DI cross | buy | SOL-USD | 12.55 | — | entry signal |
| 2026-10-14T15:15 | MFI reversion | buy | XRP-USD | 1.58 | — | entry signal |
| 2026-10-14T15:15 | MFI reversion | buy | UPRO | 4.71 | — | entry |
| 2026-10-14T15:15 | MFI reversion | buy | ETH-USD | 4.71 | — | entry signal |
| 2026-10-14T15:15 | MFI reversion | buy | AAPL | 4.71 | — | entry signal |
| 2026-10-14T15:15 | MFI reversion | sell | SPY | 3.92 | -0.00 | rebalance down |
| 2026-10-14T15:15 | MFI reversion | sell | IWM | 3.92 | -0.01 | rebalance down |
| 2026-10-14T15:15 | MFI reversion | sell | DOGE-USD | 3.94 | -0.01 | rebalance down |
| 2026-10-14T15:15 | MFI reversion | sell | BITX | 3.94 | -0.01 | rebalance down |
| 2026-10-14T15:15 | RSI(14) reversion | buy | XRP-USD | 3.89 | — | entry |
| 2026-10-14T15:15 | RSI(14) reversion | sell | TQQQ | 3.47 | -0.03 | stop-loss |
| 2026-10-14T15:15 | RSI(14) reversion | sell | QQQ | 5.55 | -0.01 | stop-loss |
| 2026-10-14T15:10 | RSI(14) reversion · 1h | sell | AMD | 22.04 | -0.24 | stop-loss |
| 2026-10-14T15:10 | MACD cross · 1h | buy | SQQQ | 7.63 | — | rebalance up |
| 2026-10-14T15:10 | MACD cross · 1h | buy | META | 7.76 | — | rebalance up |
| 2026-10-14T15:10 | MACD cross · 1h | buy | BITX | 7.77 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-16 15:25:05.000126+00:00 -> 2026-10-14 15:35:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
