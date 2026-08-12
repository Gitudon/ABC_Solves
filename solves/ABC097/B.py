X = int(input())
ans = [1]
for b in range(2, 101):
    p = 2
    while True:
        buf = b**p
        if buf <= X:
            ans.append(buf)
        else:
            break
        p += 1
print(max(ans))
