N = int(input())
D = list(map(int, input().split()))

ruisekiwa = [0] * (N)
for i in range(N - 1):
    ruisekiwa[i + 1] = ruisekiwa[i] + D[i]

for i in range(N):
    buf = []
    for j in range(i + 1, N):
        buf.append(ruisekiwa[j] - ruisekiwa[i])
    if buf != []:
        print(*buf)
