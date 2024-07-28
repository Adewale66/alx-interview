#!/usr/bin/env python3
"""Prime game
"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    b = 0
    m = 0
    for i in nums:
        number_of_prime = 0
        for j in range(1, i+1):
            if is_prime(j):
                number_of_prime += 1
        if number_of_prime % x == 0:
            m += 1
        else:
            b += 1
    return 'Ben' if b > m else 'Maria'
