N = int(input())
S = input()

ans = ""
mode = False
for i in range(N):
    if S[i] == '"':
        mode = not mode
        ans += S[i]
    elif S[i] == "," and not mode:
        ans += "."
    else:
        ans += S[i]
print(ans)
