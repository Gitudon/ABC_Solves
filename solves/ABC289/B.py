N, M = map(int, input().split())
a = list(map(int, input().split()))
p = [0] * N
reten = [False] * N
for i in range(M):
    reten[a[i] - 1] = True
current = 0
tame = 0
zyunban = 1
while 0 in p:
    if reten[current] and p[current] == 0:
        current += 1
        tame += 1
    elif not reten[current] and p[current] == 0:
        p[current] = zyunban
        zyunban += 1
        if tame >= 1:
            for i in range(tame):
                p[current - i - 1] = zyunban
                zyunban += 1
        tame = 0
    elif p[current] != 0:
        current += 1
print(*p)
