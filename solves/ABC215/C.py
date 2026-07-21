from itertools import permutations

S, K = map(str, input().split())
K = int(K)
res = []

for p in set(permutations(S)):
    res.append("".join(p))
res.sort()

print(res[K - 1])
