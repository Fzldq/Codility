from collections import deque


def fib(n):
    fib_list = [1]
    a = fib_list[0]
    b = 1
    while b <= n:
        fib_list.append(b)
        a, b = b, a + b
    return fib_list


def solution(A):
    A = [1] + A + [1]
    length = len(A)
    fib_list = fib(length)
    if length - 1 == fib_list[-1]:
        return 1
    dist = [length] * length
    dist[0] = 0
    st = deque([0])
    while st:
        sx = st.popleft()
        c = dist[sx]
        for f in fib_list:
            x = sx + f
            if x > length - 1:
                continue
            if not A[x]:
                continue
            dx = c + 1
            if dist[x] <= dx:
                continue
            dist[x] = dx
            st.append(x)
    if dist[-1] < length:
        return dist[-1]
    else:
        return -1


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))
