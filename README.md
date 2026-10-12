# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-12T17:21:05.000147+00:00 · 20417 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.38 (-4.62%)

Closed trades 57, win rate 50.9%, fees £2.20, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| AAPL | 19.08 | -0.02 |
| TNA | 19.07 | -0.02 |

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

Today: 23382 decisions in 2478 calls, $0.2968 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-12T17:21 | 5 / 15 / 9 | META 15% |  |
| Breezy | 2026-10-12T17:21 | 0 / 26 / 3 | cash |  |
| Boozy | 2026-10-12T17:21 | 0 / 27 / 2 | COIN 76% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 102.88 | 2.88 | 0 | — | -0.58 | -0.22 | -5.18 | 1 |
| 2 | Copy: Insider buying | copy | 102.30 | 2.30 | 14 | 57.1 | -12.42 | -2.04 | -20.64 | 71 |
| 3 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 4 | VWAP reversion · 1h | reversion | 101.70 | 1.70 | 39 | 41.0 | -9.06 | -2.73 | -13.79 | 118 |
| 5 | Hold SPY | benchmark | 101.43 | 1.43 | 0 | — | 0.90 | 0.58 | -3.66 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.29 | 1.28 | 6 | 50.0 | 4.67 | 2.08 | -3.27 | 17 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.22 | 1.22 | 0 | — | 1.47 | 0.72 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · TQQQ | daily | 100.75 | 0.75 | 0 | — | -4.65 | -0.75 | -15.27 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 100.68 | 0.68 | 0 | — | -1.07 | -0.56 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.50 | 0.50 | 6 | 50.0 | -3.95 | -1.31 | -9.74 | 25 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.29 | 0.29 | 10 | 30.0 | 4.50 | 1.42 | -7.55 | 43 |
| 12 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 13 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 14 | Daily: SMA 20/50 cross · AAPL | daily | 99.68 | -0.32 | 0 | — | 2.66 | 1.08 | -5.18 | 1 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.59 | -0.41 | 0 | — | -4.71 | -2.17 | -5.36 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.13 | -0.87 | 41 | 34.1 | 5.41 | 2.64 | -1.80 | 78 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -2.31 | -2.52 | -3.34 | 20 |
| 18 | Hold BTC | benchmark | 98.81 | -1.19 | 0 | — | 29.40 | 3.46 | -8.68 | 1 |
| 19 | Donchian 55/20 · 1h | breakout | 98.04 | -1.96 | 31 | 12.9 | 12.80 | 1.55 | -16.92 | 114 |
| 20 | Trend pullback · 1h | trend | 97.71 | -2.29 | 78 | 23.1 | -23.13 | -6.47 | -25.60 | 168 |
| 21 | Stochastic reversion · 1h | reversion | 97.67 | -2.33 | 96 | 53.1 | -11.25 | -2.18 | -13.91 | 335 |
| 22 | Max aggression: 1-day momentum | meta | 97.64 | -2.36 | 11 | 36.4 | -17.06 | -0.65 | -37.31 | 42 |
| 23 | Daily: Bullish score | daily | 97.61 | -2.39 | 4 | 0.0 | 0.68 | 0.28 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.17 | -2.83 | 8 | 0.0 | -3.40 | -2.61 | -4.53 | 27 |
| 25 | Z-score reversion · 1h | reversion | 96.96 | -3.04 | 44 | 43.2 | 3.82 | 0.89 | -8.60 | 157 |
| 26 | Copy: Cathie Wood (ARKK) | copy | 96.70 | -3.30 | 0 | — | 8.96 | 1.49 | -8.33 | 1 |
| 27 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -2.48 | -0.21 | -17.67 | 39 |
| 28 | ADX DI cross · 1h | trend | 96.42 | -3.58 | 62 | 19.4 | -7.75 | -1.32 | -14.05 | 254 |
| 29 | Agent (rotation) | meta | 96.28 | -3.72 | 82 | 29.3 | -12.04 | -3.70 | -15.94 | 294 |
| 30 | MACD cross · 1h | trend | 95.85 | -4.15 | 120 | 24.2 | -13.34 | -2.20 | -17.27 | 468 |
| 31 | Parabolic SAR · 1h | trend | 95.54 | -4.46 | 83 | 21.7 | 1.35 | 0.36 | -21.52 | 291 |
| 32 | EMA 20/50 cross · 1h | trend | 95.53 | -4.47 | 44 | 13.6 | 3.80 | 0.64 | -23.04 | 134 |
| 33 | Agent | meta | 95.38 | -4.62 | 57 | 50.9 | -8.69 | -4.23 | -9.39 | 254 |
| 34 | Supertrend · 1h | trend | 94.40 | -5.60 | 58 | 13.8 | 0.61 | 0.27 | -18.58 | 212 |
| 35 | Gap and go | momentum | 93.70 | -6.30 | 59 | 11.9 | 8.23 | 2.10 | -6.21 | 202 |
| 36 | Squeeze breakout · 1h | breakout | 93.56 | -6.44 | 39 | 23.1 | 4.26 | 0.93 | -9.46 | 104 |
| 37 | Agent (aggressive) | meta | 93.44 | -6.56 | 26 | 42.3 | -8.70 | -2.99 | -8.87 | 120 |
| 38 | MFI reversion · 1h | reversion | 93.37 | -6.63 | 124 | 34.7 | -8.03 | -1.22 | -16.91 | 127 |
| 39 | Connors RSI(2) · 1h | reversion | 92.67 | -7.33 | 114 | 43.0 | -18.63 | -6.14 | -21.04 | 253 |
| 40 | RSI momentum · 1h | momentum | 92.49 | -7.51 | 66 | 15.2 | 0.23 | 0.23 | -21.83 | 228 |
| 41 | Agent (ML meta-label) | meta | 92.43 | -7.57 | 424 | 18.4 | 1.49 | 0.40 | -12.38 | 401 |
| 42 | RSI(14) reversion · 1h | reversion | 92.14 | -7.86 | 30 | 30.0 | -5.28 | -1.06 | -9.03 | 147 |
| 43 | Volume breakout · 1h | breakout | 91.76 | -8.24 | 64 | 20.3 | 9.00 | 1.37 | -12.60 | 117 |
| 44 | Bollinger reversion · 1h | reversion | 91.64 | -8.36 | 83 | 37.3 | -22.18 | -5.31 | -23.38 | 318 |
| 45 | Ichimoku · 1h | trend | 91.11 | -8.89 | 47 | 17.0 | 0.85 | 0.31 | -22.34 | 126 |
| 46 | Bollinger breakout · 1h | breakout | 90.91 | -9.09 | 74 | 28.4 | 8.34 | 1.21 | -14.21 | 277 |
| 47 | Triple EMA stack · 1h | trend | 90.67 | -9.33 | 71 | 15.5 | -7.81 | -0.70 | -27.28 | 237 |
| 48 | Williams %R · 1h | reversion | 89.87 | -10.13 | 130 | 46.9 | -26.37 | -4.46 | -27.42 | 507 |
| 49 | Opening range 30m | breakout | 89.73 | -10.27 | 152 | 21.7 | -15.50 | -4.68 | -15.82 | 568 |
| 50 | CCI reversion · 1h | reversion | 88.89 | -11.11 | 111 | 45.9 | -7.62 | -0.93 | -14.35 | 406 |
| 51 | VWAP momentum · 1h | momentum | 88.57 | -11.43 | 304 | 23.0 | -32.77 | -4.88 | -40.22 | 1256 |
| 52 | OBV trend · 1h | momentum | 88.51 | -11.49 | 150 | 18.7 | -8.26 | -0.72 | -28.84 | 321 |
| 53 | Candlestick reversal · 1h | reversion | 88.43 | -11.57 | 126 | 31.7 | -29.36 | -5.75 | -29.53 | 507 |
| 54 | Heikin-Ashi · 1h | trend | 87.99 | -12.01 | 149 | 28.2 | -30.44 | -5.05 | -37.50 | 686 |
| 55 | MACD zero-line · 1h | trend | 87.85 | -12.15 | 67 | 17.9 | -15.12 | -2.42 | -21.31 | 234 |
| 56 | Donchian 20/10 · 1h | breakout | 87.62 | -12.38 | 63 | 17.5 | -0.64 | 0.13 | -19.48 | 214 |
| 57 | Max aggression: 5-day momentum | meta | 87.39 | -12.61 | 7 | 28.6 | -15.08 | -1.11 | -34.64 | 28 |
| 58 | EMA 9/21 cross · 1h | trend | 87.23 | -12.77 | 107 | 13.1 | -10.93 | -1.30 | -23.37 | 332 |
| 59 | Opening range 15m | breakout | 86.86 | -13.14 | 180 | 20.0 | -18.15 | -5.01 | -19.41 | 692 |
| 60 | Keltner breakout · 1h | breakout | 86.71 | -13.29 | 45 | 20.0 | -11.40 | -1.25 | -26.77 | 217 |
| 61 | Three white soldiers | momentum | 86.54 | -13.46 | 152 | 17.1 | -48.68 | -23.38 | -48.68 | 589 |
| 62 | ROC + volume · 1h | momentum | 85.79 | -14.21 | 139 | 21.6 | -9.03 | -1.04 | -24.79 | 400 |
| 63 | ROC + volume | momentum | 72.95 | -27.05 | 415 | 22.7 | -72.87 | -16.46 | -74.39 | 1672 |
| 64 | RSI(14) reversion | reversion | 71.06 | -28.94 | 403 | 26.8 | -72.61 | -17.72 | -72.73 | 1474 |
| 65 | Squeeze breakout | breakout | 69.91 | -30.09 | 347 | 15.3 | -62.01 | -17.81 | -62.22 | 1220 |
| 66 | Volume breakout | breakout | 69.59 | -30.41 | 274 | 14.2 | -62.23 | -17.69 | -62.26 | 898 |
| 67 | EMA 20/50 cross | trend | 68.21 | -31.79 | 351 | 19.7 | -76.22 | -14.94 | -76.28 | 1429 |
| 68 | Donchian 55/20 | breakout | 67.07 | -32.93 | 357 | 17.6 | -68.21 | -14.37 | -68.90 | 1290 |
| 69 | VWAP reversion | reversion | 65.77 | -34.23 | 423 | 25.8 | -71.14 | -15.57 | -71.20 | 1398 |
| 70 | Keltner breakout | breakout | 60.72 | -39.28 | 478 | 14.6 | -83.47 | -27.25 | -83.54 | 1847 |
| 71 | Supertrend | trend | 60.38 | -39.62 | 495 | 19.2 | -85.97 | -20.71 | -86.06 | 1900 |
| 72 | AI bee: Boozy | ai | 60.02 | -39.98 | 261 | 5.0 | — | — | — | — |
| 73 | Ichimoku | trend | 57.42 | -42.58 | 432 | 10.0 | -82.21 | -22.90 | -82.21 | 1742 |
| 74 | MFI reversion | reversion | 55.96 | -44.04 | 561 | 20.0 | -87.75 | -27.81 | -87.80 | 2108 |
| 75 | Z-score reversion | reversion | 55.89 | -44.11 | 545 | 21.3 | -85.63 | -22.84 | -85.63 | 2063 |
| 76 | AI bee: Bizzy | ai | 55.72 | -44.28 | 880 | 8.4 | — | — | — | — |
| 77 | ADX DI cross | trend | 54.02 | -45.98 | 585 | 9.9 | -89.16 | -33.92 | -89.17 | 2102 |
| 78 | Donchian 20/10 | breakout | 52.21 | -47.79 | 673 | 17.5 | -90.80 | -25.44 | -90.89 | 2643 |
| 79 | MACD zero-line | trend | 51.26 | -48.74 | 625 | 14.4 | -91.44 | -29.34 | -91.44 | 2340 |
| 80 | RSI momentum | momentum | 50.62 | -49.38 | 651 | 16.6 | -90.59 | -25.55 | -90.59 | 2372 |
| 81 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.24 | -98.63 | 5380 |
| 82 | Trend pullback ⏸ | trend | 50.55 | -49.45 | 635 | 14.2 | -91.38 | -26.59 | -91.38 | 2335 |
| 83 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.24 | -29.90 | -93.25 | 2611 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.34 | -32.45 | -97.37 | 3516 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.39 | -35.40 | -96.40 | 3601 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -25.55 | -94.38 | 2643 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -36.14 | -99.35 | 5617 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -31.29 | -96.38 | 3617 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -40.94 | -99.73 | 6125 |
| 90 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -37.51 | -97.37 | 3675 |
| 91 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.43 | -98.50 | 4656 |
| 92 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.43 | -32.47 | -93.48 | 2795 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -39.24 | -99.53 | 6108 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.89 | -32.79 | -95.89 | 3714 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -33.83 | -95.70 | 4054 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -45.20 | -99.89 | 8222 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-12T17:21 | AI bee: Bizzy | buy | META | 8.40 | — | Jev: buy (buy p=0.60) |
| 2026-10-12T17:21 | MFI reversion | buy | TNA | 7.99 | — | entry signal |
| 2026-10-12T17:21 | MFI reversion | sell | COIN | 7.99 | -0.08 | stop-loss |
| 2026-10-12T17:21 | VWAP reversion | buy | SOL-USD | 7.27 | — | entry |
| 2026-10-12T17:21 | VWAP reversion | buy | GOOGL | 7.32 | — | entry signal |
| 2026-10-12T17:21 | VWAP reversion | buy | ETHU | 7.32 | — | entry |
| 2026-10-12T17:21 | VWAP reversion | sell | XRP-USD | 3.58 | -0.02 | rebalance down |
| 2026-10-12T17:21 | VWAP reversion | sell | LABU | 3.65 | -0.01 | rebalance down |
| 2026-10-12T17:21 | VWAP reversion | sell | ETH-USD | 3.66 | -0.03 | rebalance down |
| 2026-10-12T17:21 | VWAP reversion | sell | DOGE-USD | 3.68 | -0.03 | rebalance down |
| 2026-10-12T17:21 | VWAP reversion | sell | BTC-USD | 3.66 | -0.02 | rebalance down |
| 2026-10-12T17:21 | VWAP reversion | sell | AMZN | 3.66 | -0.00 | rebalance down |
| 2026-10-12T17:21 | ADX DI cross | buy | META | 13.51 | — | entry signal |
| 2026-10-12T17:10 | MFI reversion | buy | PLTR | 7.99 | — | entry signal |
| 2026-10-12T17:10 | MFI reversion | buy | ETH-USD | 8.00 | — | entry signal |
| 2026-10-12T17:10 | MFI reversion | sell | TSLA | 3.21 | -0.00 | rebalance down |
| 2026-10-12T17:10 | MFI reversion | sell | MSTR | 3.20 | -0.01 | rebalance down |
| 2026-10-12T17:10 | MFI reversion | sell | IWM | 3.21 | -0.01 | rebalance down |
| 2026-10-12T17:10 | MFI reversion | sell | DOGE-USD | 3.19 | -0.01 | rebalance down |
| 2026-10-12T17:10 | MFI reversion | sell | COIN | 3.18 | -0.03 | rebalance down |
| 2026-10-12T17:08 | MFI reversion | buy | DOGE-USD | 2.80 | — | rebalance up |
| 2026-10-12T17:08 | MFI reversion | sell | COIN | 2.80 | -0.02 | rebalance down |
| 2026-10-12T17:07 | MFI reversion | buy | DOGE-USD | 2.80 | — | rebalance up |
| 2026-10-12T17:07 | MFI reversion | sell | MSTR | 2.80 | -0.01 | rebalance down |
| 2026-10-12T17:05 | MFI reversion | buy | DOGE-USD | 5.60 | — | entry signal |
| 2026-10-12T17:05 | MFI reversion | sell | TSLA | 2.81 | -0.00 | rebalance down |
| 2026-10-12T17:05 | VWAP reversion | buy | XRP-USD | 10.93 | — | entry signal |
| 2026-10-12T17:05 | VWAP reversion | buy | AMZN | 10.98 | — | entry signal |
| 2026-10-12T17:05 | VWAP reversion | sell | LABU | 5.48 | -0.01 | rebalance down |
| 2026-10-12T17:05 | VWAP reversion | sell | ETH-USD | 5.47 | -0.05 | rebalance down |
| 2026-10-12T17:05 | VWAP reversion | sell | DOGE-USD | 5.50 | -0.05 | rebalance down |
| 2026-10-12T17:05 | VWAP reversion | sell | BTC-USD | 5.47 | -0.04 | rebalance down |
| 2026-10-12T17:05 | Z-score reversion | buy | DOGE-USD | 5.08 | — | entry signal |
| 2026-10-12T17:05 | Z-score reversion | buy | AMZN | 5.08 | — | entry signal |
| 2026-10-12T17:05 | RSI(14) reversion | buy | XRP-USD | 1.64 | — | entry signal |
| 2026-10-12T17:05 | RSI(14) reversion | buy | AMZN | 10.14 | — | entry signal |
| 2026-10-12T17:05 | Opening range 15m | buy | META | 21.73 | — | entry signal |
| 2026-10-12T17:00 | AI bee: Bizzy | sell | META | 8.62 | -0.11 | Jev: sell (sell p=0.73) after 12 min |
| 2026-10-12T17:00 | VWAP reversion | buy | LABU | 5.51 | — | rebalance up |
| 2026-10-12T17:00 | VWAP reversion | buy | ETH-USD | 5.49 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-14 17:21:05.000147+00:00 -> 2026-10-12 17:31:05.000147+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
