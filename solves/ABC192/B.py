S = input()

ans = "Yes"
for i in range(len(S)):
    if i % 2 == 0 and ord("A") <= ord(S[i]) <= ord("Z"):
        ans = "No"
    if i % 2 == 1 and ord("a") <= ord(S[i]) <= ord("z"):
        ans = "No"

print(ans)
