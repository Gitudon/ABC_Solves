H = int(input())
i = 0
high = 0
high += 2**i
i += 1
while True:
    if high > H:
        print(i)
        break
    high += 2**i
    i += 1
