def solution(A):
    A = [i for i in A if i > 0]
    l = len(A)
    if l < 3:
        return 0
    A.sort()
    for i in range(l - 2):
        if A[i + 1] > A[i + 2] - A[i]:
            return 1
    else:
        return 0
