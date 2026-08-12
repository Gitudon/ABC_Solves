N = int(input())
A = list(map(int, input().split()))
S = [0] * (N - 1)
T = [0] * (N - 1)
for i in range(N - 1):
    S[i], T[i] = map(int, input().split())
for i in range(N - 1):
    A[i + 1] += (A[i] // S[i]) * T[i]
print(A[-1])
