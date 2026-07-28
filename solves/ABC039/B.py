from math import sqrt

X = int(input())

for i in range(1, int(sqrt(X)) + 1):
    if i**4 == X:
        print(i)
