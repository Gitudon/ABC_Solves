N, D = map(int, input().split())
T = list(map(int, input().split()))
for i in range(N):
    for j in range(i + 1, N):
        if T[j] - T[i] <= D:
            print(T[j])
            exit()
print(-1)
