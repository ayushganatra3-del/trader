# Trading agent — live leaderboard

Mode: **paper** · started 2026-09-24T19:49:18.203581Z · updated 2026-10-11T14:55:05.000173+00:00 · 19154 ticks

> Paper money unless the broker mode says otherwise. Backtests use the last ~60 days of 5-minute bars with modelled costs; past results do not predict future returns, and most day-trading strategies lose money after costs.

## Agent: £95.94 (-4.06%)

Closed trades 53, win rate 54.7%, fees £2.10, max drawdown -5.22%.

### Copy trading: what famous investors and insiders disclosed

| Book | Latest disclosure | Holdings copied (weight) | Status |
|---|---|---|---|
| Copy: Buffett (Berkshire) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Burry (Scion) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Ackman (Pershing Square) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Druckenmiller (Duquesne) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Tepper (Appaloosa) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Cathie Wood (ARK) 13F | — | — | Refresh failed: SEC refused the request (HTTP 403): set the repository variable SEC_USER_AGENT to 'Your Name your@email.com' |
| Copy: Insider buying | 2026-10-10 | BBD 12%, GGR 12%, COE 12%, BORR 12%, GME 12%, BPRE 12%, PSUS 12%, PAM 12% | ok |
| Copy: AI-Trader top agents | — | — | Refresh failed: GET https://ai4trade.ai/api/leaderboard/position-pnl: The read operation timed out |

### Market regime (QQQ, 2026-10-09)

**Uptrend** since 2026-09-21 · level normal · 2 distribution days in 25 sessions · timing exposure 100% · VXN 20.55 · VIX 14.84 · last follow-through day 2026-08-04

Best bullish scores: MSFT 8.9, PLTR 8.0, MSTR 7.0, TECL 6.7, UPRO 6.5, AMZN 6.3

### AI bees (Jev: typesafe/jev-1.13)

Today: 10515 decisions in 2103 calls, $0.1471 spent.

| Bee | Last decided (UTC) | Buy / hold / sell | Holding | Problem |
|---|---|---|---|---|
| Bizzy | 2026-10-11T14:55 | 2 / 2 / 1 | NANC 17%, COIN 15% |  |
| Breezy | 2026-10-11T14:55 | 0 / 5 / 0 | cash |  |
| Boozy | 2026-10-11T14:55 | 4 / 1 / 0 | COIN 76% |  |

### Today's picks (walk-forward)

| Strategy | Symbol | Score | Look-back return | Trades |
|---|---|---:|---:|---:|
| Z-score reversion | TNA | 2.63 | +3.96% | 6 |
| RSI momentum | IWM | 2.39 | +1.07% | 4 |
| Z-score reversion | IWM | 2.00 | +0.88% | 6 |
| MFI reversion | AAPL | 1.96 | +0.72% | 7 |
| Connors RSI(2) · 1h | META | 1.82 | +1.50% | 3 |

## Every sleeve (each started with £100)

