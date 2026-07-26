N = int(input())
A = list(map(int, input().split()))

cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + A[i]

ans = 0
for i in range(N):
    ans += A[i] * (cumsum[N] - cumsum[i + 1])

print(ans)
