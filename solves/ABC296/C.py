N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
i = 0
for j in range(N):
    while i < N and A[i] - A[j] < X:
        i += 1
    if i < N and A[i] - A[j] == X:
        print("Yes")
        exit()
print("No")
