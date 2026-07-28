N = int(input())

ans = 0

for i in range(1, N + 1):
    if i**2 <= N:
        ans = i**2
    else:
        break

print(ans)
