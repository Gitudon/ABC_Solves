x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
if (x in a and y in a) or (x in b and y in b) or (x == 2 and y == 2):
    print("Yes")
else:
    print("No")
