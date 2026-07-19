import sys

sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    A, B = map(int, input().split())
    graph[A].append(i)
    graph[B].append(i)

skills = [0] * (N + 1)
skills[0] = 1


def dfs(v):
    skills[v] = 1
    for vv in graph[v]:
        if not skills[vv]:
            dfs(vv)


dfs(0)

print(sum(skills) - 1)
