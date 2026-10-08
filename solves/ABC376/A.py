N, C = map(int, input().split())
T = list(map(int, input().split()))
time = T[0]
ans = 1
for i in range(1, N):
    if T[i] - time >= C:
        ans += 1
        time = T[i]
print(ans)
