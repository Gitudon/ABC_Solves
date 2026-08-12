N = int(input())
A = list(map(int, input().split()))
Q = int(input())
a = [[]] * Q
for i in range(Q):
    a[i] = list(map(int, input().split()))
for i in range(Q):
    if a[i][0] == 1:
        A[a[i][1] - 1] = a[i][2]
    else:
        print(A[a[i][1] - 1])
