B = int(input())
i = 1
while True:
    power = i**i
    if power == B:
        print(i)
        break
    elif power > B:
        print(-1)
        break
    else:
        i += 1
