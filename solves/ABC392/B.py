N, M = map(int, input().split())
A = list(map(int, input().split()))
kiroku = [0] * (N + 1)
ans = []
for i in range(M):
    kiroku[A[i]] += 1
for i in range(1, N + 1):
    if kiroku[i] == 0:
        ans.append(i)
print(len(ans))
print(*ans)
