A, B, C = map(int, input().split())
a = [0, 0]
if A == 5:
    a[0] += 1
elif A == 7:
    a[1] += 1
if B == 5:
    a[0] += 1
elif B == 7:
    a[1] += 1
if C == 5:
    a[0] += 1
elif C == 7:
    a[1] += 1
if a[0] == 2 and a[1] == 1:
    print("YES")
else:
    print("NO")
