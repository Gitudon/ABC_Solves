H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = "No"
kuromasu_hazi_ue = H
kuromasu_hazi_sita = -1
kuromasu_hazi_hidari = -1
kuromasu_hazi_migi = W
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if i < kuromasu_hazi_ue:
                kuromasu_hazi_ue = i
            if i > kuromasu_hazi_sita:
                kuromasu_hazi_sita = i
            if j < kuromasu_hazi_migi:
                kuromasu_hazi_migi = j
            if j > kuromasu_hazi_hidari:
                kuromasu_hazi_hidari = j
ans = "Yes"
for i in range(kuromasu_hazi_ue, kuromasu_hazi_sita + 1):
    for j in range(kuromasu_hazi_migi, kuromasu_hazi_hidari + 1):
        if S[i][j] == ".":
            ans = "No"
print(ans)
