N, L, R = map(int, input().split())
S = input()

ans = "Yes"
for i in range(L - 1, R):
    if S[i] == "x":
        ans = "No"
print(ans)
