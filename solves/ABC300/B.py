# 縦横一周してその間に一致するかしないか
H, W = map(int, input().split())
A = [0] * H
B = [0] * H
for i in range(H):
    A[i] = input()
for i in range(H):
    B[i] = input()
if A == B:
    print("Yes")
    exit()
for k in range(W):
    C = []
    for i in range(H):
        c = str(A[i])[1:] + str(A[i])[0]
        C.append(c)
    A = C
    if A == B:
        print("Yes")
        exit()
    for l in range(H):
        D = [0] * H
        D[0] = A[H - 1]
        for j in range(1, H):
            D[j] = A[j - 1]
        A = D
        if A == B:
            print("Yes")
            exit()
print("No")
