N = int(input())
A = list(map(int, input().split()))

C = [0] * (N + 1)
for i in range(N):
    # 1つ次は現在よりA[i]だけ大きい
    C[i + 1] = C[i] + A[i]

ans = 0
mod = 10**9 + 7
for i in range(N - 1):
    ans = (ans + (A[i] * (C[N] - C[i + 1]))) % mod
print(ans)
