N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

visited = [False] * N


def dfs(v):
    visited[v] = True
    for nv in G[v]:
        if not visited[nv]:
            dfs(nv)


count = 0
for v in range(N):
    if not visited[v]:
        dfs(v)
        count += 1

print(count)
