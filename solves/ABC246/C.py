N, K, X = map(int, input().split())
A = list(map(int, input().split()))
total_sum = sum(A)

S = 0
for i in range(N):
    S += A[i] // X
    A[i] %= X

if S >= K:
    print(total_sum - K * X)
else:
    K -= S
    A.sort(reverse=True)
    for i in range(min(N, K)):
        A[i] = 0
    print(sum(A))
