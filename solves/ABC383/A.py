N = int(input())
time = 0
water = 0
for i in range(N):
    T, V = map(int, input().split())
    passed_time = T - time
    time = T
    water -= passed_time
    if water < 0:
        water = 0
    water += V
print(water)
