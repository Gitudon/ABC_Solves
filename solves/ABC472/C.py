N, M, K = map(int, input().split())
A = list(map(int, input().split()))

eat = [False] * N
cal = 0
for i in range(N):
    if i >= M:
        if eat[i - M]:
            cal -= A[i - M]
    if cal + A[i] <= K:
        eat[i] = True
        cal += A[i]

for i in range(N):
    if eat[i]:
        print("Yes")
    else:
        print("No")
