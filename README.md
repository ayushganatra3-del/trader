# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T04:25:05.000155+00:00 · 25561 ticks

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

Today: 3390 decisions in 678 calls, $0.0474 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T04:25 | 1 / 3 / 1 | cash |  |
| Breezy | 2026-10-17T04:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T04:25 | 0 / 5 / 0 | COIN 68% |  |

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
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 9.03 | 1.21 | -22.12 | 109 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.33 | -2.12 | -20.62 | 75 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -9.82 | -4.04 | -11.10 | 288 |
| 17 | Hold BTC | benchmark | 96.67 | -3.33 | 0 | — | 28.85 | 3.38 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.48 | -6.46 | -22.13 | 149 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.27 | -1.46 | -13.33 | 252 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.25 | -6.75 | 96 | 21.9 | 3.29 | 0.61 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.90 | -0.33 | -22.92 | 128 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.29 | -2.19 | -9.54 | 124 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -10.74 | -5.99 | -11.91 | 243 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.38 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.25 | 0.36 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.16 | 0.98 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.17 | -0.54 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.59 | 0.40 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.09 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -9.03 | -1.11 | -27.05 | 208 |
| 42 | MACD cross · 1h | trend | 89.01 | -10.99 | 171 | 22.8 | -14.82 | -1.97 | -27.78 | 455 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.46 | -7.72 | -26.03 | 237 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.90 | -0.62 | -34.02 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.94 | -13.06 | 136 | 43.4 | -20.56 | -3.75 | -22.11 | 367 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.35 | -4.39 | -23.33 | 217 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.33 | 0.37 | -21.63 | 217 |
| 50 | Three white soldiers | momentum | 84.80 | -15.20 | 208 | 19.2 | -47.41 | -19.91 | -48.10 | 606 |
| 51 | MFI reversion · 1h | reversion | 84.04 | -15.96 | 204 | 30.4 | -21.46 | -3.60 | -22.06 | 139 |
| 52 | Heikin-Ashi · 1h | trend | 83.42 | -16.57 | 192 | 24.0 | -30.98 | -5.09 | -40.33 | 672 |
| 53 | Z-score reversion · 1h | reversion | 83.42 | -16.58 | 86 | 31.4 | -15.42 | -2.68 | -19.86 | 181 |
| 54 | VWAP momentum · 1h | momentum | 83.32 | -16.68 | 390 | 21.0 | -35.87 | -5.45 | -43.88 | 1251 |
| 55 | Agent (ML meta-label) | meta | 83.12 | -16.88 | 610 | 19.2 | -4.82 | -0.58 | -15.43 | 401 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -13.15 | -1.74 | -27.02 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.25 | -17.75 | 127 | 11.8 | -6.42 | -0.55 | -29.70 | 317 |
| 58 | Bollinger reversion · 1h | reversion | 80.15 | -19.85 | 138 | 31.2 | -30.33 | -6.31 | -32.42 | 341 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.34 | -5.60 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.46 | -2.57 | -21.70 | 168 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.03 | -2.46 | -25.55 | 429 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.03 | -6.32 | -35.88 | 531 |
| 63 | Volume breakout | breakout | 63.81 | -36.19 | 324 | 13.3 | -63.13 | -18.14 | -63.13 | 877 |
| 64 | ROC + volume | momentum | 63.09 | -36.91 | 551 | 22.0 | -75.85 | -17.75 | -77.42 | 1721 |
| 65 | Squeeze breakout | breakout | 62.84 | -37.16 | 431 | 14.6 | -62.95 | -18.01 | -64.19 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.37 | -37.63 | 647 | 25.8 | -74.52 | -16.67 | -74.57 | 1630 |
| 67 | Donchian 55/20 | breakout | 61.01 | -38.99 | 438 | 17.8 | -69.32 | -14.71 | -71.81 | 1288 |
| 68 | EMA 20/50 cross | trend | 59.13 | -40.87 | 460 | 19.1 | -77.13 | -15.31 | -79.22 | 1451 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 682 | 23.6 | -73.31 | -15.62 | -73.36 | 1502 |
| 70 | AI bee: Boozy | ai | 54.79 | -45.21 | 307 | 6.5 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.28 | -45.72 | 610 | 16.1 | -83.48 | -27.22 | -83.49 | 1841 |
| 72 | Ichimoku | trend | 51.60 | -48.40 | 556 | 11.7 | -82.06 | -23.31 | -82.06 | 1736 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -30.19 | -98.61 | 5310 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.52 | -30.72 | -93.52 | 2604 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.55 | -20.64 | -87.17 | 1918 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.52 | -25.07 | -90.52 | 2372 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.63 | -27.12 | -91.64 | 2332 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.45 | -33.16 | -97.45 | 3535 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.72 | -37.28 | -96.72 | 3622 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.38 | -26.64 | -94.43 | 2623 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -37.53 | -99.40 | 5828 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.41 | -26.25 | -91.41 | 2652 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.29 | -31.87 | -96.29 | 3558 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.93 | -99.73 | 6229 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.83 | -30.02 | -91.83 | 2375 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.49 | -39.41 | -97.49 | 3666 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.49 | -37.49 | -98.49 | 4769 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.71 | -33.66 | -93.71 | 2812 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.62 | -99.53 | 6253 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.61 | -22.41 | -86.62 | 2159 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.02 | -27.46 | -88.03 | 2154 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.95 | -33.64 | -95.95 | 3820 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.45 | -34.83 | -89.45 | 2117 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.84 | -34.66 | -95.84 | 4160 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.12 | -99.89 | 8310 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T04:20 | ROC + volume | sell | SOL-USD | 15.67 | -0.14 | stop-loss |
| 2026-10-17T04:10 | EMA 20/50 cross | buy | DOGE-USD | 14.80 | — | entry signal |
| 2026-10-17T04:05 | Keltner breakout | sell | XRP-USD | 13.54 | -0.11 | stop-loss |
| 2026-10-17T04:05 | Keltner breakout | sell | SOL-USD | 13.54 | -0.11 | stop-loss |
| 2026-10-17T04:05 | Ichimoku | sell | XRP-USD | 12.84 | -0.10 | exit signal |
| 2026-10-17T04:00 | AI bee: Boozy | sell | SOL-USD | 17.73 | -0.15 | Jev: sell (sell p=0.64) after 16 min |
| 2026-10-17T04:00 | VWAP momentum · 1h | buy | ETH-USD | 20.86 | — | entry signal |
| 2026-10-17T04:00 | MACD cross · 1h | buy | SOL-USD | 22.28 | — | entry signal |
| 2026-10-17T03:44 | AI bee: Boozy | buy | SOL-USD | 17.88 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T03:40 | Keltner breakout | buy | DOGE-USD | 13.62 | — | entry signal |
| 2026-10-17T03:40 | EMA 20/50 cross | buy | XRP-USD | 14.83 | — | entry signal |
| 2026-10-17T03:38 | AI bee: Boozy | sell | ETH-USD | 17.88 | -0.09 | Jev: buy |
| 2026-10-17T03:30 | RSI(14) reversion | sell | DOGE-USD | 15.55 | -0.05 | exit signal |
| 2026-10-17T03:30 | Keltner breakout | buy | XRP-USD | 13.65 | — | entry signal |
| 2026-10-17T03:30 | Keltner breakout | buy | SOL-USD | 13.65 | — | entry signal |
| 2026-10-17T03:30 | Keltner breakout | buy | ETH-USD | 13.65 | — | entry signal |
| 2026-10-17T03:30 | Donchian 55/20 | buy | SOL-USD | 15.29 | — | entry signal |
| 2026-10-17T03:30 | Donchian 55/20 | buy | ETH-USD | 15.29 | — | entry signal |
| 2026-10-17T03:30 | ROC + volume | buy | SOL-USD | 15.81 | — | entry signal |
| 2026-10-17T03:30 | Ichimoku | buy | XRP-USD | 12.94 | — | entry signal |
| 2026-10-17T03:30 | Ichimoku | buy | SOL-USD | 12.94 | — | entry signal |
| 2026-10-17T03:25 | VWAP reversion | sell | BTC-USD | 13.82 | -0.06 | exit signal |
| 2026-10-17T03:25 | Ichimoku | buy | ETH-USD | 12.95 | — | entry signal |
| 2026-10-17T03:25 | EMA 20/50 cross | buy | ETH-USD | 14.82 | — | entry signal |
| 2026-10-17T03:23 | AI bee: Boozy | buy | ETH-USD | 17.98 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T03:13 | AI bee: Boozy | sell | SOL-USD | 17.98 | -0.12 | Jev: sell (sell p=0.63) after 16 min |
| 2026-10-17T03:00 | VWAP momentum · 1h | buy | SOL-USD | 20.86 | — | entry signal |
| 2026-10-17T02:57 | AI bee: Boozy | buy | SOL-USD | 18.10 | — | Jev: buy (buy p=0.67) |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 04:25:05.000155+00:00 -> 2026-10-17 04:35:05.000155+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
