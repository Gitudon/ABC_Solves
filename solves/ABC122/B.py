S = input()

base = ["A", "C", "G", "T"]
ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        focus = S[i:j]
        flag = True
        for f in focus:
            if f not in base:
                flag = False
                break
        if flag:
            ans = max(ans, len(focus))
print(ans)
