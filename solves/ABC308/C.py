from decimal import Decimal, getcontext

getcontext().prec = 20
N = int(input())
A = [0] * N
B = [0] * N
C = {}
for i in range(N):
    A[i], B[i] = map(int, input().split())
for i in range(N):
    seiko = Decimal(A[i]) / Decimal(A[i] + B[i])
    C[i] = seiko
C = sorted(C.items(), key=lambda x: x[1], reverse=True)
D = []
for key, value in C:
    D.append(key + 1)
print(*D)
