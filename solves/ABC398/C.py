N = int(input())
A = list(map(int, input().split()))

kiroku = {}
for i in range(N):
    if A[i] in kiroku:
        kiroku[A[i]] += 1
    else:
        kiroku[A[i]] = 1

ans = -1
buf = 0
for i in range(N):
    if kiroku[A[i]] == 1:
        if A[i] > buf:
            buf = A[i]
            ans = i + 1
print(ans)
