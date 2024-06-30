#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Minimum number of operations
    """
    if n < 1:
        return 0
    op = 0
    count = 1
    cp = 0

    while (count != n):
        if (cp == 0):
            cp = count
        if (n % count > 0):
            count += cp
        else:
            cp = count
            count += cp
            op += 1
        op += 1
    return op
