a, b, c = map(int, input().split())

triangle = set([a, b, c])
if len(triangle) <= 2:
    print("Yes")
else:
    print("No")
