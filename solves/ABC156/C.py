N = int(input())
X = list(map(int, input().split()))

X_average_floor = sum(X) // N
X_average_ceil = X_average_floor + 1

ans_one = 0
ans_two = 0
for x in X:
    ans_one += (x - X_average_floor) ** 2
    ans_two += (x - X_average_ceil) ** 2
print(min(ans_one, ans_two))
