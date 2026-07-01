N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [0] * N
dp[0] = T[0]

for i in range(N * 2):
    dp[(i + 1) % N] = min(T[(i + 1) % N], dp[i % N] + S[i % N])
for ans in dp:
    print(ans)
