def solution(A):
    l = len(A)
    if l == 2:
        return 0
    avg = 10000
    res = 0
    for i in range(l - 1):
        tmp = (A[i] + A[i + 1]) / 2
        if tmp < avg:
            avg = tmp
            res = i
    for i in range(l - 2):
        tmp = (A[i] + A[i + 1] + A[i + 2]) / 3
        if tmp < avg:
            avg = tmp
            res = i
    return res
