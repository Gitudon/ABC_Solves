N = int(input())
A = list(map(int, input().split()))

mae = [0] * (N - 1)
ato = [0] * (N - 1)

count_mae = {}
unique_count_mae = 0
for i in range(N - 1):
    if A[i] not in count_mae:
        count_mae[A[i]] = 0
        unique_count_mae += 1
    count_mae[A[i]] += 1
    mae[i] = unique_count_mae

count_ato = {}
unique_count_ato = 0
for i in range(N - 1, 0, -1):
    if A[i] not in count_ato:
        count_ato[A[i]] = 0
        unique_count_ato += 1
    count_ato[A[i]] += 1
    ato[i - 1] = unique_count_ato

ans = 0
for i in range(N - 1):
    ans = max(ans, mae[i] + ato[i])

print(ans)
