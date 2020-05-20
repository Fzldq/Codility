from math import gcd
from functools import lru_cache


@lru_cache(maxsize=None)
def func(x, g):
    while x != 1:
        gx = gcd(x, g)
        if gx == 1:
            break
        x //= gx
    return x == 1


def same(a, b):
    g = gcd(a, b)
    return func(a, g) and func(b, g)


def solution(A, B):
    res = 0
    for a, b in zip(A, B):
        res += same(a, b)
    return res


print(solution([15, 10, 9], [75, 30, 5]))
