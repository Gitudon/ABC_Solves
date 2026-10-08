N = int(input())
S = input()
a = 0
b = 0
c = N // 2
if N % 2 != 0:
    c += 1
i = 0
while a < c and b < c:
    if S[i] == "T":
        a += 1
    else:
        b += 1
    i += 1
if a == c:
    print("T")
else:
    print("A")
