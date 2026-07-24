N, T = map(int, input().split())
t = list(map(int, input().split()))

dehazime = t[0]
next_stop = t[0] + T
oyu_time = 0
for i in range(1, N):
    if t[i] < next_stop:
        oyu_time += t[i] - dehazime
        dehazime = t[i]
        next_stop = t[i] + T
    else:
        oyu_time += T
        dehazime = t[i]
        next_stop = t[i] + T
oyu_time += T
print(oyu_time)
