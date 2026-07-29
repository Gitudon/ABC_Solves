S = input()
ans = 0
i = 0
while i < len(S):
    if S[i] == "0":
        if i != len(S) - 1:
            if S[i + 1] == "0":
                ans += 1
                i += 2
            else:
                ans += 1
                i += 1
        else:
            ans += 1
            i += 1
    else:
        ans += 1
        i += 1
print(ans)