| # | Sleeve | Style | Live £ | Live % | Trades | Win % | Backtest % | Sharpe | Max DD % | BT trades |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | VWAP reversion · 1h | reversion | 103.28 | 3.28 | 37 | 43.2 | -7.44 | -2.26 | -13.79 | 117 |
| 2 | Timing: Nasdaq FTD · TQQQ | daily | 102.59 | 2.59 | 0 | — | -4.07 | -0.65 | -15.27 | 1 |
| 3 | Copy: Warren Buffett (BRK-B) | copy | 102.27 | 2.27 | 0 | — | -3.56 | -1.45 | -7.31 | 1 |
| 4 | Copy: Insider buying | copy | 102.08 | 2.08 | 14 | 57.1 | -15.28 | -2.51 | -23.22 | 71 |
| 5 | Daily: Connors RSI(2) · 3x ETFs | daily | 101.79 | 1.78 | 1 | 100.0 | 2.37 | 0.72 | -7.93 | 7 |
| 6 | Day trade: Noise-area momentum · TQQQ/SQQQ | daytrade | 101.70 | 1.70 | 5 | 60.0 | 2.03 | 0.84 | -3.68 | 18 |
| 7 | Copy: Congress Democrats (NANC) | copy | 101.39 | 1.39 | 0 | — | 1.88 | 0.91 | -3.62 | 1 |
| 8 | Hold SPY | benchmark | 101.31 | 1.31 | 0 | — | 0.49 | 0.34 | -3.66 | 1 |
| 9 | Timing: Nasdaq FTD · QQQ | daily | 101.15 | 1.15 | 0 | — | -0.85 | -0.44 | -5.09 | 1 |
| 10 | Day trade: Open breakout · TQQQ/SQQQ | daytrade | 100.47 | 0.47 | 6 | 50.0 | -2.97 | -0.97 | -9.74 | 24 |
| 11 | Daily: Exhaustion hammer | daily | 100.00 | 0.00 | 0 | — | 0.00 | 0.00 | 0.00 | 0 |
| 12 | AI bee: Breezy | ai | 100.00 | 0.00 | 0 | — | — | — | — | — |
| 13 | Max aggression: 1-day momentum | meta | 99.81 | -0.19 | 10 | 30.0 | -15.21 | -0.53 | -37.31 | 42 |
| 14 | Copy: Hedge-fund gurus (GURU) | copy | 99.75 | -0.25 | 0 | — | -3.82 | -1.76 | -5.36 | 1 |
| 15 | Day trade: ORB 5m · TQQQ/SQQQ | daytrade | 99.58 | -0.42 | 10 | 30.0 | 3.37 | 1.07 | -7.55 | 44 |
| 16 | Day trade: Stocks in Play ORB | daytrade | 99.55 | -0.45 | 37 | 37.8 | 4.67 | 2.21 | -1.56 | 85 |
| 17 | Hold BTC | benchmark | 99.36 | -0.64 | 0 | — | 28.94 | 3.45 | -8.68 | 1 |
| 18 | Donchian 55/20 · 1h | breakout | 99.32 | -0.68 | 27 | 14.8 | 13.90 | 1.72 | -16.96 | 108 |
| 19 | Stochastic reversion · 1h | reversion | 99.17 | -0.82 | 89 | 55.1 | -9.86 | -1.90 | -14.61 | 340 |
| 20 | Day trade: Last half hour · TQQQ/SQQQ | daytrade | 99.05 | -0.95 | 7 | 28.6 | -1.85 | -1.96 | -3.34 | 21 |
| 21 | Daily: SMA 20/50 cross · AAPL | daily | 98.66 | -1.34 | 0 | — | 1.66 | 0.71 | -5.18 | 1 |
| 22 | Copy: Cathie Wood (ARKK) | copy | 98.62 | -1.38 | 0 | — | 11.52 | 1.88 | -8.33 | 1 |
| 23 | Daily: Bullish score | daily | 97.86 | -2.14 | 4 | 0.0 | 0.77 | 0.30 | -12.76 | 11 |
| 24 | Three white soldiers · 1h | momentum | 97.62 | -2.38 | 6 | 0.0 | -3.00 | -2.31 | -4.28 | 27 |
| 25 | Z-score reversion · 1h | reversion | 97.20 | -2.80 | 42 | 42.9 | 1.26 | 0.38 | -8.60 | 158 |
| 26 | Trend pullback · 1h | trend | 97.10 | -2.90 | 78 | 23.1 | -23.00 | -6.50 | -25.39 | 173 |
| 27 | EMA 20/50 cross · 1h | trend | 96.72 | -3.29 | 39 | 12.8 | 5.16 | 0.79 | -19.85 | 136 |
| 28 | Agent (rotation) | meta | 96.67 | -3.33 | 80 | 30.0 | -5.57 | -2.00 | -8.33 | 253 |
| 29 | Daily: Momentum burst | daily | 96.67 | -3.33 | 5 | 20.0 | -4.08 | -0.47 | -17.67 | 40 |
| 30 | ADX DI cross · 1h | trend | 96.36 | -3.64 | 58 | 20.7 | -1.40 | -0.05 | -13.84 | 257 |
| 31 | Parabolic SAR · 1h | trend | 96.32 | -3.68 | 82 | 22.0 | -2.81 | -0.21 | -20.87 | 294 |
| 32 | Agent | meta | 95.94 | -4.06 | 53 | 54.7 | -8.82 | -4.94 | -9.58 | 230 |
| 33 | MACD cross · 1h | trend | 95.79 | -4.21 | 113 | 23.9 | -15.01 | -2.41 | -17.27 | 464 |
| 34 | Supertrend · 1h | trend | 95.12 | -4.88 | 53 | 13.2 | 0.22 | 0.22 | -18.22 | 209 |
| 35 | Agent (aggressive) | meta | 93.96 | -6.04 | 25 | 44.0 | -4.39 | -2.00 | -6.59 | 104 |
| 36 | Gap and go | momentum | 93.89 | -6.11 | 57 | 12.3 | 8.09 | 2.08 | -6.26 | 201 |
| 37 | Squeeze breakout · 1h | breakout | 93.85 | -6.15 | 37 | 24.3 | 23.83 | 3.25 | -8.95 | 106 |
| 38 | MFI reversion · 1h | reversion | 93.54 | -6.46 | 119 | 34.5 | -11.45 | -1.81 | -17.79 | 125 |
| 39 | RSI(14) reversion · 1h | reversion | 93.14 | -6.86 | 26 | 26.9 | -2.33 | -0.40 | -9.03 | 152 |
| 40 | Connors RSI(2) · 1h | reversion | 93.02 | -6.98 | 113 | 43.4 | -18.24 | -6.05 | -20.97 | 251 |
| 41 | Agent (ML meta-label) | meta | 92.87 | -7.13 | 392 | 18.4 | -2.97 | -0.36 | -14.17 | 414 |
| 42 | Ichimoku · 1h | trend | 92.81 | -7.19 | 42 | 19.0 | -0.09 | 0.19 | -20.11 | 120 |
| 43 | RSI momentum · 1h | momentum | 92.70 | -7.30 | 64 | 15.6 | 5.05 | 0.81 | -17.07 | 220 |
| 44 | Bollinger reversion · 1h | reversion | 92.59 | -7.41 | 76 | 36.8 | -20.88 | -4.99 | -23.37 | 317 |
| 45 | Volume breakout · 1h | breakout | 92.58 | -7.42 | 56 | 19.6 | 8.38 | 1.30 | -12.60 | 119 |
| 46 | Bollinger breakout · 1h | breakout | 91.61 | -8.39 | 70 | 28.6 | 5.82 | 0.92 | -12.90 | 287 |
| 47 | Williams %R · 1h | reversion | 91.22 | -8.78 | 123 | 46.3 | -24.04 | -4.14 | -26.91 | 513 |
| 48 | Opening range 30m | breakout | 90.97 | -9.03 | 147 | 22.4 | -16.80 | -5.09 | -17.78 | 578 |
| 49 | Triple EMA stack · 1h | trend | 90.73 | -9.27 | 69 | 15.9 | -9.24 | -0.93 | -26.38 | 239 |
| 50 | Candlestick reversal · 1h | reversion | 90.17 | -9.83 | 116 | 31.9 | -26.70 | -5.22 | -28.51 | 513 |
| 51 | CCI reversion · 1h | reversion | 89.65 | -10.35 | 101 | 44.6 | -7.66 | -0.97 | -14.35 | 416 |
| 52 | VWAP momentum · 1h | momentum | 89.46 | -10.54 | 283 | 21.9 | -33.25 | -4.99 | -39.17 | 1279 |
| 53 | Opening range 15m | breakout | 89.19 | -10.81 | 170 | 21.2 | -18.41 | -5.23 | -19.81 | 700 |
| 54 | MACD zero-line · 1h | trend | 88.84 | -11.15 | 64 | 18.8 | -6.55 | -0.70 | -19.96 | 239 |
| 55 | OBV trend · 1h | momentum | 88.78 | -11.22 | 149 | 18.8 | -12.37 | -1.40 | -28.19 | 319 |
| 56 | Donchian 20/10 · 1h | breakout | 88.74 | -11.26 | 59 | 18.6 | -1.27 | 0.05 | -17.72 | 225 |
| 57 | Heikin-Ashi · 1h | trend | 88.66 | -11.34 | 138 | 25.4 | -30.26 | -5.07 | -36.59 | 699 |
| 58 | Max aggression: 5-day momentum | meta | 87.97 | -12.03 | 7 | 28.6 | -14.32 | -1.05 | -34.64 | 28 |
| 59 | EMA 9/21 cross · 1h | trend | 87.76 | -12.24 | 104 | 13.5 | -9.95 | -1.15 | -21.65 | 340 |
| 60 | Three white soldiers | momentum | 87.35 | -12.65 | 141 | 17.7 | -48.42 | -23.53 | -48.45 | 591 |
| 61 | Keltner breakout · 1h | breakout | 87.10 | -12.90 | 43 | 18.6 | -11.32 | -1.30 | -25.35 | 214 |
| 62 | ROC + volume · 1h | momentum | 86.28 | -13.72 | 132 | 21.2 | -11.45 | -1.41 | -24.23 | 411 |
| 63 | ROC + volume | momentum | 74.62 | -25.38 | 390 | 22.6 | -72.78 | -16.60 | -73.88 | 1673 |
| 64 | RSI(14) reversion | reversion | 73.91 | -26.09 | 369 | 27.6 | -72.57 | -18.24 | -72.57 | 1490 |
| 65 | Squeeze breakout | breakout | 70.54 | -29.46 | 328 | 14.6 | -62.57 | -18.52 | -62.58 | 1235 |
| 66 | Donchian 55/20 | breakout | 70.10 | -29.90 | 332 | 17.8 | -67.60 | -14.48 | -67.63 | 1294 |
| 67 | Volume breakout | breakout | 70.00 | -30.00 | 262 | 13.0 | -62.69 | -18.09 | -62.74 | 903 |
| 68 | EMA 20/50 cross | trend | 69.30 | -30.70 | 335 | 19.4 | -77.29 | -15.54 | -77.31 | 1465 |
| 69 | VWAP reversion | reversion | 67.80 | -32.20 | 403 | 25.8 | -71.36 | -16.03 | -71.42 | 1431 |
| 70 | Supertrend | trend | 63.30 | -36.70 | 464 | 19.6 | -86.07 | -21.13 | -86.12 | 1915 |
| 71 | Keltner breakout | breakout | 62.28 | -37.72 | 451 | 14.2 | -83.81 | -27.96 | -83.83 | 1851 |
| 72 | AI bee: Boozy | ai | 60.38 | -39.62 | 255 | 5.1 | — | — | — | — |
| 73 | Ichimoku | trend | 59.92 | -40.08 | 407 | 9.6 | -81.83 | -23.61 | -81.84 | 1751 |
| 74 | Z-score reversion | reversion | 59.36 | -40.64 | 508 | 22.4 | -85.36 | -23.32 | -85.36 | 2082 |
| 75 | MFI reversion | reversion | 59.13 | -40.88 | 514 | 21.2 | -87.49 | -28.54 | -87.53 | 2120 |
| 76 | AI bee: Bizzy | ai | 57.71 | -42.29 | 836 | 8.7 | — | — | — | — |
| 77 | ADX DI cross | trend | 56.15 | -43.84 | 545 | 10.1 | -89.38 | -35.74 | -89.39 | 2125 |
| 78 | Trend pullback | trend | 54.95 | -45.05 | 586 | 14.8 | -90.99 | -27.13 | -90.99 | 2339 |
| 79 | Donchian 20/10 | breakout | 54.81 | -45.19 | 638 | 17.9 | -90.87 | -26.48 | -90.88 | 2671 |
| 80 | RSI momentum | momentum | 53.35 | -46.65 | 611 | 16.7 | -90.46 | -26.09 | -90.46 | 2392 |
| 81 | MACD zero-line | trend | 52.81 | -47.19 | 594 | 14.5 | -91.63 | -30.75 | -91.64 | 2373 |
| 82 | Triple EMA stack | trend | 52.59 | -47.41 | 632 | 15.2 | -93.26 | -30.73 | -93.27 | 2627 |
| 83 | VWAP momentum ⛔ | momentum | 50.61 | -49.39 | 716 | 8.7 | -98.68 | -31.70 | -98.68 | 5405 |
| 84 | EMA 9/21 cross ⛔ | trend | 50.39 | -49.61 | 736 | 15.9 | -97.39 | -34.28 | -97.40 | 3556 |
| 85 | OBV trend ⛔ | momentum | 50.37 | -49.63 | 760 | 14.6 | -96.48 | -36.77 | -96.48 | 3623 |
| 86 | Consensus ⛔ | meta | 50.34 | -49.66 | 619 | 9.9 | -94.20 | -25.99 | -94.20 | 2686 |
| 87 | Candlestick reversal ⛔ | reversion | 50.30 | -49.70 | 807 | 14.9 | -99.35 | -38.04 | -99.35 | 5700 |
| 88 | Connors RSI(2) ⛔ | reversion | 50.25 | -49.75 | 752 | 20.2 | -96.38 | -32.01 | -96.38 | 3624 |
| 89 | MACD cross ⛔ | trend | 50.17 | -49.83 | 660 | 12.9 | -99.73 | -43.27 | -99.73 | 6210 |
| 90 | Bollinger breakout | breakout | 50.15 | -49.85 | 672 | 14.0 | -93.57 | -33.68 | -93.58 | 2825 |
| 91 | Parabolic SAR ⛔ | trend | 50.11 | -49.89 | 673 | 14.4 | -97.36 | -38.58 | -97.37 | 3691 |
| 92 | CCI reversion ⛔ | reversion | 50.01 | -49.99 | 719 | 16.8 | -98.46 | -38.10 | -98.46 | 4714 |
| 93 | Williams %R ⛔ | reversion | 49.91 | -50.09 | 708 | 18.9 | -99.52 | -41.36 | -99.52 | 6153 |
| 94 | Bollinger reversion ⛔ | reversion | 49.86 | -50.14 | 775 | 17.4 | -95.84 | -34.25 | -95.84 | 3747 |
| 95 | Stochastic reversion ⛔ | reversion | 49.77 | -50.23 | 881 | 22.8 | -95.59 | -35.03 | -95.59 | 4084 |
| 96 | Heikin-Ashi ⛔ | trend | 49.77 | -50.23 | 605 | 8.3 | -99.90 | -48.61 | -99.90 | 8320 |

