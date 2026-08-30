S = input()

ans = ""
for s in S:
    if s != "A":
        ans += "."
    else:
        ans += s
print(ans)
