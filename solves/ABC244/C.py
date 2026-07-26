N = int(input())
a = []
for i in range(1, 2 * N + 2):
    a.append(i)
while a != []:
    b = a[0]
    print(b)
    a.remove(b)
    c = int(input())
    a.remove(c)
