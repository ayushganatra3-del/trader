# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T06:55:05.000145+00:00 · 25687 ticks

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

Today: 5277 decisions in 1056 calls, $0.0738 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T06:55 | 0 / 1 / 3 | cash |  |
| Breezy | 2026-10-17T06:55 | 0 / 4 / 0 | cash |  |
| Boozy | 2026-10-17T06:55 | 1 / 2 / 1 | COIN 68% |  |

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
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 105.88 | 5.88 | 15 | 40.0 | 8.14 | 2.02 | -7.55 | 44 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 104.81 | 4.81 | 0 | — | 5.93 | 2.81 | -5.18 | 1 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | Daily: SMA 20/50 cross · AAPL | daily | 99.92 | -0.08 | 0 | — | 4.02 | 1.59 | -5.18 | 1 |
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.40 | -3.32 | -13.79 | 136 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.85 | 1.19 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.75 | -4.41 | -12.01 | 289 |
| 17 | Hold BTC | benchmark | 96.75 | -3.25 | 0 | — | 28.98 | 3.40 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.07 | -6.36 | -22.13 | 148 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.41 | -1.49 | -13.33 | 253 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.69 | -0.30 | -22.92 | 127 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.29 | -2.19 | -9.54 | 124 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.74 | -5.99 | -11.91 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.41 | -0.05 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.09 | 0.34 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.85 | 0.94 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.31 | -0.55 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.52 | 0.39 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.09 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.76 | -1.07 | -27.05 | 207 |
| 42 | MACD cross · 1h | trend | 89.03 | -10.97 | 171 | 22.8 | -14.73 | -1.96 | -27.78 | 455 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.46 | -7.72 | -26.03 | 237 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.86 | -0.61 | -34.02 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.97 | -13.03 | 137 | 43.8 | -20.54 | -3.74 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.35 | -4.39 | -23.33 | 217 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.01 | 0.33 | -21.63 | 218 |
| 50 | Three white soldiers | momentum | 84.67 | -15.33 | 209 | 19.1 | -47.41 | -19.94 | -48.02 | 606 |
| 51 | MFI reversion · 1h | reversion | 83.98 | -16.02 | 204 | 30.4 | -21.51 | -3.61 | -22.06 | 140 |
| 52 | Z-score reversion · 1h | reversion | 83.44 | -16.56 | 86 | 31.4 | -15.39 | -2.68 | -19.86 | 181 |
| 53 | Heikin-Ashi · 1h | trend | 83.42 | -16.58 | 192 | 24.0 | -30.98 | -5.09 | -40.33 | 673 |
| 54 | VWAP momentum · 1h | momentum | 83.29 | -16.71 | 390 | 21.0 | -35.95 | -5.46 | -43.98 | 1254 |
| 55 | Agent (ML meta-label) | meta | 83.14 | -16.86 | 610 | 19.2 | -7.52 | -1.04 | -17.32 | 405 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -13.02 | -1.72 | -27.02 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.21 | -0.52 | -29.70 | 314 |
| 58 | Bollinger reversion · 1h | reversion | 80.15 | -19.85 | 138 | 31.2 | -30.26 | -6.29 | -32.42 | 340 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.32 | -5.60 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.39 | -2.56 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.03 | -2.46 | -25.55 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -34.96 | -6.30 | -35.88 | 528 |
| 63 | Volume breakout | breakout | 63.77 | -36.23 | 324 | 13.3 | -63.15 | -18.16 | -63.16 | 878 |
| 64 | ROC + volume | momentum | 63.09 | -36.91 | 551 | 22.0 | -75.85 | -17.75 | -77.42 | 1721 |
| 65 | Squeeze breakout | breakout | 62.78 | -37.22 | 431 | 14.6 | -62.92 | -17.98 | -64.17 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.37 | -37.63 | 647 | 25.8 | -74.54 | -16.68 | -74.60 | 1630 |
| 67 | Donchian 55/20 | breakout | 61.07 | -38.94 | 438 | 17.8 | -69.29 | -14.70 | -71.81 | 1288 |
| 68 | EMA 20/50 cross | trend | 59.18 | -40.82 | 460 | 19.1 | -77.11 | -15.30 | -79.22 | 1452 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 682 | 23.6 | -73.19 | -15.57 | -73.24 | 1499 |
| 70 | AI bee: Boozy | ai | 54.55 | -45.45 | 309 | 6.5 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.18 | -45.82 | 612 | 16.0 | -83.46 | -27.24 | -83.46 | 1839 |
| 72 | Ichimoku | trend | 51.11 | -48.89 | 562 | 11.6 | -82.20 | -23.48 | -82.20 | 1740 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.38 | -98.63 | 5322 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -30.79 | -93.53 | 2605 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.49 | -20.57 | -87.17 | 1916 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.94 | -90.47 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.64 | -27.15 | -91.64 | 2333 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -32.94 | -97.43 | 3529 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.78 | -37.71 | -96.78 | 3632 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.24 | -26.36 | -94.33 | 2606 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.51 | -99.39 | 5822 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.38 | -26.20 | -91.39 | 2650 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.30 | -31.96 | -96.30 | 3560 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.47 | -99.74 | 6237 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.88 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.51 | -39.64 | -97.51 | 3670 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.49 | -98.48 | 4766 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.73 | -33.90 | -93.73 | 2814 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.63 | -99.53 | 6249 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.56 | -22.35 | -86.56 | 2156 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.98 | -27.41 | -87.99 | 2152 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.94 | -33.63 | -95.94 | 3819 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.44 | -34.80 | -89.44 | 2116 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -34.59 | -95.81 | 4156 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.29 | -99.89 | 8307 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T06:50 | Ichimoku | sell | SOL-USD | 12.74 | -0.09 | exit signal |
| 2026-10-17T06:40 | Squeeze breakout | buy | ETH-USD | 15.71 | — | entry signal |
| 2026-10-17T06:35 | Ichimoku | sell | XRP-USD | 12.77 | -0.09 | exit signal |
| 2026-10-17T06:32 | AI bee: Boozy | sell | ETH-USD | 17.50 | -0.11 | Jev: buy |
| 2026-10-17T06:15 | AI bee: Boozy | buy | ETH-USD | 17.60 | — | Jev: buy (buy p=0.68) |
| 2026-10-17T06:15 | Ichimoku | buy | SOL-USD | 12.83 | — | entry signal |
| 2026-10-17T06:15 | Ichimoku | buy | DOGE-USD | 12.83 | — | entry signal |
| 2026-10-17T06:10 | Volume breakout | buy | ETH-USD | 15.95 | — | entry signal |
| 2026-10-17T06:05 | Ichimoku | sell | ETH-USD | 12.78 | -0.08 | exit signal |
| 2026-10-17T06:01 | MFI reversion · 1h | buy | BTC-USD | 21.01 | — | entry signal |
| 2026-10-17T06:01 | Stochastic reversion · 1h | sell | SOL-USD | 7.98 | 0.04 | exit signal |
| 2026-10-17T06:01 | VWAP momentum · 1h | buy | BTC-USD | 6.90 | — | entry signal |
| 2026-10-17T06:01 | VWAP momentum · 1h | sell | ETH-USD | 6.90 | -0.04 | rebalance down |
| 2026-10-17T06:01 | Heikin-Ashi · 1h | buy | ETH-USD | 20.87 | — | entry signal |
| 2026-10-17T05:45 | Three white soldiers | sell | BTC-USD | 21.06 | -0.14 | exit signal |
| 2026-10-17T05:45 | Ichimoku | buy | XRP-USD | 12.85 | — | entry signal |
| 2026-10-17T05:45 | Ichimoku | buy | ETH-USD | 12.85 | — | entry signal |
| 2026-10-17T05:30 | Ichimoku | sell | SOL-USD | 12.79 | -0.09 | exit signal |
| 2026-10-17T05:25 | EMA 20/50 cross | buy | BTC-USD | 2.95 | — | rebalance up |
| 2026-10-17T05:25 | EMA 20/50 cross | sell | ETH-USD | 2.95 | -0.01 | rebalance down |
| 2026-10-17T05:24 | AI bee: Boozy | sell | SOL-USD | 17.60 | -0.13 | Jev: sell (sell p=0.58) after 15 min |
| 2026-10-17T05:10 | Three white soldiers | buy | BTC-USD | 21.20 | — | entry signal |
| 2026-10-17T05:10 | EMA 20/50 cross | buy | BTC-USD | 2.85 | — | entry signal |
| 2026-10-17T05:09 | AI bee: Boozy | buy | SOL-USD | 17.73 | — | Jev: buy (buy p=0.68) |
| 2026-10-17T05:05 | Ichimoku | buy | SOL-USD | 12.88 | — | entry signal |
| 2026-10-17T05:00 | VWAP momentum · 1h | buy | XRP-USD | 7.69 | — | entry signal |
| 2026-10-17T05:00 | VWAP momentum · 1h | buy | DOGE-USD | 16.66 | — | entry signal |
| 2026-10-17T05:00 | VWAP momentum · 1h | sell | SOL-USD | 4.15 | -0.02 | rebalance down |
| 2026-10-17T05:00 | MACD cross · 1h | buy | XRP-USD | 4.06 | — | entry signal |
| 2026-10-17T04:55 | Keltner breakout | sell | ETH-USD | 13.55 | -0.10 | exit signal |
| 2026-10-17T04:55 | Keltner breakout | sell | DOGE-USD | 13.52 | -0.10 | exit signal |
| 2026-10-17T04:55 | Ichimoku | sell | ETH-USD | 12.87 | -0.08 | exit signal |
| 2026-10-17T04:30 | Ichimoku | sell | SOL-USD | 12.83 | -0.12 | exit signal |
| 2026-10-17T04:20 | ROC + volume | sell | SOL-USD | 15.67 | -0.14 | stop-loss |
| 2026-10-17T04:10 | EMA 20/50 cross | buy | DOGE-USD | 14.80 | — | entry signal |
| 2026-10-17T04:05 | Keltner breakout | sell | XRP-USD | 13.54 | -0.11 | stop-loss |
| 2026-10-17T04:05 | Keltner breakout | sell | SOL-USD | 13.54 | -0.11 | stop-loss |
| 2026-10-17T04:05 | Ichimoku | sell | XRP-USD | 12.84 | -0.10 | exit signal |
| 2026-10-17T04:00 | AI bee: Boozy | sell | SOL-USD | 17.73 | -0.15 | Jev: sell (sell p=0.64) after 16 min |
| 2026-10-17T04:00 | VWAP momentum · 1h | buy | ETH-USD | 20.86 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 06:55:05.000145+00:00 -> 2026-10-17 07:05:05.000145+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
