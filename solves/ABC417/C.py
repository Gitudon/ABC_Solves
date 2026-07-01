from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

# j - A[j] = i + A[i]
for i in range(N):
    ans += count[i - A[i]]
    count[i + A[i]] += 1

print(ans)
