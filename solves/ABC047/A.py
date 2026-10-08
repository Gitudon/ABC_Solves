a, b, c = map(int, input().split())
if a + b + c == 2 * max(a, b, c):
    print("Yes")
else:
    print("No")
