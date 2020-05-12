def solution(K, M, A):
    left, right = max(A), sum(A)
    while left <= right:
        tmp_sum = (right + left) >> 1
        cur_sum = 0
        tmp_g = 0
        for i in A:
            cur_sum += i
            if cur_sum > tmp_sum:
                cur_sum = i
                tmp_g += 1
        if cur_sum > 0:
            tmp_g += 1
        if tmp_g <= K:
            right = tmp_sum - 1
        else:
            left = tmp_sum + 1
    return left
