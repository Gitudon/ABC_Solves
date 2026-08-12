N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
res = 2e9
for i in range(K + 1):
    res = min(res, A[i + (N - K) - 1] - A[i])
print(res)
