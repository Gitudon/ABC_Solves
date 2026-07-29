N = int(input())

div2 = [2**i for i in range(8)]

i = 0
while N >= div2[i]:
    i += 1
print(div2[i - 1])
