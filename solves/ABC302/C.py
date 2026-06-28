import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]

for perm in itertools.permutations(S):
    ok = True
    for i in range(N - 1):
        cnt = sum([1 for j in range(M) if perm[i][j] != perm[i + 1][j]])
        if cnt != 1:
            ok = False
            break
    if ok:
        print("Yes")
        exit()
print("No")
