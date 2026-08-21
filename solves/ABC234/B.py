N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())


def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, distance(x[i], y[i], x[j], y[j]))

print(ans**0.5)
