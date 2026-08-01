N = int(input())
S = input()

ans = 0
for i in range(N):
    if S[i] == "x":
        if i == 0:
            if N == 1:
                ans += 1
            elif S[i + 1] == "x":
                ans += 1
        elif i == N - 1:
            if S[i - 1] == "x":
                ans += 1
        else:
            if S[i - 1] == "x" and S[i + 1] == "x":
                ans += 1

print(ans)
