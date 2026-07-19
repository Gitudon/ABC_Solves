N, K = map(int, input().split())
a = []
for i in range(N):
    pair = tuple(map(int, input().split()))
    a.append(pair)
a = sorted(a, key=lambda x: x[0])
yaku = 0
for i in range(N):
    yaku += a[i][1]
if yaku <= K:
    print(1)
    exit()
for i in range(N):
    yaku -= a[i][1]
    if yaku <= K:
        print(a[i][0] + 1)
        exit()
