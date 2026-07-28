N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] * N
for i in range(N):
    C[i] = A[i] + B[i]

Math = sorted(A, reverse=True)
English = sorted(B, reverse=True)
Both = sorted(C, reverse=True)

P = [0] * N

for m in Math:
    if X == 0:
        break
    for i in range(N):
        if X == 0:
            break
        if A[i] == m and P[i] == 0:
            P[i] = 1
            X -= 1

for e in English:
    if Y == 0:
        break
    for i in range(N):
        if Y == 0:
            break
        if B[i] == e and P[i] == 0:
            P[i] = 1
            Y -= 1

for b in Both:
    if Z == 0:
        break
    for i in range(N):
        if Z == 0:
            break
        if C[i] == b and P[i] == 0:
            P[i] = 1
            Z -= 1

for i in range(N):
    if P[i] == 1:
        print(i + 1)
