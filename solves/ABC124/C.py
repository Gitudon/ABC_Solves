S = input()

koho1 = ""
koho2 = ""
for i in range(len(S)):
    if i % 2 == 0:
        koho1 += "0"
        koho2 += "1"
    else:
        koho1 += "1"
        koho2 += "0"

ans1 = 0
ans2 = 0

for i in range(len(S)):
    if S[i] != koho1[i]:
        ans1 += 1
    if S[i] != koho2[i]:
        ans2 += 1

print(min(ans1, ans2))
