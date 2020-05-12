def solution(A):
    import bisect
    lr = [[a - b, a + b] for a, b in enumerate(A)]
    lr.sort(key=lambda x: x[0])
    l = [i[0] for i in lr]
    r = [i[1] for i in lr]
    res = 0
    for i in range(len(r)):
        idx = bisect.bisect(l, r[i])
        res += idx - 1 - i
    if res > 1e7:
        res = -1
    return res
