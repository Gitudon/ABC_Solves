X = int(input())

ans = 0
current = 100

while current < X:
    current = current + current // 100
    ans += 1

print(ans)
