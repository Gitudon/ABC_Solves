N, c1, c2 = map(str, input().split())
S = input()
ans = ""
for s in S:
    if s != c1:
        ans += c2
    else:
        ans += s
print(ans)
