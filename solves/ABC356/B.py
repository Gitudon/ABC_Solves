N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
sessyu = [0] * M
for x in X:
    for i in range(M):
        sessyu[i] += x[i]
ans = "Yes"
for i in range(M):
    if sessyu[i] < A[i]:
        ans = "No"
        break
print(ans)
