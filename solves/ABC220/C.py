N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)

ans = N * (X // sum_A)
X %= sum_A
for i in range(N):
    if X < 0:
        break
    else:
        X -= A[i]
        ans += 1
print(ans)
