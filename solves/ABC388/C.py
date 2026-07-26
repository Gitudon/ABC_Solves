N = int(input())
A = list(map(int, input().split()))

ans = 0
max_a = A[-1]
j = 0
for i in range(N):
    a = A[i]
    b = A[i] * 2
    if b > max_a:
        break
    while j < N and A[j] < b:
        j += 1
    if j >= N:
        break
    ans += N - j
print(ans)
