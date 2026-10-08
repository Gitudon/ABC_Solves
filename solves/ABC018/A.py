a = []
A = int(input())
B = int(input())
C = int(input())
a.append(A)
a.append(B)
a.append(C)
b = sorted(a, reverse=True)
for i in range(3):
    if b[i] == A:
        print(i + 1)
for i in range(3):
    if b[i] == B:
        print(i + 1)
for i in range(3):
    if b[i] == C:
        print(i + 1)
