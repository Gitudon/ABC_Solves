N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
P -= 1
Q -= 1
R -= 1
S -= 1
for i in range(Q - P + 1):
    a = A[P + i]
    A[P + i] = A[R + i]
    A[R + i] = a
b = ""
for i in range(N - 1):
    b += str(A[i])
    b += " "
b += str(A[N - 1])
print(b)
