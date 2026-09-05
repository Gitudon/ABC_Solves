xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

AB = (xB - xA) ** 2 + (yB - yA) ** 2
BC = (xC - xB) ** 2 + (yC - yB) ** 2
CA = (xA - xC) ** 2 + (yA - yC) ** 2

if max(AB, BC, CA) == AB:
    if AB == BC + CA:
        print("Yes")
    else:
        print("No")
elif max(AB, BC, CA) == BC:
    if BC == AB + CA:
        print("Yes")
    else:
        print("No")
else:
    if CA == AB + BC:
        print("Yes")
    else:
        print("No")
