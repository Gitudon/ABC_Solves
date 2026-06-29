N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

ans = "No"
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (x[j] - x[k]) * (y[j] - y[i]) == (x[j] - x[i]) * (y[j] - y[k]):
                ans = "Yes"

print(ans)
