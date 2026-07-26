N, Q = map(int, input().split())
a = list(map(int, input().split()))
current = {}
index = {}
for i in range(N):
    if a[i] not in current:
        current[a[i]] = 0
    current[a[i]] += 1
    if a[i] not in index:
        index[a[i]] = {}
    index[a[i]][current[a[i]]] = i + 1

for _ in range(Q):
    x, k = map(int, input().split())
    if x not in current:
        print(-1)
        continue
    if k > current[x]:
        print(-1)
        continue
    if x in index and k in index[x]:
        print(index[x][k])
    else:
        print(-1)
