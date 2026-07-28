N = int(input())

W = list(map(int, input().split()))

ans = 10**10

for i in range(N - 1):
    sa = abs(sum(W[: i + 1]) - sum(W[i + 1 :]))
    ans = min(ans, sa)
print(ans)
