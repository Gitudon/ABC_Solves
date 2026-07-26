import bisect

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
ruisekiwa = [0] * (N + 1)
for i in range(N):
    ruisekiwa[i + 1] = ruisekiwa[i] + B[i]
sum_A = sum(A)

for i in range(N):
    idx = bisect.bisect_right(B, A[i])
    if idx == N:
        print(0, end=" ")
    else:
        ans = sum_A - ruisekiwa[idx]
        print(ans, end=" ")
