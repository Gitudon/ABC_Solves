integers = list(map(int, input().split()))

integers = sorted(integers)
odds = 0
for i in range(3):
    if integers[i] % 2 == 1:
        odds += 1
if odds == 0 or odds == 3:
    print((integers[2] - integers[0]) // 2 + (integers[2] - integers[1]) // 2)
else:
    if odds == 1:
        for i in range(3):
            if integers[i] % 2 == 0:
                integers[i] += 1
        print((integers[2] - integers[0]) // 2 + (integers[2] - integers[1]) // 2 + 1)
    elif odds == 2:
        for i in range(3):
            if integers[i] % 2 == 1:
                integers[i] += 1
        print((integers[2] - integers[0]) // 2 + (integers[2] - integers[1]) // 2 + 1)
