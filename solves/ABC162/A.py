N = int(input())
a = str(N)
b = 0
for i in range(3):
    if a[i] == "7":
        b += 1
if b > 0:
    print("Yes")
else:
    print("No")
