N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F = sorted(F)
S = [0] * N
S[0] = F[0]
for i in range(N - 1):
    S[i + 1] = S[i] + F[i + 1]
k = (N + D - 1) // D
ans = P * k
for i in range(k):
    ans = min(ans, S[N - 1 - (i * D)] + (P * i))
print(ans)
