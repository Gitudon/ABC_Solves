N = int(input())
S = bin(N)[2:]
ans = 0
for i in range(1, len(S) + 1):
    if S[-i] == "0":
        ans += 1
    else:
        break
print(ans)
