def solution(N, P, Q):
    n = N + 10
    sieve = list(range(n + 1))
    sieve[2::2] = [2] * (n // 2)
    for i in range(3, int(n ** 0.5) + 2, 2):
        if sieve[i] == i:
            sieve[i * i::2 * i] = [i] * ((n - i * i) // (2 * i) + 1)
    lst = []
    for i in range(1, n):
        a = sieve[i]
        b = i // a
        if i != a and b == sieve[b]:
            lst.append(i)
    import bisect
    res = []
    dici, dicj = {}, {}
    for i, j in zip(P, Q):
        if j not in dicj:
            dicj[j] = bisect.bisect(lst, j)
        if i not in dici:
            dici[i] = bisect.bisect(lst, i - 1)
        res.append(dicj[j] - dici[i])
    return res


print(solution(26, [1, 4, 16], [26, 10, 20]))
