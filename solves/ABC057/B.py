N, M = map(int, input().split())
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
c = [0] * M
d = [0] * M
for i in range(M):
    c[i], d[i] = map(int, input().split())


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


ans = [0] * N

for i in range(N):
    foo = 10**10
    ans[i] = -1
    for j in range(M):
        if foo > manhattan(a[i], b[i], c[j], d[j]):
            foo = manhattan(a[i], b[i], c[j], d[j])
            ans[i] = j + 1

for i in range(N):
    print(ans[i])
