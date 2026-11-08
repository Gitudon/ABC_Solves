import itertools

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


bunsi = 0

for p in itertools.permutations([i for i in range(N)]):
    buf = 0
    for i in range(N - 1):
        buf += distance(x[p[i]], y[p[i]], x[p[i + 1]], y[p[i + 1]])
    bunsi += buf

bunbo = 1
for i in range(1, N + 1):
    bunbo *= i

print(bunsi / bunbo)
