N, D = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (10**6 + 1)
for x in A:
    cnt[x] += 1
if D == 0:
    ans = 0
    for x in cnt:
        ans += max(0, x - 1)
    print(ans)
    exit()


def solve(x):
    if not x:
        return 0
    x = [0] + x
    dp = [0] * (len(x) + 1)
    for i in range(1, len(x)):
        dp[i + 1] = min(dp[i] + x[i], dp[i - 1] + x[i - 1])
    return dp[-1]


ans = 0
for i in range(D):
    ans += solve(cnt[i::D])
print(ans)
