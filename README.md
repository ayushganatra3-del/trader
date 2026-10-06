# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-06T20:57:05.000170+00:00 · 13851 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £98.29 (-1.71%)

Closed trades 37, win rate 62.2%, fees £1.28, max drawdown -2.16%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-06 | SLBT 12%, KOD 12%, ADRX 12%, BBD 12%, GME 12%, BPRE 12%, PAM 12%, BORR 12% | Refresh failed: OpenInsider unreachable: GET https://openinsider.com/screener: <urlopen error [Errno 111] Connection refused> | GET http://openinsider.com/screener: <urlopen error timed out> |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-06)

**Uptrend** since 2026-09-21 · level normal · 1 distribution days in 25 sessions · timing exposure 100% · VXN 21.09 · VIX 15.13 · last follow-through day 2026-08-04

Best bullish scores: PLTR 9.0, MSFT 8.9, MSTR 7.5, AMD 7.3, BITX 7.0, ETHU 7.0

### AI bees (Jev: typesafe/jev-1.13)

Today: 36739 decisions in 2945 calls, $0.4539 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-06T20:57 | 0 / 3 / 2 | cash |  |
| Breezy | 2026-10-06T20:57 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-06T20:57 | 2 / 2 / 1 | MSTR 69% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Stochastic reversion · 1h | DOGE-USD | 3.08 | +5.12% | 5 |
| Bollinger breakout | BITX | 1.97 | +1.54% | 5 |
| VWAP reversion · 1h | DOGE-USD | 1.89 | +3.24% | 5 |
| Volume breakout | LABU | 1.81 | +2.37% | 3 |
| EMA 20/50 cross | LABU | 1.79 | +4.63% | 4 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Timing: Nasdaq FTD · TQQQ | daily | 105.99 | 5.99 | 0 | — | 0.74 | 0.28 | -15.27 | 1 |
| 2 | VWAP reversion · 1h | reversion | 102.76 | 2.76 | 30 | 46.7 | -8.81 | -2.78 | -13.79 | 113 |
| 3 | Hold BTC | benchmark | 102.06 | 2.06 | 0 | — | 31.99 | 3.87 | -8.68 | 1 |
| 4 | Timing: Nasdaq FTD · QQQ | daily | 101.94 | 1.94 | 0 | — | 0.76 | 0.49 | -5.09 | 1 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.73 | -7.93 | 7 |
| 6 | Copy: Congress Democrats (NANC) | copy | 101.60 | 1.60 | 0 | — | 3.37 | 1.61 | -3.62 | 1 |
| 7 | Donchian 55/20 · 1h | breakout | 101.40 | 1.40 | 17 | 0.0 | 12.58 | 1.72 | -16.96 | 110 |
| 8 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.33 | 1.33 | 4 | 50.0 | 1.82 | 0.77 | -4.03 | 18 |
| 9 | Daily: Bullish score | daily | 101.31 | 1.31 | 3 | 0.0 | 5.96 | 0.99 | -12.76 | 10 |
| 10 | Hold SPY | benchmark | 101.05 | 1.05 | 0 | — | 1.03 | 0.67 | -3.66 | 1 |
| 11 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 100.98 | 0.98 | 7 | 28.6 | 5.08 | 1.54 | -7.55 | 43 |
| 12 | Candlestick reversal · 1h | reversion | 100.32 | 0.33 | 68 | 38.2 | -21.59 | -4.94 | -23.37 | 489 |
| 13 | Day trade: Stocks in Play ORB | daytrade | 100.09 | 0.09 | 26 | 34.6 | 3.95 | 1.91 | -1.59 | 84 |
| 14 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 15 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 16 | Copy: Warren Buffett (BRK-B) | copy | 100.00 | -0.00 | 0 | — | -2.39 | -0.91 | -7.65 | 1 |
| 17 | Stochastic reversion · 1h | reversion | 99.98 | -0.02 | 56 | 64.3 | -7.96 | -1.63 | -10.88 | 325 |
| 18 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 99.95 | -0.05 | 4 | 50.0 | -4.04 | -1.39 | -9.74 | 23 |
| 19 | Copy: Hedge-fund gurus (GURU) | copy | 99.92 | -0.08 | 0 | — | -3.80 | -1.86 | -5.14 | 1 |
| 20 | EMA 20/50 cross · 1h | trend | 99.87 | -0.13 | 29 | 6.9 | 7.91 | 1.16 | -17.11 | 140 |
| 21 | RSI(14) reversion · 1h | reversion | 99.53 | -0.47 | 12 | 58.3 | 3.14 | 0.93 | -6.57 | 123 |
| 22 | Connors RSI(2) · 1h | reversion | 99.43 | -0.57 | 73 | 45.2 | -10.99 | -3.98 | -14.77 | 218 |
| 23 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.41 | -0.59 | 5 | 40.0 | -1.37 | -1.47 | -2.90 | 21 |
| 24 | Copy: Cathie Wood (ARKK) | copy | 99.21 | -0.79 | 0 | — | 18.30 | 2.78 | -6.29 | 1 |
| 25 | Trend pullback · 1h | trend | 98.82 | -1.18 | 66 | 24.2 | -20.71 | -6.10 | -24.41 | 166 |
| 26 | Agent (aggressive) | meta | 98.46 | -1.54 | 16 | 56.2 | -0.17 | -0.04 | -4.23 | 102 |
| 27 | Daily: Momentum burst | daily | 98.37 | -1.63 | 3 | 0.0 | 1.48 | 0.40 | -16.91 | 41 |
| 28 | Three white soldiers · 1h | momentum | 98.30 | -1.70 | 4 | 0.0 | -3.00 | -2.38 | -3.95 | 25 |
| 29 | Agent | meta | 98.29 | -1.71 | 37 | 62.2 | -7.71 | -4.92 | -9.35 | 222 |
| 30 | Z-score reversion · 1h | reversion | 98.26 | -1.74 | 23 | 52.2 | 3.80 | 0.92 | -8.60 | 151 |
| 31 | Copy: Insider buying | copy | 97.92 | -2.08 | 11 | 54.5 | -15.61 | -2.88 | -21.08 | 73 |
| 32 | Bollinger reversion · 1h | reversion | 97.92 | -2.08 | 49 | 46.9 | -15.16 | -3.78 | -17.03 | 301 |
| 33 | Daily: SMA 20/50 cross · AAPL | daily | 97.45 | -2.55 | 0 | — | -0.63 | -0.16 | -5.18 | 1 |
| 34 | Agent (rotation) | meta | 97.19 | -2.81 | 63 | 28.6 | -1.12 | -0.21 | -10.40 | 270 |
| 35 | ADX DI cross · 1h | trend | 96.76 | -3.24 | 43 | 11.6 | -2.94 | -0.37 | -13.84 | 256 |
| 36 | Supertrend · 1h | trend | 96.70 | -3.30 | 33 | 9.1 | 1.69 | 0.42 | -16.43 | 212 |
| 37 | Agent (ML meta-label) | meta | 96.58 | -3.42 | 265 | 14.7 | 5.52 | 1.13 | -13.16 | 379 |
| 38 | Williams %R · 1h | reversion | 96.37 | -3.62 | 85 | 52.9 | -20.19 | -3.79 | -20.57 | 495 |
| 39 | Parabolic SAR · 1h | trend | 96.35 | -3.65 | 65 | 15.4 | -4.28 | -0.39 | -19.45 | 300 |
| 40 | CCI reversion · 1h | reversion | 96.24 | -3.76 | 71 | 49.3 | 0.55 | 0.25 | -12.41 | 406 |
| 41 | MACD cross · 1h | trend | 95.64 | -4.36 | 90 | 20.0 | -13.77 | -2.23 | -17.27 | 469 |
| 42 | RSI momentum · 1h | momentum | 95.35 | -4.65 | 45 | 2.2 | 0.03 | 0.20 | -16.65 | 228 |
| 43 | MFI reversion · 1h | reversion | 95.05 | -4.95 | 75 | 28.0 | -10.55 | -1.84 | -16.99 | 121 |
| 44 | Squeeze breakout · 1h | breakout | 94.99 | -5.01 | 30 | 20.0 | 15.23 | 2.56 | -8.06 | 107 |
| 45 | Max aggression: 1-day momentum | meta | 94.92 | -5.08 | 7 | 42.9 | -23.54 | -1.22 | -37.31 | 42 |
| 46 | Ichimoku · 1h | trend | 94.83 | -5.17 | 34 | 14.7 | 2.45 | 0.51 | -16.99 | 125 |
| 47 | Triple EMA stack · 1h | trend | 94.48 | -5.52 | 57 | 10.5 | -9.19 | -0.89 | -24.82 | 253 |
| 48 | Bollinger breakout · 1h | breakout | 94.46 | -5.54 | 51 | 23.5 | 7.53 | 1.13 | -12.06 | 295 |
| 49 | Gap and go | momentum | 94.27 | -5.73 | 47 | 8.5 | 6.64 | 1.74 | -6.49 | 199 |
| 50 | Opening range 30m | breakout | 93.72 | -6.28 | 102 | 21.6 | -17.53 | -5.43 | -17.86 | 567 |
| 51 | Volume breakout · 1h | breakout | 93.55 | -6.45 | 36 | 11.1 | 6.28 | 1.03 | -12.60 | 131 |
| 52 | EMA 9/21 cross · 1h | trend | 92.57 | -7.43 | 83 | 10.8 | -3.17 | -0.23 | -18.47 | 348 |
| 53 | Opening range 15m | breakout | 92.26 | -7.74 | 118 | 20.3 | -18.95 | -5.62 | -19.29 | 686 |
| 54 | Max aggression: 5-day momentum | meta | 91.28 | -8.72 | 5 | 40.0 | -19.91 | -1.72 | -29.56 | 29 |
| 55 | MACD zero-line · 1h | trend | 91.24 | -8.76 | 50 | 18.0 | -4.54 | -0.41 | -18.32 | 244 |
| 56 | Donchian 20/10 · 1h | breakout | 91.21 | -8.79 | 42 | 14.3 | 2.44 | 0.51 | -16.18 | 223 |
| 57 | Three white soldiers | momentum | 90.94 | -9.06 | 102 | 19.6 | -49.33 | -24.88 | -49.53 | 589 |
| 58 | VWAP momentum · 1h | momentum | 90.64 | -9.36 | 229 | 22.7 | -37.09 | -5.71 | -37.12 | 1268 |
| 59 | OBV trend · 1h | momentum | 90.40 | -9.60 | 109 | 11.9 | -12.68 | -1.42 | -26.73 | 332 |
| 60 | Heikin-Ashi · 1h | trend | 89.90 | -10.10 | 116 | 25.0 | -31.15 | -5.36 | -34.37 | 687 |
| 61 | Keltner breakout · 1h | breakout | 89.62 | -10.38 | 30 | 6.7 | -10.65 | -1.24 | -23.31 | 227 |
| 62 | ROC + volume · 1h | momentum | 87.24 | -12.76 | 112 | 16.1 | -9.52 | -1.15 | -23.04 | 412 |
| 63 | RSI(14) reversion | reversion | 85.53 | -14.47 | 225 | 32.0 | -71.88 | -19.69 | -72.18 | 1427 |
| 64 | Squeeze breakout | breakout | 77.44 | -22.57 | 251 | 15.5 | -62.40 | -18.99 | -62.42 | 1224 |
| 65 | VWAP reversion | reversion | 77.20 | -22.80 | 278 | 28.4 | -68.98 | -16.19 | -69.13 | 1385 |
| 66 | ROC + volume | momentum | 76.75 | -23.25 | 319 | 20.7 | -73.79 | -17.78 | -73.79 | 1643 |
| 67 | Donchian 55/20 | breakout | 76.05 | -23.95 | 259 | 17.4 | -68.90 | -15.33 | -68.91 | 1304 |
| 68 | EMA 20/50 cross | trend | 74.36 | -25.64 | 266 | 18.4 | -78.48 | -16.24 | -78.49 | 1476 |
| 69 | Volume breakout | breakout | 73.43 | -26.57 | 211 | 12.3 | -65.12 | -19.59 | -65.12 | 918 |
| 70 | Z-score reversion | reversion | 71.03 | -28.97 | 357 | 27.5 | -85.11 | -25.35 | -85.11 | 2044 |
| 71 | MFI reversion | reversion | 69.81 | -30.19 | 357 | 21.0 | -87.21 | -30.93 | -87.22 | 2101 |
| 72 | Supertrend | trend | 69.26 | -30.74 | 360 | 20.0 | -87.19 | -22.48 | -87.20 | 1927 |
| 73 | Keltner breakout | breakout | 67.94 | -32.06 | 350 | 13.1 | -85.48 | -30.55 | -85.49 | 1884 |
| 74 | AI bee: Bizzy | ai | 67.39 | -32.61 | 610 | 8.9 | — | — | — | — |
| 75 | Ichimoku | trend | 66.78 | -33.22 | 320 | 9.1 | -82.20 | -24.91 | -82.20 | 1767 |
| 76 | AI bee: Boozy | ai | 66.11 | -33.89 | 218 | 3.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 64.26 | -35.74 | 403 | 9.2 | -89.71 | -37.26 | -89.72 | 2103 |
| 78 | MACD zero-line | trend | 62.99 | -37.01 | 454 | 15.4 | -91.56 | -31.23 | -91.56 | 2365 |
| 79 | Donchian 20/10 | breakout | 62.42 | -37.58 | 493 | 18.1 | -91.15 | -27.73 | -91.15 | 2668 |
| 80 | RSI momentum | momentum | 61.51 | -38.49 | 458 | 16.8 | -90.68 | -27.02 | -90.69 | 2382 |
| 81 | Triple EMA stack | trend | 60.00 | -40.00 | 510 | 15.3 | -93.37 | -32.70 | -93.38 | 2630 |
| 82 | Trend pullback | trend | 60.00 | -40.00 | 492 | 15.4 | -91.45 | -30.70 | -91.45 | 2347 |
| 83 | Bollinger breakout | breakout | 59.21 | -40.79 | 501 | 14.0 | -94.00 | -35.83 | -94.00 | 2822 |
| 84 | Stochastic reversion | reversion | 57.90 | -42.10 | 722 | 23.3 | -95.53 | -37.27 | -95.53 | 4038 |
| 85 | Bollinger reversion | reversion | 57.48 | -42.52 | 664 | 17.9 | -95.66 | -36.41 | -95.66 | 3674 |
| 86 | Consensus | meta | 57.11 | -42.90 | 490 | 10.0 | -94.66 | -27.35 | -94.66 | 2721 |
| 87 | EMA 9/21 cross | trend | 55.35 | -44.65 | 628 | 16.4 | -97.43 | -35.61 | -97.43 | 3550 |
| 88 | Connors RSI(2) | reversion | 53.79 | -46.21 | 679 | 20.2 | -96.57 | -35.37 | -96.57 | 3638 |
| 89 | OBV trend | momentum | 52.01 | -47.99 | 740 | 14.7 | -96.48 | -40.05 | -96.48 | 3604 |
| 90 | CCI reversion | reversion | 51.84 | -48.16 | 699 | 17.3 | -98.45 | -40.66 | -98.45 | 4688 |
| 91 | Candlestick reversal ⏸ | reversion | 50.65 | -49.35 | 803 | 14.9 | -99.30 | -39.84 | -99.30 | 5622 |
| 92 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.72 | -32.23 | -98.72 | 5358 |
| 93 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.72 | -46.87 | -99.72 | 6125 |
| 94 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.40 | -42.50 | -97.40 | 3681 |
| 95 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.51 | -44.38 | -99.51 | 6093 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -52.73 | -99.90 | 8240 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-06T20:49 | AI bee: Boozy | sell | ETH-USD | 20.42 | -0.11 | Jev: add (buy p=0.53) |
| 2026-10-06T20:40 | Stochastic reversion | sell | BTC-USD | 11.60 | -0.05 | exit signal |
| 2026-10-06T20:40 | Bollinger breakout | buy | ETH-USD | 14.81 | — | entry signal |
| 2026-10-06T20:40 | RSI momentum | buy | ETH-USD | 15.39 | — | entry signal |
| 2026-10-06T20:40 | MACD zero-line | buy | ETH-USD | 15.78 | — | entry signal |
| 2026-10-06T20:40 | MACD zero-line | buy | BTC-USD | 15.78 | — | entry signal |
| 2026-10-06T20:35 | Donchian 20/10 | buy | ETH-USD | 15.61 | — | entry signal |
| 2026-10-06T20:34 | AI bee: Boozy | buy | ETH-USD | 20.53 | — | Jev: buy (buy p=0.71) |
| 2026-10-06T20:33 | AI bee: Bizzy | sell | SOL-USD | 9.70 | -0.07 | Jev: sell (sell p=0.73) after 11 min |
| 2026-10-06T20:31 | AI bee: Bizzy | sell | XRP-USD | 9.50 | -0.06 | Jev: sell (sell p=0.70) after 11 min |
| 2026-10-06T20:31 | MFI reversion | sell | ETH-USD | 17.45 | -0.07 | exit signal |
| 2026-10-06T20:31 | RSI(14) reversion | sell | ETH-USD | 21.36 | -0.06 | exit signal |
| 2026-10-06T20:31 | Supertrend | buy | ETH-USD | 17.33 | — | entry signal |
| 2026-10-06T20:31 | MACD zero-line | buy | XRP-USD | 15.79 | — | entry signal |
| 2026-10-06T20:25 | CCI reversion | sell | XRP-USD | 12.96 | -0.04 | exit signal |
| 2026-10-06T20:25 | CCI reversion | sell | ETH-USD | 10.38 | -0.04 | exit signal |
| 2026-10-06T20:25 | Bollinger reversion | sell | DOGE-USD | 14.38 | -0.05 | exit signal |
| 2026-10-06T20:25 | Bollinger breakout | buy | SOL-USD | 14.83 | — | entry signal |
| 2026-10-06T20:25 | Donchian 20/10 | buy | SOL-USD | 15.63 | — | entry signal |
| 2026-10-06T20:25 | Ichimoku | buy | SOL-USD | 16.71 | — | entry signal |
| 2026-10-06T20:25 | Supertrend | buy | XRP-USD | 17.36 | — | entry signal |
| 2026-10-06T20:25 | Supertrend | buy | SOL-USD | 17.36 | — | entry signal |
| 2026-10-06T20:25 | EMA 9/21 cross | buy | XRP-USD | 13.86 | — | entry signal |
| 2026-10-06T20:25 | EMA 9/21 cross | buy | ETH-USD | 13.86 | — | entry signal |
| 2026-10-06T20:22 | AI bee: Bizzy | buy | SOL-USD | 9.76 | — | Jev: buy (buy p=0.58) |
| 2026-10-06T20:20 | AI bee: Bizzy | buy | XRP-USD | 9.56 | — | Jev: buy (buy p=0.57) |
| 2026-10-06T20:20 | MFI reversion | sell | XRP-USD | 17.40 | -0.08 | exit signal |
| 2026-10-06T20:20 | CCI reversion | buy | XRP-USD | 2.61 | — | rebalance up |
| 2026-10-06T20:20 | CCI reversion | buy | DOGE-USD | 2.61 | — | rebalance up |
| 2026-10-06T20:20 | CCI reversion | sell | SOL-USD | 10.37 | -0.04 | exit signal |
| 2026-10-06T20:20 | CCI reversion | sell | BTC-USD | 10.37 | -0.05 | exit signal |
| 2026-10-06T20:20 | Stochastic reversion | sell | DOGE-USD | 11.59 | -0.05 | exit signal |
| 2026-10-06T20:20 | OBV trend | buy | SOL-USD | 13.01 | — | entry signal |
| 2026-10-06T20:20 | RSI momentum | buy | SOL-USD | 15.40 | — | entry signal |
| 2026-10-06T20:20 | Triple EMA stack | buy | SOL-USD | 15.01 | — | entry signal |
| 2026-10-06T20:20 | EMA 20/50 cross | buy | SOL-USD | 18.60 | — | entry signal |
| 2026-10-06T20:15 | Consensus | buy | SOL-USD | 14.28 | — | entry |
| 2026-10-06T20:15 | Z-score reversion | sell | BTC-USD | 14.22 | -0.10 | exit signal |
| 2026-10-06T20:15 | MACD zero-line | buy | SOL-USD | 15.79 | — | entry signal |
| 2026-10-06T20:15 | EMA 9/21 cross | buy | BTC-USD | 13.86 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-08 20:57:05.000170+00:00 -> 2026-10-06 21:07:05.000170+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
