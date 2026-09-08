N, A, B = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    s = 0
    for j in str(i):
        s += int(j)
    if A <= s <= B:
        ans += i

print(ans)
