[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Seixx43/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Seixx43/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess

Entry for the make.fun bounty [tiny-chess-01 — Build the strongest chess engine in 4 KB of Python](https://make.fun/bounty/tiny-chess-01).

- `main.py` is **4,037 bytes** (limit 4,096): a 0x88 mailbox engine — negamax
  with null-move pruning, LMR, killers, MVV-LVA ordering, tuple-key TT,
  quiescence and tapered PST eval — iterative deepening to a fixed node
  budget (deterministic), lzma-packed into a `#coding:l1` + base85 stub.
- Python 3.13, stdlib only, no model calls. Run: `MAKEFUN_ENV_URL=<env> python3.13 main.py`.
- Practice trial: 4 wins / 2 losses vs the six house anchors ≈ **Elo 1,451**
  (gate 1,154; house baseline ~1,365).
