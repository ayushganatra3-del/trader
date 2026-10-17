# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-17T08:25:05.000130+00:00 · 25761 ticks

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

Today: 6387 decisions in 1278 calls, $0.0893 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-17T08:25 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-17T08:25 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-17T08:25 | 0 / 3 / 2 | COIN 68% |  |

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
| 11 | Donchian 55/20 · 1h | breakout | 98.83 | -1.17 | 36 | 16.7 | 8.66 | 1.18 | -22.12 | 108 |
| 12 | Max aggression: 5-day momentum | meta | 98.73 | -1.27 | 8 | 37.5 | -17.17 | -1.40 | -34.64 | 26 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.63 | -1.37 | 3 | 33.3 | -0.05 | 0.12 | -7.93 | 9 |
| 14 | Hold SPY | benchmark | 98.60 | -1.40 | 0 | — | -1.57 | -0.85 | -3.23 | 1 |
| 15 | Copy: Insider buying | copy | 98.15 | -1.85 | 20 | 45.0 | -12.64 | -2.19 | -20.62 | 72 |
| 16 | Agent (rotation) | meta | 97.12 | -2.88 | 108 | 33.3 | -10.51 | -4.31 | -11.77 | 285 |
| 17 | Hold BTC | benchmark | 96.89 | -3.11 | 0 | — | 29.15 | 3.41 | -8.68 | 1 |
| 18 | Timing: Nasdaq FTD · QQQ | daily | 96.43 | -3.57 | 0 | — | -6.58 | -3.59 | -6.88 | 1 |
| 19 | Copy: Congress Democrats (NANC) | copy | 96.43 | -3.57 | 0 | — | -2.60 | -1.03 | -5.31 | 1 |
| 20 | Trend pullback · 1h | trend | 96.21 | -3.79 | 87 | 24.1 | -21.23 | -6.32 | -22.13 | 145 |
| 21 | Copy: Hedge-fund gurus (GURU) | copy | 95.55 | -4.45 | 0 | — | -6.53 | -2.56 | -7.59 | 1 |
| 22 | Three white soldiers · 1h | momentum | 95.36 | -4.64 | 12 | 0.0 | -0.34 | -0.14 | -5.23 | 31 |
| 23 | ADX DI cross · 1h | trend | 94.78 | -5.22 | 81 | 19.8 | -9.03 | -1.61 | -13.33 | 256 |
| 24 | Squeeze breakout · 1h | breakout | 93.74 | -6.26 | 41 | 24.4 | 4.03 | 0.91 | -9.46 | 99 |
| 25 | Gap and go | momentum | 93.26 | -6.74 | 67 | 13.4 | 9.12 | 2.32 | -6.78 | 197 |
| 26 | Parabolic SAR · 1h | trend | 93.17 | -6.83 | 96 | 21.9 | 3.09 | 0.58 | -22.55 | 278 |
| 27 | Daily: Momentum burst | daily | 92.99 | -7.01 | 5 | 20.0 | -7.17 | -0.95 | -20.58 | 42 |
| 28 | EMA 20/50 cross · 1h | trend | 92.91 | -7.09 | 54 | 14.8 | -4.13 | -0.37 | -22.92 | 129 |
| 29 | Agent (aggressive) | meta | 92.15 | -7.85 | 38 | 31.6 | -6.29 | -2.19 | -9.54 | 124 |
| 30 | Agent | meta | 91.99 | -8.01 | 77 | 39.0 | -9.73 | -5.90 | -10.92 | 245 |
| 31 | Volume breakout · 1h | breakout | 91.65 | -8.35 | 78 | 23.1 | -1.38 | -0.04 | -14.55 | 116 |
| 32 | Opening range 30m | breakout | 91.23 | -8.77 | 194 | 29.9 | -12.22 | -3.40 | -17.60 | 572 |
| 33 | RSI momentum · 1h | momentum | 91.18 | -8.82 | 76 | 17.1 | 1.41 | 0.38 | -26.55 | 217 |
| 34 | Bollinger breakout · 1h | breakout | 90.79 | -9.21 | 83 | 28.9 | 5.79 | 0.93 | -14.21 | 271 |
| 35 | Daily: Bullish score | daily | 90.65 | -9.35 | 7 | 0.0 | -5.99 | -0.58 | -13.10 | 13 |
| 36 | Triple EMA stack · 1h | trend | 90.39 | -9.61 | 80 | 16.2 | -7.74 | -0.60 | -33.23 | 231 |
| 37 | Ichimoku · 1h | trend | 90.28 | -9.72 | 52 | 15.4 | 1.52 | 0.39 | -22.64 | 118 |
| 38 | Timing: Nasdaq FTD · TQQQ | daily | 89.46 | -10.54 | 0 | — | -19.73 | -3.76 | -20.60 | 1 |
| 39 | Supertrend · 1h | trend | 89.29 | -10.71 | 84 | 11.9 | -3.70 | -0.22 | -30.09 | 213 |
| 40 | Copy: Cathie Wood (ARKK) | copy | 89.25 | -10.75 | 0 | — | -0.14 | 0.15 | -14.37 | 1 |
| 41 | Keltner breakout · 1h | breakout | 89.09 | -10.91 | 52 | 23.1 | -8.62 | -1.05 | -27.05 | 206 |
| 42 | MACD cross · 1h | trend | 89.00 | -11.00 | 171 | 22.8 | -14.58 | -1.93 | -27.88 | 457 |
| 43 | Connors RSI(2) · 1h | reversion | 87.98 | -12.02 | 145 | 40.0 | -25.46 | -7.72 | -26.03 | 237 |
| 44 | OBV trend · 1h | momentum | 87.98 | -12.02 | 169 | 18.3 | -7.84 | -0.61 | -34.02 | 318 |
| 45 | Stochastic reversion · 1h | reversion | 86.93 | -13.07 | 140 | 44.3 | -20.71 | -3.78 | -22.11 | 366 |
| 46 | Opening range 15m | breakout | 86.61 | -13.39 | 243 | 25.5 | -17.21 | -4.51 | -21.40 | 709 |
| 47 | MACD zero-line · 1h | trend | 86.10 | -13.90 | 80 | 16.2 | -22.35 | -4.39 | -23.33 | 217 |
| 48 | Max aggression: 1-day momentum | meta | 85.95 | -14.05 | 14 | 35.7 | -10.69 | -0.24 | -37.31 | 43 |
| 49 | Donchian 20/10 · 1h | breakout | 84.97 | -15.03 | 78 | 17.9 | 0.82 | 0.31 | -21.63 | 218 |
| 50 | Three white soldiers | momentum | 84.67 | -15.33 | 209 | 19.1 | -47.41 | -19.94 | -48.02 | 606 |
| 51 | MFI reversion · 1h | reversion | 84.01 | -15.99 | 204 | 30.4 | -21.48 | -3.60 | -22.06 | 140 |
| 52 | Z-score reversion · 1h | reversion | 83.44 | -16.56 | 86 | 31.4 | -15.39 | -2.68 | -19.86 | 181 |
| 53 | Heikin-Ashi · 1h | trend | 83.39 | -16.61 | 192 | 24.0 | -31.00 | -5.09 | -40.33 | 674 |
| 54 | VWAP momentum · 1h | momentum | 83.36 | -16.64 | 390 | 21.0 | -35.89 | -5.45 | -43.98 | 1254 |
| 55 | Agent (ML meta-label) | meta | 83.14 | -16.86 | 611 | 19.1 | -5.45 | -0.68 | -15.43 | 406 |
| 56 | ROC + volume · 1h | momentum | 82.98 | -17.02 | 192 | 21.4 | -12.97 | -1.71 | -27.02 | 404 |
| 57 | EMA 9/21 cross · 1h | trend | 82.16 | -17.84 | 127 | 11.8 | -5.77 | -0.45 | -29.38 | 314 |
| 58 | Bollinger reversion · 1h | reversion | 80.12 | -19.88 | 139 | 30.9 | -30.32 | -6.30 | -32.42 | 340 |
| 59 | Williams %R · 1h | reversion | 80.08 | -19.92 | 180 | 42.2 | -34.37 | -5.61 | -35.92 | 527 |
| 60 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 74 | 20.3 | -14.19 | -2.52 | -21.70 | 166 |
| 61 | CCI reversion · 1h | reversion | 79.03 | -20.97 | 161 | 38.5 | -18.98 | -2.45 | -25.55 | 424 |
| 62 | Candlestick reversal · 1h | reversion | 76.11 | -23.89 | 205 | 25.4 | -35.06 | -6.32 | -35.88 | 529 |
| 63 | Volume breakout | breakout | 63.62 | -36.38 | 326 | 13.2 | -63.18 | -18.19 | -63.18 | 878 |
| 64 | ROC + volume | momentum | 63.09 | -36.91 | 551 | 22.0 | -75.85 | -17.75 | -77.42 | 1721 |
| 65 | Squeeze breakout | breakout | 62.75 | -37.25 | 431 | 14.6 | -62.94 | -17.99 | -64.19 | 1217 |
| 66 | RSI(14) reversion | reversion | 62.37 | -37.63 | 647 | 25.8 | -74.57 | -16.69 | -74.63 | 1631 |
| 67 | Donchian 55/20 | breakout | 61.06 | -38.94 | 438 | 17.8 | -69.30 | -14.70 | -71.81 | 1289 |
| 68 | EMA 20/50 cross | trend | 59.23 | -40.77 | 460 | 19.1 | -77.11 | -15.29 | -79.22 | 1452 |
| 69 | VWAP reversion | reversion | 55.47 | -44.53 | 682 | 23.6 | -73.16 | -15.56 | -73.21 | 1498 |
| 70 | AI bee: Boozy | ai | 54.43 | -45.56 | 310 | 6.5 | — | — | — | — |
| 71 | Keltner breakout | breakout | 54.14 | -45.86 | 612 | 16.0 | -83.44 | -27.23 | -83.44 | 1839 |
| 72 | Ichimoku | trend | 51.02 | -48.98 | 563 | 11.5 | -82.23 | -23.51 | -82.23 | 1741 |
| 73 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.61 | -30.22 | -98.61 | 5313 |
| 74 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.55 | -30.84 | -93.55 | 2606 |
| 75 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -86.47 | -20.56 | -87.17 | 1915 |
| 76 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.46 | -24.95 | -90.48 | 2369 |
| 77 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.65 | -27.14 | -91.66 | 2333 |
| 78 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.43 | -32.98 | -97.43 | 3529 |
| 79 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.80 | -37.77 | -96.80 | 3635 |
| 80 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.10 | -26.08 | -94.22 | 2595 |
| 81 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.39 | -37.45 | -99.39 | 5815 |
| 82 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -91.36 | -26.19 | -91.36 | 2649 |
| 83 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.32 | -32.09 | -96.32 | 3563 |
| 84 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.74 | -42.53 | -99.74 | 6239 |
| 85 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.77 | -29.89 | -91.77 | 2369 |
| 86 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.52 | -39.80 | -97.52 | 3674 |
| 87 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.47 | -37.36 | -98.47 | 4761 |
| 88 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -93.75 | -34.01 | -93.75 | 2816 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.70 | -99.53 | 6250 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -86.56 | -22.35 | -86.56 | 2156 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -87.99 | -27.43 | -87.99 | 2152 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.59 | -95.92 | 3816 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.39 | -34.68 | -89.39 | 2113 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.80 | -34.56 | -95.80 | 4154 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.89 | -47.41 | -99.89 | 8310 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-17T08:10 | Volume breakout | sell | ETH-USD | 15.83 | -0.10 | exit signal |
| 2026-10-17T08:00 | Agent (ML meta-label) | buy | XRP-USD | 3.19 | — | entry |
| 2026-10-17T08:00 | Agent (ML meta-label) | sell | BTC-USD | 3.19 | -0.02 | selected signal exited |
| 2026-10-17T08:00 | Stochastic reversion · 1h | sell | BTC-USD | 7.94 | -0.00 | exit signal |
| 2026-10-17T08:00 | Bollinger reversion · 1h | buy | XRP-USD | 8.91 | — | entry |
| 2026-10-17T08:00 | Bollinger reversion · 1h | sell | DOGE-USD | 8.98 | -0.04 | exit signal |
| 2026-10-17T08:00 | Parabolic SAR · 1h | buy | ETH-USD | 23.31 | — | entry signal |
| 2026-10-17T08:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 20.56 | — | entry signal |
| 2026-10-17T07:48 | AI bee: Boozy | sell | ETH-USD | 17.38 | -0.12 | Jev: buy |
| 2026-10-17T07:35 | Volume breakout | buy | ETH-USD | 15.93 | — | entry signal |
| 2026-10-17T07:35 | Squeeze breakout | buy | BTC-USD | 15.70 | — | entry signal |
| 2026-10-17T07:35 | Keltner breakout | buy | BTC-USD | 13.54 | — | entry signal |
| 2026-10-17T07:35 | Donchian 55/20 | buy | BTC-USD | 15.28 | — | entry signal |
| 2026-10-17T07:35 | Ichimoku | buy | DOGE-USD | 12.76 | — | entry signal |
| 2026-10-17T07:33 | AI bee: Boozy | buy | ETH-USD | 17.50 | — | Jev: buy (buy p=0.69) |
| 2026-10-17T07:20 | Volume breakout | sell | ETH-USD | 15.87 | -0.08 | exit signal |
| 2026-10-17T07:20 | Ichimoku | sell | DOGE-USD | 12.72 | -0.11 | target is flat |
| 2026-10-17T07:00 | Stochastic reversion · 1h | sell | XRP-USD | 7.93 | 0.01 | exit signal |
| 2026-10-17T07:00 | Stochastic reversion · 1h | sell | ETH-USD | 7.95 | 0.02 | exit signal |
| 2026-10-17T07:00 | Heikin-Ashi · 1h | buy | XRP-USD | 20.86 | — | entry signal |
| 2026-10-17T07:00 | MACD cross · 1h | buy | BTC-USD | 11.05 | — | entry signal |
| 2026-10-17T07:00 | MACD cross · 1h | sell | SOL-USD | 11.05 | -0.07 | rebalance down |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-19 08:25:05.000130+00:00 -> 2026-10-17 08:35:05.000130+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
