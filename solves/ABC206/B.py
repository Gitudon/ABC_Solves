N = int(input())

ans = 1
total = 0
while total < N:
    total += ans
    ans += 1
print(ans - 1)
