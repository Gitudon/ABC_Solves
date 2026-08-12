N = int(input())
A = list(map(int, input().split()))

gokei = 0
bosu = 0
for i in range(N):
    gokei += A[i]
    if A[i] != 0:
        bosu += 1

print((gokei + bosu - 1) // bosu)
