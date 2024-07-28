#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    if total < 1:
        return 0
    pos = 0
    count = 0
    coins.sort(reverse=True)
    while total != 0 and pos < len(coins):
        while pos < len(coins) and total < coins[pos]:
            pos += 1
        if pos >= len(coins):
            return -1
        total -= coins[pos]
        count += 1

    return count
