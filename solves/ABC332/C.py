N, M = map(int, input().split())
S = input()

muji = M
logo = 0
ans = 0
for i in range(N):
    if S[i] == "0":
        muji = M
        logo = ans
    elif S[i] == "1":
        if muji > 0:
            muji -= 1
        else:
            if logo > 0:
                logo -= 1
            else:
                ans += 1
    else:
        if logo > 0:
            logo -= 1
        else:
            ans += 1
print(ans)
