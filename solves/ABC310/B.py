N, M = map(int, input().split())
A = [[0] * N for i in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        a = 0
        if A[i][0] >= A[j][0]:
            a += 1
        if all(elem in A[j][2:] for elem in A[i][2:]):
            a += 1
        if (A[i][0] > A[j][0]) or (any(elem in A[j][2:] for elem in A[i][2:])):
            a += 1
        if A[i] != A[j]:
            a += 1
        if a >= 4:
            print("Yes")
            exit()
print("No")
