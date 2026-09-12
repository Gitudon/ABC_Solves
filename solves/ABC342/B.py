N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    A, B = map(int, input().split())
    a = 0
    b = 0
    for i in range(N):
        if P[i] == A:
            a = i
        if P[i] == B:
            b = i
    if a < b:
        print(A)
    else:
        print(B)
