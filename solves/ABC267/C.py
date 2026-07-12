N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * (N + 1)
for i in range(1, N + 1):
    C[i] = C[i - 1] + A[i - 1]

sum_i = [0] * (N - M + 1)
now = 0
for i in range(M):
    now += A[i] * (i + 1)
sum_i[0] = now

for i in range(1, N - M + 1):
    sum_i[i] = sum_i[i - 1] + M * A[M + i - 1] - (C[M + i - 1] - C[i - 1])

print(max(sum_i))
