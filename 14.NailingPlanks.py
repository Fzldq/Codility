# def solution(A, B, C):
#     n, m = len(A), len(C)
#     M = m << 1 | 1
#     left, right, res = 0, m, -1
#     while left <= right:
#         mid = (left + right) >> 1
#         cur = [0] * M
#         for i in range(mid):
#             cur[C[i]] += 1
#         for i in range(M):
#             cur[i] += cur[i - 1]
#         can = True
#         for i in range(n):
#             if cur[B[i]] - cur[A[i] - 1] == 0:
#                 can = False
#                 break
#         if can:
#             res = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return res


from collections import deque


def solution(A, B, C):
    n, m = len(A), len(C)
    M = (m << 1) | 1
    nail = [float('inf')] * M
    for i in range(m - 1, -1, -1):
        nail[C[i]] = i
    plank = [0] * M
    for i in range(n):
        plank[B[i]] = max(plank[B[i]], A[i])
    left, right, res = 0, 0, 0
    st = deque()
    for i in range(1, M):
        if plank[i] > left:
            left = plank[i]
            while st:
                if st[0] < left:
                    st.popleft()
                else:
                    break
            for right in range(max(right, left), i + 1):
                while st:
                    if nail[st[-1]] >= nail[right]:
                        st.pop()
                    else:
                        break
                st.append(right)
            if st:
                res = max(res, nail[st[0]])
            if res >= float('inf'):
                return -1
    return res + 1


print(solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2]))
