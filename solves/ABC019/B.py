s = input()

i = 0
ans = ""
count = 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        count += 1
    else:
        ans += s[i] + str(count + 1)
        count = 0
    i += 1
ans += s[i] + str(count + 1)

print(ans)
