N, M = map(int, input().split())
H = list(map(int, input().split()))

i = 0
while True:
    if M == 0 or i == N:
        print(i)
        break
    else:
        if H[i] <= M:
            M -= H[i]
            i += 1
        else:
            print(i)
            break
