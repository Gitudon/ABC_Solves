N, T = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())

ans = 0
for i in range(1, N):
    if A[i] - A[i - 1] > T:
        ans += T
    else:
        ans += A[i] - A[i - 1]

print(ans + T)
