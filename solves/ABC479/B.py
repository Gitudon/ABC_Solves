N = int(input())
S = input()

ans = 0
current = 0

for i in range(N):
    if S[i] == "R":
        current += 1
    else:
        ans = max(current, ans)
        current = 0
ans = max(current, ans)
print(ans)
