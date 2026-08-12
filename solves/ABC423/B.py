N = int(input())
L = list(map(int, input().split()))

ans = [0] * (N + 1)
ans[0] = 1
ans[-1] = 1
i = 0
while i < N:
    if L[i] == 1:
        break
    ans[i + 1] = 1
    i += 1

j = -1
while abs(j) <= N:
    if L[j] == 1:
        break
    ans[j - 1] = 1
    j -= 1

answer = 0
for i in range(N + 1):
    if ans[i] == 0:
        answer += 1

print(answer)
