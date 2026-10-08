S = input()
ans = ""
i = 0
m = len(S)
while S[i] != "|":
    ans += S[i]
    i += 1
i += 1
while S[i] != "|":
    i += 1
i += 1
while i != m:
    ans += S[i]
    i += 1
print(ans)
