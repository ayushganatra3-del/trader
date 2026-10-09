# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-09T10:00:05.000143+00:00 · 16622 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.71 (-4.29%)

Closed trades 50, win rate 54.0%, fees £2.06, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| MSFT | 19.14 | -0.01 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BORR 12%, BPRE 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-08)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 21.98 · VIX 15.41 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.3, AMD 7.1, TECL 6.1, BITX 6.0, MSTR 6.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 7200 decisions in 1440 calls, $0.1006 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-09T10:00 | 0 / 4 / 1 | SOXL 15%, AMD 15% |  |
| Breezy | 2026-10-09T10:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-09T10:00 | 1 / 4 / 0 | COIN 74% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Bollinger reversion | SOXL | 2.37 | +5.31% | 12 |
| MFI reversion | IWM | 2.15 | +1.05% | 5 |
| Bollinger reversion · 1h | UPRO | 2.07 | +5.59% | 3 |
| Bollinger breakout | BITX | 1.96 | +1.97% | 6 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.00 | 3.00 | 36 | 41.7 | -8.13 | -2.48 | -13.79 | 120 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.71 | -7.93 | 7 |
| 3 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.83 | -3.68 | 18 |
| 4 | Copy: Warren Buffett (BRK-B) | copy | 101.37 | 1.37 | 0 | — | -4.29 | -1.79 | -7.31 | 1 |
| 5 | Timing: Nasdaq FTD · TQQQ | daily | 101.22 | 1.22 | 0 | — | -6.17 | -1.07 | -15.27 | 1 |
| 6 | Hold SPY | benchmark | 100.67 | 0.67 | 0 | — | -0.11 | -0.02 | -3.66 | 1 |
| 7 | Copy: Congress Democrats (NANC) | copy | 100.63 | 0.63 | 0 | — | 1.17 | 0.59 | -3.62 | 1 |
| 8 | Timing: Nasdaq FTD · QQQ | daily | 100.62 | 0.62 | 0 | — | -1.64 | -0.89 | -5.09 | 1 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -3.83 | -1.25 | -9.74 | 25 |
| 10 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 11 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.72 | -0.28 | 0 | — | 0.61 | 0.31 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.97 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.26 | -0.74 | 6 | 33.3 | -1.41 | -1.47 | -3.04 | 21 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.18 | -1.52 | 86 |
| 16 | Hold BTC | benchmark | 98.73 | -1.27 | 0 | — | 26.73 | 3.19 | -8.68 | 1 |
| 17 | Copy: Hedge-fund gurus (GURU) | copy | 98.72 | -1.28 | 0 | — | -5.06 | -2.42 | -5.36 | 1 |
| 18 | Copy: Insider buying | copy | 98.43 | -1.57 | 12 | 50.0 | -15.88 | -2.79 | -21.08 | 71 |
| 19 | Stochastic reversion · 1h | reversion | 98.20 | -1.80 | 81 | 53.1 | -12.44 | -2.48 | -15.04 | 344 |
| 20 | Donchian 55/20 · 1h | breakout | 98.07 | -1.93 | 26 | 15.4 | 10.01 | 1.34 | -16.96 | 109 |
| 21 | Three white soldiers · 1h | momentum | 97.53 | -2.47 | 6 | 0.0 | -3.03 | -2.34 | -4.15 | 26 |
| 22 | Agent (rotation) | meta | 96.55 | -3.45 | 78 | 28.2 | 0.55 | 0.25 | -7.43 | 261 |
| 23 | Trend pullback · 1h | trend | 96.54 | -3.46 | 78 | 23.1 | -23.26 | -6.53 | -25.53 | 168 |
| 24 | ADX DI cross · 1h | trend | 96.42 | -3.58 | 54 | 22.2 | -3.42 | -0.45 | -13.84 | 244 |
| 25 | Copy: Cathie Wood (ARKK) | copy | 96.32 | -3.67 | 0 | — | 8.88 | 1.50 | -8.33 | 1 |
| 26 | EMA 20/50 cross · 1h | trend | 96.16 | -3.84 | 36 | 11.1 | 0.51 | 0.28 | -20.52 | 135 |
| 27 | Z-score reversion · 1h | reversion | 96.13 | -3.87 | 36 | 38.9 | -0.39 | 0.04 | -8.60 | 168 |
| 28 | Daily: Momentum burst | daily | 95.99 | -4.01 | 4 | 0.0 | -4.75 | -0.57 | -17.67 | 40 |
| 29 | Daily: Bullish score | daily | 95.74 | -4.26 | 3 | 0.0 | -1.35 | 0.02 | -12.76 | 10 |
| 30 | Agent | meta | 95.71 | -4.29 | 50 | 54.0 | -9.25 | -5.16 | -9.81 | 244 |
| 31 | MACD cross · 1h | trend | 95.21 | -4.79 | 105 | 22.9 | -17.50 | -2.77 | -18.84 | 460 |
| 32 | Parabolic SAR · 1h | trend | 95.12 | -4.88 | 82 | 22.0 | -4.58 | -0.46 | -20.80 | 289 |
| 33 | Squeeze breakout · 1h | breakout | 94.88 | -5.12 | 34 | 26.5 | 15.40 | 2.52 | -8.14 | 102 |
| 34 | Supertrend · 1h | trend | 94.37 | -5.63 | 51 | 13.7 | -5.23 | -0.56 | -18.09 | 213 |
| 35 | Agent (aggressive) | meta | 94.25 | -5.75 | 22 | 45.5 | -6.66 | -3.08 | -7.27 | 109 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.31 | 1.87 | -6.52 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.40 | -6.60 | 102 | 41.2 | -18.29 | -6.02 | -20.97 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.21 | 0.23 | -19.98 | 118 |
| 39 | Bollinger breakout · 1h | breakout | 92.55 | -7.45 | 65 | 30.8 | 6.38 | 0.97 | -12.06 | 285 |
| 40 | RSI momentum · 1h | momentum | 92.38 | -7.62 | 60 | 15.0 | 1.60 | 0.40 | -16.65 | 217 |
| 41 | RSI(14) reversion · 1h | reversion | 92.28 | -7.72 | 26 | 26.9 | -3.95 | -0.74 | -9.03 | 153 |
| 42 | Agent (ML meta-label) | meta | 92.17 | -7.83 | 364 | 18.1 | -4.85 | -0.75 | -13.91 | 389 |
| 43 | Volume breakout · 1h | breakout | 92.13 | -7.87 | 45 | 17.8 | 6.47 | 1.04 | -12.60 | 121 |
| 44 | Bollinger reversion · 1h | reversion | 91.57 | -8.43 | 68 | 33.8 | -21.98 | -5.31 | -23.94 | 318 |
| 45 | Max aggression: 1-day momentum | meta | 91.27 | -8.73 | 9 | 33.3 | -23.96 | -1.22 | -37.31 | 43 |
| 46 | Triple EMA stack · 1h | trend | 91.21 | -8.79 | 68 | 16.2 | -10.07 | -1.08 | -25.80 | 233 |
| 47 | MFI reversion · 1h | reversion | 91.01 | -8.99 | 99 | 30.3 | -14.92 | -2.55 | -16.99 | 129 |
| 48 | Opening range 30m | breakout | 90.76 | -9.23 | 131 | 20.6 | -17.37 | -5.24 | -17.94 | 562 |
| 49 | Candlestick reversal · 1h | reversion | 90.47 | -9.53 | 100 | 30.0 | -29.71 | -5.87 | -31.03 | 503 |
| 50 | MACD zero-line · 1h | trend | 90.34 | -9.66 | 58 | 20.7 | -5.71 | -0.59 | -19.00 | 238 |
| 51 | Williams %R · 1h | reversion | 90.18 | -9.82 | 107 | 44.9 | -26.95 | -4.74 | -27.50 | 516 |
| 52 | Three white soldiers | momentum | 89.14 | -10.86 | 122 | 18.9 | -47.86 | -22.88 | -47.91 | 581 |
| 53 | Opening range 15m | breakout | 88.59 | -11.41 | 153 | 19.0 | -19.52 | -5.58 | -20.06 | 683 |
| 54 | EMA 9/21 cross · 1h | trend | 88.44 | -11.56 | 99 | 14.1 | -11.07 | -1.29 | -20.75 | 336 |
| 55 | Donchian 20/10 · 1h | breakout | 88.32 | -11.68 | 55 | 20.0 | -1.95 | -0.03 | -17.36 | 219 |
| 56 | OBV trend · 1h | momentum | 88.27 | -11.73 | 139 | 18.0 | -14.82 | -1.68 | -30.19 | 314 |
| 57 | VWAP momentum · 1h | momentum | 88.22 | -11.78 | 262 | 21.4 | -36.59 | -5.54 | -39.21 | 1266 |
| 58 | CCI reversion · 1h | reversion | 87.66 | -12.34 | 91 | 40.7 | -10.88 | -1.47 | -14.35 | 418 |
| 59 | Keltner breakout · 1h | breakout | 87.65 | -12.35 | 41 | 19.5 | -11.10 | -1.28 | -24.35 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 87.57 | -12.43 | 133 | 25.6 | -32.41 | -5.49 | -36.34 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.17 | -12.83 | 128 | 21.1 | -10.45 | -1.26 | -23.15 | 407 |
| 62 | Max aggression: 5-day momentum | meta | 83.59 | -16.41 | 7 | 28.6 | -27.10 | -2.40 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.28 | -23.72 | 354 | 21.5 | -72.70 | -16.37 | -73.75 | 1644 |
| 64 | RSI(14) reversion | reversion | 75.62 | -24.38 | 339 | 28.0 | -73.44 | -18.38 | -73.64 | 1501 |
| 65 | Squeeze breakout | breakout | 74.17 | -25.83 | 280 | 15.0 | -62.04 | -18.15 | -62.13 | 1205 |
| 66 | EMA 20/50 cross | trend | 72.46 | -27.54 | 289 | 18.7 | -77.31 | -15.27 | -77.50 | 1449 |
| 67 | Donchian 55/20 | breakout | 72.23 | -27.77 | 284 | 16.9 | -68.38 | -14.57 | -68.57 | 1279 |
| 68 | Volume breakout | breakout | 71.89 | -28.11 | 230 | 13.0 | -63.56 | -18.16 | -63.56 | 897 |
| 69 | VWAP reversion | reversion | 68.60 | -31.40 | 379 | 25.3 | -72.09 | -16.13 | -72.38 | 1440 |
| 70 | Supertrend | trend | 67.37 | -32.63 | 418 | 20.3 | -86.64 | -21.06 | -86.86 | 1925 |
| 71 | Keltner breakout | breakout | 65.23 | -34.77 | 392 | 13.8 | -84.48 | -27.96 | -84.48 | 1845 |
| 72 | Ichimoku | trend | 62.68 | -37.32 | 364 | 9.1 | -81.82 | -23.27 | -81.82 | 1733 |
| 73 | AI bee: Bizzy | ai | 62.40 | -37.60 | 721 | 8.9 | — | — | — | — |
| 74 | MFI reversion | reversion | 62.36 | -37.64 | 447 | 20.8 | -87.97 | -28.38 | -87.99 | 2125 |
| 75 | Z-score reversion | reversion | 62.11 | -37.89 | 462 | 23.6 | -86.03 | -23.45 | -86.10 | 2095 |
| 76 | ADX DI cross | trend | 60.60 | -39.40 | 496 | 10.5 | -89.62 | -34.21 | -89.63 | 2134 |
| 77 | MACD zero-line | trend | 59.80 | -40.20 | 520 | 16.0 | -91.28 | -28.85 | -91.28 | 2345 |
| 78 | AI bee: Boozy | ai | 59.45 | -40.55 | 245 | 5.3 | — | — | — | — |
| 79 | Donchian 20/10 | breakout | 59.43 | -40.57 | 557 | 18.3 | -90.96 | -25.94 | -90.97 | 2640 |
| 80 | Trend pullback | trend | 59.25 | -40.75 | 512 | 15.8 | -90.55 | -26.80 | -90.55 | 2288 |
| 81 | RSI momentum | momentum | 58.56 | -41.44 | 522 | 17.6 | -90.35 | -25.38 | -90.37 | 2347 |
| 82 | Triple EMA stack | trend | 57.60 | -42.40 | 553 | 15.4 | -93.14 | -30.03 | -93.15 | 2590 |
| 83 | Bollinger breakout | breakout | 55.22 | -44.77 | 584 | 14.7 | -93.65 | -32.87 | -93.65 | 2800 |
| 84 | Consensus | meta | 53.63 | -46.37 | 553 | 9.9 | -94.16 | -25.15 | -94.16 | 2651 |
| 85 | EMA 9/21 cross | trend | 52.04 | -47.96 | 707 | 16.3 | -97.32 | -32.46 | -97.32 | 3523 |
| 86 | Connors RSI(2) | reversion | 51.07 | -48.93 | 742 | 20.5 | -96.16 | -31.20 | -96.16 | 3554 |
| 87 | Stochastic reversion | reversion | 50.81 | -49.19 | 866 | 23.0 | -95.66 | -33.72 | -95.68 | 4068 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.70 | -30.16 | -98.71 | 5337 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.42 | -36.43 | -96.43 | 3572 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.34 | -35.88 | -99.34 | 5667 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -41.42 | -99.73 | 6136 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.06 | -97.37 | 3637 |
| 93 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.50 | -36.51 | -98.50 | 4703 |
| 94 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -39.25 | -99.52 | 6119 |
| 95 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.92 | -33.12 | -95.92 | 3731 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -45.96 | -99.90 | 8237 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-09T10:00 | Agent (ML meta-label) | buy | XRP-USD | 6.15 | — | entry |
| 2026-10-09T10:00 | Connors RSI(2) | buy | ETH-USD | 12.79 | — | entry signal |
| 2026-10-09T10:00 | Connors RSI(2) | sell | SOL-USD | 12.73 | -0.07 | exit signal |
| 2026-10-09T10:00 | Ichimoku | sell | ETH-USD | 15.61 | -0.12 | exit signal |
| 2026-10-09T09:55 | Consensus | buy | BTC-USD | 13.42 | — | entry |
| 2026-10-09T09:55 | Triple EMA stack | sell | SOL-USD | 14.33 | -0.11 | exit signal |
| 2026-10-09T09:55 | EMA 9/21 cross | sell | SOL-USD | 12.95 | -0.10 | exit signal |
| 2026-10-09T09:50 | Agent (ML meta-label) | sell | XRP-USD | 5.39 | -0.03 | selected signal exited |
| 2026-10-09T09:50 | MACD zero-line | sell | SOL-USD | 14.85 | -0.13 | exit signal |
| 2026-10-09T09:45 | Agent (ML meta-label) | buy | XRP-USD | 5.42 | — | entry |
| 2026-10-09T09:45 | Stochastic reversion | buy | XRP-USD | 12.71 | — | entry signal |
| 2026-10-09T09:45 | Connors RSI(2) | buy | SOL-USD | 12.80 | — | entry signal |
| 2026-10-09T09:45 | Connors RSI(2) | sell | XRP-USD | 12.74 | -0.08 | exit signal |
| 2026-10-09T09:45 | Ichimoku | sell | SOL-USD | 15.61 | -0.12 | exit signal |
| 2026-10-09T09:40 | AI bee: Bizzy | sell | DOGE-USD | 9.34 | -0.06 | Jev: sell (sell p=0.59) after 10 min |
| 2026-10-09T09:40 | Agent (ML meta-label) | sell | XRP-USD | 6.10 | -0.05 | selected signal exited |
| 2026-10-09T09:38 | AI bee: Bizzy | sell | ETH-USD | 8.82 | -0.06 | Jev: sell (sell p=0.51) after 13 min |
| 2026-10-09T09:35 | Trend pullback | sell | XRP-USD | 14.77 | -0.11 | exit signal |
| 2026-10-09T09:30 | AI bee: Bizzy | buy | DOGE-USD | 9.40 | — | Jev: buy (buy p=0.60) |
| 2026-10-09T09:30 | Ichimoku | buy | SOL-USD | 15.73 | — | entry signal |
| 2026-10-09T09:30 | Ichimoku | buy | ETH-USD | 15.73 | — | entry signal |
| 2026-10-09T09:25 | AI bee: Bizzy | buy | ETH-USD | 8.88 | — | Jev: buy (buy p=0.57) |
| 2026-10-09T09:25 | Agent (ML meta-label) | buy | XRP-USD | 6.15 | — | entry |
| 2026-10-09T09:25 | Z-score reversion | buy | DOGE-USD | 15.54 | — | entry signal |
| 2026-10-09T09:25 | Connors RSI(2) | sell | DOGE-USD | 12.76 | -0.07 | exit signal |
| 2026-10-09T09:25 | MACD zero-line | buy | SOL-USD | 14.98 | — | entry signal |
| 2026-10-09T09:20 | Connors RSI(2) | buy | XRP-USD | 12.82 | — | entry signal |
| 2026-10-09T09:20 | Triple EMA stack | buy | SOL-USD | 14.44 | — | entry signal |
| 2026-10-09T09:20 | Triple EMA stack | sell | XRP-USD | 11.58 | -0.03 | exit signal |
| 2026-10-09T09:20 | EMA 9/21 cross | buy | SOL-USD | 13.04 | — | entry signal |
| 2026-10-09T09:20 | EMA 9/21 cross | sell | XRP-USD | 10.43 | -0.04 | exit signal |
| 2026-10-09T09:15 | AI bee: Boozy | sell | ETH-USD | 15.55 | -0.11 | Jev: sell |
| 2026-10-09T09:15 | Stochastic reversion | buy | BTC-USD | 12.72 | — | entry signal |
| 2026-10-09T09:15 | EMA 20/50 cross | buy | SOL-USD | 3.83 | — | rebalance up |
| 2026-10-09T09:15 | EMA 20/50 cross | sell | DOGE-USD | 14.45 | 0.07 | exit signal |
| 2026-10-09T09:10 | AI bee: Bizzy | sell | SOL-USD | 9.09 | -0.08 | Jev: sell (sell p=0.76) after 11 min |
| 2026-10-09T09:10 | Agent (ML meta-label) | sell | XRP-USD | 4.74 | -0.03 | selected signal exited |
| 2026-10-09T09:05 | Connors RSI(2) | buy | DOGE-USD | 12.83 | — | entry signal |
| 2026-10-09T09:01 | ADX DI cross · 1h | buy | XRP-USD | 24.14 | — | entry signal |
| 2026-10-09T09:01 | RSI momentum | buy | ETH-USD | 14.66 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-11 10:00:05.000143+00:00 -> 2026-10-09 10:10:05.000143+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
