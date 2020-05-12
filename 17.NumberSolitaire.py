def solution(A):
    from collections import deque
    length = len(A)
    A += ['out'] * 6
    inf = float('-inf')
    dist = [inf] * (length + 6)
    dist[0] = A[0]
    move = list(range(1, 7))
    st = deque([0])
    while st:
        sx = st.popleft()
        for i in move:
            x = sx + i
            if A[x] == 'out':
                continue
            dx = dist[sx] + A[x]
            if dx <= dist[x]:
                continue
            dist[x] = dx
            st.append(x)
    return dist[length - 1]
