def solution(A):
    acc1, acc2 = [0], [0]
    for i in A[1:-2]:
        acc1 += [i + acc1[-1] if i + acc1[-1] > 0 else 0]
    for i in A[-2:1:-1]:
        acc2 += [i + acc2[-1] if i + acc2[-1] > 0 else 0]
    acc2.reverse()
    res = max([a + b for a, b in zip(acc1, acc2)])
    return res


A = [3, 2, 6, -1, 4, 5, -1, 2]
[0, 2, 8, 7, 11, 16]
[14, 8, 9, 5, 0, 0]
print(solution(A))
