# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T10:00:05.000117+00:00 · 15463 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.70 (-3.31%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.47 | +0.09 |
| ETHU | 19.48 | +0.10 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-07 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, BORR 12%, PSUS 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 7655 decisions in 1531 calls, $0.1074 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T10:00 | 1 / 3 / 1 | DOGE-USD 15%, PLTR 15% |  |
| Breezy | 2026-10-08T10:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T10:00 | 2 / 3 / 0 | MSTR 70% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |
| RSI(14) reversion | SOXL | 1.90 | +5.73% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.84 | 5.84 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.31 | 2.31 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.72 | 1.72 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Hold SPY | benchmark | 101.41 | 1.41 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 7 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 8 | Donchian 55/20 · 1h | breakout | 101.24 | 1.24 | 18 | 5.6 | 11.91 | 1.62 | -16.96 | 108 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.78 | 0.78 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.74 | 0.74 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.55 | 0.55 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.98 | -0.02 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Hold BTC | benchmark | 99.62 | -0.38 | 0 | — | 27.56 | 3.32 | -8.68 | 1 |
| 17 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.93 | -1.07 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.61 | -1.39 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.60 | -1.40 | 68 | 23.5 | -20.84 | -5.96 | -23.40 | 173 |
| 21 | EMA 20/50 cross · 1h | trend | 98.51 | -1.49 | 34 | 5.9 | 7.06 | 0.98 | -19.45 | 135 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.52 | -2.48 | 62 | 58.1 | -10.90 | -2.17 | -11.26 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.50 | -2.50 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.17 | -2.83 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.83 | -3.17 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | Agent | meta | 96.70 | -3.31 | 42 | 57.1 | -9.52 | -5.41 | -10.39 | 247 |
| 28 | Copy: Insider buying | copy | 96.60 | -3.40 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 30 | Supertrend · 1h | trend | 95.86 | -4.14 | 42 | 9.5 | -3.06 | -0.26 | -17.19 | 209 |
| 31 | RSI(14) reversion · 1h | reversion | 95.78 | -4.22 | 20 | 35.0 | 2.15 | 0.65 | -6.57 | 118 |
| 32 | Candlestick reversal · 1h | reversion | 95.60 | -4.40 | 86 | 32.6 | -26.57 | -6.04 | -26.83 | 484 |
| 33 | Parabolic SAR · 1h | trend | 95.55 | -4.46 | 80 | 21.2 | -6.92 | -0.81 | -20.87 | 294 |
| 34 | Z-score reversion · 1h | reversion | 95.42 | -4.58 | 32 | 40.6 | -0.75 | -0.03 | -8.60 | 159 |
| 35 | Bollinger reversion · 1h | reversion | 95.29 | -4.71 | 55 | 41.8 | -17.16 | -4.29 | -18.92 | 311 |
| 36 | ADX DI cross · 1h | trend | 95.27 | -4.73 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -0.97 | -0.38 | -6.03 | 109 |
| 38 | Max aggression: 1-day momentum | meta | 95.02 | -4.98 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.98 | -5.02 | 290 | 15.5 | 0.02 | 0.15 | -12.80 | 361 |
| 40 | MACD cross · 1h | trend | 94.97 | -5.03 | 101 | 22.8 | -12.22 | -1.72 | -17.27 | 466 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 14.79 | 2.46 | -8.12 | 102 |
| 42 | RSI momentum · 1h | momentum | 94.27 | -5.73 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 94.01 | -5.99 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.60 | -6.40 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.58 | -6.42 | 63 | 30.2 | 7.34 | 1.09 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.30 | -6.70 | 61 | 11.5 | -8.83 | -0.89 | -24.26 | 242 |
| 48 | Volume breakout · 1h | breakout | 92.77 | -7.23 | 44 | 15.9 | 6.50 | 1.05 | -12.60 | 121 |
| 49 | Williams %R · 1h | reversion | 92.53 | -7.47 | 96 | 47.9 | -23.19 | -4.22 | -23.35 | 499 |
| 50 | MFI reversion · 1h | reversion | 92.45 | -7.55 | 87 | 27.6 | -12.24 | -2.11 | -16.99 | 122 |
| 51 | Opening range 15m | breakout | 92.33 | -7.67 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.26 | -8.74 | 50 | 20.0 | 2.07 | 0.46 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.24 | -8.76 | 90 | 11.1 | -4.49 | -0.40 | -18.86 | 339 |
| 54 | CCI reversion · 1h | reversion | 90.82 | -9.18 | 82 | 43.9 | -6.24 | -0.79 | -12.41 | 408 |
| 55 | MACD zero-line · 1h | trend | 90.61 | -9.39 | 57 | 19.3 | -5.63 | -0.56 | -19.00 | 240 |
| 56 | VWAP momentum · 1h | momentum | 90.43 | -9.57 | 243 | 22.6 | -36.27 | -5.51 | -38.01 | 1273 |
| 57 | Three white soldiers | momentum | 90.14 | -9.86 | 108 | 18.5 | -48.57 | -24.17 | -48.57 | 583 |
| 58 | OBV trend · 1h | momentum | 89.36 | -10.64 | 126 | 16.7 | -13.84 | -1.54 | -28.48 | 325 |
| 59 | Keltner breakout · 1h | breakout | 88.99 | -11.01 | 39 | 17.9 | -9.27 | -1.04 | -23.68 | 225 |
| 60 | Heikin-Ashi · 1h | trend | 88.75 | -11.25 | 126 | 24.6 | -31.86 | -5.42 | -35.62 | 690 |
| 61 | ROC + volume · 1h | momentum | 87.09 | -12.91 | 123 | 19.5 | -8.94 | -1.05 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.82 | -19.18 | 272 | 30.9 | -72.26 | -19.00 | -72.36 | 1433 |
| 64 | ROC + volume | momentum | 75.83 | -24.17 | 329 | 20.1 | -73.27 | -17.04 | -73.62 | 1649 |
| 65 | Squeeze breakout | breakout | 75.49 | -24.51 | 265 | 14.7 | -62.06 | -18.26 | -62.16 | 1213 |
| 66 | Donchian 55/20 | breakout | 73.91 | -26.09 | 269 | 16.7 | -68.63 | -14.84 | -68.75 | 1289 |
| 67 | VWAP reversion | reversion | 72.83 | -27.17 | 326 | 27.9 | -70.36 | -16.08 | -70.51 | 1400 |
| 68 | Volume breakout | breakout | 72.80 | -27.20 | 216 | 12.0 | -64.34 | -18.85 | -64.34 | 907 |
| 69 | EMA 20/50 cross | trend | 72.78 | -27.22 | 276 | 17.8 | -78.05 | -15.83 | -78.07 | 1468 |
| 70 | Supertrend | trend | 68.56 | -31.44 | 376 | 19.1 | -86.93 | -21.67 | -86.99 | 1930 |
| 71 | MFI reversion | reversion | 66.17 | -33.83 | 410 | 21.5 | -87.53 | -29.44 | -87.55 | 2112 |
| 72 | Keltner breakout | breakout | 65.86 | -34.14 | 367 | 12.5 | -85.23 | -29.37 | -85.23 | 1872 |
| 73 | Ichimoku | trend | 65.23 | -34.77 | 334 | 9.0 | -81.71 | -23.61 | -81.76 | 1733 |
| 74 | Z-score reversion | reversion | 65.19 | -34.81 | 419 | 24.1 | -85.47 | -24.21 | -85.53 | 2071 |
| 75 | AI bee: Bizzy | ai | 64.34 | -35.66 | 663 | 8.3 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.35 | -37.65 | 430 | 8.6 | -89.74 | -35.65 | -89.74 | 2112 |
| 77 | AI bee: Boozy | ai | 62.26 | -37.74 | 230 | 3.5 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 61.45 | -38.55 | 510 | 17.5 | -91.13 | -26.71 | -91.14 | 2666 |
| 79 | MACD zero-line | trend | 60.88 | -39.12 | 485 | 14.6 | -91.52 | -29.93 | -91.52 | 2364 |
| 80 | Trend pullback | trend | 59.87 | -40.13 | 495 | 15.4 | -90.99 | -28.07 | -90.99 | 2322 |
| 81 | RSI momentum | momentum | 59.86 | -40.14 | 479 | 16.1 | -90.40 | -25.64 | -90.43 | 2366 |
| 82 | Triple EMA stack | trend | 59.00 | -41.00 | 518 | 15.1 | -93.30 | -31.26 | -93.31 | 2618 |
| 83 | Bollinger breakout | breakout | 57.14 | -42.86 | 533 | 13.3 | -93.86 | -34.37 | -93.86 | 2829 |
| 84 | Consensus | meta | 56.01 | -43.99 | 507 | 9.9 | -94.39 | -25.56 | -94.39 | 2684 |
| 85 | EMA 9/21 cross | trend | 53.60 | -46.40 | 656 | 15.7 | -97.39 | -33.84 | -97.39 | 3535 |
| 86 | Stochastic reversion | reversion | 53.07 | -46.93 | 773 | 22.0 | -95.62 | -34.78 | -95.62 | 4040 |
| 87 | Connors RSI(2) | reversion | 52.97 | -47.03 | 697 | 19.9 | -96.34 | -32.17 | -96.34 | 3589 |
| 88 | Bollinger reversion | reversion | 52.27 | -47.73 | 719 | 16.7 | -95.78 | -34.13 | -95.79 | 3695 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.69 | -31.00 | -98.69 | 5349 |
| 90 | OBV trend ⛔ | momentum | 50.34 | -49.66 | 757 | 14.4 | -96.39 | -37.41 | -96.40 | 3594 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.32 | -37.61 | -99.32 | 5598 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.71 | -99.73 | 6128 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.25 | -97.39 | 3662 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.48 | -37.96 | -98.48 | 4684 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -40.89 | -99.51 | 6097 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.87 | -99.90 | 8256 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T10:00 | VWAP momentum · 1h | buy | XRP-USD | 5.03 | — | entry signal |
| 2026-10-08T10:00 | VWAP momentum · 1h | buy | DOGE-USD | 5.03 | — | entry signal |
| 2026-10-08T10:00 | MACD zero-line | buy | SOL-USD | 6.42 | — | entry signal |
| 2026-10-08T09:55 | ROC + volume | buy | DOGE-USD | 18.97 | — | entry signal |
| 2026-10-08T09:55 | MACD zero-line | buy | ETH-USD | 15.24 | — | entry signal |
| 2026-10-08T09:52 | AI bee: Bizzy | buy | DOGE-USD | 9.60 | — | Jev: buy (buy p=0.60) |
| 2026-10-08T09:50 | Ichimoku | buy | BTC-USD | 16.31 | — | entry signal |
| 2026-10-08T09:46 | AI bee: Bizzy | sell | SOL-USD | 9.13 | -0.06 | Jev: sell (sell p=0.67) after 12 min |
| 2026-10-08T09:40 | Squeeze breakout | buy | XRP-USD | 18.89 | — | entry signal |
| 2026-10-08T09:35 | Stochastic reversion | sell | ETH-USD | 13.25 | -0.03 | exit signal |
| 2026-10-08T09:35 | Bollinger reversion | sell | ETH-USD | 13.04 | -0.03 | exit signal |
| 2026-10-08T09:35 | Squeeze breakout | buy | DOGE-USD | 18.90 | — | entry signal |
| 2026-10-08T09:35 | Bollinger breakout | buy | DOGE-USD | 1.95 | — | entry signal |
| 2026-10-08T09:35 | Donchian 55/20 | buy | XRP-USD | 18.43 | — | entry signal |
| 2026-10-08T09:35 | Donchian 55/20 | buy | DOGE-USD | 18.50 | — | entry signal |
| 2026-10-08T09:34 | AI bee: Bizzy | buy | SOL-USD | 9.19 | — | Jev: buy (buy p=0.57) |
| 2026-10-08T09:25 | Ichimoku | buy | DOGE-USD | 16.31 | — | entry |
| 2026-10-08T09:20 | Ichimoku | sell | DOGE-USD | 16.30 | -0.13 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | SOL-USD | 13.26 | -0.05 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | DOGE-USD | 13.25 | -0.03 | exit signal |
| 2026-10-08T09:05 | Stochastic reversion | sell | BTC-USD | 13.23 | -0.07 | exit signal |
| 2026-10-08T09:05 | Bollinger breakout | buy | XRP-USD | 14.29 | — | entry signal |
| 2026-10-08T09:00 | AI bee: Bizzy | sell | XRP-USD | 9.70 | -0.06 | Jev: sell (sell p=0.51) after 10 min |
| 2026-10-08T09:00 | Candlestick reversal · 1h | buy | SOL-USD | 4.86 | — | rebalance up |
| 2026-10-08T09:00 | Candlestick reversal · 1h | buy | ETH-USD | 4.83 | — | rebalance up |
| 2026-10-08T09:00 | Candlestick reversal · 1h | sell | BTC-USD | 19.10 | -0.05 | exit signal |
| 2026-10-08T08:52 | OBV trend | sell | XRP-USD | 11.93 | -0.07 | Kill switch: down 50% from peak |
| 2026-10-08T08:50 | AI bee: Bizzy | buy | XRP-USD | 9.76 | — | Jev: buy (buy p=0.61) |
| 2026-10-08T08:50 | OBV trend | buy | XRP-USD | 12.00 | — | entry signal |
| 2026-10-08T08:50 | EMA 20/50 cross | buy | XRP-USD | 17.63 | — | entry signal |
| 2026-10-08T08:45 | MFI reversion | buy | ETH-USD | 16.54 | — | entry signal |
| 2026-10-08T08:45 | Stochastic reversion | buy | DOGE-USD | 13.28 | — | entry signal |
| 2026-10-08T08:40 | Stochastic reversion | buy | ETH-USD | 13.28 | — | entry signal |
| 2026-10-08T08:40 | Bollinger reversion | buy | ETH-USD | 13.08 | — | entry signal |
| 2026-10-08T08:40 | MACD zero-line | sell | XRP-USD | 15.17 | -0.11 | exit signal |
| 2026-10-08T08:35 | Bollinger breakout | sell | XRP-USD | 2.02 | -0.01 | exit signal |
| 2026-10-08T08:35 | Bollinger breakout | sell | DOGE-USD | 14.23 | -0.11 | exit signal |
| 2026-10-08T08:35 | Donchian 20/10 | buy | DOGE-USD | 11.09 | — | entry |
| 2026-10-08T08:35 | Donchian 20/10 | sell | BTC-USD | 11.09 | -0.10 | exit signal |
| 2026-10-08T08:35 | OBV trend | sell | BTC-USD | 12.00 | -0.13 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 10:00:05.000117+00:00 -> 2026-10-08 10:10:05.000117+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
