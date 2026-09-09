W = input()

ans = ""
for i in range(len(W)):
    if W[i] not in "aeiou":
        ans += W[i]

print(ans)
