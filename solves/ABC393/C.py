N, M = map(int, input().split())
graph = {}
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        ans += 1
    else:
        if (u in graph and v in graph[u]) or (v in graph and u in graph[v]):
            ans += 1
        else:
            if u not in graph:
                graph[u] = set()
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)

print(ans)
