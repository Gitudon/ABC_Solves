N, M, L = map(int, input().split())
A = list(map(int, input().split()))

groups = [[] for _ in range(L)]
for i in range(N):
    groups[i % L].append(A[i] % M)
cost = [[0] * M for _ in range(L)]
for g in range(L):
    for t in range(M):
        s = 0
        for x in groups[g]:
            s += (t - x + M) % M
        cost[g][t] = s

INF = 10**18
dp = [[INF] * M for _ in range(L + 1)]
dp[0][0] = 0
for g in range(L):
    for r in range(M):
        if dp[g][r] == INF:
            continue
        for t in range(M):
            nr = (r + t) % M
            dp[g + 1][nr] = min(dp[g + 1][nr], dp[g][r] + cost[g][t])
print(dp[L][0])
