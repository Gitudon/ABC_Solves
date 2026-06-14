S = input()

cnt = [0] * 26
summ = [0] * 26
n = len(S)
ans = 0
for i in range(n):
    v = ord(S[i]) - ord("A")
    ans += (i - 1) * cnt[v] - summ[v]
    cnt[v] += 1
    summ[v] += i
print(ans)
