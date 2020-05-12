def solution(A, B):
    length = len(A)
    if length <= 1:
        return length
    C = sorted(list(zip(A, B)), key=lambda x: x[1])
    prep = C[0][1]
    res = 1
    for left, right in C[1:]:
        if left > prep:
            res += 1
            prep = right
    return res
