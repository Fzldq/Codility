def solution(H):
    stack = []
    res = 0
    for i in H:
        while stack:
            if i < stack[-1]:
                stack.pop()
                res += 1
            else:
                break
        else:
            stack.append(i)
        if i > stack[-1]:
            stack.append(i)
    res += len(stack)
    return res


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))
