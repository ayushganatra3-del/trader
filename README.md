# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T02:55:05.000163+00:00 · 25481 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £91.99 (-8.01%)

Closed trades 77, win rate 39.0%, fees £2.69, max drawdown -8.92%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| GOOGL | 18.15 | -0.23 |
| SQQQ | 19.18 | +0.80 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-16 | BORR 12%, GGR 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-16)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 27.13 · VIX 19.99 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.1, AAPL 6.3, SQQQ 5.6, PLTR 5.4, META 4.5, BITX 4.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 2190 decisions in 438 calls, $0.0307 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T02:55 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-17T02:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T02:55 | 3 / 2 / 0 | COIN 67% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | ETHU | 2.27 | +3.35% | 6 |
| VWAP momentum · 1h | SQQQ | 2.13 | +12.90% | 7 |
| ROC + volume · 1h | SQQQ | 2.11 | +14.98% | 3 |
| Bollinger reversion | SQQQ | 2.01 | +0.94% | 8 |
| Opening range 30m | AMZN | 1.94 | +3.77% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 107.79 | 7.79 | 10 | 70.0 | 9.21 | 3.08 | -3.27 | 19 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 107.08 | 7.08 | 11 | 72.7 | 1.21 | 0.45 | -9.61 | 27 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.15 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.59 | -3.36 | -13.80 | 136 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.33 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -9.85 | -4.05 | -11.12 | 287 |
| 17 | Hold BTC | benchmark | 96.60 | -3.40 | 0 | — | 28.63 | 3.36 | -8.68 | 1 |
| 18 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 19 | Timing: Nasdaq FTD · QQQ | daily | 96.42 | -3.58 | 0 | — | -6.59 | -3.59 | -6.88 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.02 | -6.26 | -22.15 | 150 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.27 | -1.46 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.17 | 2.34 | -6.73 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -4.00 | -0.35 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.79 | -2.37 | -10.02 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.84 | -5.99 | -12.21 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.39 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.25 | 0.36 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.16 | 0.98 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.39 | -0.56 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.08 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | MACD cross · 1h | trend | 89.13 | -10.87 | 171 | 22.8 | -14.61 | -1.94 | -27.78 | 454 |
| 42 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.85 | -1.09 | -27.05 | 208 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.46 | -7.73 | -26.03 | 237 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -8.17 | -0.65 | -34.23 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.86 | -13.14 | 136 | 43.4 | -20.59 | -3.75 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.22 | -4.51 | -21.41 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.53 | -4.43 | -23.33 | 218 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.34 | 0.37 | -21.63 | 217 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.29 | -19.30 | -48.32 | 601 |
| 51 | MFI reversion · 1h | reversion | 84.04 | -15.96 | 204 | 30.4 | -20.43 | -3.48 | -21.05 | 140 |
| 52 | VWAP momentum · 1h | momentum | 83.43 | -16.57 | 390 | 21.0 | -35.79 | -5.43 | -43.85 | 1249 |
| 53 | Z-score reversion · 1h | reversion | 83.41 | -16.59 | 86 | 31.4 | -15.43 | -2.69 | -19.86 | 182 |
| 54 | Heikin-Ashi · 1h | trend | 83.40 | -16.60 | 192 | 24.0 | -31.78 | -5.25 | -40.65 | 675 |
| 55 | Agent (ML meta-label) | meta | 83.08 | -16.92 | 610 | 19.2 | -5.65 | -0.68 | -15.65 | 395 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.65 | -1.67 | -26.96 | 403 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.85 | -0.61 | -29.70 | 318 |
| 58 | Bollinger reversion · 1h | reversion | 80.12 | -19.89 | 138 | 31.2 | -30.23 | -6.27 | -32.42 | 345 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.39 | -5.61 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.33 | -2.55 | -21.70 | 165 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.11 | -2.47 | -25.55 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.51 | -6.38 | -36.41 | 532 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.13 | -18.14 | -63.13 | 877 |
| 64 | ROC + volume | momentum | 63.23 | -36.77 | 550 | 22.0 | -75.81 | -17.71 | -77.38 | 1718 |
| 65 | Squeeze breakout | breakout | 62.84 | -37.16 | 431 | 14.6 | -62.93 | -18.00 | -64.19 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.39 | -37.61 | 646 | 25.9 | -74.75 | -16.71 | -74.81 | 1636 |
| 67 | Donchian 55/20 | breakout | 61.15 | -38.85 | 438 | 17.8 | -69.25 | -14.67 | -71.81 | 1286 |
| 68 | EMA 20/50 cross | trend | 59.28 | -40.72 | 460 | 19.1 | -77.20 | -15.34 | -79.17 | 1451 |
| 69 | VWAP reversion | reversion | 55.50 | -44.50 | 681 | 23.6 | -73.59 | -15.70 | -73.65 | 1509 |
| 70 | AI bee: Boozy | ai | 55.16 | -44.84 | 304 | 6.6 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.59 | -45.41 | 608 | 16.1 | -83.39 | -26.98 | -83.47 | 1837 |
| 72 | Ichimoku | trend | 51.81 | -48.19 | 555 | 11.7 | -81.99 | -23.19 | -82.05 | 1733 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -30.13 | -98.60 | 5309 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.51 | -30.67 | -93.51 | 2601 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.52 | -20.57 | -87.11 | 1915 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.50 | -25.01 | -90.50 | 2368 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -27.18 | -91.66 | 2333 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -33.11 | -97.45 | 3531 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -37.20 | -96.72 | 3615 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.32 | -26.66 | -94.38 | 2619 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -37.47 | -99.41 | 5841 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.38 | -26.15 | -91.38 | 2648 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.31 | -32.07 | -96.32 | 3562 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.99 | -99.73 | 6231 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -29.87 | -91.79 | 2371 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.48 | -39.25 | -97.48 | 3660 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -37.51 | -98.50 | 4774 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.67 | -33.45 | -93.67 | 2808 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -40.59 | -99.54 | 6262 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.61 | -22.40 | -86.62 | 2159 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.90 | -27.57 | -87.90 | 2157 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.01 | -33.66 | -96.01 | 3829 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.34 | -34.40 | -89.34 | 2116 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.86 | -34.66 | -95.87 | 4164 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -46.71 | -99.89 | 8307 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T02:55 | VWAP reversion | sell | DOGE-USD | 13.85 | -0.05 | exit signal |
| 2026-10-17T02:40 | VWAP reversion | buy | BTC-USD | 13.89 | — | entry signal |
| 2026-10-17T02:35 | EMA 20/50 cross | sell | ETH-USD | 14.73 | -0.13 | stop-loss |
| 2026-10-17T02:30 | Squeeze breakout | sell | SOL-USD | 15.60 | -0.15 | stop-loss |
| 2026-10-17T02:30 | Donchian 55/20 | sell | SOL-USD | 15.18 | -0.15 | stop-loss |
| 2026-10-17T02:30 | Ichimoku | sell | ETH-USD | 12.87 | -0.11 | stop-loss |
| 2026-10-17T02:19 | AI bee: Boozy | sell | ETH-USD | 18.10 | -0.14 | Jev: sell |
| 2026-10-17T02:10 | EMA 20/50 cross | buy | ETH-USD | 14.86 | — | entry signal |
| 2026-10-17T02:05 | Agent (ML meta-label) | buy | SOL-USD | 2.79 | — | entry |
| 2026-10-17T02:05 | Agent (ML meta-label) | buy | DOGE-USD | 3.20 | — | entry |
| 2026-10-17T02:05 | Agent (ML meta-label) | sell | BTC-USD | 5.99 | -0.04 | rebalance down |
| 2026-10-17T02:05 | VWAP reversion | sell | XRP-USD | 13.89 | -0.02 | exit signal |
| 2026-10-17T02:05 | Squeeze breakout | buy | SOL-USD | 15.75 | — | entry signal |
| 2026-10-17T02:05 | Donchian 55/20 | buy | SOL-USD | 15.33 | — | entry signal |
| 2026-10-17T02:05 | Ichimoku | buy | ETH-USD | 12.98 | — | entry signal |
| 2026-10-17T02:04 | AI bee: Boozy | buy | ETH-USD | 18.24 | — | Jev: buy (buy p=0.68) |
| 2026-10-17T02:00 | VWAP momentum · 1h | sell | SOL-USD | 20.79 | -0.14 | exit signal |
| 2026-10-17T02:00 | VWAP momentum · 1h | sell | ETH-USD | 20.78 | -0.15 | exit signal |
| 2026-10-17T02:00 | Heikin-Ashi · 1h | sell | ETH-USD | 16.65 | -0.12 | exit signal |
| 2026-10-17T01:45 | VWAP reversion | buy | DOGE-USD | 13.90 | — | entry signal |
| 2026-10-17T01:40 | EMA 20/50 cross | sell | ETH-USD | 14.85 | -0.11 | exit signal |
| 2026-10-17T01:15 | RSI(14) reversion | buy | DOGE-USD | 15.61 | — | entry signal |
| 2026-10-17T01:05 | EMA 20/50 cross | sell | DOGE-USD | 14.77 | -0.20 | stop-loss |
| 2026-10-17T01:00 | VWAP momentum · 1h | buy | SOL-USD | 20.93 | — | entry signal |
| 2026-10-17T01:00 | VWAP momentum · 1h | buy | ETH-USD | 20.93 | — | entry signal |
| 2026-10-17T01:00 | Heikin-Ashi · 1h | sell | XRP-USD | 12.00 | -0.11 | exit signal |
| 2026-10-17T01:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 16.55 | -0.22 | exit signal |
| 2026-10-17T00:55 | EMA 20/50 cross | sell | XRP-USD | 14.85 | -0.11 | exit signal |
| 2026-10-17T00:50 | Supertrend | sell | SOL-USD | 12.61 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-17T00:50 | Supertrend | sell | ETH-USD | 12.61 | -0.11 | Kill switch: down 50% from peak |
| 2026-10-17T00:45 | Ichimoku | sell | SOL-USD | 12.90 | -0.11 | exit signal |
| 2026-10-17T00:35 | VWAP reversion | sell | ETH-USD | 13.93 | -0.02 | exit signal |
| 2026-10-17T00:35 | VWAP reversion | sell | DOGE-USD | 13.85 | -0.11 | exit signal |
| 2026-10-17T00:35 | Ichimoku | buy | SOL-USD | 13.01 | — | entry signal |
| 2026-10-17T00:25 | Supertrend | sell | XRP-USD | 12.60 | -0.12 | exit signal |
| 2026-10-17T00:20 | Supertrend | sell | DOGE-USD | 12.60 | -0.12 | exit signal |
| 2026-10-17T00:20 | EMA 20/50 cross | buy | ETH-USD | 8.93 | — | rebalance up |
| 2026-10-17T00:20 | EMA 20/50 cross | buy | DOGE-USD | 3.00 | — | rebalance up |
| 2026-10-17T00:20 | EMA 20/50 cross | sell | BTC-USD | 14.88 | -0.11 | exit signal |
| 2026-10-17T00:15 | Heikin-Ashi · 1h | buy | XRP-USD | 4.17 | — | rebalance up |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 02:55:05.000163+00:00 -> 2026-10-17 03:05:05.000163+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
