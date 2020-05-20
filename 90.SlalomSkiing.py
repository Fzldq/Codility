import bisect


def solution(A):
    max_num = max(A)
    trans = []
    for i in A:
        trans += [2 * max_num + i, 2 * max_num - i, i]
    num_list = [-1, trans[0]]
    for i in trans[1:]:
        if i > num_list[-1]:
            num_list.append(i)
        elif i < num_list[-1]:
            idx = bisect.bisect_left(num_list, i)
            num_list[idx] = i
    return len(num_list) - 1
