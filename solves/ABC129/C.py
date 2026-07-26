N, M = map(int, input().split())
alist = [0] * N
for _ in range(M):
    a = int(input())
    alist[a - 1] = 1
dp = [0] * (N + 2)
dp[1] = 1
for i in range(N):
    if alist[i] != 1:
        dp[i + 2] = (dp[i + 1] + dp[i]) % 1000000007
print(dp[-1])
