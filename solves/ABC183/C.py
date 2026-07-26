N, K = list(map(int, input().split()))
T = [[]] * N
for i in range(N):
    T[i] = list(map(int, input().split()))
ans = 0
b = []


def tra(s):
    if len(str(s)) == N:
        s = s * 10 + 1
        if s not in b:
            b.append(s)
        return
    c = []
    for i in range(1, N):
        if str(i + 1) not in str(s):
            c.append(i + 1)
    for d in c:
        tra(s * 10 + d)


tra(1)
for d in b:
    a = 0
    for i in range(len(str(d)) - 1):
        a += T[int(str(d)[i]) - 1][int(str(d)[i + 1]) - 1]
    if a == K:
        ans += 1
print(ans)
