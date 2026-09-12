A, B = map(int, input().split())
ans = 0
for i in range(-100, 201):
    buf = [A, B, i]
    buf.sort()
    if abs(buf[0] - buf[1]) == abs(buf[1] - buf[2]):
        ans += 1
print(ans)
