N, X = map(str, input().split())
N = int(N)

x = ord(X) - ord("A")
ans = "No"
for i in range(N):
    S = input()
    if S[x] == "o":
        ans = "Yes"
        break

print(ans)
