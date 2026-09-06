N = int(input())
S = input()

ans = ""
for i in range(len(S)):
    ans += chr((ord(S[i]) + N - 65) % 26 + 65)
print(ans)
