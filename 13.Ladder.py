import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)


@lru_cache(maxsize=None)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def solution(A, B):
    n = max(A)
    fib_list = [fib(i) for i in range(n + 1)]
    res = []
    for a, b in zip(A, B):
        res.append(fib_list[a] & ((1 << b) - 1))
    return res


A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
print(solution(A, B))
