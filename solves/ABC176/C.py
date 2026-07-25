N = int(input())
A = list(map(int, input().split()))

current_max = A[0]
ans = 0
for i in range(1, N):
    if A[i] > current_max:
        current_max = A[i]
    else:
        ans += current_max - A[i]
print(ans)
