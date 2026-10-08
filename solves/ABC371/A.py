SAB, SAC, SBC = map(str, input().split())
if SAB == "<":
    if SAC == "<":
        if SBC == "<":
            print("B")
        else:
            print("C")
    else:
        if SBC == "<":
            pass
        else:
            print("A")
else:
    if SAC == "<":
        if SBC == "<":
            print("A")
        else:
            pass
    else:
        if SBC == "<":
            print("C")
        else:
            print("B")
