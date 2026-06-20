H, W, A, B = map(int, input().split())
ans = 0


def dfs(num, a, b, bit):
    if a == 0 and b == 0 and bit == (1 << H * W) - 1:
        global ans
        ans += 1
        return
    elif (a == 0 and b == 0) or bit == (1 << H * W) - 1 or num > H * W:
        return
    if bit & (1 << num) > 0:
        dfs(num + 1, a, b, bit)
    else:
        if num % W < W - 1 and bit & (1 << (num + 1)) == 0 and a > 0:
            dfs(num + 2, a - 1, b, bit | (1 << num) | (1 << (num + 1)))
        if num + W < H * W and bit & (1 << (num + W)) == 0 and a > 0:
            dfs(num + 1, a - 1, b, bit | (1 << num) | (1 << (num + W)))
        if b > 0:
            dfs(num + 1, a, b - 1, bit | (1 << num))


dfs(0, A, B, 0)
print(ans)
