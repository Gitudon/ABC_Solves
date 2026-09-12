S = input()

ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        buf = S[i:j]
        res = 0
        if len(buf) >= 3 and buf[0] == "t" and buf[0] == buf[-1]:
            foo = 0
            for k in range(len(buf)):
                if buf[k] == "t":
                    foo += 1
            res = (foo - 2) / (len(buf) - 2)
        ans = max(ans, res)
print(ans)
