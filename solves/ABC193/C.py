N = int(input())

kiroku = set()

a = 2

while True:
    val = a**2
    if val > N:
        break
    while val <= N:
        kiroku.add(val)
        val *= a
    a += 1

print(N - len(kiroku))
