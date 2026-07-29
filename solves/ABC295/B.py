R, C = map(int, input().split())
B = [0] * R
for i in range(R):
    B[i] = input()
D = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = []
c = []
for i in range(R):
    for j in range(C):
        if B[i][j] != "." and B[i][j] != "#":
            b.append([i, j])
            c.append(int(B[i][j]))
if len(b) == 0:
    for i in range(R):
        print(B[i])
    exit()
for i in range(R):
    d = ""
    e = [0] * C
    for j in range(C):
        e[j] = B[i][j]
        for k in range(len(c)):
            if abs(j - b[k][1]) + abs(i - b[k][0]) <= c[k]:
                e[j] = "."
        if e[j] in D:
            e[j] = "."
        d += e[j]
    print(d)
