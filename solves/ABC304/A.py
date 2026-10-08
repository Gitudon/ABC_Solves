N = int(input())
S = [0] * N
A = [0] * N
for i in range(N):
    S[i], A[i] = map(str, input().split())
    A[i] = int(A[i])
a = min(A)
b = 0
while a != A[b]:
    b += 1
for i in range(b, N):
    print(S[i])
for i in range(b):
    print(S[i])
