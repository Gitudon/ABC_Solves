N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = 0
kiroku = [[] for _ in range(N)]
for i in range(N):
    kiroku[A[i] - 1].append(W[i])
for i in range(N):
    if kiroku[i] != []:
        ans += sum(kiroku[i]) - max(kiroku[i])
print(ans)
