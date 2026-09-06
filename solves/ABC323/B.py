N = int(input())
S = [input() for _ in range(N)]
kachisu = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            kachisu[i] += 1
kachisu2 = kachisu.copy()
kachisu2 = list(set(kachisu2))
kachisu2.sort(reverse=True)
ans = []
for i in range(len(kachisu2)):
    for j in range(N):
        if kachisu2[i] == kachisu[j]:
            ans.append(j + 1)
print(*ans)
