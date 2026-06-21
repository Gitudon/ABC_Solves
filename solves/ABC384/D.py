import bisect

N, S = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N)
for i in range(N):
    B[i] = A[-(i + 1)]

cumulative_sum_A = [0] * (N + 1)
for i in range(N):
    cumulative_sum_A[i + 1] = cumulative_sum_A[i] + A[i]
cumulative_sum_B = [0] * (N + 1)
for i in range(N):
    cumulative_sum_B[i + 1] = cumulative_sum_B[i] + B[i]
ans = "No"
temp = S % (cumulative_sum_A[-1])
sub = cumulative_sum_A[-1] - temp
li = [temp, sub]
loopflag = False
for i in range(N + 1):
    idx = bisect.bisect_left(cumulative_sum_B, li[0] - cumulative_sum_A[i])
    if idx <= N and cumulative_sum_A[i] + cumulative_sum_B[idx] in li:
        ans = "Yes"
        break
    idx = bisect.bisect_left(cumulative_sum_B, li[1] - cumulative_sum_A[i])
    if idx <= N and cumulative_sum_A[i] + cumulative_sum_B[idx] in li:
        ans = "Yes"
        break
print(ans)
