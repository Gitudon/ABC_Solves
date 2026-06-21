S = input()

ans = ""
for s in S:
    if s.isdecimal():
        ans += s
print(ans)
