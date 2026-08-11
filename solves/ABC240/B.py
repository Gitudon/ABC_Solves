N = int(input())
A = list(map(int, input().split()))

kiroku = []
for i in range(N):
    if A[i] not in kiroku:
        kiroku.append(A[i])
print(len(kiroku))
