n, m = map(int, input().split())
ls = []
for _ in range(m):
    a, b = map(int, input().split())
    d = a - b
    ls.append((d, a, b))
ls.sort()
ans = 0
for d, a, b in ls:
    if a > n:
        continue
    x = (n - a) // d + 1
    ans += x
    n -= x * d
print(ans)
