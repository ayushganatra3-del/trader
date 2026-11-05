# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T12:25:05.000158+00:00 · 48432 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.49 (-10.52%)

Closed trades 146, win rate 37.7%, fees £4.05, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, KNOP 12%, LRN 12%, ASPE 12%, MSM 12%, RAPP 12%, SRRK 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-04)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 25.08 · VIX 16.61 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.0, TSLA 6.0, LABU 6.0, IWM 5.8, TNA 5.2, AAPL 5.1

### AI bees (Jev: typesafe/jev-1.13)

Today: 9969 decisions in 1998 calls, $0.1393 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T12:25 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-05T12:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T12:25 | 1 / 4 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum · 1h | LABU | 2.22 | +16.70% | 3 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| CCI reversion · 1h | DOGE-USD | 2.01 | +6.22% | 6 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.04 | 13.04 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.69 | 0.69 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.95 | -0.05 | 105 | 46.7 | -10.73 | -2.78 | -12.84 | 138 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.17 | -0.83 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.06 | -1.94 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.38 | -4.62 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 94.94 | -5.06 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.24 | -5.76 | 18 | 11.1 | -3.42 | -3.19 | -5.62 | 27 |
| 17 | Hold BTC | benchmark | 94.11 | -5.89 | 0 | — | 0.64 | 0.28 | -13.22 | 1 |
| 18 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Max aggression: 5-day momentum | meta | 91.30 | -8.70 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.86 | -9.14 | 103 | 22.3 | -16.32 | -6.03 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.83 | -10.16 | 157 | 28.0 | -15.13 | -3.35 | -19.35 | 245 |
| 24 | Copy: Insider buying | copy | 89.61 | -10.39 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.73 | -5.15 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.45 | -3.23 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.04 | -12.96 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.88 | -13.12 | 249 | 47.8 | -20.40 | -3.85 | -24.98 | 380 |
| 30 | Donchian 55/20 · 1h | breakout | 86.75 | -13.26 | 62 | 12.9 | -13.08 | -2.78 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.16 | -13.84 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.13 | -14.87 | 155 | 18.1 | -17.97 | -3.22 | -22.68 | 270 |
| 34 | MFI reversion · 1h | reversion | 84.44 | -15.56 | 324 | 34.3 | -13.54 | -2.03 | -18.45 | 151 |
| 35 | Volume breakout · 1h | breakout | 84.41 | -15.59 | 135 | 29.6 | -14.43 | -3.31 | -18.09 | 103 |
| 36 | Keltner breakout · 1h | breakout | 83.66 | -16.34 | 94 | 24.5 | -21.57 | -4.48 | -22.57 | 176 |
| 37 | Connors RSI(2) · 1h | reversion | 83.09 | -16.91 | 197 | 41.1 | -19.33 | -6.38 | -20.16 | 128 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 82.07 | -17.93 | 85 | 12.9 | -20.38 | -4.31 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.39 | -18.61 | 150 | 26.0 | -18.68 | -3.83 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 80.99 | -19.01 | 278 | 46.4 | -21.88 | -3.14 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.46 | -20.54 | 92 | 10.9 | -19.07 | -3.35 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 78.85 | -21.15 | 375 | 22.7 | -40.55 | -8.47 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.33 | -21.67 | 144 | 17.4 | -25.09 | -5.21 | -28.21 | 215 |
| 45 | Z-score reversion · 1h | reversion | 78.04 | -21.96 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 46 | MACD cross · 1h | trend | 77.96 | -22.04 | 317 | 24.0 | -30.79 | -6.02 | -33.62 | 479 |
| 47 | Supertrend · 1h | trend | 77.80 | -22.20 | 147 | 12.9 | -28.65 | -5.23 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 76.95 | -23.05 | 233 | 40.3 | -27.79 | -5.43 | -30.29 | 367 |
| 50 | Williams %R · 1h | reversion | 76.68 | -23.32 | 290 | 47.6 | -32.58 | -5.85 | -34.03 | 522 |
| 51 | RSI momentum · 1h | momentum | 76.46 | -23.54 | 142 | 12.0 | -28.25 | -5.40 | -30.33 | 226 |
| 52 | Triple EMA stack · 1h | trend | 75.89 | -24.11 | 131 | 13.7 | -27.70 | -5.42 | -31.75 | 213 |
| 53 | OBV trend · 1h | momentum | 75.22 | -24.78 | 249 | 17.3 | -31.39 | -6.89 | -31.67 | 299 |
| 54 | Donchian 20/10 · 1h | breakout | 74.35 | -25.65 | 124 | 19.4 | -27.70 | -5.04 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.15 | -25.85 | 324 | 26.2 | -32.81 | -6.30 | -35.77 | 383 |
| 56 | RSI(14) reversion · 1h | reversion | 72.23 | -27.77 | 136 | 28.7 | -20.71 | -3.44 | -26.28 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 69.55 | -30.45 | 225 | 9.8 | -37.26 | -7.61 | -39.10 | 336 |
| 58 | Candlestick reversal · 1h | reversion | 69.23 | -30.77 | 376 | 30.1 | -34.68 | -6.39 | -37.32 | 546 |
| 59 | Agent (ML meta-label) | meta | 69.15 | -30.84 | 1449 | 22.2 | -9.51 | -1.83 | -18.11 | 317 |
| 60 | VWAP momentum · 1h | momentum | 68.95 | -31.05 | 742 | 22.4 | -54.19 | -11.37 | -55.84 | 1233 |
| 61 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.21 | -21.89 | -47.21 | 635 |
| 62 | Max aggression: 1-day momentum | meta | 66.63 | -33.37 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.93 | -46.08 | -98.93 | 5171 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.93 | -25.39 | -80.10 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.33 | -46.87 | -93.33 | 2516 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.72 | -30.99 | -88.73 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.62 | -39.23 | -90.62 | 2305 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.77 | -32.78 | -90.78 | 2242 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -54.60 | -97.66 | 3458 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.19 | -59.22 | -96.19 | 3398 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.90 | -34.09 | -93.95 | 2480 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.00 | -37.29 | -82.00 | 1654 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -53.95 | -99.47 | 5862 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -44.39 | -92.73 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.82 | -37.96 | -95.82 | 3445 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -72.70 | -99.79 | 6160 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -44.06 | -91.63 | 2259 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.65 | -26.54 | -74.70 | 1553 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.71 | -61.65 | -97.71 | 3528 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.69 | -61.23 | -98.69 | 4828 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.43 | -28.64 | -69.91 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.68 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.52 | -36.09 | -84.52 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.18 | -99.62 | 6309 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.15 | -29.90 | -88.25 | 2241 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -75.98 | -18.45 | -76.57 | 1690 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.60 | -36.92 | -90.62 | 2219 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.39 | -49.24 | -96.39 | 3826 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.23 | -52.14 | -89.23 | 2151 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.48 | -27.77 | -65.56 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -25.12 | -73.64 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.18 | -18.04 | -76.90 | 1600 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.94 | -51.02 | -96.94 | 4252 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -98.61 | -99.93 | 8231 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T12:00 | MACD cross · 1h | sell | XRP-USD | 3.86 | -0.04 | exit signal |
| 2026-11-05T12:00 | MACD cross · 1h | sell | SOL-USD | 3.87 | -0.03 | exit signal |
| 2026-11-05T11:00 | Bollinger breakout · 1h | sell | BTC-USD | 4.80 | 0.04 | exit signal |
| 2026-11-05T11:00 | VWAP momentum · 1h | sell | DOGE-USD | 6.23 | -0.05 | exit signal |
| 2026-11-05T10:05 | Three white soldiers | sell | BTC-USD | 16.74 | -0.12 | exit signal |
| 2026-11-05T10:00 | Bollinger breakout · 1h | sell | ETH-USD | 4.78 | 0.16 | exit signal |
| 2026-11-05T10:00 | Three white soldiers | buy | BTC-USD | 16.86 | — | entry signal |
| 2026-11-05T09:46 | Three white soldiers | sell | XRP-USD | 16.77 | -0.12 | exit signal |
| 2026-11-05T09:40 | Three white soldiers | buy | XRP-USD | 16.89 | — | entry signal |
| 2026-11-05T09:05 | Three white soldiers | sell | XRP-USD | 16.77 | -0.16 | stop-loss |
| 2026-11-05T09:00 | Williams %R · 1h | buy | DOGE-USD | 1.12 | — | entry signal |
| 2026-11-05T09:00 | VWAP reversion · 1h | sell | DOGE-USD | 25.01 | 0.03 | exit signal |
| 2026-11-05T09:00 | Connors RSI(2) · 1h | sell | DOGE-USD | 20.84 | 0.07 | exit signal |
| 2026-11-05T09:00 | Three white soldiers · 1h | buy | XRP-USD | 23.63 | — | entry signal |
| 2026-11-05T09:00 | OBV trend · 1h | buy | DOGE-USD | 6.28 | — | entry signal |
| 2026-11-05T09:00 | VWAP momentum · 1h | buy | SOL-USD | 6.15 | — | entry signal |
| 2026-11-05T09:00 | VWAP momentum · 1h | buy | DOGE-USD | 6.28 | — | entry signal |
| 2026-11-05T09:00 | Parabolic SAR · 1h | buy | SOL-USD | 9.99 | — | entry signal |
| 2026-11-05T09:00 | MACD cross · 1h | buy | XRP-USD | 3.90 | — | entry signal |
| 2026-11-05T09:00 | MACD cross · 1h | buy | SOL-USD | 3.90 | — | entry signal |
| 2026-11-05T08:30 | Three white soldiers | buy | XRP-USD | 16.93 | — | entry signal |
| 2026-11-05T08:00 | OBV trend · 1h | sell | DOGE-USD | 6.77 | -0.07 | exit signal |
| 2026-11-05T08:00 | VWAP momentum · 1h | sell | ETH-USD | 6.21 | -0.08 | exit signal |
| 2026-11-05T08:00 | VWAP momentum · 1h | sell | BTC-USD | 6.22 | -0.06 | exit signal |
| 2026-11-05T08:00 | MACD zero-line · 1h | sell | SOL-USD | 8.64 | 0.11 | exit signal |
| 2026-11-05T08:00 | MACD cross · 1h | sell | SOL-USD | 4.11 | 0.09 | exit signal |
| 2026-11-05T07:05 | VWAP reversion · 1h | buy | DOGE-USD | 24.98 | — | entry |
| 2026-11-05T07:00 | Connors RSI(2) · 1h | sell | ETH-USD | 20.75 | -0.03 | exit signal |
| 2026-11-05T07:00 | Connors RSI(2) · 1h | sell | BTC-USD | 20.72 | -0.06 | exit signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | XRP-USD | 5.98 | — | entry signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | ETH-USD | 6.28 | — | entry signal |
| 2026-11-05T07:00 | VWAP momentum · 1h | buy | BTC-USD | 6.28 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | ETH-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | DOGE-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Connors RSI(2) · 1h | buy | BTC-USD | 20.78 | — | entry signal |
| 2026-11-05T06:00 | Volume breakout · 1h | sell | ETH-USD | 7.04 | 0.07 | exit signal |
| 2026-11-05T06:00 | Volume breakout · 1h | sell | BTC-USD | 7.67 | -0.02 | exit signal |
| 2026-11-05T06:00 | VWAP momentum · 1h | sell | XRP-USD | 5.26 | -0.03 | exit signal |
| 2026-11-05T05:45 | Three white soldiers | sell | XRP-USD | 16.82 | -0.14 | exit signal |
| 2026-11-05T05:40 | Three white soldiers | buy | XRP-USD | 16.97 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 12:25:05.000158+00:00 -> 2026-11-05 12:35:05.000158+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 12:25:05.000158+00:00 -> 2026-11-05 12:35:05.000158+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 12:25:05.000158+00:00 -> 2026-11-05 12:35:05.000158+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
