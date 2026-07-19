import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
visited = [False] * N
K = 0


def dfs(v):
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            dfs(g)


for i in range(N):
    if not visited[i]:
        dfs(i)
        K += 1

print(max(0, M - N + K))
