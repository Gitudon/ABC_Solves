S = input()

ans = len(S)

buf = 0
for i in range(len(S) - 1, -1, -1):
    back = (int(S[i]) - buf) % 10
    ans += back
    buf = buf + back % 10

print(ans)
