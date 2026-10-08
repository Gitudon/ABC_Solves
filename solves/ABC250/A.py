H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 0

for c in range(1, H + 1):
    for d in range(1, W + 1):
        if abs(R - c) + abs(C - d) == 1:
            ans += 1
print(ans)
