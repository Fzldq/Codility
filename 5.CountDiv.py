def solution(A, B, K):
    a = (A // K + (A % K != 0)) * K
    b = (B // K) * K
    if a > b:
        return 0
    else:
        return (b - a) // K + 1
