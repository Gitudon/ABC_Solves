N = int(input())
P = [0, 0] + list(map(int, input().split()))

a = N
b = 0

while a != 1:
    b += 1
    a = P[a]
print(b)
