N = int(input())
A = list(map(int, input().split()))
ans = N
tosa = -1
cnt = 0
for i in range(N - 1):
    if tosa == -1:
        tosa = A[i + 1] - A[i]
        cnt += 1
    else:
        if A[i + 1] - A[i] == tosa:
            cnt += 1
        else:
            tosa = A[i + 1] - A[i]
            ans += cnt * (cnt + 1) // 2
            cnt = 1
ans += cnt * (cnt + 1) // 2
print(ans)
