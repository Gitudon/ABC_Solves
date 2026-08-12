from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))

if N <= 2:
    print("Yes")
else:
    B = [0] * (N - 1)
    for i in range(N - 1):
        B[i] = Fraction(A[i + 1], A[i])
    C = list(set(B))
    if len(C) == 1:  # ここで誤判定
        print("Yes")
    else:
        print("No")
