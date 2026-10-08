N = int(input())

a = str(1.08 * N)
a_i, a_d = a.split(".")
b = int(a_i)
if b < 206:
    print("Yay!")
elif b == 206:
    print("so-so")
else:
    print(":(")
