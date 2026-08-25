N, K = map(int, input().split())
S = [0] * N
for i in range(N):
    S[i] = input()
if N != K:
    winner = S[:K]
else:
    winner = S
winner = sorted(winner)
print(*winner)
