n, m = map(int, input().split())
a = []
idx = [[] for _ in range(n)]
cnt = [0] * m
for i in range(m):
    k, *foods = map(int, input().split())
    cnt[i] = k
    a.append([f - 1 for f in foods])
    for f in a[i]:
        idx[f].append(i)
B = list(map(int, input().split()))
ans = 0
for b in B:
    b -= 1
    for id in idx[b]:
        cnt[id] -= 1
        if cnt[id] == 0:
            ans += 1
    print(ans)
