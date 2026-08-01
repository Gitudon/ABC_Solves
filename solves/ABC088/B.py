N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0
a = sorted(a, reverse=True)
i = 0
while True:
    if i >= len(a):
        break
    Alice += a[i]
    i += 1
    if i >= len(a):
        break
    Bob += a[i]
    i += 1
print(Alice - Bob)
