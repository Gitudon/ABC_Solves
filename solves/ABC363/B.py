N, T, P = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
while True:
    cnt = 0
    for i in range(N):
        if L[i] >= T:
            cnt += 1
    if cnt >= P:
        break
    for i in range(N):
        L[i] += 1
    ans += 1
print(ans)
