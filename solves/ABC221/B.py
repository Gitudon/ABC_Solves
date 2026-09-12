S = input()
T = input()

ans = "No"
if S == T:
    ans = "Yes"
else:
    for i in range(len(S) - 1):
        if S[:i] + S[i + 1] + S[i] + S[i + 2 :] == T:
            ans = "Yes"
print(ans)
