a = int(input())
b = int(input())

if a < b:
    print(min((10 - b + a), b - a))
elif a > b:
    print(min((10 - a + b), a - b))
