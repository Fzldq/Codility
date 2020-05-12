def solution(A):
    count = []
    tmp = 0
    for i in A[::-1]:
        tmp += i
        count.append(tmp)
    count.reverse()
    res = 0
    for i in range(len(A)):
        if not A[i]:
            res += count[i]
    if res > 1e9:
        res = -1
    return res
