N, A = map(int, input().split())
T = list(map(int, input().split()))
time = 0
i = 0
while i < N:
    if time < T[i]:
        time = T[i]
    elif time >= T[i]:
        time += A
        print(time)
        i += 1
