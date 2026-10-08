N, K, A = map(int, input().split())

ans = A - 1
for i in range(K):
    ans += 1
    if ans > N:
        ans = 1
print(ans)
