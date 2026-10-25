N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    # 登る
    if A[i] <= K and K <= A[i + 1]:
        ans += 1
    # 降りる
    if A[i] >= K and A[i + 1] <= K:
        ans += 1
for i in range(1, N - 1):
    # 重複して数えている所をマイナス
    if A[i] == K:
        ans -= 1
print(ans)
