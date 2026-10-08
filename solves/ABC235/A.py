abc = int(input())
t = str(abc)

a = int(t[0])
b = int(t[1])
c = int(t[2])

d = a * 100 + b * 10 + c
e = b * 100 + c * 10 + a
f = c * 100 + a * 10 + b

print(d + e + f)
