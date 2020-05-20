def solution(A):
    A.sort()
    length = len(A)
    left, right = 0, length - 1
    res = 2 * min(abs(A[left]), abs(A[right]))
    while left < right:
        res = min(abs(A[left] + A[right]), res)
        if abs(A[left]) < abs(A[right]):
            right -= 1
            res = min(2 * abs(A[right]), res)
        else:
            left += 1
            res = min(2 * abs(A[left]), res)
    return res
