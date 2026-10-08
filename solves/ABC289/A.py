s = input()
t = ""
for i in range(len(s)):
    if s[i] == "0":
        t += "1"
    else:
        t += "0"
print(t)
