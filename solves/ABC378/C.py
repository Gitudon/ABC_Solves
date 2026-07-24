N = int(input())
A = list(map(int, input().split()))
B = [0] * N
last_seen = {}

for i in range(N):
    if A[i] in last_seen:
        B[i] = last_seen[A[i]] + 1
    else:
        B[i] = -1
    last_seen[A[i]] = i

print(*B)
