X = int(input())

str_X = str(X)
if str_X[-1] == "0":
    str_X = str_X[:-1]
else:
    if len(str_X) == 1:
        str_X = "0." + str_X
    elif len(str_X) == 2 and str_X[0] == "-":
        str_X = "-0." + str_X[1]
    else:
        str_X = str_X[:-1] + "." + str_X[-1]

if X == 0:
    print(0)
elif X > 0:
    if "." in str_X:
        idx = 0
        while str_X[idx] != ".":
            idx += 1
        print(int(str_X[:idx]))
    else:
        print(str_X)
else:
    if "." in str_X:
        idx = 0
        while str_X[idx] != ".":
            idx += 1
        print(int(str_X[:idx]) - 1)
    else:
        print(str_X)
