S = input()

MOD = 998244353
length = 1
ans = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        length += 1
    else:
        ans += length * (length + 1) // 2
        ans %= MOD
        length = 1

ans += length * (length + 1) // 2 % MOD

print(ans)
