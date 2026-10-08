s = input()
ans = ""
for i in range(len(s)):
    if s[i] == ",":
        ans += " "
    else:
        ans += s[i]
print(ans)
