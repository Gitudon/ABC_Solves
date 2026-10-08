R, C = map(int, input().split())
A11, A12 = map(int, input().split())
A21, A22 = map(int, input().split())

if R == 1:
    if C == 1:
        print(A11)
    else:
        print(A12)
else:
    if C == 1:
        print(A21)
    else:
        print(A22)
