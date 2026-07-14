N = int(input())
A = list(map(int, input().split()))

ans = []

dict = {}
for i in range(N):
    dict[A[i]] = i + 1

next = dict[-1]
ans.append(dict[-1])
while len(ans) < N:
    next = dict[next]
    ans.append(next)
print(*ans)
