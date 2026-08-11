N = int(input())
A = [[0] * N for i in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
B = [[0] * N for i in range(N)]
for i in range(N):
    B[i] = list(map(int, input().split()))
# 置き換えた物を三つ作って四つをBと比較
a = True
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            if B[i][j] == 0:
                a = False
if a:
    print("Yes")
    exit()
for _ in range(3):
    for k in range(N):
        C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = A[N - 1 - j][i]
    A = C
    a = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if B[i][j] == 0:
                    a = False
    if a:
        print("Yes")
        exit()
print("No")
