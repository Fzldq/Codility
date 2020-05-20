def solution(A):
    l = len(A)
    if l <= 2:
        return 0
    peak = []
    for i in range(l - 2):
        if A[i] < A[i + 1] > A[i + 2]:
            peak.append(i + 1)
    lp = len(peak)
    if lp <= 1:
        return lp
    max_flag = min(lp, int(i ** 0.5) + 1)
    for i in range(max_flag, 1, - 1):
        res, tmp = 1, peak[0]
        for j in peak[1:]:
            if j - tmp >= i:
                res += 1
                tmp = j
            if res == i:
                return res
    return res
