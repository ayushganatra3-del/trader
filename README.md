# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T16:05:05.000116+00:00 · 38026 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.19 (-9.81%)

Closed trades 112, win rate 38.4%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 18.03 | +0.04 |
| PLTR | 18.20 | +0.22 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-27 | IAM 12%, BPRE 12%, APLD 12%, RENT 12%, CTY 12%, FBK 12%, PLUR 12%, RAPP 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-26)

**Correction** since 2026-10-16 · level correction · 7 distribution days in 25 sessions · timing exposure 0% · VXN 26.40 · VIX 18.39 · last follow-through day 2026-08-04

Best bullish scores: TSLA 7.4, MSFT 7.3, PLTR 6.5, AAPL 5.6, SQQQ 4.7, MSTR 2.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 20269 decisions in 2351 calls, $0.2596 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T16:05 | 10 / 13 / 7 | cash |  |
| Breezy | 2026-10-27T16:05 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-27T16:05 | 8 / 21 / 1 | TQQQ 53% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP momentum | PLTR | 2.30 | +6.55% | 6 |
| RSI(14) reversion | SPY | 1.92 | +0.47% | 3 |
| VWAP reversion | META | 1.90 | +1.93% | 3 |
| MACD zero-line | MSFT | 1.88 | +0.58% | 4 |
| Z-score reversion | TSLA | 1.87 | +2.31% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.41 | 7.41 | 0 | — | 7.87 | 3.90 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.95 | 6.95 | 14 | 71.4 | 4.13 | 1.34 | -6.62 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.70 | 5.70 | 19 | 47.4 | 8.19 | 2.60 | -4.92 | 26 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.87 | 0.87 | 0 | — | 2.64 | 1.24 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.15 | -3.64 | -14.07 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.61 | -0.39 | 0 | — | 0.68 | 0.44 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.05 | -0.94 | 81 | 34.6 | 8.11 | 3.75 | -2.29 | 98 |
| 11 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 12 | Copy: Congress Democrats (NANC) | copy | 97.59 | -2.41 | 0 | — | 0.30 | 0.19 | -5.99 | 1 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.02 | -1.91 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.44 | -3.56 | 122 | 31.1 | -3.07 | -1.62 | -6.39 | 192 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 95.74 | -4.26 | 0 | — | -6.01 | -2.47 | -7.83 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 5.06 | 1.18 | -7.93 | 8 |
| 17 | Gap and go | momentum | 95.58 | -4.42 | 112 | 25.9 | 5.56 | 1.80 | -8.76 | 210 |
| 18 | Hold BTC | benchmark | 95.49 | -4.51 | 0 | — | 2.63 | 0.60 | -9.28 | 1 |
| 19 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 20 | Opening range 30m | breakout | 93.70 | -6.30 | 272 | 34.2 | -9.55 | -2.82 | -17.21 | 593 |
| 21 | Trend pullback · 1h | trend | 93.65 | -6.35 | 96 | 22.9 | -21.79 | -6.94 | -22.19 | 116 |
| 22 | Donchian 55/20 · 1h | breakout | 93.54 | -6.46 | 49 | 16.3 | -14.95 | -3.26 | -17.32 | 98 |
| 23 | Copy: Insider buying | copy | 93.29 | -6.71 | 27 | 37.0 | -18.68 | -3.57 | -22.94 | 63 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.09 | -7.91 | 0 | — | -1.15 | -0.02 | -14.57 | 1 |
| 25 | Parabolic SAR · 1h | trend | 91.99 | -8.01 | 121 | 25.6 | -20.46 | -5.06 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.86 | -8.14 | 13 | 15.4 | -17.68 | -3.40 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.78 | -8.22 | 119 | 18.5 | -11.46 | -2.45 | -14.45 | 276 |
| 28 | Daily: Bullish score | daily | 91.59 | -8.41 | 11 | 18.2 | -5.41 | -0.60 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.86 | -2.07 | -16.91 | 1 |
| 30 | Squeeze breakout · 1h | breakout | 91.15 | -8.85 | 52 | 23.1 | -4.30 | -1.11 | -12.00 | 92 |
| 31 | Max aggression: 5-day momentum | meta | 91.00 | -9.00 | 12 | 41.7 | -14.46 | -1.30 | -27.23 | 25 |
| 32 | Volume breakout · 1h | breakout | 90.41 | -9.59 | 105 | 23.8 | -11.67 | -2.38 | -16.00 | 113 |
| 33 | Agent | meta | 90.19 | -9.81 | 112 | 38.4 | -11.09 | -6.95 | -12.47 | 223 |
| 34 | Bollinger breakout · 1h | breakout | 88.83 | -11.18 | 109 | 26.6 | -12.75 | -2.50 | -18.15 | 248 |
| 35 | Agent (aggressive) | meta | 88.50 | -11.50 | 56 | 35.7 | -10.80 | -3.55 | -14.77 | 99 |
| 36 | Stochastic reversion · 1h | reversion | 87.88 | -12.12 | 204 | 47.1 | -21.48 | -3.95 | -22.81 | 394 |
| 37 | Keltner breakout · 1h | breakout | 87.29 | -12.71 | 74 | 23.0 | -19.77 | -3.80 | -23.13 | 184 |
| 38 | Opening range 15m | breakout | 87.17 | -12.83 | 338 | 30.8 | -13.33 | -3.68 | -17.87 | 719 |
| 39 | Z-score reversion · 1h | reversion | 86.56 | -13.45 | 125 | 36.0 | -12.85 | -2.04 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.85 | -14.15 | 114 | 14.0 | -25.36 | -5.11 | -28.20 | 230 |
| 41 | RSI momentum · 1h | momentum | 85.16 | -14.84 | 104 | 15.4 | -20.97 | -4.24 | -24.07 | 210 |
| 42 | Connors RSI(2) · 1h | reversion | 85.03 | -14.96 | 176 | 40.9 | -26.40 | -7.94 | -26.79 | 198 |
| 43 | MACD cross · 1h | trend | 84.38 | -15.62 | 244 | 22.1 | -28.32 | -5.68 | -30.37 | 480 |
| 44 | EMA 20/50 cross · 1h | trend | 84.14 | -15.86 | 73 | 11.0 | -22.39 | -4.44 | -24.31 | 130 |
| 45 | Ichimoku · 1h | trend | 83.94 | -16.06 | 68 | 11.8 | -20.03 | -4.08 | -24.73 | 109 |
| 46 | MFI reversion · 1h | reversion | 83.45 | -16.55 | 270 | 32.2 | -16.10 | -2.48 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.45 | -16.55 | 101 | 14.9 | -27.86 | -5.32 | -30.72 | 206 |
| 48 | CCI reversion · 1h | reversion | 82.25 | -17.75 | 230 | 45.2 | -23.57 | -3.35 | -28.06 | 465 |
| 49 | Donchian 20/10 · 1h | breakout | 81.92 | -18.08 | 99 | 20.2 | -24.15 | -4.60 | -26.89 | 220 |
| 50 | Williams %R · 1h | reversion | 81.87 | -18.13 | 231 | 46.8 | -35.11 | -5.91 | -35.98 | 538 |
| 51 | MACD zero-line · 1h | trend | 81.39 | -18.61 | 111 | 15.3 | -23.26 | -4.90 | -25.41 | 227 |
| 52 | Agent (ML meta-label) | meta | 80.99 | -19.01 | 957 | 20.8 | -8.57 | -1.54 | -16.43 | 333 |
| 53 | Bollinger reversion · 1h | reversion | 80.93 | -19.07 | 182 | 37.4 | -28.38 | -5.69 | -30.39 | 365 |
| 54 | OBV trend · 1h | momentum | 80.24 | -19.76 | 209 | 17.7 | -30.91 | -6.55 | -32.80 | 296 |
| 55 | RSI(14) reversion · 1h | reversion | 80.01 | -19.99 | 106 | 26.4 | -16.15 | -2.99 | -24.48 | 184 |
| 56 | ROC + volume · 1h | momentum | 79.25 | -20.75 | 259 | 25.9 | -31.48 | -6.12 | -33.75 | 386 |
| 57 | Heikin-Ashi · 1h | trend | 78.45 | -21.55 | 295 | 22.7 | -43.62 | -9.62 | -45.12 | 660 |
| 58 | Three white soldiers | momentum | 77.56 | -22.44 | 317 | 18.9 | -44.47 | -20.26 | -44.95 | 608 |
| 59 | Candlestick reversal · 1h | reversion | 77.25 | -22.75 | 282 | 29.4 | -34.12 | -6.70 | -34.94 | 550 |
| 60 | VWAP momentum · 1h | momentum | 76.90 | -23.10 | 567 | 21.9 | -48.85 | -10.39 | -51.09 | 1247 |
| 61 | EMA 9/21 cross · 1h | trend | 76.67 | -23.33 | 176 | 10.8 | -30.49 | -6.54 | -32.50 | 337 |
| 62 | Max aggression: 1-day momentum | meta | 71.92 | -28.08 | 20 | 30.0 | -38.11 | -2.48 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.41 | -45.59 | 785 | 22.4 | -74.27 | -26.09 | -75.04 | 1593 |
| 64 | Volume breakout | breakout | 52.94 | -47.06 | 474 | 12.4 | -62.97 | -26.02 | -63.52 | 812 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.84 | -41.97 | -98.87 | 5157 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.27 | -23.16 | -80.06 | 1419 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.53 | -41.43 | -93.77 | 2531 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.20 | -30.20 | -89.36 | 1924 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.22 | -35.49 | -91.53 | 2345 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.39 | -31.73 | -90.49 | 2167 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.82 | -48.41 | -97.89 | 3507 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.03 | -51.09 | -96.17 | 3388 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.04 | -35.55 | -94.06 | 2456 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -81.99 | -30.94 | -82.69 | 1700 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.42 | -51.51 | -99.42 | 5760 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.68 | -40.90 | -92.92 | 2646 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.40 | -38.18 | -95.41 | 3362 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -71.27 | -99.78 | 6167 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.25 | -44.03 | -92.35 | 2323 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.72 | -58.77 | -97.77 | 3582 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -58.00 | -98.67 | 4791 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.74 | -28.29 | -68.59 | 1181 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.55 | -53.71 | -94.65 | 2781 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.27 | -38.00 | -84.57 | 1835 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.09 | -99.61 | 6280 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.31 | -28.85 | -88.31 | 2233 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.67 | -18.94 | -76.94 | 1684 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.52 | -36.38 | -90.62 | 2278 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.91 | -96.28 | 3820 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.04 | -49.34 | -90.07 | 2125 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.52 | -23.53 | -73.47 | 1293 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.24 | -17.96 | -76.40 | 1581 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.36 | -96.55 | 4188 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.59 | -99.92 | 8322 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T16:05 | Agent (ML meta-label) | buy | AMD | 20.25 | — | entry |
| 2026-10-27T16:05 | RSI momentum · 1h | buy | ETH-USD | 4.27 | — | entry |
| 2026-10-27T16:05 | RSI momentum · 1h | sell | TECL | 4.27 | 0.12 | rebalance down |
| 2026-10-27T16:05 | Three white soldiers | buy | LABU | 6.36 | — | rebalance up |
| 2026-10-27T16:05 | Three white soldiers | buy | ETHU | 6.51 | — | rebalance up |
| 2026-10-27T16:05 | Three white soldiers | buy | ETH-USD | 6.50 | — | rebalance up |
| 2026-10-27T16:05 | Three white soldiers | buy | COIN | 6.43 | — | rebalance up |
| 2026-10-27T16:05 | Three white soldiers | sell | BTC-USD | 12.88 | -0.10 | exit signal |
| 2026-10-27T16:05 | Three white soldiers | sell | BITX | 12.92 | -0.06 | exit signal |
| 2026-10-27T16:05 | Volume breakout | buy | GOOGL | 8.83 | — | entry signal |
| 2026-10-27T16:05 | Volume breakout | sell | XRP-USD | 7.55 | -0.07 | exit signal |
| 2026-10-27T16:05 | Volume breakout | sell | DOGE-USD | 7.55 | -0.05 | exit signal |
| 2026-10-27T16:05 | ROC + volume | buy | PLTR | 3.20 | — | entry |
| 2026-10-27T16:05 | ROC + volume | sell | AAPL | 4.17 | -0.01 | exit signal |
| 2026-10-27T16:00 | Agent (ML meta-label) | sell | AMD | 20.21 | 0.01 | selected signal exited |
| 2026-10-27T16:00 | CCI reversion · 1h | buy | MSTR | 6.85 | — | rebalance up |
| 2026-10-27T16:00 | CCI reversion · 1h | buy | GOOGL | 4.15 | — | rebalance up |
| 2026-10-27T16:00 | CCI reversion · 1h | sell | SOL-USD | 13.67 | -0.02 | exit signal |
| 2026-10-27T16:00 | Z-score reversion · 1h | sell | SOL-USD | 21.56 | -0.08 | exit signal |
| 2026-10-27T16:00 | Candlestick reversal · 1h | buy | SOL-USD | 5.16 | — | rebalance up |
| 2026-10-27T16:00 | Candlestick reversal · 1h | buy | MSTR | 5.17 | — | rebalance up |
| 2026-10-27T16:00 | Candlestick reversal · 1h | buy | ETHU | 5.05 | — | rebalance up |
| 2026-10-27T16:00 | Candlestick reversal · 1h | sell | DOGE-USD | 7.73 | 0.03 | exit signal |
| 2026-10-27T16:00 | ADX DI cross · 1h | buy | SOL-USD | 4.62 | — | entry signal |
| 2026-10-27T16:00 | ADX DI cross · 1h | buy | ETH-USD | 6.56 | — | entry signal |
| 2026-10-27T16:00 | ADX DI cross · 1h | buy | BTC-USD | 6.56 | — | entry signal |
| 2026-10-27T16:00 | ADX DI cross · 1h | buy | AAPL | 6.56 | — | entry |
| 2026-10-27T16:00 | ADX DI cross · 1h | sell | UPRO | 4.76 | 0.07 | rebalance down |
| 2026-10-27T16:00 | ADX DI cross · 1h | sell | TSLA | 4.97 | 0.14 | rebalance down |
| 2026-10-27T16:00 | ADX DI cross · 1h | sell | TECL | 5.17 | 0.25 | rebalance down |
| 2026-10-27T16:00 | ADX DI cross · 1h | sell | SPY | 4.68 | 0.03 | rebalance down |
| 2026-10-27T16:00 | ADX DI cross · 1h | sell | NVDA | 4.73 | 0.05 | rebalance down |
| 2026-10-27T16:00 | Triple EMA stack · 1h | buy | DOGE-USD | 4.80 | — | entry signal |
| 2026-10-27T16:00 | Triple EMA stack · 1h | sell | TNA | 4.80 | 0.23 | rebalance down |
| 2026-10-27T16:00 | Volume breakout | buy | SPY | 7.55 | — | entry |
| 2026-10-27T16:00 | Volume breakout | buy | PLTR | 7.58 | — | entry |
| 2026-10-27T16:00 | Volume breakout | sell | XRP-USD | 2.98 | -0.02 | rebalance down |
| 2026-10-27T16:00 | Volume breakout | sell | TSLA | 3.08 | 0.02 | rebalance down |
| 2026-10-27T16:00 | Volume breakout | sell | QQQ | 3.03 | 0.00 | rebalance down |
| 2026-10-27T16:00 | Volume breakout | sell | ETH-USD | 3.02 | -0.02 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 16:05:05.000116+00:00 -> 2026-10-27 16:15:05.000116+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
