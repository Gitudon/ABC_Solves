S = input()

ans = 0
for i in range(len(S)):
    ans += (26**i) * (ord(S[-1 - i]) - ord("A") + 1)
print(ans)
