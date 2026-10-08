N, M, P = map(int, input().split())
day = M
ans = 0
while day <= N:
    ans += 1
    day += P
print(ans)
