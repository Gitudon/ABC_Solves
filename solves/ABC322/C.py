N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (N + 1)
for i in range(M):
    B[A[i]] = A[i]

focus_idx = 0
for i in range(1, N + 1):
    if B[i] == 0:
        B[i] = A[focus_idx]
    else:
        focus_idx += 1

for i in range(1, N + 1):
    print(B[i] - i)
