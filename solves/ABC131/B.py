N, L = map(int, input().split())

yotei = 0
for i in range(N):
    yotei += L + i

sa = 10**10
ans = -1
for i in range(N):
    foo = yotei - (L + i)
    if sa > abs(yotei - foo):
        sa = abs(yotei - foo)
        ans = foo
print(ans)