## Recent trades

| Time (UTC) | Sleeve | Side | Symbol | £ | P/L £ | Why |
|---|---|---|---|---:|---:|---|
| 2026-10-11T14:55 | RSI momentum | buy | BTC-USD | 2.71 | — | entry signal |
| 2026-10-11T14:55 | RSI momentum | sell | DOGE-USD | 2.68 | -0.01 | rebalance down |
| 2026-10-11T14:55 | Supertrend | buy | BTC-USD | 6.49 | — | entry signal |
| 2026-10-11T14:55 | Supertrend | sell | XRP-USD | 3.20 | -0.01 | rebalance down |
| 2026-10-11T14:55 | Supertrend | sell | DOGE-USD | 3.29 | -0.00 | rebalance down |
| 2026-10-11T14:50 | Squeeze breakout | buy | BTC-USD | 17.64 | — | entry signal |
| 2026-10-11T14:50 | Supertrend | buy | SOL-USD | 15.73 | — | entry signal |
| 2026-10-11T14:45 | AI bee: Bizzy | sell | XRP-USD | 8.38 | -0.06 | Jev: sell (sell p=0.67) after 11 min |
| 2026-10-11T14:45 | Squeeze breakout | buy | SOL-USD | 17.65 | — | entry signal |
| 2026-10-11T14:45 | RSI momentum | buy | SOL-USD | 13.34 | — | entry signal |
| 2026-10-11T14:45 | MACD zero-line | buy | BTC-USD | 13.21 | — | entry signal |
| 2026-10-11T14:45 | Triple EMA stack | buy | SOL-USD | 5.41 | — | entry signal |
| 2026-10-11T14:45 | Triple EMA stack | sell | XRP-USD | 2.78 | -0.00 | rebalance down |
| 2026-10-11T14:45 | Triple EMA stack | sell | DOGE-USD | 2.64 | -0.01 | rebalance down |
| 2026-10-11T14:45 | EMA 20/50 cross | buy | SOL-USD | 7.07 | — | entry signal |
| 2026-10-11T14:45 | EMA 20/50 cross | sell | XRP-USD | 3.56 | -0.01 | rebalance down |
| 2026-10-11T14:45 | EMA 20/50 cross | sell | DOGE-USD | 3.51 | -0.00 | rebalance down |
| 2026-10-11T14:40 | AI bee: Bizzy | sell | DOGE-USD | 7.93 | -0.03 | Jev: sell (sell p=0.50) after 22 min |
| 2026-10-11T14:40 | Ichimoku | buy | ETH-USD | 14.99 | — | entry signal |
| 2026-10-11T14:40 | MACD zero-line | buy | SOL-USD | 13.23 | — | entry signal |
| 2026-10-11T14:40 | MACD zero-line | buy | ETH-USD | 13.23 | — | entry signal |
| 2026-10-11T14:40 | Triple EMA stack | buy | BTC-USD | 13.04 | — | entry signal |
| 2026-10-11T14:35 | Volume breakout | buy | XRP-USD | 17.52 | — | entry signal |
| 2026-10-11T14:35 | Volume breakout | buy | DOGE-USD | 17.52 | — | entry signal |
| 2026-10-11T14:35 | Squeeze breakout | buy | XRP-USD | 17.67 | — | entry signal |
| 2026-10-11T14:35 | Squeeze breakout | buy | DOGE-USD | 17.67 | — | entry signal |
| 2026-10-11T14:35 | Keltner breakout | buy | XRP-USD | 15.58 | — | entry signal |
| 2026-10-11T14:35 | Keltner breakout | buy | DOGE-USD | 15.58 | — | entry signal |
| 2026-10-11T14:35 | Bollinger breakout | buy | XRP-USD | 10.05 | — | entry signal |
| 2026-10-11T14:35 | Bollinger breakout | buy | SOL-USD | 10.05 | — | entry signal |
| 2026-10-11T14:35 | Bollinger breakout | buy | ETH-USD | 10.05 | — | entry signal |
| 2026-10-11T14:35 | Bollinger breakout | buy | DOGE-USD | 10.05 | — | entry signal |
| 2026-10-11T14:35 | Bollinger breakout | buy | BTC-USD | 10.05 | — | entry signal |
| 2026-10-11T14:35 | Donchian 55/20 | buy | XRP-USD | 17.54 | — | entry signal |
| 2026-10-11T14:35 | Donchian 55/20 | buy | DOGE-USD | 17.54 | — | entry signal |
| 2026-10-11T14:35 | Donchian 20/10 | buy | SOL-USD | 13.71 | — | entry signal |
| 2026-10-11T14:35 | Donchian 20/10 | buy | ETH-USD | 13.71 | — | entry signal |
| 2026-10-11T14:35 | RSI momentum | buy | XRP-USD | 13.37 | — | entry signal |
| 2026-10-11T14:35 | RSI momentum | buy | ETH-USD | 13.37 | — | entry signal |
| 2026-10-11T14:35 | RSI momentum | buy | DOGE-USD | 13.37 | — | entry signal |

## Data problems on the last tick

- AXIA: yfinance: $AXIA: possibly delisted; no price data found  (5m 2026-08-13 14:55:05.000173+00:00 -> 2026-10-11 15:05:05.000173+00:00); yahoo: cooling down after a rate limit
- CRAFX: yfinance: 'tradingPeriods'; yahoo: cooling down after a rate limit
- CYBN: yfinance: $CYBN: possibly delisted; no timezone found; yahoo: cooling down after a rate limit
- GREE: yfinance: $GREE: possibly delisted; no timezone found; yahoo: cooling down after a rate limit

Open `dashboard.html` (download it or use a raw HTML viewer) for charts.
