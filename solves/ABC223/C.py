N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

T = 0
for i in range(N):
    T += A[i] / (B[i] * 2)

ans = 0
i = 0
while T > 0:
    if T >= A[i] / B[i]:
        ans += A[i]
        T -= A[i] / B[i]
    else:
        ans += B[i] * T
        T = 0
    i += 1

print(ans)
