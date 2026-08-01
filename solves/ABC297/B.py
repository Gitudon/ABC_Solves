S = input()
N = len(S)
x = 0
while S[x] != "B":
    x += 1
y = x + 1
while S[y] != "B":
    y += 1
if (x % 2) == (y % 2):
    print("No")
    exit()
x = 0
while S[x] != "R":
    x += 1
y = x + 1
while S[y] != "R":
    y += 1
z = 0
while S[z] != "K":
    z += 1
if x < z < y:
    print("Yes")
else:
    print("No")
