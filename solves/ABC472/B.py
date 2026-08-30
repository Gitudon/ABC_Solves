N = int(input())
L = list(map(int, input().split()))

ans = 10**10
zencho = sum(L)

ruisekiwa = [0] * N
ruisekiwa[0] = L[0]
for i in range(1, N):
    ruisekiwa[i] = ruisekiwa[i - 1] + L[i]

for i in range(N):
    ans = min(ans, abs(zencho - 2 * ruisekiwa[i]))
print(ans)
