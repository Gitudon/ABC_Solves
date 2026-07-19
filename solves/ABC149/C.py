import sympy

X = int(input())

if X != 2 and X % 2 == 0:
    X += 1
while True:
    if sympy.isprime(X):
        print(X)
        break
    X += 2
