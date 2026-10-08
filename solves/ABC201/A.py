A1, A2, A3 = map(int, input().split())

a = max(A1, A2, A3)
b = min(A1, A2, A3)
c = A1 + A2 + A3 - a - b

if a - c == c - b:
    print("Yes")
else:
    print("No")
