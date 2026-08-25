n = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(1, n - 1):
    foo = [p[i - 1], p[i], p[i + 1]]
    if sum(foo) - max(foo) - min(foo) == p[i]:
        ans += 1
print(ans)
