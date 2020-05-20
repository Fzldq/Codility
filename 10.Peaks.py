def solution(A):
    l = len(A)
    if l <= 2:
        return 0
    is_peak = [0] * l
    for i in range(l - 2):
        if A[i] < A[i + 1] > A[i + 2]:
            is_peak[i + 1] = 1
    sp = sum(is_peak)
    if not sp:
        return 0
    for i in range(l, 0, -1):
        if sp < i or l % i:
            continue
        block = l // i
        for j in range(i):
            if sum(is_peak[j * block: (j + 1) * block]) == 0:
                break
        else:
            return i
    else:
        return 0
