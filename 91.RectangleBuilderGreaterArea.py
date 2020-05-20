def solution(A, X):
    length = len(A)
    if length < 5:
        return 0
    from collections import Counter
    c = Counter(A)
    A1 = [i for i, j in c.items() if j > 1]
    A2 = [i for i, j in c.items() if j > 3]
    A1.sort()
    A2.sort()
    import bisect
    res = 0
    l1, l2 = len(A1), len(A2)
    for i in range(l1 - 1, -1, -1):
        div = X / A1[i]
        if div > A1[i]:
            break
        idx = bisect.bisect_left(A1, div)
        res += i - idx
    for i in range(l2 - 1, -1, -1):
        sqr = A2[i] ** 2
        if sqr < X:
            break
        res += 1
    if res > 10 ** 9:
        res = -1
    return res
