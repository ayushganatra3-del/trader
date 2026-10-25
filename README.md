# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T01:40:05.000153+00:00 · 34911 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £89.17 (-10.83%)

Closed trades 102, win rate 38.2%, fees £3.21, max drawdown -11.24%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-23 | PAM 12%, PEP 12%, GME 12%, BORR 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-23)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 28.30 · VIX 19.45 · last follow-through day 2026-08-04

Best bullish scores: AAPL 6.2, PLTR 6.0, SQQQ 5.5, TSLA 4.5, MSFT 4.2, MSTR 3.8

### AI bees (Jev: typesafe/jev-1.13)

Today: 1227 decisions in 246 calls, $0.0171 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T01:40 | 4 / 1 / 0 | DOGE-USD 18%, SOL-USD 15%, XRP-USD 14% |  |
| Breezy | 2026-10-25T01:40 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T01:40 | 4 / 1 / 0 | ETH-USD 60% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| VWAP momentum | PLTR | 2.11 | +6.67% | 8 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.16 | 2.01 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -11.85 | -3.25 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 5.84 | 2.80 | -1.76 | 103 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.39 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Hold BTC | benchmark | 95.52 | -4.47 | 0 | — | 0.47 | 0.25 | -9.28 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.16 | -5.84 | 25 | 40.0 | -16.19 | -3.09 | -21.83 | 67 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.75 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.85 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 29 | ADX DI cross · 1h | trend | 91.14 | -8.86 | 108 | 18.5 | -11.87 | -2.40 | -14.69 | 257 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -12.91 | -2.65 | -16.09 | 115 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 88.95 | -11.05 | 105 | 27.6 | -12.15 | -2.37 | -16.41 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.92 | -3.92 | -22.47 | 390 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.72 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.46 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.07 | -4.63 | -17.87 | 703 |
| 40 | Supertrend · 1h | trend | 85.60 | -14.40 | 109 | 14.7 | -24.21 | -5.04 | -26.85 | 215 |
| 41 | RSI momentum · 1h | momentum | 85.54 | -14.46 | 101 | 15.8 | -21.46 | -4.53 | -23.32 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 43 | MACD cross · 1h | trend | 84.52 | -15.48 | 223 | 22.9 | -23.42 | -4.64 | -26.90 | 461 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.50 | -16.50 | 109 | 33.9 | -15.57 | -2.62 | -21.48 | 206 |
| 46 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.14 | -28.32 | 211 |
| 47 | MFI reversion · 1h | reversion | 81.65 | -18.35 | 260 | 31.5 | -17.69 | -2.83 | -20.66 | 149 |
| 48 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.70 | -4.49 | -25.14 | 218 |
| 49 | Donchian 20/10 · 1h | breakout | 81.28 | -18.72 | 97 | 19.6 | -24.18 | -4.62 | -27.15 | 217 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.43 | -6.83 | -32.95 | 305 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.21 | -6.42 | -36.69 | 531 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.86 | -6.61 | -32.19 | 372 |
| 53 | Three white soldiers | momentum | 80.13 | -19.87 | 283 | 19.4 | -44.17 | -20.63 | -44.28 | 593 |
| 54 | CCI reversion · 1h | reversion | 79.84 | -20.16 | 203 | 42.4 | -27.03 | -4.03 | -28.17 | 462 |
| 55 | Agent (ML meta-label) | meta | 79.48 | -20.52 | 868 | 18.8 | -11.91 | -2.07 | -15.87 | 379 |
| 56 | Heikin-Ashi · 1h | trend | 78.95 | -21.05 | 272 | 22.8 | -43.04 | -9.88 | -44.22 | 659 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.23 | -5.96 | -31.40 | 381 |
| 58 | EMA 9/21 cross · 1h | trend | 77.03 | -22.97 | 161 | 11.8 | -30.34 | -6.14 | -33.63 | 319 |
| 59 | Candlestick reversal · 1h | reversion | 76.95 | -23.05 | 260 | 28.5 | -35.52 | -6.67 | -36.26 | 552 |
| 60 | RSI(14) reversion · 1h | reversion | 76.90 | -23.11 | 99 | 23.2 | -16.17 | -2.98 | -24.41 | 194 |
| 61 | VWAP momentum · 1h | momentum | 75.46 | -24.54 | 528 | 21.0 | -50.86 | -11.59 | -51.24 | 1227 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.96 | -43.04 | 716 | 22.3 | -75.04 | -26.75 | -75.05 | 1557 |
| 64 | Volume breakout | breakout | 55.70 | -44.30 | 433 | 12.7 | -62.22 | -26.01 | -62.22 | 782 |
| 65 | Squeeze breakout | breakout | 52.83 | -47.17 | 562 | 14.1 | -67.04 | -28.37 | -67.09 | 1160 |
| 66 | Donchian 55/20 | breakout | 52.77 | -47.23 | 569 | 19.0 | -71.66 | -22.93 | -71.91 | 1258 |
| 67 | EMA 20/50 cross | trend | 52.04 | -47.96 | 626 | 20.0 | -78.80 | -22.89 | -79.37 | 1417 |
| 68 | RSI(14) reversion | reversion | 51.34 | -48.66 | 851 | 26.2 | -77.30 | -19.74 | -77.57 | 1692 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.73 | -43.86 | -98.75 | 5066 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.85 | -43.78 | -93.94 | 2525 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.74 | -29.70 | -88.96 | 1895 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.33 | -37.04 | -91.46 | 2324 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.34 | -29.72 | -90.38 | 2153 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.80 | -51.20 | -97.84 | 3502 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.10 | -56.05 | -96.13 | 3347 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.88 | -34.27 | -93.92 | 2440 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.93 | -34.78 | -83.05 | 1693 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -52.25 | -99.41 | 5759 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.38 | -40.39 | -92.48 | 2595 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.34 | -37.96 | -95.35 | 3359 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.76 | -73.01 | -99.76 | 6145 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.28 | -43.81 | -92.32 | 2334 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.58 | -59.05 | -97.59 | 3539 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.58 | -56.47 | -98.60 | 4767 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.41 | -55.36 | -94.43 | 2757 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.95 | -38.20 | -84.02 | 1781 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.57 | -62.35 | -99.58 | 6230 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.06 | -28.61 | -88.18 | 2216 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -36.89 | -90.61 | 2265 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.18 | -46.37 | -96.20 | 3787 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.74 | -48.30 | -89.90 | 2113 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.98 | -17.73 | -76.44 | 1577 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.30 | -46.87 | -96.35 | 4162 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -92.59 | -99.91 | 8210 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T01:35 | Squeeze breakout | sell | XRP-USD | 13.19 | -0.06 | exit signal |
| 2026-10-25T01:15 | Heikin-Ashi · 1h | buy | BTC-USD | 3.93 | — | rebalance up |
| 2026-10-25T01:15 | Heikin-Ashi · 1h | sell | ETH-USD | 3.93 | -0.00 | rebalance down |
| 2026-10-25T01:12 | Agent (ML meta-label) | sell | ETH-USD | 1.03 | -0.01 | selected signal exited |
| 2026-10-25T01:10 | Volume breakout | sell | XRP-USD | 13.99 | -0.06 | exit signal |
| 2026-10-25T01:10 | Squeeze breakout | sell | DOGE-USD | 13.18 | -0.07 | stop-loss |
| 2026-10-25T01:05 | Three white soldiers | sell | SOL-USD | 20.07 | -0.13 | exit signal |
| 2026-10-25T01:05 | Three white soldiers | sell | BTC-USD | 19.95 | -0.14 | exit signal |
| 2026-10-25T01:05 | Volume breakout | sell | SOL-USD | 13.95 | -0.09 | exit signal |
| 2026-10-25T01:05 | Volume breakout | sell | ETH-USD | 13.94 | -0.10 | exit signal |
| 2026-10-25T01:05 | Volume breakout | sell | DOGE-USD | 13.82 | -0.12 | exit signal |
| 2026-10-25T01:05 | Squeeze breakout | sell | SOL-USD | 13.25 | 0.01 | exit signal |
| 2026-10-25T01:00 | Z-score reversion · 1h | buy | DOGE-USD | 1.84 | — | entry |
| 2026-10-25T01:00 | Z-score reversion · 1h | buy | BTC-USD | 6.43 | — | entry |
| 2026-10-25T01:00 | Z-score reversion · 1h | sell | XRP-USD | 8.26 | 0.13 | exit signal |
| 2026-10-25T01:00 | RSI(14) reversion · 1h | sell | SOL-USD | 8.62 | 0.12 | exit signal |
| 2026-10-25T01:00 | Bollinger breakout · 1h | buy | XRP-USD | 22.26 | — | entry signal |
| 2026-10-25T01:00 | RSI momentum · 1h | buy | XRP-USD | 21.41 | — | entry signal |
| 2026-10-25T01:00 | Heikin-Ashi · 1h | buy | BTC-USD | 11.73 | — | entry signal |
| 2026-10-25T01:00 | Heikin-Ashi · 1h | sell | DOGE-USD | 3.96 | 0.02 | rebalance down |
| 2026-10-25T01:00 | ADX DI cross · 1h | buy | XRP-USD | 22.81 | — | entry signal |
| 2026-10-25T00:50 | Volume breakout | buy | DOGE-USD | 13.94 | — | entry signal |
| 2026-10-25T00:40 | ROC + volume | sell | SOL-USD | 14.20 | -0.08 | exit signal |
| 2026-10-25T00:35 | Three white soldiers | buy | BTC-USD | 20.09 | — | entry signal |
| 2026-10-25T00:35 | ROC + volume | sell | ETH-USD | 14.19 | -0.10 | exit signal |
| 2026-10-25T00:25 | Three white soldiers | sell | DOGE-USD | 19.99 | -0.13 | exit signal |
| 2026-10-25T00:20 | Agent (ML meta-label) | buy | ETH-USD | 1.04 | — | entry |
| 2026-10-25T00:20 | Three white soldiers | buy | DOGE-USD | 20.11 | — | entry |
| 2026-10-25T00:15 | Three white soldiers | sell | DOGE-USD | 20.06 | -0.15 | exit signal |
| 2026-10-25T00:15 | Three white soldiers | sell | BTC-USD | 20.07 | -0.14 | exit signal |
| 2026-10-25T00:15 | Volume breakout | sell | BTC-USD | 13.91 | -0.11 | exit signal |
| 2026-10-25T00:00 | RSI(14) reversion · 1h | buy | ETH-USD | 8.32 | — | entry |
| 2026-10-25T00:00 | RSI(14) reversion · 1h | sell | XRP-USD | 8.32 | 0.09 | exit signal |
| 2026-10-25T00:00 | Donchian 20/10 · 1h | buy | XRP-USD | 20.32 | — | entry signal |
| 2026-10-25T00:00 | Supertrend · 1h | buy | XRP-USD | 21.10 | — | entry signal |
| 2026-10-25T00:00 | Supertrend · 1h | buy | SOL-USD | 21.41 | — | entry signal |
| 2026-10-25T00:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 12.84 | — | entry signal |
| 2026-10-24T23:40 | Volume breakout | buy | BTC-USD | 14.02 | — | entry signal |
| 2026-10-24T23:35 | Agent (ML meta-label) | sell | XRP-USD | 1.04 | 0.00 | selected signal exited |
| 2026-10-24T23:35 | MFI reversion · 1h | buy | DOGE-USD | 4.10 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 01:40:05.000153+00:00 -> 2026-10-25 01:50:05.000153+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
