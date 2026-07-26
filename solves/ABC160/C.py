K, N = map(int, input().split())
A = list(map(int, input().split()))

amari = K - A[-1]

ans = 10**10
# 順走
for i in range(N):
    if i == 0:
        ans = min(ans, A[-1] - A[i])
    else:
        ans = min(ans, A[-1] + amari)
# 逆走
for i in range(N):
    if i == N - 1:
        ans = min(ans, A[i] - A[0])
    else:
        ans = min(ans, A[i] + K - A[i + 1])
print(ans)
