N = int(input())
graph = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

ans = "No"
for i in range(1, N + 1):
    if graph[i] == N - 1:
        ans = "Yes"

print(ans)
