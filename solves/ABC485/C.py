N = int(input())
C = list(map(int, input().split()))

INF = 10**10

# i より左で、C[j] != C[i] となる最大の j
left = [-INF] * N
for i in range(1, N):
    if C[i - 1] != C[i]:
        left[i] = i - 1
    else:
        left[i] = left[i - 1]

# i より右で、C[j] != C[i]
right = [INF] * N
for i in range(N - 2, -1, -1):
    if C[i + 1] != C[i]:
        right[i] = i + 1
    else:
        right[i] = right[i + 1]

for i in range(N):
    ans = min(i - left[i], right[i] - i)
    print(ans, end=" ")
