# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-05T12:55:05.000129+00:00 · 48460 ticks

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

Today: 10389 decisions in 2082 calls, $0.1452 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-05T12:55 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-11-05T12:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-05T12:55 | 2 / 3 / 0 | ETH-USD 52% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 113.12 | 13.12 | 0 | — | 14.28 | 4.94 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.47 | 5.47 | 18 | 66.7 | 6.02 | 1.88 | -4.91 | 25 |
| 3 | Daily: SMA 20/50 cross · AAPL | daily | 100.77 | 0.77 | 0 | — | 4.55 | 1.38 | -6.60 | 1 |
| 4 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 5 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 6 | VWAP reversion · 1h | reversion | 99.95 | -0.05 | 105 | 46.7 | -10.71 | -2.78 | -12.83 | 138 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 99.24 | -0.76 | 5 | 40.0 | 4.51 | 1.08 | -7.24 | 8 |
| 8 | Hold SPY | benchmark | 98.13 | -1.87 | 0 | — | -0.62 | -0.27 | -3.94 | 1 |
| 9 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 97.94 | -2.06 | 28 | 42.9 | -3.60 | -1.02 | -9.61 | 28 |
| 10 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 97.50 | -2.50 | 28 | 25.0 | 4.26 | 1.12 | -8.61 | 43 |
| 11 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 96.04 | -3.96 | 114 | 35.1 | 5.87 | 2.72 | -3.32 | 90 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 95.46 | -4.54 | 19 | 21.1 | -5.50 | -5.17 | -6.27 | 21 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 95.45 | -4.55 | 0 | — | -3.89 | -1.44 | -6.35 | 1 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.01 | -4.99 | 0 | — | -2.42 | -0.89 | -7.64 | 1 |
| 16 | Three white soldiers · 1h | momentum | 94.10 | -5.90 | 19 | 10.5 | -3.57 | -3.31 | -5.77 | 27 |
| 17 | Gap and go | momentum | 93.59 | -6.41 | 160 | 28.8 | -1.27 | -0.36 | -9.18 | 219 |
| 18 | Hold BTC | benchmark | 93.53 | -6.47 | 0 | — | -0.11 | 0.15 | -13.22 | 1 |
| 19 | Agent (rotation) | meta | 93.45 | -6.55 | 174 | 27.6 | -8.04 | -6.63 | -8.49 | 184 |
| 20 | Max aggression: 5-day momentum | meta | 91.37 | -8.63 | 16 | 43.8 | -23.80 | -1.37 | -36.71 | 25 |
| 21 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 22 | Trend pullback · 1h | trend | 90.74 | -9.26 | 103 | 22.3 | -16.46 | -6.10 | -17.67 | 79 |
| 23 | Parabolic SAR · 1h | trend | 89.81 | -10.19 | 157 | 28.0 | -14.95 | -3.31 | -19.35 | 245 |
| 24 | Copy: Insider buying | copy | 89.67 | -10.33 | 38 | 39.5 | -21.61 | -4.36 | -23.32 | 63 |
| 25 | Agent | meta | 89.49 | -10.52 | 146 | 37.7 | -11.99 | -7.17 | -12.78 | 213 |
| 26 | Opening range 30m | breakout | 88.84 | -11.16 | 365 | 32.9 | -15.74 | -5.16 | -17.21 | 589 |
| 27 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.52 | -3.28 | -14.15 | 89 |
| 28 | Daily: Bullish score | daily | 87.07 | -12.93 | 14 | 21.4 | -8.59 | -1.31 | -16.58 | 14 |
| 29 | Stochastic reversion · 1h | reversion | 86.94 | -13.06 | 249 | 47.8 | -20.39 | -3.85 | -24.97 | 380 |
| 30 | Donchian 55/20 · 1h | breakout | 86.48 | -13.53 | 62 | 12.9 | -13.41 | -2.86 | -19.91 | 105 |
| 31 | Copy: Cathie Wood (ARKK) | copy | 86.22 | -13.78 | 1 | 0.0 | -6.88 | -1.00 | -16.59 | 1 |
| 32 | Agent (aggressive) | meta | 85.25 | -14.75 | 71 | 31.0 | -12.54 | -4.14 | -14.77 | 98 |
| 33 | ADX DI cross · 1h | trend | 85.08 | -14.92 | 155 | 18.1 | -18.09 | -3.24 | -22.68 | 270 |
| 34 | MFI reversion · 1h | reversion | 84.49 | -15.51 | 324 | 34.3 | -13.54 | -2.03 | -18.45 | 151 |
| 35 | Volume breakout · 1h | breakout | 84.45 | -15.55 | 135 | 29.6 | -14.26 | -3.27 | -18.09 | 103 |
| 36 | Keltner breakout · 1h | breakout | 83.60 | -16.40 | 96 | 26.0 | -20.45 | -4.21 | -22.57 | 179 |
| 37 | Connors RSI(2) · 1h | reversion | 83.09 | -16.91 | 197 | 41.1 | -19.33 | -6.38 | -20.16 | 128 |
| 38 | Opening range 15m | breakout | 82.22 | -17.78 | 445 | 30.6 | -20.00 | -6.08 | -21.19 | 718 |
| 39 | Ichimoku · 1h | trend | 81.92 | -18.08 | 85 | 12.9 | -20.58 | -4.36 | -26.10 | 130 |
| 40 | Bollinger breakout · 1h | breakout | 81.44 | -18.56 | 150 | 26.0 | -18.52 | -3.79 | -23.94 | 250 |
| 41 | CCI reversion · 1h | reversion | 81.04 | -18.96 | 278 | 46.4 | -21.85 | -3.13 | -27.71 | 445 |
| 42 | EMA 20/50 cross · 1h | trend | 79.29 | -20.71 | 92 | 10.9 | -19.29 | -3.40 | -27.87 | 132 |
| 43 | Heikin-Ashi · 1h | trend | 78.91 | -21.09 | 375 | 22.7 | -40.55 | -8.47 | -43.89 | 678 |
| 44 | MACD zero-line · 1h | trend | 78.37 | -21.63 | 144 | 17.4 | -25.09 | -5.21 | -28.21 | 215 |
| 45 | Z-score reversion · 1h | reversion | 78.09 | -21.91 | 152 | 37.5 | -15.60 | -2.29 | -23.02 | 219 |
| 46 | MACD cross · 1h | trend | 78.01 | -22.00 | 317 | 24.0 | -30.77 | -6.01 | -33.62 | 479 |
| 47 | Supertrend · 1h | trend | 77.68 | -22.32 | 147 | 12.9 | -28.78 | -5.26 | -31.09 | 227 |
| 48 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.23 | -4.26 | -33.57 | 33 |
| 49 | Bollinger reversion · 1h | reversion | 77.00 | -23.00 | 233 | 40.3 | -28.20 | -5.52 | -30.69 | 367 |
| 50 | Williams %R · 1h | reversion | 76.72 | -23.28 | 291 | 47.4 | -33.13 | -5.95 | -34.59 | 521 |
| 51 | RSI momentum · 1h | momentum | 76.31 | -23.69 | 142 | 12.0 | -28.46 | -5.45 | -30.33 | 226 |
| 52 | Triple EMA stack · 1h | trend | 75.66 | -24.34 | 131 | 13.7 | -27.91 | -5.47 | -31.75 | 213 |
| 53 | OBV trend · 1h | momentum | 75.02 | -24.98 | 250 | 17.2 | -31.78 | -6.97 | -31.81 | 300 |
| 54 | Donchian 20/10 · 1h | breakout | 74.22 | -25.78 | 124 | 19.4 | -27.95 | -5.10 | -31.68 | 218 |
| 55 | ROC + volume · 1h | momentum | 74.19 | -25.81 | 324 | 26.2 | -33.21 | -6.41 | -36.15 | 386 |
| 56 | RSI(14) reversion · 1h | reversion | 72.28 | -27.72 | 136 | 28.7 | -20.71 | -3.44 | -26.28 | 215 |
| 57 | EMA 9/21 cross · 1h | trend | 69.41 | -30.59 | 225 | 9.8 | -37.36 | -7.65 | -39.08 | 336 |
| 58 | Candlestick reversal · 1h | reversion | 69.25 | -30.75 | 376 | 30.1 | -34.62 | -6.41 | -37.16 | 548 |
| 59 | Agent (ML meta-label) | meta | 69.17 | -30.83 | 1449 | 22.2 | -3.94 | -0.56 | -16.97 | 312 |
| 60 | VWAP momentum · 1h | momentum | 68.90 | -31.10 | 742 | 22.4 | -54.26 | -11.39 | -55.84 | 1233 |
| 61 | Three white soldiers | momentum | 67.32 | -32.67 | 445 | 16.2 | -47.21 | -21.89 | -47.21 | 635 |
| 62 | Max aggression: 1-day momentum | meta | 66.68 | -33.32 | 24 | 29.2 | -35.94 | -2.14 | -50.32 | 42 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.94 | -46.16 | -98.94 | 5173 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.94 | -25.42 | -80.10 | 1423 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.40 | -47.81 | -93.40 | 2522 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.72 | -30.99 | -88.73 | 1901 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -38.79 | -90.57 | 2303 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.98 | -32.93 | -90.98 | 2257 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.66 | -54.59 | -97.66 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.22 | -60.50 | -96.22 | 3403 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.85 | -33.79 | -93.91 | 2478 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.03 | -37.39 | -82.03 | 1655 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.47 | -54.01 | -99.47 | 5864 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.72 | -44.39 | -92.73 | 2595 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.83 | -38.01 | -95.83 | 3445 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -72.87 | -99.79 | 6160 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.63 | -44.09 | -91.63 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.65 | -26.54 | -74.70 | 1553 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -62.51 | -97.74 | 3533 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.68 | -60.17 | -98.68 | 4826 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.43 | -28.64 | -69.91 | 1195 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.57 | -55.68 | -94.57 | 2753 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.52 | -36.09 | -84.52 | 1782 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.62 | -70.51 | -99.62 | 6311 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.20 | -30.05 | -88.25 | 2241 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.33 | -18.83 | -76.67 | 1698 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.54 | -36.61 | -90.54 | 2218 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.41 | -49.81 | -96.41 | 3830 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.21 | -51.96 | -89.21 | 2149 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.48 | -27.77 | -65.56 | 807 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.52 | -25.12 | -73.64 | 1267 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.05 | -17.93 | -76.66 | 1603 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.00 | -52.06 | -97.00 | 4262 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.93 | -97.94 | -99.93 | 8230 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-05T12:40 | Williams %R · 1h | sell | DOGE-USD | 1.10 | -0.02 | stop-loss |
| 2026-11-05T12:40 | Keltner breakout · 1h | sell | ETH-USD | 5.92 | 0.15 | stop-loss |
| 2026-11-05T12:40 | Keltner breakout · 1h | sell | BTC-USD | 5.97 | 0.01 | stop-loss |
| 2026-11-05T12:40 | OBV trend · 1h | sell | DOGE-USD | 6.15 | -0.13 | stop-loss |
| 2026-11-05T12:35 | Three white soldiers · 1h | sell | XRP-USD | 23.22 | -0.41 | stop-loss |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-07 12:55:05.000129+00:00 -> 2026-11-05 13:05:05.000129+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-07 12:55:05.000129+00:00 -> 2026-11-05 13:05:05.000129+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-07 12:55:05.000129+00:00 -> 2026-11-05 13:05:05.000129+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
