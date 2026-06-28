S = input()
east = 0
west = 0
for s in S:
    if s == "E":
        east += 1
    else:
        west += 1
if east > west:
    print("East")
else:
    print("West")
