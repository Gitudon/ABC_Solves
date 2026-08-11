N = int(input())
C = list(map(int, input().split()))

color = [0] * N

for i in range(N):
    color[C[i] - 1] += 1

print(N - max(color))
