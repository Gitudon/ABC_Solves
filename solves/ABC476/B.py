N = int(input())
S = input()
T = input()

ans = "Yes"
for i in range(N):
    if S[i] != T[i] and T[i] != "*":
        ans = "No"
print(ans)
