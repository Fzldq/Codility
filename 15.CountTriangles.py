def solution(A):
    length = len(A)
    if length < 3:
        return 0
    A.sort()
    res = 0
    for i in range(length - 2):
        k = i + 2
        for j in range(i + 1, length - 1):
            k = max(j + 1, k)
            while k < length:
                if A[i] + A[j] <= A[k]:
                    break
                k += 1
            res += k - j - 1
    return res


def solution(A):
    length = len(A)
    if length < 3:
        return 0
    import bisect
    A.sort()
    res = 0
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            idx = bisect.bisect_left(A, A[i] + A[j])
            if idx > j + 1:
                res += idx - j - 1
                # print(A[i], A[j], A[j + 1:idx])
    return res
