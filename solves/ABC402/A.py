S = input()

ans = ""
for i in range(len(S)):
    if ord("A") <= ord(S[i]) <= ord("Z"):
        ans += S[i]

print(ans)
