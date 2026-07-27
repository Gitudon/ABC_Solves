S = input()

ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        for k in range(j + 1, len(S)):
            if j - i == k - j:
                if S[i] == "A" and S[j] == "B" and S[k] == "C":
                    ans += 1
print(ans)
