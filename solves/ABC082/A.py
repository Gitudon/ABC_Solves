a, b = map(int, input().split())
x = (a + b) // 2
if (a + b) % 2 == 1:
    x += 1
print(x)
