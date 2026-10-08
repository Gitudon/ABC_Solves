S = input()
ans = ""
i = -1
while True:
    if S[i] == ".":
        break
    ans = S[i] + ans
    i -= 1
print(ans)
