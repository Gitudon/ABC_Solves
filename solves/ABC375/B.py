import math

N = int(input())
X = [0] * (N + 2)
Y = [0] * (N + 2)
for i in range(1, N + 1):
    X[i], Y[i] = map(int, input().split())


def solve(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


ans = 0
for i in range(N + 1):
    ans += solve(X[i], Y[i], X[i + 1], Y[i + 1])
print(ans)
