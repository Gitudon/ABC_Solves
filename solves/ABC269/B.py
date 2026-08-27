S1 = input()
S2 = input()
S3 = input()
S4 = input()
S5 = input()
S6 = input()
S7 = input()
S8 = input()
S9 = input()
S10 = input()

S = S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8 + S9 + S10
u = 0
a = 0
for h in range(0, 100):
    if S[h] == "#":
        u += 1
for i in range(0, 100):
    if S[i] == ".":
        a += 1
    else:
        break
b = a % 10 + 1
c = a // 10 + 1
e = 0
if c == 1:
    for j in range(0, 10):
        if S1[j] == "#":
            e += 1
elif c == 2:
    for j in range(0, 10):
        if S2[j] == "#":
            e += 1
elif c == 3:
    for j in range(0, 10):
        if S3[j] == "#":
            e += 1
elif c == 4:
    for j in range(0, 10):
        if S4[j] == "#":
            e += 1
elif c == 5:
    for j in range(0, 10):
        if S5[j] == "#":
            e += 1
elif c == 6:
    for j in range(0, 10):
        if S6[j] == "#":
            e += 1
elif c == 7:
    for j in range(0, 10):
        if S7[j] == "#":
            e += 1
elif c == 8:
    for j in range(0, 10):
        if S8[j] == "#":
            e += 1
elif c == 9:
    for j in range(0, 10):
        if S9[j] == "#":
            e += 1
else:
    for j in range(0, 10):
        if S10[j] == "#":
            e += 1
f = b + e - 1
g = u // e
k = c + g - 1

A = c
B = k
C = b
D = f

print(A, B)
print(C, D)
