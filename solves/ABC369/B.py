N = int(input())
exhaust = 0
L = -1
R = -1
for i in range(N):
    A, S = map(str, input().split())
    A = int(A)
    if S == "L":
        if L == -1:
            L = A
        else:
            exhaust += abs(A - L)
            L = A
    else:
        if R == -1:
            R = A
        else:
            exhaust += abs(A - R)
            R = A
print(exhaust)
