N, M = map(int, input().split())

cities = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    cities[a] += 1
    cities[b] += 1

for i in range(1, N + 1):
    print(cities[i])
