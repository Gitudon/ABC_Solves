N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    for j in range(1, D[i - 1] + 1):
        c = []
        for a in str(i):
            c.append(a)
        for a in str(j):
            c.append(a)
        c = set(c)
        if len(c) == 1:
            ans += 1
print(ans)
