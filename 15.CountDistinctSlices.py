def solution(M, A):
    res = 0
    length = end = len(A)
    idx = [length] * (M + 1)
    for i in range(length - 1, -1, -1):
        end = min(end, idx[A[i]])
        idx[A[i]] = i
        res += end - i
    if res > 10 ** 9:
        res = 10 ** 9
    return res
