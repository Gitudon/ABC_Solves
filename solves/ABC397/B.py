S = input()

ans = 0
i = 0
c = 0
while i < len(S):
    if c % 2 == 0:
        if S[i] == "o":
            ans += 1
        else:
            i += 1
    else:
        if S[i] == "i":
            ans += 1
        else:
            i += 1
    c += 1

if c % 2 == 0:
    print(ans)
else:
    print(ans + 1)
