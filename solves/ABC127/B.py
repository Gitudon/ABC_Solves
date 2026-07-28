r, D, x = map(int, input().split())

for i in range(10):
    next = r * x - D
    print(next)
    x = next
