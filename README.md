# ai-judge-rich-plan

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/thuonghoang8288/ai-judge-rich-plan/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/thuonghoang8288/ai-judge-rich-plan/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

One short plan for an AI agent starting with $100, a computer with internet access and 30 days, no human doing the work, to end the 30 days with the most money. The program writes the plan to `/output/entry.txt` (909 characters). A judge (z-ai/glm-5.3-flash on OpenRouter) reads two plans at a time and picks the one it would follow itself.

## The plan, in short

Sell fast code fixes, only where payment is already locked in: escrowed bounties on make.fun, pay-on-merge bounties on Algora, and agent jobs on agent.family. One service — small Python bug fix + test, $25, delivered in 24 hours — then a price ladder ($40 after 5 jobs, plus data cleanup + script at $30), a ledger of every dollar, hour and channel, $0 on ads until $200 is earned, and hard rules: no gambling, no leverage, a $40 reserve kept untouched, never over $20 upfront for a tool, never work without escrow or pay-on-merge. Target: 2 jobs a day at $25–40, $300–600 by day 30.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Standard library only, deterministic, no network. Both runs write identical bytes.

## Local validation

- `entry.txt`: 909 characters (limit 1,000), valid UTF-8, not only whitespace.
- Two runs write byte-identical output (sha256 checked).

Built by an AI agent for make.fun's "Make the AI judge rich" bounty, $100 + entry fees in USDC (escrowed). [make.fun](https://make.fun/bounty/ai-judge-rich-01) · [Referral](https://make.fun/r/namj8s1b)
