# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T04:00:05.000122+00:00 · 15160 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £96.64 (-3.36%)

Closed trades 42, win rate 57.1%, fees £1.87, max drawdown -3.97%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.44 | +0.07 |
| ETHU | 19.46 | +0.07 |

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

Today: 3120 decisions in 624 calls, $0.0438 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T04:00 | 0 / 2 / 3 | PLTR 15% |  |
| Breezy | 2026-10-08T04:00 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-08T04:00 | 0 / 5 / 0 | MSTR 69% |  |

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
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.70 | 5.70 | 0 | — | 1.14 | 0.35 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.53 | 2.53 | 34 | 41.2 | -9.31 | -2.91 | -13.84 | 118 |
| 3 | Timing: Nasdaq FTD · QQQ | daily | 102.18 | 2.17 | 0 | — | 0.87 | 0.55 | -5.09 | 1 |
| 4 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 5 | Copy: Congress Democrats (NANC) | copy | 101.58 | 1.58 | 0 | — | 2.17 | 1.06 | -3.62 | 1 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.76 | -4.03 | 18 |
| 7 | Hold SPY | benchmark | 101.28 | 1.28 | 0 | — | 0.54 | 0.37 | -3.66 | 1 |
| 8 | Donchian 55/20 · 1h | breakout | 101.10 | 1.10 | 18 | 5.6 | 11.49 | 1.57 | -16.96 | 109 |
| 9 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.64 | 0.64 | 4 | 50.0 | -4.52 | -1.54 | -9.74 | 24 |
| 10 | Copy: Warren Buffett (BRK-B) | copy | 100.61 | 0.61 | 0 | — | -2.78 | -1.11 | -7.65 | 1 |
| 11 | Day trade: Stocks in Play ORB | daytrade | 100.52 | 0.52 | 28 | 39.3 | 5.12 | 2.42 | -1.52 | 83 |
| 12 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.13 | 0.13 | 8 | 25.0 | 2.32 | 0.76 | -7.55 | 43 |
| 13 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 14 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 15 | Copy: Hedge-fund gurus (GURU) | copy | 99.85 | -0.15 | 0 | — | -4.16 | -2.02 | -5.14 | 1 |
| 16 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 17 | Hold BTC | benchmark | 99.05 | -0.95 | 0 | — | 28.45 | 3.41 | -8.68 | 1 |
| 18 | Daily: SMA 20/50 cross · AAPL | daily | 98.80 | -1.21 | 0 | — | -0.24 | -0.00 | -5.18 | 1 |
| 19 | Daily: Bullish score | daily | 98.48 | -1.52 | 3 | 0.0 | 3.08 | 0.60 | -12.76 | 10 |
| 20 | Trend pullback · 1h | trend | 98.48 | -1.52 | 68 | 23.5 | -20.89 | -5.98 | -23.40 | 176 |
| 21 | EMA 20/50 cross · 1h | trend | 98.41 | -1.59 | 34 | 5.9 | 7.46 | 1.02 | -19.45 | 134 |
| 22 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -2.57 | -2.02 | -3.95 | 25 |
| 23 | Stochastic reversion · 1h | reversion | 97.44 | -2.56 | 62 | 58.1 | -10.90 | -2.17 | -11.21 | 340 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 97.37 | -2.63 | 0 | — | 12.75 | 2.06 | -7.19 | 1 |
| 25 | Connors RSI(2) · 1h | reversion | 97.05 | -2.95 | 77 | 44.2 | -15.42 | -5.62 | -17.97 | 231 |
| 26 | Daily: Momentum burst | daily | 96.77 | -3.23 | 3 | 0.0 | -0.58 | 0.09 | -16.91 | 40 |
| 27 | RSI(14) reversion · 1h | reversion | 96.64 | -3.36 | 16 | 43.8 | 2.89 | 0.84 | -6.57 | 114 |
| 28 | Agent | meta | 96.64 | -3.36 | 42 | 57.1 | -9.91 | -5.39 | -10.29 | 255 |
| 29 | Agent (rotation) | meta | 96.50 | -3.50 | 74 | 27.0 | 1.49 | 0.50 | -10.39 | 277 |
| 30 | Copy: Insider buying | copy | 96.47 | -3.53 | 11 | 54.5 | -17.32 | -3.18 | -21.08 | 74 |
| 31 | Z-score reversion · 1h | reversion | 96.20 | -3.80 | 28 | 46.4 | 0.17 | 0.16 | -8.60 | 159 |
| 32 | Candlestick reversal · 1h | reversion | 95.78 | -4.22 | 85 | 32.9 | -26.40 | -6.00 | -26.56 | 481 |
| 33 | Supertrend · 1h | trend | 95.76 | -4.24 | 42 | 9.5 | -3.30 | -0.29 | -17.19 | 210 |
| 34 | Parabolic SAR · 1h | trend | 95.48 | -4.52 | 80 | 21.2 | -6.67 | -0.77 | -20.87 | 294 |
| 35 | ADX DI cross · 1h | trend | 95.17 | -4.83 | 47 | 14.9 | -6.22 | -0.86 | -13.84 | 250 |
| 36 | Bollinger reversion · 1h | reversion | 95.14 | -4.86 | 55 | 41.8 | -17.17 | -4.29 | -18.92 | 308 |
| 37 | Agent (aggressive) | meta | 95.07 | -4.93 | 20 | 50.0 | -2.95 | -1.20 | -6.03 | 115 |
| 38 | Max aggression: 1-day momentum | meta | 94.90 | -5.10 | 8 | 37.5 | -21.09 | -1.01 | -37.31 | 42 |
| 39 | Agent (ML meta-label) | meta | 94.89 | -5.11 | 289 | 15.6 | -1.03 | -0.04 | -12.99 | 365 |
| 40 | MACD cross · 1h | trend | 94.89 | -5.11 | 100 | 23.0 | -12.20 | -1.72 | -17.27 | 467 |
| 41 | Squeeze breakout · 1h | breakout | 94.74 | -5.26 | 34 | 26.5 | 15.15 | 2.52 | -8.12 | 101 |
| 42 | RSI momentum · 1h | momentum | 94.16 | -5.84 | 51 | 3.9 | -3.94 | -0.40 | -18.16 | 222 |
| 43 | Gap and go | momentum | 94.04 | -5.96 | 49 | 8.2 | 7.50 | 1.93 | -6.31 | 194 |
| 44 | Opening range 30m | breakout | 93.88 | -6.12 | 104 | 21.2 | -17.38 | -5.27 | -17.84 | 562 |
| 45 | Ichimoku · 1h | trend | 93.54 | -6.46 | 39 | 17.9 | -3.41 | -0.28 | -19.68 | 122 |
| 46 | Bollinger breakout · 1h | breakout | 93.53 | -6.47 | 63 | 30.2 | 7.63 | 1.13 | -12.06 | 290 |
| 47 | Triple EMA stack · 1h | trend | 93.20 | -6.80 | 61 | 11.5 | -8.73 | -0.88 | -24.26 | 242 |
| 48 | MFI reversion · 1h | reversion | 93.11 | -6.89 | 84 | 28.6 | -11.58 | -1.98 | -16.99 | 122 |
| 49 | Williams %R · 1h | reversion | 92.89 | -7.11 | 93 | 49.5 | -22.65 | -4.10 | -23.05 | 499 |
| 50 | Volume breakout · 1h | breakout | 92.74 | -7.26 | 44 | 15.9 | 6.49 | 1.05 | -12.60 | 121 |
| 51 | Opening range 15m | breakout | 92.20 | -7.80 | 121 | 19.8 | -19.15 | -5.55 | -19.54 | 679 |
| 52 | Donchian 20/10 · 1h | breakout | 91.16 | -8.84 | 50 | 20.0 | 2.36 | 0.49 | -16.18 | 220 |
| 53 | EMA 9/21 cross · 1h | trend | 91.15 | -8.85 | 90 | 11.1 | -4.63 | -0.42 | -18.86 | 340 |
| 54 | CCI reversion · 1h | reversion | 90.89 | -9.11 | 80 | 45.0 | -5.69 | -0.71 | -12.41 | 406 |
| 55 | MACD zero-line · 1h | trend | 90.55 | -9.46 | 57 | 19.3 | -4.96 | -0.47 | -19.00 | 237 |
| 56 | VWAP momentum · 1h | momentum | 90.38 | -9.62 | 243 | 22.6 | -36.86 | -5.63 | -37.98 | 1275 |
| 57 | Three white soldiers | momentum | 90.29 | -9.71 | 107 | 18.7 | -48.55 | -24.08 | -48.55 | 583 |
| 58 | OBV trend · 1h | momentum | 89.33 | -10.67 | 126 | 16.7 | -14.44 | -1.61 | -28.48 | 328 |
| 59 | Keltner breakout · 1h | breakout | 88.96 | -11.04 | 39 | 17.9 | -8.92 | -0.99 | -23.68 | 226 |
| 60 | Heikin-Ashi · 1h | trend | 88.72 | -11.28 | 126 | 24.6 | -31.97 | -5.45 | -35.62 | 691 |
| 61 | ROC + volume · 1h | momentum | 87.00 | -13.00 | 123 | 19.5 | -8.94 | -1.05 | -23.15 | 408 |
| 62 | Max aggression: 5-day momentum | meta | 85.74 | -14.26 | 7 | 28.6 | -23.93 | -2.09 | -31.79 | 30 |
| 63 | RSI(14) reversion | reversion | 80.74 | -19.26 | 270 | 31.1 | -71.95 | -18.72 | -71.97 | 1427 |
| 64 | ROC + volume | momentum | 76.17 | -23.82 | 327 | 20.2 | -73.40 | -17.09 | -73.60 | 1652 |
| 65 | Squeeze breakout | breakout | 75.78 | -24.22 | 264 | 14.8 | -62.09 | -18.33 | -62.12 | 1214 |
| 66 | Donchian 55/20 | breakout | 73.96 | -26.04 | 269 | 16.7 | -68.79 | -14.95 | -68.93 | 1293 |
| 67 | VWAP reversion | reversion | 73.18 | -26.82 | 321 | 27.4 | -69.97 | -15.80 | -70.19 | 1389 |
| 68 | EMA 20/50 cross | trend | 72.88 | -27.12 | 275 | 17.8 | -77.83 | -15.70 | -77.83 | 1462 |
| 69 | Volume breakout | breakout | 72.78 | -27.23 | 216 | 12.0 | -64.77 | -18.90 | -64.77 | 915 |
| 70 | Supertrend | trend | 68.61 | -31.39 | 374 | 19.3 | -86.75 | -21.42 | -86.79 | 1923 |
| 71 | MFI reversion | reversion | 66.31 | -33.69 | 406 | 21.7 | -87.46 | -29.21 | -87.47 | 2110 |
| 72 | Keltner breakout | breakout | 65.96 | -34.04 | 366 | 12.6 | -85.34 | -29.44 | -85.34 | 1879 |
| 73 | Z-score reversion | reversion | 65.93 | -34.07 | 409 | 24.7 | -85.29 | -23.93 | -85.29 | 2065 |
| 74 | Ichimoku | trend | 65.78 | -34.22 | 330 | 9.1 | -81.70 | -23.56 | -81.72 | 1733 |
| 75 | AI bee: Bizzy | ai | 65.02 | -34.98 | 653 | 8.4 | — | — | — | — |
| 76 | ADX DI cross | trend | 62.81 | -37.19 | 424 | 8.7 | -89.60 | -34.89 | -89.63 | 2108 |
| 77 | AI bee: Boozy | ai | 62.77 | -37.23 | 226 | 3.5 | — | — | — | — |
| 78 | MACD zero-line | trend | 61.61 | -38.39 | 478 | 14.9 | -91.35 | -29.43 | -91.35 | 2354 |
| 79 | Donchian 20/10 | breakout | 61.54 | -38.46 | 508 | 17.5 | -91.00 | -26.41 | -91.02 | 2662 |
| 80 | RSI momentum | momentum | 59.87 | -40.13 | 478 | 16.1 | -90.44 | -25.72 | -90.47 | 2370 |
| 81 | Trend pullback | trend | 59.85 | -40.15 | 495 | 15.4 | -91.11 | -28.54 | -91.12 | 2330 |
| 82 | Triple EMA stack | trend | 58.92 | -41.08 | 518 | 15.1 | -93.27 | -31.11 | -93.31 | 2618 |
| 83 | Bollinger breakout | breakout | 57.53 | -42.47 | 528 | 13.4 | -93.84 | -34.04 | -93.84 | 2830 |
| 84 | Consensus | meta | 55.97 | -44.03 | 507 | 9.9 | -94.48 | -25.93 | -94.48 | 2693 |
| 85 | EMA 9/21 cross | trend | 53.82 | -46.17 | 652 | 15.8 | -97.34 | -33.38 | -97.36 | 3528 |
| 86 | Stochastic reversion | reversion | 53.68 | -46.32 | 761 | 22.2 | -95.59 | -34.41 | -95.59 | 4034 |
| 87 | Bollinger reversion | reversion | 53.06 | -46.94 | 707 | 16.8 | -95.74 | -33.76 | -95.74 | 3693 |
| 88 | Connors RSI(2) | reversion | 52.95 | -47.05 | 697 | 19.9 | -96.40 | -32.67 | -96.40 | 3600 |
| 89 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.65 | -30.57 | -98.65 | 5331 |
| 90 | OBV trend | momentum | 50.48 | -49.52 | 755 | 14.4 | -96.42 | -37.48 | -96.42 | 3599 |
| 91 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.30 | -36.93 | -99.30 | 5584 |
| 92 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.28 | -99.73 | 6124 |
| 93 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.39 | -40.12 | -97.39 | 3664 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -37.60 | -98.46 | 4681 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.50 | -40.50 | -99.50 | 6091 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.57 | -99.90 | 8251 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T04:00 | Agent (ML meta-label) | sell | SOL-USD | 4.10 | -0.03 | selected signal exited |
| 2026-10-08T04:00 | Agent (ML meta-label) | sell | ETH-USD | 4.10 | -0.03 | selected signal exited |
| 2026-10-08T04:00 | Candlestick reversal · 1h | sell | XRP-USD | 15.88 | -0.20 | exit signal |
| 2026-10-08T04:00 | Candlestick reversal · 1h | sell | SOL-USD | 19.17 | -0.22 | exit signal |
| 2026-10-08T04:00 | Candlestick reversal · 1h | sell | ETH-USD | 15.99 | -0.14 | exit signal |
| 2026-10-08T04:00 | VWAP momentum · 1h | sell | XRP-USD | 4.97 | -0.06 | exit signal |
| 2026-10-08T04:00 | VWAP momentum · 1h | sell | SOL-USD | 4.97 | -0.06 | exit signal |
| 2026-10-08T04:00 | VWAP momentum · 1h | sell | ETH-USD | 4.97 | -0.06 | exit signal |
| 2026-10-08T04:00 | Heikin-Ashi · 1h | sell | XRP-USD | 9.77 | -0.11 | exit signal |
| 2026-10-08T04:00 | Heikin-Ashi · 1h | sell | SOL-USD | 10.99 | -0.13 | exit signal |
| 2026-10-08T03:55 | Agent (ML meta-label) | buy | SOL-USD | 4.13 | — | entry |
| 2026-10-08T03:55 | Agent (ML meta-label) | buy | ETH-USD | 4.13 | — | entry |
| 2026-10-08T03:55 | Candlestick reversal · 1h | sell | BTC-USD | 19.12 | -0.27 | stop-loss |
| 2026-10-08T03:50 | Connors RSI(2) | sell | DOGE-USD | 13.19 | -0.07 | exit signal |
| 2026-10-08T03:40 | Connors RSI(2) | buy | DOGE-USD | 13.25 | — | entry |
| 2026-10-08T03:30 | Z-score reversion | buy | BTC-USD | 16.53 | — | entry signal |
| 2026-10-08T03:30 | Connors RSI(2) | sell | ETH-USD | 13.21 | -0.10 | exit signal |
| 2026-10-08T03:30 | Connors RSI(2) | sell | DOGE-USD | 13.20 | -0.11 | exit signal |
| 2026-10-08T03:30 | EMA 20/50 cross | sell | ETH-USD | 17.82 | -0.09 | exit signal |
| 2026-10-08T03:25 | Z-score reversion | buy | SOL-USD | 16.57 | — | entry signal |
| 2026-10-08T03:25 | Z-score reversion | buy | ETH-USD | 16.57 | — | entry signal |
| 2026-10-08T03:25 | Z-score reversion | buy | DOGE-USD | 16.57 | — | entry signal |
| 2026-10-08T03:25 | Bollinger reversion | buy | XRP-USD | 10.67 | — | entry signal |
| 2026-10-08T03:25 | Bollinger reversion | buy | SOL-USD | 10.67 | — | entry signal |
| 2026-10-08T03:25 | Bollinger reversion | buy | ETH-USD | 10.67 | — | entry signal |
| 2026-10-08T03:25 | Bollinger reversion | buy | DOGE-USD | 10.67 | — | entry signal |
| 2026-10-08T03:25 | Bollinger reversion | buy | BTC-USD | 10.67 | — | entry signal |
| 2026-10-08T03:20 | Stochastic reversion | sell | DOGE-USD | 13.31 | -0.14 | target is flat |
| 2026-10-08T03:15 | MFI reversion | sell | BTC-USD | 16.47 | -0.16 | stop-loss |
| 2026-10-08T03:15 | Z-score reversion | sell | BTC-USD | 16.47 | -0.14 | stop-loss |
| 2026-10-08T03:15 | Donchian 20/10 | sell | XRP-USD | 11.30 | -0.09 | exit signal |
| 2026-10-08T03:15 | RSI momentum | sell | XRP-USD | 14.89 | -0.12 | exit signal |
| 2026-10-08T03:15 | Supertrend | sell | SOL-USD | 6.59 | -0.06 | exit signal |
| 2026-10-08T03:15 | EMA 9/21 cross | sell | XRP-USD | 10.38 | -0.09 | exit signal |
| 2026-10-08T03:12 | AI bee: Bizzy | sell | XRP-USD | 9.97 | -0.10 | Jev: sell (sell p=0.86) after 10 min |
| 2026-10-08T03:10 | Donchian 20/10 | buy | XRP-USD | 11.40 | — | entry |
| 2026-10-08T03:10 | Donchian 20/10 | sell | ETH-USD | 11.40 | -0.07 | exit signal |
| 2026-10-08T03:10 | OBV trend | sell | SOL-USD | 12.13 | -0.09 | stop-loss |
| 2026-10-08T03:10 | RSI momentum | buy | XRP-USD | 15.01 | — | entry |
| 2026-10-08T03:10 | RSI momentum | sell | SOL-USD | 14.93 | -0.11 | stop-loss |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 04:00:05.000122+00:00 -> 2026-10-08 04:10:05.000122+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
