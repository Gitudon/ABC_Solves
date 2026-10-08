one = ["N", "W", "S", "E"]
two = ["NE", "NW", "SE", "SW"]

D = input()
if D in one:
    if D == "N":
        print("S")
    elif D == "W":
        print("E")
    elif D == "S":
        print("N")
    else:
        print("W")
else:
    if D == "NE":
        print("SW")
    elif D == "NW":
        print("SE")
    elif D == "SE":
        print("NW")
    else:
        print("NE")
