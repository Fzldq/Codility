def solution(A):
    l = len(A)
    if l == 1:
        return 0
    from collections import Counter
    c = Counter(A)
    leader = None
    for i, lcnt in c.items():
        if lcnt > l / 2:
            leader = i
            break
    if leader is None:
        return 0
    res = cnt = 0
    for i in range(l):
        if A[i] == leader:
            cnt += 1
        if cnt > (i + 1) / 2 and lcnt - cnt > (l - i - 1) / 2:
            res += 1
    return res


A = [0, 0]
print(solution(A))
