n = int(input())
ans = 10**9
for h in range(1, n + 1):
    for w in range(1, h + 1):
        if h * w > n:
            break
        ans = min(ans, n - h * w + abs(h - w))
print(ans)
