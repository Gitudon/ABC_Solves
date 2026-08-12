N, M = map(int, input().split())

K = [0] * N
A = [0] * N
for i in range(N):
    foo = list(map(int, input().split()))
    K[i] = foo[0]
    A[i] = foo[1:]

result = [0] * (M + 1)
for i in range(N):
    for k in range(K[i]):
        result[A[i][k]] += 1

ans = 0
for i in range(1, M + 1):
    if result[i] == N:
        ans += 1
print(ans)
