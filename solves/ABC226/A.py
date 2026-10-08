X = float(input())

x = str(X)
x_i, x_d = x.split(".")
i = int(x_i)
d = int(x_d[0])
if d >= 5:
    print(i + 1)
else:
    print(i)
