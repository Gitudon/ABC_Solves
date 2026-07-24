N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

P = [[] for _ in range(M + 1)]
for i in range(N):
    P[C[i]].append(i)

ans = ["?"] * N
for i in range(1, M + 1):
    k = len(P[i])
    for j in range(k):
        ans[P[i][(j + 1) % k]] = S[P[i][j]]

for a in ans:
    print(a, end="")
