def solution(A):
    l = len(A)
    if not l:
        return 0
    A = [abs(i) for i in A]
    maxA = max(A)
    m = l * maxA
    res = x = y = 1 << m
    for i in A:
        res = res << i | res >> i
    for i in range(m + 1):
        if x & res or y & res:
            return i
        x <<= 1
        y >>= 1
