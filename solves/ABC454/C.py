import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A - 1].append(B - 1)

items = [0] * N
done = [False] * N


def dfs(v):
    done[v] = True
    items[v] = 1
    for nv in graph[v]:
        if not done[nv]:
            dfs(nv)


dfs(0)
print(sum(items))
