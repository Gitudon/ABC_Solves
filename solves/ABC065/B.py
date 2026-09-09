N = int(input())

trained = [False] * (N + 1)
a = [0] * (N + 1)
for i in range(1, N + 1):
    a[i] = int(input())

now = 1
cnt = 0
while True:
    if now == 2:
        print(cnt)
        break
    if trained[now]:
        print(-1)
        break
    trained[now] = True
    now = a[now]
    cnt += 1
