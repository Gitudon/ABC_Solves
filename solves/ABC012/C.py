N = int(input())

kuku_sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        kuku_sum += i * j

atomawashi = kuku_sum - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == atomawashi:
            print(str(i) + " x " + str(j))
