N, K = map(int, input().split())
A = list(map(int, input().split()))
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
ans = 0
for i in range(N):
    foo = 10**18
    for j in range(K):
        foo = min(foo, (X[i] - X[A[j] - 1]) ** 2 + (Y[i] - Y[A[j] - 1]) ** 2)
    ans = max(ans, foo)
print(ans**0.5)
