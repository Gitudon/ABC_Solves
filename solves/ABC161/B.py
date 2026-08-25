N, M = map(int, input().split())
A = list(map(int, input().split()))

# A_sum=sum(A)
A_sum = 0
for i in range(N):
    A_sum += A[i]
base = 1 / (4 * M) * A_sum

foo = 0
for i in range(N):
    if A[i] >= base:
        foo += 1
if foo >= M:
    print("Yes")
else:
    print("No")
