# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T20:55:05.000126+00:00 · 23999 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £92.85 (-7.14%)

Closed trades 76, win rate 39.5%, fees £2.65, max drawdown -7.57%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-15 | BBD 12%, BORR 12%, GGR 12%, COE 12%, GME 12%, BPRE 12%, PSUS 12%, AXIA 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-15)

**Uptrend** since 2026-09-21 · level high · 5 distribution days in 25 sessions · timing exposure 50% · VXN 22.70 · VIX 16.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 8.5, MSFT 8.4, AAPL 6.1, META 5.7, GOOGL 5.5, MSTR 5.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 37302 decisions in 3027 calls, $0.4609 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T20:55 | 0 / 2 / 3 | MSTR 15% |  |
| Breezy | 2026-10-15T20:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T20:55 | 2 / 3 / 0 | COIN 71% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| ROC + volume | META | 1.74 | +2.50% | 3 |
| Squeeze breakout | META | 1.51 | +2.55% | 5 |
| VWAP reversion | PLTR | 1.50 | +3.07% | 7 |
| Ichimoku | NVDA | 1.50 | +0.13% | 3 |
| Connors RSI(2) · 1h | AAPL | 1.50 | +2.23% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Daily: Connors RSI(2) · 3x ETFs | daily | 105.02 | 5.02 | 1 | 100.0 | 5.79 | 1.46 | -7.93 | 9 |
| 2 | Copy: Warren Buffett (BRK-B) | copy | 104.03 | 4.03 | 0 | — | 4.58 | 2.21 | -5.18 | 1 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 103.54 | 3.54 | 10 | 70.0 | -2.42 | -0.72 | -9.61 | 27 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.11 | 3.11 | 9 | 66.7 | 4.56 | 2.04 | -3.27 | 18 |
| 5 | Hold SPY | benchmark | 100.11 | 0.10 | 0 | — | -0.55 | -0.28 | -3.26 | 1 |
| 6 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 7 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 8 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.93 | -0.07 | 14 | 35.7 | 2.16 | 0.74 | -7.55 | 43 |
| 9 | Daily: SMA 20/50 cross · AAPL | daily | 99.88 | -0.12 | 0 | — | 3.48 | 1.38 | -5.18 | 1 |
| 10 | VWAP reversion · 1h | reversion | 99.82 | -0.18 | 58 | 39.7 | -10.94 | -3.13 | -13.79 | 128 |
| 11 | Copy: Insider buying | copy | 99.40 | -0.60 | 20 | 45.0 | -16.49 | -2.63 | -21.97 | 76 |
| 12 | Copy: Congress Democrats (NANC) | copy | 98.82 | -1.18 | 0 | — | -0.59 | -0.20 | -4.45 | 1 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 14 | Timing: Nasdaq FTD · QQQ | daily | 97.85 | -2.15 | 0 | — | -5.22 | -2.90 | -6.38 | 1 |
| 15 | Hold BTC | benchmark | 97.73 | -2.27 | 0 | — | 30.01 | 3.46 | -8.68 | 1 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 17 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.03 | 0.87 | -22.11 | 113 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 97.00 | -3.00 | 0 | — | -5.50 | -2.16 | -7.50 | 1 |
| 19 | Trend pullback · 1h | trend | 96.69 | -3.31 | 86 | 24.4 | -21.45 | -6.01 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.29 | -3.71 | 11 | 0.0 | -4.10 | -3.12 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -15.89 | -5.52 | -17.79 | 295 |
| 22 | ADX DI cross · 1h | trend | 95.72 | -4.29 | 70 | 21.4 | -10.70 | -1.95 | -15.34 | 256 |
| 23 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.00 | -6.00 | 0 | — | 4.68 | 0.86 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.92 | 1.08 | -9.46 | 101 |
| 26 | Parabolic SAR · 1h | trend | 93.61 | -6.39 | 93 | 22.6 | 3.02 | 0.56 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.33 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.27 | -6.73 | 0 | — | -16.05 | -3.06 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.25 | -6.75 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.18 | -6.82 | 51 | 15.7 | 4.52 | 0.70 | -24.30 | 134 |
| 31 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.81 | -6.21 | -11.32 | 244 |
| 32 | MACD cross · 1h | trend | 92.81 | -7.19 | 154 | 22.1 | -13.33 | -1.80 | -26.23 | 460 |
| 33 | Max aggression: 5-day momentum | meta | 92.13 | -7.87 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 34 | Bollinger breakout · 1h | breakout | 92.00 | -8.00 | 79 | 30.4 | 6.45 | 1.01 | -14.21 | 273 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.22 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.51 | -8.49 | 74 | 13.5 | -1.69 | 0.02 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.34 | -8.66 | 73 | 17.8 | -0.07 | 0.21 | -26.40 | 224 |
| 39 | Stochastic reversion · 1h | reversion | 91.25 | -8.75 | 128 | 44.5 | -15.85 | -2.97 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.20 | -9.80 | 77 | 16.9 | -7.13 | -0.53 | -32.05 | 234 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -5.96 | -2.16 | -7.37 | 120 |
| 43 | MFI reversion · 1h | reversion | 89.93 | -10.07 | 191 | 30.4 | -17.58 | -3.04 | -20.76 | 145 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.93 | -25.00 | 244 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.73 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.45 | -11.55 | 73 | 35.6 | -10.28 | -1.86 | -17.27 | 183 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.93 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.90 | -12.10 | 165 | 18.8 | -10.52 | -0.89 | -34.81 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.35 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.20 | -12.80 | 568 | 18.5 | -3.20 | -0.40 | -15.24 | 417 |
| 51 | MACD zero-line · 1h | trend | 86.94 | -13.06 | 74 | 16.2 | -22.28 | -4.33 | -22.42 | 229 |
| 52 | VWAP momentum · 1h | momentum | 86.45 | -13.55 | 354 | 21.8 | -34.48 | -5.00 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.32 | -13.68 | 170 | 26.5 | -29.97 | -4.83 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 86.03 | -13.97 | 180 | 21.7 | -8.69 | -1.05 | -25.31 | 399 |
| 55 | Three white soldiers | momentum | 85.86 | -14.14 | 200 | 19.5 | -47.55 | -19.04 | -48.85 | 607 |
| 56 | Donchian 20/10 · 1h | breakout | 85.86 | -14.14 | 72 | 19.4 | -0.23 | 0.18 | -20.57 | 219 |
| 57 | Bollinger reversion · 1h | reversion | 85.03 | -14.97 | 132 | 31.8 | -26.90 | -5.81 | -31.47 | 340 |
| 58 | EMA 9/21 cross · 1h | trend | 84.62 | -15.38 | 120 | 12.5 | -5.62 | -0.44 | -29.09 | 321 |
| 59 | Williams %R · 1h | reversion | 84.03 | -15.97 | 168 | 42.9 | -31.27 | -5.11 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.39 | -16.61 | 61 | 23.0 | -12.35 | -2.31 | -18.95 | 171 |
| 61 | CCI reversion · 1h | reversion | 83.39 | -16.61 | 143 | 42.7 | -15.27 | -1.97 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 80.29 | -19.71 | 183 | 25.7 | -32.23 | -6.05 | -33.71 | 523 |
| 63 | RSI(14) reversion | reversion | 66.62 | -33.38 | 572 | 28.7 | -73.18 | -16.13 | -74.06 | 1555 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.80 | -16.99 | -76.52 | 1701 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.36 | -17.84 | -63.36 | 890 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.95 | -17.56 | -63.44 | 1218 |
| 67 | Donchian 55/20 | breakout | 63.26 | -36.74 | 418 | 18.2 | -68.96 | -14.20 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 61.93 | -38.07 | 431 | 19.7 | -77.00 | -14.85 | -78.49 | 1445 |
| 69 | AI bee: Boozy | ai | 58.77 | -41.23 | 279 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.46 | -14.94 | -72.51 | 1429 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.57 | -25.95 | -83.77 | 1853 |
| 72 | Supertrend | trend | 54.55 | -45.45 | 609 | 20.4 | -86.28 | -19.85 | -86.52 | 1913 |
| 73 | Ichimoku | trend | 53.39 | -46.61 | 530 | 11.9 | -81.97 | -22.34 | -82.04 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.36 | -48.64 | 1035 | 9.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.57 | -28.60 | -98.61 | 5289 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.42 | -28.68 | -93.47 | 2587 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -23.91 | -90.71 | 2366 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.57 | -26.18 | -91.57 | 2325 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -31.10 | -97.45 | 3517 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -34.10 | -96.57 | 3580 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.47 | -24.55 | -94.47 | 2642 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -34.41 | -99.39 | 5710 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.19 | -24.91 | -91.24 | 2640 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.21 | -30.42 | -96.21 | 3548 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.74 | -99.73 | 6154 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.68 | -28.27 | -91.77 | 2363 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.46 | -36.15 | -97.46 | 3655 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -34.82 | -98.51 | 4676 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.56 | -31.42 | -93.56 | 2797 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -37.30 | -99.54 | 6164 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.05 | -21.71 | -86.36 | 2103 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.45 | -26.23 | -87.80 | 2102 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -31.31 | -96.05 | 3757 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.32 | -32.30 | -89.47 | 2106 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -32.25 | -95.82 | 4068 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.30 | -99.89 | 8224 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T20:55 | Keltner breakout | sell | ETH-USD | 14.02 | -0.11 | stop-loss |
| 2026-10-15T20:55 | Donchian 55/20 | sell | XRP-USD | 15.77 | -0.11 | exit signal |
| 2026-10-15T20:55 | Donchian 55/20 | sell | BTC-USD | 15.77 | -0.10 | exit signal |
| 2026-10-15T20:55 | ROC + volume | sell | ETH-USD | 16.49 | -0.13 | exit signal |
| 2026-10-15T20:55 | Ichimoku | sell | SOL-USD | 13.34 | -0.13 | exit signal |
| 2026-10-15T20:55 | Ichimoku | sell | ETH-USD | 13.36 | -0.10 | exit signal |
| 2026-10-15T20:55 | Supertrend | buy | SOL-USD | 2.73 | — | rebalance up |
| 2026-10-15T20:55 | Supertrend | sell | XRP-USD | 10.88 | -0.04 | exit signal |
| 2026-10-15T20:55 | Supertrend | sell | BTC-USD | 10.88 | -0.07 | exit signal |
| 2026-10-15T20:47 | AI bee: Bizzy | sell | DOGE-USD | 7.48 | -0.05 | Jev: sell (sell p=0.78) after 10 min |
| 2026-10-15T20:37 | AI bee: Boozy | sell | ETH-USD | 17.30 | -0.09 | Jev: buy |
| 2026-10-15T20:37 | AI bee: Bizzy | buy | DOGE-USD | 7.53 | — | Jev: buy (buy p=0.59) |
| 2026-10-15T20:32 | AI bee: Bizzy | sell | ETH-USD | 7.89 | -0.05 | Jev: sell (sell p=0.59) after 12 min |
| 2026-10-15T20:20 | AI bee: Boozy | buy | ETH-USD | 17.40 | — | Jev: buy (buy p=0.71) |
| 2026-10-15T20:20 | AI bee: Bizzy | buy | ETH-USD | 7.94 | — | Jev: buy (buy p=0.62) |
| 2026-10-15T20:15 | Squeeze breakout | sell | DOGE-USD | 16.01 | -0.13 | exit signal |
| 2026-10-15T20:15 | Ichimoku | sell | XRP-USD | 13.33 | -0.11 | exit signal |
| 2026-10-15T20:15 | Ichimoku | sell | BTC-USD | 13.36 | -0.10 | stop-loss |
| 2026-10-15T20:05 | ROC + volume | sell | XRP-USD | 16.52 | -0.10 | exit signal |
| 2026-10-15T20:05 | ROC + volume | sell | DOGE-USD | 16.53 | -0.10 | exit signal |
| 2026-10-15T20:00 | CCI reversion · 1h | sell | DOGE-USD | 4.62 | 0.11 | exit signal |
| 2026-10-15T20:00 | MACD zero-line · 1h | buy | ETH-USD | 19.21 | — | entry signal |
| 2026-10-15T20:00 | MACD zero-line · 1h | buy | BTC-USD | 21.80 | — | entry signal |
| 2026-10-15T19:59 | AI bee: Bizzy | buy | MSTR | 7.46 | — | Jev: buy (buy p=0.58) |
| 2026-10-15T19:55 | Agent (rotation) | sell | TQQQ | 32.20 | 0.24 | selected signal exited |
| 2026-10-15T19:55 | Day trade: Open breakout · TQQQ/SQQQ | sell | TQQQ | 103.54 | 0.77 | target is flat |
| 2026-10-15T19:55 | MFI reversion · 1h | buy | PLTR | 1.99 | — | entry |
| 2026-10-15T19:55 | VWAP reversion | sell | SQQQ | 14.47 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | VWAP reversion | sell | AAPL | 14.59 | 0.02 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | SQQQ | 16.62 | -0.06 | end-of-day flatten |
| 2026-10-15T19:55 | RSI(14) reversion | sell | AAPL | 16.66 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TQQQ | 21.53 | 0.13 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TNA | 21.54 | 0.12 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | TECL | 21.37 | -0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Three white soldiers | sell | QQQ | 21.42 | 0.00 | end-of-day flatten |
| 2026-10-15T19:55 | Volume breakout | sell | TNA | 16.19 | -0.02 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | TSLA | 16.18 | 0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | PLTR | 16.12 | -0.05 | end-of-day flatten |
| 2026-10-15T19:55 | Squeeze breakout | sell | AMD | 13.13 | 0.21 | end-of-day flatten |
| 2026-10-15T19:55 | Keltner breakout | buy | ETH-USD | 14.13 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 20:55:05.000126+00:00 -> 2026-10-15 21:05:05.000126+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
