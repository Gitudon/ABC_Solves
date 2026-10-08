X = float(input())

x = str(X)
x_i, x_d = x.split(".")
i = int(x_i)
d = int(x_d)

if 0 <= d <= 2:
    print(x_i + "-")
elif 3 <= d <= 6:
    print(x_i)
else:
    print(x_i + "+")
