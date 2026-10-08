N = int(input())
a = N % 100
if a != 0:
    print(N // 100 + 1)
else:
    print(N // 100)
