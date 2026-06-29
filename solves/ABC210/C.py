N, K = map(int, input().split())
c = list(map(int, input().split()))

candies = {}
for i in range(K):
    if c[i] in candies:
        candies[c[i]] += 1
    else:
        candies[c[i]] = 1

ans = len(candies.keys())

for i in range(1, N - K + 1):
    left = c[i - 1]
    right = c[i + K - 1]
    if right in candies:
        candies[right] += 1
    else:
        candies[right] = 1
    if left in candies:
        candies[left] -= 1
        if candies[left] == 0:
            del candies[left]
    ans = max(ans, len(candies.keys()))

print(ans)
