N = int(input())
H = list(map(int, input().split()))
T = 0
for h in H:
    n = h // 5
    T += n * 3
    h -= n * 5
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1
print(T)
