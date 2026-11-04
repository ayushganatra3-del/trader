# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-04T07:55:05.000166+00:00 · 47045 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 143, win rate 38.5%, fees £3.99, max drawdown -11.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-04 | BBTX 12%, MGM 12%, LRN 12%, MSM 12%, RAPP 12%, SRRK 12%, PLBY 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-03)

**Correction** since 2026-10-16 · level correction · 8 distribution days in 25 sessions · timing exposure 0% · VXN 30.53 · VIX 20.83 · last follow-through day 2026-08-04

Best bullish scores: SQQQ 7.7, TSLA 6.7, LABU 3.7, IWM 3.7, MSTR 2.1, BITX 2.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 5505 decisions in 1101 calls, $0.0770 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-04T07:55 | 0 / 1 / 4 | cash |  |
| Breezy | 2026-11-04T07:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-11-04T07:55 | 1 / 4 / 0 | ETH-USD 65% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | BITX | 2.15 | +6.47% | 6 |
| MACD zero-line | MSFT | 2.05 | +0.72% | 5 |
| Connors RSI(2) | SOXL | 1.98 | +4.10% | 13 |
| Supertrend | AMD | 1.96 | +2.83% | 3 |
| Bollinger reversion · 1h | MSFT | 1.91 | +3.39% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 108.66 | 8.66 | 0 | — | 10.13 | 4.43 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.61 | 6.61 | 17 | 70.6 | 7.32 | 2.29 | -4.91 | 24 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 102.45 | 2.45 | 26 | 46.2 | 0.94 | 0.42 | -5.37 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.11 | 0.11 | 27 | 25.9 | 7.75 | 1.99 | -6.74 | 43 |
| 5 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 6 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 7 | VWAP reversion · 1h | reversion | 99.92 | -0.08 | 104 | 46.2 | -11.33 | -3.00 | -13.06 | 141 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -2.68 | -1.87 | -5.83 | 1 |
| 9 | Hold SPY | benchmark | 96.50 | -3.50 | 0 | — | -1.84 | -0.96 | -3.94 | 1 |
| 10 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 96.26 | -3.74 | 18 | 22.2 | -4.89 | -4.79 | -6.25 | 21 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 96.24 | -3.76 | 108 | 35.2 | 4.78 | 2.31 | -3.26 | 94 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 95.57 | -4.43 | 0 | — | -0.79 | -0.22 | -6.60 | 1 |
| 13 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.54 | -4.46 | 5 | 40.0 | 0.63 | 0.28 | -7.93 | 8 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 94.95 | -5.05 | 0 | — | -4.35 | -1.63 | -6.35 | 1 |
| 15 | Three white soldiers · 1h | momentum | 94.51 | -5.49 | 18 | 11.1 | -3.13 | -2.92 | -5.33 | 26 |
| 16 | Agent (rotation) | meta | 94.18 | -5.82 | 157 | 28.7 | -7.85 | -5.79 | -8.69 | 171 |
| 17 | Copy: Congress Democrats (NANC) | copy | 93.92 | -6.08 | 0 | — | -3.46 | -1.33 | -7.64 | 1 |
| 18 | Gap and go | momentum | 92.58 | -7.42 | 149 | 26.8 | -2.18 | -0.68 | -9.18 | 213 |
| 19 | Hold BTC | benchmark | 91.61 | -8.39 | 0 | — | -0.15 | 0.15 | -13.22 | 1 |
| 20 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -8.84 | -2.03 | -16.91 | 1 |
| 21 | Trend pullback · 1h | trend | 90.54 | -9.46 | 102 | 21.6 | -16.58 | -6.15 | -17.53 | 79 |
| 22 | Agent | meta | 90.19 | -9.81 | 143 | 38.5 | -10.72 | -6.49 | -12.22 | 205 |
| 23 | Opening range 30m | breakout | 89.82 | -10.18 | 350 | 33.4 | -14.22 | -4.61 | -17.21 | 584 |
| 24 | Squeeze breakout · 1h | breakout | 88.72 | -11.28 | 64 | 21.9 | -9.62 | -3.35 | -14.15 | 89 |
| 25 | Daily: Bullish score | daily | 88.33 | -11.67 | 14 | 21.4 | -7.60 | -1.05 | -14.82 | 15 |
| 26 | Donchian 55/20 · 1h | breakout | 88.02 | -11.98 | 61 | 13.1 | -14.86 | -3.36 | -18.06 | 100 |
| 27 | Copy: Insider buying | copy | 87.99 | -12.01 | 37 | 37.8 | -22.47 | -4.59 | -23.13 | 61 |
| 28 | Parabolic SAR · 1h | trend | 87.64 | -12.36 | 153 | 26.8 | -15.48 | -3.60 | -18.16 | 239 |
| 29 | Copy: Cathie Wood (ARKK) | copy | 86.09 | -13.90 | 1 | 0.0 | -6.46 | -0.92 | -16.59 | 1 |
| 30 | Agent (aggressive) | meta | 85.82 | -14.18 | 69 | 31.9 | -12.53 | -4.16 | -14.77 | 94 |
| 31 | Max aggression: 5-day momentum | meta | 85.19 | -14.81 | 15 | 40.0 | -29.00 | -1.90 | -36.71 | 25 |
| 32 | Volume breakout · 1h | breakout | 84.56 | -15.44 | 130 | 28.5 | -15.32 | -3.50 | -18.37 | 92 |
| 33 | Stochastic reversion · 1h | reversion | 84.45 | -15.55 | 242 | 47.1 | -23.25 | -4.67 | -25.31 | 387 |
| 34 | Keltner breakout · 1h | breakout | 83.96 | -16.04 | 90 | 23.3 | -21.37 | -4.48 | -22.20 | 164 |
| 35 | Connors RSI(2) · 1h | reversion | 83.83 | -16.17 | 191 | 40.8 | -19.70 | -6.55 | -20.18 | 131 |
| 36 | MFI reversion · 1h | reversion | 83.52 | -16.48 | 312 | 33.7 | -15.96 | -2.53 | -17.89 | 153 |
| 37 | ADX DI cross · 1h | trend | 82.55 | -17.45 | 153 | 17.6 | -20.19 | -3.93 | -22.30 | 261 |
| 38 | Opening range 15m | breakout | 82.51 | -17.49 | 426 | 30.8 | -19.09 | -5.72 | -20.73 | 716 |
| 39 | Ichimoku · 1h | trend | 81.24 | -18.76 | 84 | 13.1 | -17.75 | -3.59 | -25.58 | 119 |
| 40 | Bollinger breakout · 1h | breakout | 80.65 | -19.35 | 145 | 24.1 | -18.45 | -3.76 | -23.80 | 231 |
| 41 | EMA 20/50 cross · 1h | trend | 78.99 | -21.01 | 92 | 10.9 | -18.52 | -3.31 | -27.05 | 130 |
| 42 | CCI reversion · 1h | reversion | 78.67 | -21.33 | 268 | 44.8 | -24.85 | -3.83 | -27.71 | 455 |
| 43 | Bollinger reversion · 1h | reversion | 78.01 | -21.99 | 227 | 39.2 | -26.89 | -5.24 | -29.70 | 379 |
| 44 | Z-score reversion · 1h | reversion | 77.19 | -22.82 | 144 | 34.7 | -14.42 | -2.10 | -23.02 | 221 |
| 45 | Daily: Momentum burst | daily | 77.04 | -22.96 | 23 | 13.0 | -30.80 | -4.36 | -33.56 | 33 |
| 46 | Supertrend · 1h | trend | 76.77 | -23.23 | 145 | 12.4 | -30.47 | -5.57 | -31.84 | 220 |
| 47 | MACD zero-line · 1h | trend | 76.61 | -23.39 | 141 | 15.6 | -26.44 | -5.92 | -28.29 | 214 |
| 48 | Williams %R · 1h | reversion | 76.50 | -23.50 | 280 | 46.8 | -36.07 | -6.47 | -37.32 | 530 |
| 49 | MACD cross · 1h | trend | 76.36 | -23.64 | 306 | 23.2 | -32.36 | -6.31 | -34.56 | 486 |
| 50 | RSI momentum · 1h | momentum | 75.40 | -24.60 | 141 | 12.1 | -29.28 | -5.69 | -30.97 | 215 |
| 51 | Triple EMA stack · 1h | trend | 75.33 | -24.67 | 130 | 13.8 | -28.84 | -5.65 | -32.26 | 205 |
| 52 | Heikin-Ashi · 1h | trend | 75.28 | -24.72 | 370 | 22.7 | -42.67 | -9.65 | -43.69 | 666 |
| 53 | OBV trend · 1h | momentum | 74.62 | -25.38 | 245 | 17.1 | -30.40 | -6.53 | -32.27 | 295 |
| 54 | Donchian 20/10 · 1h | breakout | 74.43 | -25.57 | 123 | 19.5 | -27.58 | -5.02 | -30.98 | 203 |
| 55 | ROC + volume · 1h | momentum | 72.85 | -27.15 | 313 | 25.2 | -35.54 | -6.99 | -36.42 | 372 |
| 56 | RSI(14) reversion · 1h | reversion | 72.65 | -27.35 | 130 | 26.2 | -20.78 | -3.91 | -26.28 | 198 |
| 57 | Candlestick reversal · 1h | reversion | 70.53 | -29.47 | 361 | 28.5 | -33.64 | -6.38 | -37.01 | 544 |
| 58 | Agent (ML meta-label) | meta | 69.59 | -30.41 | 1372 | 21.8 | -16.90 | -2.87 | -20.07 | 270 |
| 59 | Max aggression: 1-day momentum | meta | 68.64 | -31.36 | 23 | 30.4 | -32.21 | -1.80 | -50.32 | 42 |
| 60 | Three white soldiers | momentum | 68.24 | -31.76 | 425 | 15.8 | -46.84 | -21.56 | -46.95 | 624 |
| 61 | VWAP momentum · 1h | momentum | 68.07 | -31.93 | 717 | 21.9 | -56.43 | -12.12 | -56.51 | 1230 |
| 62 | EMA 9/21 cross · 1h | trend | 67.70 | -32.30 | 224 | 9.4 | -38.79 | -7.93 | -40.34 | 332 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.92 | -42.16 | -98.97 | 5144 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -80.16 | -24.48 | -80.33 | 1413 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.16 | -39.61 | -93.54 | 2510 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -88.46 | -27.85 | -89.23 | 1899 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -90.77 | -33.32 | -91.29 | 2314 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.79 | -31.30 | -90.79 | 2213 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.64 | -46.77 | -97.77 | 3455 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.09 | -49.56 | -96.30 | 3374 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.69 | -33.00 | -93.76 | 2430 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.13 | -35.38 | -82.13 | 1650 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.49 | -54.21 | -99.49 | 5882 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.77 | -39.30 | -93.14 | 2614 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.36 | -36.53 | -95.36 | 3367 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.79 | -67.58 | -99.80 | 6176 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.65 | -40.99 | -91.88 | 2258 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -74.40 | -25.72 | -75.21 | 1547 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -55.49 | -97.80 | 3514 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.70 | -61.27 | -98.71 | 4821 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -69.61 | -28.51 | -70.54 | 1207 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.62 | -48.11 | -94.85 | 2775 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.38 | -34.34 | -85.11 | 1788 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.63 | -72.17 | -99.63 | 6319 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.34 | -30.55 | -88.43 | 2246 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.91 | -19.29 | -77.06 | 1705 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.34 | -36.46 | -90.45 | 2235 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.56 | -52.20 | -96.57 | 3830 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.25 | -51.56 | -89.41 | 2129 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -65.16 | -26.92 | -65.75 | 806 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -73.09 | -23.26 | -74.37 | 1263 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -77.07 | -18.96 | -77.34 | 1613 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.00 | -53.19 | -97.01 | 4248 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.53 | -99.92 | 8194 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-04T07:00 | Z-score reversion · 1h | sell | SOL-USD | 3.96 | -0.01 | exit signal |
| 2026-11-04T07:00 | Heikin-Ashi · 1h | buy | BTC-USD | 9.40 | — | entry signal |
| 2026-11-04T07:00 | Heikin-Ashi · 1h | sell | XRP-USD | 9.33 | -0.07 | rebalance down |
| 2026-11-04T07:00 | MACD zero-line · 1h | buy | BTC-USD | 19.16 | — | entry signal |
| 2026-11-04T07:00 | MACD cross · 1h | buy | ETH-USD | 4.24 | — | entry signal |
| 2026-11-04T07:00 | MACD cross · 1h | buy | BTC-USD | 4.24 | — | entry signal |
| 2026-11-04T07:00 | Triple EMA stack · 1h | buy | ETH-USD | 18.84 | — | entry signal |
| 2026-11-04T07:00 | EMA 9/21 cross · 1h | buy | ETH-USD | 11.30 | — | entry signal |
| 2026-11-04T07:00 | EMA 9/21 cross · 1h | buy | BTC-USD | 11.30 | — | entry signal |
| 2026-11-04T07:00 | EMA 9/21 cross · 1h | sell | XRP-USD | 5.58 | -0.04 | rebalance down |
| 2026-11-04T06:00 | Williams %R · 1h | buy | SOL-USD | 4.54 | — | entry |
| 2026-11-04T06:00 | Williams %R · 1h | sell | BTC-USD | 4.54 | 0.05 | exit signal |
| 2026-11-04T06:00 | Z-score reversion · 1h | buy | SOL-USD | 3.97 | — | entry |
| 2026-11-04T06:00 | Z-score reversion · 1h | sell | BTC-USD | 3.97 | 0.04 | exit signal |
| 2026-11-04T06:00 | OBV trend · 1h | buy | XRP-USD | 14.79 | — | entry signal |
| 2026-11-04T06:00 | OBV trend · 1h | buy | ETH-USD | 14.93 | — | entry signal |
| 2026-11-04T06:00 | VWAP momentum · 1h | buy | SOL-USD | 5.67 | — | entry signal |
| 2026-11-04T06:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.67 | — | entry signal |
| 2026-11-04T06:00 | Heikin-Ashi · 1h | buy | XRP-USD | 18.85 | — | entry signal |
| 2026-11-04T06:00 | ADX DI cross · 1h | buy | XRP-USD | 10.32 | — | entry signal |
| 2026-11-04T06:00 | ADX DI cross · 1h | buy | ETH-USD | 10.32 | — | entry signal |
| 2026-11-04T06:00 | ADX DI cross · 1h | buy | BTC-USD | 10.32 | — | entry signal |
| 2026-11-04T06:00 | Parabolic SAR · 1h | buy | XRP-USD | 8.66 | — | entry signal |
| 2026-11-04T06:00 | Parabolic SAR · 1h | buy | ETH-USD | 17.53 | — | entry signal |
| 2026-11-04T06:00 | Parabolic SAR · 1h | buy | BTC-USD | 17.53 | — | entry signal |
| 2026-11-04T06:00 | Supertrend · 1h | buy | ETH-USD | 6.98 | — | entry signal |
| 2026-11-04T06:00 | Supertrend · 1h | buy | BTC-USD | 6.98 | — | entry signal |
| 2026-11-04T06:00 | Triple EMA stack · 1h | buy | XRP-USD | 18.86 | — | entry signal |
| 2026-11-04T06:00 | EMA 9/21 cross · 1h | buy | XRP-USD | 16.96 | — | entry signal |
| 2026-11-04T05:30 | Three white soldiers | sell | XRP-USD | 16.99 | -0.10 | exit signal |
| 2026-11-04T05:00 | MFI reversion · 1h | buy | ETH-USD | 13.89 | — | entry signal |
| 2026-11-04T05:00 | MFI reversion · 1h | buy | DOGE-USD | 13.89 | — | entry signal |
| 2026-11-04T05:00 | Bollinger reversion · 1h | buy | DOGE-USD | 2.11 | — | entry |
| 2026-11-04T05:00 | Bollinger reversion · 1h | sell | BTC-USD | 2.11 | 0.01 | exit signal |
| 2026-11-04T05:00 | VWAP momentum · 1h | buy | XRP-USD | 6.80 | — | entry signal |
| 2026-11-04T05:00 | VWAP momentum · 1h | buy | ETH-USD | 6.80 | — | entry signal |
| 2026-11-04T05:00 | VWAP momentum · 1h | buy | BTC-USD | 6.80 | — | entry signal |
| 2026-11-04T04:50 | Three white soldiers | buy | XRP-USD | 17.09 | — | entry signal |
| 2026-11-04T04:35 | Three white soldiers | sell | XRP-USD | 17.03 | -0.07 | exit signal |
| 2026-11-04T04:00 | Williams %R · 1h | buy | DOGE-USD | 1.92 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-06 07:55:05.000166+00:00 -> 2026-11-04 08:05:05.000166+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-06 07:55:05.000166+00:00 -> 2026-11-04 08:05:05.000166+00:00); yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no price data found  (5m 2026-09-06 07:55:05.000166+00:00 -> 2026-11-04 08:05:05.000166+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
