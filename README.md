# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T04:25:05.000157+00:00 · 23210 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £93.10 (-6.91%)

Closed trades 72, win rate 41.7%, fees £2.56, max drawdown -7.33%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-14 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-14)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.87 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.2, AAPL 6.2, META 5.5, GOOGL 5.4, SPY 4.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 3300 decisions in 660 calls, $0.0463 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T04:25 | 1 / 4 / 0 | TNA 15% |  |
| Breezy | 2026-10-15T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T04:25 | 5 / 0 / 0 | COIN 77% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| MFI reversion | AAPL | 1.54 | +0.60% | 4 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Triple EMA stack | NVDA | 1.50 | +0.75% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 104.33 | 4.33 | 0 | — | 4.16 | 1.99 | -5.18 | 1 |
| 2 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 6.49 | 2.69 | -3.27 | 19 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 102.77 | 2.77 | 9 | 66.7 | -2.45 | -0.74 | -9.84 | 26 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 5 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 101.05 | 1.05 | 13 | 38.5 | 2.90 | 0.97 | -7.55 | 43 |
| 6 | VWAP reversion · 1h | reversion | 100.76 | 0.76 | 46 | 39.1 | -8.87 | -2.65 | -13.79 | 126 |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 100.34 | 0.34 | 0 | — | 4.04 | 1.58 | -5.18 | 1 |
| 8 | Copy: Insider buying | copy | 100.17 | 0.17 | 20 | 45.0 | -16.02 | -2.54 | -21.97 | 76 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Hold SPY | benchmark | 99.96 | -0.04 | 0 | — | -0.98 | -0.53 | -3.44 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.28 | -3.79 | -3.91 | 21 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.63 | -1.37 | 0 | — | -1.10 | -0.42 | -3.75 | 1 |
| 14 | Day trade: Stocks in Play ORB | daytrade | 98.42 | -1.58 | 48 | 33.3 | 1.68 | 1.01 | -2.07 | 67 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 98.42 | -1.58 | 0 | — | -5.15 | -2.02 | -6.99 | 1 |
| 16 | Timing: Nasdaq FTD · QQQ | daily | 98.34 | -1.66 | 0 | — | -4.93 | -2.74 | -5.36 | 1 |
| 17 | Donchian 55/20 · 1h | breakout | 96.99 | -3.01 | 36 | 16.7 | 5.91 | 0.86 | -22.11 | 114 |
| 18 | Hold BTC | benchmark | 96.90 | -3.10 | 0 | — | 27.94 | 3.25 | -8.68 | 1 |
| 19 | Trend pullback · 1h | trend | 96.85 | -3.15 | 86 | 24.4 | -24.00 | -6.87 | -24.88 | 168 |
| 20 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.60 | -0.55 | -17.67 | 39 |
| 21 | Three white soldiers · 1h | momentum | 96.63 | -3.37 | 10 | 0.0 | -3.86 | -2.92 | -4.98 | 29 |
| 22 | Agent (rotation) | meta | 96.14 | -3.86 | 93 | 30.1 | -13.19 | -4.79 | -14.73 | 280 |
| 23 | ADX DI cross · 1h | trend | 95.68 | -4.32 | 70 | 21.4 | -10.50 | -1.91 | -14.52 | 250 |
| 24 | Daily: Bullish score | daily | 94.69 | -5.31 | 5 | 0.0 | -2.87 | -0.17 | -12.76 | 12 |
| 25 | Max aggression: 1-day momentum | meta | 94.60 | -5.40 | 13 | 38.5 | -9.94 | -0.18 | -37.31 | 42 |
| 26 | Timing: Nasdaq FTD · TQQQ | daily | 94.52 | -5.48 | 0 | — | -15.33 | -2.92 | -16.54 | 1 |
| 27 | Gap and go | momentum | 93.89 | -6.11 | 63 | 12.7 | 9.60 | 2.41 | -6.73 | 199 |
| 28 | EMA 20/50 cross · 1h | trend | 93.80 | -6.20 | 48 | 16.7 | 5.21 | 0.78 | -23.21 | 138 |
| 29 | Parabolic SAR · 1h | trend | 93.78 | -6.22 | 93 | 22.6 | 0.58 | 0.27 | -23.42 | 287 |
| 30 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 5.07 | 1.09 | -9.46 | 102 |
| 31 | MACD cross · 1h | trend | 93.37 | -6.63 | 149 | 22.8 | -11.85 | -1.59 | -21.42 | 454 |
| 32 | Agent | meta | 93.10 | -6.91 | 72 | 41.7 | -5.87 | -2.10 | -9.51 | 240 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 92.77 | -7.23 | 0 | — | 3.87 | 0.74 | -11.29 | 1 |
| 34 | Max aggression: 5-day momentum | meta | 91.92 | -8.08 | 8 | 37.5 | -6.02 | -0.21 | -34.64 | 27 |
| 35 | Bollinger breakout · 1h | breakout | 91.79 | -8.21 | 78 | 29.5 | 7.55 | 1.12 | -14.21 | 277 |
| 36 | RSI momentum · 1h | momentum | 91.69 | -8.31 | 73 | 17.8 | 0.45 | 0.27 | -25.52 | 226 |
| 37 | Supertrend · 1h | trend | 91.50 | -8.50 | 73 | 13.7 | 1.72 | 0.41 | -23.21 | 207 |
| 38 | Stochastic reversion · 1h | reversion | 91.27 | -8.73 | 119 | 47.1 | -17.57 | -3.29 | -17.97 | 359 |
| 39 | Volume breakout · 1h | breakout | 90.83 | -9.17 | 77 | 22.1 | 7.66 | 1.21 | -12.60 | 121 |
| 40 | Ichimoku · 1h | trend | 90.40 | -9.60 | 51 | 15.7 | -0.36 | 0.17 | -23.46 | 125 |
| 41 | Agent (aggressive) | meta | 90.33 | -9.67 | 37 | 32.4 | -8.47 | -2.75 | -10.83 | 121 |
| 42 | Triple EMA stack · 1h | trend | 90.22 | -9.78 | 77 | 16.9 | -11.28 | -1.02 | -34.69 | 237 |
| 43 | Connors RSI(2) · 1h | reversion | 89.38 | -10.62 | 137 | 40.1 | -23.03 | -6.86 | -24.82 | 249 |
| 44 | Z-score reversion · 1h | reversion | 89.28 | -10.72 | 65 | 35.4 | -8.90 | -1.62 | -13.36 | 163 |
| 45 | Opening range 30m | breakout | 89.19 | -10.81 | 168 | 23.2 | -13.51 | -4.00 | -17.60 | 556 |
| 46 | MFI reversion · 1h | reversion | 88.56 | -11.44 | 180 | 29.4 | -17.54 | -3.09 | -18.09 | 135 |
| 47 | OBV trend · 1h | momentum | 88.02 | -11.98 | 164 | 18.9 | -10.97 | -0.95 | -35.00 | 320 |
| 48 | Keltner breakout · 1h | breakout | 87.53 | -12.47 | 51 | 21.6 | -7.31 | -0.76 | -26.76 | 215 |
| 49 | Agent (ML meta-label) | meta | 87.47 | -12.53 | 540 | 18.1 | -3.55 | -0.42 | -14.25 | 402 |
| 50 | MACD zero-line · 1h | trend | 87.23 | -12.77 | 74 | 16.2 | -23.33 | -4.51 | -23.82 | 227 |
| 51 | Donchian 20/10 · 1h | breakout | 86.53 | -13.47 | 71 | 19.7 | -1.06 | 0.07 | -20.38 | 217 |
| 52 | VWAP momentum · 1h | momentum | 85.84 | -14.16 | 347 | 21.9 | -36.79 | -5.52 | -42.60 | 1240 |
| 53 | RSI(14) reversion · 1h | reversion | 85.68 | -14.32 | 53 | 24.5 | -4.19 | -0.56 | -14.72 | 151 |
| 54 | ROC + volume · 1h | momentum | 85.64 | -14.36 | 179 | 21.2 | -11.73 | -1.59 | -25.35 | 396 |
| 55 | Heikin-Ashi · 1h | trend | 85.58 | -14.42 | 169 | 26.0 | -31.50 | -5.16 | -39.47 | 664 |
| 56 | EMA 9/21 cross · 1h | trend | 85.04 | -14.96 | 120 | 12.5 | -10.26 | -1.18 | -26.92 | 325 |
| 57 | Opening range 15m | breakout | 84.93 | -15.07 | 214 | 20.6 | -18.22 | -4.91 | -21.41 | 692 |
| 58 | Bollinger reversion · 1h | reversion | 84.67 | -15.33 | 110 | 32.7 | -25.93 | -5.47 | -28.60 | 327 |
| 59 | Three white soldiers | momentum | 84.01 | -15.99 | 184 | 16.3 | -48.84 | -21.86 | -48.84 | 593 |
| 60 | CCI reversion · 1h | reversion | 83.77 | -16.23 | 132 | 41.7 | -16.92 | -2.22 | -20.87 | 415 |
| 61 | Williams %R · 1h | reversion | 82.31 | -17.69 | 158 | 42.4 | -33.12 | -5.47 | -34.15 | 509 |
| 62 | Candlestick reversal · 1h | reversion | 81.45 | -18.55 | 163 | 27.0 | -31.00 | -5.69 | -31.10 | 510 |
| 63 | ROC + volume | momentum | 67.43 | -32.57 | 483 | 21.5 | -74.20 | -16.33 | -76.32 | 1668 |
| 64 | Volume breakout | breakout | 65.88 | -34.12 | 307 | 13.7 | -63.16 | -17.68 | -63.17 | 886 |
| 65 | RSI(14) reversion | reversion | 65.42 | -34.58 | 543 | 26.5 | -74.09 | -16.88 | -74.32 | 1555 |
| 66 | Squeeze breakout | breakout | 64.76 | -35.24 | 400 | 14.8 | -63.22 | -17.72 | -63.22 | 1211 |
| 67 | Donchian 55/20 | breakout | 63.25 | -36.75 | 398 | 16.8 | -69.00 | -14.34 | -70.95 | 1270 |
| 68 | EMA 20/50 cross | trend | 62.11 | -37.89 | 414 | 19.1 | -77.38 | -15.07 | -78.05 | 1431 |
| 69 | VWAP reversion | reversion | 58.30 | -41.70 | 569 | 23.6 | -73.56 | -15.35 | -73.72 | 1454 |
| 70 | AI bee: Boozy | ai | 57.65 | -42.35 | 272 | 4.8 | — | — | — | — |
| 71 | Keltner breakout | breakout | 56.29 | -43.71 | 551 | 14.2 | -83.28 | -26.06 | -83.31 | 1825 |
| 72 | Supertrend | trend | 55.43 | -44.57 | 571 | 18.9 | -86.37 | -19.96 | -86.37 | 1890 |
| 73 | Ichimoku | trend | 53.88 | -46.12 | 489 | 9.8 | -81.93 | -22.26 | -81.93 | 1703 |
| 74 | AI bee: Bizzy | ai | 51.61 | -48.39 | 994 | 8.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.60 | -29.09 | -98.60 | 5295 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -29.02 | -93.44 | 2567 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.56 | -23.99 | -90.56 | 2338 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.70 | -26.21 | -91.73 | 2343 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.46 | -31.58 | -97.46 | 3506 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.53 | -34.22 | -96.53 | 3554 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.36 | -24.12 | -94.39 | 2623 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -34.96 | -99.41 | 5753 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.06 | -24.81 | -91.06 | 2610 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.33 | -30.16 | -96.33 | 3569 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -39.27 | -99.73 | 6153 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.88 | -28.79 | -91.88 | 2347 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.42 | -36.25 | -97.42 | 3637 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.54 | -35.83 | -98.55 | 4689 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.48 | -31.35 | -93.48 | 2776 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.55 | -38.18 | -99.56 | 6156 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.38 | -22.21 | -86.50 | 2101 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.91 | -26.78 | -88.02 | 2131 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.11 | -32.05 | -96.11 | 3769 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.50 | -33.03 | -89.50 | 2100 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -33.08 | -95.83 | 4074 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -43.11 | -99.89 | 8198 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T04:25 | RSI(14) reversion | sell | XRP-USD | 16.38 | 0.06 | exit signal |
| 2026-10-15T04:25 | RSI(14) reversion | sell | SOL-USD | 16.37 | 0.06 | exit signal |
| 2026-10-15T04:25 | Squeeze breakout | buy | DOGE-USD | 16.20 | — | entry signal |
| 2026-10-15T04:15 | AI bee: Bizzy | sell | SOL-USD | 7.39 | -0.07 | Jev: sell (sell p=0.71) after 11 min |
| 2026-10-15T04:04 | AI bee: Bizzy | buy | SOL-USD | 7.46 | — | Jev: buy (buy p=0.58) |
| 2026-10-15T04:00 | MFI reversion · 1h | buy | SOL-USD | 21.21 | — | entry signal |
| 2026-10-15T04:00 | MFI reversion · 1h | buy | DOGE-USD | 22.07 | — | entry signal |
| 2026-10-15T03:00 | Agent (ML meta-label) | buy | XRP-USD | 3.13 | — | entry |
| 2026-10-15T03:00 | Agent (ML meta-label) | buy | SOL-USD | 3.13 | — | entry |
| 2026-10-15T03:00 | Agent (ML meta-label) | buy | ETH-USD | 3.13 | — | entry |
| 2026-10-15T03:00 | Agent (ML meta-label) | buy | DOGE-USD | 3.13 | — | entry |
| 2026-10-15T03:00 | Agent (ML meta-label) | buy | BTC-USD | 3.13 | — | entry |
| 2026-10-15T03:00 | Williams %R · 1h | buy | XRP-USD | 1.44 | — | entry signal |
| 2026-10-15T03:00 | Williams %R · 1h | buy | SOL-USD | 11.80 | — | entry signal |
| 2026-10-15T03:00 | Williams %R · 1h | buy | ETH-USD | 11.80 | — | entry signal |
| 2026-10-15T03:00 | Williams %R · 1h | buy | DOGE-USD | 11.80 | — | entry signal |
| 2026-10-15T03:00 | Williams %R · 1h | buy | BTC-USD | 11.80 | — | entry signal |
| 2026-10-15T03:00 | Candlestick reversal · 1h | buy | XRP-USD | 4.53 | — | entry signal |
| 2026-10-15T03:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.53 | — | entry signal |
| 2026-10-15T03:00 | Candlestick reversal · 1h | buy | BTC-USD | 4.53 | — | entry signal |
| 2026-10-15T02:45 | VWAP reversion | sell | SOL-USD | 14.67 | 0.14 | exit signal |
| 2026-10-15T02:45 | VWAP reversion | sell | BTC-USD | 14.53 | -0.00 | exit signal |
| 2026-10-15T02:40 | VWAP reversion | sell | XRP-USD | 14.55 | 0.03 | exit signal |
| 2026-10-15T02:40 | RSI(14) reversion | buy | ETH-USD | 16.30 | — | entry signal |
| 2026-10-15T02:40 | RSI(14) reversion | buy | DOGE-USD | 16.34 | — | entry signal |
| 2026-10-15T02:35 | VWAP reversion | buy | ETH-USD | 14.53 | — | entry signal |
| 2026-10-15T02:35 | RSI(14) reversion | buy | SOL-USD | 16.31 | — | entry signal |
| 2026-10-15T02:31 | VWAP reversion | buy | XRP-USD | 14.53 | — | entry signal |
| 2026-10-15T02:31 | VWAP reversion | buy | SOL-USD | 14.53 | — | entry signal |
| 2026-10-15T02:31 | VWAP reversion | buy | BTC-USD | 14.53 | — | entry signal |
| 2026-10-15T02:31 | RSI(14) reversion | buy | XRP-USD | 16.32 | — | entry signal |
| 2026-10-15T02:25 | Agent (rotation) | sell | ETH-USD | 2.38 | -0.09 | selected signal exited |
| 2026-10-15T02:25 | Agent (rotation) | sell | DOGE-USD | 2.36 | -0.11 | selected signal exited |
| 2026-10-15T02:25 | Agent (ML meta-label) | sell | XRP-USD | 3.05 | -0.09 | selected signal exited |
| 2026-10-15T02:25 | Agent (ML meta-label) | sell | SOL-USD | 3.05 | -0.09 | selected signal exited |
| 2026-10-15T02:25 | Agent (ML meta-label) | sell | ETH-USD | 3.04 | -0.10 | selected signal exited |
| 2026-10-15T02:25 | Agent (ML meta-label) | sell | DOGE-USD | 3.03 | -0.11 | selected signal exited |
| 2026-10-15T02:25 | Agent (ML meta-label) | sell | BTC-USD | 3.10 | -0.05 | selected signal exited |
| 2026-10-15T02:25 | MFI reversion · 1h | sell | XRP-USD | 12.41 | -0.50 | stop-loss |
| 2026-10-15T02:25 | MFI reversion · 1h | sell | ETH-USD | 12.48 | -0.52 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 04:25:05.000157+00:00 -> 2026-10-15 04:35:05.000157+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
