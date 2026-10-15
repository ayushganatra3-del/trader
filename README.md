# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-15T21:25:05.000145+00:00 · 24021 ticks

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

Today: 37632 decisions in 3093 calls, $0.4656 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-15T21:25 | 1 / 3 / 1 | SOL-USD 14%, MSTR 15% |  |
| Breezy | 2026-10-15T21:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-15T21:25 | 2 / 3 / 0 | COIN 71% |  |

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
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.73 | -1.27 | 9 | 22.2 | -3.24 | -3.74 | -3.91 | 20 |
| 13 | Copy: Congress Democrats (NANC) | copy | 98.72 | -1.28 | 0 | — | -0.70 | -0.25 | -4.45 | 1 |
| 14 | Hold BTC | benchmark | 98.01 | -1.99 | 0 | — | 30.62 | 3.51 | -8.68 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.85 | -2.15 | 0 | — | -5.22 | -2.90 | -6.38 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 97.66 | -2.34 | 0 | — | -4.87 | -1.94 | -7.50 | 1 |
| 17 | Day trade: Stocks in Play ORB | daytrade | 97.63 | -2.37 | 51 | 31.4 | 0.84 | 0.50 | -2.85 | 68 |
| 18 | Donchian 55/20 · 1h | breakout | 97.05 | -2.95 | 36 | 16.7 | 6.03 | 0.87 | -22.11 | 113 |
| 19 | Trend pullback · 1h | trend | 96.69 | -3.31 | 86 | 24.4 | -21.45 | -6.01 | -23.30 | 155 |
| 20 | Three white soldiers · 1h | momentum | 96.29 | -3.71 | 11 | 0.0 | -4.10 | -3.12 | -5.31 | 31 |
| 21 | Agent (rotation) | meta | 96.08 | -3.92 | 106 | 32.1 | -14.74 | -4.75 | -16.67 | 289 |
| 22 | ADX DI cross · 1h | trend | 95.76 | -4.25 | 71 | 21.1 | -10.45 | -1.90 | -15.34 | 255 |
| 23 | Daily: Momentum burst | daily | 95.64 | -4.36 | 5 | 20.0 | -4.65 | -0.55 | -17.75 | 39 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 94.00 | -6.00 | 0 | — | 4.68 | 0.86 | -13.89 | 1 |
| 25 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.71 | 1.03 | -9.46 | 102 |
| 26 | Parabolic SAR · 1h | trend | 93.61 | -6.39 | 93 | 22.6 | 3.02 | 0.56 | -22.05 | 281 |
| 27 | Gap and go | momentum | 93.38 | -6.62 | 66 | 13.6 | 9.28 | 2.33 | -6.78 | 199 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 93.27 | -6.73 | 0 | — | -16.05 | -3.06 | -19.22 | 1 |
| 29 | Daily: Bullish score | daily | 93.25 | -6.75 | 7 | 0.0 | -4.32 | -0.36 | -12.76 | 13 |
| 30 | EMA 20/50 cross · 1h | trend | 93.18 | -6.82 | 51 | 15.7 | 4.27 | 0.67 | -24.30 | 135 |
| 31 | MACD cross · 1h | trend | 92.90 | -7.10 | 154 | 22.1 | -13.26 | -1.78 | -26.23 | 460 |
| 32 | Agent | meta | 92.85 | -7.14 | 76 | 39.5 | -10.81 | -6.21 | -11.32 | 244 |
| 33 | Bollinger breakout · 1h | breakout | 92.14 | -7.86 | 79 | 30.4 | 6.61 | 1.03 | -14.21 | 273 |
| 34 | Max aggression: 5-day momentum | meta | 92.13 | -7.87 | 8 | 37.5 | -7.43 | -0.37 | -34.64 | 26 |
| 35 | Opening range 30m | breakout | 91.78 | -8.22 | 188 | 30.3 | -11.77 | -3.22 | -17.60 | 567 |
| 36 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -2.60 | -0.23 | -14.55 | 117 |
| 37 | Supertrend · 1h | trend | 91.58 | -8.42 | 74 | 13.5 | -1.61 | 0.02 | -28.77 | 213 |
| 38 | RSI momentum · 1h | momentum | 91.44 | -8.56 | 73 | 17.8 | 0.03 | 0.22 | -26.40 | 224 |
| 39 | Stochastic reversion · 1h | reversion | 91.25 | -8.75 | 128 | 44.5 | -15.85 | -2.97 | -19.84 | 349 |
| 40 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 0.96 | 0.32 | -22.64 | 122 |
| 41 | Triple EMA stack · 1h | trend | 90.20 | -9.80 | 77 | 16.9 | -7.30 | -0.55 | -32.05 | 235 |
| 42 | Agent (aggressive) | meta | 90.18 | -9.82 | 38 | 31.6 | -5.96 | -2.16 | -7.37 | 120 |
| 43 | MFI reversion · 1h | reversion | 90.02 | -9.98 | 191 | 30.4 | -17.53 | -3.03 | -20.79 | 145 |
| 44 | Connors RSI(2) · 1h | reversion | 89.76 | -10.24 | 143 | 40.6 | -23.27 | -6.93 | -25.00 | 244 |
| 45 | Max aggression: 1-day momentum ⏸ | meta | 89.13 | -10.88 | 14 | 35.7 | -18.65 | -0.73 | -37.31 | 43 |
| 46 | Z-score reversion · 1h | reversion | 88.47 | -11.53 | 73 | 35.6 | -10.26 | -1.85 | -17.27 | 182 |
| 47 | Keltner breakout · 1h | breakout | 88.13 | -11.87 | 52 | 23.1 | -14.02 | -1.93 | -29.15 | 211 |
| 48 | OBV trend · 1h | momentum | 87.90 | -12.10 | 165 | 18.8 | -10.52 | -0.89 | -34.81 | 315 |
| 49 | Opening range 15m | breakout | 87.32 | -12.68 | 237 | 25.7 | -16.89 | -4.35 | -21.40 | 704 |
| 50 | Agent (ML meta-label) | meta | 87.25 | -12.75 | 568 | 18.5 | -5.11 | -0.71 | -16.28 | 427 |
| 51 | MACD zero-line · 1h | trend | 87.11 | -12.89 | 74 | 16.2 | -22.10 | -4.29 | -22.42 | 229 |
| 52 | VWAP momentum · 1h | momentum | 86.52 | -13.48 | 354 | 21.8 | -34.45 | -4.99 | -43.06 | 1256 |
| 53 | Heikin-Ashi · 1h | trend | 86.36 | -13.64 | 171 | 26.3 | -29.94 | -4.82 | -39.15 | 672 |
| 54 | ROC + volume · 1h | momentum | 86.17 | -13.83 | 180 | 21.7 | -8.56 | -1.03 | -25.31 | 399 |
| 55 | Donchian 20/10 · 1h | breakout | 86.02 | -13.98 | 72 | 19.4 | -0.08 | 0.20 | -20.57 | 219 |
| 56 | Three white soldiers | momentum | 85.86 | -14.14 | 200 | 19.5 | -47.55 | -19.04 | -48.85 | 607 |
| 57 | Bollinger reversion · 1h | reversion | 85.03 | -14.97 | 132 | 31.8 | -26.92 | -5.81 | -31.47 | 340 |
| 58 | EMA 9/21 cross · 1h | trend | 84.73 | -15.27 | 120 | 12.5 | -5.53 | -0.43 | -29.09 | 322 |
| 59 | Williams %R · 1h | reversion | 84.03 | -15.97 | 168 | 42.9 | -31.28 | -5.12 | -34.85 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 83.41 | -16.59 | 61 | 23.0 | -12.58 | -2.36 | -18.95 | 171 |
| 61 | CCI reversion · 1h | reversion | 83.39 | -16.61 | 143 | 42.7 | -15.27 | -1.97 | -23.38 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 80.30 | -19.70 | 184 | 25.5 | -32.20 | -6.04 | -33.69 | 522 |
| 63 | RSI(14) reversion | reversion | 66.62 | -33.38 | 572 | 28.7 | -73.17 | -16.12 | -74.05 | 1554 |
| 64 | ROC + volume | momentum | 66.12 | -33.88 | 527 | 22.6 | -74.80 | -16.99 | -76.52 | 1701 |
| 65 | Volume breakout | breakout | 64.80 | -35.20 | 317 | 13.6 | -63.36 | -17.84 | -63.36 | 890 |
| 66 | Squeeze breakout | breakout | 64.49 | -35.51 | 420 | 15.0 | -62.96 | -17.57 | -63.44 | 1218 |
| 67 | Donchian 55/20 | breakout | 63.33 | -36.67 | 418 | 18.2 | -68.93 | -14.18 | -71.15 | 1282 |
| 68 | EMA 20/50 cross | trend | 62.07 | -37.93 | 431 | 19.7 | -76.95 | -14.82 | -78.49 | 1445 |
| 69 | AI bee: Boozy | ai | 58.77 | -41.23 | 279 | 5.4 | — | — | — | — |
| 70 | VWAP reversion | reversion | 57.99 | -42.01 | 586 | 24.6 | -72.46 | -14.94 | -72.51 | 1429 |
| 71 | Keltner breakout | breakout | 56.36 | -43.64 | 590 | 16.4 | -83.55 | -25.92 | -83.74 | 1852 |
| 72 | Supertrend | trend | 54.64 | -45.36 | 609 | 20.4 | -86.26 | -19.85 | -86.54 | 1914 |
| 73 | Ichimoku | trend | 53.39 | -46.61 | 530 | 11.9 | -81.97 | -22.34 | -82.04 | 1727 |
| 74 | AI bee: Bizzy | ai | 51.35 | -48.65 | 1035 | 9.2 | — | — | — | — |
| 75 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.56 | -28.46 | -98.60 | 5285 |
| 76 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.44 | -28.74 | -93.47 | 2589 |
| 77 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.55 | -23.89 | -90.71 | 2366 |
| 78 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.58 | -26.21 | -91.58 | 2328 |
| 79 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -31.06 | -97.44 | 3516 |
| 80 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.57 | -34.12 | -96.58 | 3582 |
| 81 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.46 | -24.57 | -94.46 | 2641 |
| 82 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -34.31 | -99.39 | 5710 |
| 83 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.18 | -24.90 | -91.24 | 2640 |
| 84 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.22 | -30.46 | -96.22 | 3548 |
| 85 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -38.75 | -99.73 | 6155 |
| 86 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.67 | -28.25 | -91.76 | 2362 |
| 87 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.44 | -36.14 | -97.44 | 3651 |
| 88 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.45 | -34.64 | -98.50 | 4676 |
| 89 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.56 | -31.43 | -93.56 | 2797 |
| 90 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.54 | -37.23 | -99.54 | 6168 |
| 91 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.05 | -21.71 | -86.36 | 2104 |
| 92 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.44 | -26.20 | -87.77 | 2102 |
| 93 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.93 | -31.15 | -96.03 | 3756 |
| 94 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.35 | -32.36 | -89.47 | 2107 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.70 | -32.18 | -95.82 | 4069 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -42.26 | -99.89 | 8225 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-15T21:18 | AI bee: Bizzy | buy | SOL-USD | 7.13 | — | Jev: buy (buy p=0.56) |
| 2026-10-15T21:01 | Candlestick reversal · 1h | sell | XRP-USD | 3.27 | -0.01 | exit signal |
| 2026-10-15T21:01 | Heikin-Ashi · 1h | sell | BTC-USD | 6.10 | -0.05 | exit signal |
| 2026-10-15T21:01 | ADX DI cross · 1h | sell | BTC-USD | 9.52 | -0.11 | exit signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-17 21:25:05.000145+00:00 -> 2026-10-15 21:35:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
