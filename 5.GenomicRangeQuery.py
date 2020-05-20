def solution(S, P, Q):
    dic = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    count = [0] * 4
    cur = []
    for i in S:
        count[dic[i] - 1] += 1
        tmp_count = count[:]
        cur.append(tmp_count)
    res = []
    for i in range(len(P)):
        p, q = P[i], Q[i]
        if p != 0:
            tmp = [b - a for a, b in zip(cur[p - 1], cur[q])]
            for idx, j in enumerate(tmp, 1):
                if j > 0:
                    res.append(idx)
                    break
        else:
            for idx, j in enumerate(cur[q], 1):
                if j > 0:
                    res.append(idx)
                    break
    return res


S, P, Q = ('CAGCCTA', [2, 5, 0], [4, 5, 6])
print(solution(S, P, Q))
