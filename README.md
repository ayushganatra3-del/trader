# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-22T08:49:05.000152+00:00 · 31681 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.67 (-9.33%)

Closed trades 93, win rate 40.9%, fees £3.03, max drawdown -9.99%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-21 | PAM 12%, BORR 12%, PEP 12%, GME 12%, IAM 12%, BPRE 12%, APLD 12%, CTY 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-21)

**Correction** since 2026-10-16 · level correction · 6 distribution days in 25 sessions · timing exposure 0% · VXN 24.42 · VIX 16.68 · last follow-through day 2026-08-04

Best bullish scores: PLTR 7.5, TSLA 7.0, MSFT 7.0, AMZN 6.6, BITX 6.5, MSTR 5.2

### AI bees (Jev: typesafe/jev-1.13)

Today: 6735 decisions in 1347 calls, $0.0944 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-22T08:49 | 0 / 2 / 3 | cash |  |
| Breezy | 2026-10-22T08:49 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-22T08:49 | 2 / 3 / 0 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Opening range 30m | TSLA | 2.26 | +2.38% | 4 |
| VWAP reversion | ETHU | 1.91 | +4.36% | 4 |
| Bollinger reversion | ETHU | 1.90 | +6.78% | 15 |
| VWAP reversion | BITX | 1.81 | +2.89% | 6 |
| Connors RSI(2) | LABU | 1.75 | +3.42% | 18 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 105.92 | 5.92 | 0 | — | 8.54 | 3.99 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 104.64 | 4.64 | 12 | 66.7 | 0.18 | 0.14 | -8.92 | 26 |
| 3 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.25 | 4.25 | 18 | 33.3 | 6.36 | 1.61 | -7.11 | 43 |
| 4 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 103.17 | 3.17 | 15 | 46.7 | 5.58 | 1.80 | -4.86 | 23 |
| 5 | VWAP reversion · 1h | reversion | 102.50 | 2.50 | 75 | 48.0 | -8.12 | -2.20 | -13.79 | 130 |
| 6 | Max aggression: 5-day momentum | meta | 101.39 | 1.40 | 10 | 50.0 | -7.32 | -0.34 | -34.64 | 26 |
| 7 | Daily: Connors RSI(2) · 3x ETFs | daily | 100.12 | 0.12 | 4 | 50.0 | 9.05 | 1.91 | -7.93 | 8 |
| 8 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 9 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 10 | Daily: SMA 20/50 cross · AAPL | daily | 99.52 | -0.48 | 0 | — | 2.33 | 1.06 | -5.02 | 1 |
| 11 | Hold SPY | benchmark | 99.30 | -0.70 | 0 | — | 1.08 | 0.67 | -3.13 | 1 |
| 12 | Day trade: Stocks in Play ORB | daytrade | 99.26 | -0.74 | 65 | 35.4 | 2.65 | 1.54 | -2.29 | 65 |
| 13 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 98.30 | -1.70 | 12 | 25.0 | -3.61 | -3.94 | -4.04 | 21 |
| 14 | Copy: Congress Democrats (NANC) | copy | 97.39 | -2.61 | 0 | — | 0.79 | 0.39 | -5.31 | 1 |
| 15 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.13 | -1.78 | -5.83 | 1 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 96.95 | -3.04 | 0 | — | -4.00 | -1.52 | -7.04 | 1 |
| 17 | Hold BTC | benchmark | 96.69 | -3.31 | 0 | — | 4.40 | 0.83 | -8.68 | 1 |
| 18 | Copy: Insider buying | copy | 96.58 | -3.42 | 25 | 40.0 | -11.33 | -1.93 | -20.62 | 72 |
| 19 | Agent (rotation) | meta | 95.74 | -4.26 | 117 | 30.8 | -8.74 | -5.13 | -8.79 | 235 |
| 20 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -3.98 | -3.06 | -5.48 | 30 |
| 21 | ADX DI cross · 1h | trend | 95.37 | -4.63 | 92 | 19.6 | -10.20 | -1.85 | -16.14 | 259 |
| 22 | Daily: Momentum burst | daily | 94.83 | -5.17 | 6 | 16.7 | -9.31 | -1.37 | -20.58 | 38 |
| 23 | Trend pullback · 1h | trend | 94.80 | -5.20 | 92 | 23.9 | -19.74 | -6.15 | -19.97 | 126 |
| 24 | Gap and go | momentum | 94.30 | -5.70 | 89 | 21.3 | 6.57 | 2.04 | -7.13 | 200 |
| 25 | Donchian 55/20 · 1h | breakout | 93.99 | -6.01 | 45 | 17.8 | -16.23 | -3.32 | -17.32 | 103 |
| 26 | Opening range 30m | breakout | 93.69 | -6.31 | 236 | 35.2 | -10.91 | -3.09 | -17.26 | 568 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 92.82 | -7.18 | 0 | — | 0.08 | 0.17 | -14.37 | 1 |
| 28 | Parabolic SAR · 1h | trend | 92.77 | -7.23 | 113 | 25.7 | -16.71 | -3.69 | -19.79 | 270 |
| 29 | Squeeze breakout · 1h | breakout | 92.47 | -7.53 | 50 | 24.0 | -3.00 | -0.66 | -11.48 | 101 |
| 30 | Daily: Bullish score | daily | 92.11 | -7.89 | 8 | 0.0 | -2.45 | -0.15 | -13.10 | 13 |
| 31 | Bollinger breakout · 1h | breakout | 91.94 | -8.05 | 93 | 30.1 | -10.27 | -1.86 | -14.43 | 259 |
| 32 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -10.31 | -1.94 | -16.91 | 1 |
| 33 | Agent | meta | 90.67 | -9.33 | 93 | 40.9 | -17.66 | -6.40 | -19.13 | 258 |
| 34 | Volume breakout · 1h | breakout | 90.31 | -9.69 | 95 | 24.2 | -14.07 | -2.45 | -14.11 | 109 |
| 35 | Supertrend · 1h | trend | 89.57 | -10.43 | 93 | 15.1 | -21.15 | -4.23 | -26.66 | 218 |
| 36 | RSI momentum · 1h | momentum | 89.05 | -10.95 | 89 | 18.0 | -18.15 | -3.63 | -20.65 | 218 |
| 37 | Stochastic reversion · 1h | reversion | 88.42 | -11.58 | 172 | 46.5 | -14.88 | -2.45 | -22.24 | 368 |
| 38 | Opening range 15m | breakout | 88.29 | -11.71 | 291 | 31.3 | -15.49 | -4.19 | -19.07 | 704 |
| 39 | EMA 20/50 cross · 1h | trend | 88.24 | -11.76 | 63 | 12.7 | -21.58 | -3.69 | -24.24 | 143 |
| 40 | Keltner breakout · 1h | breakout | 87.62 | -12.38 | 67 | 23.9 | -20.71 | -4.02 | -22.53 | 199 |
| 41 | Agent (aggressive) | meta | 87.40 | -12.60 | 46 | 34.8 | -18.56 | -4.37 | -20.33 | 128 |
| 42 | MACD cross · 1h | trend | 87.36 | -12.64 | 202 | 22.3 | -25.38 | -4.85 | -27.85 | 470 |
| 43 | Z-score reversion · 1h | reversion | 86.74 | -13.26 | 102 | 34.3 | -11.48 | -1.77 | -21.32 | 196 |
| 44 | Ichimoku · 1h | trend | 86.44 | -13.56 | 61 | 13.1 | -18.20 | -3.42 | -20.25 | 118 |
| 45 | Connors RSI(2) · 1h | reversion | 86.07 | -13.93 | 165 | 40.6 | -25.27 | -7.17 | -25.37 | 203 |
| 46 | Donchian 20/10 · 1h | breakout | 85.35 | -14.65 | 87 | 20.7 | -25.34 | -4.52 | -27.58 | 229 |
| 47 | MFI reversion · 1h | reversion | 85.25 | -14.75 | 229 | 33.2 | -13.19 | -1.95 | -21.11 | 141 |
| 48 | Triple EMA stack · 1h | trend | 85.11 | -14.89 | 94 | 16.0 | -27.16 | -5.00 | -28.08 | 219 |
| 49 | MACD zero-line · 1h | trend | 84.43 | -15.57 | 92 | 15.2 | -23.97 | -4.61 | -26.48 | 229 |
| 50 | Agent (ML meta-label) | meta | 83.79 | -16.21 | 744 | 19.9 | -14.58 | -2.68 | -17.65 | 367 |
| 51 | OBV trend · 1h | momentum | 83.44 | -16.56 | 191 | 18.3 | -30.60 | -5.74 | -31.47 | 304 |
| 52 | ROC + volume · 1h | momentum | 82.70 | -17.30 | 218 | 23.9 | -31.06 | -5.05 | -33.00 | 387 |
| 53 | Williams %R · 1h | reversion | 82.55 | -17.45 | 199 | 44.7 | -31.50 | -4.88 | -36.62 | 517 |
| 54 | Three white soldiers | momentum | 82.43 | -17.57 | 259 | 20.5 | -44.91 | -17.97 | -45.55 | 600 |
| 55 | CCI reversion · 1h | reversion | 82.08 | -17.92 | 188 | 43.6 | -20.26 | -2.63 | -27.44 | 437 |
| 56 | Bollinger reversion · 1h | reversion | 81.96 | -18.04 | 163 | 36.2 | -29.61 | -5.74 | -32.84 | 350 |
| 57 | Heikin-Ashi · 1h | trend | 81.37 | -18.63 | 251 | 23.9 | -42.85 | -9.17 | -46.38 | 678 |
| 58 | RSI(14) reversion · 1h | reversion | 80.84 | -19.16 | 85 | 24.7 | -16.40 | -2.78 | -24.99 | 177 |
| 59 | EMA 9/21 cross · 1h | trend | 80.67 | -19.33 | 145 | 11.7 | -28.38 | -5.52 | -30.49 | 335 |
| 60 | Candlestick reversal · 1h | reversion | 78.93 | -21.07 | 231 | 30.3 | -39.08 | -7.21 | -41.79 | 547 |
| 61 | VWAP momentum · 1h | momentum | 78.92 | -21.08 | 483 | 22.2 | -48.74 | -9.87 | -52.95 | 1251 |
| 62 | Max aggression: 1-day momentum | meta | 77.06 | -22.94 | 17 | 29.4 | -34.21 | -2.14 | -41.57 | 42 |
| 63 | ROC + volume | momentum | 59.80 | -40.20 | 679 | 23.4 | -77.76 | -21.79 | -78.97 | 1701 |
| 64 | Volume breakout | breakout | 59.16 | -40.84 | 401 | 13.7 | -64.17 | -19.32 | -64.95 | 858 |
| 65 | Donchian 55/20 | breakout | 56.43 | -43.57 | 535 | 19.8 | -72.03 | -19.18 | -74.04 | 1276 |
| 66 | Squeeze breakout | breakout | 56.15 | -43.85 | 523 | 14.1 | -67.04 | -22.78 | -67.93 | 1201 |
| 67 | EMA 20/50 cross | trend | 55.24 | -44.76 | 575 | 20.5 | -78.95 | -19.41 | -80.87 | 1438 |
| 68 | RSI(14) reversion | reversion | 53.85 | -46.15 | 783 | 26.4 | -75.83 | -17.08 | -76.01 | 1634 |
| 69 | VWAP reversion | reversion | 51.69 | -48.30 | 783 | 25.4 | -72.22 | -14.47 | -72.68 | 1487 |
| 70 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.83 | -32.00 | -98.85 | 5295 |
| 71 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.94 | -33.05 | -94.26 | 2581 |
| 72 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -87.92 | -23.41 | -88.71 | 1893 |
| 73 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.28 | -28.18 | -91.74 | 2358 |
| 74 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -91.10 | -25.25 | -91.24 | 2254 |
| 75 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.77 | -35.58 | -97.83 | 3506 |
| 76 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.83 | -36.47 | -96.98 | 3584 |
| 77 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.50 | -28.33 | -94.50 | 2555 |
| 78 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -83.14 | -28.00 | -83.41 | 1730 |
| 79 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.46 | -37.97 | -99.46 | 5769 |
| 80 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.22 | -29.79 | -92.73 | 2618 |
| 81 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.84 | -30.76 | -95.84 | 3462 |
| 82 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.77 | -42.38 | -99.77 | 6153 |
| 83 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -91.79 | -30.21 | -91.92 | 2334 |
| 84 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.73 | -38.95 | -97.73 | 3615 |
| 85 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.60 | -38.37 | -98.60 | 4721 |
| 86 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 87 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.20 | -34.75 | -94.46 | 2789 |
| 88 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -83.31 | -27.53 | -84.44 | 1788 |
| 89 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.58 | -40.92 | -99.58 | 6212 |
| 90 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -87.66 | -23.46 | -87.71 | 2165 |
| 91 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -88.42 | -27.23 | -88.45 | 2152 |
| 92 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.17 | -34.14 | -96.17 | 3783 |
| 93 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.58 | -34.31 | -89.58 | 2098 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.14 | -34.96 | -96.16 | 4110 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.91 | -45.99 | -99.91 | 8277 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-22T08:45 | Agent (ML meta-label) | buy | SOL-USD | 9.31 | — | entry |
| 2026-10-22T08:45 | VWAP reversion | buy | XRP-USD | 10.31 | — | entry signal |
| 2026-10-22T08:45 | VWAP reversion | buy | ETH-USD | 10.36 | — | entry signal |
| 2026-10-22T08:45 | VWAP reversion | buy | DOGE-USD | 10.36 | — | entry signal |
| 2026-10-22T08:45 | VWAP reversion | sell | BTC-USD | 2.61 | -0.02 | rebalance down |
| 2026-10-22T08:45 | RSI(14) reversion | buy | XRP-USD | 10.79 | — | entry signal |
| 2026-10-22T08:45 | RSI(14) reversion | buy | ETH-USD | 10.80 | — | entry signal |
| 2026-10-22T08:45 | RSI(14) reversion | buy | DOGE-USD | 10.80 | — | entry signal |
| 2026-10-22T08:45 | RSI(14) reversion | buy | BTC-USD | 10.80 | — | entry signal |
| 2026-10-22T08:45 | RSI(14) reversion | sell | SOL-USD | 2.70 | -0.02 | rebalance down |
| 2026-10-22T08:40 | Agent (ML meta-label) | sell | SOL-USD | 7.57 | -0.06 | selected signal exited |
| 2026-10-22T08:40 | Connors RSI(2) · 1h | sell | ETH-USD | 21.46 | -0.49 | stop-loss |
| 2026-10-22T08:40 | VWAP reversion | sell | DOGE-USD | 10.34 | -0.11 | stop-loss |
| 2026-10-22T08:40 | RSI(14) reversion | sell | DOGE-USD | 13.48 | -0.14 | stop-loss |
| 2026-10-22T08:35 | Agent (ML meta-label) | sell | DOGE-USD | 8.26 | -0.21 | selected signal exited |
| 2026-10-22T08:35 | Stochastic reversion · 1h | buy | XRP-USD | 21.55 | — | entry |
| 2026-10-22T08:35 | Stochastic reversion · 1h | buy | SOL-USD | 16.01 | — | rebalance up |
| 2026-10-22T08:35 | Stochastic reversion · 1h | sell | ETH-USD | 12.50 | -0.27 | stop-loss |
| 2026-10-22T08:35 | Stochastic reversion · 1h | sell | DOGE-USD | 12.52 | -0.31 | stop-loss |
| 2026-10-22T08:35 | Stochastic reversion · 1h | sell | BTC-USD | 12.54 | -0.24 | stop-loss |
| 2026-10-22T08:35 | VWAP reversion | buy | BTC-USD | 5.18 | — | rebalance up |
| 2026-10-22T08:35 | VWAP reversion | sell | XRP-USD | 12.91 | -0.15 | stop-loss |
| 2026-10-22T08:35 | VWAP reversion | sell | ETH-USD | 10.35 | -0.11 | stop-loss |
| 2026-10-22T08:35 | RSI(14) reversion | sell | XRP-USD | 13.46 | -0.16 | stop-loss |
| 2026-10-22T08:35 | RSI(14) reversion | sell | BTC-USD | 13.49 | -0.13 | stop-loss |
| 2026-10-22T08:31 | VWAP reversion | buy | BTC-USD | 2.60 | — | rebalance up |
| 2026-10-22T08:31 | VWAP reversion | sell | ETH-USD | 2.60 | -0.02 | rebalance down |
| 2026-10-22T08:30 | VWAP reversion | buy | BTC-USD | 5.23 | — | entry signal |
| 2026-10-22T08:30 | VWAP reversion | sell | SOL-USD | 2.61 | -0.02 | rebalance down |
| 2026-10-22T08:30 | VWAP reversion | sell | DOGE-USD | 2.61 | -0.02 | rebalance down |
| 2026-10-22T08:30 | RSI(14) reversion | buy | SOL-USD | 13.57 | — | entry signal |
| 2026-10-22T08:25 | Agent (ML meta-label) | buy | SOL-USD | 7.63 | — | entry |
| 2026-10-22T08:25 | Agent (ML meta-label) | sell | XRP-USD | 9.20 | -0.11 | selected signal exited |
| 2026-10-22T08:21 | VWAP reversion | buy | XRP-USD | 2.59 | — | rebalance up |
| 2026-10-22T08:21 | VWAP reversion | buy | SOL-USD | 2.61 | — | rebalance up |
| 2026-10-22T08:21 | VWAP reversion | buy | ETH-USD | 2.61 | — | rebalance up |
| 2026-10-22T08:21 | VWAP reversion | buy | DOGE-USD | 2.61 | — | rebalance up |
| 2026-10-22T08:21 | VWAP reversion | sell | BTC-USD | 10.42 | -0.09 | stop-loss |
| 2026-10-22T08:15 | VWAP reversion | buy | XRP-USD | 10.46 | — | entry signal |
| 2026-10-22T08:15 | VWAP reversion | buy | SOL-USD | 10.47 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-24 08:49:05.000152+00:00 -> 2026-10-22 08:59:05.000152+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
