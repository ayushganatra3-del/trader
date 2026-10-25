# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-25T05:10:05.000123+00:00 · 35083 ticks

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

Today: 3795 decisions in 762 calls, $0.0530 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-25T05:10 | 1 / 0 / 4 | cash |  |
| Breezy | 2026-10-25T05:10 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-25T05:10 | 1 / 4 / 0 | ETH-USD 57% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | BITX | 2.56 | +2.84% | 15 |
| VWAP momentum | PLTR | 2.20 | +6.89% | 7 |
| Connors RSI(2) | TSLA | 2.20 | +0.57% | 9 |
| Connors RSI(2) | LABU | 1.86 | +3.56% | 15 |
| RSI momentum | MSTR | 1.77 | +12.68% | 6 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 106.49 | 6.49 | 0 | — | 7.97 | 4.13 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 105.90 | 5.89 | 13 | 69.2 | 3.53 | 1.18 | -6.08 | 25 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 103.59 | 3.59 | 20 | 30.0 | 7.21 | 1.95 | -5.17 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.52 | 3.52 | 18 | 44.4 | 6.17 | 2.02 | -4.92 | 26 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.82 | 0.82 | 0 | — | 3.44 | 1.60 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.50 | 0.50 | 89 | 44.9 | -12.07 | -3.34 | -13.74 | 156 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 98.93 | -1.07 | 74 | 33.8 | 6.21 | 2.99 | -1.37 | 102 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.21 | -1.78 | 13 | 23.1 | -3.70 | -4.33 | -4.06 | 22 |
| 11 | Hold SPY | benchmark | 97.84 | -2.17 | 0 | — | -0.72 | -0.38 | -3.13 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.43 | -2.18 | -5.83 | 1 |
| 13 | Agent (rotation) | meta | 96.13 | -3.87 | 120 | 30.8 | -2.31 | -1.33 | -6.22 | 195 |
| 14 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 3.40 | 0.85 | -7.93 | 8 |
| 15 | Copy: Congress Democrats (NANC) | copy | 95.69 | -4.31 | 0 | — | -0.88 | -0.31 | -5.99 | 1 |
| 16 | Hold BTC | benchmark | 95.60 | -4.40 | 0 | — | 0.55 | 0.26 | -9.28 | 1 |
| 17 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.19 | -2.02 | -4.59 | 26 |
| 18 | Copy: Hedge-fund gurus (GURU) | copy | 94.55 | -5.45 | 0 | — | -6.51 | -2.72 | -7.76 | 1 |
| 19 | Copy: Insider buying | copy | 94.13 | -5.87 | 25 | 40.0 | -17.34 | -3.33 | -21.47 | 61 |
| 20 | Gap and go | momentum | 93.96 | -6.04 | 92 | 21.7 | 4.76 | 1.57 | -8.68 | 184 |
| 21 | Trend pullback · 1h | trend | 93.76 | -6.24 | 95 | 23.2 | -21.52 | -6.94 | -21.82 | 115 |
| 22 | Donchian 55/20 · 1h | breakout | 93.15 | -6.85 | 48 | 16.7 | -15.71 | -3.50 | -17.07 | 97 |
| 23 | Opening range 30m | breakout | 92.94 | -7.06 | 253 | 34.4 | -11.16 | -3.42 | -17.21 | 562 |
| 24 | Max aggression: 5-day momentum | meta | 92.92 | -7.08 | 11 | 45.5 | -14.93 | -1.36 | -27.80 | 24 |
| 25 | Parabolic SAR · 1h | trend | 92.04 | -7.96 | 118 | 25.4 | -20.83 | -4.85 | -24.17 | 253 |
| 26 | Daily: Momentum burst | daily | 91.73 | -8.27 | 10 | 10.0 | -17.52 | -3.35 | -20.97 | 40 |
| 27 | Squeeze breakout · 1h | breakout | 91.34 | -8.66 | 51 | 23.5 | -3.43 | -0.82 | -11.55 | 92 |
| 28 | ADX DI cross · 1h | trend | 91.26 | -8.74 | 108 | 18.5 | -11.75 | -2.37 | -14.69 | 257 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.96 | -2.35 | -16.91 | 1 |
| 30 | Daily: Bullish score | daily | 89.55 | -10.45 | 9 | 0.0 | -8.04 | -1.03 | -14.40 | 14 |
| 31 | Volume breakout · 1h | breakout | 89.39 | -10.61 | 102 | 23.5 | -13.75 | -2.78 | -16.90 | 115 |
| 32 | Agent | meta | 89.17 | -10.83 | 102 | 38.2 | -11.63 | -7.70 | -12.35 | 210 |
| 33 | Copy: Cathie Wood (ARKK) | copy | 89.16 | -10.85 | 0 | — | -5.31 | -0.76 | -14.52 | 1 |
| 34 | Bollinger breakout · 1h | breakout | 89.07 | -10.93 | 105 | 27.6 | -12.03 | -2.34 | -16.40 | 241 |
| 35 | Agent (aggressive) | meta | 87.24 | -12.76 | 48 | 35.4 | -12.42 | -4.23 | -14.77 | 95 |
| 36 | Stochastic reversion · 1h | reversion | 87.18 | -12.82 | 186 | 45.2 | -20.93 | -3.92 | -22.47 | 390 |
| 37 | Keltner breakout · 1h | breakout | 86.31 | -13.69 | 73 | 23.3 | -22.60 | -4.72 | -24.23 | 189 |
| 38 | EMA 20/50 cross · 1h | trend | 86.14 | -13.86 | 71 | 11.3 | -22.71 | -4.46 | -25.03 | 138 |
| 39 | Opening range 15m | breakout | 86.12 | -13.88 | 318 | 30.5 | -16.06 | -4.63 | -17.87 | 703 |
| 40 | RSI momentum · 1h | momentum | 85.66 | -14.34 | 101 | 15.8 | -21.36 | -4.51 | -23.32 | 216 |
| 41 | Supertrend · 1h | trend | 85.63 | -14.37 | 109 | 14.7 | -24.22 | -5.04 | -26.85 | 216 |
| 42 | Connors RSI(2) · 1h | reversion | 85.40 | -14.60 | 173 | 40.5 | -26.20 | -7.92 | -26.96 | 196 |
| 43 | MACD cross · 1h | trend | 84.57 | -15.43 | 223 | 22.9 | -23.37 | -4.62 | -26.90 | 461 |
| 44 | Ichimoku · 1h | trend | 83.91 | -16.09 | 65 | 12.3 | -23.25 | -4.74 | -25.24 | 110 |
| 45 | Z-score reversion · 1h | reversion | 83.50 | -16.50 | 109 | 33.9 | -15.55 | -2.62 | -21.48 | 206 |
| 46 | Triple EMA stack · 1h | trend | 83.47 | -16.53 | 98 | 15.3 | -26.12 | -5.14 | -28.32 | 211 |
| 47 | MFI reversion · 1h | reversion | 81.68 | -18.32 | 260 | 31.5 | -17.57 | -2.81 | -20.56 | 149 |
| 48 | MACD zero-line · 1h | trend | 81.57 | -18.43 | 105 | 15.2 | -21.70 | -4.49 | -25.23 | 219 |
| 49 | Donchian 20/10 · 1h | breakout | 81.39 | -18.61 | 97 | 19.6 | -24.07 | -4.59 | -27.15 | 217 |
| 50 | OBV trend · 1h | momentum | 81.10 | -18.90 | 203 | 17.2 | -31.43 | -6.83 | -32.95 | 305 |
| 51 | Williams %R · 1h | reversion | 80.93 | -19.07 | 213 | 44.1 | -36.21 | -6.42 | -36.69 | 531 |
| 52 | Bollinger reversion · 1h | reversion | 80.19 | -19.81 | 171 | 34.5 | -31.86 | -6.61 | -32.19 | 372 |
| 53 | Three white soldiers | momentum | 80.13 | -19.87 | 283 | 19.4 | -44.20 | -20.68 | -44.31 | 594 |
| 54 | CCI reversion · 1h | reversion | 79.82 | -20.18 | 204 | 42.2 | -27.04 | -4.03 | -28.17 | 462 |
| 55 | Agent (ML meta-label) | meta | 79.41 | -20.59 | 871 | 18.8 | -15.88 | -3.08 | -17.39 | 392 |
| 56 | Heikin-Ashi · 1h | trend | 79.06 | -20.94 | 272 | 22.8 | -42.96 | -9.85 | -44.22 | 659 |
| 57 | ROC + volume · 1h | momentum | 78.19 | -21.81 | 240 | 23.8 | -30.38 | -5.99 | -31.55 | 380 |
| 58 | EMA 9/21 cross · 1h | trend | 77.02 | -22.98 | 161 | 11.8 | -30.43 | -6.16 | -33.63 | 323 |
| 59 | Candlestick reversal · 1h | reversion | 76.92 | -23.08 | 261 | 28.4 | -35.49 | -6.66 | -36.26 | 551 |
| 60 | RSI(14) reversion · 1h | reversion | 76.90 | -23.10 | 99 | 23.2 | -16.16 | -2.98 | -24.41 | 194 |
| 61 | VWAP momentum · 1h | momentum | 75.40 | -24.60 | 529 | 21.0 | -50.95 | -11.64 | -51.19 | 1232 |
| 62 | Max aggression: 1-day momentum | meta | 67.41 | -32.59 | 18 | 27.8 | -42.46 | -2.93 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 56.96 | -43.04 | 716 | 22.3 | -74.85 | -26.52 | -74.86 | 1554 |
| 64 | Volume breakout | breakout | 55.59 | -44.41 | 434 | 12.7 | -62.38 | -26.10 | -62.38 | 784 |
| 65 | Donchian 55/20 | breakout | 52.80 | -47.20 | 570 | 18.9 | -71.65 | -22.92 | -71.91 | 1258 |
| 66 | Squeeze breakout | breakout | 52.63 | -47.37 | 564 | 14.0 | -67.16 | -28.65 | -67.22 | 1162 |
| 67 | EMA 20/50 cross | trend | 52.11 | -47.89 | 626 | 20.0 | -78.77 | -22.83 | -79.37 | 1417 |
| 68 | RSI(14) reversion | reversion | 51.34 | -48.66 | 851 | 26.2 | -77.30 | -19.74 | -77.58 | 1692 |
| 69 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.77 | -44.86 | -98.79 | 5082 |
| 70 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.90 | -44.60 | -93.94 | 2529 |
| 71 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.75 | -29.73 | -88.96 | 1895 |
| 72 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.34 | -37.09 | -91.46 | 2324 |
| 73 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.40 | -29.99 | -90.43 | 2157 |
| 74 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -52.12 | -97.84 | 3506 |
| 75 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.16 | -58.27 | -96.17 | 3363 |
| 76 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.05 | -35.31 | -94.08 | 2459 |
| 77 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.17 | -35.88 | -83.21 | 1699 |
| 78 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.40 | -52.15 | -99.41 | 5764 |
| 79 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.41 | -40.66 | -92.48 | 2596 |
| 80 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.42 | -38.67 | -95.42 | 3373 |
| 81 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -77.31 | -99.77 | 6160 |
| 82 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.28 | -43.90 | -92.32 | 2335 |
| 83 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.63 | -61.84 | -97.63 | 3550 |
| 84 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.59 | -57.20 | -98.61 | 4772 |
| 85 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 86 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.52 | -58.24 | -94.54 | 2768 |
| 87 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.05 | -38.70 | -84.11 | 1784 |
| 88 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -63.64 | -99.58 | 6237 |
| 89 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.06 | -28.61 | -88.18 | 2216 |
| 90 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -37.07 | -90.59 | 2266 |
| 91 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.19 | -46.48 | -96.20 | 3788 |
| 92 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.72 | -48.36 | -89.87 | 2113 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -75.96 | -17.74 | -76.42 | 1576 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.31 | -47.12 | -96.35 | 4164 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -100.86 | -99.92 | 8228 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-25T05:00 | Supertrend · 1h | buy | DOGE-USD | 14.04 | — | entry |
| 2026-10-25T05:00 | Supertrend · 1h | sell | XRP-USD | 6.96 | 0.04 | rebalance down |
| 2026-10-25T05:00 | Supertrend · 1h | sell | SOL-USD | 7.08 | -0.02 | rebalance down |
| 2026-10-25T05:00 | EMA 9/21 cross · 1h | buy | DOGE-USD | 5.22 | — | entry signal |
| 2026-10-25T05:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 5.22 | 0.03 | rebalance down |
| 2026-10-25T04:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.82 | — | entry |
| 2026-10-25T04:00 | Candlestick reversal · 1h | sell | BTC-USD | 4.82 | -0.03 | exit signal |
| 2026-10-25T04:00 | VWAP momentum · 1h | buy | DOGE-USD | 7.11 | — | entry signal |
| 2026-10-25T04:00 | VWAP momentum · 1h | sell | BTC-USD | 7.11 | -0.02 | exit signal |
| 2026-10-25T03:45 | Squeeze breakout | sell | BTC-USD | 13.12 | -0.09 | exit signal |
| 2026-10-25T03:41 | Agent (ML meta-label) | sell | ETH-USD | 4.38 | -0.03 | selected signal exited |
| 2026-10-25T03:15 | Volume breakout | sell | XRP-USD | 13.81 | -0.11 | exit signal |
| 2026-10-25T03:11 | Agent (ML meta-label) | buy | ETH-USD | 4.41 | — | entry |
| 2026-10-25T03:05 | Squeeze breakout | sell | SOL-USD | 13.10 | -0.11 | exit signal |
| 2026-10-25T03:05 | Donchian 55/20 | buy | ETH-USD | 2.87 | — | rebalance up |
| 2026-10-25T03:05 | Donchian 55/20 | buy | BTC-USD | 2.66 | — | rebalance up |
| 2026-10-25T03:05 | Donchian 55/20 | sell | DOGE-USD | 10.50 | -0.07 | exit signal |
| 2026-10-25T03:00 | Agent (ML meta-label) | sell | DOGE-USD | 4.38 | -0.03 | selected signal exited |
| 2026-10-25T03:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 6.18 | — | entry signal |
| 2026-10-25T02:55 | Agent (ML meta-label) | buy | DOGE-USD | 4.42 | — | entry |
| 2026-10-25T02:55 | Volume breakout | buy | XRP-USD | 13.93 | — | entry signal |
| 2026-10-25T02:40 | Squeeze breakout | buy | SOL-USD | 13.21 | — | entry signal |
| 2026-10-25T02:40 | Squeeze breakout | buy | BTC-USD | 13.21 | — | entry signal |
| 2026-10-25T02:00 | Agent (ML meta-label) | sell | DOGE-USD | 4.23 | 0.05 | selected signal exited |
| 2026-10-25T02:00 | CCI reversion · 1h | buy | ETH-USD | 3.46 | — | entry |
| 2026-10-25T02:00 | CCI reversion · 1h | sell | BTC-USD | 3.46 | -0.01 | exit signal |
| 2026-10-25T02:00 | MACD zero-line · 1h | buy | XRP-USD | 20.39 | — | entry signal |
| 2026-10-25T02:00 | EMA 9/21 cross · 1h | buy | SOL-USD | 11.01 | — | entry signal |
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

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-27 05:10:05.000123+00:00 -> 2026-10-25 05:20:05.000123+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
