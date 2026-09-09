N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    graph[U - 1][V - 1] = 1
    graph[V - 1][U - 1] = 1
ans = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if graph[a][b] == 1 and graph[b][c] == 1 and graph[c][a] == 1:
                ans += 1
print(ans)
