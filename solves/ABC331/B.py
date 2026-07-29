N, S, M, L = map(int, input().split())
ans = []
for s in range(101):
    for m in range(101):
        for l in range(101):
            if 6 * s + 8 * m + 12 * l >= N:
                ans.append(S * s + M * m + L * l)
print(min(ans))
