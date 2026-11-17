# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one fixed
# plan to /output/entry.txt — the plan an AI agent would follow to turn $100,
# a computer with internet access and 30 days into the most money, with no human
# doing the work. The gate takes UTF-8 text of 1 to 1,000 characters that is not
# only white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program runs twice
# with no network, and both runs must write the same bytes.
#
# The plan's edge: it only takes work whose payment is already locked in
# (escrowed bounties or pay-on-merge), so expected day-30 money is the sum of
# finished jobs, not a hope — and it prices small, delivers the same day, and
# prunes any channel that does not pay within a week.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell fast code fixes, only where payment is already locked in.",
        "Day 1: open profiles on make.fun, Algora and agent.family; offer one service: small Python bug fix + test, $25, delivered in 24 hours.",
        "Days 2-7: take only escrowed or pay-on-merge jobs under 2 hours, deliver the same day, and log every dollar, hour and channel.",
        "Days 8-14: after 5 jobs done, raise the price to $40 and add data cleanup + script, $30.",
        "Days 15-30: spend $0 on ads until $200 is earned, then $10 a day only on the best-paying channel; drop any channel with no sale in 7 days; give repeat buyers 10% off the next order.",
        "Rules: no gambling, no leverage, keep a $40 reserve untouched, never pay over $20 upfront for a tool, never work without escrow or pay-on-merge.",
        "Why this wins: every hour worked is already paid for, so the day-30 balance is the sum of finished jobs, not a hope. Target: 2 jobs a day at $25-40, $300-600 by day 30.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
