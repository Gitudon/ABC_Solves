N = int(input())
R = [0] * N
C = [0] * N
for i in range(N):
    R[i], C[i] = map(int, input().split())

opt_row = (min(R) + max(R)) // 2
opt_col = (min(C) + max(C)) // 2

max_distance = 0
for i in range(N):
    distance = max(abs(R[i] - opt_row), abs(C[i] - opt_col))
    if distance > max_distance:
        max_distance = distance

print(max_distance)
