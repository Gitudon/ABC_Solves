H, W = map(int, input().split())
a = []

for i in range(H):
    a_i = input()
    if a_i.count("#") == 0:
        continue
    else:
        a.append(a_i)

for j in range(W):
    flag = True
    for i in range(len(a)):
        if a[i][j] == "#":
            flag = False
            break
    if flag:
        for i in range(len(a)):
            a[i] = a[i][:j] + "-" + a[i][j + 1 :]

for i in range(len(a)):
    print(a[i].replace("-", ""))
