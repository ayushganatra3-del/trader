# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-11-17T15:10:05.000149+00:00 · 63304 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £85.86 (-14.14%)

Closed trades 204, win rate 36.3%, fees £5.78, max drawdown -15.45%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-11-17 | FUN 12%, STWD 12%, LRN 12%, PSEC 12%, BH 12%, LILA 12%, HUBS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-11-16)

**Correction** since 2026-11-13 · level correction · 2 distribution days in 25 sessions · timing exposure 0% · VXN 32.90 · VIX 22.91 · last follow-through day 2026-11-11

Best bullish scores: SQQQ 8.1, AAPL 6.2, AMZN 4.5, TSLA 2.6, META 2.0, AMD 1.5

### AI bees (Jev: typesafe/jev-1.13)

Today: 14727 decisions in 2421 calls, $0.1986 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-11-17T15:10 | 1 / 5 / 25 | cash |  |
| Breezy | 2026-11-17T15:10 | 0 / 25 / 6 | cash |  |
| Boozy | 2026-11-17T15:10 | 3 / 20 / 8 | cash |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| MACD cross | COIN | 2.37 | +4.67% | 10 |
| Z-score reversion | SOXL | 2.33 | +17.16% | 6 |
| CCI reversion | SOXL | 2.24 | +17.57% | 11 |
| RSI momentum | TNA | 2.20 | +2.71% | 4 |
| RSI momentum | IWM | 2.02 | +0.61% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Copy: Warren Buffett (BRK-B) | copy | 117.38 | 17.38 | 0 | — | 13.21 | 4.40 | -5.18 | 1 |
| 2 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 112.95 | 12.95 | 37 | 32.4 | 19.00 | 2.84 | -8.66 | 44 |
| 3 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 110.78 | 10.78 | 24 | 62.5 | 16.04 | 3.26 | -5.42 | 27 |
| 4 | Daily: SMA 20/50 cross · AAPL | daily | 104.27 | 4.27 | 0 | — | 6.20 | 1.69 | -6.60 | 0 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.39 | 1.40 | 36 | 41.7 | -0.06 | 0.11 | -9.64 | 32 |
| 6 | Gap and go | momentum | 100.14 | 0.14 | 194 | 33.0 | 7.67 | 2.13 | -9.06 | 224 |
| 7 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 8 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 9 | Day trade: Stocks in Play ORB | daytrade | 100.00 | -0.00 | 148 | 35.1 | -2.48 | -2.10 | -4.08 | 71 |
| 10 | Daily: Connors RSI(2) · 3x ETFs | daily | 98.33 | -1.67 | 8 | 50.0 | -1.28 | 0.16 | -18.69 | 6 |
| 11 | Hold SPY | benchmark | 96.22 | -3.78 | 0 | — | -3.14 | -0.99 | -6.18 | 1 |
| 12 | Timing: Nasdaq FTD · QQQ | daily | 95.20 | -4.80 | 2 | 0.0 | -5.02 | -2.99 | -7.38 | 2 |
| 13 | Three white soldiers · 1h | momentum | 93.89 | -6.12 | 20 | 10.0 | -3.42 | -3.20 | -5.99 | 22 |
| 14 | Agent (rotation) | meta | 93.88 | -6.12 | 197 | 29.9 | -1.84 | -0.59 | -8.15 | 158 |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 93.84 | -6.16 | 0 | — | -6.92 | -1.80 | -8.27 | 1 |
| 16 | Copy: Insider buying | copy | 91.89 | -8.12 | 47 | 42.6 | -8.59 | -1.69 | -14.79 | 62 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 91.88 | -8.12 | 24 | 16.7 | -9.29 | -7.71 | -9.46 | 22 |
| 18 | Copy: Congress Democrats (NANC) | copy | 91.67 | -8.33 | 0 | — | -7.07 | -1.89 | -11.05 | 1 |
| 19 | VWAP reversion · 1h | reversion | 90.96 | -9.04 | 152 | 46.1 | -11.42 | -3.33 | -18.48 | 147 |
| 20 | Trend pullback · 1h | trend | 90.28 | -9.72 | 113 | 23.9 | -15.36 | -6.94 | -17.30 | 65 |
| 21 | Squeeze breakout · 1h | breakout | 87.36 | -12.64 | 67 | 20.9 | -11.21 | -4.40 | -16.20 | 73 |
| 22 | Timing: Nasdaq FTD · TQQQ | daily | 87.28 | -12.72 | 2 | 0.0 | -15.30 | -3.10 | -20.94 | 2 |
| 23 | Daily: Bullish score | daily | 87.11 | -12.89 | 17 | 17.6 | -3.79 | -0.55 | -19.56 | 14 |
| 24 | Opening range 30m | breakout | 86.09 | -13.91 | 437 | 33.6 | -10.05 | -3.19 | -14.11 | 574 |
| 25 | Agent | meta | 85.86 | -14.14 | 204 | 36.3 | -14.58 | -7.17 | -16.15 | 197 |
| 26 | Agent (aggressive) | meta | 82.74 | -17.26 | 98 | 33.7 | -16.47 | -4.54 | -17.06 | 95 |
| 27 | Parabolic SAR · 1h | trend | 82.72 | -17.28 | 181 | 28.2 | -25.18 | -6.90 | -26.75 | 205 |
| 28 | Keltner breakout · 1h | breakout | 80.85 | -19.15 | 121 | 25.6 | -18.01 | -4.03 | -25.47 | 159 |
| 29 | Connors RSI(2) · 1h | reversion | 80.36 | -19.64 | 214 | 40.2 | -14.40 | -6.35 | -14.84 | 95 |
| 30 | Donchian 55/20 · 1h | breakout | 80.31 | -19.69 | 76 | 13.2 | -24.96 | -6.49 | -29.06 | 84 |
| 31 | Volume breakout · 1h | breakout | 79.59 | -20.41 | 162 | 28.4 | -16.94 | -5.37 | -22.48 | 86 |
| 32 | Max aggression: 5-day momentum | meta | 79.13 | -20.87 | 21 | 42.9 | -48.58 | -3.25 | -55.24 | 22 |
| 33 | Opening range 15m | breakout | 78.07 | -21.93 | 531 | 31.6 | -16.79 | -4.51 | -21.37 | 686 |
| 34 | Copy: Cathie Wood (ARKK) | copy | 77.18 | -22.82 | 2 | 0.0 | -14.83 | -1.82 | -24.55 | 1 |
| 35 | Max aggression: 1-day momentum | meta | 75.91 | -24.09 | 30 | 26.7 | -25.13 | -0.99 | -57.50 | 39 |
| 36 | Hold BTC | benchmark | 75.51 | -24.49 | 2 | 0.0 | -15.10 | -2.12 | -28.91 | 1 |
| 37 | Ichimoku · 1h | trend | 75.16 | -24.84 | 101 | 14.9 | -29.39 | -8.54 | -29.91 | 112 |
| 38 | ADX DI cross · 1h | trend | 74.99 | -25.01 | 207 | 19.3 | -28.44 | -4.58 | -35.77 | 259 |
| 39 | Bollinger breakout · 1h | breakout | 74.14 | -25.86 | 186 | 22.0 | -24.39 | -5.20 | -31.76 | 235 |
| 40 | Stochastic reversion · 1h | reversion | 73.63 | -26.37 | 333 | 44.1 | -32.86 | -4.88 | -33.49 | 415 |
| 41 | MFI reversion · 1h | reversion | 71.78 | -28.22 | 421 | 34.2 | -24.60 | -3.52 | -27.91 | 162 |
| 42 | Supertrend · 1h | trend | 71.76 | -28.24 | 187 | 16.0 | -31.96 | -5.44 | -38.90 | 202 |
| 43 | MACD zero-line · 1h | trend | 71.47 | -28.54 | 178 | 18.0 | -26.16 | -5.18 | -32.48 | 199 |
| 44 | RSI momentum · 1h | momentum | 71.25 | -28.75 | 175 | 14.3 | -30.86 | -5.62 | -37.39 | 202 |
| 45 | Triple EMA stack · 1h | trend | 71.24 | -28.76 | 154 | 14.9 | -31.24 | -6.26 | -37.12 | 181 |
| 46 | Heikin-Ashi · 1h | trend | 70.88 | -29.12 | 461 | 23.2 | -39.26 | -7.50 | -43.58 | 639 |
| 47 | EMA 20/50 cross · 1h | trend | 70.68 | -29.32 | 112 | 9.8 | -35.59 | -9.76 | -38.77 | 114 |
| 48 | ROC + volume · 1h | momentum | 70.23 | -29.77 | 405 | 28.4 | -28.26 | -4.66 | -37.60 | 356 |
| 49 | MACD cross · 1h | trend | 70.06 | -29.94 | 409 | 22.2 | -34.41 | -5.03 | -43.62 | 477 |
| 50 | Daily: Momentum burst | daily | 69.40 | -30.60 | 30 | 13.3 | -35.54 | -4.89 | -37.91 | 32 |
| 51 | OBV trend · 1h | momentum | 68.90 | -31.10 | 304 | 19.1 | -34.55 | -7.30 | -39.35 | 262 |
| 52 | Donchian 20/10 · 1h | breakout | 67.51 | -32.49 | 158 | 18.4 | -31.27 | -5.29 | -39.31 | 208 |
| 53 | CCI reversion · 1h | reversion | 67.34 | -32.66 | 378 | 42.1 | -40.92 | -6.69 | -42.39 | 458 |
| 54 | Bollinger reversion · 1h | reversion | 66.00 | -34.00 | 336 | 38.7 | -36.90 | -5.59 | -37.30 | 408 |
| 55 | Williams %R · 1h | reversion | 63.99 | -36.01 | 422 | 41.5 | -44.97 | -7.59 | -45.31 | 545 |
| 56 | EMA 9/21 cross · 1h | trend | 63.54 | -36.46 | 278 | 11.2 | -40.19 | -8.01 | -45.62 | 320 |
| 57 | Agent (ML meta-label) | meta | 60.45 | -39.55 | 1879 | 24.5 | -23.00 | -3.79 | -26.43 | 329 |
| 58 | RSI(14) reversion · 1h | reversion | 59.07 | -40.94 | 204 | 31.9 | -40.86 | -6.01 | -41.95 | 240 |
| 59 | Z-score reversion · 1h | reversion | 58.93 | -41.07 | 221 | 35.7 | -35.62 | -4.92 | -36.86 | 244 |
| 60 | VWAP momentum · 1h | momentum | 57.66 | -42.34 | 950 | 21.7 | -52.70 | -9.33 | -57.59 | 1203 |
| 61 | Candlestick reversal · 1h | reversion | 56.65 | -43.35 | 538 | 27.0 | -46.10 | -8.38 | -46.20 | 616 |
| 62 | Three white soldiers | momentum | 55.89 | -44.12 | 578 | 14.7 | -49.32 | -22.00 | -49.49 | 659 |
| 63 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -99.01 | -43.70 | -99.01 | 5303 |
| 64 | EMA 20/50 cross ⛔ | trend | 50.58 | -49.42 | 644 | 20.0 | -81.18 | -25.31 | -81.80 | 1419 |
| 65 | Triple EMA stack ⛔ | trend | 50.49 | -49.51 | 666 | 15.5 | -93.94 | -43.01 | -93.96 | 2495 |
| 66 | Supertrend ⛔ | trend | 50.43 | -49.57 | 642 | 19.5 | -90.14 | -31.65 | -90.18 | 1939 |
| 67 | RSI momentum ⛔ | momentum | 50.40 | -49.60 | 658 | 16.7 | -91.30 | -39.14 | -91.34 | 2304 |
| 68 | Trend pullback ⛔ | trend | 50.40 | -49.60 | 637 | 14.1 | -90.00 | -30.67 | -90.02 | 2138 |
| 69 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.92 | -47.67 | -97.92 | 3470 |
| 70 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.50 | -53.40 | -96.50 | 3432 |
| 71 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -93.68 | -37.59 | -93.72 | 2259 |
| 72 | Ichimoku ⛔ | trend | 50.30 | -49.70 | 572 | 11.4 | -82.74 | -33.16 | -82.74 | 1634 |
| 73 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.59 | -52.63 | -99.59 | 6056 |
| 74 | Donchian 20/10 ⛔ | breakout | 50.25 | -49.75 | 739 | 17.2 | -92.02 | -41.27 | -92.02 | 2579 |
| 75 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -95.17 | -37.67 | -95.17 | 3336 |
| 76 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.81 | -67.59 | -99.81 | 6150 |
| 77 | MACD zero-line ⛔ | trend | 50.15 | -49.85 | 682 | 14.8 | -92.38 | -43.43 | -92.38 | 2260 |
| 78 | ROC + volume ⛔ | momentum | 50.11 | -49.89 | 880 | 21.7 | -76.46 | -26.34 | -76.46 | 1662 |
| 79 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.65 | -57.96 | -97.65 | 3459 |
| 80 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -99.00 | -55.12 | -99.00 | 4949 |
| 81 | AI bee: Boozy ⛔ | ai | 49.97 | -50.03 | 347 | 5.8 | — | — | — | — |
| 82 | Squeeze breakout ⛔ | breakout | 49.93 | -50.07 | 610 | 14.1 | -68.46 | -27.00 | -68.53 | 1235 |
| 83 | Bollinger breakout ⛔ | breakout | 49.93 | -50.07 | 685 | 14.5 | -94.63 | -54.66 | -94.64 | 2755 |
| 84 | Keltner breakout ⛔ | breakout | 49.91 | -50.09 | 708 | 16.7 | -84.52 | -37.55 | -84.54 | 1748 |
| 85 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.69 | -64.86 | -99.69 | 6378 |
| 86 | Z-score reversion ⛔ | reversion | 49.91 | -50.09 | 678 | 22.0 | -90.47 | -29.69 | -90.50 | 2322 |
| 87 | RSI(14) reversion ⛔ | reversion | 49.88 | -50.12 | 865 | 25.9 | -79.76 | -18.67 | -79.85 | 1826 |
| 88 | MFI reversion ⛔ | reversion | 49.87 | -50.12 | 749 | 19.8 | -90.85 | -34.99 | -90.85 | 2152 |
| 89 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -97.50 | -45.06 | -97.50 | 3920 |
| 90 | ADX DI cross ⛔ | trend | 49.84 | -50.16 | 668 | 10.2 | -89.48 | -60.53 | -89.49 | 2163 |
| 91 | Volume breakout ⛔ | breakout | 49.84 | -50.16 | 526 | 12.5 | -66.59 | -30.53 | -66.59 | 830 |
| 92 | Donchian 55/20 ⛔ | breakout | 49.83 | -50.17 | 629 | 19.2 | -71.93 | -23.22 | -72.49 | 1242 |
| 93 | VWAP reversion ⛔ | reversion | 49.77 | -50.23 | 825 | 24.8 | -80.31 | -17.53 | -80.45 | 1763 |
| 94 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -97.54 | -44.78 | -97.55 | 4349 |
| 95 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.94 | -97.89 | -99.94 | 8386 |
| 96 | AI bee: Bizzy ⛔ | ai | 49.68 | -50.32 | 1067 | 8.9 | — | — | — | — |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-11-17T15:10 | Agent (aggressive) | sell | COIN | 41.07 | -0.60 | selected signal exited |
| 2026-11-17T15:10 | Agent | sell | COIN | 16.98 | -0.25 | selected signal exited |
| 2026-11-17T15:10 | Opening range 30m | buy | SQQQ | 21.52 | — | entry signal |
| 2026-11-17T15:10 | Opening range 15m | buy | SQQQ | 19.52 | — | entry signal |
| 2026-11-17T15:05 | MFI reversion · 1h | buy | BTC-USD | 4.83 | — | rebalance up |
| 2026-11-17T15:05 | MFI reversion · 1h | sell | ETHU | 10.16 | -0.14 | target is flat |
| 2026-11-17T15:05 | Three white soldiers | sell | UPRO | 13.90 | -0.09 | exit signal |
| 2026-11-17T15:00 | Agent (ML meta-label) | sell | SQQQ | 15.06 | -0.12 | selected signal exited |
| 2026-11-17T15:00 | Agent (ML meta-label) | sell | SPY | 15.16 | -0.01 | selected signal exited |
| 2026-11-17T15:00 | OBV trend · 1h | buy | XRP-USD | 17.24 | — | entry signal |
| 2026-11-17T15:00 | ROC + volume · 1h | buy | DOGE-USD | 16.59 | — | entry signal |
| 2026-11-17T15:00 | ROC + volume · 1h | buy | BTC-USD | 17.60 | — | entry signal |
| 2026-11-17T15:00 | VWAP momentum · 1h | buy | SQQQ | 5.16 | — | rebalance up |
| 2026-11-17T15:00 | VWAP momentum · 1h | sell | ETH-USD | 7.17 | -0.08 | exit signal |
| 2026-11-17T15:00 | Parabolic SAR · 1h | buy | DOGE-USD | 20.82 | — | entry signal |
| 2026-11-17T15:00 | MACD zero-line · 1h | buy | BTC-USD | 17.11 | — | entry signal |
| 2026-11-17T15:00 | Triple EMA stack · 1h | buy | SOL-USD | 17.80 | — | entry signal |
| 2026-11-17T15:00 | EMA 20/50 cross · 1h | buy | XRP-USD | 17.74 | — | entry signal |
| 2026-11-17T15:00 | Three white soldiers | buy | UPRO | 13.99 | — | entry signal |
| 2026-11-17T15:00 | Opening range 15m | buy | AMZN | 19.53 | — | entry signal |
| 2026-11-17T14:55 | Day trade: Stocks in Play ORB | sell | MSTR | 24.83 | -0.25 | target is flat |
| 2026-11-17T14:55 | Agent (ML meta-label) | buy | SQQQ | 15.18 | — | entry |
| 2026-11-17T14:55 | Agent (ML meta-label) | buy | SPY | 15.18 | — | entry |
| 2026-11-17T14:55 | Opening range 15m | buy | AAPL | 19.53 | — | entry signal |
| 2026-11-17T14:50 | Day trade: Stocks in Play ORB | buy | AMZN | 25.09 | — | entry |
| 2026-11-17T14:45 | Agent (rotation) | sell | SQQQ | 31.31 | 0.03 | selected signal exited |
| 2026-11-17T14:45 | Day trade: Stocks in Play ORB | sell | SQQQ | 25.16 | 0.08 | target is flat |
| 2026-11-17T14:45 | Day trade: ORB 5m · TQQQ/SQQQ | sell | SQQQ | 112.95 | 0.11 | target is flat |
| 2026-11-17T14:45 | Agent (aggressive) | buy | COIN | 41.67 | — | following MACD cross |
| 2026-11-17T14:45 | Agent | buy | COIN | 17.22 | — | following MACD cross |
| 2026-11-17T14:45 | Candlestick reversal · 1h | buy | IWM | 2.47 | — | entry |
| 2026-11-17T14:45 | OBV trend · 1h | sell | META | 17.18 | -0.12 | stop-loss |
| 2026-11-17T14:42 | Agent (ML meta-label) | sell | META | 15.21 | -0.02 | selected signal exited |
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | SQQQ | 25.08 | — | entry |
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | MSTR | 25.08 | — | entry |
| 2026-11-17T14:40 | Day trade: Stocks in Play ORB | buy | COIN | 25.08 | — | entry |
| 2026-11-17T14:40 | Agent (ML meta-label) | buy | META | 15.22 | — | entry |
| 2026-11-17T14:35 | Agent (rotation) | buy | SQQQ | 31.28 | — | entry |
| 2026-11-17T14:35 | Day trade: ORB 5m · TQQQ/SQQQ | buy | SQQQ | 112.84 | — | entry |
| 2026-11-17T14:35 | Agent (ML meta-label) | buy | NVDA | 15.21 | — | entry |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-09-19 15:10:05.000149+00:00 -> 2026-11-17 15:20:05.000149+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no price data found  (5m 2026-09-19 15:10:05.000149+00:00 -> 2026-11-17 15:20:05.000149+00:00); yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
