N = int(input())
A = list(map(int, input().split()))

dictionary = {}
for i in range(N):
    dictionary[A[i]] = i + 1

ans = []
for i in range(1, N + 1):
    ans.append(dictionary[i])
print(*ans)
