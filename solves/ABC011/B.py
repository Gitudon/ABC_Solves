S = input()

ans = ""

if S[0].islower():
    ans = S[0].upper()
else:
    ans = S[0]
for i in range(1, len(S)):
    if S[i].isupper():
        ans += S[i].lower()
    else:
        ans += S[i]
print(ans)
