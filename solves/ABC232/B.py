S = input()
T = input()

ans = "Yes"
for i in range(len(S) - 1):
    if (ord(S[i]) - ord(T[i])) % 26 != (ord(S[i + 1]) - ord(T[i + 1])) % 26:
        ans = "No"
print(ans)
