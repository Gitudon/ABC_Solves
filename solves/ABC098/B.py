N = int(input())
S = input()
ans = []
for i in range(1, N):
    hidari = set(S[:i])
    migi = set(S[i:])
    ans.append(len(hidari & migi))
print(max(ans))
