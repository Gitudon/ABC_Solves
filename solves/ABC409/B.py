N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)

for i in range(N + 1):
    for j in range(N):
        if A[j] >= i:
            cnt[i] += 1
    if cnt[i] < i:
        cnt[i] = 0

ans = 0
for i in range(1, N + 1):
    if cnt[-i] != 0:
        ans = N - i + 1
        break
print(ans)
