# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T11:25:05.000160+00:00 · 25908 ticks

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

Today: 8592 decisions in 1719 calls, $0.1201 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T11:25 | 1 / 4 / 0 | cash |  |
| Breezy | 2026-10-17T11:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T11:25 | 1 / 4 / 0 | COIN 68% |  |

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
| 8 | VWAP reversion · 1h | reversion | 99.61 | -0.40 | 60 | 38.3 | -11.29 | -3.28 | -13.79 | 135 |
| 9 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.09 | -0.91 | 10 | 30.0 | -2.88 | -3.30 | -3.91 | 21 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 98.90 | -1.10 | 52 | 32.7 | 2.10 | 1.15 | -2.96 | 69 |
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.74 | -4.40 | -12.05 | 289 |
| 17 | Hold BTC | benchmark | 96.74 | -3.26 | 0 | — | 29.06 | 3.41 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.23 | -6.32 | -22.13 | 145 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -8.65 | -1.54 | -13.33 | 254 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.18 | -6.82 | 96 | 21.9 | -0.71 | 0.08 | -22.55 | 275 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -3.68 | -0.30 | -22.92 | 127 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -4.42 | -1.46 | -8.28 | 123 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.63 | -5.68 | -10.82 | 247 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.10 | -0.00 | -14.55 | 115 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.09 | 0.34 | -26.55 | 218 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 6.68 | 1.05 | -14.21 | 268 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.65 | -0.59 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | -3.52 | -0.29 | -20.98 | 117 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -9.26 | -1.18 | -29.71 | 211 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.02 | -0.96 | -27.05 | 204 |
| 42 | MACD cross · 1h | trend | 88.95 | -11.05 | 171 | 22.8 | -14.91 | -1.99 | -27.95 | 458 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.61 | -7.79 | -26.06 | 236 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.99 | -0.62 | -34.02 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.90 | -13.10 | 140 | 44.3 | -20.72 | -3.78 | -22.11 | 366 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.00 | -14.00 | 80 | 16.2 | -22.43 | -4.41 | -23.41 | 218 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 1.56 | 0.40 | -21.63 | 215 |
| 50 | Three white soldiers | momentum | 84.53 | -15.47 | 210 | 19.0 | -47.33 | -19.86 | -47.86 | 605 |
| 51 | MFI reversion · 1h | reversion | 83.98 | -16.02 | 204 | 30.4 | -21.51 | -3.61 | -22.06 | 140 |
| 52 | Z-score reversion · 1h | reversion | 83.42 | -16.58 | 86 | 31.4 | -15.41 | -2.68 | -19.86 | 181 |
| 53 | Heikin-Ashi · 1h | trend | 83.08 | -16.92 | 195 | 23.6 | -31.26 | -5.15 | -40.50 | 675 |
| 54 | VWAP momentum · 1h | momentum | 83.07 | -16.93 | 392 | 20.9 | -36.14 | -5.50 | -44.12 | 1254 |
| 55 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.60 | -1.65 | -27.02 | 402 |
| 56 | Agent (ML meta-label) | meta | 82.94 | -17.06 | 623 | 18.9 | -11.07 | -1.75 | -20.40 | 401 |
| 57 | EMA 9/21 cross · 1h | trend | 82.03 | -17.97 | 127 | 11.8 | -5.46 | -0.41 | -29.43 | 313 |
| 58 | Bollinger reversion · 1h | reversion | 80.09 | -19.91 | 140 | 30.7 | -30.35 | -6.31 | -32.42 | 340 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.52 | -5.64 | -35.92 | 526 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.41 | -2.56 | -21.70 | 162 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -19.09 | -2.47 | -25.55 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.10 | -6.33 | -35.88 | 531 |
| 63 | Volume breakout | breakout | 63.62 | -36.38 | 326 | 13.2 | -63.13 | -18.15 | -63.13 | 877 |
| 64 | ROC + volume | momentum | 63.09 | -36.91 | 551 | 22.0 | -75.85 | -17.75 | -77.42 | 1721 |
| 65 | Squeeze breakout | breakout | 62.53 | -37.47 | 434 | 14.5 | -62.96 | -18.01 | -64.31 | 1216 |
| 66 | RSI(14) reversion | reversion | 62.29 | -37.71 | 648 | 25.8 | -74.38 | -16.64 | -74.40 | 1626 |
| 67 | Donchian 55/20 | breakout | 60.91 | -39.09 | 440 | 17.7 | -69.26 | -14.68 | -71.81 | 1287 |
| 68 | EMA 20/50 cross | trend | 58.91 | -41.09 | 464 | 19.0 | -76.99 | -15.21 | -79.30 | 1446 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 682 | 23.6 | -73.13 | -15.54 | -73.18 | 1497 |
| 70 | AI bee: Boozy | ai | 54.12 | -45.88 | 313 | 6.4 | — | — | — | — |
| 71 | Keltner breakout | breakout | 53.99 | -46.01 | 614 | 16.0 | -83.47 | -27.30 | -83.47 | 1839 |
| 72 | Ichimoku | trend | 50.76 | -49.24 | 566 | 11.5 | -82.21 | -23.39 | -82.23 | 1739 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.63 | -30.37 | -98.63 | 5316 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.59 | -30.98 | -93.59 | 2608 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.43 | -20.51 | -87.23 | 1912 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.51 | -25.05 | -90.51 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.67 | -27.26 | -91.67 | 2335 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.42 | -32.91 | -97.42 | 3526 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.82 | -37.66 | -96.82 | 3636 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.13 | -26.38 | -94.23 | 2596 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.38 | -37.58 | -99.38 | 5811 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.38 | -26.24 | -91.38 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.34 | -32.51 | -96.34 | 3567 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.75 | -99.74 | 6245 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.69 | -29.60 | -91.70 | 2364 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.53 | -39.61 | -97.53 | 3672 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.63 | -98.48 | 4766 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.77 | -34.05 | -93.77 | 2816 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.85 | -99.53 | 6249 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.64 | -22.51 | -86.64 | 2161 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.95 | -27.35 | -87.95 | 2149 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.67 | -95.92 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.26 | -34.23 | -89.27 | 2107 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.81 | -34.64 | -95.81 | 4155 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.37 | -99.89 | 8308 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T11:20 | Squeeze breakout | sell | ETH-USD | 15.55 | -0.11 | stop-loss |
| 2026-10-17T11:20 | Ichimoku | sell | ETH-USD | 12.62 | -0.09 | exit signal |
| 2026-10-17T11:05 | Agent (ML meta-label) | sell | XRP-USD | 2.30 | -0.01 | selected signal exited |
| 2026-10-17T11:05 | Agent (ML meta-label) | sell | ETH-USD | 3.30 | -0.02 | selected signal exited |
| 2026-10-17T11:00 | Agent (ML meta-label) | sell | SOL-USD | 3.30 | -0.02 | selected signal exited |
| 2026-10-17T11:00 | Bollinger reversion · 1h | sell | XRP-USD | 8.85 | -0.05 | exit signal |
| 2026-10-17T11:00 | MACD zero-line · 1h | buy | ETH-USD | 21.53 | — | entry signal |
| 2026-10-17T11:00 | Ichimoku | buy | ETH-USD | 12.71 | — | entry signal |
| 2026-10-17T10:56 | Agent (ML meta-label) | buy | SOL-USD | 3.32 | — | entry |
| 2026-10-17T10:56 | Agent (ML meta-label) | buy | ETH-USD | 3.32 | — | entry |
| 2026-10-17T10:55 | Agent (ML meta-label) | sell | SOL-USD | 2.77 | -0.01 | selected signal exited |
| 2026-10-17T10:55 | Agent (ML meta-label) | sell | ETH-USD | 6.14 | 0.03 | selected signal exited |
| 2026-10-17T10:51 | AI bee: Boozy | sell | ETH-USD | 17.06 | -0.10 | Jev: buy |
| 2026-10-17T10:50 | RSI(14) reversion | sell | DOGE-USD | 15.51 | -0.08 | target is flat |
| 2026-10-17T10:45 | Squeeze breakout | buy | ETH-USD | 15.66 | — | entry signal |
| 2026-10-17T10:36 | AI bee: Boozy | buy | ETH-USD | 17.16 | — | Jev: buy (buy p=0.70) |
| 2026-10-17T10:25 | EMA 20/50 cross | sell | BTC-USD | 14.70 | -0.10 | exit signal |
| 2026-10-17T10:15 | EMA 20/50 cross | sell | SOL-USD | 11.96 | -0.03 | exit signal |
| 2026-10-17T10:10 | Agent (ML meta-label) | buy | SOL-USD | 2.78 | — | entry |
| 2026-10-17T10:05 | AI bee: Boozy | sell | ETH-USD | 17.16 | -0.11 | Jev: sell |
| 2026-10-17T10:05 | Agent (ML meta-label) | sell | SOL-USD | 3.43 | -0.03 | selected signal exited |
| 2026-10-17T10:05 | Keltner breakout | sell | ETH-USD | 13.42 | -0.10 | stop-loss |
| 2026-10-17T10:05 | Donchian 55/20 | sell | SOL-USD | 15.16 | -0.13 | exit signal |
| 2026-10-17T10:00 | VWAP momentum · 1h | buy | ETH-USD | 6.88 | — | rebalance up |
| 2026-10-17T10:00 | VWAP momentum · 1h | buy | BTC-USD | 13.93 | — | rebalance up |
| 2026-10-17T10:00 | VWAP momentum · 1h | sell | XRP-USD | 7.63 | -0.06 | exit signal |
| 2026-10-17T10:00 | VWAP momentum · 1h | sell | DOGE-USD | 16.54 | -0.12 | exit signal |
| 2026-10-17T10:00 | Heikin-Ashi · 1h | sell | SOL-USD | 16.75 | -0.03 | exit signal |
| 2026-10-17T10:00 | Heikin-Ashi · 1h | sell | BTC-USD | 20.69 | -0.15 | exit signal |
| 2026-10-17T10:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 20.53 | — | entry signal |
| 2026-10-17T10:00 | Donchian 55/20 | sell | BTC-USD | 15.17 | -0.11 | stop-loss |
| 2026-10-17T10:00 | Ichimoku | sell | SOL-USD | 12.64 | -0.10 | exit signal |
| 2026-10-17T09:56 | Agent (ML meta-label) | buy | XRP-USD | 2.31 | — | entry |
| 2026-10-17T09:56 | Agent (ML meta-label) | buy | DOGE-USD | 3.32 | — | entry |
| 2026-10-17T09:55 | Agent (ML meta-label) | sell | XRP-USD | 1.91 | -0.01 | selected signal exited |
| 2026-10-17T09:55 | Agent (ML meta-label) | sell | DOGE-USD | 3.72 | -0.02 | selected signal exited |
| 2026-10-17T09:55 | Keltner breakout | buy | ETH-USD | 13.52 | — | entry signal |
| 2026-10-17T09:55 | Ichimoku | buy | SOL-USD | 12.74 | — | entry signal |
| 2026-10-17T09:50 | AI bee: Boozy | buy | ETH-USD | 17.27 | — | Jev: buy (buy p=0.71) |
| 2026-10-17T09:45 | Agent (ML meta-label) | buy | XRP-USD | 1.92 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 11:25:05.000160+00:00 -> 2026-10-17 11:35:05.000160+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
