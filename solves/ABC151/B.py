N, K, M = map(int, input().split())
A = list(map(int, input().split()))
goal = N * M
sum = 0

for i in A:
    sum += i

dis = goal - sum

if dis > K:
    print(-1)
elif dis < 0:
    print(0)
else:
    print(dis)
