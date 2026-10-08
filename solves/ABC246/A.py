x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x3 and y1 == y2:
    x = x2
    y = y3
elif x1 == x2 and y1 == y3:
    x = x3
    y = y2
elif x2 == x3 and y1 == y2:
    x = x1
    y = y3
elif x2 == x3 and y1 == y3:
    x = x1
    y = y2
elif x1 == x3 and y2 == y3:
    x = x2
    y = y1
elif x1 == x2 and y2 == y3:
    x = x3
    y = y1
print(x, y)
