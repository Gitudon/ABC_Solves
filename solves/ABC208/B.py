import math

P = int(input())

coins = [0] * 11
for i in range(1, 11):
    coins[i] = math.factorial(i)

ans = 0
while P > 0:
    for i in range(10, 0, -1):
        if P >= coins[i]:
            P -= coins[i]
            ans += 1
            break
print(ans)
