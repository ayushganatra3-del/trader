# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-27T17:05:05.000174+00:00 · 38075 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £90.06 (-9.94%)

Closed trades 113, win rate 38.9%, fees £3.45, max drawdown -11.45%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| PLTR | 18.09 | +0.11 |

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

Today: 24619 decisions in 2498 calls, $0.3104 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-27T17:05 | 3 / 15 / 11 | cash |  |
| Breezy | 2026-10-27T17:05 | 0 / 25 / 4 | cash |  |
| Boozy | 2026-10-27T17:05 | 7 / 20 / 2 | ETHU 70% |  |

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
| 1 | Copy: Warren Buffett (BRK-B) | copy | 107.49 | 7.49 | 0 | — | 7.99 | 3.97 | -5.18 | 1 |
| 2 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 106.42 | 6.42 | 14 | 71.4 | 3.72 | 1.22 | -6.57 | 26 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 105.17 | 5.17 | 19 | 47.4 | 7.86 | 2.54 | -4.92 | 25 |
| 4 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 104.77 | 4.76 | 22 | 31.8 | 10.67 | 2.75 | -5.17 | 43 |
| 5 | Daily: SMA 20/50 cross · AAPL | daily | 100.72 | 0.72 | 0 | — | 2.37 | 1.12 | -5.02 | 1 |
| 6 | VWAP reversion · 1h | reversion | 100.53 | 0.53 | 90 | 45.6 | -13.18 | -3.64 | -14.11 | 149 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Hold SPY | benchmark | 99.50 | -0.50 | 0 | — | 0.41 | 0.29 | -3.13 | 1 |
| 10 | Day trade: Stocks in Play ORB | daytrade | 99.00 | -1.00 | 82 | 35.4 | 7.11 | 3.40 | -1.80 | 98 |
| 11 | Copy: Congress Democrats (NANC) | copy | 97.79 | -2.21 | 0 | — | 0.73 | 0.37 | -5.99 | 1 |
| 12 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 97.78 | -2.22 | 14 | 21.4 | -3.15 | -4.23 | -3.99 | 21 |
| 13 | Timing: Nasdaq FTD · QQQ | daily | 97.06 | -2.94 | 1 | 0.0 | -3.06 | -1.93 | -5.83 | 1 |
| 14 | Agent (rotation) | meta | 96.23 | -3.77 | 122 | 31.1 | -2.39 | -1.36 | -6.39 | 180 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 96.02 | -3.98 | 0 | — | -5.80 | -2.36 | -7.83 | 1 |
| 16 | Daily: Connors RSI(2) · 3x ETFs | daily | 95.72 | -4.28 | 5 | 40.0 | 4.92 | 1.15 | -7.93 | 8 |
| 17 | Hold BTC | benchmark | 95.66 | -4.34 | 0 | — | 2.16 | 0.52 | -9.28 | 1 |
| 18 | Three white soldiers · 1h | momentum | 95.48 | -4.52 | 15 | 13.3 | -2.87 | -2.48 | -4.59 | 27 |
| 19 | Gap and go | momentum | 95.47 | -4.53 | 114 | 27.2 | 5.81 | 1.87 | -8.76 | 210 |
| 20 | Opening range 30m | breakout | 93.53 | -6.47 | 272 | 34.2 | -9.74 | -2.89 | -17.21 | 593 |
| 21 | Donchian 55/20 · 1h | breakout | 93.49 | -6.51 | 49 | 16.3 | -13.10 | -2.95 | -15.45 | 97 |
| 22 | Trend pullback · 1h | trend | 93.47 | -6.53 | 96 | 22.9 | -21.96 | -7.01 | -22.19 | 116 |
| 23 | Copy: Insider buying | copy | 92.51 | -7.49 | 27 | 37.0 | -18.91 | -3.64 | -22.94 | 63 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 92.49 | -7.51 | 0 | — | -1.48 | -0.07 | -14.57 | 1 |
| 25 | Parabolic SAR · 1h | trend | 91.96 | -8.04 | 121 | 25.6 | -20.53 | -5.08 | -23.02 | 247 |
| 26 | Daily: Momentum burst | daily | 91.86 | -8.14 | 13 | 15.4 | -17.87 | -3.44 | -19.44 | 39 |
| 27 | ADX DI cross · 1h | trend | 91.69 | -8.31 | 119 | 18.5 | -11.12 | -2.37 | -14.45 | 275 |
| 28 | Daily: Bullish score | daily | 91.31 | -8.69 | 11 | 18.2 | -5.89 | -0.68 | -14.40 | 14 |
| 29 | Timing: Nasdaq FTD · TQQQ | daily | 91.23 | -8.77 | 1 | 0.0 | -9.96 | -2.09 | -16.91 | 1 |
| 30 | Max aggression: 5-day momentum | meta | 91.04 | -8.96 | 12 | 41.7 | -14.48 | -1.30 | -27.23 | 25 |
| 31 | Squeeze breakout · 1h | breakout | 90.90 | -9.10 | 52 | 23.1 | -4.60 | -1.20 | -12.07 | 95 |
| 32 | Volume breakout · 1h | breakout | 90.15 | -9.85 | 108 | 25.9 | -12.21 | -2.52 | -15.94 | 112 |
| 33 | Agent | meta | 90.06 | -9.94 | 113 | 38.9 | -11.28 | -7.08 | -12.47 | 221 |
| 34 | Bollinger breakout · 1h | breakout | 88.76 | -11.24 | 109 | 26.6 | -12.98 | -2.56 | -18.15 | 249 |
| 35 | Agent (aggressive) | meta | 88.23 | -11.77 | 56 | 35.7 | -10.53 | -3.45 | -14.77 | 96 |
| 36 | Stochastic reversion · 1h | reversion | 87.87 | -12.13 | 205 | 47.3 | -21.52 | -3.96 | -22.80 | 394 |
| 37 | Keltner breakout · 1h | breakout | 87.06 | -12.94 | 74 | 23.0 | -21.50 | -4.27 | -23.42 | 189 |
| 38 | Opening range 15m | breakout | 87.01 | -12.99 | 338 | 30.8 | -13.51 | -3.75 | -17.87 | 719 |
| 39 | Z-score reversion · 1h | reversion | 86.72 | -13.28 | 125 | 36.0 | -12.71 | -2.01 | -21.48 | 211 |
| 40 | Supertrend · 1h | trend | 85.64 | -14.36 | 114 | 14.0 | -25.57 | -5.20 | -28.20 | 230 |
| 41 | Connors RSI(2) · 1h | reversion | 85.18 | -14.82 | 176 | 40.9 | -24.35 | -7.41 | -24.94 | 197 |
| 42 | RSI momentum · 1h | momentum | 84.90 | -15.10 | 104 | 15.4 | -21.55 | -4.38 | -24.34 | 211 |
| 43 | MACD cross · 1h | trend | 84.28 | -15.72 | 244 | 22.1 | -28.48 | -5.35 | -30.42 | 473 |
| 44 | EMA 20/50 cross · 1h | trend | 84.07 | -15.93 | 73 | 11.0 | -23.03 | -4.68 | -24.37 | 134 |
| 45 | Ichimoku · 1h | trend | 83.71 | -16.29 | 68 | 11.8 | -20.19 | -4.14 | -24.73 | 111 |
| 46 | MFI reversion · 1h | reversion | 83.45 | -16.55 | 272 | 32.4 | -16.20 | -2.50 | -20.70 | 153 |
| 47 | Triple EMA stack · 1h | trend | 83.27 | -16.73 | 101 | 14.9 | -28.56 | -5.47 | -31.33 | 203 |
| 48 | CCI reversion · 1h | reversion | 82.33 | -17.67 | 230 | 45.2 | -23.51 | -3.34 | -28.06 | 465 |
| 49 | Williams %R · 1h | reversion | 81.91 | -18.09 | 232 | 47.0 | -35.45 | -5.97 | -36.34 | 535 |
| 50 | Donchian 20/10 · 1h | breakout | 81.82 | -18.18 | 99 | 20.2 | -24.32 | -4.66 | -26.89 | 222 |
| 51 | MACD zero-line · 1h | trend | 81.27 | -18.73 | 111 | 15.3 | -24.30 | -5.23 | -25.57 | 231 |
| 52 | Bollinger reversion · 1h | reversion | 80.83 | -19.17 | 182 | 37.4 | -29.38 | -5.98 | -30.47 | 365 |
| 53 | Agent (ML meta-label) | meta | 80.78 | -19.22 | 968 | 20.7 | -10.10 | -2.03 | -17.84 | 350 |
| 54 | RSI(14) reversion · 1h | reversion | 80.20 | -19.80 | 107 | 27.1 | -18.22 | -3.45 | -24.48 | 190 |
| 55 | OBV trend · 1h | momentum | 80.15 | -19.85 | 209 | 17.7 | -30.78 | -6.55 | -32.60 | 295 |
| 56 | ROC + volume · 1h | momentum | 79.01 | -20.99 | 259 | 25.9 | -31.41 | -6.12 | -33.32 | 385 |
| 57 | Heikin-Ashi · 1h | trend | 78.22 | -21.78 | 295 | 22.7 | -43.38 | -9.58 | -44.65 | 672 |
| 58 | Three white soldiers | momentum | 77.35 | -22.65 | 321 | 19.0 | -44.56 | -20.14 | -45.09 | 606 |
| 59 | Candlestick reversal · 1h | reversion | 77.29 | -22.71 | 282 | 29.4 | -34.38 | -6.64 | -35.20 | 560 |
| 60 | VWAP momentum · 1h | momentum | 76.86 | -23.14 | 567 | 21.9 | -48.77 | -10.51 | -50.95 | 1241 |
| 61 | EMA 9/21 cross · 1h | trend | 76.54 | -23.46 | 176 | 10.8 | -30.92 | -6.67 | -32.69 | 339 |
| 62 | Max aggression: 1-day momentum | meta | 71.89 | -28.11 | 20 | 30.0 | -38.18 | -2.49 | -50.32 | 42 |
| 63 | ROC + volume | momentum | 54.06 | -45.94 | 803 | 22.4 | -74.80 | -26.60 | -75.29 | 1586 |
| 64 | Volume breakout | breakout | 52.72 | -47.28 | 481 | 12.9 | -63.09 | -25.94 | -63.60 | 811 |
| 65 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.85 | -42.34 | -98.87 | 5157 |
| 66 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -79.18 | -23.09 | -79.95 | 1417 |
| 67 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.61 | -42.23 | -93.79 | 2532 |
| 68 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -89.15 | -29.95 | -89.33 | 1926 |
| 69 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.38 | -36.63 | -91.58 | 2344 |
| 70 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.41 | -31.82 | -90.48 | 2176 |
| 71 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.83 | -48.53 | -97.89 | 3505 |
| 72 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.07 | -51.90 | -96.19 | 3378 |
| 73 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.14 | -36.30 | -94.14 | 2458 |
| 74 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.25 | -32.57 | -82.62 | 1689 |
| 75 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.41 | -51.44 | -99.42 | 5758 |
| 76 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.70 | -41.04 | -92.92 | 2644 |
| 77 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.44 | -38.52 | -95.45 | 3379 |
| 78 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.78 | -69.66 | -99.78 | 6166 |
| 79 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.27 | -44.05 | -92.34 | 2321 |
| 80 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.75 | -60.95 | -97.76 | 3581 |
| 81 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.66 | -57.95 | -98.67 | 4794 |
| 82 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 83 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -67.78 | -28.33 | -68.58 | 1180 |
| 84 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.58 | -53.99 | -94.63 | 2782 |
| 85 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.30 | -37.94 | -84.56 | 1833 |
| 86 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.61 | -64.13 | -99.61 | 6296 |
| 87 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -88.25 | -28.67 | -88.27 | 2227 |
| 88 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -76.65 | -18.92 | -76.93 | 1680 |
| 89 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.62 | -36.67 | -90.71 | 2266 |
| 90 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -96.26 | -46.91 | -96.28 | 3822 |
| 91 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -90.09 | -49.57 | -90.10 | 2128 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -72.78 | -24.02 | -73.52 | 1293 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -76.15 | -17.88 | -76.40 | 1582 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -96.55 | -48.32 | -96.55 | 4195 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.92 | -93.42 | -99.92 | 8303 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-27T17:05 | Agent (ML meta-label) | sell | AMD | 20.17 | -0.02 | selected signal exited |
| 2026-10-27T17:01 | MFI reversion · 1h | sell | BTC-USD | 20.83 | 0.01 | exit signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | buy | ETH-USD | 13.72 | — | entry signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | buy | BTC-USD | 18.22 | — | entry signal |
| 2026-10-27T17:01 | Squeeze breakout · 1h | sell | XRP-USD | 4.57 | -0.01 | rebalance down |
| 2026-10-27T17:01 | Squeeze breakout · 1h | sell | IWM | 4.76 | 0.03 | rebalance down |
| 2026-10-27T16:55 | Agent (ML meta-label) | buy | NVDA | 4.04 | — | rebalance up |
| 2026-10-27T16:55 | Agent (ML meta-label) | buy | AMD | 4.04 | — | rebalance up |
| 2026-10-27T16:55 | Agent (ML meta-label) | sell | META | 12.07 | -0.02 | selected signal exited |
| 2026-10-27T16:50 | VWAP momentum · 1h | buy | ETHU | 1.59 | — | entry |
| 2026-10-27T16:50 | VWAP momentum · 1h | buy | COIN | 2.95 | — | entry |
| 2026-10-27T16:50 | VWAP momentum · 1h | sell | BTC-USD | 3.89 | 0.01 | rebalance down |
| 2026-10-27T16:50 | Gap and go | buy | TNA | 7.87 | — | rebalance up |
| 2026-10-27T16:50 | Gap and go | buy | SOXL | 4.77 | — | rebalance up |
| 2026-10-27T16:50 | Gap and go | buy | AMD | 7.95 | — | rebalance up |
| 2026-10-27T16:50 | Gap and go | sell | TQQQ | 19.00 | 0.19 | stop-loss |
| 2026-10-27T16:50 | ROC + volume | sell | TSLA | 13.52 | -0.01 | exit signal |
| 2026-10-27T16:50 | ROC + volume | sell | SOXL | 13.50 | -0.08 | exit signal |
| 2026-10-27T16:45 | Agent (ML meta-label) | buy | META | 12.10 | — | following VWAP reversion |
| 2026-10-27T16:45 | Agent (ML meta-label) | sell | NVDA | 4.06 | -0.01 | rebalance down |
| 2026-10-27T16:45 | Agent (ML meta-label) | sell | AMD | 4.07 | -0.01 | rebalance down |
| 2026-10-27T16:45 | Gap and go | buy | SOXL | 9.81 | — | rebalance up |
| 2026-10-27T16:45 | Gap and go | sell | TECL | 15.94 | 0.27 | stop-loss |
| 2026-10-27T16:45 | ROC + volume | buy | TSLA | 9.34 | — | rebalance up |
| 2026-10-27T16:45 | ROC + volume | buy | SOXL | 9.04 | — | rebalance up |
| 2026-10-27T16:45 | ROC + volume | buy | AMZN | 9.01 | — | rebalance up |
| 2026-10-27T16:45 | ROC + volume | sell | UPRO | 4.51 | -0.02 | exit signal |
| 2026-10-27T16:45 | ROC + volume | sell | TNA | 4.51 | -0.02 | exit signal |
| 2026-10-27T16:45 | ROC + volume | sell | TECL | 4.20 | 0.01 | exit signal |
| 2026-10-27T16:45 | ROC + volume | sell | QQQ | 4.19 | 0.00 | exit signal |
| 2026-10-27T16:45 | ROC + volume | sell | NVDA | 4.19 | 0.00 | stop-loss |
| 2026-10-27T16:45 | ROC + volume | sell | LABU | 4.47 | -0.06 | stop-loss |
| 2026-10-27T16:45 | ROC + volume | sell | ETHU | 4.19 | 0.01 | exit signal |
| 2026-10-27T16:45 | ROC + volume | sell | AMD | 3.01 | -0.01 | exit signal |
| 2026-10-27T16:41 | Day trade: Stocks in Play ORB | sell | SOXL | 25.01 | 0.42 | target is flat |
| 2026-10-27T16:41 | Agent (ML meta-label) | buy | NVDA | 20.21 | — | entry |
| 2026-10-27T16:41 | Agent (ML meta-label) | sell | MSFT | 20.20 | -0.03 | selected signal exited |
| 2026-10-27T16:41 | MFI reversion · 1h | buy | GOOGL | 20.91 | — | entry |
| 2026-10-27T16:41 | Candlestick reversal · 1h | buy | NVDA | 6.85 | — | entry |
| 2026-10-27T16:41 | Volume breakout · 1h | buy | SPY | 12.89 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-29 17:05:05.000174+00:00 -> 2026-10-27 17:15:05.000174+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
