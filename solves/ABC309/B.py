N = int(input())
A = [0] * N
for i in range(N):
    A[i] = input()
B = [[0] * N for i in range(N)]
C = []
for i in range(1, N - 1):
    for j in range(1, N - 1):
        B[i][j] = A[i][j]
for i in range(N):
    C.append(A[0][i])
for i in range(1, N):
    C.append(A[i][N - 1])
for i in range(1, N):
    C.append(A[N - 1][N - 1 - i])
for i in range(1, N - 1):
    C.append(A[N - 1 - i][0])
j = 0
for i in range(1, N):
    B[0][i] = C[j]
    j += 1
for i in range(1, N):
    B[i][N - 1] = C[j]
    j += 1
for i in range(1, N):
    B[N - 1][N - 1 - i] = C[j]
    j += 1
for i in range(1, N - 1):
    B[N - 1 - i][0] = C[j]
    j += 1
B[0][0] = A[1][0]
for i in range(N):
    c = ""
    for j in range(N):
        c += str(B[i][j])
    print(c)
