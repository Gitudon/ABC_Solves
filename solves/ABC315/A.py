S = input()
no = ["a", "e", "i", "o", "u"]
ans = ""
for i in range(len(S)):
    if S[i] not in no:
        ans += S[i]
print(ans)
