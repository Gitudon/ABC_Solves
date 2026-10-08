H, W = map(int, input().split())
h, w = map(int, input().split())

ans = H * W
ans -= h * W
ans -= (H - h) * w
print(ans)
