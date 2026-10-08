n = int(input())
a = str(n)
b = []
for i in range(3):
    b.append(a[i])
for i in range(3):
    if b[i] == "1":
        b[i] = "9"
    elif b[i] == "9":
        b[i] = "1"
c = ""
for i in range(3):
    c += b[i]
print(c)
