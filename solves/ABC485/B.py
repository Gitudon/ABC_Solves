N, M = map(int, input().split())
jaguchi = [0] * N
haisuikan = [0] * M
for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == "o":
            jaguchi[i] = 1
            haisuikan[j] = 1

ans = ""
for i in range(N):
    if jaguchi[i] == 0:
        ans = f"Faucet {i + 1}"
for j in range(M):
    if haisuikan[j] == 0:
        ans = f"Drain {j + 1}"
print(ans)
