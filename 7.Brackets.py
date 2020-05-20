def solution(S):
    l = len(S)
    if l % 2:
        return 0
    dic = {'(': ')', '[': ']', '{': '}'}
    half = ['(', '[', '{']
    stack = []
    for i in S:
        if i in half:
            stack.append(i)
        elif not stack:
            return 0
        elif dic[stack.pop()] != i:
            return 0
    if stack:
        return 0
    else:
        return 1
