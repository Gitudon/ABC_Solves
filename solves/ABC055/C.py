N, M = map(int, input().split())

ans = 0
if N <= M // 2:
    ans += N
    M -= 2 * N
    ans += M // 4
else:
    ans += M // 2

print(ans)
