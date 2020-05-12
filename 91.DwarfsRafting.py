def solution(N, S, T):
    raft = [[0 for _ in range(N)] for _ in range(N)]
    for i in S.split():
        raft[int(i[:-1]) - 1][ord(i[-1]) - 65] = 'b'
    for i in T.split():
        raft[int(i[:-1]) - 1][ord(i[-1]) - 65] = 1
    half = N // 2
    lub = half ** 2 - sum(1 for i in range(half)
                          for j in range(half) if raft[i][j] == 'b')
    rub = half ** 2 - sum(1 for i in range(half)
                          for j in range(half, N) if raft[i][j] == 'b')
    ldb = half ** 2 - sum(1 for i in range(half, N)
                          for j in range(half) if raft[i][j] == 'b')
    rdb = half ** 2 - sum(1 for i in range(half, N)
                          for j in range(half, N) if raft[i][j] == 'b')
    lud = sum(1 for i in range(half)
              for j in range(half) if raft[i][j] == 1)
    rud = sum(1 for i in range(half)
              for j in range(half, N) if raft[i][j] == 1)
    ldd = sum(1 for i in range(half, N)
              for j in range(half) if raft[i][j] == 1)
    rdd = sum(1 for i in range(half, N)
              for j in range(half, N) if raft[i][j] == 1)
    if lub < rdd or rub < ldd or ldb < rud or rdb < lud:
        return -1
    m1 = min(lub, rdb)
    m2 = min(rub, ldb)
    return (m1 * 2 - lud - rdd) + (m2 * 2 - rud - ldd)


print(solution(4, '1B 1C 4B 1D 2A', '3B 2D'))
