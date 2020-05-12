def solution(A, B):
    s = sum(B)
    n = len(B)
    res = 0
    stack = []
    if s == n or s == 0:
        return n
    for i in range(n):
        if B[i]:
            stack.append(A[i])
        else:
            while stack:
                if A[i] > stack[-1]:
                    stack.pop()
                else:
                    break
            else:
                res += 1
    res += len(stack)
    return res


A = [1, 2, 3, 4, 5]
B = [0, 0, 0, 0, 0]
print(solution(A, B))
