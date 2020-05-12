def solution(A):
    cur_max1 = cur_max2 = min(A)
    left, right = [], []
    for i in A[::-1]:
        if i >= cur_max2:
            cur_max2 = i
        right.append(cur_max2)
    right.reverse()
    for i in A:
        if i >= cur_max1:
            cur_max1 = i
        left.append(cur_max1)
    res = 0
    for i, j, k in zip(A, left, right):
        left_deep = j - i
        right_deep = k - i
        res = max(res, min(left_deep, right_deep))
    return res
