N = int(input())
F = [0] * N
S = [0] * N
azi_oisisa = {}

for i in range(N):
    F[i], S[i] = map(int, input().split())
    if F[i] not in azi_oisisa:
        azi_oisisa[F[i]] = [S[i], 0]
    else:
        if azi_oisisa[F[i]][0] < S[i]:
            azi_oisisa[F[i]][1] = azi_oisisa[F[i]][0]
            azi_oisisa[F[i]][0] = S[i]
        elif azi_oisisa[F[i]][1] < S[i]:
            azi_oisisa[F[i]][1] = S[i]

max_oisisa = 0
second_max_oisisa = 0
ans = 0
for k in azi_oisisa:
    if azi_oisisa[k][0] > max_oisisa:
        second_max_oisisa = max_oisisa
        max_oisisa = azi_oisisa[k][0]
    elif azi_oisisa[k][0] > second_max_oisisa:
        second_max_oisisa = azi_oisisa[k][0]
    ans = max(ans, azi_oisisa[k][0] + (azi_oisisa[k][1] // 2))

ans = max(ans, max_oisisa + second_max_oisisa)
print(ans)
