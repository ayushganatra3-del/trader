# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-08T18:30:05.000151+00:00 · 15871 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.74 (-4.26%)

Closed trades 48, win rate 54.2%, fees £2.03, max drawdown -5.22%.

| Holding | Value £ | P/L £ |
|---|---:|---:|
| BITX | 19.14 | -0.01 |
| MSFT | 38.29 | -0.00 |
| TECL | 19.30 | +0.17 |

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-08 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, COE 12%, GME 12%, BPRE 12%, BORR 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-07)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.00 · VIX 15.08 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, BITX 7.0, MSTR 7.0, TECL 6.5, AMD 6.4

### AI bees (Jev: typesafe/jev-1.13)

Today: 32206 decisions in 2722 calls, $0.4004 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-08T18:30 | 1 / 24 / 5 | BITX 15%, COIN 14%, XRP-USD 14%, MSTR 15% |  |
| Breezy | 2026-10-08T18:30 | 0 / 26 / 4 | cash |  |
| Boozy | 2026-10-08T18:30 | 4 / 25 / 1 | BITX 55% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| VWAP reversion | TECL | 2.25 | +4.04% | 4 |
| VWAP reversion · 1h | DOGE-USD | 2.19 | +3.28% | 4 |
| Bollinger breakout | BITX | 2.13 | +1.63% | 6 |
| VWAP reversion | MSFT | 1.92 | +0.90% | 3 |
| Connors RSI(2) · 1h | MSFT | 1.92 | +1.43% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 102.65 | 2.65 | 35 | 40.0 | -8.35 | -2.58 | -13.79 | 118 |
| 2 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 101.73 | 1.73 | 0 | — | -1.57 | -0.58 | -7.65 | 1 |
| 4 | Timing: Nasdaq FTD · TQQQ | daily | 101.56 | 1.56 | 0 | — | -4.74 | -0.79 | -15.27 | 1 |
| 5 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.15 | 1.15 | 4 | 50.0 | 1.52 | 0.65 | -3.68 | 18 |
| 6 | Timing: Nasdaq FTD · QQQ | daily | 100.78 | 0.78 | 0 | — | -1.12 | -0.60 | -5.09 | 1 |
| 7 | Hold SPY | benchmark | 100.66 | 0.66 | 0 | — | 0.03 | 0.06 | -3.66 | 1 |
| 8 | Copy: Congress Democrats (NANC) | copy | 100.38 | 0.38 | 0 | — | 0.65 | 0.35 | -3.62 | 1 |
| 9 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 10 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 11 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.94 | -0.07 | 5 | 40.0 | -3.46 | -1.15 | -9.74 | 24 |
| 12 | Daily: SMA 20/50 cross · AAPL | daily | 99.57 | -0.42 | 0 | — | 0.84 | 0.40 | -5.18 | 1 |
| 13 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.47 | -0.53 | 9 | 22.2 | 3.05 | 0.98 | -7.55 | 43 |
| 14 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.26 | -1.33 | -2.90 | 20 |
| 15 | Day trade: Stocks in Play ORB | daytrade | 99.08 | -0.92 | 32 | 34.4 | 4.65 | 2.20 | -1.52 | 86 |
| 16 | Copy: Hedge-fund gurus (GURU) | copy | 98.66 | -1.34 | 0 | — | -5.19 | -2.48 | -5.49 | 1 |
| 17 | Copy: Insider buying | copy | 98.34 | -1.66 | 12 | 50.0 | -15.64 | -2.78 | -21.08 | 75 |
| 18 | Donchian 55/20 · 1h | breakout | 98.20 | -1.80 | 26 | 15.4 | 10.08 | 1.36 | -16.96 | 108 |
| 19 | Three white soldiers · 1h | momentum | 97.74 | -2.26 | 5 | 0.0 | -2.81 | -2.21 | -3.95 | 25 |
| 20 | Hold BTC | benchmark | 97.35 | -2.65 | 0 | — | 24.90 | 3.02 | -8.68 | 1 |
| 21 | Stochastic reversion · 1h | reversion | 97.17 | -2.83 | 76 | 50.0 | -13.29 | -2.67 | -15.16 | 344 |
| 22 | Trend pullback · 1h | trend | 96.48 | -3.52 | 78 | 23.1 | -23.83 | -6.79 | -25.54 | 172 |
| 23 | ADX DI cross · 1h | trend | 96.38 | -3.62 | 54 | 22.2 | -7.16 | -1.07 | -13.84 | 253 |
| 24 | EMA 20/50 cross · 1h | trend | 96.34 | -3.66 | 35 | 8.6 | -2.06 | -0.04 | -20.41 | 137 |
| 25 | Agent (rotation) | meta | 96.27 | -3.73 | 76 | 26.3 | 2.05 | 0.60 | -9.46 | 282 |
| 26 | Z-score reversion · 1h | reversion | 95.94 | -4.06 | 36 | 38.9 | -0.32 | 0.06 | -8.60 | 163 |
| 27 | Copy: Cathie Wood (ARKK) | copy | 95.87 | -4.13 | 0 | — | 9.86 | 1.65 | -8.33 | 1 |
| 28 | Daily: Momentum burst | daily | 95.78 | -4.22 | 4 | 0.0 | -4.20 | -0.48 | -17.67 | 40 |
| 29 | Agent | meta | 95.74 | -4.26 | 48 | 54.2 | -10.70 | -5.71 | -11.19 | 243 |
| 30 | MACD cross · 1h | trend | 95.15 | -4.85 | 105 | 22.9 | -14.92 | -2.26 | -17.27 | 460 |
| 31 | Daily: Bullish score | daily | 95.01 | -4.99 | 3 | 0.0 | -1.96 | -0.06 | -12.76 | 10 |
| 32 | Parabolic SAR · 1h | trend | 94.93 | -5.07 | 82 | 22.0 | -5.46 | -0.58 | -20.80 | 291 |
| 33 | Squeeze breakout · 1h | breakout | 94.85 | -5.15 | 34 | 26.5 | 15.15 | 2.50 | -8.14 | 103 |
| 34 | Agent (aggressive) | meta | 94.76 | -5.24 | 21 | 47.6 | -9.01 | -3.37 | -9.81 | 116 |
| 35 | Supertrend · 1h | trend | 94.18 | -5.82 | 51 | 13.7 | -3.86 | -0.36 | -18.09 | 212 |
| 36 | Gap and go | momentum | 93.81 | -6.19 | 50 | 8.0 | 7.32 | 1.89 | -6.56 | 194 |
| 37 | Connors RSI(2) · 1h | reversion | 93.57 | -6.43 | 100 | 41.0 | -18.32 | -6.13 | -21.10 | 252 |
| 38 | Ichimoku · 1h | trend | 93.08 | -6.92 | 41 | 19.5 | 0.08 | 0.21 | -19.98 | 119 |
| 39 | Agent (ML meta-label) | meta | 92.68 | -7.32 | 339 | 18.0 | -4.91 | -0.73 | -14.66 | 389 |
| 40 | RSI(14) reversion · 1h | reversion | 92.49 | -7.51 | 26 | 26.9 | -0.40 | 0.02 | -9.03 | 131 |
| 41 | Bollinger breakout · 1h | breakout | 92.48 | -7.52 | 65 | 30.8 | 5.31 | 0.85 | -12.06 | 289 |
| 42 | RSI momentum · 1h | momentum | 92.29 | -7.71 | 60 | 15.0 | -2.56 | -0.15 | -18.20 | 219 |
| 43 | Volume breakout · 1h | breakout | 91.97 | -8.03 | 45 | 17.8 | 5.53 | 0.92 | -12.60 | 123 |
| 44 | Bollinger reversion · 1h | reversion | 91.35 | -8.65 | 68 | 33.8 | -22.37 | -5.39 | -23.91 | 314 |
| 45 | Triple EMA stack · 1h | trend | 91.12 | -8.88 | 68 | 16.2 | -10.98 | -1.21 | -25.97 | 238 |
| 46 | MFI reversion · 1h | reversion | 91.04 | -8.96 | 92 | 26.1 | -15.64 | -2.70 | -17.07 | 127 |
| 47 | Max aggression: 1-day momentum | meta | 90.80 | -9.20 | 9 | 33.3 | -24.41 | -1.26 | -37.31 | 43 |
| 48 | Opening range 30m | breakout | 90.54 | -9.46 | 127 | 18.1 | -17.74 | -5.35 | -18.06 | 569 |
| 49 | Candlestick reversal · 1h ⏸ | reversion | 90.44 | -9.56 | 97 | 29.9 | -30.97 | -6.26 | -31.95 | 498 |
| 50 | Williams %R · 1h | reversion | 90.37 | -9.63 | 107 | 44.9 | -25.58 | -4.49 | -27.07 | 514 |
| 51 | MACD zero-line · 1h | trend | 90.27 | -9.73 | 58 | 20.7 | -6.10 | -0.65 | -19.00 | 239 |
| 52 | Three white soldiers | momentum | 89.40 | -10.61 | 114 | 19.3 | -48.80 | -24.33 | -48.80 | 588 |
| 53 | EMA 9/21 cross · 1h | trend | 88.58 | -11.42 | 99 | 14.1 | -9.61 | -1.10 | -20.61 | 333 |
| 54 | Opening range 15m | breakout | 88.37 | -11.63 | 149 | 16.8 | -19.59 | -5.63 | -19.90 | 689 |
| 55 | VWAP momentum · 1h | momentum | 88.34 | -11.66 | 262 | 21.4 | -36.47 | -5.59 | -39.09 | 1262 |
| 56 | Donchian 20/10 · 1h | breakout | 88.31 | -11.69 | 55 | 20.0 | -3.12 | -0.18 | -17.36 | 222 |
| 57 | OBV trend · 1h | momentum | 88.14 | -11.86 | 137 | 17.5 | -15.08 | -1.76 | -28.22 | 318 |
| 58 | Keltner breakout · 1h | breakout | 87.71 | -12.29 | 41 | 19.5 | -10.27 | -1.12 | -24.33 | 226 |
| 59 | Heikin-Ashi · 1h | trend | 87.66 | -12.34 | 133 | 25.6 | -33.09 | -5.69 | -36.15 | 687 |
| 60 | CCI reversion · 1h | reversion | 87.60 | -12.40 | 91 | 40.7 | -10.09 | -1.36 | -14.35 | 411 |
| 61 | ROC + volume · 1h | momentum | 87.10 | -12.90 | 128 | 21.1 | -10.60 | -1.29 | -23.15 | 409 |
| 62 | Max aggression: 5-day momentum | meta | 83.16 | -16.84 | 7 | 28.6 | -27.52 | -2.46 | -34.64 | 30 |
| 63 | ROC + volume | momentum | 76.50 | -23.50 | 338 | 20.4 | -72.81 | -16.64 | -73.83 | 1635 |
| 64 | RSI(14) reversion ⏸ | reversion | 75.63 | -24.37 | 338 | 28.1 | -73.53 | -18.77 | -73.86 | 1503 |
| 65 | Squeeze breakout | breakout | 74.47 | -25.52 | 273 | 14.7 | -62.35 | -18.55 | -62.38 | 1210 |
| 66 | Donchian 55/20 | breakout | 72.74 | -27.25 | 274 | 16.8 | -68.33 | -14.76 | -68.46 | 1277 |
| 67 | Volume breakout | breakout | 72.67 | -27.33 | 221 | 12.2 | -63.51 | -18.26 | -63.69 | 899 |
| 68 | EMA 20/50 cross | trend | 72.20 | -27.80 | 283 | 18.0 | -77.74 | -15.63 | -77.92 | 1455 |
| 69 | VWAP reversion ⏸ | reversion | 68.88 | -31.12 | 376 | 25.5 | -71.83 | -16.19 | -72.16 | 1441 |
| 70 | Supertrend | trend | 67.10 | -32.90 | 403 | 18.6 | -86.96 | -21.50 | -87.20 | 1935 |
| 71 | Keltner breakout | breakout | 66.15 | -33.85 | 373 | 13.1 | -84.81 | -28.28 | -84.95 | 1862 |
| 72 | Ichimoku | trend | 64.47 | -35.53 | 344 | 9.0 | -81.59 | -23.37 | -81.72 | 1727 |
| 73 | AI bee: Bizzy | ai | 64.46 | -35.54 | 682 | 9.1 | — | — | — | — |
| 74 | MFI reversion ⏸ | reversion | 62.56 | -37.44 | 446 | 20.9 | -88.04 | -29.40 | -88.19 | 2134 |
| 75 | Z-score reversion ⏸ | reversion | 62.25 | -37.75 | 459 | 23.7 | -86.04 | -23.97 | -86.19 | 2102 |
| 76 | ADX DI cross | trend | 61.72 | -38.28 | 462 | 8.9 | -89.60 | -34.89 | -89.80 | 2131 |
| 77 | AI bee: Boozy | ai | 60.84 | -39.16 | 237 | 5.1 | — | — | — | — |
| 78 | Donchian 20/10 | breakout | 60.59 | -39.41 | 530 | 17.9 | -90.94 | -26.26 | -91.07 | 2641 |
| 79 | MACD zero-line | trend | 60.36 | -39.64 | 501 | 14.8 | -91.46 | -29.76 | -91.54 | 2346 |
| 80 | Trend pullback | trend | 59.61 | -40.39 | 505 | 15.4 | -90.70 | -27.81 | -90.74 | 2301 |
| 81 | RSI momentum | momentum | 59.15 | -40.85 | 498 | 16.5 | -90.30 | -25.59 | -90.42 | 2344 |
| 82 | Triple EMA stack | trend | 59.01 | -40.99 | 527 | 15.4 | -93.17 | -30.65 | -93.23 | 2597 |
| 83 | Consensus | meta | 56.52 | -43.48 | 514 | 10.3 | -94.27 | -25.68 | -94.28 | 2672 |
| 84 | Bollinger breakout | breakout | 56.43 | -43.57 | 555 | 13.7 | -93.72 | -33.56 | -93.80 | 2812 |
| 85 | EMA 9/21 cross | trend | 52.81 | -47.19 | 681 | 15.7 | -97.39 | -33.27 | -97.42 | 3520 |
| 86 | Connors RSI(2) | reversion | 52.68 | -47.32 | 715 | 21.0 | -96.27 | -32.33 | -96.27 | 3572 |
| 87 | Stochastic reversion | reversion | 51.15 | -48.85 | 851 | 22.7 | -95.75 | -35.15 | -95.79 | 4078 |
| 88 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -30.76 | -98.69 | 5325 |
| 89 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.34 | -36.55 | -96.36 | 3558 |
| 90 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.36 | -37.51 | -99.37 | 5699 |
| 91 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.11 | -99.74 | 6153 |
| 92 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.34 | -39.22 | -97.35 | 3631 |
| 93 | Bollinger reversion ⏸ | reversion | 50.09 | -49.91 | 772 | 17.5 | -95.93 | -34.13 | -95.95 | 3741 |
| 94 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.52 | -37.91 | -98.53 | 4712 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.53 | -40.99 | -99.53 | 6124 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -47.59 | -99.90 | 8241 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-08T18:30 | AI bee: Bizzy | buy | MSTR | 9.36 | — | Jev: buy (buy p=0.58) |
| 2026-10-08T18:30 | AI bee: Bizzy | sell | TECL | 9.28 | 0.03 | Jev: sell |
| 2026-10-08T18:30 | Agent (ML meta-label) | buy | IWM | 2.25 | — | entry |
| 2026-10-08T18:30 | Agent (ML meta-label) | buy | COIN | 5.57 | — | entry |
| 2026-10-08T18:30 | Agent (ML meta-label) | buy | BITX | 5.57 | — | following Bollinger breakout |
| 2026-10-08T18:30 | Agent (ML meta-label) | buy | AMD | 5.57 | — | entry |
| 2026-10-08T18:30 | Agent (ML meta-label) | sell | MSTR | 4.83 | 0.05 | rebalance down |
| 2026-10-08T18:30 | Agent (ML meta-label) | sell | ETH-USD | 9.21 | -0.06 | selected signal exited |
| 2026-10-08T18:30 | Consensus | buy | IWM | 5.79 | — | entry |
| 2026-10-08T18:30 | Consensus | sell | SQQQ | 2.89 | 0.01 | rebalance down |
| 2026-10-08T18:30 | Consensus | sell | AAPL | 2.90 | 0.01 | rebalance down |
| 2026-10-08T18:30 | MFI reversion · 1h | buy | COIN | 22.38 | — | entry signal |
| 2026-10-08T18:30 | CCI reversion · 1h | buy | MSTR | 11.51 | — | entry signal |
| 2026-10-08T18:30 | CCI reversion · 1h | buy | LABU | 14.61 | — | entry signal |
| 2026-10-08T18:30 | CCI reversion · 1h | buy | COIN | 14.61 | — | entry signal |
| 2026-10-08T18:30 | CCI reversion · 1h | sell | TNA | 7.34 | 0.03 | rebalance down |
| 2026-10-08T18:30 | CCI reversion · 1h | sell | IWM | 7.25 | -0.00 | rebalance down |
| 2026-10-08T18:30 | Williams %R · 1h | buy | UPRO | 6.93 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | TSLA | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | TQQQ | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | TECL | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | SPY | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | SOXL | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | QQQ | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | MSFT | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | buy | META | 6.96 | — | entry signal |
| 2026-10-08T18:30 | Williams %R · 1h | sell | TNA | 15.61 | 0.06 | rebalance down |
| 2026-10-08T18:30 | Williams %R · 1h | sell | LABU | 15.79 | 0.19 | rebalance down |
| 2026-10-08T18:30 | Williams %R · 1h | sell | IWM | 15.52 | -0.00 | rebalance down |
| 2026-10-08T18:30 | Williams %R · 1h | sell | COIN | 15.65 | -0.19 | rebalance down |
| 2026-10-08T18:30 | Z-score reversion · 1h | buy | SOXL | 10.00 | — | entry signal |
| 2026-10-08T18:30 | Z-score reversion · 1h | buy | META | 19.19 | — | entry signal |
| 2026-10-08T18:30 | Z-score reversion · 1h | sell | LABU | 4.99 | 0.06 | rebalance down |
| 2026-10-08T18:30 | Bollinger reversion · 1h | buy | UPRO | 8.31 | — | entry signal |
| 2026-10-08T18:30 | Bollinger reversion · 1h | buy | TQQQ | 9.14 | — | entry signal |
| 2026-10-08T18:30 | Bollinger reversion · 1h | buy | SPY | 9.14 | — | entry signal |
| 2026-10-08T18:30 | Bollinger reversion · 1h | buy | SOXL | 9.14 | — | entry signal |
| 2026-10-08T18:30 | Bollinger reversion · 1h | buy | QQQ | 9.14 | — | entry signal |
| 2026-10-08T18:30 | Bollinger reversion · 1h | sell | TSLA | 13.18 | -0.08 | rebalance down |
| 2026-10-08T18:30 | Bollinger reversion · 1h | sell | META | 9.04 | -0.04 | rebalance down |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-10 18:30:05.000151+00:00 -> 2026-10-08 18:40:05.000151+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
