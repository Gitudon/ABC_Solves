import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = "Yes"

for i in range(N):
    if len(graph[i]) != 2:
        ans = "No"
        break

visited = set()


def dfs(v):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(u)


dfs(0)

if len(visited) != N:
    ans = "No"

print(ans)
