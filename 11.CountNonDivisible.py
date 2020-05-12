def solution(A):
    from collections import defaultdict, Counter
    cnt = defaultdict(int, Counter(A))
    dset = defaultdict(set)
    l = len(A)
    for i in cnt:
        for j in range(1, int(i ** 0.5) + 1):
            if not i % j:
                dset[i].add(j)
                dset[i].add(i // j)
    res = [l - sum([cnt[j] for j in dset[i]]) for i in A]
    return res
